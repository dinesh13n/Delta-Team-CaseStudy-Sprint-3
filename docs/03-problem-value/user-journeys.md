# User Journeys

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

The four declared business flows [VF]; steps are [INF] and show where today's evidence breaks.
| Flow | Steps | Where it breaks today |
|---|---|---|
| Booking to pickup | request, book, assign, pick up | no booking logic exists in code |
| Hub scan to route assignment | scan, record event, assign route | duplicate events; restricted-zone flag not enforced (known-gaps) |
| Carrier booking saga | book, confirm, retry, compensate | duplicate bookings and retry counts in data; no saga code |
| Exception investigation to delivery evidence | detect, look up record, review advice, decide, evidence | wrong-record lookup; advice unverified; no decision trail |
