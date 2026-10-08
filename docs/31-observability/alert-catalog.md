# Alert catalogue

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (as code) / CONDITIONAL (never fired) |
| Evidence sources | evidence/31-observability/EVD-N-01-observability-validation.json (SHA-256 b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485) |
| Assumptions | [ASM] thresholds are starting values |
| Unresolved issues | OQ-05 recipients |
| Residual risks | N-R-01 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Source: `observability/alerts/alerts.yaml` (Prometheus rule format). Severity `page` = wake someone; `ticket` = next working day. Recipients are **undefined** (OQ-05). [VF] for expressions; [ASM] for thresholds.

| Alert | Condition | for | Sev | Why it exists |
|---|---|---|---|---|
| ApiHighErrorRate | 5xx / all > 2% | 10m | page | availability SLO |
| ApiLatencyP95High | p95 > 0.5 s | 10m | ticket | latency SLO (fixture p95 ≈ 9 ms single, ≈ 45 ms at 8 workers) |
| AuthDeniedSpike | > 1 /s sustained | 5m | ticket | credential stuffing or mis-set client |
| PolicyDeniedSpike | > 1 /s sustained | 5m | ticket | probing or role mapping fault |
| AiRateLimitHits | > 10 × 429 in 10m | 0m | ticket | abuse or a broken client loop |
| AiOutputLeakBlocked | any `output_policy_violation` in 15m | 0m | page | a model tried to emit a forbidden value |
| AiSchemaViolations | > 3 in 15m | 0m | ticket | model or prompt drift |
| AiFallbackRateHigh | fallback / AI requests > 20% | 15m | ticket | model quality or provider trouble |
| AiCircuitOpen | breaker not closed | 5m | ticket | provider failing; deterministic provider serving |
| AiLatencyP95High | p95 > 5 s | 10m | ticket | provider slow |
| AiSuggestionsRejectedHigh | rejects > 50% of decisions / day | 0m | ticket | usefulness or drift |
| AuditChainBroken | `audit_chain_valid == 0` | 0m | page | tampering or corruption |
| DataStale | load age > 25 h | 0m | ticket | daily batch missed |
| DataLoadMissing | age < 0 | 5m | page | no readable report |
| MetricsAbsent | no `http_requests_total` | 10m | page | service or scrape down |

## What was proven and what was not
- Proven: all 15 expressions parse with a PromQL parser; every metric, label and grouping label exists in the exposition produced by a workload that exercised ok, 404/422, 401, 403, AI deterministic, human decision, schema violation, output leak, provider down, rate-limited (429) and `/metrics`.
- Two label selectors matched no series in that workload: `status=~"5.."` (no server error occurred) and `abstained="true"`. They are syntactically and semantically valid; whether they fire is untested.
- **Not proven**: that any alert fires, that Alertmanager routes it, that anyone receives it. The first time these run on a real Prometheus is the test.
- `AiOutputLeakBlocked` is a `page` alert; with a leaking model it would page for every blocked output. The fallback has already protected the user, so the severity is a policy choice for the owner. Proposed, not decided.
