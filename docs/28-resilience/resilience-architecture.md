# Resilience architecture

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (code) / CONDITIONAL (platform) |
| Evidence sources | apps/api/resilience.py, evidence/28-resilience/EVD-M-03-drills/ |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Principle (K1 link): when a dependency fails, the system may lose *intelligence* but never *control*. What continues is a human-control decision: the core read workflow (records, shipments, events, KPIs) and the audit chain continue; AI suggestions degrade to a deterministic summary or to a 503.

```
client -> [auth, policy, rate limit, body cap] -> core read path (CSV curated layer)      always available
                                                |
                                                +-> AI gateway -> guarded( timeout -> circuit breaker -> provider )
                                                        |  failure of any kind
                                                        +-> deterministic fallback provider (in process, no dependency)
batch: staged write -> per-file os.replace publish (readers never see a half-written file)
booking: saga with idempotency key, bounded retries (<= 5), compensation, durable JSONL store
```
| Mechanism | Code | Status |
|---|---|---|
| Timeout on model calls (default 5 s) | `resilience.call_with_timeout` | tested, drilled |
| Circuit breaker (5 failures, 30 s reset, one half-open probe) | `resilience.CircuitBreaker` | tested, drilled |
| Bulkhead | `resilience.Bulkhead` | tested; **not wired** (F-M3-02) |
| Fallback provider | `DeterministicProvider` | tested, drilled |
| Retry with backoff, ceiling, jitter | `carrier_saga` | tested, simulated |
| Idempotency | saga key; ETL business keys | tested, drilled |
| Staged publication | `etl.publish` | tested, drilled |
| Kill switch | `AI_ENABLED` | tested, drilled |
| Readiness with data freshness | `/ready`, `DATA_MAX_AGE_S` | tested, drilled |
| Rate limit, body cap | `main.py` | tested |

Not present: multi-instance, replication, queueing, cache layer beyond the mtime-keyed in-process CSV cache.
