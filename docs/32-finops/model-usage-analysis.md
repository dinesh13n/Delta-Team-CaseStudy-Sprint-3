# Model usage analysis

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT MEASURED (no model) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac); evidence/26-tevv/EVD-L-02-final-eval-run.json |
| Assumptions | See body |
| Unresolved issues | OQ-02, OQ-03 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Usage fact | Value |
|---|---|
| Model calls ever made by this system | **0** (`real_model_called: false` in the evaluation evidence) |
| Producers observed | deterministic 346, fallback 3 (of 349 fixture requests) |
| Model provider configured | no: `UnconfiguredModelProvider` fails closed |
| Models compared | none yet (Stage Q: two Anthropic models, which limits the portability claim) |

Anything claiming model cost, quality per model or latency per model would be invented. This document exists so the gap is explicit.
