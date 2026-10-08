# Demo day script

| Field | Value |
|---|---|
| Stage | Q: Model portability and demonstration |
| Runbook step | Q3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, rehearsed by author only |
| Evidence sources | evidence/42-executive/EVD-Q-03-demo-rehearsal.txt; evidence/07-repo-assessment/EVD-C-02-quickstart-transcript.txt; evidence/26-tevv; evidence/31-observability; evidence/28-resilience |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## Format and budget (OQ-16, OQ-17: PROPOSED, no one has confirmed)
- Environment: this repository on one laptop, offline, deterministic AI provider (no model, no network). [ASM]
- Budget: **10 minutes**, 5 minutes questions. The offline commands below take **28 seconds** in total (author rehearsal, `EVD-Q-03-demo-rehearsal.txt`). [VF]
- The rehearsal was run by one person, without an audience, and not recorded on video. Q-X5 is therefore **not met in the sense the runbook intends**.

## Beats (strongest evidence first)
| # | Time | Say | Show | Evidence |
|---|---|---|---|---|
| 1 | 0:00-2:00 | "The delivered quick-start does not run." | baseline `pytest -q` exit 2 (httpx missing), wrong `uvicorn apps/api...` path; then the same on the new build: 176 passed | EVD-C-02, rehearsal beat 1 |
| 2 | 2:00-4:00 | "Same attacks, two builds." | red-team summary: baseline 10 of 12 succeed, v2 0 of 12 | EVD-L-03-redteam-baseline/v2.json |
| 3 | 4:00-6:00 | "One business event, reconstructed end to end." | `python -m scripts.reconstruction_evidence`: read, AI summary, human decision, same correlation id; tamper test marks the chain untrusted | EVD-N-02 |
| 4 | 6:00-7:30 | "When the AI is off, the work continues." | failure drills 1-5 PASS, drill 2 (timeout / AI disabled) | EVD-M-03-drills |
| 5 | 7:30-8:30 | "Is the design model-independent?" | **Say it was not tested.** Show the pre-registered protocol and hashes | model-comparison.md |
| 6 | 8:30-10:00 | "What does an outcome cost?" | formula; human review dominates; money figure unknown; NPV negative at fixture volume | cost-per-outcome.md, npv-model.md |

## Predictable challenges
**What did you not fix, and why?** Infrastructure provisions nothing (no platform decision, OQ-01); traces are not implemented (correlation id only); the Angular portal never existed, a thin operations view replaces it; secrets removed from the tree are **not revoked** and remain in history; CI is written but has never run on GitHub; self-approval is possible (HC-R-01).

**What can you still not prove?** Anything about a real model; behaviour under real load or a deployed platform; any business KPI change (none is measurable); that people can follow the incident playbook (the tabletop was one author); portability across models; independent review of any gate (all gates were signed by the operator, PROVISIONAL).

**What would you do with two more weeks?** Name owners and a sponsor (OQ-05, OQ-24); revoke and rotate the H3 credentials; run CI on GitHub with branch protection; run the portability test with a second model; stand up a collector and scrape a deployed instance; get one independent reviewer and one human tabletop; measure real review time to turn the cost formula into a number.

## Failure plan
If a live command fails, show the stored evidence file for that beat (all are in `evidence/`, hashed in the manifests) and say it is a replay.
