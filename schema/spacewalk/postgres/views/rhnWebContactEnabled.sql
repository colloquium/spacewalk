-- oracle equivalent source sha1 fb808d26c21beb950018ef40af165b6921f382f0
-- retrieved from ./1235066623/21f37df477f4c9a372b85916798c9ad2ff734e58/schema/spacewalk/rhnsat/views/rhnWebContactEnabled.sql
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

create or replace view
rhnWebContactEnabled
as
select
   wcon.id,
   wcon.org_id,
   wcon.login,
   wcon.login_uc,
   wcon.password,
   wcon.old_password,
   wcon.oracle_contact_id,
   wcon.created,
   wcon.modified,
   wcon.ignore_flag
from
   web_contact wcon
except
select
   wcd.id,
   wcd.org_id,
   wcd.login,
   wcd.login_uc,
   wcd.password,
   wcd.old_password,
   wcd.oracle_contact_id,
   wcd.created,
   wcd.modified,
   wcd.ignore_flag
from
   rhnWebContactDisabled wcd;

