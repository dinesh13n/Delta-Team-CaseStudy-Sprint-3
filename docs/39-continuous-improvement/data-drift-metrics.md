# Data drift metrics

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/39-continuous-improvement/EVD-P-03-drift-check-clean.json (SHA-256 68b946cf2f1147b84059905b7a80e23bdaeea3e6bc06eca8a3492b7a59d8258f) and -drifted.json (SHA-256 702f90ca3f04232249f31c3dc207c67aee97f3e3afa0b9914b9f6df54adc29a4) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Metric | Reference | Investigate when |
|---|---|---|
| Quarantine ratio | 0.0141 (30 of 2,124) | rises > 0.02 absolute, or above the contract limit 0.05 |
| Rows per entity | 354 each | changes > 20% |
| Flag rate per flag | e.g. `enum_violation:service_tier` 332/354 | moves > 10 points; or a flag not in the reference |
| Duplicate keys, incomplete rows | K7/K8 on raw layer | any new class |
Thresholds are proposed starting values in `evaluation/drift-thresholds.json`, not tuned on production data.
