#
# Copyright (c) 2008--2010 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.
#
#
#
# Database driver for PostgreSQL
#

import sys
import re
import psycopg2
import hashlib

import sql_base
from spacewalk.server import rhnSQL
from spacewalk.server.rhnSQL import sql_types

from spacewalk.common import log_debug, log_error, UserDictCase
from const import POSTGRESQL

def convert_named_query_params(query):
    """ 
    Convert a query with named parameters (i.e. :id, :name, etc) into one
    that uses %(id)s, %(name)s parameters instead.

    python-psycopg2 requires parameters to be in this form, so to keep our
    existing queries intact we'll convert them when provided to the 
    postgresql driver.

    RETURNS: tuple with:
        - the new query with parameters replaced
        - hash of each named parameter to an ordered list of the positions
          where it was used.
        - number of arguments found and replaced
    """
    log_debug(6, "Converting query for PostgreSQL: %s" % query)
    new_query = re.sub(r'(\W):(\w+)', r'\1%(\2)s', query.replace('%', '%%'))
    log_debug(6, "New query: %s" % new_query)
    return new_query


class Function(sql_base.Procedure):
    """
    Function implementation for PostgreSQL. As there is no support in the Python
    driver we use direct SQL.
    """

    def __init__(self, name, cursor, ret_type):
        sql_base.Procedure.__init__(self, name, cursor)
        self.ret_type = ret_type

    def __call__(self, *args):
        log_debug(2, self.name, args)

        # Buildup a string for the positional arguments to the procedure:
        positional_args = ""
        i = 1
        for arg in args:
            if len(positional_args) == 0:
                positional_args = "%s"
            else:
                positional_args = positional_args + ", %s"
            i += 1
        query = "SELECT %s(%s)" % (self.name, positional_args)

        log_debug(2, query, args)
        ret = self.cursor.execute(query, args)
        if self.ret_type == None:
            return ret
        else:
            return self.cursor.fetchone()[0]


class Procedure(Function):
    """
    PostgreSQL functions are somewhat different than stored procedures in
    other databases. As a result the python-pgsql does not even implement
    the Python DBI API callproc method.

    To workaround this and keep rhnSQL database independent, we'll translate
    any incoming requests to call a procedure into a PostgreSQL query.
    """

    def __init__(self, name, cursor):
        Function.__init__(self, name, cursor, None)
        self.ret_type = None

    def __call__(self, *args):
        result = Function.__call__(self, *args)
        # we do not expect any result (this is procedure)
        #if not (type(result) == 'tuple' and result[0] == ''):
            #raise rhnSQL.SQLError("Unexpected result returned by procedure %s: %s" % (self.name, str(result)))

def decimal2intfloat(dec, cursor):
    "Convert a Decimal to an int or a float with no loss of information."
    "The dec is passed in as str (not Decimal) so we cannot check its type."
    if dec is None:
        return None
    "If we can convert to int without loss of information, return int, float otherwise."
    try:
        if float(dec) == float(int(dec)):
            return int(dec)
        return float(dec)
    except ValueError:
        return float(dec)

class Database(sql_base.Database):
    """ Class for PostgreSQL database operations. """

    def __init__(self, host=None, port=None, username=None,
                 password=None, database=None):

        self.host = host
        self.port = port

        # pgsql module prefers -1 for an unspecified port:
        if not port:
            self.port = -1

        self.username = username
        self.password = password
        self.database = database

        # Minimum requirements to connect to a PostgreSQL db:
        if not (self.username and self.database):
            raise AttributeError, "PostgreSQL requires at least a user and database name."

        sql_base.Database.__init__(self, host, port, username, password, database)

    def connect(self, reconnect=1):
        try:
            if self.host is None:
                self.dbh = psycopg2.connect(database=self.database, user=self.username,
                                            password=self.password)
            else:
                self.dbh = psycopg2.connect(database=self.database, user=self.username,
                                            password=self.password, host=self.host, port=self.port)
            # convert all DECIMAL types to float (let Python to choose one)
            DEC2INTFLOAT = psycopg2.extensions.new_type(psycopg2._psycopg.DECIMAL.values,
                                                            'DEC2INTFLOAT', decimal2intfloat)
            psycopg2.extensions.register_type(DEC2INTFLOAT)
        except Exception, e:
            if reconnect:
                # Try one more time:
                return self.connect(reconnect=0)

            # Failed reconnect, time to error out:
            raise apply(sql_base.SQLConnectError,
                        [self.database, e.pgcode, e.pgerror, "Attempting Re-Connect to the database failed",])

    def is_connected_to(self, backend, host, port, username, password,
                        database):
        adjusted_port = -1
        if port:
            adjusted_port = port
        return (backend == POSTGRESQL) and (self.host == host) and \
               (self.port == adjusted_port) and (self.username == username) \
               and (self.password == password) and (self.database == database)

    def check_connection(self):
        try:
            c = self.prepare("select 1")
            c.execute()
        except: # try to reconnect, that one MUST WORK always
            log_error("DATABASE CONNECTION TO '%s' LOST" % self.database,
                      "Exception information: %s" % sys.exc_info()[1])
            self.connect() # only allow one try

    def prepare(self, sql, force=0, params=None):
        if params != None:              # support for anonymour plpgsql
            sql = re.sub(r'/\*pg_cs\*/\s*cursor', '', sql)
            sql = re.sub(r'/\*pg (.+?)\*/', '\g<1>', sql)
            sql = re.sub(r':(\w+)', '\g<1>', sql)
            s = hashlib.new('sha1')
            s.update(sql)
            sha1 = s.hexdigest()
            c = self.prepare("select 1 from information_schema.routines where routine_name = 'rhn_asdf_' || :sha1");
            c.execute(sha1=sha1)
            if not c.fetchone():
                c = self.prepare("create function rhn_asdf_%s (%s) returns void as $x%s$%s$x%s$ language plpgsql" % ( sha1, ','.join(params), sha1, sql, sha1 ))
                c.execute()
            qparams = ','.join(map(lambda x: re.sub(r'^(\w+).*', ':\g<1>', x), params))
            sql = "select rhn_asdf_%s(%s)" % (sha1, qparams)
        return Cursor(dbh=self.dbh, sql=sql, force=force)

    def transaction(self, name):
        if not name:
            raise rhnException("Can not set a transaction without a name", name)
        c = self.prepare("savepoint %s" % name)
        return c.execute()

    def commit(self):
        self.dbh.commit()

    def rollback(self, name=None):
        if name:
            c = self.prepare("rollback to %s" % name)
            return c.execute()
        else:
            return self.dbh.rollback()

    def procedure(self, name):
        c = self.dbh.cursor()
        # Pass the cursor in so we can close it after execute()
        return Procedure(name, c)

    def _function(self, name, ret_type):
        c = self.dbh.cursor()
        return Function(name, c, ret_type)

    def cursor(self):
        return Cursor(dbh=self.dbh)

    def _read_lob(self, lob):
        return str(lob)



class Cursor(sql_base.Cursor):
    """ PostgreSQL specific wrapper over sql_base.Cursor. """

    def __init__(self, dbh=None, sql=None, force=None):

        sql_base.Cursor.__init__(self, dbh, sql, force)

        # Accept Oracle style named query params, but convert for python-pgsql
        # under the hood:
        temp_sql = ""
        if self.sql is not None:
            temp_sql = self.sql
        self.sql = convert_named_query_params(temp_sql)

    def _prepare_sql(self):
        cursor = self.dbh.cursor()
        return cursor

    def _execute_wrapper(self, function, *p, **kw):
        params =  ','.join(["%s: %s" % (key, value) for key, value \
                            in kw.items()])
        log_debug(5, "Executing SQL: \"%s\" with bind params: {%s}"
                  % (self.sql, params))
        if self.sql is None:
            raise rhnException("Cannot execute empty cursor")

        try:
            retval = apply(function, p, kw)
        except psycopg2.ProgrammingError, e:
            # TODO: Constructor for this exception expects a first arg of db,
            # and yet the Oracle driver passes it an errno? Suspect it's not
            # even used.
            raise rhnSQL.SQLStatementPrepareError(0, str(e), self.sql)
        return retval

    def _execute_(self, args, kwargs):
        """
        PostgreSQL specific execution of the query.
        """
        params = UserDictCase(kwargs)
        self._real_cursor.execute(self.sql, params)
        self.description = self._real_cursor.description
        return self._real_cursor.rowcount

    def _executemany(self, *args, **kwargs):
        if not kwargs:
            return 0

        params = UserDictCase(kwargs)

        # First break all the incoming keyword arg lists into individual
        # hashes:
        all_kwargs = []
        for key in params.keys():
            if len(all_kwargs) < len(params[key]):
                for i in range(len(params[key])):
                    all_kwargs.append({})

            i = 0
            for val in params[key]:
                all_kwargs[i][key] = val
                i = i + 1

        self._real_cursor.executemany(self.sql, all_kwargs)
        self.description = self._real_cursor.description
        rowcount = self._real_cursor.rowcount
        return rowcount

    def update_blob(self, table_name, column_name, where_clause, data, 
                    **kwargs):
        """ 
        PostgreSQL uses bytea columns instead of blobs. Nothing special
        needs to be done to insert text into one.
        """
        # NOTE: Injecting a :column_name parameter here
        sql = "UPDATE %s SET %s = :%s %s" % (table_name, column_name,
                                             column_name, where_clause)
        c = rhnSQL.prepare(sql)
        kwargs[column_name] = data
        apply(c.execute, (), kwargs)
