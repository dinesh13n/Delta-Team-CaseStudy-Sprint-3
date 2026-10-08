# Baseline Behaviour

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 5-7) |
| Runbook step | C2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-C-02 |
| Assumptions | See body |
| Unresolved issues | Independent intended-versus-defect ruling by an owner (UNRESOLVED) |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Quick start executed verbatim (Step C2)
Run on a **copy** of the as-delivered subtree (original untouched), Python 3.11.16, fresh venv. Full transcript: `evidence/07-repo-assessment/EVD-C-02-quickstart-transcript.txt`.

| Command (README) | Result | Exit | Finding |
|---|---|---|---|
| `python -m venv .venv` | ok | 0 | |
| `pip install -r requirements.txt` | ok, pinned versions install on 3.11 | 0 | |
| `pytest -q` | **fails at collection**: `RuntimeError: The starlette.testclient module requires the httpx package` | 2 | F-02 confirmed |
| `python etl/run_daily_batch.py --sample` | prints `{'processed': 354, 'malformed': 1, 'sample': True}` | 0 | F-40 (defect counted, exits 0) |
| `uvicorn apps/api.main:app --reload` | **fails**: `ModuleNotFoundError: No module named 'apps/api'` (reloader kept running until the 15 s timeout, exit 124 is the timeout) | 124 | F-03 confirmed |

## Intended legacy behaviour versus defects
| Behaviour | Class |
|---|---|
| `/health` returns static ok | defect scheduled for change (F-46) |
| Unknown record returns first row | defect (F-32) |
| `REC-0001` resolves to first shipments row | defect (F-30) |
| Role from header, default operator | defect (F-17) |
| ETL tolerates and counts blank rows | intended legacy behaviour to be preserved as counting, defect for discarding (F-40) |
| AI summary returns templated string | intended placeholder (F-29) |

[VF] pip installed pinned packages on Python 3.11; on 3.14 the pin `pydantic==2.8.2` does not build (EVD-A-03c).
