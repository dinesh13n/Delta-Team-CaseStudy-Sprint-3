# Scope and Exclusions

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

**In scope:** one complete trustworthy path for exception investigation (flow 4) end to end, plus the data and control foundations it needs (identity, record lookup, audit, correlation).
**Out of scope for the MVP (proposed):** full booking, routing optimisation and ETA prediction; real production data; real carrier integrations.
**Undecided:** operator portal (OQ-06), agentic behaviour (OQ-18), regulated-data handling (OQ-04, OQ-21).
