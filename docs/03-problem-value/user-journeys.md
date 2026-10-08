# User Journeys

| Field | Value |
|---|---|
| Stage | B: Qualification, Stakeholders and Problem Framing (Spine 3) |
| Runbook step | B3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/domain-specific-spec.md; A4 workflow-overview |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

The four declared flows [VF spec]: (1) Booking to pickup, (2) Hub scan to route assignment, (3) Carrier booking saga, (4) Exception investigation to delivery evidence.

Journey 4 as the reference journey: exception raised -> requester identified -> correct shipment record located -> related events and bookings shown -> decision made -> decision recorded with actor and request identifier -> evidence retrievable. Pain points today [VF A4]: wrong record may be returned, identity is self-declared, trail lacks actor.
