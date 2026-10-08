# Deterministic vs AI boundary (as built)

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | docs/08-ai-qualification/deterministic-vs-ai-boundaries.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Decision | Mechanism | Deterministic? |
|---|---|---|
| Who may see what | PolicyEngine / Rego | yes |
| Which fields enter a prompt | ai-context-policy allow-list + enum gate | yes |
| Is the output acceptable | JSON schema + forbidden-value filter + confidence floor | yes |
| Abstain or answer | gateway rules | yes |
| Wording of the summary | provider (deterministic today; a model later) | the only probabilistic step, once a model exists |
| Act on the suggestion | **never by the system**; human approval endpoint only | n/a |
The model, when present, can only produce text that passes the deterministic checks; it has no tools, no writes and no memory (L0).
