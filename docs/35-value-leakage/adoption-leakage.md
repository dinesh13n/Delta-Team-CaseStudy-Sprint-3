# Adoption leakage

| Field | Value |
|---|---|
| Stage | O |
| Runbook step | O2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (identified) / unquantified |
| Evidence sources | docs/23-human-control |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Adoption cannot leak where there is no adoption to lose. Pre-conditions for adoption that do not exist: named users and roles from an IdP, onboarding, an explanation of the suggestion's facts beside the text (OPT-06), a reviewer workload agreement, a feedback route. The human-control design assumes a competent reviewer with time; if review becomes a rubber stamp (HC-R-01), the control exists on paper and value leaks into risk.
