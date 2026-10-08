# Risk acceptance register

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | residual-security-risks.md, residual-tevv-risks.md, privacy-impact-assessment.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | all rows |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

An accepted risk has a description, an owner role, the reason, a review date and a condition that cancels the acceptance. **Acceptance by an agent is not acceptance.** Every row is "PROPOSED for acceptance" until a named person signs (OQ-05).

| ID | Risk | Reason it is tolerable now | Cancelled if | Proposed owner | Review |
|---|---|---|---|---|---|
| RA-01 | **Regulatory scope unresolved** (OQ-04): obligations unknown | pilot on synthetic data only; no real personal data | any real personal data or any hosted model | Sponsor + Compliance | before any real data |
| RA-02 | HS256 shared-secret identity (R-SEC-01) | local pilot, synthetic data | any multi-user or networked deployment | Security | before deployment |
| RA-03 | Purpose defaulting (R-SEC-04, RL-02) | one persona uses it; approval has no downstream effect | any action integration | Security | before action integration |
| RA-04 | No four-eyes on approvals (HC-R-01) | suggest-only; no action | any action integration | Product | before action integration |
| RA-05 | Approvals never expire (HC-R-03) | low impact while no action | action integration | Product | same |
| RA-06 | Builder and grader are the same agent (TEVV-R-01) | none: this is a gap | not acceptable for GO | Release approver | before R1 can be unconditional |
| RA-07 | Secrets in git history (R-SEC-02) | synthetic; rotation plan | real credentials ever used | Security | on rotation |
| RA-08 | stale_gps undetectable (no timestamp) | no assignment code consumes position | position used for assignment | Data owner | with data contract change |
| RA-09 | Real model untested (R-SEC-07, TEVV-R-02) | no real model enabled | OQ-02 closed | AI governance | before enabling |
| RA-10 | Retention and subject rights undefined (P-06, P-07) | synthetic data | real data | Compliance | before real data |
| RA-11 | Rate limit in memory (R-SEC-03) | single process | scale-out | Platform | at deployment |
| RA-12 | CI and branch protection unproven (R-SEC-08) | local gates pass | none; must be run | Repo owner | first push |

[VF] 12 risks, 0 signed. K-X6 is met by the "formally recorded as an accepted unresolved risk" route, with the signature outstanding.
