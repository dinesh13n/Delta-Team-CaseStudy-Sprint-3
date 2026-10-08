# Fallback matrix

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/ai/gateway.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Dependency / condition | Primary | Fallback | User sees | Autonomy impact |
|---|---|---|---|---|
| model slow/down/unconfigured | model | deterministic provider | summary with `generated_by: fallback` and reason | none; still needs approval |
| model output invalid / leaking | model | deterministic provider | same | none |
| AI switched off | – | 503 on AI route only | "AI disabled" | humans work from the record |
| curated data missing | – | `/ready` 503, data routes 404/500 | not ready | none |
| data stale | – | `/ready` 503 if `DATA_MAX_AGE_S` set; responses carry `X-Data-Load-Id` | stale values until reload | humans can see the load id |
| audit sink down | – | requests fail (fail closed) | 500 with correlation id | no unaudited action |
| IdP down (future) | JWKS | none: all tokens refused (fail closed) | 401 | no access |
| carrier down (future) | carrier | retry within ceiling, then FAILED + human queue | booking failed | human decides |

A *second model* as fallback is not configured (OQ-02). The fallback is the in-process deterministic provider, which has no external dependency and therefore cannot fail the same way.
