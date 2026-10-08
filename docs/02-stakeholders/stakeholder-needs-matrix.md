# Stakeholder Needs Matrix

| Field | Value |
|---|---|
| Stage | B: Stakeholders (Spine 2) |
| Runbook step | B2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/*; docs/00-preflight/operating-contract/*; docs/00-preflight/stage-a-gate.md; docs/01-engagement/* |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-05 |
| Residual risks | No independent approver exists |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Needs are [INF] from role names and findings; none was elicited from a real person.
| Role | Need | Concern | Evidence link |
|---|---|---|---|
| Dispatcher | Correct shipment record on first lookup | Wrong record returned silently | F-31, F-32 |
| Warehouse ops | Reliable event ordering and duplicates removed | duplicate_tracking_events | known-gaps.md |
| Fleet manager | Vehicle and route data that respect restrictions | route_ignores_restrictions | known-gaps.md |
| Driver | Privacy of own location | location_data_overexposure | threat-model.md |
| Customs agent | Customs flags reliable | blank/duplicate rows | A4 data profile |
| Customer support | Trace of what happened and why | audit gaps | F-43 |
| Carrier partner | No duplicate bookings or retry storms | duplicate_carrier_booking | known-gaps.md |
| Security Owner | Real authentication, no hard-coded secrets | F-09..F-21 | A4 |
| Compliance Owner | Obligations mapped, retention defined | OQ-04, OQ-10 | |
| CTO | A defensible readiness decision with evidence | unsupported claims | rubric |
