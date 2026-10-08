# Operator exercises

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (defined) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Five practical exercises, scripted in `scripts/operator_exercises.py`, each on a clean copy of the source tree, using only documented commands and environment variables:

| # | Skill | Task | Pass condition |
|---|---|---|---|
| EX-1 | deploy | run the ETL, start the service with `APP_ENV=staging` and env-var configuration | `/health` 200, `/ready` 200 with fresh data, docs 404, authenticated read 200, unauthenticated 401 |
| EX-2 | observe | scrape `/metrics` with an ops token | request, AI, policy-denied, chain-valid, data-age and circuit series present; a dispatcher token is refused |
| EX-3 | diagnose | reconstruct an AI request by correlation id from the audit file | chain valid; event, actor and data load found |
| EX-4 | roll back | kill switch restart; edit the prompt, observe refusal to start, restore, restart | AI 503 with core 200; edited prompt refused; AI 200 after restore |
| EX-5 | recover | backup, destroy, restore, compare | all restore checks pass |
