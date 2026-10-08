# SBOM summary

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS |
| Evidence sources | evidence/27-hardening/EVD-M-01-sbom-*.cdx.json |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Item | Value |
|---|---|
| Format | CycloneDX 1.5 JSON |
| Tool | cyclonedx-py 7.5.0 (cyclonedx-bom 7.5.0) |
| Generated | 2026-10-08 (UTC) from `requirements.txt` and `requirements-dev.txt` |
| Runtime SBOM | `EVD-M-01-sbom-runtime.cdx.json`, 21 components |
| Dev SBOM | `EVD-M-01-sbom-dev.cdx.json`, 58 components (37 beyond runtime) |

## Runtime components
annotated-doc 0.0.5, annotated-types 0.8.0, anyio 4.15.1, attrs 26.1.0, click 8.5.0, fastapi 0.142.4, h11 0.16.0, idna 3.20, jsonschema 4.26.0, jsonschema-specifications 2025.9.1, opentelemetry-api 1.45.1, pydantic 2.13.5, pydantic-core 2.46.5, pyjwt 2.15.1, pyyaml 6.0.3, referencing 0.37.0, rpds-py 2026.9.1, starlette 1.7.0, typing-extensions 4.16.0, typing-inspection 0.4.4, uvicorn 0.54.0.

## Limits
- Built from the lock file, not from an installed environment: no licence data, no file hashes in the SBOM.
- The application's own code is listed only as the root component; the evaluation datasets and the prompt (`prompts.lock.json`) are not SBOM items.
- **No AI model is in the SBOM because there is none.** A real model would need an "ML-BOM" entry (name, version, provider, licence, training-data statement).
