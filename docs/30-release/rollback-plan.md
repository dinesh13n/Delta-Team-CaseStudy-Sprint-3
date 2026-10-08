# Rollback plan

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | docs/14-transformation/rollback-strategy.md; evidence/28-resilience/EVD-M-03-drills/ |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | N-R-12 rollback never rehearsed on a platform |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Trigger | Action | Time (estimate) | Tested? |
|---|---|---|---|
| Behaviour doubt in one feature | flip the env flag (FF table), restart | minutes | flags tested in unit tests |
| AI misbehaviour | `AI_ENABLED=false`, restart; users keep core workflows | minutes | yes (drill 1, M3; tabletop contain step) |
| Bad release | redeploy previous image digest / `git revert` of the increment group / check out the previous tag | minutes to an hour | not on a platform |
| Bad data load | none needed: atomic publish keeps the previous load; re-run ETL with the corrected input | minutes | yes (drill 5) |
| Corrupted state | restore from backup (backup-validation.md) | seconds at fixture size | yes at repo level |
| Total loss of confidence | check out `baseline/v0.1-as-delivered-bytes`; `sha256sum -c` proves byte identity | n/a | yes in G |

## Rollback limits
- The audit log is append-only; a rollback never rewrites it. Events written by the bad release remain and are explained in the incident record.
- Audit format v1 cannot be re-created (FF-06 withdrawn).
- Rolling back the code does not un-send anything a real provider already received; no provider is wired today.
- Credentials exposed in git history are not rolled back by any of this; they must be revoked (P-X5).
