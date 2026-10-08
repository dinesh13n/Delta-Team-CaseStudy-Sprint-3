# Deployment strategy

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (design only) |
| Evidence sources | Dockerfile; apps/api/main.py /ready; docs/28-resilience |
| Assumptions | See body |
| Unresolved issues | shared audit store |
| Residual risks | N-R-10 single replica = single point of failure |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Chosen shape
Single container, single replica initially, rolling replacement with the health endpoints as gates: `/health` (liveness, no dependencies) and `/ready` (data present, optionally fresh, audit writable). The Dockerfile carries a HEALTHCHECK on `/health`.

## Why not more
- Audit is a local hash-chained file: **two replicas writing one file would fork the chain**. Multi-replica needs a shared audit store design first (backlog, DEBT-N3-01). Until then, one replica, `Recreate` strategy rather than overlapping rolling.
- No canary tooling or traffic split exists. A canary is replaced by "AI off first, data/API first" staged enablement.
- Blue/green needs two audit paths and a switch; not designed.

## Order of enablement
`AI_ENABLED=false` → verify reads and policy → enable AI (deterministic) → enable model provider only after TEVV on that model.

## Data
Run ETL before the API starts; the API refuses readiness without published data. ETL publishes atomically, so a failed run leaves the last good load.
