# Circuit breaker policy

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/resilience.py, tests/test_resilience.py, evidence/28-resilience/EVD-M-03-drills/drill-2-ai-gateway-timeout.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Parameter | Default | Env | Rationale |
|---|---|---|---|
| failure threshold | 5 consecutive failures | `AI_BREAKER_THRESHOLD` | tolerate blips |
| reset window | 30 s | `AI_BREAKER_RESET_S` | short enough to recover, long enough to stop a storm |
| half-open | exactly one probe call; failure re-opens immediately | – | |
| what counts as failure | any exception, **including a timeout** | – | seen in drill 2: a timeout counted as the first failure |
| what does not | schema-invalid or low-confidence *successful* answers | – | the call worked; the content is handled separately |
| state | per process, in memory | – | a restart closes the breaker; multi-instance would need shared state or per-instance behaviour accepted |

Open: no metric is exported for breaker state (only the fallback reason counter). Add `ai_circuit_state` gauge in N1 follow-up (backlog DB-17).
