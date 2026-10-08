# Personas

| Field | Value |
|---|---|
| Stage | B: Qualification, Stakeholders and Problem Framing (Spine 3) |
| Runbook step | B3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/domain-specific-spec.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Eight personas from `docs/domain-specific-spec.md` [VF]:
| Persona | Goal (ASM from the spec) | Key risk |
|---|---|---|
| dispatcher | assign work, resolve delays | acting on wrong record |
| warehouse_ops | hub scans, handling | duplicate or stale scan events |
| fleet_manager | vehicle readiness and capacity | stale vehicle data |
| driver | pickup and delivery | seeing others' locations |
| customs_agent | clearance | missing or wrong documents |
| customer_support | answer customers | unverifiable status |
| carrier_partner | booking confirmation | duplicate bookings, retries |
| ai_agent | automated assistant (non-human) | unbounded actions |
