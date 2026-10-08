# ADR-0009: Container-based, platform-neutral deployment (resolves OQ-01 provisionally)

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
- **Context:** No platform chosen (OQ-01); no container or IaC (F-07, F-48).
- **Decision:** Package as an OCI image (non-root, health checks, read-only filesystem friendly); Terraform expressed for a generic container host; a specific cloud is chosen by the Architecture owner. Readiness only (OQ-20 default).
- **Consequences:** No real deployment evidence; release is rehearsed locally.
- **Evidence:** C6 root causes, C7 assessment, PRD requirements.
