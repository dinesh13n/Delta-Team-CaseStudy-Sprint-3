# Characterization Test Plan

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 7 repository assessment) |
| Runbook step | C7 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | C2-C6 documents; runbook/01-BASELINE-ASSESSMENT.md findings register; direct reading of the subtree |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Eleven behaviours (runbook C8). Label: IL = intended legacy behaviour, DEF = defect scheduled for approved change.
| # | Behaviour | Test | Label | Finding |
|---|---|---|---|---|
| 1 | Unknown id returns the first row, asserted by values | test_unknown_id_returns_first_row | DEF | F-32, F-51 |
| 2 | REC-0001 collides across six files | test_rec0001_in_all_six_entities | DEF | F-30 |
| 3 | Match on non-key column | test_lookup_matches_non_key_column | DEF | F-31 |
| 4 | No role header succeeds | test_records_without_role_header_succeeds | DEF | F-17 |
| 5 | `clinician` succeeds | test_records_clinician_role_succeeds | DEF | F-19 |
| 6 | AI endpoint with no role | test_ai_summary_without_any_role | DEF | F-20 |
| 7 | guardrail not_enforced | test_ai_guardrail_status_not_enforced | DEF | F-24 |
| 8 | Summary echoes first column | test_ai_summary_echoes_first_column | DEF | F-29 |
| 9 | Audit has no actor or correlation id | test_audit_event_has_no_actor_or_correlation | DEF | F-43 |
| 10 | Health independent of data layer | test_health_ok_without_data_layer | DEF | F-46 |
| 11 | ETL reports malformed and exits 0 | test_etl_reports_malformed_and_exits_zero | IL (counting), DEF (no quarantine) | F-40 |
Status after execution is in the C8 evidence (EVD-C-08).
