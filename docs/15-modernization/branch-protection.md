# Branch protection and review gate (policy + required settings)

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL (settings not applied; needs GitHub admin) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | Owner to apply settings (OQ-05) |
| Residual risks | TR-02 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

[VF] `CODEOWNERS`, PR template and `ci.yml` exist in the repository. [UNK] Whether GitHub branch protection is enabled: the agent has no repository admin access and could not verify.

Required settings on `main` (to be applied by the Repository Owner):
- Require pull request with 1 review from CODEOWNERS; dismiss stale approvals.
- Required status checks: `lint`, `typecheck`, `test (3.11)`, `test (3.14)`, `secret-scan`, `rego`, `openapi-route-diff`.
- Block force pushes and deletions; require linear history; require signed commits [ASM, recommended].
- Tags `baseline/*`, `repo/*`, `release/*` protected from deletion.

Why CONDITIONAL: F-08 is remediated in files, not in enforcement.
