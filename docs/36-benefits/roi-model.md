# ROI model

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (assumption model) |
| Evidence sources | evidence/36-benefits/EVD-O-03-benefit-model.json (SHA-256 2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

`ROI = (monthly_net_hours × 36 − build_hours) / build_hours`, with `monthly_net_hours = outcomes × minutes_saved / 60 − ops_hours`, `outcomes = 354 × volume × adoption × approval`.

| Scenario | Monthly net hours | 36-month ROI |
|---|---|---|
| Optimistic | +196 | +10.8× |
| Expected | −12 | −1.7× |
| Downside | −41 | −2.2× |

**There is no single ROI number.** The expected case is negative at fixture volume: 354 exceptions per month cannot repay an operations overhead of 16 hours per month unless each approved outcome saves about 7.75 minutes. The optimistic case needs 10× volume and 5 minutes saved. [Arithmetic on assumptions, EVD-O-03]
