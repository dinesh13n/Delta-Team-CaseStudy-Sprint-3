# Portability assessment

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (design evidence; no portability test yet) |
| Evidence sources | docs/40-scale (Q) |
| Assumptions | See body |
| Unresolved issues | Q not yet run |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Portable by design: provider interface, semantic-layer policy files, prompt files with locked hashes, evaluation datasets and thresholds (independent of provider), data in CSV/JSONL.

**Test that would prove it:** Stage Q regenerates a subset with a second model and scores it against unchanged oracles (rule baseline, H4 allow/deny matrix, J2 datasets). Result and its limit (same vendor) are recorded in `docs/40-scale/` once run. Until then portability is a design claim, not a result.
