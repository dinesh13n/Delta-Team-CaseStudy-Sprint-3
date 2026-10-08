# Final operating boundaries

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/37-operating-model; docs/23-human-control |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Allowed: read, summarise, record a human decision, report. Not allowed: any change to shipments, routes, bookings; any AI call to an external model (no egress configured); any real personal data; production use. Kill switches: `AI_ENABLED=false`; prompt and model locks; audit verification before release. Incident: `docs/29-incident-bcdr` (author-tabletop only).
