# Intervention Options

| Field | Value |
|---|---|
| Stage | E: Intervention Qualification and Initial PRD (Spine 8-9) |
| Runbook step | E1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/03-problem-value/; docs/06-root-cause/; docs/07-repo-assessment/; semantic-layer/business-rules.yaml; docs/00-preflight/ai-economics/ |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Candidate interventions, each evaluated against: process/policy change, deterministic software, rules engine, workflow automation, analytics, classical ML, GenAI, agentic AI.

| ID | Intervention | Root cause | Findings |
|---|---|---|---|
| I1 | Return exactly the requested record or not-found | RC-2 | F-30, F-31, F-32 |
| I2 | Verified identity and contextual access decision | RC-2 | F-17..F-21 |
| I3 | Intake validation with quarantine | RC-3 | F-33..F-38, F-40 |
| I4 | Prevent duplicate carrier bookings | RC-3 | F-38, F-39 |
| I5 | Enforce restricted-zone route rule | RC-3 | semantic rule BR-06 |
| I6 | Correlated, attributable, tamper-evident audit | RC-1 | F-42..F-45 |
| I7 | ETA prediction | declared, unimplemented | F-29 |
| I8 | Route optimisation | declared, unimplemented | F-29 |
| I9 | Exception copilot (summary and suggested next step) | declared, simulated | F-22..F-29 |
| I10 | Autonomous multi-step exception handling | not declared | OQ-18 |
