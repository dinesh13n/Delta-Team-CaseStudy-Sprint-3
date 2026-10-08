# Elevator pitch

| Field | Value |
|---|---|
| Stage | Q: Model portability and demonstration |
| Runbook step | Q3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | docs/42-executive/demo-day-script.md; stage gates |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## 30 seconds
We were handed a logistics operations repository that could not run its own quick-start, let any caller claim any role, and let an AI endpoint answer with no check. We measured it, pinned today's behaviour with tests, then fixed it with evidence at every step. A 12-attack red team now succeeds **0 times out of 12** where it succeeded **10** times against the delivered code. We also say plainly what is still unproven: there is no real model, no deployment, no named owner and no measured business benefit.

## One sentence
Controls are verified and measured; business value is not, and we say so.

## Do not say
"Production ready" without the conditions; "AI saves cost" (no benefit is verified; the model is NPV-negative at fixture volume); "model-independent" as a demonstrated fact (not run).
