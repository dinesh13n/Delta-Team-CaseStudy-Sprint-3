# Vendor inventory

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N5 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (inventory) / CONDITIONAL (critical vendors undecided) |
| Evidence sources | evidence/27-hardening/EVD-M-01-sbom-runtime.cdx.json; .github/workflows/ci.yml; Dockerfile |
| Assumptions | See body |
| Unresolved issues | OQ-01, OQ-02, OQ-07 |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

**The delivered system has no runtime vendor today.** The model is a deterministic in-process provider; there is no outbound call in the code (verified by M1 review). Critical vendors are *future* and undecided.

| Dependency | Role | Status | Criticality |
|---|---|---|---|
| Model provider | AI suggestions | **not chosen** (OQ-02/03) | critical when added |
| Target platform / cloud | hosting, secrets, storage, network | **not chosen** (OQ-01) | critical |
| Identity provider | JWKS tokens | **not chosen** (OQ-07) | critical |
| GitHub | source, CI | in use | high (development) |
| GitHub Actions (checkout v4, setup-python v5, setup-opa v2, upload-artifact v4) | CI | used in `ci.yml`, **pinned by tag not SHA**, never run | medium |
| PyPI + 21 runtime packages (FastAPI, Starlette, Pydantic, PyJWT, PyYAML, uvicorn, jsonschema, …) | runtime libraries | in use, hash-pinned, SBOM | high |
| Docker Hub `python:3.14-slim` | base image | referenced, never built, **not digest-pinned** | high |
| Open Policy Agent | policy tests | dev/CI tool | low |
| opentelemetry-api | transitive dependency; no SDK used | present | low |
