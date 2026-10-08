# Controlled change process

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (P-X3 met technically for prompts and models) |
| Evidence sources | tests/test_prompt_lock.py; evidence/38-handover/EVD-P-02-operator-exercises.json (SHA-256 0482bd0cf4b1edf59e04ea08f2b7ab4a6ba2d2d45fc2e423b430b1e3be6780ab) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | P-R-03 lock and prompt live in the same repository; an attacker with deploy rights defeats it |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

P-X3: untracked prompt or model change in production is **technically prevented**, not merely prohibited.

| Mechanism | Enforcement | Test |
|---|---|---|
| Prompt file edited | `registry.load()` compares SHA-256 with `prompts.lock.json`; mismatch raises and the AI gateway does not start | `test_edited_prompt_file_is_refused`, `test_gateway_construction_fails_closed_on_a_modified_prompt`, operator exercise EX-4 (observed on a running copy) |
| Prompt without a lock entry | refused | `test_missing_lock_entry_is_refused` |
| Model not listed | `registry.verify_model` raises at service construction | `test_unlisted_model_or_version_is_refused`, `test_app_start_refuses_an_unlisted_model` |
| Model version bump | refused until the lock lists it | same |
| Changing the lock files | requires a reviewed pull request (CODEOWNERS on `apps/api/ai/`) | process control; branch protection not applied |
| Provider model changed silently by the provider | **not preventable by a lock**; detected by the evaluation cadence | cadence |
| Someone with write access to the deployed filesystem edits prompt **and** lock | not prevented (integrity check is local); mitigated by an immutable image | image unbuilt |

Process: change → lock updated in the same PR → CI → evaluation → red team → AI Governance approval → release. Every response records `prompt_version` and `config_hash`, so the change point is visible in the audit.
