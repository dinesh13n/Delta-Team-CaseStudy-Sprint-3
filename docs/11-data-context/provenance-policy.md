# Provenance policy

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

Every AI-assisted output carries: model id, prompt version, context hash, policy decision id, correlation id, and `generated_by` = deterministic|model. Every curated record carries load_id and source row. Outputs shown to humans are labelled "AI suggestion". Provenance is written to the hash-chained audit log.
