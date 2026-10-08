# Problem Statement

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

Operations staff who book, route, track and investigate shipments act on records that are sometimes the wrong record, sometimes duplicated or incomplete, and often cannot be linked to the events around them. When a shipment goes wrong, there is no reliable account of who did what, with which information, and on whose approval. Partner bookings can repeat without limit, and the cost of handling each shipment cannot be traced to the shipment. As a result, staff cannot be sure what they see is correct, managers cannot reconstruct decisions, and the business cannot show that its operations are controlled.

**Scope of the statement:** what must be true for operations to be trustworthy, traceable and controllable, regardless of how it is built.
