# Data contracts

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-A-04b data profile; EVD-C-05 profile; semantic-layer/entities.yaml |
| Assumptions | See body |
| Unresolved issues | OQ-14 ruling provisional; approvers UNRESOLVED |
| Residual risks | See data-context-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Contracts follow the six entities in `semantic-layer/entities.yaml`: shipments, tracking_events, vehicles, routes, carrier_bookings, ai_invocations, plus the event record from events.jsonl.
| Contract | Source | Key | Consumers | Notes |
|---|---|---|---|---|
| DC-shipments | shipments.csv | shipment_id | API, AI gateway, KPIs | first column in file is shipment_id (value REC-nnnn) |
| DC-tracking_events | tracking_events.csv | event_id | API, KPIs | confidence must be in [0,1] |
| DC-vehicles | vehicles.csv | vehicle_id | API | |
| DC-routes | routes.csv | route_id | API | |
| DC-carrier_bookings | carrier_bookings.csv | booking_id | API | retry_count policy check |
| DC-ai_invocations | ai_invocations.csv | ai_call_id | audit/FinOps | |
| DC-event | events.jsonl | event_id | audit, observability | correlation_id mandatory for new events |
Each contract: field list, types, nullability, enum domain and sensitivity come from the YAML; breaking changes need a version bump and ADR. Quarantine contract DC-quarantine: original row, rule id, load_id, source_file, source_row. Curated rows add load_id.
