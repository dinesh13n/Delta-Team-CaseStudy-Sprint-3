# Knowledge model

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | semantic-layer/relationships.yaml, ai-context-policy.yaml |
| Assumptions | See body |
| Unresolved issues | Owners UNRESOLVED |
| Residual risks | See data-context-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Entities (6): shipments, tracking_events, vehicles, routes, carrier_bookings, ai_invocations, plus the event record. Relationships per `relationships.yaml` [VF]: tracking_events, carrier_bookings and ai_invocations reference shipments.shipment_id (many-to-one); shipments.customer_id and vehicles.driver_id point to external masters that are not in the repo [VF]. There is no declared FK between shipments and routes or vehicles in the fixture [INF], which limits cross-entity rules (a declared gap). Business knowledge: glossary, status taxonomy, 25 business rules (6 declared gaps), 10 KPIs. No unstructured corpus exists [VF], so no RAG corpus is justified (retrieval-strategy). Knowledge ownership UNRESOLVED.
