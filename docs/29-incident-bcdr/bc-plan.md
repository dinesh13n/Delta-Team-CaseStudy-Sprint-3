# Business continuity plan

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | docs/28-resilience/graceful-degradation-design.md |
| Assumptions | See body |
| Unresolved issues | manual fallback owner |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**Critical activities** (what dispatchers need): read a shipment, read its events, see exceptions, see KPIs. AI suggestions are not critical.
| Scenario | Continuity measure |
|---|---|
| AI unavailable | proceeds without AI (AI-disabled mode); dispatchers use records and events |
| API unavailable | **no manual alternative is defined**: before the transformation the same API was the only path. A manual fallback (spreadsheet export of the curated layer) is proposed: `data/curated/*.csv` are plain files that can be opened without the service |
| Data stale | use the last load; check `X-Data-Load-Id` and age |
| Batch failed | previous publication stays; rerun ETL after fixing input (idempotent) |
| Key person absent | not addressed: roles are unnamed (OQ-05) |
Review: after each incident and every 6 months [ASM].
