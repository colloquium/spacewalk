-- oracle equivalent source sha1 60702e902f24095fb5ba504e4532022b43309918
-- retrieved from ./1241132947/9984c41fb98d15becf3c29432c19cd7a266dece4/schema/spacewalk/oracle/triggers/rhnKickstartSession.sql
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


create or replace function rhn_ks_session_mod_trig_fun() returns trigger
as
$$
begin
        new.modified := current_timestamp;

        return new;
end;
$$ language plpgsql;

create trigger 
rhn_ks_session_mod_trig
before insert or update on rhnKickstartSession
for each row
execute procedure rhn_ks_session_mod_trig_fun();


create or replace function rhn_ks_session_history_trigger_fun() returns trigger
as
$$
begin
        if tg_op ='INSERT' then
                insert into rhnKickstartSessionHistory (
                                id, kickstart_session_id, action_id, state_id
                        ) values (
                                nextval('rhn_ks_sessionhist_id_seq'),
                                new.id,
                                new.action_id,
                                new.state_id
                        );
        end if;
        if tg_op ='UPDATE' then
          if new.state_id is distinct from old.state_id then
                insert into rhnKickstartSessionHistory (
                                id, kickstart_session_id, action_id, state_id
                        ) values (
                                nextval('rhn_ks_sessionhist_id_seq'),
                                new.id,
                                new.action_id,
                                new.state_id
                        );
          end if;
        end if;
end;
$$ language plpgsql;




create trigger
rhn_ks_session_history_trigger
after insert or update on rhnKickstartSession
for each row
execute procedure rhn_ks_session_history_trigger_fun();


