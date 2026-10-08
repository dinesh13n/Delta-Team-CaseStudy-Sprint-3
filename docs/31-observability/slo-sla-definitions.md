# SLO and SLA definitions

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (SLOs proposed; no SLA) |
| Evidence sources | evidence/28-resilience/EVD-M-02-load-probe.json; evidence/31-observability/EVD-N-01-observability-validation.json (SHA-256 b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485) |
| Assumptions | [ASM] targets are proposals |
| Unresolved issues | OQ-08 service owner and consumers |
| Residual risks | N-R-06 SLOs not ratified |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**No SLA is defined or offered.** An SLA is a commitment to a customer with consequences; no customer, contract or platform exists (OQ-01, OQ-08). The table below is proposed internal SLOs awaiting owner ratification. [ASM]

| SLO | Indicator | Target (proposed) | Window | Measurable today? |
|---|---|---|---|---|
| Availability | non-5xx / all requests (excluding 4xx) | 99.5% | 30 d | yes, from `http_requests_total` |
| Latency | p95 request duration | ≤ 500 ms | 30 d | yes, histogram |
| AI latency | p95 AI endpoint duration | ≤ 5 s | 30 d | yes; fixture value is milliseconds because the provider is deterministic, so this says nothing about a real model |
| AI safety | blocked leaks reaching a response | 0 | always | yes: leaks are counted when blocked; a leak that is NOT detected cannot be counted |
| Audit integrity | `audit_chain_valid` = 1 | 100% of scrapes | always | yes |
| Data freshness | load age ≤ 25 h | 99% of the time | 30 d | yes; threshold depends on an ETL schedule that does not exist (no scheduler) |
| Decision traceability | AI responses with a matching audit event | 100% | always | by reconstruction test, not by metric |

## Baseline from the fixture (load probe, one process, loopback) [VF]
Record lookup p95 6.3 ms (1 worker) and 33.6 ms (8 workers); AI summary p95 7.7 ms and 42.2 ms; throughput 145 to 244 rps. These show the application code is not slow. They are not capacity numbers for any deployment.

## Not measurable today
- Staleness of GPS positions: no timestamp in the source.
- Business outcomes (on-time delivery, exception resolution time): batch KPIs only, and the fixture is static.
- True user-perceived latency: loopback only.
