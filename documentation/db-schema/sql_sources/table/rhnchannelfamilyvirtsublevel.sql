-- created by Oraschemadoc Tue Nov  2 08:32:28 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."RHNCHANNELFAMILYVIRTSUBLEVEL" 
   (	"CHANNEL_FAMILY_ID" NUMBER NOT NULL ENABLE, 
	"VIRT_SUB_LEVEL_ID" NUMBER NOT NULL ENABLE, 
	"CREATED" DATE DEFAULT (sysdate) NOT NULL ENABLE, 
	"MODIFIED" DATE DEFAULT (sysdate) NOT NULL ENABLE, 
	 CONSTRAINT "RHN_CFVSL_CFID_FK" FOREIGN KEY ("CHANNEL_FAMILY_ID")
	  REFERENCES "SPACEWALK"."RHNCHANNELFAMILY" ("ID") ENABLE, 
	 CONSTRAINT "RHN_CFVSL_VSLID_FK" FOREIGN KEY ("VIRT_SUB_LEVEL_ID")
	  REFERENCES "SPACEWALK"."RHNVIRTSUBLEVEL" ("ID") ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" ENABLE ROW MOVEMENT 
 
/
