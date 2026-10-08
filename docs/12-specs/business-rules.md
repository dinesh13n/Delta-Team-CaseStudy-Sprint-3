# Business rules specification

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | openapi.yaml; schemas/; docs/09-initial-prd; docs/10-architecture; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; open items in docs/12-specs/spec-readiness.md |
| Residual risks | Specs are PROVISIONAL until OQ-01/02/03/05/11 are ruled |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

The authoritative definitions are `semantic-layer/business-rules.yaml` (25 rules: BR-K-* key patterns, BR-P-* primary-key uniqueness, BR-01..BR-13 semantic rules including the 6 declared gaps), evaluated by `semantic-layer/tests/rule_eval.py`. The baseline violation count per rule is frozen in `evidence/11-data-context/EVD-D-05-rule-baseline.json` and is the oracle for Stage H tests. Gaps BR-03 (stale GPS) and BR-06 (route restrictions) carry `data_gap`: they are specified but not enforceable on this data [VF]. Runtime enforcement point: ETL validation (block -> quarantine, warn -> flag).
