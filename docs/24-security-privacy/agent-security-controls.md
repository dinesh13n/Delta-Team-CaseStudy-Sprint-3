# Agent security controls

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | NOT APPLICABLE (justified) + guard rails |
| Evidence sources | docs/22-agentic-engineering/not-applicable.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

No agent exists (OQ-18; `docs/22-agentic-engineering/not-applicable.md`). The following guard rails prevent one from appearing unnoticed:
- the OpenAPI test fails if a new mutating route is added (K1 D-09);
- the AI persona has read-only access to `shipments` for purpose `exception_summary` and is denied writes (test);
- the saga is deterministic code, not a planner.
If an agent is introduced later, a new threat model section (tool misuse, memory poisoning, confused deputy) is required before release.
