# ADR-0010: Structured logs, metrics and traces-ready correlation

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
- **Context:** No telemetry (F-46).
- **Decision:** JSON logs with correlation id; /metrics in Prometheus text format; SLO definitions in docs; trace-context headers propagated so an OpenTelemetry collector can be added without code change.
- **Consequences:** Dashboards as code are specified, not hosted.
- **Evidence:** C6 root causes, C7 assessment, PRD requirements.
