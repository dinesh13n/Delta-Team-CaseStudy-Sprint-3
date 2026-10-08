# Data intake, validation and quarantine

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/09-initial-prd/functional-requirements.md; openapi.yaml |
| Assumptions | See body |
| Unresolved issues | See spec-readiness.md |
| Residual risks | Provisional |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**Behaviour.** ETL reads the immutable fixture, applies rules in `business-rules.yaml` and DQ-01..DQ-09, writes curated rows (with load_id, source_file, source_row) and quarantine rows (with rule id and original row). Prints and writes a JSON report: processed, curated, quarantined by rule, duplicates, multiple active carrier bookings per shipment. Exit code 0 if quarantine ratio <= 5% (DQ-09), else 1. The fixture is never modified; a run is idempotent for the same input (same hash).
**State.** Load runs are versioned by load_id (UTC timestamp + input hash).

**Requirements.** FR-06, FR-07, FR-08. **Findings addressed.** F-33, F-34, F-35, F-36, F-37, F-38, F-40, F-41, F-54. **Acceptance criteria.** see `../acceptance-criteria.md`.
