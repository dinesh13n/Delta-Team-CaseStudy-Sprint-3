# Stage D Gate Review

| Field | Value |
|---|---|
| Stage | D: Semantic Layer Extraction |
| Runbook step | D6 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | evidence/11-data-context/ |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| # | Criterion | Result | Evidence |
|---|---|---|---|
| D-X1 | Nine files from the capture PDF exist | **PASS** (README, glossary, entities, status-taxonomy, relationships, business-rules, metrics, access-semantics, ai-context-policy) | test_nine_files_exist |
| D-X2 | Every column of six datasets defined | **PASS**: 56 of 56 | EVD-D-01 |
| D-X3 | Every categorical field has a domain; violations listed with remedy | **PASS**: 29 fields, 0 blank remedies | EVD-D-02 |
| D-X4 | Six declared gaps as rules | **PASS**; two (stale_gps BR-03, route_ignores_restrictions BR-06) carry a recorded data gap because the dataset lacks a position timestamp and an override field | EVD-D-03 |
| D-X5 | metrics.yaml matches frozen C1 definitions | **PASS**: automated comparison, 10 of 10 | test_metrics_match_frozen_kpi_dictionary |
| D-X6 | Tests pass; JSON generated | **PASS**: 16 tests passed; JSON from generate.py, comparison test guards drift | EVD-D-05 |
| D-X7 | No model, framework or vendor content | **PASS**: automated keyword test over all YAML; reviewer read-through by the operator still outstanding | test_layer_is_vendor_framework_and_model_neutral |

## Status
**CONDITIONAL PASS.** Open: PROPOSED enum domains and the two data gaps need the Data Owner (UNRESOLVED); D-X7 human read-through.

## Baseline oracle
`EVD-D-05-rule-baseline.json` records current violations per rule (for example duplicate keys 6 per dataset, 353 retry counts above the assumed ceiling), reused by Stage H regression tests.

## Newly found during Stage D (decision-log D-011)
F-61: `routes.weather_risk` contains the numeric value 1.42 in a categorical field. F-62: every dataset has a malformed key of the form `*-BAD1` (for example `SHI-BAD1`), caught by the key-pattern rule.

## Required Final Response
Status: CONDITIONAL PASS. Findings: F-61, F-62; 25 rules, 29 field domains. Risks: PROPOSED domains unconfirmed. Assumptions: freshness limit 15 min, retry ceiling 5. Artifacts: 9 layer files, schema, tests, generator, generated JSON, 7 evidence files. Blocking: none. Next: Stage E.
