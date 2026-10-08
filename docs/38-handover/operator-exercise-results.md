# Operator exercise results

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (P-X2 not met: author-run) |
| Evidence sources | evidence/38-handover/EVD-P-02-operator-exercises.json (SHA-256 0482bd0cf4b1edf59e04ea08f2b7ab4a6ba2d2d45fc2e423b430b1e3be6780ab) |
| Assumptions | See body |
| Unresolved issues | receiving team |
| Residual risks | P-R-02 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Run 2026-10-08 by the author from a clean copy. Evidence: `EVD-P-02-operator-exercises.json` (SHA-256 `0482bd0cf4b1edf59e04ea08f2b7ab4a6ba2d2d45fc2e423b430b1e3be6780ab`).

| # | Result | Observed |
|---|---|---|
| EX-1 deploy | PASS | ETL exit 0; /health 200; /ready 200; /docs 404; read 200; no token 401 |
| EX-2 observe | PASS | all six series present; dispatcher refused on /metrics (403) |
| EX-3 diagnose | PASS | chain valid; `ai.summary` for SHI-00027 found by correlation id |
| EX-4 roll back | PASS | AI 503 and core 200 when off; edited prompt refused at start; AI 200 after restore |
| EX-5 recover | PASS | backup/restore checks all true from the clean copy |

## What the exercise found
1. The first clean-copy attempt failed: the service reads `data/contracts/*.schema.json` at run time, and the copy omitted it. The same gap exists in the container recipe, which also looked for `semantic-layer` inside the app directory (it is one level above) and never ran the ETL before serving. **Dockerfile, entrypoint, dockerignore and compose were corrected** (build still not run: no container runtime).
2. The first run of the harness crashed on a connection error with no diagnostic; it now raises the server's output if the process dies.

## P-X2 verdict
"The receiving team demonstrated deploy, observe, diagnose, rollback and recover" is **not met**: there is no receiving team, and the author running its own exercises shows the procedures work, not that others can follow them.
