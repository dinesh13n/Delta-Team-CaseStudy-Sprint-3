# Human override policy

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (policy) / CONDITIONAL (operation) |
| Evidence sources | docs/18-delivery/delivery-backlog.md (DB-12) |
| Assumptions | See body |
| Unresolved issues | BR-06 override authority |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- A human may **reject** any suggestion with no justification required; a reason is optional and stored. A human may **ignore** a suggestion by not deciding.
- A human cannot override: the key-pattern check, the policy engine, the forbidden-field rule, the audit write. These are not user options; changing them requires a code/config change under AG-2/AG-3.
- A human may **disable the AI** at any time (`AI_ENABLED=false`); the operations view continues without summaries.
- A human override of the *deterministic recommendation* (e.g. dispatching despite a restricted-zone flag) happens outside the system today. It is **not recorded**. Recording an override with a reason is a backlog item (DB-12) and is the prerequisite for BR-06 to be enforceable.
- No override may be applied silently: any change to a decision after the fact is a new audit event, never an edit (hash chain).

[VF] Implemented: reject, ignore, kill switch, immutable audit. [UNK] Who may override a restricted-zone rule: owner ruling (BR-06) outstanding.
