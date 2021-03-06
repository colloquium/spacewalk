-- created by Oraschemadoc Tue Nov  2 08:32:47 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE TABLE "SPACEWALK"."RHN_LL_NETSAINT" 
   (	"NETSAINT_ID" NUMBER NOT NULL ENABLE, 
	"CITY" VARCHAR2(255), 
	 CONSTRAINT "RHN_LLNTS_SAT_CLUSTER_IDFK" FOREIGN KEY ("NETSAINT_ID")
	  REFERENCES "SPACEWALK"."RHN_SAT_CLUSTER" ("RECID") ENABLE
   ) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)
  TABLESPACE "USERS" ENABLE ROW MOVEMENT 
 
/
