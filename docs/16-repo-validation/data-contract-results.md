# Data-contract results

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H11 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-H-06, EVD-H-07, EVD-H-08, EVD-A-01 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Contract | Result |
|---|---|
| Fixture immutability (`data/synthetic`, `data/manifest.json`) | all OK; the 20 manifest mismatches are only the deliberately modified non-data files (EVD-H-11-tg5-tg6.txt) |
| Rule oracle (`EVD-D-05-rule-baseline.json`) vs ETL | curated shipments 349; quarantine 30 of 2124 rows (1.41%), matches the oracle; enum noise flagged, not quarantined |
| Schemas | `audit-event.schema.json` v1.1 and `ai-summary-output.schema.json` v1.1 validate generated output: 349/349 AI summaries schema-valid (EVD-H-07); audit chain valid over 351 records (EVD-H-08) |
| OpenAPI | route set equals implemented routes (10 operations); spec validates with openapi-spec-validator |
| Semantic layer | 16 tests pass; K4 amended and regenerated (D-012) |
