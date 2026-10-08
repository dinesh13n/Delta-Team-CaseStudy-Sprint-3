# Data Flow Overview

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

## 1. Stores
| Store | Type | Writers | Readers |
|---|---|---|---|
| `data/synthetic/*.csv` (6 files, 354 rows each) | flat file | none in code | API (shipments only), ETL, legacy |
| `data/synthetic/events.jsonl` (3,000 events) | flat file | none in code | `scripts/sanity_check.py` (count only) |
| `logs/audit.log` | flat file, created at runtime | `audit.write_event` | none |

## 2. Flows in code
- [VF] Read: HTTP `/records/{id}` -> `load_record` -> scan of `shipments.csv` matching `record_id in row.values()` (any column) -> returns row, else first row (`domain_service.py` lines 11-15).
- [VF] AI: HTTP `/ai/summarize/{id}` -> same loader -> `PROMPT_TEMPLATE.format(record=record)` -> simulated response with `token_estimate = words * 2`.
- [VF] Audit: each call appends `{ts, action, details}` where details hold `record_id` and role (read) or `record_id` and fixed model name (AI); no actor, tenant, correlation id.
- [VF] Batch: ETL reads `shipments.csv`, counts rows with any empty value, prints `{processed, malformed, sample}`; malformed rows are counted only, not stored (`run_daily_batch.py`).

## 3. Data observations (EVD-A-04b, measured on files matching the A1 baseline hashes)
- [VF] Each CSV: 354 data rows, 3 duplicated primary-key values, 1 row with a blank field, exactly 1 key with the `REC-` prefix (the first row, e.g. `REC-0001` in all six files, including the vehicles and routes files).
- [VF] `events.jsonl`: 3,000 events; `correlation_id` is null in 983 (32.8%); 529 distinct correlation ids, each used at most 6 times; no duplicate `event_id` or `payload_hash`; every event carries `actor`, `latency_ms`, `cost_units`.
- [VF] Categorical columns hold values that do not match their column meaning (e.g. `shipments.origin` = `standard`, `routes.origin` = `pending`; `ai_invocations.use_case` = `not_enforced`).
- [INF] The generator filled categorical columns from a shared word list; domain semantics are weak outside identifiers and numerics.
- [UNK] Data volumes, freshness and retention in any real system.
