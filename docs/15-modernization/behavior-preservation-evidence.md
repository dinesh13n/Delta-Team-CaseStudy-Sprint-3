# Behaviour preservation evidence

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H10 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL |
| Evidence sources | EVD-H-09, EVD-H-10, EVD-A-01 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## What was deliberately preserved
| Asset | Evidence it is preserved |
|---|---|
| `data/synthetic/*` bytes | `sha256sum -c evidence/00-preflight/EVD-A-01-baseline-file-manifest.sha256` (EVD-H-11-tg5-tg6.txt): 31 OK, 20 changed. All 20 are code/config/doc files deliberately modified in Stage H (list in the gate); every `data/synthetic/*`, `data/manifest.json` and `docs/domain-specific-spec.md` entry is OK |
| `/health` response body | probe P1 identical before and after |
| `scripts/sanity_check.py` original assertions | kept verbatim; extensions appended; `make smoke` passes (EVD-H-09) |
| Legacy ETL first output line `{'processed': 354, 'malformed': 1, ...}` | asserted in `tests/test_etl_quarantine.py` |
| Enum and status vocabulary in the data | not rewritten; flagged only |
| Legacy modules (`services/audit.py`, `services/domain_service.py`) | retained, marked legacy, still import cleanly |

## What changed and why it is safe
Every change maps to an approved-change ID in `approved-behavior-changes.md`. A change without an ID is a regression by rule; none was found.
