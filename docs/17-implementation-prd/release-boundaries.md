# Release boundaries

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | docs/09-initial-prd/mvp-scope.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Release | Contents | Entry condition | Exit condition |
|---|---|---|---|
| R0 (done) | Stage H hardening | G gate | `repo/v2-validated` |
| R1 (this delivery) | thin view, saga library, TEVV, supply chain, resilience, observability, handover | I gate | Stage R decision |
| R2 (conditional) | real model, real IdP, external audit sink, CI on platform | OQ-02, OQ-03, OQ-07 resolved | production readiness review |
| R3 (future) | ETA, route optimisation, portal, agents | real history, owner approval | new PRD |

Not in any release now: agentic behaviour (L0 only).
