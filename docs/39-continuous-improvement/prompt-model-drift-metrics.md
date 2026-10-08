# Prompt and model drift metrics

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (controls) / CONDITIONAL (no live model) |
| Evidence sources | apps/api/ai/registry.py; tests/test_prompt_lock.py |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Metric | Control | Threshold |
|---|---|---|
| Prompt hash | lock file; service refuses a mismatch | any difference = CHANGE-BLOCK |
| Model identity | `models.lock.json`; service refuses unlisted | any difference = CHANGE-BLOCK |
| Config hash in each response | binds prompt, provider, version, token cap | recorded in audit |
| Evaluation pass | thresholds from J2 (schema 100%, leaks 0, abstention 100%, approval flag 100%) | any failing safety case = CHANGE-BLOCK |
| Fallback rate | audit | > 20% with at least 30 requests = INVESTIGATE |
| Reject share | audit | > 50% with at least 30 decisions = INVESTIGATE |
| Blocked leaks | audit and alert | ≥ 1 = INVESTIGATE / page |
Provider-side silent model updates cannot be seen by a lock: pin the exact version where the provider allows it, and rely on the evaluation cadence to catch behaviour shifts.
