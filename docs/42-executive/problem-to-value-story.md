# Problem-to-value story

| Field | Value |
|---|---|
| Stage | R: Executive Defence, Final PRD, Evidence Pack |
| Runbook step | R3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/03-problem-value; docs/34-after-kpis; docs/36-benefits |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Problem (technology-neutral, from B3)
Operations staff must find the right shipment record, understand an exception and decide what to do, using data that is partly wrong, under access rules nobody can check, with no trail of who decided what. [VF, `docs/03-problem-value/problem-statement.md` (sha256 `f580a33f48126b2dd1a853ca7c197f3e6e150601e96f73d6f82b82afe3605544`)]

## Value hypothesis and what became of it
| Hypothesis | Outcome | Evidence |
|---|---|---|
| Wrong-record and unauthorised access can be removed | **Achieved** (tested) | `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv` (sha256 `c78a8433c06d9266db854f14d8ee3393ff348a4dd42dc5cdd032114fc0c92b58`) |
| Decisions can be reconstructed from the audit | **Achieved** (author-run, one event) | `evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`) |
| Bad rows are caught instead of silently flowing on | **Achieved** (30 of 2,124 rows quarantined in the sample run; fixture untouched) | `evidence/15-modernization/EVD-H-06-etl-dq-report.json` (sha256 `1f091a63cc2100d80f936f5d6649fd30561f2f009820ef1e63c79f81f9520ed7`) |
| AI saves review time | **Not shown**: no model, no reviewer, no review-time data | `docs/32-finops/cost-per-outcome.md` (sha256 `cb975734b539c38349625ddf989ed9fd2a374c37e1e13d1fa74b5de7704ba695`) |
| Cycle time, cost per shipment, exception rate improve | **Not measurable**: no business KPI exists in the data | `evidence/34-after-kpis/EVD-O-01-after-kpis.json` (sha256 `3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717`) |

## Value, stated plainly
The value delivered is **risk reduction and controllability**, which has not been priced because no loss data exists. Business value is a hypothesis awaiting measurement of human review time and approval rate. [INF]
