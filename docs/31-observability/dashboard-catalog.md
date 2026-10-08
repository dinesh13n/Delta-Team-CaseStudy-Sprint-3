# Dashboard catalogue

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (as code) / CONDITIONAL (not rendered) |
| Evidence sources | evidence/31-observability/EVD-N-01-observability-validation.json (SHA-256 b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Dashboards are JSON under `observability/dashboards/`, Grafana-style panel lists with a datasource variable. They are **not** imported into a Grafana instance; what was verified is that every expression parses and every metric and grouping label exists in the live exposition. [VF]

| Dashboard | Panels | Audience | Question it answers |
|---|---|---|---|
| service-red | 5 | on-call, owner | Is the API up, fast and not erroring? Who is being denied? |
| ai-quality | 8 | AI owner, reviewers | Is the model used, falling back, being blocked, being trusted by humans? |
| integrity-data | 3 | on-call, auditor | Is the audit chain intact, is data fresh, is the AI endpoint throttling? |

## Rendering risks
- Panel units and thresholds are untested visually.
- `${DS_PROMETHEUS}` must be bound at deploy.
- The ai-quality "human decisions" panel will be empty until reviewers actually decide suggestions; with the fixture, only validation traffic exists.
- No business dashboards (on-time, exception backlog): KPI computation is batch (`kpis.py`), not exported as metrics. Operational KPIs are reported in the O-stage docs, not live.
