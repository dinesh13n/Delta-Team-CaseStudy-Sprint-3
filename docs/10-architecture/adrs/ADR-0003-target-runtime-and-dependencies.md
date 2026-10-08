# ADR-0003: Target runtime and locked dependencies

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
- **Context:** Pins fail on Python 3.14 (EVD-A-03c); httpx is undeclared; no lockfile (F-02, F-04). Operator asked for the latest Python.
- **Decision:** Target Python 3.14; supported 3.11 and 3.14 (CI matrix). Direct dependencies pinned in requirements.txt; fully hashed lock generated with uv (requirements.lock). Dev/test tools in requirements-dev.txt. httpx declared.
- **Consequences:** Reproducible installs; a deprecation watch on both interpreters.
- **Evidence:** C6 root causes, C7 assessment, PRD requirements.
