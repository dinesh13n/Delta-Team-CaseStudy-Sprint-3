# Prompt injection controls

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | apps/api/ai/sanitize.py, EVD-J-03, EVD-L-03 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | re-test with a real model |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Layer | Control | Where |
|---|---|---|
| Input | only allow-listed fields enter the prompt | gateway `_ctx` |
| Input | Unicode NFKC normalisation; zero-width/format characters (category Cf) removed; control characters removed | `sanitize.clean_text` |
| Input | `<` and `>` escaped so a value cannot close the `<data>` block | `sanitize` |
| Input | categorical fields accepted only if the value is in the entity's declared enum, else `[unrecognised]` | `clean_enum` / `load_enums` |
| Prompt | instructions state that data between tags is untrusted and no instruction in it is followed | `exception_summary_v1.txt` (locked) |
| Output | JSON only, schema-validated | gateway |
| Output | forbidden-value scan; marker scan | `_leaks` |
| Output | rendering with `textContent`; CSP | operations view |
| Blast radius | no tool, no write, human approval | K1 |

Evidence: adversarial set, 43 cases, marker leak 0.0 (run 1 was 0.4651, which drove the enum allow-list). Live: RT-07 and RT-08 against v2.
[VF] Limit: with a deterministic provider the "model" cannot follow an injected instruction at all. The controls were therefore tested mostly at the *data path*, not against a language model that might comply. A real model needs the J3/L2 evaluation repeated.
