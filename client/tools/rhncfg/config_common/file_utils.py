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

import os
import os.path
import time
import tempfile
import base64
try:
    from selinux import lgetfilecon
except:
    # on rhel4 we do not support selinux
    def lgetfilecon(path):
        return [0, '']

from config_common import utils

class FileProcessor:
    file_struct_fields = {
        'file_contents'     : None,
        'delim_start'       : None,
        'delim_end'         : None,
    }
    def __init__(self):
        pass

    def process(self, file_struct, directory=None, strict_ownership=1):
        # Older servers will not return directories; if filetype is missing,
        # assume file
    	if file_struct.get('filetype') == 'directory':
                return directory, []

        if file_struct.get('filetype') == 'symlink':
            if not file_struct.has_key('symlink'):
                raise Exception, "Missing key symlink"

            (dirname, filename) = os.path.split(file_struct['path'])
            temppath = ".rhn-cfg-tmp_%s_%s_%.8f" % (filename, os.getpid(), time.time())
            os.symlink(file_struct['symlink'], temppath)
            return temppath, []

        for k in self.file_struct_fields.keys():
            if not file_struct.has_key(k):
                # XXX
                raise Exception, "Missing key %s" % k

        encoding = ''

        if file_struct.has_key('encoding'):
            encoding = file_struct['encoding']
        
        contents = file_struct['file_contents']

        if contents and (encoding == 'base64'):
            contents = base64.decodestring(contents)
        
        delim_start = file_struct['delim_start']
        delim_end = file_struct['delim_end']

        fh = None        

        (fullpath, dirs_created, fh) = maketemp(prefix=".rhn-cfg-tmp",
                                  directory=directory)

        try:
            fh.write(contents)
        except Exception:
            if fh:
                fh.close()  # don't leak fds...
            raise
        else:
            fh.close()

        return fullpath, dirs_created


    def diff(self, file_struct):
        self._validate_struct(file_struct)

        temp_file, temp_dirs = self.process(file_struct)
        path = file_struct['path']
        sectx_result = ''
        result = ''

        cur_sectx = lgetfilecon(path)[1]
        if cur_sectx == None:
            cur_sectx = ''
        if file_struct.has_key('selinux_ctx') and file_struct['selinux_ctx']:
            if cur_sectx != file_struct['selinux_ctx']:
                sectx_result = "SELinux contexts differ:  actual: [%s], expected: [%s]\n" % (cur_sectx, file_struct['selinux_ctx'])

        if file_struct['filetype'] == 'symlink':
            try:
                curlink = os.path.abspath(os.readlink(path))
                newlink = os.path.abspath(os.readlink(temp_file))
                if curlink == newlink:
                    result = ''
                else:
                    result = "Link targets differ for [%s]: actual: [%s], expected: [%s]\n" % (path, curlink, newlink)
            except OSError, e:
                if e.errno == 22:
                    result = "Deployed symlink is no longer a symlink!"
                else:
                    raise e
        else:
            pipe = os.popen("/usr/bin/diff -u %s %s" % (path, temp_file))
            result = pipe.read()

        os.unlink(temp_file)
        return sectx_result + result
        
    def _validate_struct(self, file_struct):
        for k in self.file_struct_fields.keys():
            if not file_struct.has_key(k):
                # XXX
                raise Exception, "Missing key %s" % k
        

def maketemp(prefix=None, directory=None):
    """Creates a temporary file (guaranteed to be new), using the
       specified prefix.

       Returns the filename and an open stream
    """
    if not directory:
        directory = tempfile.gettempdir()

    dirs_created = None
    if not os.path.exists(directory):
        dirs_created = utils.mkdir_p(directory)
    
    if not prefix:
    # Create the file in /tmp by default
        prefix = 'rhncfg-tempfile'

    file_prefix = "%s-%s-" % (prefix, os.getpid())
    (fd, filename) = tempfile.mkstemp(prefix=file_prefix, dir=directory)

    return filename, dirs_created, os.fdopen(fd, "w+")

