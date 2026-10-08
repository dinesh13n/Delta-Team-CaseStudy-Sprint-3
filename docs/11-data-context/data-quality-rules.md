# Data quality rules and thresholds

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-A-04b data profile; EVD-C-05 profile; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | OQ-14 ruling provisional; approvers UNRESOLVED |
| Residual risks | See data-context-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Rule | Metric | Baseline [VF] | Threshold (target) | Action on breach |
|---|---|---|---|---|---|
| DQ-01 | Unique primary key | duplicate keys per file | 3 per file | 0 in curated | quarantine later duplicates, keep first, log |
| DQ-02 | No blank rows | blank rows | 1 per file | 0 | drop to quarantine |
| DQ-03 | Timestamp sanity (not 1900-01-01, not future) | invalid ts | 1 per file | 0 | quarantine |
| DQ-04 | Enum conformance to status-taxonomy | out-of-domain values | see enum-violations.md | 0 | map where unambiguous, else quarantine |
| DQ-05 | Confidence in [0,1] | out-of-range | max 1.42 | 0 | clamp-not-allowed; reject |
| DQ-06 | correlation_id present and non-empty on events | missing rate (null or empty) | 66.4% | 0% for new events | reject at write |
| DQ-07 | Carrier retry within policy | out-of-range | 51-4995 | per BR rule | flag |
| DQ-08 | Referential integrity per relationships.yaml | orphans | measured in EVD-D | 0 curated | quarantine |
| DQ-09 | Quarantine rate gate | quarantined/total | n/a | <=5% else fail load | fail load, page owner |
Thresholds are proposals [ASM]; owners UNRESOLVED.
