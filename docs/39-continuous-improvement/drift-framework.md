# Drift framework

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (framework + script) / CONDITIONAL (no production data) |
| Evidence sources | evidence/39-continuous-improvement/EVD-P-03-drift-check-clean.json (SHA-256 68b946cf2f1147b84059905b7a80e23bdaeea3e6bc06eca8a3492b7a59d8258f) and -drifted.json (SHA-256 702f90ca3f04232249f31c3dc207c67aee97f3e3afa0b9914b9f6df54adc29a4); scripts/drift_check.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Drift = a change in what the system sees or does, with or without a code change. Classes and where each is covered:

| Class | Signal | Covered by |
|---|---|---|
| Data | quarantine ratio, row counts, flag rates, new flags | `scripts/drift_check.py` data checks against `evaluation/reference-data-profile.json` |
| Knowledge / retrieval | n/a (no retrieval) | not applicable |
| Prompt | prompt hash ≠ lock | lock check; start refuses; drift script reports CHANGE-BLOCK |
| Model | (provider, version) not listed | model lock; start refuses |
| Model behaviour | evaluation below thresholds; fallback rate; reject share; leaks | `--with-eval`, `--audit` runtime checks, alerts |
| Agent | n/a (L0) | not applicable |
| Reliability, latency | SLO alerts | N1 alerts |
| Adoption | decisions per period | audit counts |
| Cost | tokens per request | `finops_estimate.py`, tokens metric |

Evidence: clean run OK (192 of 192 evaluation cases); a deliberately drifted dataset (34% rows removed, 60 weights blanked, new status values, quarantine 19.5%) gave INVESTIGATE on quarantine ratio and the shipments entity. See `EVD-P-03-*`.
**Limits:** the clean run compares the fixture with itself, so it proves the plumbing, not sensitivity to real drift. The drifted run proves the thresholds can trip. Flags are counted by name: a new *value* inside an existing flag (e.g. the status `teleported`) is invisible.
