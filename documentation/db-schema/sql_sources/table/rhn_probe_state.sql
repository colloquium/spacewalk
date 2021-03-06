-- created by Oraschemadoc Tue Nov  2 08:32:48 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."RHN_PROBE_STATE" 
   (	"PROBE_ID" NUMBER(12,0) NOT NULL ENABLE, 
	"SCOUT_ID" NUMBER(12,0) NOT NULL ENABLE, 
	"STATE" VARCHAR2(20), 
	"OUTPUT" VARCHAR2(4000), 
	"LAST_CHECK" DATE, 
	 CONSTRAINT "PRBST_PROBE_ID_SCOUT_ID_PK" PRIMARY KEY ("PROBE_ID", "SCOUT_ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS"  ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" ENABLE ROW MOVEMENT 
 
/
