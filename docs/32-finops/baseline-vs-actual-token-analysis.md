# Baseline vs actual token analysis

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (not comparable like for like) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac); docs/00-preflight/ai-economics/provisional-token-budget.md |
| Assumptions | See body |
| Unresolved issues | [UNK] no model, platform or price exists |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Quantity | A6/E2 envelope (baseline) | Actual (EVD-N-04, 349 requests) | Within envelope? |
|---|---|---|---|
| Tokens per request, mean | 2,562 [M, fixture column] | 271.2 (estimate) | yes |
| Tokens per request, p95 / max | max observed 4,989 | 274 / 275 | yes (typical ≤ 3,000, hard cap ≤ 5,000) |
| Cost per request | 2.245 cost units (fixture mean) | not measurable: no price, no provider | n/a |
| Latency p95 | fixture 13,707 ms event latency; constraint ≤ 3,000 ms AI, ≤ 500 ms non-AI | 7.7 ms (single worker), 42 ms (8 workers), deterministic provider | **not meaningful for a model** |
| Retries | allowance 1 per request | breaker: 5 failures to open; no retry loop | within |

## Variance and why it is mostly not an improvement
The 89% drop (2,562 → 271) must **not** be reported as a saving. [INF]
1. The baseline figure is a column of the fixture's `ai_invocations` data with a scrambled schema (F-28/F-57); the baseline AI endpoint did not call a model and echoed the first column.
2. The actual figure is an estimate (`len/4`) of the **allow-listed facts only**, with no system prompt, no instructions, no output tokens and no model.
3. A real model call adds prompt boilerplate and output tokens. The right comparison is made once a model is chosen, with provider-reported usage.
What the number does show: the context budget (`max_record_tokens` 2,000, events trimmed to the last 10 plus exceptions) keeps the context small by construction; the envelope is not at risk from the context itself.

3 of 349 requests fell back to the deterministic summary (0.9%); the reason was not analysed in this run.
