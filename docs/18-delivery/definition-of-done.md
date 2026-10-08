# Definition of Done (evidence-bearing)

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

A work item is done only when **all** hold:
1. Code merged through a PR with CODEOWNERS review (or, pre-protection, the commit is tagged).
2. Tests pass on Python 3.14 and 3.11; ruff, mypy clean; coverage not reduced.
3. A **named evidence artifact** exists under `evidence/<NN>/` and is registered in that directory's `MANIFEST.md` with SHA-256, command, UTC time and operator.
4. The traceability row (finding -> requirement -> spec -> test -> evidence) is updated.
5. Behaviour changes carry an approved-change ID, a flag or revert path, and a test.
6. Unknowns are labelled [UNK]/[ASM]; nothing is reported PASS without a run.
A passing test without registered evidence does **not** meet this definition.
