# Business Requirements

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

| ID | Requirement | Source |
|---|---|---|
| BR-1 | A request for a shipment returns exactly that shipment or a clear not-found | problem statement, F-31/F-32 |
| BR-2 | Every action records who acted, on what, when, and under which approval | F-43 |
| BR-3 | Events for one business case can be linked together | F-42 |
| BR-4 | A shipment is never booked twice with a partner by accident, and retries are bounded | F-38, F-39 |
| BR-5 | Records meet defined quality rules or are held aside with a reason | F-33..F-37 |
| BR-6 | Advice given to staff is bounded, labelled, reviewable and never acted on without a recorded human decision | challenge guide ch. 9 |
| BR-7 | Personal location data is exposed only where an operational purpose exists | location_data_overexposure |
| BR-8 | Cost of handling can be tied to shipments | F-57, domain spec |
| BR-9 | The environment can be rebuilt by a new team from documented steps | challenge 5 |
