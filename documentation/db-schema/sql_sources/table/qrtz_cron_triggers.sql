-- created by Oraschemadoc Tue Nov  2 08:32:25 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."QRTZ_CRON_TRIGGERS" 
   (	"TRIGGER_NAME" VARCHAR2(200) NOT NULL ENABLE, 
	"TRIGGER_GROUP" VARCHAR2(200) NOT NULL ENABLE, 
	"CRON_EXPRESSION" VARCHAR2(120) NOT NULL ENABLE, 
	"TIME_ZONE_ID" VARCHAR2(80), 
	 PRIMARY KEY ("TRIGGER_NAME", "TRIGGER_GROUP")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS"  ENABLE, 
	 FOREIGN KEY ("TRIGGER_NAME", "TRIGGER_GROUP")
	  REFERENCES "SPACEWALK"."QRTZ_TRIGGERS" ("TRIGGER_NAME", "TRIGGER_GROUP") ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" 
 
/