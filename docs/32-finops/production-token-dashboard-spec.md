# Production token dashboard specification

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (spec) / CONDITIONAL (no real tokens) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac) |
| Assumptions | See body |
| Unresolved issues | [UNK] no model, platform or price exists |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Panels already in `observability/dashboards/ai-quality.json`: token estimate rate, AI requests by producer, fallbacks by reason, AI latency, human decisions.

| Panel to add when a model is wired | Source | Why |
|---|---|---|
| Input / output / cached tokens by model and prompt version | provider usage fields | the estimate cannot split input from output |
| Tokens per approved suggestion | tokens ÷ `ai_decisions_total{decision="approve"}` | unit cost per outcome |
| Wasted tokens | tokens on fallbacks, rejects, retries | token leakage |
| Spend vs daily ceiling | tokens × configured price | guardrail |
| Cache hit ratio | cache counters (none exist) | cache effectiveness |

Today `ai_tokens_total` is the gateway's `len/4` estimate over the context it would send. **No provider has been called, so there is no billed or reported token count anywhere in this repository** (F-28 stands for production: it is resolved only for the estimate).
