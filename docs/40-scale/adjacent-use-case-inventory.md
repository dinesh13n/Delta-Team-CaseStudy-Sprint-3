# Adjacent use case inventory

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (assessment; none validated) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Candidate | Fit with proven components | Extra risk | Readiness |
|---|---|---|---|
| Carrier exception triage summary | high: same gateway and data | carrier data sharing | medium |
| Route delay explanation | medium: needs route/time data (timestamps are invalid in the fixture) | data quality | low |
| Fleet maintenance prioritisation | low: no maintenance data | new data, new rules | low |
| Customer notification draft | medium | **outbound text to customers**: write access, privacy; needs a new threat model and agency review | do not start |
| Delivery evidence summary | medium | document/photo inputs, retrieval | low |
Nothing was tried on any of these. They are hypotheses ranked by overlap.
