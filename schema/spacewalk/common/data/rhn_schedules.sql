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
--
--
-- 
--

--data for rhn_schedules (uses sequence)
--only include the 24 x 7 schedule

insert into rhn_schedules(recid,schedule_type_id,description,last_update_user,
last_update_date,customer_id) 
    values ( sequence_nextval('rhn_schedules_recid_seq'),1,'24x7','system',current_timestamp,NULL);
commit;

--
--Revision 1.4  2004/06/17 20:48:59  kja
--bugzilla 124970 -- _data is in for 350.
--
--Revision 1.3  2004/05/29 21:51:49  pjones
--bugzilla: none -- _data is not for 340, so says kja.
--
--Revision 1.2  2004/05/04 20:03:38  kja
--Added commits.
--
--Revision 1.1  2004/04/22 19:05:45  kja
--Added the 24 x 7 schedule data.  Corrected logic for skipping sequence numbers
--in rhn_notification_formats_data.sql and rhn_strategies_data.sql.
--
