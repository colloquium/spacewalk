-- oracle equivalent source sha1 7c7c4cdfdddbb19afed68b330cd9094bfc39479d
-- retrieved from ./1241102873/cdc6d42049bf86fbc9f1d3a5c54275eeacbd641d/schema/spacewalk/oracle/triggers/rhnPackageSyncBlacklist.sql
create or replace function rhn_packagesyncbl_mod_trig_fun() returns trigger as
$$
begin
	new.modified := current_timestamp;
       
	return new;
end;
$$ language plpgsql;

create trigger
rhn_packagesyncbl_mod_trig
before insert or update on rhnPackageSyncBlacklist
for each row
execute procedure rhn_packagesyncbl_mod_trig_fun();

