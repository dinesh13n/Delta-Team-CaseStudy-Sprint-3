# ADR-0002: Supersedes ADR-0001 (partial modernisation, never revisited)

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
- **Context:** ADR-0001 kept legacy batch jobs beside the new API and recorded that business rules and audit behaviour now differ across code paths. It was never revisited (F-53).
- **Decision:** One domain core owns identity, validation, access and audit rules. The API and the batch/ETL entry points are thin adapters over the same core and the same semantic layer. Legacy scripts are retained only as thin wrappers (for compatibility) and are retired by trigger, not by deletion: legacy/reconcile_legacy.py is retired when the curated-layer reconcile command reaches count parity for two consecutive runs. ADR-0001 gets a supersession note in Stage H.
- **Consequences:** Single implementation of each rule. Coexistence rules in docs/14-transformation/coexistence-strategy.md.
- **Evidence:** C6 root causes, C7 assessment, PRD requirements.
