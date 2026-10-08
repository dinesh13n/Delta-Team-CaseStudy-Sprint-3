# Current Process Map

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 5 current state) |
| Runbook step | C4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/00-preflight/discovery/; evidence/05-current-state/EVD-C-04-flow-to-code-trace.md |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Actors (spec personas) -> steps -> systems, as implemented:

1. Requester (any caller) sends `GET /records/{id}` with a self-declared role header -> API allow-list check -> CSV scan -> row returned (first row if none match) -> audit line appended (no actor).
2. Requester sends `POST /ai/summarize/{id}` (no role check) -> same lookup -> simulated summary -> audit line.
3. Scheduler/operator (manual) runs `etl/run_daily_batch.py` or `legacy/reconcile_legacy.py` -> counts rows -> prints.
There are no queues, handoffs, approvals or notifications in code [VF].
