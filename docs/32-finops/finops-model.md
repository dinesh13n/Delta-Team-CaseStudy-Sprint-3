# FinOps model

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (parameterised) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Reproducible: `python -m scripts.finops_estimate --out ...` (EVD-N-04). Parameters and where they come from:

| Parameter | Source | State |
|---|---|---|
| tokens per request | measured estimate (349 requests) | measured, estimate |
| audit bytes per request | measured | measured |
| metric series | measured (53) | measured |
| volume | 354 / 3,540 / 35,400 per period | [ASM] multipliers |
| p_in, p_out | none | [UNK]; illustrative 1, 5, 15 USD/Mtok |
| review minutes, labour rate | none | [UNK] |
| platform compute/storage | none | [UNK] |

Scenario table (tokens only, illustrative prices): 1× → 96 k tokens per period, $0.10 / $0.48 / $1.44; 10× → 0.96 M, $0.96 / $4.80 / $14.40; 100× → 9.6 M, $9.60 / $48 / $144.
**These are order-of-magnitude arithmetic, not a forecast.**
