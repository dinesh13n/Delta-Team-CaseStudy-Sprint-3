# Delivery dependencies

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

DB-02 -> DB-03 (datasets before evaluation); DB-03 -> DB-09 (thresholds informed by results); DB-04, DB-05 -> DB-11 (observability of the workflow); DB-07 -> DB-09 (red team follows threat model); DB-10 -> DB-15; DB-14 depends on an external second model (BLOCKED). External dependencies: OQ-02 model, OQ-03 egress, OQ-05 approvers, OQ-07 IdP, GitHub admin for protection and CI.
