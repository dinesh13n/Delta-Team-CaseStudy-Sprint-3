# Hardening plan

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (with CONDITIONAL items) |
| Evidence sources | evidence/27-hardening/* |
| Assumptions | See body |
| Unresolved issues | OQ-01 platform |
| Residual risks | M-R-01..M-R-05 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Area | Baseline weakness | Hardening done | Evidence | Status |
|---|---|---|---|---|
| Identity | role taken from a self-asserted header (F-17) | verified bearer JWT, required `exp`/`sub`/role, 60 s leeway, `legacy_header` refused outside local | 27 security tests | DONE; HS256 only (R-SEC-01) |
| RBAC | any persona string accepted (F-19) | deny-by-default policy from YAML, generated Rego, parity test | policy tests | DONE |
| Secrets | credentials in code, `.env.example`, Terraform (F-09..F-15) | removed, env-only, scan, placeholders | `secrets-hardening.md`, H3 scans | DONE; history exposure accepted (OQ-19) |
| Network | none defined | single port 8000; no outbound calls in code; platform firewall not defined | Dockerfile | CONDITIONAL (OQ-01) |
| Runtime | debug logging default (F-13), docs open everywhere | `LOG_LEVEL=INFO`; `/docs`, `/redoc`, `/openapi.json` off outside local; `Cache-Control: no-store` and `nosniff` on API; non-root container user; HEALTHCHECK | tests, Dockerfile | DONE in code; image never built (no container runtime) |
| Infrastructure | Terraform emitted a credential file (F-15) | resource removed; module emits no credential | `infra/terraform/main.tf` | **BLOCKED**: no platform, so no real IaC (M-X2) |
| Dependencies | no lock, no scan | hash-pinned requirements (`uv pip compile --generate-hashes`), `--require-hashes` in CI and Dockerfile, pip-audit 0 findings | `EVD-M-01-pip-audit-*.json` | DONE |
| APIs | unbounded page, body, rate | page ≤ 100, body ≤ 64 KiB (Content-Length), AI rate limit | tests | DONE |
| CI/CD | no gates | ruff, format, mypy, secret scan, tests with coverage floor, OPA check, sanity, evidence artefacts; `permissions: contents: read` | `ci.yml` | DONE as code; **never ran on GitHub** |
| Build artefacts | none | SBOM (CycloneDX 1.5) for runtime and dev | `EVD-M-01-sbom-*.cdx.json` | DONE; no signing or provenance attestation |
| Supply chain | no provenance | hashes pinned, SBOM, CODEOWNERS; no SLSA attestation | `supply-chain-controls.md` | PARTIAL |
