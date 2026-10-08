# Data source inventory

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-A-04b data profile; EVD-C-05 profile; semantic-layer/entities.yaml |
| Assumptions | See body |
| Unresolved issues | OQ-14 ruling provisional; approvers UNRESOLVED |
| Residual risks | See data-context-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Corrected on 2026-10-08: an earlier draft of this file named files that do not exist (drivers, warehouses, carriers). The table below was checked against `git ls-files` of the subtree.
| ID | Source (under `07-…/data/synthetic/`) | Format | Rows | Owner | Class | Notes |
|---|---|---|---|---|---|---|
| DS-01 | `shipments.csv` | CSV | 354 data rows (355 lines incl. header) | UNRESOLVED | [VF] | primary file read by the API; 3 duplicate keys, blank row, 1900-01-01 timestamp |
| DS-02 | `tracking_events.csv` | CSV | 354 | UNRESOLVED | [VF] | confidence max 1.42 |
| DS-03 | `vehicles.csv` | CSV | 354 | UNRESOLVED | [VF] | |
| DS-04 | `routes.csv` | CSV | 354 | UNRESOLVED | [VF] | |
| DS-05 | `carrier_bookings.csv` | CSV | 354 | UNRESOLVED | [VF] | retry_count 51-4995 |
| DS-06 | `ai_invocations.csv` | CSV | 354 | UNRESOLVED | [VF] | AI call log fixture |
| DS-07 | `events.jsonl` | JSONL | 3,000 events | UNRESOLVED | [VF] | 983 null + 1,009 empty correlation_id (1,992, 66.4%) |
| DS-08 | `data/manifest.json`, `data/quality_issues.json` | JSON | 2 | UNRESOLVED | [VF] | shipped metadata |
| DS-09 | `semantic-layer/` YAML (repo root) | YAML | 9 files | Delta-Team | [VF] | new in Stage D |
| DS-10 | `logs/audit.log` (runtime) | JSONL | created at run time | n/a | [VF] | written by audit.py, no actor, no correlation id |
All data is synthetic [VF]. Real systems (TMS, telematics, carrier APIs) are [UNK].
