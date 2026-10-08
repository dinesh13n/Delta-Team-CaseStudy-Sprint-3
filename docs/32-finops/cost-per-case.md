# Cost per case

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | BLOCKED (cases cannot be tied to cost) |
| Evidence sources | docs/00-preflight/ai-economics/volume-assumptions.md |
| Assumptions | See body |
| Unresolved issues | case identifier |
| Residual risks | N-R-15 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

A "case" is an exception to be resolved. The fixture's events carry **no shipment id** (F-M3-01 related; volume-assumptions.md), so no event, retry or resolution can be attributed to a case from data. Cost per case therefore **cannot be measured**.

What can be said: if a case triggers `k` AI summaries, `cost_case_ai = k × cost_request`. `k` is unknown; the fixture requests exactly one per shipment by construction of the test, which says nothing about behaviour. Human time per case (the dominant term) is unmeasured.

Unblock: production case identifiers on events, and instrumentation of requests per case (the audit already holds resource id and correlation id, so `k` becomes countable once real use exists).
