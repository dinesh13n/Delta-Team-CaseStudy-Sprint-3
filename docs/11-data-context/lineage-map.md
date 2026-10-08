# Lineage map

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

```
data/synthetic/*.csv,jsonl (immutable fixture)
   -> ETL extract (read-only)
   -> validate (DQ-01..08)
        -> pass  -> curated layer (data/curated/*.parquet|csv, versioned by load_id)
        -> fail  -> quarantine layer (data/quarantine/*.jsonl with reason)
   -> DataRepository port -> API / policy engine -> AI gateway (allow-listed context only)
   -> audit hash chain (inputs hash, policy decision, model/prompt version)
```
Every curated row carries `load_id`, `source_file`, `source_row`. Every AI call records the input hash and the context field list. [INF] design; implemented in Stage H.
