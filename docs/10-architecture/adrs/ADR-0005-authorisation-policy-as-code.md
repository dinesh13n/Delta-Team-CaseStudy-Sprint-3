# ADR-0005: Contextual authorisation from the semantic layer

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

- **Status:** Proposed, PROVISIONAL (owner UNRESOLVED)
- **Date:** 2026-10-08
- **Context:** Role-only allow-list (F-18) and an unused Rego file (F-21).
- **Decision:** access-semantics.yaml is the single source. A runtime policy engine evaluates persona x entity x field x purpose x scope with deny by default and returns an explainable decision. A Rego policy is generated from the same file and tested with opa when available; a parity test compares decisions.
- **Consequences:** No second hand-written copy of the rules.
- **Evidence:** C6 root causes, C7 assessment, PRD requirements.
