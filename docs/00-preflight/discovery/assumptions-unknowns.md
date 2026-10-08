# Assumptions and Unknowns

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0A pre-flight discovery |
| Runbook step | A4 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, pending Transformation Lead review |
| Evidence sources | EVD-A-04-repo-tree-annotated.txt; EVD-A-04b-data-profile.txt; direct file reads of the repository; runbook/04-OPEN-QUESTIONS-REGISTER.md |
| Assumptions | See assumptions-unknowns.md |
| Unresolved issues | See assumptions-unknowns.md |
| Residual risks | Read-only discovery only; no behavioural run yet (Stage C) |

Classification key: **[VF]** Verified Fact (read in a cited file), **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown. Paths are relative to `07-logistics-shipment-fleet-routing-ops/`. This document makes no transformation recommendations (Spine 0A).

## 1. Assumptions
| ID | Assumption | Basis |
|---|---|---|
| ASM-1 | The repository is the whole estate in scope | README; no other repos named |
| ASM-2 | All data and credentials are synthetic | `data/README.md`, `quality_issues.json` safety note |
| ASM-3 | Operator Dinesh holds all role slots provisionally | OQ-05 default, decision-log D-001 to D-004 |

## 2. Unknowns
| ID | Unknown | Linked open question |
|---|---|---|
| UNK-1 | Target platform | OQ-01 |
| UNK-2 | The two models for the comparison | OQ-02 |
| UNK-3 | Network egress policy | OQ-03 |
| UNK-4 | Named approvers | OQ-05 |
| UNK-5 | Authorisation to modify the repository | OQ-11 |
| UNK-6 | Current test pass/fail result | Stage C |
| UNK-7 | Real runtime topology, users and systems of record | none yet |
| UNK-8 | Windows host tools and exact Node version | EVD-A-03d/e |

## 3. Cross-check of the runbook figure for F-42 (RESOLVED, reversed by D-012)
- [VF] Runbook finding F-42 states 1,992 of 3,000 events (66.4%) have no correlation id. An earlier count here used `grep -c '"correlation_id": null'` = 983 (32.8%) and wrongly called the runbook figure wrong. That count missed events whose `correlation_id` is the empty string.
- [VF] Re-count on the baseline-hash-verified file (EVD-A-04c): null 983, empty string 1,009, non-empty 1,008. Null or empty = 1,992 = 66.4%. The runbook figure was right.
- Action: D-007, D-008 and D-010 (as far as they concern F-42 and C1) are superseded by D-012. Other quantitative findings were re-verified in Stage C.
