# Economic value summary

| Field | Value |
|---|---|
| Stage | R: Executive Defence, Final PRD, Evidence Pack |
| Runbook step | R3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/32-finops; docs/36-benefits |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Item | Figure | Class |
|---|---|---|
| Token cost per request | $0.0003 to $0.004 at illustrative prices | [ASM] |
| Cost per period at 354 requests | $0.10 to $1.44 | [ASM] |
| Measured audit storage per AI request | 1,170 bytes | [VF] `evidence/32-finops/EVD-N-04-finops-model.json` (sha256 `207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac`) |
| NPV over 36 months (analyst-hours) | −970 expected; +5,525 optimistic; −2,466 downside | model output on stated assumptions `evidence/36-benefits/EVD-O-03-benefit-model.json` (sha256 `2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52`) |
| Verified monetary benefit | **nil** | [VF] |
| Cost per outcome | **not stated**: three of five terms unknown (review minutes, labour rate, approval rate) | [UNK] |

Conclusion: human review dominates cost by orders of magnitude; token spend is immaterial. The case depends on review time saved, which has not been measured. Do not present any saving.
