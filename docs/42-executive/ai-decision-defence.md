# AI decision defence

| Field | Value |
|---|---|
| Stage | R: Executive Defence, Final PRD, Evidence Pack |
| Runbook step | R3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/08-ai-qualification; docs/19-intelligence |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Was AI appropriate?
**Partly, and only suggest-only.** Of ten interventions, seven are deterministic fixes (identity, exact lookup, ETL validation, audit, correlation, contracts, resilience), two are deferred, and one (exception summary, I9) retains GenAI behind a human approval gate (`docs/08-ai-qualification/ai-vs-no-ai-matrix.md` (sha256 `63cc7d724b2a9971f8506327106cd33922cedee6879547cdc1577d0d8e47d27b`)). The delivered "AI" returned the first column of a row (F-29); there was no AI quality to preserve.

## What the AI path does now
Allow-listed fields only; untrusted text delimited as data; JSON-schema validated output with abstention and deterministic fallback; evaluated guardrail; prompt and model locks that stop the service from starting if changed; every suggestion needs a recorded human decision.

## What we cannot say
No real model was called, so answer quality, latency, token cost and injection resistance **of a real model** are unmeasured (`real_model_called: false`, `evidence/26-tevv/EVD-L-02-final-eval-run.json` (sha256 `dfdf29d208c4cdc05911c3fe8c76ba6ccfe66ccbd6d9a0677aee10d40c8ee54e`)). The three AI capabilities in the delivered docs (ETA Prediction, Route Optimization, Exception Copilot) remain not implemented. Portability across models was designed for and **not tested** (`docs/40-scale/model-comparison.md` (sha256 `862e58f164d967c55491c61f732866224603a97f129696fd2a657a763b74a63d`)).

## Challenge to expect
"Why keep GenAI at all?" Answer: the case for it rests on review-time saved, which is unmeasured; the economic model is negative at fixture volume and positive only at about 10× volume with several minutes saved per outcome (`docs/36-benefits/npv-model.md` (sha256 `2f861d51bca536e3f6739aace8c190872596bb9873cc8656f82a3b57329a4129`)). Keep it behind a flag until measured.
