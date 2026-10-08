# Corrective action backlog

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (backlog) |
| Evidence sources | docs/35-value-leakage/* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Action | Closes |
|---|---|---|
| CA-01 | Obtain business baseline (cycle time, cost per shipment, exception rate, on-time) from the operating owner | F-57, OQ-08 |
| CA-02 | Add shipment id to events and a producer correlation id | cost-per-case, F-M3-01 |
| CA-03 | Pilot with named reviewers; measure adoption, override, time per decision | adoption, human-override metrics |
| CA-04 | Fix enum noise in the contract with the data owner | DEBT-15 |
| CA-05 | Independent re-run of TEVV and red team | TEVV-R-01 |
| CA-06 | Four-eyes and approval expiry | HC-R-01, HC-R-03 |
| CA-07 | Scheduler for ETL | DATA_STALE |
| CA-08 | Revoke exposed credentials | P-X5 |
