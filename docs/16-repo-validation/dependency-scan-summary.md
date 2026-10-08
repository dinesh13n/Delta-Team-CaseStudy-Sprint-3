# Dependency scan summary

| Field | Value |
|---|---|
| Stage | H |
| Runbook step | H11 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (Python), CONDITIONAL (npm) |
| Evidence sources | EVD-H-11-dependency-audit |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

[VF] `pip-audit` over the hash-pinned runtime+dev lock: 21 dependencies, 0 known vulnerabilities (EVD-H-11-dependency-audit.json, 2026-10-08). The audit depends on the advisory database at run time; re-run at each release.
[VF] Locks regenerated with `uv pip compile --universal --python-version 3.11 --generate-hashes`; install verified on 3.14.7 and 3.11.
[UNK] npm: `apps/web/package-lock.json` exists but `npm audit` was not run in this sandbox; the web app is a scaffold with no runtime dependencies in use (CONDITIONAL).
[UNK] SBOM and provenance: M1.
