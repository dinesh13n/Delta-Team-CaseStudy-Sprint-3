# Problem Framing Canvas

| Field | Value |
|---|---|
| Stage | B: Problem Framing (Spine 3) |
| Runbook step | B3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/*; docs/00-preflight/operating-contract/*; docs/00-preflight/stage-a-gate.md; docs/01-engagement/*; docs/domain-specific-spec.md (repo) |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-08, OQ-24 |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Element | Content |
|---|---|
| Symptom | Operators receive records and recommendations that cannot be traced or trusted |
| Root problem (hypothesis) | Identity, data meaning and decision history are not defined or recorded consistently across old and new code paths (to be confirmed in Stage C) |
| Proposed solution (not assumed) | None yet; options are weighed in Stage E |
| Assumed need for any particular technology | Not assumed |
| Who is affected | the eight personas in personas.md |
| Evidence | A4 pack: duplicate keys and blank rows in every dataset, 983 of 3,000 events without a correlation id, role taken from a request header, first row returned on a missed lookup |
