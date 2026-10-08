# Integration inventory

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (as scoped) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Integration | Direction | State | Notes |
|---|---|---|---|
| CSV/JSONL fixture -> ETL -> curated layer | in | built | batch; no live system of record exists |
| Identity provider (JWKS) | in | stub, fail closed | OQ-07 |
| Model provider | out | port + deterministic adapter | OQ-02, OQ-03 |
| Carrier booking | out | port + simulated carrier + saga | no live carrier in the repo |
| Legacy reconcile job (`legacy/reconcile_legacy.py`) | out | kept, secrets removed | not exercised (needs DB) |
| Audit sink | out | local JSONL, hash chain | external sink deferred (F-44) |
| Metrics | out | Prometheus text at /metrics | scraper not deployed |
