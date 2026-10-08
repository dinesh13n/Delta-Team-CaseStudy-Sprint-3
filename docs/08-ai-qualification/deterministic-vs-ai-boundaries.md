# Deterministic versus AI Boundaries

| Field | Value |
|---|---|
| Stage | E: Intervention Qualification and Initial PRD (Spine 8-9) |
| Runbook step | E1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/03-problem-value/; docs/06-root-cause/; docs/07-repo-assessment/; semantic-layer/business-rules.yaml; docs/00-preflight/ai-economics/ |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Rule: the model may only **suggest text**; it never decides identity, access, validity, routing or booking.

| Concern | Owner | Why |
|---|---|---|
| Which record is shown | deterministic | exact key |
| Who may see which fields | policy engine | semantic access rules |
| What enters the prompt | deterministic context builder (allow-list) | ai-context-policy.yaml |
| Summary wording and next-step suggestion | model (optional) | language task |
| Whether a suggestion becomes an action | human approval | A5 approval rules |
| Fallback when the model is down or output invalid | deterministic template | availability |
Rejected AI use (E-X2): I5 route-restriction enforcement and I1/I2/I3/I4/I6, each moved to deterministic mechanisms.
