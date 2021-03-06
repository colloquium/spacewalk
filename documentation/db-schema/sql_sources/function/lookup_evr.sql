-- created by Oraschemadoc Tue Nov  2 08:33:19 2010
-- visit http://www.yarpen.cz/oraschemadoc/ for more info

  CREATE OR REPLACE FUNCTION "SPACEWALK"."LOOKUP_EVR" (e_in IN VARCHAR2, v_in IN VARCHAR2, r_in IN VARCHAR2)
RETURN NUMBER
IS
	PRAGMA AUTONOMOUS_TRANSACTION;
	evr_id		NUMBER;
BEGIN
	SELECT id INTO evr_id
          FROM rhnPackageEvr
         WHERE ((epoch IS NULL and e_in IS NULL) OR (epoch = e_in))
           AND version = v_in AND release = r_in;

	RETURN evr_id;
EXCEPTION
        WHEN NO_DATA_FOUND THEN
            INSERT INTO rhnPackageEvr (id, epoch, version, release, evr)
            VALUES (rhn_pkg_evr_seq.nextval, e_in, v_in, r_in,
                EVR_T(e_in, v_in, r_in))
            RETURNING id INTO evr_id;
        COMMIT;
	RETURN evr_id;
END;
 
/
