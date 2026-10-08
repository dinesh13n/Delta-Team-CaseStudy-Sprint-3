# Data and context risks

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

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| DR-01 | Synthetic data masks real-data defects | High | High | treat all DQ results as lower bound; revalidate on real feed |
| DR-02 | Curated drift from fixture | Med | Med | load_id + hash checks |
| DR-03 | PII leak into AI context | Low after H | High | allow-list + test |
| DR-04 | Owner of thresholds absent | High | Med | OQ-05; thresholds flagged ASM |
| DR-05 | Quarantine growth hides defects | Med | Med | DQ-09 gate and dashboard |
