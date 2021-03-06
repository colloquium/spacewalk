-- oracle equivalent source sha1 c99c0b72a32681747aae82f00b243fd5af149a3b
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


create or replace function rhn_confrevision_mod_trig_func() returns trigger as
$$
begin
	new.modified := current_timestamp;
	return new;
end;
$$ language plpgsql;


create trigger
rhn_confrevision_mod_trig
before insert or update on rhnConfigRevision
for each row
execute procedure rhn_confrevision_mod_trig_func();


-- right now we're not doing accounting for rhnConfigRevision updates.
-- we shouldn't ever _do_ updates, but right now the perms exist.

create or replace function rhn_confrevision_acct_trig_fun() returns trigger
as
$$
declare
        org_id numeric;
        available numeric;
        added numeric;
begin
        -- find the current amount of quota available
        select  cc.org_id,
                        oq.total + oq.bonus - oq.used,
                        content.file_size
        into    org_id, available, added
        from    rhnConfigContent        content,
                        rhnOrgQuota                     oq,
                        rhnConfigChannel        cc,
                        rhnConfigFile           cf
        where   cf.id = new.config_file_id
                        and cf.config_channel_id = cc.org_id
                        and cc.org_id = oq.org_id
                        and new.config_file_type_id = (select id from rhnConfigFileType where label='file')
                        and new.config_content_id = content.id;

        if added > available then
                perform rhn_exception.raise_exception('not_enough_quota');
        end if;

        return new;
end;
$$
language plpgsql;

create trigger
rhn_confrevision_acct_trig
after insert on rhnConfigRevision
for each row
execute procedure rhn_confrevision_acct_trig_fun();



create or replace function rhn_confrevision_del_trig_fun() returns trigger 
as
$$
declare
         snapshot_curs_id	numeric;
begin
        for snapshot_curs_id in
                select  snapshot_id
                from    rhnSnapshotConfigRevision
                where   config_revision_id = old.id
	loop
		update rhnSnapshot
                        set invalid = lookup_snapshot_invalid_reason('cr_removed')
                        where id = snapshot_curs_id;
                delete from rhnSnapshotConfigRevision
                        where snapshot_id = snapshot_curs_id
                                and config_revision_id = old.id;
                               
	end loop;
	
        return old;
end;
$$ language plpgsql;


create trigger
rhn_confrevision_del_trig
before delete on rhnConfigRevision
for each row
execute procedure rhn_confrevision_del_trig_fun();
