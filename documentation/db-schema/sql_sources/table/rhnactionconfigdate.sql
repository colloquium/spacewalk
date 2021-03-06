-- created by Oraschemadoc Tue Nov  2 08:32:25 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."RHNACTIONCONFIGDATE" 
   (	"ACTION_ID" NUMBER NOT NULL ENABLE, 
	"START_DATE" DATE NOT NULL ENABLE, 
	"END_DATE" DATE, 
	"IMPORT_CONTENTS" CHAR(1) NOT NULL ENABLE, 
	"CREATED" DATE DEFAULT (sysdate) NOT NULL ENABLE, 
	"MODIFIED" DATE DEFAULT (sysdate) NOT NULL ENABLE, 
	 CONSTRAINT "RHN_ACTIONCD_FILE_IC_CK" CHECK (import_contents in ('Y','N')) ENABLE, 
	 CONSTRAINT "RHN_ACTIONCD_AID_FK" FOREIGN KEY ("ACTION_ID")
	  REFERENCES "SPACEWALK"."RHNACTION" ("ID") ON DELETE CASCADE ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" ENABLE ROW MOVEMENT 
 
/
