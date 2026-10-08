# Prompt registry

| Field | Value |
|---|---|
| Stage | J |
| Runbook step | J1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-H-07, apps/api/ai/registry.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Prompt | Version | File | SHA-256 | Used by |
|---|---|---|---|---|
| exception_summary | v1 | `apps/api/ai/prompts/exception_summary_v1.txt` (620 chars) | `96b454af407d1b72d729d86b7727fb43cf053bf6fa6076fd4c4d72af4cc35155` | `AiGateway` |

[VF] The registry is code (`apps/api/ai/registry.py`): `(name, version) -> file`; adding a version means adding a file and a registry row, never editing v1 in place. Each response carries `prompt_version` and `config_hash` = sha256(prompt sha | provider | provider version | max_record_tokens). With the deterministic provider the hash is `b397c28d74371723ecf697c92ce1c6e896d0f424c5893d13865213bf91e0d5a8`.
[VF] Prompt rules: data between `<data>` tags is untrusted; facts only; one JSON object; suggest-only. The data block escapes `<` and `>` so a value cannot close the tag.
Closes F-27 (no provenance): every output can be traced to prompt text and configuration.
