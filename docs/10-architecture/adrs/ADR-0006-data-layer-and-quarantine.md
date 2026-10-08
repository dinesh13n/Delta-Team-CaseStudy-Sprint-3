# ADR-0006: Curated layer derived from an immutable fixture (rules OQ-14)

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
- **Context:** sanity_check.py asserts exact fixture counts (F-54); defects must be remediated without editing the fixture.
- **Decision:** data/synthetic stays immutable. An intake pipeline validates it with the semantic rules and writes data/curated/<version>/ (valid rows) and data/quarantine/<version>/ (invalid rows with reasons) plus a run report. The API reads only the curated layer through a repository port.
- **Consequences:** Row counts differ between layers by design and are reported.
- **Evidence:** C6 root causes, C7 assessment, PRD requirements.
