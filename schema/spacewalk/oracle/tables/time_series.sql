--
-- Copyright (c) 2008 Red Hat, Inc.
--
-- This software is licensed to you under the GNU General Public License,
-- version 2 (GPLv2). There is NO WARRANTY for this software, express or
-- implied, including the implied warranties of MERCHANTABILITY or FITNESS
-- FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
-- along with this software; if not, see
-- http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
-- 
-- Red Hat trademarks are not licensed under GPLv2. No permission is
-- granted to use or replicate Red Hat trademarks that are incorporated
-- in this software or its documentation. 
--

CREATE TABLE time_series
(
    o_id        VARCHAR2(64) NOT NULL, 
    entry_time  NUMBER NOT NULL, 
    data        VARCHAR2(1024)
)
ENABLE ROW MOVEMENT
;

CREATE INDEX time_series_probe_id_idx
  ON time_series(SUBSTR(O_ID, INSTR(O_ID, '-') + 1,
   (INSTR(O_ID, '-', INSTR(O_ID, '-') + 1) - INSTR(O_ID, '-')) - 1
  ))
  TABLESPACE [[64k_tbs]]
  NOLOGGING;

CREATE INDEX time_series_oid_entry_idx
    ON time_series (o_id, entry_time)
    TABLESPACE [[64k_tbs]];

