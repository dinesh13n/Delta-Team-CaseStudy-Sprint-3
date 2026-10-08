# Evaluation cadence

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PROPOSED |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Cadence | Run | Owner role |
|---|---|---|
| Every pull request | unit tests, policy parity, prompt/model lock tests | CI |
| Every prompt/model/policy change | full evaluation, red team, security suite | AI Governance / Security |
| Daily | ETL + data drift check | Data Owner |
| Weekly | `drift_check --audit` runtime review; AI decision review | SRE / AI Governance |
| Quarterly | refresh evaluation cases with new real-world exceptions; red-team refresh; independent review | Reviewer |
No scheduler exists; each line is a duty without an executor.
