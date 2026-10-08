# Cost leakage

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (identified) |
| Evidence sources | docs/32-finops |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Token cost per request is below $0.005 at illustrative prices and is not a material leak. Larger leaks: reviewer time on rejected or low-value suggestions, `/metrics` O(n) audit verification, unbounded audit growth, wasted model calls on fallbacks (0.9% in the deterministic run), evaluation re-runs with a paid model. See `docs/32-finops/token-leakage-analysis.md`.
