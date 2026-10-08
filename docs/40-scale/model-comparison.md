# Model comparison (Q2)

| Field | Value |
|---|---|
| Stage | Q: Model portability and demonstration |
| Runbook step | Q2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v2.0 (supersedes v1.0 "NOT PERFORMED") |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5) as Model A and judge; Model B = claude-haiku-5-5 (subagent); operator Dinesh |
| Status | PERFORMED for one subset and one run; Model B does not meet the pre-registered thresholds |
| Evidence sources | EVD-Q-06-comparison.csv; EVD-Q-04; EVD-Q-05 |
| Assumptions | Single run; same vendor family; classification of differences made by the Model A author |
| Unresolved issues | IMP-Q04..IMP-Q13 |
| Residual risks | Comparison favours Model A by construction (harness derived from its behaviour) |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

The full scorecard is `evidence/40-scale/EVD-Q-06-comparison.csv` (it supersedes `EVD-Q-02-comparison.csv`, which stays as the pre-run record with `NOT RUN`; evidence is append-only).

| Dimension | Model A (claude-sonnet-5-5) | Model B (claude-haiku-5-5) |
|---|---|---|
| Scope built | full system | four-behaviour subset (1,390 app lines, 360 test lines) |
| Effort | multi-session | one attempt, 31 tool calls, 235,628 tokens, 37.6 minutes |
| Evaluation cases passing every strict check | 192 of 192 | 8 of 192 |
| Safety gates (schema, unsupported claims, forbidden leaks, injection leaks, approval flag) | 5 of 5 pass | 5 of 5 pass |
| Fidelity gates (abstention, recommendation class) | 2 of 2 pass | 0 of 2 pass (0.875; 0.1667) |
| Black-box API checks | 24 of 24 | 21 of 24 (24 of 24 with an `ai_agent` token, post hoc) |
| Original attacks that succeed | 0 of 12 | 0 of 12 |
| Audit chain: valid, and tampering detected | yes | yes |

## Reading it
- On everything that protects data, people and the audit trail, the two builds are indistinguishable on this harness. [VF]
- Where they differ, the specification is silent or contradicts itself (D1 to D8 in `semantic-layer-portability-test.md`). The corrective actions are IMP-Q04..IMP-Q13. None is implemented yet. [VF]
- The model-B column is not a quality ranking: a smaller model, a subset, one run, and a harness written around the other build. [INF]
- The earlier statement "the semantic layer is model-independent" is now **partly supported** (access, lookup, guardrail, audit) and **not supported** for AI output wording, abstention rules and role naming. [INF]
