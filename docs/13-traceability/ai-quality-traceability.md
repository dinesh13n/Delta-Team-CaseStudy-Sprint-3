# AI quality traceability

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-E-03; EVD-F-04; acceptance-criteria.md |
| Assumptions | See body |
| Unresolved issues | Test files are PLANNED (written in Stage H/J/L); no test result is claimed here |
| Residual risks | See coverage-gap-register.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| AI requirement | Finding | Test | Metric / threshold (to be predeclared in L1) |
|---|---|---|---|
| FR-10 | F-22 | AC-13 | injection corpus: 0 successful of N |
| FR-10 | F-23 | AC-14 | format-string payloads: 0 evaluated |
| FR-11 | F-24 | AC-12 | guardrail_status always enforced|blocked |
| FR-11 | F-25 | AC-12, AC-15, AC-16 | 100% outputs schema-valid or abstained |
| FR-12 | F-26 | AC-17 | 100% of suggestions need an approval record |
| FR-09 | F-27 | AC-12 | 100% outputs carry model and prompt version |
| FR-09, FR-17 | F-28 | AC-23 | token count source labelled; cost per request <= 2.25 |
| FR-09 | F-29 | AC-12 + eval set | groundedness / factuality on eval set (threshold set in L1) |

Thresholds are NOT set here (they are predeclared in Stage L1). AI-quality results require a real model; with the deterministic provider only structural properties can be verified [INF].
