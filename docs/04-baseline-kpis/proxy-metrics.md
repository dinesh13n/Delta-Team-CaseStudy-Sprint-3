# Proxy Metrics and Limitations

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

| Proxy | What it stands in for | Limitation |
|---|---|---|
| K1 latency | service responsiveness | uniformly random values up to 15 s; not measured from a running service |
| K2 cost units | spend per transaction | no currency, no price card, not tied to a shipment (events carry no shipment id) |
| K3 severe share | failure rate | severities evenly distributed (about 20% each), so not a real error rate |
| K4 correlation | traceability | counts presence only, not whether ids join to real requests |
| K5 tokens | AI usage | declared by the dataset, never produced by a model |
| K6 retries | carrier reliability | values 51 to 4,995 are implausible; a saga that retries this much would not complete |
| K7/K8 | data quality | seeded defects; not a production error rate |
| K9/K10 | engineering health | three trivial tests |
No KPI above is a business outcome.
