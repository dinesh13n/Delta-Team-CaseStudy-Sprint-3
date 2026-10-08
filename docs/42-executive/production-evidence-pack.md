# Production Evidence Pack

| Field | Value |
|---|---|
| Stage | R |
| Runbook step | R2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft; independent review absent |
| Evidence sources | evidence/ (111 manifest rows, all hashes verified); PRODUCTION_EVIDENCE_PACK_TEMPLATE.md |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

This is the delivered `PRODUCTION_EVIDENCE_PACK_TEMPLATE.md` populated: the fifteen headings are the template's own, in its order. Each claim cites an evidence file by path and SHA-256. Every hash was verified against its `MANIFEST.md` on 2026-10-08 (`evidence/EVIDENCE-INDEX.md`). A claim with no file is marked **NO EVIDENCE**. Status words: MET, PARTIAL, NOT MET.

## Release Summary
- Release candidate `release/v1-production-candidate` (tag created in R5). Production release **not performed**; pilot release **not performed**; no environment exists (`docs/30-release/release-outcome.md` (sha256 `f6a82aeadf625e80c38dfb50b8b0e15093343dc6cd4519cb610fdb295d3ce463`)).
- Decision: NO-GO production on real data; CONDITIONAL GO controlled pilot on synthetic data (`docs/42-executive/production-readiness-decision.md` (sha256 `10af5d5ed2dd0e61fe526c31a4ae67c2607544ba42591553c8f7ea45e7b29fa0`)).
- Findings: 62 (57 in the baseline register plus F-58..F-62). Final dispositions: 43 fixed, 4 fixed in tree with history residual, 10 partial, 2 changed, 2 deferred, 1 proposed-accepted, 0 unaddressed (`evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv` (sha256 `24dc4df12754670d842a7f1d8fb2d8dfa03eb8214dd35758a7e26577a6e774d1`)).

## Behavioural Baseline Evidence
- Quick-start fails on the delivered baseline: `pytest -q` exits 2 (no `httpx`); `uvicorn apps/api.main:app` fails with `No module named 'apps/api'` (`evidence/07-repo-assessment/EVD-C-02-quickstart-transcript.txt` (sha256 `74e85bd8cec2ade87fc4ccf8a95b40552928010bfd689e761b21868fdf541581`)). MET.
- Baseline suite after adding `httpx` in a throwaway venv: 3 passed, coverage 45% of 98 statements (`evidence/07-repo-assessment/EVD-C-03-junit.xml` (sha256 `1d96dc44eb81588a1155ba4566d8d87ab7ef22d62ba21b803f7835d3926ca8da`); `evidence/07-repo-assessment/EVD-C-03-coverage.xml` (sha256 `85210479df1b835c07459cca3a26494695ede817d7399bc85133811e92b607e8`)).
- Behaviour pinned before change: 12 characterization tests covering the 11 behaviours; 5 stay green and 7 are marked approved-change xfail (`evidence/07-repo-assessment/EVD-C-08-characterization-junit.xml` (sha256 `b35040581e79ee0e1b912f8399b855e60ef591ad76c24faa27eb7c0169ffd90e`)). Before/after probes P1-P9 (`evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv` (sha256 `c78a8433c06d9266db854f14d8ee3393ff348a4dd42dc5cdd032114fc0c92b58`)).
- Data profile (6 CSVs of 354 rows, 3,000 events) and KPI proxies (`evidence/04-baseline-kpis/EVD-C-05-data-profile.json` (sha256 `6314f00faa1df6c781714c3be2e946cae1b323858f1b435868989a8f4dced202`)). Fixture bytes unchanged: the seven `data/synthetic` files are byte-identical to the baseline tag (verified 2026-10-08; EVD-A-01 manifest).

## IAM and Least Privilege Evidence
- Header-asserted role replaced by signed bearer token; policy decision per persona, entity, field and purpose; denial audited. 16 negative-access tests (`evidence/15-modernization/EVD-H-04-negative-access-tests.txt` (sha256 `c724516d79f2e15cce8017516c2a82a30c2eb663c4fe08b5cc83b181213eb2eb`)); allow/deny matrix (`evidence/15-modernization/EVD-H-04-policy-allow-deny-matrix.csv` (sha256 `f838baffa93da9043a972b23f70f36a84f9442848d2805d4a2d029f4a96ad25a`)). MET for the local model.
- NOT MET: no real identity provider (HS256 shared secret, JWKS stub; OQ-07, RA-02); hub/fleet scope not enforceable (DEBT-05).

## Secrets and Encryption Evidence
- Working tree: 0 secret findings (`evidence/15-modernization/EVD-H-03-secret-scan.json` (sha256 `9be399823ccf9be244917852a3f19b4ee67b5e5d2c813fae5b7f4c4fd20c4dab`)). MET.
- Git history: **10 findings remain; nothing revoked** (`evidence/15-modernization/EVD-H-03-secret-scan-history.json` (sha256 `473b47bb982b7ab65985c869a7f35068253b7c3719d610e9ad90ed8f85849a4c`)). The repository is public. NOT MET (RA-07, GOV-07).
- Encryption in transit and at rest: **NO EVIDENCE**; deferred to an undecided platform (F-16, GAP-01).

## IaC Evidence
- NOT MET. `infra/terraform/main.tf` no longer emits a credential but provisions nothing; no provider, backend or state (F-48, M-X2). Container recipe exists (Dockerfile, compose, entrypoint) and was exercised from a clean copy (`evidence/38-handover/EVD-P-02-operator-exercises.json` (sha256 `0482bd0cf4b1edf59e04ea08f2b7ab4a6ba2d2d45fc2e423b430b1e3be6780ab`)) but the image was never built.

## Policy-as-Code Evidence
- Rego generated from `access-semantics.yaml`; `opa check` and `opa test` (7 of 7) pass; the Python policy engine is in the request path (`evidence/16-repo-validation/EVD-H-11-static-analysis.txt` (sha256 `a133801206f5d18f1b8a2a73b357919ecee21be91088555fcfe65cc6f14ee960`); CI run 2 `evidence/15-modernization/EVD-R-02-ci-run-2-green.txt` (sha256 `ecc80c2198e52f243b4fad863caae96b5c55ec8c2d8c9f451f5306e8222a6b28`)). MET. Limit: OPA is not in the request path; parity is by test.

## CI/CD and Supply Chain Evidence
- GitHub Actions ran twice: run 1 failed at the coverage gate, run 2 green on Python 3.11 and 3.14 (`evidence/15-modernization/EVD-R-02-ci-run-1-failed.txt` (sha256 `23711892040269c52df2765ce8ae5dfa695369196cf274543ce27f000826a70c`); `evidence/15-modernization/EVD-R-02-ci-run-2-green.txt` (sha256 `ecc80c2198e52f243b4fad863caae96b5c55ec8c2d8c9f451f5306e8222a6b28`)). PARTIAL: CI lacks SAST, dependency audit and SBOM steps; branch protection off; CI artifacts exist on GitHub but could not be downloaded from this workspace.
- SBOM CycloneDX runtime (`evidence/27-hardening/EVD-M-01-sbom-runtime.cdx.json` (sha256 `7b6b270a171dbb86fec07b9dd599d04792188e95a3b08805269d0f15e4c34395`)) and dev (`evidence/27-hardening/EVD-M-01-sbom-dev.cdx.json` (sha256 `34d4a0df90df63d0c2ae3cd90a86f0db75f78f3b8ec90b219cdf11a35316cf1d`)); pip-audit runtime (`evidence/27-hardening/EVD-M-01-pip-audit-runtime.json` (sha256 `97b9424c9b9bdb1905993a93f0557a2705afc63f2c4421c46d1079d3e24d756d`)) and dev (`evidence/27-hardening/EVD-M-01-pip-audit-dev.json` (sha256 `70ef1b6fa497f5d480a0f3ea6e5841f0434f7d16c4d23be138e086f178b54abf`)); bandit (`evidence/27-hardening/EVD-M-01-bandit.json` (sha256 `8a6e8b7670108e14cfedbe5432c7dc3a7b9b94fa189a5ede434b50772e32baa6`)). No provenance attestation or signing.

## Observability and Traceability Evidence
- 3 dashboards and 15 alerts as code; 31 rules validated, 0 failed (`evidence/31-observability/EVD-N-01-observability-validation.json` (sha256 `b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485`)). Trace sample with correlation id (`evidence/15-modernization/EVD-H-08-trace-sample.json` (sha256 `5b79ef4cf9cc76f6b5d6e39dd9300d709b0e7633f933e1c21029adc4b07a1e88`)). One event reconstructed end to end with 10/10 field coverage and a tamper test (`evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`)). PARTIAL: no spans/traces; no collector has run; SLO owners unnamed.

## AI Security and Guardrails Evidence
- Allow-listed prompt fields, schema validation, evaluated guardrail, prompt and model locks, approval gate (`evidence/15-modernization/EVD-H-07-ai-gateway-results.json` (sha256 `38fe45eb845bc0d5c3aebbc45d155f9d0a2997ee758cf39c497312d245b1aec6`); `evidence/23-human-control/EVD-K-01-human-control-tests.txt` (sha256 `ebd91a777fa2223e03d14f0f9a949ecafa3b80e17a0da4cf179519ccde821828`)). 192 evaluation cases, 0 failures, thresholds committed before results (`evidence/26-tevv/EVD-L-02-final-eval-run.json` (sha256 `dfdf29d208c4cdc05911c3fe8c76ba6ccfe66ccbd6d9a0677aee10d40c8ee54e`); `evidence/19-intelligence/EVD-J-02-dataset-manifest.json` (sha256 `12f6d1e61249453395f330787076dddd9376797833fe8a27632fd34e3c444479`)).
- Red team 0 of 12 on the transformed build vs 10 of 12 on the baseline (`evidence/26-tevv/EVD-L-03-redteam-v2.json` (sha256 `b6f65533d6d71145d1d98da52ee5886590871091c704bc514e07984327d03356`)).
- NOT MET: **no real model was ever called** (`real_model_called: false`); second-model portability not tested (`evidence/40-scale/EVD-Q-01-preregistration.json` (sha256 `d050b98fe3a419f360f48be9edb646e952ccd3d08488cd5639d41556da875014`)).

## Performance and Scalability Evidence
- Loopback, one uvicorn process, deterministic provider: record lookup 189 req/s (p95 6.3 ms) with 1 worker and 244 req/s (p95 33.6 ms) with 8 (`evidence/28-resilience/EVD-M-02-load-probe.json` (sha256 `fe069284369b402e6ad264b65bcec643eafb054804d6877036f375ae34d212af`)). **Not a capacity test.** Model, network and platform latency UNMEASURED (TEVV-R-03).

## Reliability and Failure Engineering Evidence
- Five declared failure drills PASS (`evidence/28-resilience/EVD-M-03-drills/summary.json` (sha256 `eec9e4e654674cf439c8ed4a888514c0e2485679fdd7f61bc513294b343f00ac`)); AI-disabled mode demonstrated (`evidence/28-resilience/EVD-M-03-drills/drill-2-ai-gateway-timeout.json` (sha256 `50001fe1c3022b876dcd94b1e7c511b7d99c7297dfb1378ccb1017df3a331def`)). Saga: idempotency and retry ceiling 5 against a simulated carrier (`evidence/21-integration/EVD-J-05-saga-simulation.json` (sha256 `66c0a6ef457835fb26ed61804acde5eff5cc78e3e9272c0beeb9e183ef863fe7`)). Backup restore (`evidence/30-release/EVD-N-03-backup-restore.json` (sha256 `a2bf3c55a72cf2c96b00ad4b938ef0f78edeee97df911f918e8e95a2b6a4268e`)). Tabletop simulation, author-run (`evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json` (sha256 `4b0a559a37a34090a95c38774c364d70c4b012dc734a41a55a2171aaaba8cb10`)). PARTIAL: bulkhead unwired; no human tabletop; rollback never exercised in a deployment.

## AI FinOps Evidence
- Measured per request: 349 requests, tokens estimated at len/4 (mean 271), audit bytes per AI request 1,170 (`evidence/32-finops/EVD-N-04-finops-model.json` (sha256 `207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac`)). Benefit model: NPV -970 h expected, +5,525 h optimistic, -2,466 h downside over 36 months (`evidence/36-benefits/EVD-O-03-benefit-model.json` (sha256 `2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52`)). No real token usage or price; **verified monetary benefit nil**. After-intervention KPIs (`evidence/34-after-kpis/EVD-O-01-after-kpis.json` (sha256 `3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717`)): definitions unchanged, no operational improvement measurable.

## Automated Security Validation Evidence
- 25 security tests (`evidence/24-security-privacy/EVD-K-02b-security-suite-after-m1.txt` (sha256 `deebe2780f9a2931192922f3af183473ca9c1b1a2da63e1869a64b6ae1f43859`)); full suite and observability checks (`evidence/31-observability/EVD-N-01b-full-suite-after-p.txt` (sha256 `d05daff4a35eb0de4423bbce4f3887cd4c58c2116bfb10cfc36c642e4d19d842`)); secret scan, ruff, mypy (`evidence/15-modernization/EVD-R-01-final-verification.txt` (sha256 `510e7971405b8f1f097dc385fcbe5cb700a6ed54d5011e7108a64bc83b7db92f`)). Drift check clean and drifted (`evidence/39-continuous-improvement/EVD-P-03-drift-check-clean.json` (sha256 `68b946cf2f1147b84059905b7a80e23bdaeea3e6bc06eca8a3492b7a59d8258f`); `evidence/39-continuous-improvement/EVD-P-03-drift-check-drifted.json` (sha256 `702f90ca3f04232249f31c3dc207c67aee97f3e3afa0b9914b9f6df54adc29a4`)).

## Auditability and Compliance Evidence
- Hash-chained audit v2 with actor, correlation id, tenant, resource, policy decision, model and prompt version, approval id (`/audit/verify`); tamper test marks the chain untrusted (`evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`)). PARTIAL: local file sink; retention and subject rights undefined (RA-10); regulatory scope unresolved (RA-01); compliance review by no one.
- Every finding has a final disposition (`evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv` (sha256 `24dc4df12754670d842a7f1d8fb2d8dfa03eb8214dd35758a7e26577a6e774d1`)).

## Production Readiness Decision
`docs/42-executive/production-readiness-decision.md` (sha256 `10af5d5ed2dd0e61fe526c31a4ae67c2607544ba42591553c8f7ea45e7b29fa0`). NO-GO production on real data; CONDITIONAL GO controlled pilot on synthetic data; no risk accepted by any named person; G8-G12 failed.
