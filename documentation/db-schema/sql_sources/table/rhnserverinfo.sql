-- created by Oraschemadoc Tue Nov  2 08:32:40 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."RHNSERVERINFO" 
   (	"SERVER_ID" NUMBER NOT NULL ENABLE, 
	"CHECKIN" DATE DEFAULT (sysdate), 
	"CHECKIN_COUNTER" NUMBER DEFAULT (0), 
	 CONSTRAINT "RHN_SERVER_INFO_SID_FK" FOREIGN KEY ("SERVER_ID")
	  REFERENCES "SPACEWALK"."RHNSERVER" ("ID") ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" ENABLE ROW MOVEMENT 
 
/
