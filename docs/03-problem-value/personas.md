# Personas

| Field | Value |
|---|---|
| Stage | B: Problem Framing (Spine 3) |
| Runbook step | B3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/*; docs/00-preflight/operating-contract/*; docs/00-preflight/stage-a-gate.md; docs/01-engagement/*; docs/domain-specific-spec.md (repo) |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-08, OQ-24 |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Source: eight names in docs/domain-specific-spec.md [VF]. Descriptions are [INF]; no persona was interviewed.
| Persona | Role in operations (inferred) | Main data touched |
|---|---|---|
| dispatcher | Assigns routes and responds to exceptions | shipments, routes, carrier_bookings |
| warehouse_ops | Handles hub scans and handoffs | tracking_events |
| fleet_manager | Manages vehicles and capacity | vehicles, routes |
| driver | Carries out pickups and deliveries | vehicles, tracking_events |
| customs_agent | Clears cross-border shipments | shipments (customs_required) |
| customer_support | Answers customer questions about status | shipments, tracking_events |
| carrier_partner | External party receiving bookings | carrier_bookings |
| ai_agent | Automated actor that prepares recommendations | ai_invocations |
