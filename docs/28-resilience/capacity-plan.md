# Capacity plan

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (single-process measurement only) |
| Evidence sources | evidence/28-resilience/EVD-M-02-load-probe.json |
| Assumptions | See body |
| Unresolved issues | traffic figures |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Measured (one process, loopback, 2 vCPU sandbox-class host, deterministic provider, 354 rows per entity)
Evidence: `evidence/28-resilience/EVD-M-02-load-probe.json`.

| Request | Workers | Throughput | p50 | p95 | p99 |
|---|---|---|---|---|---|
| GET /records/{id} | 1 | 189 rps | 5.0 ms | 6.3 ms | 8.2 ms |
| GET /shipments?limit=100 | 1 | 146 rps | 6.5 ms | 8.7 ms | 10.5 ms |
| POST /ai/summarize/{id} | 1 | 161 rps | 5.9 ms | 7.7 ms | 8.8 ms |
| GET /records/{id} | 8 | 244 rps | 30.2 ms | 33.6 ms | 35.1 ms |
| GET /shipments?limit=100 | 8 | 188 rps | 39.7 ms | 44.7 ms | 47.0 ms |
| POST /ai/summarize/{id} | 8 | 200 rps | 37.5 ms | 42.2 ms | 43.8 ms |

All 2400 requests returned 200. The AI row exercises the deterministic provider including audit append, approval registration and metrics.

## What this does and does not say
- [VF] One process saturates at roughly 200-250 rps on this host; latency is queueing-dominated beyond a few concurrent clients (single event loop plus synchronous handlers on a thread pool).
- [VF] Record lookup scans a list in memory (O(n)); at 354 rows it is negligible. The data growth path is a database index (not designed here).
- [INF] The E2 envelope (AI p95 ≤ 3,000 ms) leaves large headroom for the *service*; all the budget belongs to a future model call.
- [UNK] Real traffic volume, user count, data size: no figure was provided. No sizing for a deployment can be derived.
- Rate limiting is per process (30/min per subject by default).

## Limits to watch
CSV files are loaded fully into memory per entity; the AI trace and audit files grow without rotation (retention policy is a proposal).
