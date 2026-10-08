# API implementation map

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-H-09 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Operation | Role needed | Audit action | Notes |
|---|---|---|---|
| GET /health | none | n/a | liveness (preserved from baseline) |
| GET /ready | none | n/a | data layer readiness |
| GET /metrics | `ops` platform role | n/a | Prometheus text |
| GET /shipments | persona with shipments:read | shipment.list | paging, status filter, field mask |
| GET /shipments/{id}/events | tracking_events:read | event.list | 404 if shipment missing |
| GET /records/{id} | shipments:read | record.read | 422 bad key, 404 missing |
| POST /ai/summarize/{id} | shipments:read + AI policy | ai.summary | rate limit, kill switch |
| POST /ai/summaries/{id}/decision | shipments:write | ai.decision | 409 on second decision |
| GET /audit/verify | `auditor` platform role | n/a | chain check |
| GET /kpis | persona | n/a | K1..K8 computed; K9/K10 data_gap |
Contract: `data/contracts/openapi.yaml`; drift gate in `make smoke` and tests. `/ops` is a static mount and not part of the API contract.
