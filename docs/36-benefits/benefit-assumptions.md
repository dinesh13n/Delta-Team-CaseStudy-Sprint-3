# Benefit assumptions

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (assumptions listed) / all monetary values are assumptions |
| Evidence sources | evidence/36-benefits/EVD-O-03-benefit-model.json (SHA-256 2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52) |
| Assumptions | See body |
| Unresolved issues | OQ-09 |
| Residual risks | O-R-06 every input is a guess |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

O-X4: every figure below is an **assumption** [ASM], illustrative, in analyst-hours (no wage exists, OQ-09). Source: `scripts/benefit_model.py` (EVD-O-03).

| Parameter | Optimistic | Expected | Downside | Basis |
|---|---|---|---|---|
| AI-assisted exceptions per month, 1× | 3,540 (10×) | 354 | 354 | fixture invocation count as a planning unit |
| Adoption | 80% | 50% | 20% | none |
| Approval rate | 90% | 70% | 50% | none |
| Review minutes saved per approved outcome | +5 | +2 | **−1** (control adds time) | none; the central unknown |
| Operations overhead, hours per month | 16 | 16 | 40 | alerts, drift check, upkeep |
| One-time build + governance, hours | 600 | 600 | 1,200 | none; delivery effort was not tracked |
| Horizon / discount | 36 months / 10% per year | same | same | convention |
