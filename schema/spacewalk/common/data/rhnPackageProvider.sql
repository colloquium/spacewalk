--
-- Copyright (c) 2008--2010 Red Hat, Inc.
--
-- This software is licensed to you under the GNU General Public License,
-- version 2 (GPLv2). There is NO WARRANTY for this software, express or
-- implied, including the implied warranties of MERCHANTABILITY or FITNESS
-- FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
-- along with this software; if not, see
-- http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
-- 
-- Red Hat trademarks are not licensed under GPLv2. No permission is
-- granted to use or replicate Red Hat trademarks that are incorporated
-- in this software or its documentation. 
--
--

insert into rhnPackageProvider (id, name) values
(sequence_nextval('rhn_package_provider_id_seq'), 'Red Hat Inc.' );
insert into rhnPackageProvider (id, name) values
(sequence_nextval('rhn_package_provider_id_seq'), 'Fedora' );
insert into rhnPackageProvider (id, name) values
(sequence_nextval('rhn_package_provider_id_seq'), 'CentOS' );
insert into rhnPackageProvider (id, name) values
(sequence_nextval('rhn_package_provider_id_seq'), 'Scientific Linux' );
insert into rhnPackageProvider (id, name) values
(sequence_nextval('rhn_package_provider_id_seq'), 'Suse' );
insert into rhnPackageProvider (id, name) values
(sequence_nextval('rhn_package_provider_id_seq'), 'Oracle Inc.' );
insert into rhnPackageProvider (id, name) values
(sequence_nextval('rhn_package_provider_id_seq'), 'Spacewalk' );




commit;

--
-- Revision 1.1  2008/07/02 23:42:28  jsherrill
-- Sequence; data to populate stuff
--

