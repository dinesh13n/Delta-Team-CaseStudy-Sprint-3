# Environment and Toolchain Snapshot

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation (Spine 0A to 0C), runbook step A3 |
| Runbook step | A3 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, closed with recorded unknowns |
| Evidence sources | evidence/00-preflight/EVD-A-03-toolchain-snapshot.txt (SHA-256 b9bc4bf6585621edcdd934895f923a0e2d4a643e0c5fed30c418715993b3231f) |
| Assumptions | The sandbox is the build/test environment until OQ-01 (platform) is answered |
| Unresolved issues | OQ-01 platform, OQ-03 egress policy; Windows host facts unknown |
| Residual risks | Tests cannot run until dependencies are installed; CI/sandbox Python versions differ |

## 1. Scope
Read-only snapshot of the cloud sandbox where Stages A to G will run. Nothing was installed or changed.

## 2. Verified Facts (sandbox, from EVD-A-03)
- OS Ubuntu 22.04.5; Python 3.10.12; Node v22.23.2; npm 10.9.8; git 2.34.1; 2 CPUs; about 2.9 GB RAM.
- Present: make, jq.
- Absent: terraform, opa, docker, podman, syft, trivy, grype, gitleaks, ruff, mypy, pytest, uvicorn, playwright.
- Repo dependency state:

| Package | Pinned | Installed |
|---|---|---|
| fastapi | 0.115.0 | MISSING |
| uvicorn | 0.30.6 | MISSING |
| pydantic | 2.8.2 | MISSING |
| pytest | 8.3.2 | MISSING |
| python-dotenv | 1.0.1 | 1.2.3 (drift) |
| PyYAML | 6.0.2 | 6.0.3 (drift) |
| httpx | not pinned | MISSING (needed by tests/test_api_contract.py, finding F-02) |

- CI (.github/workflows/ci.yml) uses Python 3.11; sandbox has 3.10.12.

## 3. Inferences
- Stage C behavioural baseline needs a venv with pinned deps plus httpx; CI uses Python 3.11 and the host default is 3.11.9.
- Terraform, OPA, container, SBOM and secret-scan steps (later stages) need tools installed, or an alternative runner, before they can produce evidence. Network egress for installs is governed by OQ-03.

## 3a. Windows host (Verified Facts, EVD-A-03b, operator-pasted)
- Windows 10.0.26200.9457. Default `python` is 3.11.9 (first on PATH); Python 3.14, 3.12, Anaconda and the Store stub also on PATH. pip 24.0 (under 3.11).
- Node v26.8.1 (sandbox has v26.11.1, so host is behind); npm 11.19.0.
- EVD-A-03d: Python 3.14.7 and 3.11.9 via `py` launcher; git 2.35.1.windows.2 (old; sandbox has 2.34.1); Node still v26.8.1 (upgrade not yet applied or not yet picked up).
- Inference: host default 3.11.9 suits the Stage C baseline; 3.14 is available for the target runtime. Install it into venvs, not globally.

## 3b. Operator statement (EVD-A-03e) - Inference, unverified
- Operator reports empty output from the tool-presence check: terraform, opa, docker, syft, trivy, gitleaks, ruff, mypy, make, gh treated as ABSENT on the host.
- core.autocrlf reported unset at all levels, which conflicts with the CRLF to LF change seen at the baseline commit. Unresolved; baseline is protected by .gitattributes regardless.
- Node version after upgrade unconfirmed (last seen v26.8.1).

## 4. Unknowns
- Windows host: effective core.autocrlf (global printed nothing; the 'for' line errored), presence of terraform/opa/docker/syft/trivy/gitleaks/ruff/mypy/make/gh, exact Python 3.14/3.12 versions. (Host terminal tool failed with WinError 267; operator pasted partial output as EVD-A-03b.)
- Whether the target platform (OQ-01) offers Docker/Terraform runners.

## 4a. Runtime upgrade (operator request: Python 3.14, latest Node)
Verified Facts from EVD-A-03c:
- Sandbox now also has Python 3.14.6 and 3.11.15 (via uv) and Node v26.11.1. System Python 3.10.12 left in place.
- Delivered pins FAIL on 3.14 (pydantic 2.8.2 / pydantic-core 2.20.1 has no 3.14 wheel). They pass on 3.11 with httpx added.
- Unpinned latest packages install on 3.14 (fastapi 0.142.4, pydantic 2.13.5).
Decision needed (logged as D-006): Stage C baseline runs on 3.11 (matches CI, keeps pins untouched, preserves byte-exact baseline). 3.14 and the upgraded pins become the target from Stage H, after write authorisation (OQ-11).

## 5. Exit check
Evidence file exists, hashed, listed in evidence/00-preflight/MANIFEST.md. Windows section remains open.
