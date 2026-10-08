# Jobs to Be Done

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

[INF] derived from persona names and business flows.
| Persona | Job | Success looks like |
|---|---|---|
| dispatcher | Find the right shipment and decide a route fast | Exact record or a clear not-found |
| warehouse_ops | Record scans in order without duplicates | One event per scan, ordered |
| fleet_manager | Match vehicles to loads within constraints | No restricted route assigned unflagged |
| driver | Complete a job with minimal exposure of personal data | Location shown only for operational need |
| customs_agent | Clear shipments with accurate flags | Flags consistent with the record |
| customer_support | Explain what happened | A trace with reasons |
| carrier_partner | Receive one clear booking | No duplicates or repeated retries |
| ai_agent (as actor) | Prepare a recommendation | Bounded, reviewable, never self-executing |
