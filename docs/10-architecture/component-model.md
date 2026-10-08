# Component Model

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

| Component | Responsibility | Package (planned) |
|---|---|---|
| API | HTTP, auth dependency, correlation, error mapping | apps/api |
| Config | environment settings, secrets handling | apps/api/config.py |
| Identity | token verification, principal | apps/api/security |
| Policy | decisions from access semantics | apps/api/policy |
| Repository | curated data access | apps/api/data |
| Intake | validation, quarantine, report | etl |
| AI gateway | context, provider, validation, fallback, accounting | apps/api/ai |
| Audit | event build, chain, verify | apps/api/audit |
| Telemetry | logs, metrics | apps/api/telemetry |
