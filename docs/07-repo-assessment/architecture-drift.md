# Architecture Drift

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 7 repository assessment) |
| Runbook step | C7 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | C2-C6 documents; runbook/01-BASELINE-ASSESSMENT.md findings register; direct reading of the subtree |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- Documented: Angular portal, three AI capabilities, OPA policy, Terraform IaC (README, current-state.md).
- Actual: two TypeScript classes, one simulated summary function, a policy not referenced by any code, a `local_file` resource.
- Divergence between layers: audit and access rules differ for API versus batch paths (ADR-0001). [VF]
