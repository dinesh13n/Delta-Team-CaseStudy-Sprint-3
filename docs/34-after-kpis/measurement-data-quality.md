# Measurement data quality

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (limits stated) |
| Evidence sources | evidence/34-after-kpis/EVD-O-01-after-kpis.json (SHA-256 3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717); docs/04-baseline-kpis/baseline-data-quality.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Source | Quality issue | Effect on any claim |
|---|---|---|
| events.jsonl | random latencies, evenly spread severities, 66% of correlation ids null or empty, no shipment id | K1 to K4 are not service measurements |
| ai_invocations.csv | scrambled schema (values in the wrong columns), enum noise in 353 of 354 rows | K5 is not model usage |
| carrier_bookings.csv | retry counts 51 to 4,995 | K6 implausible |
| All CSVs | seeded duplicates and blank rows | K7/K8 are seeded, not observed |
| Test metrics K9/K10 | measure the repository | not operations |
| Fixture | no time span (impossible timestamps) | no measurement window can be stated |

The fixture is the only data. It is the same fixture as the baseline.
