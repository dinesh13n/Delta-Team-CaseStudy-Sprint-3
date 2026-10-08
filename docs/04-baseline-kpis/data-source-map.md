# Data Source Map

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 4 KPI baseline) |
| Runbook step | C1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | evidence/04-baseline-kpis/EVD-C-05-data-profile.json; evidence/04-baseline-kpis/EVD-C-05-profile.py |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| KPI | File | Field |
|---|---|---|
| K1 | data/synthetic/events.jsonl | latency_ms |
| K2 | events.jsonl | cost_units, business_entity |
| K3 | events.jsonl | severity |
| K4 | events.jsonl | correlation_id |
| K5 | ai_invocations.csv | token_count |
| K6 | carrier_bookings.csv | retry_count |
| K7, K8 | six CSVs | primary key columns, all fields |
| K9, K10 | tests/, apps/, etl/, legacy/, scripts/ | pytest and coverage output |
