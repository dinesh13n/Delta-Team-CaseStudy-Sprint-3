# Readiness assessment by rubric criterion

| Field | Value |
|---|---|
| Stage | S: Evidence index and rubric traceability (runbook/03-EVIDENCE-RUBRIC-TRACEABILITY.md) |
| Runbook step | 03-4 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PROVISIONAL; this is not a grade |
| Evidence sources | rubric-coverage-matrix.md; blocker-status.md; finding-rubric-map.md; stage gates |
| Assumptions | Self-assessment by the same agent that built the evidence; no independent reviewer |
| Unresolved issues | Marks are awarded by evaluators, not by the author |
| Residual risks | An evidence-coverage index is not a score and must not be quoted as one |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## What this is
For each criterion: how many of its sub-dimensions are MET, PARTIAL, NOT MET or BLOCKED, an **evidence-coverage index** (MET counts 1, PARTIAL 0.5, others 0, divided by the number of sub-dimensions), the strongest evidence and what cannot be claimed. It says how complete the evidence is. It does not say how many marks an evaluator will give, and I have deliberately not converted it to marks.

| Criterion | Marks | MET | PARTIAL | NOT MET | BLOCKED | Evidence-coverage index |
|---|---|---|---|---|---|---|
| R1 As-Is understanding | 20 | 6 | 1 | 0 | 0 | 0.93 |
| R2 Repo 2.0 design | 25 | 5 | 4 | 0 | 0 | 0.78 |
| R3 Governance, risk, security | 20 | 5 | 2 | 1 | 1 | 0.67 |
| R4 PRD and working application | 25 | 4 | 1 | 0 | 1 | 0.75 |
| R5 Presentation and defence | 10 | 4 | 1 | 0 | 0 | 0.90 |

## Per criterion
**R1 As-Is understanding (20).** Strongest evidence: the paired quick-start transcripts (as-delivered fails, transformed passes), 62 findings, data profile, 13 discovery artifacts. Gap: no owner confirmed the partial-modernisation root cause; no business KPI moved, so before/after proof is behavioural, not commercial. R1 depends on no open question and is the most complete criterion.

**R2 Repo 2.0 design (25).** Strongest evidence: ADR-0002..0010 with the supersession of ADR-0001, the semantic layer with tests and generation, Rego generated from `access-semantics.yaml`, red team 10 of 12 to 0 of 12, five drills, CI green on two Python versions. Gaps: no platform, IaC or traces (B-4); scope narrowing declared but not enforced; portability shown for access, lookup, guardrail and audit only, and the second model failed two fidelity gates.

**R3 Governance, risk, security (20).** Strongest evidence: approval enforced in code, hash-chained audit with tamper detection and reconstruction, injection defence, threat model, SBOM. Gaps: the one NOT MET row (named owners and signed acceptances, B-8), compliance mapping blocked (B-3), observability without a deployed collector, change governance without branch protection or a signed authorisation. R3 is where the missing human decisions bite hardest.

**R4 PRD and working application (25).** Strongest evidence: three PRDs, 62-row finding matrix and 48-row requirement matrix, 176 tests, a running service with a browser check. Gaps: no real model (B-1), the end-to-end demonstration is a thin view run by its author. This criterion carries the most marks and has the one BLOCKED row that needs a model decision.

**R5 Presentation and defence (10).** Strongest evidence: executive narrative, defence documents with rejected alternatives, voluntary limitations, a one-lookup answer for any finding. Gap: the rehearsal had no audience and no recording of a person.

## Effort allocation (the scheduling judgement in Document 03 section 4)
Document 03 warned that findings concentrate in R3 while marks concentrate in R4, and that governance work must not starve the working-application work.
- Findings: R3 31, R2 22, R1 24, R4 6 (62 findings, a finding can count for more than one).
- Evidence rows by criterion (a file can count for more than one; 116 of 140 rows are stage-assigned): R1 30, R2 71, R3 19, R4 20, R5 36.
- Reading: evidence volume leans to R2 (about half of the rows) while R3 and R4, which together carry 45 marks, hold the fewest rows. The thinness of R4 and R3 evidence is not a volume problem but a *kind* problem: they are blocked by missing people and a missing model, not by missing work. [INF]
- Time actually spent per stage was not recorded, so the allocation of effort is [UNK].

## Where a day of effort would move the evidence most
1. **R3, B-8:** name approvers and sign or reject the 12 risk acceptances. It needs people and about an hour of their time; it converts the only NOT MET row. Nothing I can do alone.
2. **R4, B-1:** provide one model and its egress (OQ-02, OQ-03); I can then run the evaluation and the workflow end to end and repeat the second-model test with a different family.
3. **R5/R4:** run the demo once with a person watching and keep the recording.
4. **R2/R3, B-13:** revoke and rotate the credentials in history; it costs minutes and removes a standing finding.
5. **R2:** close IMP-Q04..IMP-Q10 so the specification pins down AI output behaviour.
