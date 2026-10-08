# Runtime hardening

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (code) / CONDITIONAL (image) |
| Evidence sources | Dockerfile, docker-compose.yml |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | M-R-02 image unbuilt |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Control | Where | Verified |
|---|---|---|
| Container runs as non-root uid 10001 | `Dockerfile` | read only: **image not built** (no container runtime in the sandbox) |
| Base image `python:3.14-slim`; no build tools in the runtime layer | `Dockerfile` | read only |
| Dependencies installed with `--require-hashes` | `Dockerfile` | the same lock is installed by CI and was audited |
| No secrets in the image or `docker-compose.yml` (`AUTH_SECRET` must come from the environment) | files | read; scan clean |
| `APP_ENV=prod` default in the image, so start-up fails without `AUTH_SECRET` | `config.validate` | tested via config tests |
| One port (8000), no shell entrypoint | `Dockerfile` | read |
| HEALTHCHECK on `/health` | `Dockerfile` | read only |
| API docs off outside local; `Cache-Control: no-store`; `nosniff`; CSP on `/ops` | `main.py` | tested |
| Logs: JSON, correlation id, no tokens | `main.py` | tested for secrets absent from metrics/ready/openapi |
| Writable paths limited to `logs/` | `Dockerfile` | read |

Recommended for the platform (not enforceable here): read-only root filesystem, drop all capabilities, CPU/memory limits, no outbound network except the IdP and the model endpoint, TLS at the edge, HSTS.
[VF] Because the image was never built, none of the container controls is evidence of a working container; they are configuration that must be validated on a platform with Docker (backlog DB-13).
