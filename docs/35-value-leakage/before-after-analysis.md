# Before and after analysis

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (analysis) / no business effect found |
| Evidence sources | evidence/34-after-kpis/EVD-O-01-after-kpis.json (SHA-256 3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717); evidence/26-tevv |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Dimension | Before | After | Attributable to intervention? |
|---|---|---|---|
| Proxy KPIs K1 to K8 | baseline values | identical | n/a: no change |
| Identity | self-asserted header role | verified token | yes (control, tested) |
| Access | any persona string | deny-by-default policy | yes |
| AI | endpoint echoed first column, no guardrail, no human step | schema-validated, leak-checked, suggest-only, approval record | yes |
| Audit | no actor, no correlation, no tamper evidence | actor, correlation, policy decision, hash chain | yes |
| Data | defective rows served | quarantined with reason | yes |
| Red team | 10 of 12 attacks succeed | 0 of 12 | yes |
| Business outcomes (cycle time, cost per shipment, exception rate, on-time) | unknown (F-57) | unknown | **not measurable** |

The intervention changed **control properties**, which are verified by tests and attacks. It did not and could not change the proxy KPIs, and no business KPI exists to move.
