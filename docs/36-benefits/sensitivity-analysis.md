# Sensitivity analysis

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/36-benefits/EVD-O-03-benefit-model.json (SHA-256 2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

One-at-a-time swings of NPV around the expected scenario (hours): volume (1×→10×) 1,159; operations overhead (8→40 h/month) 998; build effort (300→1,200 h) 900; minutes saved (−1→5) 386; adoption (20%→80%) 155; approval (50%→90%) 74.

At the expected volume, the answer is driven by **fixed costs and volume**, not by the quantities the AI affects. Doubling adoption or approval barely moves it. Reducing operations overhead (automation of drift checks, alert tuning) matters more than improving the suggestion.
