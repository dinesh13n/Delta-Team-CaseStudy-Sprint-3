# KPI variance table

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/34-after-kpis/EVD-O-01-after-kpis.json (SHA-256 3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| KPI | Baseline | After | Variance | Direction |
|---|---|---|---|---|
| K1 p95 | 13709 | 13709 | 0 | none |
| K2 | 2.2451 | 2.2451 | 0 | none |
| K3 | 39.6% | 39.6% | 0 | none |
| K4 | 33.6% | 33.6% | 0 | none (source stream) |
| K5 | 904,432 | 904,432 | 0 | none |
| K6 max | 4995 | 4995 | 0 | none |
| K7 | 18 | 18 | 0 | none (raw layer) |
| K8 | 6 | 6 | 0 | none (raw layer) |
| K7 curated / K8 curated | n/a | 0 / 0 | not comparable | quarantine moved the rows; a different population |
| K9 tests | 3 | 170 | +167 | engineering |
| K10 coverage | 45% | 97% | +52 pts | engineering |

Zero variance on K1 to K8 is the expected and correct result for an unchanged fixture; it is reported rather than hidden.
