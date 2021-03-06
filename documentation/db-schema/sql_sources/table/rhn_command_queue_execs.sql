-- created by Oraschemadoc Tue Nov  2 08:32:46 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."RHN_COMMAND_QUEUE_EXECS" 
   (	"INSTANCE_ID" NUMBER(12,0) NOT NULL ENABLE, 
	"NETSAINT_ID" NUMBER(12,0) NOT NULL ENABLE, 
	"DATE_ACCEPTED" DATE, 
	"DATE_EXECUTED" DATE, 
	"EXIT_STATUS" NUMBER(5,0), 
	"EXECUTION_TIME" NUMBER(10,6), 
	"STDOUT" VARCHAR2(4000), 
	"STDERR" VARCHAR2(4000), 
	"LAST_UPDATE_DATE" DATE, 
	"TARGET_TYPE" VARCHAR2(10) NOT NULL ENABLE, 
	 CONSTRAINT "RHN_CQEXE_INST_ID_NSAINT_PK" PRIMARY KEY ("INSTANCE_ID", "NETSAINT_ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS"  ENABLE, 
	 CONSTRAINT "RHN_CQEXE_CQINS_INST_ID_FK" FOREIGN KEY ("INSTANCE_ID")
	  REFERENCES "SPACEWALK"."RHN_COMMAND_QUEUE_INSTANCES" ("RECID") ON DELETE CASCADE ENABLE, 
	 CONSTRAINT "RHN_CQEXE_SATCL_NSAINT_ID_FK" FOREIGN KEY ("NETSAINT_ID", "TARGET_TYPE")
	  REFERENCES "SPACEWALK"."RHN_COMMAND_TARGET" ("RECID", "TARGET_TYPE") ON DELETE CASCADE ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" ENABLE ROW MOVEMENT 
 
/
