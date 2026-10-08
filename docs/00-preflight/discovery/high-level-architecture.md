# High-Level Architecture

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0A pre-flight discovery |
| Runbook step | A4 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, pending Transformation Lead review |
| Evidence sources | EVD-A-04-repo-tree-annotated.txt; EVD-A-04b-data-profile.txt; direct file reads of the repository |
| Assumptions | See assumptions-unknowns.md |
| Unresolved issues | See assumptions-unknowns.md |
| Residual risks | Read-only discovery only; no behavioural run yet (Stage C) |

Classification key: **[VF]** Verified Fact (read in a cited file), **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown. Paths are relative to `07-logistics-shipment-fleet-routing-ops/`. This document makes no transformation recommendations (Spine 0A).

## 1. As-found structure
```
client (curl/.http, web scaffold)
   |  HTTP
FastAPI app (apps/api/main.py)
   |-- GET  /health
   |-- GET  /records/{record_id}  --> domain_service.load_record --> data/synthetic/shipments.csv
   |                              --> audit.write_event --> logs/audit.log (local file)
   '-- POST /ai/summarize/{id}    --> domain_service.load_record --> ai_gateway.summarize_record (simulated)
                                  --> audit.write_event
Batch side (not connected to the API): etl/run_daily_batch.py, legacy/reconcile_legacy.py -> read shipments.csv, print counts
```
- [VF] Everything is single-process, synchronous, file-backed. No layering beyond `main.py` calling three service modules.
- [VF] The API handlers import services directly; no dependency injection, configuration module or settings object.
- [VF] ADR 0001 records "Keep legacy batch jobs while introducing FastAPI services... never revisited" (`docs/ADR/0001-partial-modernization.md`).
- [INF] The two code paths (API, batch) share only the CSV file; business rules are duplicated or absent rather than shared.
- [UNK] The intended production topology; `docs/architecture/target-state-principles.md` lists principles only.
