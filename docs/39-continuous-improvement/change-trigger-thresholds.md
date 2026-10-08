# Change trigger thresholds

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PROPOSED |
| Evidence sources | evaluation/drift-thresholds.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Condition | Result |
|---|---|
| Any prompt/model lock mismatch, evaluation safety failure | CHANGE-BLOCK (exit 2): do not promote or serve |
| Data quarantine > 5% | ETL status fails (contract limit) and INVESTIGATE |
| Quarantine +2 points, entity rows ±20%, flag rate ±10 points, new flag | INVESTIGATE (exit 1) |
| Fallback > 20%, reject > 50% (≥ 30 samples), any blocked leak | INVESTIGATE |
| AI p95 > 5 s, API 5xx > 2%, chain invalid | alerts (N1) |
Machine-readable: `evaluation/drift-thresholds.json`. Thresholds may be changed only before the observation they judge (J-X2 principle) and with a written reason.
