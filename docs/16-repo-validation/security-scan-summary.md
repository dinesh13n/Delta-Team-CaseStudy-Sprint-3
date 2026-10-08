# Security scan summary

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H11 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS with conditions |
| Evidence sources | EVD-H-03, EVD-H-04, EVD-H-11-static-analysis |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Check | Result | Evidence |
|---|---|---|
| Secret scan, working tree | 0 findings | EVD-H-03-secret-scan.json |
| Secret scan, history | 10 findings, all in 7ba349e; disposition in secrets-hardening.md | EVD-H-03-secret-scan-history.json |
| Negative access tests | 16 passed (no token, bad token, expired, wrong role, field masking, AI endpoint, scope) | EVD-H-04-negative-access-tests.txt |
| Policy allow/deny matrix | 8 personas x resources x actions exported | EVD-H-04-policy-allow-deny-matrix.csv |
| Static analysis (ruff) | clean | EVD-H-11-static-analysis.txt |
| SAST beyond ruff (bandit/semgrep) | NOT RUN [UNK] | to K3 |
| Container image scan | NOT RUN: no container runtime | M1 |

Known limits: JWKS verifier is a fail-closed stub (OQ-07); scope narrowing (hub/fleet) is reported but not enforced because the data has no such attributes.
