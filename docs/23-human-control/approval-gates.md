# Approval gates

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | apps/api/main.py |
| Assumptions | See body |
| Unresolved issues | OQ-05 |
| Residual risks | HC-R-01..03 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Gate | Who | Mechanism | Tested |
|---|---|---|---|
| AG-1 Accept an AI suggestion | dispatcher with purpose `dispatch` | decision endpoint, policy `shipments:write` | yes |
| AG-2 Change a prompt version | code owner (pull request) | prompt lock | yes |
| AG-3 Change access rules | security owner (pull request) | parity test must pass | yes |
| AG-4 Turn on a real model | AI governance owner | env setting plus model card update | partly (falls back when unconfigured) |
| AG-5 Release | release approver | R1 decision, CI | CI never ran on GitHub (see Stage H) |

## Known weaknesses (honest)
- **HC-R-01 No separation of duties.** The same dispatcher who requested a suggestion can approve it. For a *suggest-only* pilot that is acceptable; for any action integration, a different approver (four-eyes) should be required. The approval record stores requester and decider, so the check is a small change.
- **HC-R-02 Purpose defaulting.** A token with no `purpose` is treated as having the persona's first declared purpose (RL-02). For a dispatcher that includes `dispatch`, so a purpose-less dispatcher token can approve.
- **HC-R-03 No expiry.** A pending suggestion stays decidable forever; an old suggestion could be approved after the shipment moved on.
- Named approvers do not exist (OQ-05): the gates are roles, not people.
