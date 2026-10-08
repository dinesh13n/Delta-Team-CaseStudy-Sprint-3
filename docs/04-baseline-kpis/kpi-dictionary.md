# KPI Dictionary (frozen)

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

**No business KPI data exists in the repository (F-57).** There is no cycle time, cost per shipment, exception rate, on-time rate, rework rate or adoption figure. Every KPI below is a **proxy** measured from the synthetic fixture. Definitions are FROZEN as of this document; they must not change to improve results (Spine 34/35).

| ID | Name | Meaning | Formula | Unit | Owner (role) | Source | Period | Segmentation |
|---|---|---|---|---|---|---|---|---|
| K1 | Event latency | time recorded per event | percentile (index method, sorted[int(p/100*n)]) of `latency_ms` | ms | SRE Owner UNRESOLVED | events.jsonl | fixture, span unknown | by business_entity |
| K2 | Cost per event | declared cost units per event | sum(cost_units)/count(events) | cost units | Business Sponsor UNRESOLVED | events.jsonl | fixture | by business_entity |
| K3 | Severe-event share | share of events with severity error or critical | (error+critical)/total | % | SRE Owner UNRESOLVED | events.jsonl | fixture | by event_type |
| K4 | Correlation completeness | events with a non-null, non-empty correlation_id (amended D-012) | usable/total | % | Compliance Owner UNRESOLVED | events.jsonl | fixture | by actor |
| K5 | Declared AI tokens | token_count summed over invocations | sum(token_count), parseable rows | tokens | AI Governance Owner UNRESOLVED | ai_invocations.csv | fixture | by use_case |
| K6 | Carrier retry level | retry_count distribution | min/mean/max of retry_count | count | Operations Owner UNRESOLVED | carrier_bookings.csv | fixture | by carrier |
| K7 | Duplicate business keys | keys appearing more than once | count over all six datasets | keys | Data Owner UNRESOLVED | six CSVs | fixture | by dataset |
| K8 | Incomplete rows | rows with any blank field | count over six datasets | rows | Data Owner UNRESOLVED | six CSVs | fixture | by dataset |
| K9 | Baseline test result | passing tests / collected | pytest result | tests | Repository Owner UNRESOLVED | EVD-C-03 | run date | n/a |
| K10 | Baseline coverage | statement coverage of apps, etl, legacy, scripts | coverage.py | % | Repository Owner UNRESOLVED | EVD-C-03 | run date | by module |
