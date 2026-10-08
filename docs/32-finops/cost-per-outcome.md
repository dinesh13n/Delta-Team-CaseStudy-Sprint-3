# Cost per business outcome

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (model with explicit unknowns) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac) |
| Assumptions | See body |
| Unresolved issues | OQ-09 financial data; review time |
| Residual risks | N-R-16 value case depends on unmeasured human time |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Challenge 12 standard: cost explained per business outcome. Outcome O1 = **an exception resolved with a reviewed, approved AI suggestion.**

`cost_outcome = (cost_request × requests_per_outcome + review_minutes × labour_rate / 60) / approval_rate`

| Term | Value | Class |
|---|---|---|
| cost_request | $0.0003 to $0.004 at illustrative prices | [ASM] |
| requests_per_outcome | ≥ 1; unknown | [UNK] |
| review_minutes | unknown; sensitivity 1, 2, 5 min | [UNK] |
| labour_rate | unknown (OQ-09: no financial data) | [UNK] |
| approval_rate | unknown: no human has reviewed a real suggestion (tabletop and tests only) | [UNK] |

## What can be concluded without the unknowns
- At $15 per million tokens one request costs about $0.004. One minute of review costs the same when the labour rate is about **$0.24 per hour**. For any realistic rate, **human oversight dominates the cost of an outcome by two or more orders of magnitude**. [INF, arithmetic on stated assumptions]
- Therefore the value case rests on review time saved or errors prevented, not on token spend. O-stage must treat review time as the primary cost.
- Dividing by `approval_rate` means a low approval rate multiplies every cost: 50% approval doubles cost per outcome.

No monetary outcome figure is stated, because three of five terms are unknown. Total spend per period at 1× (354 requests) is $0.10 to $1.44 in tokens at the illustrative prices, which is immaterial next to review time.
