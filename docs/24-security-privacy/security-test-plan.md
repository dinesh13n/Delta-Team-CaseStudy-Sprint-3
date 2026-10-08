# Security test plan

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | tests, .github/workflows |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Level | What | How often | Tool |
|---|---|---|---|
| Unit/API security | 25 tests in `tests/test_security_suite.py` (identity, tampering, injection, disclosure, DoS, audit) | every commit (CI job `test`) | pytest |
| Human control | 9 tests | every commit | pytest |
| AI safety | 192 evaluation cases | every commit that touches `apps/api/ai` or the prompts; before release | `evaluation/run_eval.py` |
| Secret scan | whole tree | every commit, pre-commit hook | `test_secret_scan.py` |
| Dependency scan | requirements | weekly and on change | pip-audit (M1) |
| Red team | 12 attacks, baseline vs build | before release | `scripts/red_team.py` |
| Browser flow | operations view end to end | before release | Playwright (not yet run via npx) |

K-X5: automation is present as tests and CI configuration (`.github/workflows`); the CI has never executed on GitHub.
