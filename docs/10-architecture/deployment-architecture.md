# Deployment Architecture

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

OCI image, one process per container, config via environment, non-root, read-only root filesystem except a writable data volume for audit and curated layers, health and readiness probes, resource limits. Environments: local, ci, staging-equivalent (compose). Cloud target undecided (OQ-01).
