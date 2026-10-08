# AI versus No-AI Matrix

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

| ID | Decision | Justification | Rejected alternatives |
|---|---|---|---|
| I1 | **No AI**: deterministic lookup by exact key | exact-match problem; no uncertainty or language | model-assisted fuzzy match (unsafe: wrong-record risk) |
| I2 | **No AI**: policy as code | decision must be explainable, repeatable, auditable | model-based risk scoring (unexplainable) |
| I3 | **No AI**: rules engine from the semantic layer | defects are deterministic (duplicates, ranges, patterns) | ML anomaly detection (adds false positives to a rule-solvable problem) |
| I4 | **No AI**: idempotency key and at-most-one-active rule | invariant, not prediction | agentic retries (caused the retry storm risk) |
| I5 | **No AI (rejected)**: boolean rule on restricted_zone_flag | a safety constraint must never be probabilistic | GenAI route checking |
| I6 | **No AI**: structured audit with hash chain | evidence must be exact | AI-generated audit summaries as evidence |
| I7 | **Deferred / no AI now**: use the stored route estimate; classical forecasting only if real history exists | fixture values are random; no labelled history; AI benefit unprovable | GenAI ETA (hallucination risk), classical ML (no valid training data) |
| I8 | **Deferred / no AI now**: deterministic rules plus existing estimates; classical optimisation only with real constraints | needs real network data | GenAI route generation (rejected: cannot guarantee constraints) |
| I9 | **GenAI retained, bounded**: single call, read-only suggestion, human approval, deterministic fallback summary | free-text synthesis of heterogeneous events is the one language task here | rule-based templates only (kept as fallback); agentic workflow |
| I10 | **Rejected** | minimum agency principle; no tool authority needed | agent with tools (OQ-18 undecided, default: out) |
