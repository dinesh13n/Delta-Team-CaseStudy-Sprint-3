# Schema and data migration plan

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/10-architecture; docs/11-data-context; docs/12-specs |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; platform OQ-01 |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

1. No in-place change to `data/synthetic`. 2. ETL writes `data/curated/<entity>.csv` and `data/quarantine/<entity>.jsonl` with `load_id`. 3. Curated schema = semantic-layer entity definitions + `load_id`, `source_file`, `source_row`, `data_quality_flags`. 4. Audit v2 is a new file; v1 is read-only history; historical events with null correlation ids are never rewritten (flag only). 5. Rollback: delete `data/curated` and `data/quarantine` and set `DATA_LAYER=fixture`; no destructive step exists. 6. Idempotency: same input hash gives same curated hash (AC-10). 7. Test oracle: EVD-D-05-rule-baseline.json.
