# Data retention plan

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (classes proposed; durations are the Compliance Owner's) |
| Evidence sources | docs/25-governance/evidence-retention-policy.md |
| Assumptions | See body |
| Unresolved issues | RA-01, OQ-04, OQ-21 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Data | Proposed class | Duration |
|---|---|---|
| Audit log and approvals | evidence | UNRESOLVED (RA-01); never shorter than the longest decision it supports |
| Curated and quarantine layers | derived, rebuildable | until the next load plus rollback window |
| Raw source files | source of record | per data owner |
| Metrics, logs | operational | short (days to weeks) [ASM] |
| Backups | recovery | UNRESOLVED |
| Evaluation sets, red-team transcripts | evidence | life of the model that they certify + 1 year [ASM] |
Deletion and rights requests (P-06, P-07) are **not implemented**.
