# Risk and control summary

| Field | Value |
|---|---|
| Stage | R: Executive Defence, Final PRD, Evidence Pack |
| Runbook step | R3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/23-human-control; docs/24-security-privacy; docs/25-governance |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Risk (original finding) | Control now | Test / evidence | Residual |
|---|---|---|---|
| Self-asserted role (F-17, F-19, F-20) | signed token; policy per persona/entity/field/purpose; AI endpoint authorised | `evidence/15-modernization/EVD-H-04-negative-access-tests.txt` (sha256 `c724516d79f2e15cce8017516c2a82a30c2eb663c4fe08b5cc83b181213eb2eb`) | HS256 only; no IdP |
| Prompt injection, format-string (F-22, F-23) | allow-list, delimiting, no `str.format` on data | `evidence/19-intelligence/EVD-J-03-eval-run2-after-remediation.json` (sha256 `3f729728c7e621fc037ceb2cbe9c829882f019fa74ba8119302bc8bc46bd5f3d`) | constructed payloads only |
| No guardrail, no approval (F-24, F-26) | evaluated guardrail; approval record | `evidence/23-human-control/EVD-K-01-human-control-tests.txt` (sha256 `ebd91a777fa2223e03d14f0f9a949ecafa3b80e17a0da4cf179519ccde821828`) | self-approval possible (HC-R-01) |
| Wrong record (F-30..F-32) | exact key, 404/422 | `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv` (sha256 `c78a8433c06d9266db854f14d8ee3393ff348a4dd42dc5cdd032114fc0c92b58`) | owner intent for `REC-0001` unconfirmed |
| Untraceable audit (F-43, F-44) | hash chain, correlation id, `/audit/verify` | `evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`) | local file sink |
| Secrets (F-09..F-12) | env-only; scanner in CI | `evidence/15-modernization/EVD-H-03-secret-scan.json` (sha256 `9be399823ccf9be244917852a3f19b4ee67b5e5d2c813fae5b7f4c4fd20c4dab`) | **history not rewritten, not revoked** |
| Retry storm, duplicate bookings (F-39) | ceiling 5, idempotency key | `evidence/21-integration/EVD-J-05-saga-simulation.json` (sha256 `66c0a6ef457835fb26ed61804acde5eff5cc78e3e9272c0beeb9e183ef863fe7`) | simulated carrier |
| Location-data overexposure | field masking; forbidden AI fields; log exclusion | `evidence/24-security-privacy/EVD-K-02b-security-suite-after-m1.txt` (sha256 `deebe2780f9a2931192922f3af183473ca9c1b1a2da63e1869a64b6ae1f43859`) | retention and rights undefined |

Governance: obligations mapped but regulatory scope unresolved; 12 risk acceptances proposed, 0 signed (`docs/25-governance/risk-acceptance-register.md` (sha256 `f8203bd34b108c709ff28490e241d1003a25966789e12b393e074190d634fbab`)).
