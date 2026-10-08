# Vendor risk acceptance

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | BLOCKED (no accepting owner) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | OQ-05 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Risk | Proposed acceptance | Accepted by |
|---|---|---|
| Base image and Actions not pinned by digest/SHA | accept for the candidate; fix before first deploy | **nobody** (OQ-05) |
| H3 credentials in git history not revoked | **not acceptable to leave**; revoke | nobody |
| pip-audit not run in the 3.14 target environment | accept until CI runs | nobody |
| No vendors chosen | n/a: block production until chosen | nobody |

No acceptance has been signed. The register in `docs/25-governance/risk-acceptance-register.md` stays at 0 of 12 signed.
