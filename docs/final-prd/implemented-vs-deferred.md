# Implemented versus deferred

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | requirement-disposition-matrix.md; residual-risks.md |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**Implemented**: see `final-capability-map.md` (Delivered rows).
**Deferred**: availability and AI latency/cost measurement (NFR-2, 9, 10); IdP; platform and IaC; tracing; external audit sink; four-eyes and approval expiry; bulkhead wiring; real model and portability test; ETA, route and copilot capabilities; owner rulings (BR-04, weight discrepancy, `REC-0001` intent); credential revocation; branch protection.
**Rejected**: Angular portal; agentic AI; audit v1 feature flag.
