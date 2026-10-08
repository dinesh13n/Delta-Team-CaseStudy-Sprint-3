# Behaviour-difference report

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H10 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-H-10, EVD-H-05, EVD-C-08 (characterization) |
| Assumptions | See body |
| Unresolved issues | Approver ratification (OQ-05) |
| Residual risks | TR-02 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## 1. Method
[VF] The tag `baseline/v0.1-as-delivered-bytes` was extracted to a scratch worktree and run with its own dependencies (Python 3.11 venv). A fixed probe set (`~/fde/probe.py`, 9 probes, 18 request variants with and without a token) was run against the baseline and against the transformed app. The 12 Stage C characterization tests plus the 2 original tests were run against the transformed app. Raw results: `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv` and `evidence/15-modernization/EVD-H-05-behaviour-change.md`.

## 2. Characterization tests (Stage C8) against the transformed system
[VF] 14 tests: 5 passed unchanged, 7 now fail by design and are marked `xfail(strict)` with an approved-change ID (so an unexpected pass also fails the build), 2 original tests adapted for the new auth and still pass (see `test-results.md`). Zero unexplained failures.

| Test | Before (baseline) | After | Classification | Spec clause | Approver |
|---|---|---|---|---|---|
| test_records_without_role_header_succeeds | 200 with data | 401 problem+json | Approved change AB-03 | FR-03, AC-04, AC-05 | PROVISIONAL (D-009) |
| test_records_clinician_role_succeeds | 200 for a foreign-domain role | 403 (role not in persona set) | AB-04 | FR-04 | PROVISIONAL |
| test_unknown_role_is_forbidden_with_http_200 | HTTP 200 with `{"error":"forbidden"}` | 401/403 problem+json | AB-05 | FR-05, AC-07 | PROVISIONAL |
| test_ai_summary_without_any_role | 200 with summary | 401 | AB-06 | FR-03, AC-04 | PROVISIONAL |
| test_ai_guardrail_status_not_enforced | literal `not_enforced` | evaluated `enforced` or `blocked` | AB-07 | FR-11, AC-12 | PROVISIONAL |
| test_ai_summary_echoes_first_column | first column echoed | derived from allow-listed facts | AB-08 | FR-09, AC-12 | PROVISIONAL |
| test_audit_event_has_no_actor_or_correlation | ts, action, details only | v2 event with actor, correlation, policy decision, hash chain | AB-09 | FR-13, AC-18 | PROVISIONAL |
| 5 others (health, list shape, record shape for a valid id, original sanity/ETL first-line, etc.) | pass | pass | PRESERVED | n/a | n/a |

## 3. Probe differences (18 variants)
See the CSV. Summary:

| Behaviour | Before | After | Class |
|---|---|---|---|
| /health | 200 | 200, same body | PRESERVED |
| Any business route with no identity | 200 data | 401 | AB-03 |
| Valid id, authenticated | 200 full row | 200, `customer_id` masked `***` for the persona | AB-10 (field policy) |
| Unknown id (`DOES-NOT-EXIST`), `REC-0001`, `CUS-00002` (non-key column) | 200 with the first row or a wrong row | 422 (identifier does not match the declared pattern); a well-formed missing id gives 404 | AB-02 |
| Role header (`clinician`, `guest`) | honoured | ignored; the token role decides | AB-03, AB-04 |
| AI summarize without auth | 200 | 401 | AB-06 |
| AI summarize with token | echo of record | deterministic schema-valid summary, approval pending | AB-07, AB-08 |
| Daily ETL | counts and discards | quarantines, exits 1 past 5%, report; first output line preserved | AB-11 |

## 4. Regressions
[VF] None found. Method limit [INF]: the probe set is 9 paths; behaviour outside it is covered only by the test suites.

## 5. Not covered
- [UNK] Behaviour of the web scaffold (no runnable app exists; F-05).
- [ASM] AB IDs were issued by the agent; no named approver has ratified them (OQ-05, OQ-11).
