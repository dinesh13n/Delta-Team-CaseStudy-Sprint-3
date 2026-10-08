# Economics Baseline Reconciliation (Step E2)

| Field | Value |
|---|---|
| Stage | E: Intervention Qualification and Initial PRD (Spine 8-9) |
| Runbook step | E2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/00-preflight/ai-economics/economics-readiness.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Comparison with `docs/00-preflight/ai-economics/` (retired assumptions struck through, not deleted).

| A6 assumption | Status after E1 |
|---|---|
| ASM-W1 AI assists exception investigation first | **retained** (I9) |
| ~~S3 GenAI applied to ETA prediction~~ | **retired** (I7 deferred) |
| ~~S3 GenAI applied to route optimisation~~ | **retired** (I8 deferred) |
| ~~S4 agentic scenario costs~~ | **retired** (I10 rejected; 4.5M tokens per 1x period no longer applicable) |
| Tokens per request <= 3,000 typical, <= 5,000 cap | **retained**: the single I9 call fits |
| Context <= 8,000 tokens, loop = 1 call, 0 tool loops | **retained** |
| p95 latency <= 3,000 ms | **retained**; a deterministic fallback guarantees an answer when the model is slower |
| Cost per request <= 2.25 units | **retained** (provisional; unit undefined) |
Remaining AI volume: one call per exception case instead of three capabilities. Real prices unknown (OQ-02), so cost stays a ceiling, not a forecast.
