# Graceful degradation design

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/28-resilience/EVD-M-03-drills/ |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Levels, from healthy to minimal. Each level is reachable by configuration or happens automatically, and every level keeps the audit chain and the human decision rule.

| Level | Condition | Behaviour | Automatic? |
|---|---|---|---|
| 0 Normal | all healthy | model (if configured) or deterministic summary + approval | – |
| 1 AI degraded | model slow/error/leak | deterministic fallback; reason shown | yes |
| 2 AI isolated | breaker open | no model calls; deterministic only | yes |
| 3 AI off | `AI_ENABLED=false` | AI route 503; everything else normal | operator |
| 4 Data stale | last load older than the limit | `/ready` fails (platform can stop routing); API still serves the last load with `X-Data-Load-Id` | detection automatic if configured |
| 5 Data unavailable | curated layer missing | not ready; data routes fail | yes |
| 6 Audit unavailable | audit sink errors | requests fail closed | yes |

Rule: degradation is announced in the response (`generated_by`, `fallback_reason`, status codes), never silent.
