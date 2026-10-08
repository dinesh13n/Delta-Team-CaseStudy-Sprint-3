# RTO and RPO

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (ASM; no business figures) |
| Evidence sources | docs/28-resilience/failure-injection-results.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Asset | Recreatable from | RPO (proposed) | RTO (proposed) | Basis |
|---|---|---|---|---|
| Application code, prompts, policy | git | 0 (every merged commit) | 1 h to redeploy | [ASM] |
| Curated and quarantine layers | ETL from the synthetic/source files | 0 if the source is intact | ETL runtime (seconds on the fixture) | verified: ETL is idempotent and byte-identical (drill 3) |
| Source data (`data/synthetic`) | git (immutable fixture); in production: the source system | n/a | n/a | |
| Audit log | backups only | 15 min if shipped continuously; 24 h if daily | 4 h | [ASM]; **no off-host copy exists** |
| Approval records | backups only | same as audit | 4 h | |
| In-memory state (rate limits, breaker, cache) | none needed | n/a | restart | |

[UNK] No business statement of tolerable downtime or data loss exists. These numbers are proposals to be overwritten. Restore of audit and approvals was verified mechanically in N3 (`EVD-N-03-backup-restore.json`).
