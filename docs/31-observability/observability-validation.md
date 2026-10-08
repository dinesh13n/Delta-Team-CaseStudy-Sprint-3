# Observability validation

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (repo level) / CONDITIONAL (production) |
| Evidence sources | evidence/31-observability/EVD-N-01-observability-validation.json (SHA-256 b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | N-R-01 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## What was run [VF]
`python -m scripts.validate_observability workload` (application interpreter, Python 3.14) then `... check` (scan interpreter with promql-parser). Evidence: `EVD-N-01-observability-validation.json` (SHA-256 `b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485`); full suite `EVD-N-01-full-suite.txt` (SHA-256 `dcd4e5b0fa68b3dfb016e6b78802228458437b48d4f3d1de44da866debd0c916`).

| Check | Result |
|---|---|
| Alert + dashboard expressions parsed | 31 of 31 |
| Metric names referenced exist in live exposition | 31 of 31 (after fix) |
| Label names and grouping labels exist | 31 of 31 |
| Required families exported | 13 of 13 |
| Workload paths exercised | ok, 422, 401 ×2, 403, AI deterministic, human decision, schema/invalid output, output leak, provider down ×2, 429 ×2, `/metrics` |
| Test suite | 170 passed, 7 xfailed; coverage 97% (apps + etl); ruff, format, mypy clean |

## Defects the validation found
1. `ai_guardrail_blocked_total` absent until first increment, so a first-event alert would be missed. Fixed by zero-initialisation; first validation run FAILED 2 rules on this, final run 0 failed.
2. The leak path uses a different counter than the playbook assumed. Documented; alert uses the right one.

## What this does not show
- No alert fired, no dashboard rendered, no collector scraped. These are the production unknowns.
- The workload ran in-process with a test client; real network behaviour is untested.
- Thresholds are not tuned.

Gate (N-X1, partial): metrics, alerts and dashboards exist as code and agree with the code. Gate is CONDITIONAL until a collector scrapes a deployed instance (blocked by OQ-01).
