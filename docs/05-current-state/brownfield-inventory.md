# Brownfield Inventory

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

| Area | Items | Source |
|---|---|---|
| Code | 6 Python modules + sanity script (about 140 lines) | tree |
| Tests | 3 pytest, 1 Playwright spec | tests/ |
| Data | 6 CSV x 354 rows, 3,000 events | data/ |
| Docs | 10 short markdown files, 1 ADR | docs/ |
| Config | .env.example, pyproject, CI, Makefile | root |
| Stubs | Terraform, OPA, OpenAPI fragment | infra, policy, data/contracts |
Three engineering generations (legacy, FastAPI, AI) per docs/architecture/current-state.md.
