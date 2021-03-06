-- created by Oraschemadoc Tue Nov  2 08:32:46 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."RHN_CONFIG_PARAMETER" 
   (	"GROUP_NAME" VARCHAR2(255) NOT NULL ENABLE, 
	"NAME" VARCHAR2(255) NOT NULL ENABLE, 
	"VALUE" VARCHAR2(255), 
	"SECURITY_TYPE" VARCHAR2(255) NOT NULL ENABLE, 
	"LAST_UPDATE_USER" VARCHAR2(40), 
	"LAST_UPDATE_DATE" DATE, 
	 CONSTRAINT "RHN_CONFP_GROUP_NAME_NAME_PK" PRIMARY KEY ("GROUP_NAME", "NAME")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS"  ENABLE, 
	 CONSTRAINT "RHN_CONFP_GRPNM_GROUP_NAME_FK" FOREIGN KEY ("GROUP_NAME")
	  REFERENCES "SPACEWALK"."RHN_CONFIG_GROUP" ("NAME") ENABLE, 
	 CONSTRAINT "RHN_CONFP_SCRTY_SEC_TYPE_FK" FOREIGN KEY ("SECURITY_TYPE")
	  REFERENCES "SPACEWALK"."RHN_CONFIG_SECURITY_TYPE" ("NAME") ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" ENABLE ROW MOVEMENT 
 
/
