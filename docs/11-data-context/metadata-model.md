# Metadata model

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

Per field: name, entity, type, nullable, enum domain, sensitivity (public/internal/PII), allowed AI context (ai-context-policy.yaml), owner, source, DQ rules. Per dataset: load_id, schema version, row counts, quarantine count, hash. 56 fields catalogued in the semantic layer [VF]. Stored as generated JSON `semantic-layer/generated/semantic-layer.json`.
