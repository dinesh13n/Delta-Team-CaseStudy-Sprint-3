# Critical Workflow Inventory

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 7 repository assessment) |
| Runbook step | C7 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | C2-C6 documents; runbook/01-BASELINE-ASSESSMENT.md findings register; direct reading of the subtree |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Behaviour that must be preserved or deliberately changed (judged in H10):
| ID | Workflow | Preserve / Change |
|---|---|---|
| W1 | `/health` returns `{"status":"ok","repo":...}` with 200 | Preserve contract; extend with readiness |
| W2 | `/records/{id}` returns the matching shipments row | Preserve for a valid id |
| W3 | Unknown id returns first row | Change to 404 (approved defect fix) |
| W4 | `/ai/summarize/{id}` returns summary, model, guardrail_status, recommendation, token fields | Preserve keys; add governance fields |
| W5 | `run_daily_batch --sample` prints processed/malformed counts | Preserve counts; add quarantine |
| W6 | `make smoke` passes on the delivered fixture | Preserve, decouple from exact counts (F-54) |
| W7 | Audit line per read and per AI call | Preserve; add actor and correlation |
