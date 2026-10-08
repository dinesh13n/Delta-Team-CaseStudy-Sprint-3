# Exception metrics

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (data exceptions measured) / business exceptions not measurable |
| Evidence sources | data/reports/latest.json; evidence/34-after-kpis/EVD-O-01-after-kpis.json (SHA-256 3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717) |
| Assumptions | See body |
| Unresolved issues | business exception data |
| Residual risks | O-R-03 enum noise inflates flags |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

What can be measured is **data exceptions** handled by the ETL contract, from the latest published report (`data/reports/latest.json`, load `ld-0c0f0315d16f`): [VF]

| Metric | Value |
|---|---|
| Rows processed (all entities) | 2,124 |
| Rows quarantined | 30 (1.41%, threshold 5%) |
| Multiple active bookings flagged | 2 shipments (SHI-00005, SHI-00019) |
| Legacy-compat malformed row | 1 |
| Enum violations flagged but kept | e.g. `use_case` 353 of 354 AI-invocation rows (DEBT-15 noise: fixture values fall outside the declared enum) |

Baseline served every row, defective or not (K7 18 duplicate keys, K8 6 incomplete rows). Now defective rows are quarantined with a reason and a source row. This is **a control**, not a business improvement: the number of quarantined rows is a property of the seeded fixture.

Business exceptions (late, damaged, mis-routed shipments) have no data source in the repository (F-57).
