# Supply chain controls

| Field | Value |
|---|---|
| Stage | M |
| Runbook step | M1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PARTIAL |
| Evidence sources | supply-chain/dependency-risk-register.md, .github/workflows/ci.yml |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | no provenance attestation |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Control | State | Gap |
|---|---|---|
| Pinned versions with hashes | yes | – |
| Single trusted index (PyPI), no extra index | yes | no mirror or proxy policy |
| SBOM | yes, CycloneDX 1.5, runtime + dev | generated from the lock file, so it has names and versions but **no licences or hashes per component** |
| Vulnerability scanning | pip-audit on both locks: 0 known | scan covers only the known-vulnerability database at scan time |
| Source scanning | bandit on `apps etl scripts evaluation` (2891 lines): 12 findings, all dispositioned | – |
| Secret scanning | working tree clean; history has 10 findings (baseline commit) | accepted, OQ-19 |
| Provenance / build attestation | **none**: there is no build pipeline run to attest | needs CI on GitHub plus a signing step |
| Code review | CODEOWNERS present | branch protection never enabled/tested |
| Reproducible build | lock is deterministic; image never built | – |
| Third-party GitHub Actions | pinned by tag (`@v4`, `@v5`, `@v2`), not by commit SHA | pin by SHA before production |
