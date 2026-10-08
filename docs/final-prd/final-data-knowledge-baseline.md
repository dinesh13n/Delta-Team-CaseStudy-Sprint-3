# Final data and knowledge baseline

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | semantic-layer/; evidence/04-baseline-kpis; evidence/11-data-context |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- Fixture: six CSVs of 354 rows and 3,000 events, byte-identical to the baseline tag; never edited. Seeded defects: 3 duplicate keys, 1 blank row, 1 impossible timestamp (3 files), confidence 1.42, `REC-0001` as first key in all six, orphan references, `*-BAD1` keys, categorical columns polluted with status words.
- Curated layer and quarantine are derived (OQ-14 ruling provisional): 30 of 2,124 rows quarantined in the verification run (`evidence/15-modernization/EVD-H-06-etl-dq-report.json` (sha256 `1f091a63cc2100d80f936f5d6649fd30561f2f009820ef1e63c79f81f9520ed7`)).
- Semantic layer: glossary, entities, status taxonomy, relationships, business rules, metrics, access semantics, AI context policy, JSON schema, generated JSON, 16 tests passing (`evidence/11-data-context/EVD-D-05-generated-semantic-layer.json` (sha256 `edf62772dc55687db93dd20f3e520331db0e5f247d936c0ced401cee79083bf2`)). Enum meanings are inferred, not owner-confirmed.
- Knowledge/RAG: none. No retrieval, no vector store, no embeddings. Context is the single record's allow-listed fields.
