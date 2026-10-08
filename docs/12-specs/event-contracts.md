# Event contracts

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | openapi.yaml; schemas/; docs/09-initial-prd; docs/10-architecture; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; open items in docs/12-specs/spec-readiness.md |
| Residual risks | Specs are PROVISIONAL until OQ-01/02/03/05/11 are ruled |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

No message broker exists [VF]; "events" are (a) the tracking and operational event records in `events.jsonl` and `tracking_events.csv`, (b) audit events, (c) log lines.
| Event | Producer | Schema | Mandatory fields |
|---|---|---|---|
| operational event | API/ETL | semantic-layer DC-event | event_id, business_entity, event_type, severity, correlation_id (non-empty for all new events, closes F-42 going forward), actor, latency_ms, cost_units, payload_hash |
| audit event | API | `schemas/audit-event.schema.json` | see F-43 |
| log line | all | JSON: ts, level, msg, correlation_id, route, status, latency_ms | |
Ordering: audit events are totally ordered by the hash chain. Delivery: local append, at-least-once is not applicable. Historical events with a null or empty correlation id (1,992 of 3,000) are never rewritten; they are flagged in the curated layer.
