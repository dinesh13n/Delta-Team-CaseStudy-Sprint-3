# Cost guardrails

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (controls in code) / CONDITIONAL (no spend limit) |
| Evidence sources | apps/api/config.py; apps/api/ai/gateway.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Guardrail | Implemented? | Where |
|---|---|---|
| Context cap per record | yes | `max_record_tokens` 2,000, events trimmed |
| Per-subject rate limit | yes | 30/min default, 429 |
| Provider timeout | yes | 5 s |
| Circuit breaker | yes | 5 failures, 30 s reset |
| Kill switch | yes | `AI_ENABLED=false` |
| Retry cap | yes | none beyond the breaker; no retry loop |
| Daily token ceiling / spend alert | **no** | needs price and volume; propose ceiling at 3× expected daily tokens once measured |
| Per-environment budget | **no** | platform |
| Evaluation spend cap | **no** | needed before the first model evaluation |

Guardrails limit runaway use; they do not set a budget. A budget needs an owner and a price.
