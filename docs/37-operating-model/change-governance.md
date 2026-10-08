# Change governance

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (mechanisms in repo) / CONDITIONAL (reviewers) |
| Evidence sources | docs/14-transformation/transformation-gates.md; .github/CODEOWNERS |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | HC / TEVV-R-01 self-review |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Change | Gate |
|---|---|
| Code | pull request template, CODEOWNERS, CI (ruff, format, mypy, secrets, tests, coverage floor, OPA parity), reviewer ≠ author (**today the same agent wrote and reviewed everything**) |
| Prompt | edit + `scripts/lock_prompts.py` + review of the lock; the service refuses to serve a mismatched prompt |
| Model | `models.lock.json` entry + evaluation at thresholds + red team re-run |
| Access policy | YAML change → regenerated Rego → parity test → Security Owner approval |
| Data contract | Data Owner ruling recorded in the decision log |
| KPI definition | **frozen**; a change is a new version with a new baseline, never an edit |
| Evidence | append-only manifests; superseded files kept |
Branch protection requiring review: **not applied** (never pushed to a protected repository).
