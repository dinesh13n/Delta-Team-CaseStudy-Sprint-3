# Transformation risks

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/14-transformation; characterization tests EVD-C-08 |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Risk | L | I | Mitigation |
|---|---|---|---|---|
| TR-01 | Behaviour change breaks a consumer of the old API | M | M | compatibility keys kept; difference report; flags |
| TR-02 | Authorisation is operator-only, not owner-signed | H | H | recorded in G4 as a condition; CTO ratification requested |
| TR-03 | Python 3.14 compatibility surprises | M | M | CI matrix 3.11 and 3.14 (ADR-0003) |
| TR-04 | Synthetic-data results overstate quality | H | M | label all results synthetic; DR-01 |
| TR-05 | Fixture accidentally modified | L | H | TG-6 each increment |
| TR-06 | opa or terraform binaries unavailable, so policy/IaC checks stay CONDITIONAL | M | M | parity test in Python; state CONDITIONAL honestly |
| TR-07 | Scope creep into feature work | M | M | sequence classes; MVP scope |
| TR-08 | AI quality cannot be demonstrated without a real model | H | M | deterministic default; CONDITIONAL in J/L |
