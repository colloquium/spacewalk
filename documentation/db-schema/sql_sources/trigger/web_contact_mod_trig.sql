-- created by Oraschemadoc Tue Nov  2 08:33:18 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE OR REPLACE TRIGGER "SPACEWALK"."WEB_CONTACT_MOD_TRIG" 
before insert or update on web_contact
for each row
begin
        :new.modified := sysdate;
        :new.login_uc := UPPER(:new.login);
        IF :new.password <> :old.password THEN
                :new.old_password := :old.password;
        END IF;
end;
ALTER TRIGGER "SPACEWALK"."WEB_CONTACT_MOD_TRIG" ENABLE
 
/
