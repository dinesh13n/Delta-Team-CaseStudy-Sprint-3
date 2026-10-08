# Portability assessment

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (design evidence plus one same-vendor subset test; see `docs/40-scale/semantic-layer-portability-test.md`) |
| Evidence sources | docs/40-scale (Q) |
| Assumptions | See body |
| Unresolved issues | Q not yet run |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Portable by design: provider interface, semantic-layer policy files, prompt files with locked hashes, evaluation datasets and thresholds (independent of provider), data in CSV/JSONL.

**Test that would prove it:** Stage Q regenerates a subset with a second model and scores it against unchanged oracles (rule baseline, H4 allow/deny matrix, J2 datasets). **Run on 2026-10-08 with `claude-haiku-5-5` (same vendor, one run, subset):** safety-critical behaviour carried over, AI-output fidelity did not; results and limits are in `docs/40-scale/`. Portability to another vendor family remains a design claim.
