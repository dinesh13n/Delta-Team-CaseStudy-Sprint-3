# Dependency hardening

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | requirements*.txt, EVD-M-01-sbom-* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

- `requirements.in` / `requirements-dev.in` hold direct dependencies; `requirements*.txt` are compiled with hashes for Python 3.11+ (`--universal`), so the lock works on 3.11 and 3.14 (both tested).
- Runtime set: 21 packages; dev set: 58 components in the SBOM.
- Update policy [ASM]: weekly `pip-audit`, monthly refresh, immediate for a vulnerability with a fix; each refresh re-runs the full suite and the evaluation.
- No dependency was added for this stage's code (`resilience.py` is standard library only).
- Observed oddity: the runtime lock lists `opentelemetry-api` as a dependency "via fastapi". It is installed but not imported by the application. Recorded in the vulnerability register as an inventory item, not a finding.
- `requirements-dev` includes scan tools only in the scan environment (`venv_scan`), not in the product lock, so the product lock stays minimal.
