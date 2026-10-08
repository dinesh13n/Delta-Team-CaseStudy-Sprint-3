# Security test results

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | EVD-K-02, EVD-L-03 |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | SEC-G-01 chunked bodies |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Evidence: `evidence/24-security-privacy/EVD-K-02-security-suite.txt` (24 tests at capture), `evidence/26-tevv/EVD-L-03-*`.

| Run | Result |
|---|---|
| Security suite at K3 capture | 24 passed |
| Security suite after adding the body-size test (K3 follow-up) | 25 passed |
| Security suite after the docs-endpoint hardening (M1) | 26 passed; full suite 160 passed, 7 xfailed |
| Red team v2 | 0 of 12 |
| Red team baseline | 10 of 12 (RT-08, RT-10 not applicable) |
| Secret scan | clean (allow marker on `process.env.E2E_TOKEN` only) |

## Findings fixed in K3
| ID | Finding | Fix |
|---|---|---|
| SEC-G-01 | security-spec item 6 (64 KiB request limit) was **not implemented** | Content-Length cap with 413 and a test. Chunked requests without Content-Length are not covered; the platform proxy should cap them. |
| SEC-G-02 | `test_identity_headers…` assumed a persona masks `customer_id` that does not | test corrected to a dispatcher token |
| SEC-G-03 (M1) | `/docs`, `/redoc`, `/openapi.json` were served in every environment | disabled unless `APP_ENV=local`; test added (26 security tests) |

[VF] A spec that said "yes" while the code said "no" was found by reading, not by a test: security specs need a test per line.
