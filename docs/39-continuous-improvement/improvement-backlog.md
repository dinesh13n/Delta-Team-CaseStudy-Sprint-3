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

**Added after the Stage Q portability run (2026-10-08, `docs/40-scale/semantic-layer-portability-test.md`).** IMP-Q01 is done (single run). IMP-Q02 becomes the list below.
- IMP-Q04 (D1) define the recommendation classes and their meaning in FEAT-04 and replace the wording-based check in the harness with a class check; the current check measures similarity to Model A.
- IMP-Q05 (D2) state in `business-rules.yaml` or FEAT-04 that a booking above the BR-13 retry ceiling yields a retry-check recommendation (or that it does not).
- IMP-Q06 (D3) state how legacy or non-canonical shipment statuses (for example `approved`) are treated in the AI path: abstain, or summarise with a flag.
- IMP-Q07 (D4) define "required fields missing" and "sources conflict" for the AI path (no events and no bookings; duplicate bookings).
- IMP-Q08 (D5) resolve the contradiction between FEAT-04 (fallback on schema violation and low confidence) and the output schema and datasets (abstain `schema_violation`, `low_confidence`).
- IMP-Q09 (D6) state which personas may call `POST /ai/summarize`; align `access-semantics.yaml` and `api-contracts.md`.
- IMP-Q10 (D7) add the approver, reviewer, ops and auditor roles to `access-semantics.yaml` instead of the [ASM] platform-role table in code.
- IMP-Q11 (D8) specify the purpose parameter, the field-mask format, audit failure behaviour, audit of 404, scope narrowing and tenant filtering; add checks for each.
- IMP-Q12 repeat with three runs per model and Model A re-run from the same bundle; replace IMP-Q03 wording: a model of another vendor family.
- IMP-Q13 independent review of the difference classification and of the harness for bias towards Model A.

