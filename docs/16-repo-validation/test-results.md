# Test results (H11)

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H11 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-H-09, EVD-H-11-pytest-coverage, EVD-H-04 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Suite | Python 3.14.7 | Python 3.11 |
|---|---|---|
| Whole suite | 86 passed, 7 xfailed (approved changes), 1 warning (httpx deprecation in Starlette TestClient) | 86 passed, 7 xfailed |
| Characterization | 5 passed, 7 xfailed (strict) | same |
| Rego (OPA 1.21.1) | 7/7 PASS | n/a |
| Policy parity (Python vs Rego, full grid) | pass (inside the 86) | pass |
| Smoke (`scripts/sanity_check.py`) | `status: ok`, `rego_current: True`, `openapi_route_diff: clean` | n/a |

[VF] Coverage on `apps` + `etl`: **96%** (1127 statements, 50 missed) versus baseline 45% (EVD-C-03). Uncovered lines are error branches in `ai/gateway.py` (12), `main.py` (12) and the two legacy shims. Raw: `EVD-H-11-pytest-coverage.txt`.
[INF] 96% line coverage does not equal behavioural coverage; the model path is exercised only through the deterministic provider.
