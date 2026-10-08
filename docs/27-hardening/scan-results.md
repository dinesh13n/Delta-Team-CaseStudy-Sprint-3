# Scan results

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/27-hardening/* |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Scan | Tool and version | Scope | Result | Evidence |
|---|---|---|---|---|
| Dependency vulnerabilities | pip-audit (OSV/PyPI), `--no-deps --disable-pip` against the hash-pinned locks | 21 runtime + 57 dev packages | no known vulnerabilities | `EVD-M-01-pip-audit-runtime.json`, `…-dev.json` |
| Source security | bandit 1.9.4 | 2891 lines | 12 findings: 1 HIGH (false positive), 11 LOW | `EVD-M-01-bandit.json` |
| Secrets | `scripts/secret_scan.py` | working tree | 0 findings | H3 evidence, CI |
| Lint/types | ruff, mypy strict config | whole repo | clean (mypy: 45 source files) | CI config |
| Policy | `opa check` / `opa test` | Rego | passed at H8 (OPA 1.21.1) | H-evidence |
| IaC | none | – | **not scanned**: no IaC exists beyond a variable/output stub | – |
| Container image | none | – | **not scanned**: image never built | – |

pip-audit note: the tool was run with `--no-deps --disable-pip` because the device Python (3.10) cannot resolve 3.11+-only wheels. This is valid because the lock is fully pinned with hashes (no resolution needed), but it means transitive packages not in the lock are not examined; the lock is universal and complete by construction.
Date dependence: "no known vulnerabilities" is true on 2026-10-08 and decays.
