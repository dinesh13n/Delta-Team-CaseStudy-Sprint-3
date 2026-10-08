# Production KPI baseline

| Field | Value |
|---|---|
| Stage | R: Final As-Built PRD |
| Runbook step | R4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | `evidence/34-after-kpis/EVD-O-01-after-kpis.json` (sha256 `3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717`) |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

There is **no production KPI baseline** because there is no production. The frozen proxy set K1..K10 (latency, cost units, error share, correlation completeness 33.6% usable, AI tokens 904,432 over 353 rows, retry range 51-4,995, duplicates 18, blank rows 6, baseline tests 3/3 after `httpx`, coverage 45%) was recomputed on the same fixture and is unchanged. Definitions are byte-identical in dictionary and `metrics.yaml`. To obtain a real baseline, run the pilot with named reviewers and record review time, approval rate and cycle time first.
