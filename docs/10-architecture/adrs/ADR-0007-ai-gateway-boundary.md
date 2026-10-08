# ADR-0007: Governed model gateway with deterministic fallback

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
- **Context:** Prompt built by str.format of the whole record, no schema, no gate (F-22..F-26).
- **Decision:** Model access goes through a ModelProvider port. Context builder uses the allow-list; output validated against a schema with abstention; deterministic provider is default and the fallback; a suggestion is never an action; approval record required. Real providers are adapters selected by configuration (OQ-02).
- **Consequences:** Second-model comparison needs two configured providers (BLOCKED until models are named).
- **Evidence:** C6 root causes, C7 assessment, PRD requirements.
