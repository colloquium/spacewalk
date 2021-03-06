-- created by Oraschemadoc Tue Nov  2 08:32:46 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."RHN_CONTACT_METHODS" 
   (	"RECID" NUMBER NOT NULL ENABLE, 
	"METHOD_NAME" VARCHAR2(20), 
	"CONTACT_ID" NUMBER(12,0) NOT NULL ENABLE, 
	"SCHEDULE_ID" NUMBER(12,0), 
	"METHOD_TYPE_ID" NUMBER(12,0) NOT NULL ENABLE, 
	"PAGER_TYPE_ID" NUMBER(12,0), 
	"PAGER_PIN" VARCHAR2(20), 
	"PAGER_EMAIL" VARCHAR2(50), 
	"PAGER_MAX_MESSAGE_LENGTH" NUMBER(6,0), 
	"PAGER_SPLIT_LONG_MESSAGES" CHAR(1), 
	"EMAIL_ADDRESS" VARCHAR2(50), 
	"EMAIL_REPLY_TO" VARCHAR2(50), 
	"LAST_UPDATE_USER" VARCHAR2(40), 
	"LAST_UPDATE_DATE" DATE, 
	"SNMP_HOST" VARCHAR2(255), 
	"SNMP_PORT" NUMBER(5,0), 
	"NOTIFICATION_FORMAT_ID" NUMBER(12,0) DEFAULT (4) NOT NULL ENABLE, 
	"SENDER_SAT_CLUSTER_ID" NUMBER(12,0), 
	 CONSTRAINT "RHN_CMETH_RECID_NOTZERO" CHECK (recid > 0) ENABLE, 
	 CONSTRAINT "RHN_CMETH_PGR_LENGTH_LIMIT" CHECK (pager_max_message_length between 10 and 1920) ENABLE, 
	 CONSTRAINT "RHN_CMETH_RECID_PK" PRIMARY KEY ("RECID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS"  ENABLE, 
	 CONSTRAINT "RHN_CMETH_CONTACT_ID_FK" FOREIGN KEY ("CONTACT_ID")
	  REFERENCES "SPACEWALK"."WEB_CONTACT" ("ID") ENABLE, 
	 CONSTRAINT "RHN_CMETH_METHOD_TYPE_ID_FK" FOREIGN KEY ("METHOD_TYPE_ID")
	  REFERENCES "SPACEWALK"."RHN_METHOD_TYPES" ("RECID") ENABLE, 
	 CONSTRAINT "RHN_CMETH_PAGER_TYPE_ID_FK" FOREIGN KEY ("PAGER_TYPE_ID")
	  REFERENCES "SPACEWALK"."RHN_PAGER_TYPES" ("RECID") ENABLE, 
	 CONSTRAINT "RHN_CMETH_SENDER_SAT_CLUS_FK" FOREIGN KEY ("SENDER_SAT_CLUSTER_ID")
	  REFERENCES "SPACEWALK"."RHN_SAT_CLUSTER" ("RECID") ENABLE, 
	 CONSTRAINT "RHN_CMETH_SCHEDULE_ID_FK" FOREIGN KEY ("SCHEDULE_ID")
	  REFERENCES "SPACEWALK"."RHN_SCHEDULES" ("RECID") ENABLE, 
	 CONSTRAINT "RHN_CMETH_NTFMT_ID_FK" FOREIGN KEY ("NOTIFICATION_FORMAT_ID")
	  REFERENCES "SPACEWALK"."RHN_NOTIFICATION_FORMATS" ("RECID") ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" ENABLE ROW MOVEMENT 
 
/
