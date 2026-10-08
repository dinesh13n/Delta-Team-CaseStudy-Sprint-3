# Third-party risk assessment

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | evidence/27-hardening/pip-audit-runtime.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | N-R-17 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Risk | Dependency | Likelihood / impact (judgement) | Control in repo | Gap |
|---|---|---|---|---|
| Malicious or vulnerable package | PyPI libraries | medium / high | hash-pinned locks, `--require-hashes`, pip-audit 0 findings at 2026-10-08, SBOM | no scheduled re-scan; no signing/provenance |
| Compromised CI action | GitHub Actions | low-medium / high | `permissions: contents: read` | actions pinned by tag, not commit SHA |
| Base image drift | `python:3.14-slim` | medium / medium | none | not digest-pinned; image never built or scanned |
| Secret exposure via history | git history (H3 credentials) | **realised** | removed from tree | **not revoked** (owner action, P-X5) |
| Model provider data use | future | unknown / high | ai-context-policy forbids customer identifiers, output leak check | contract unknown |
| Provider outage | future | medium / medium | timeout, breaker, deterministic fallback, kill switch | tested with fakes only |
| IdP outage | future | medium / high | fail-closed JWKS stub | no cache or grace policy designed |

pip-audit ran with `--no-deps --disable-pip` on the locked files (resolution failed on Python 3.10); a scan in the real 3.14 environment is open.
