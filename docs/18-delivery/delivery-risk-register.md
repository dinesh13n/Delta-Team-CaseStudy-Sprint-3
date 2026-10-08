# Delivery risk register

| Field | Value |
|---|---|
| Stage | I |
| Runbook step | I2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Risk | L | I | Mitigation | Owner |
|---|---|---|---|---|---|
| DR-1 | No named approvers: gates stay provisional | H | H | operator attestation recorded; ask sponsor to name | Delivery lead |
| DR-2 | Agent grades its own work | H | M | independent review step recommended; sign-off notes the gap | Delivery lead |
| DR-3 | No real model: AI quality claims limited to deterministic path | H | M | label claims; Stage Q BLOCKED | AI lead |
| DR-4 | CI never executed on platform | M | M | run on first push | Repository Owner |
| DR-5 | Secret-shaped values in public history | M | H | rotation plan | Repository Owner |
| DR-6 | Synthetic data only: KPI after-values are fixture proxies | H | M | label as proxy | Business analyst |
