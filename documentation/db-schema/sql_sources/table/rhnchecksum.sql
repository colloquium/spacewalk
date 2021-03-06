-- created by Oraschemadoc Tue Nov  2 08:32:29 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."RHNCHECKSUM" 
   (	"ID" NUMBER NOT NULL ENABLE, 
	"CHECKSUM_TYPE_ID" NUMBER NOT NULL ENABLE, 
	"CHECKSUM" VARCHAR2(128) NOT NULL ENABLE, 
	 CONSTRAINT "RHNCHECKSUM_PK" PRIMARY KEY ("ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS"  ENABLE, 
	 CONSTRAINT "RHNCHECKSUM_CHSUM_UQ" UNIQUE ("CHECKSUM", "CHECKSUM_TYPE_ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS"  ENABLE, 
	 CONSTRAINT "RHNCHECKSUM_TYPEID_FK" FOREIGN KEY ("CHECKSUM_TYPE_ID")
	  REFERENCES "SPACEWALK"."RHNCHECKSUMTYPE" ("ID") ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" ENABLE ROW MOVEMENT 
 
/
