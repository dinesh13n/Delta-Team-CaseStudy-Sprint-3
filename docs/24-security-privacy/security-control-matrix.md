# Security control matrix

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | tests |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | C-16 CI unproven |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Control | Objective | Implemented at | Automated test |
|---|---|---|---|
| C-01 Bearer JWT verification | identity | `security/tokens.py` | yes |
| C-02 Policy-as-code authorisation | least privilege | `security/policy.py` + generated Rego | parity tests |
| C-03 Field masking | privacy | policy overrides | yes |
| C-04 Key patterns and exact lookup | integrity | `data/repository.py`, `check_key` | yes |
| C-05 Curated/quarantine layers | data quality | ETL | yes |
| C-06 AI context allow-list | privacy | gateway + `ai-context-policy.yaml` | eval |
| C-07 Sanitiser + enum allow-list | injection | `ai/sanitize.py` | eval, unit |
| C-08 Output validation + leak check | exfiltration | gateway | eval |
| C-09 Prompt lock | integrity | `registry.py` | yes |
| C-10 Human approval record | agency | `approvals.py`, decision route | yes |
| C-11 Rate limit | availability | `main.py` | yes |
| C-12 Body size cap | availability | `main.py` | yes |
| C-13 Timeout + breaker | availability | `resilience.py` | yes |
| C-14 Hash-chained audit | accountability | `audit_chain.py` | yes |
| C-15 Correlation id (validated) | traceability | `correlation.py` | yes |
| C-16 Secret scan | secrets | `scripts/` + pre-commit + CI | yes |
| C-17 CSP etc. on `/ops` | XSS | middleware | yes |
| C-18 Error hygiene | disclosure | `errors.py` | yes |

[ASM] C-16 in CI and branch protection have never run on GitHub (H12).
