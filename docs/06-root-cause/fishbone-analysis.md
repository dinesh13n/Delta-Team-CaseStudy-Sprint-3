# Fishbone Analysis

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 6 root cause) |
| Runbook step | C6 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/07-repo-assessment/baseline-behaviour.md; docs/05-current-state/; EVD-C-02, EVD-C-03, EVD-C-05; docs/ADR in subtree |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Effect: operational information cannot be trusted or proven.
| Category | Causes |
|---|---|
| Process | no change control; no data intake process; no incident process (F-08, F-40, F-56) |
| People | no named owners; single-operator engagement (OQ-05) |
| Policy | OPA policy role-only and unused (F-21); no retention policy |
| Data | seeded defects; polluted enums; no keys constraints (F-33..F-38) |
| Technology | file storage; header auth; simulated AI; thin tests (F-17, F-29, F-51) |
| Organisation | overlapping ownership across three generations (ADR-0001) |
| Architecture | no layering, no contracts, no telemetry |
