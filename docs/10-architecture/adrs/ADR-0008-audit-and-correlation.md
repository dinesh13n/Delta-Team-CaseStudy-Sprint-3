# ADR-0008: Hash-chained audit with correlation ids

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
- **Context:** Audit has no actor or correlation id, and the sink is a local file the app can rewrite (F-43, F-44).
- **Decision:** Each request gets a correlation id (accepted or generated). Audit events carry actor, tenant, resource, policy decision, model and prompt version, input hash, approval id and the hash of the previous event. A verifier detects tampering. Storage is behind an AuditSink port: local file adapter now; an external append-only store on the chosen platform later.
- **Consequences:** Local file is evidence-grade only for tests and demos.
- **Evidence:** C6 root causes, C7 assessment, PRD requirements.
