# Test Overview

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0A pre-flight discovery |
| Runbook step | A4 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, pending Transformation Lead review |
| Evidence sources | EVD-A-04-repo-tree-annotated.txt; EVD-A-04b-data-profile.txt; direct file reads of the repository; evidence/00-preflight/EVD-A-03c-runtime-upgrade-compat.txt |
| Assumptions | See assumptions-unknowns.md |
| Unresolved issues | See assumptions-unknowns.md |
| Residual risks | Read-only discovery only; no behavioural run yet (Stage C) |

Classification key: **[VF]** Verified Fact (read in a cited file), **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown. Paths are relative to `07-logistics-shipment-fleet-routing-ops/`. This document makes no transformation recommendations (Spine 0A).

## 1. Tests present
| Test | Type | What it asserts |
|---|---|---|
| `tests/test_api_contract.py::test_health_contract` | API | `/health` returns 200 and `status == ok` |
| `tests/test_api_contract.py::test_ai_summary_has_minimum_contract` | API | `/ai/summarize/REC-0001` returns 200 with `summary`, `model`, `guardrail_status` keys |
| `tests/test_characterization.py` | Characterisation | unknown id returns a non-empty dict (documents the first-row fallback) |
| `tests/playwright/operations.spec.ts` | UI | `/` loads and body visible; no runner, no server, no browser config |
| `scripts/sanity_check.py` (`make smoke`) | Fixture | file presence, CSV row counts equal `manifest.json`, event count 3000 |

## 2. Observations
- [VF] 3 pytest tests in total. None covers `/records/{id}`, authorisation outcomes, the ETL, the legacy script or the audit log.
- [VF] `test_api_contract.py` needs `httpx` which `requirements.txt` omits; pytest also is not installed in the sandbox, so tests were not run (not executed in Stage A).
- [VF] `sanity_check.py` fails if row counts differ from 354 or events from 3000, so it breaks if the fixture is cleaned.
- [VF] CI runs only `pytest -q` (`ci.yml`); no lint, type check, coverage, security scan or Playwright.
- [UNK] Current pass/fail status; established in Stage C.
