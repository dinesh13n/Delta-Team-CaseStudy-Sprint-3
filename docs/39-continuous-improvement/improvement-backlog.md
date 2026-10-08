# Improvement backlog

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

IMP-01 drift reference from real data; IMP-02 flag-value-level drift (not only flag names); IMP-03 schedule the drift check and alert on exit codes; IMP-04 evaluation with a real model; IMP-05 provider-reported usage; IMP-06 population stability for categorical fields; IMP-07 per-role adoption metrics; IMP-08 export KPIs as metrics.


**Added in Stage Q (2026-10-08):** IMP-Q01 run the pre-registered portability test with a second model (`docs/40-scale/semantic-layer-portability-test.md`); IMP-Q02 add any specification ambiguity it reveals as a spec change with a test; IMP-Q03 repeat with a model of a different family if OQ-02 allows.
