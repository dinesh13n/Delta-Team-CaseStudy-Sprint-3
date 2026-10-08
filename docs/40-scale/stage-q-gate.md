# Stage Q gate review

| Field | Value |
|---|---|
| Stage | Q: Model portability and demonstration |
| Runbook step | Q4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (Q1-Q2 not performed) |
| Evidence sources | EVD-Q-01, EVD-Q-02, EVD-Q-03 |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| # | Criterion | Result | Evidence |
|---|---|---|---|
| Q-X1 | Model B built from semantic layer and specs only | **NOT MET**: no Model B | `semantic-layer-portability-test.md` |
| Q-X2 | Both builds evaluated on identical unchanged datasets and predeclared thresholds | **NOT MET** (one build); inputs and thresholds are pre-registered with SHA-256 | EVD-Q-01 |
| Q-X3 | Differences classified model-attributable or ambiguity | **NOT MET**: nothing to classify | `model-comparison.md` |
| Q-X4 | Ambiguities logged as corrective actions | **PARTIAL**: IMP-Q01..03 log the missing run, no ambiguity | `improvement-backlog.md` |
| Q-X5 | Demo rehearsed end to end within budget | **PARTIAL**: author run of the offline commands, 28 s, no audience, no recording of a person; budget unconfirmed | EVD-Q-03 |

**Stage Q result: CONDITIONAL, with the portability claim withdrawn.** The Challenge Guide step "test the semantic layer with a new model" was not done. Condition to lift: run the pre-registered protocol with a second model (OQ-02). Stage R may proceed; the readiness decision must state this gap.
