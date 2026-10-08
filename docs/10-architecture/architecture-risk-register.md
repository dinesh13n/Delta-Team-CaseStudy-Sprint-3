# Architecture Risk Register

| Field | Value |
|---|---|
| Stage | F: Target Architecture, Data and Context Strategy, Specs, Traceability (Spine 10) |
| Runbook step | F1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/09-initial-prd/; docs/06-root-cause/; docs/07-repo-assessment/; semantic-layer/access-semantics.yaml; subtree docs/architecture/target-state-principles.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Risk | Mitigation |
|---|---|---|
| AR-1 | Policy engine bug locks everyone out | deny-by-default tests, parity test, break-glass is not provided; rollback via flag |
| AR-2 | Curated layer drifts from semantic layer | tests tie them together |
| AR-3 | Local audit file tamperable | hash chain verifier, external sink adapter |
| AR-4 | Python 3.14 ecosystem gaps | CI matrix with 3.11 |
| AR-5 | Model outage | deterministic fallback |
