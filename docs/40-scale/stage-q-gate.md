# Stage Q gate review

| Field | Value |
|---|---|
| Stage | Q: Model portability and demonstration |
| Runbook step | Q4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v2.0 (supersedes v1.0 "NOT PERFORMED") |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5) as Model A and judge; Model B = claude-haiku-5-5 (subagent); operator Dinesh |
| Status | CONDITIONAL: Q1 to Q3 performed once; the pre-registered gate for Model B FAILS (2 of 8 threshold gates); Q-X5 partial |
| Evidence sources | EVD-Q-01, EVD-Q-03, EVD-Q-04, EVD-Q-05, EVD-Q-06 |
| Assumptions | Single run; same vendor family; classification of differences made by the Model A author |
| Unresolved issues | IMP-Q04..IMP-Q13; OQ-02 |
| Residual risks | Self-approved gate until named approvers exist; a single same-vendor run |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| # | Criterion | Result | Evidence |
|---|---|---|---|
| Q-X1 | Model B built from semantic layer and specs only | **MET for the subset**, with the qualifiers that Model B also saw the Stage F specs and PRD (written by Model A), the build was one attempt, and the model is from the same vendor family. Blindness verified from the full transcript (0 of 31 tool calls outside the bundle). | `semantic-layer-portability-test.md`, EVD-Q-05 |
| Q-X2 | Both builds evaluated on identical unchanged datasets and predeclared thresholds | **MET WITH DEVIATIONS**: datasets, `thresholds.json` and `red_team.py` unchanged (hashes recorded); a model-neutral scorer with identical scoring replaced `run_eval.py`, and Model A was re-scored as a control. **Model B does not pass the thresholds** (6 of 8 gates). | EVD-Q-01, EVD-Q-04 |
| Q-X3 | Differences classified model-attributable or ambiguity | **MET, not independently reviewed**: 8 differences, 0 model-attributable, 7 ambiguity, 1 specification contradiction. | `semantic-layer-portability-test.md` |
| Q-X4 | Ambiguities logged as corrective actions | **MET as logged, OPEN as fixed**: IMP-Q04..IMP-Q13 logged; none implemented. | `improvement-backlog.md` |
| Q-X5 | Demo rehearsed end to end within budget | **PARTIAL** (unchanged): author run of the offline commands, 28 s, no audience, no recording of a person; budget unconfirmed. | EVD-Q-03 |

**Stage Q result: CONDITIONAL.** The portability claim is upgraded from "design claim only" to "demonstrated for access, lookup, guardrail and audit behaviour with one same-vendor model; not demonstrated for AI-output fidelity, where eight specification gaps were found". The pre-registered thresholds were not met by Model B and were not relaxed.

Condition to lift: (1) rule on D1 to D8 in the specifications (IMP-Q04..IMP-Q10); (2) re-run from the revised bundle with a fresh Model B, three runs per model, a model of another vendor family if OQ-02 allows (IMP-Q03, IMP-Q12); (3) one independent reviewer of the classification (IMP-Q13). Stage R was completed before this run and its documents are updated for it; they carry the same conditions.
