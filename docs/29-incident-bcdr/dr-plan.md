# Disaster recovery plan

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (no platform) |
| Evidence sources | rto-rpo.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Step | Action | Evidence |
|---|---|---|
| 1 declare | incident commander declares DR when the primary environment cannot be recovered within RTO | – |
| 2 provision | recreate the runtime from the image / `python -m uvicorn` on any host (platform-neutral, ADR-0009) | image never built; local start verified |
| 3 secrets | inject `AUTH_SECRET` from the secret store (new value; old tokens invalid) | design |
| 4 data | restore `logs/audit-v2.log` and `logs/approvals.jsonl` from the last backup; run the ETL from the source | N3 restore check |
| 5 verify | `/ready` 200; `/audit/verify` valid; record tip hash compared with the externally recorded hash | N3 |
| 6 switch | point traffic | platform |
| 7 review | within 5 days | – |
Region/zone failover: not applicable (no platform). Single-instance, file-based state means DR = rebuild + restore, not failover.
