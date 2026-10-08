# Executive evidence index

| Field | Value |
|---|---|
| Stage | R |
| Runbook step | R3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | evidence/ |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Every material claim in the executive documents maps to one of these files. Full index with step and citing document: `evidence/EVIDENCE-INDEX.md`.

| # | Claim | Evidence (path, sha256) |
|---|---|---|
| 1 | Delivered quick-start fails (exit 2; wrong module path) | `evidence/07-repo-assessment/EVD-C-02-quickstart-transcript.txt` (sha256 `74e85bd8cec2ade87fc4ccf8a95b40552928010bfd689e761b21868fdf541581`) |
| 2 | Baseline: 3 tests, 45% coverage after adding httpx | `evidence/07-repo-assessment/EVD-C-03-junit.xml` (sha256 `1d96dc44eb81588a1155ba4566d8d87ab7ef22d62ba21b803f7835d3926ca8da`) |
| 3 | Behaviour pinned before change | `evidence/07-repo-assessment/EVD-C-08-characterization-junit.xml` (sha256 `b35040581e79ee0e1b912f8399b855e60ef591ad76c24faa27eb7c0169ffd90e`) |
| 4 | Fixture profile and KPI proxies | `evidence/04-baseline-kpis/EVD-C-05-data-profile.json` (sha256 `6314f00faa1df6c781714c3be2e946cae1b323858f1b435868989a8f4dced202`) |
| 5 | Correlation id: 983 null + 1,009 empty = 1,992 unusable | `evidence/00-preflight/EVD-A-04c-correlation-recount.txt` (sha256 `c2600111796cca839e726d805f30ac37f26904872fdff92ceaebd1663716707c`) |
| 6 | Declared flows mapped to code or NOT IMPLEMENTED | `evidence/05-current-state/EVD-C-04-flow-to-code-trace.md` (sha256 `4ddd2316209f21774efc175f323585b52c0363bda79b040be3515c3fbd7559f1`) |
| 7 | Semantic layer generated and tested | `evidence/11-data-context/EVD-D-05-semantic-layer-junit.xml` (sha256 `cb1fc7cbbef53af7b1e21ab6a657e65dcc0b84dcfe178ca91dad5ebb127dae45`) |
| 8 | OpenAPI covers every route | `evidence/12-specs/EVD-F-03-openapi.yaml` (sha256 `6016a47d34dccadb44c6f7237cd3077f44edce88f5029801d5d1249272215c87`) |
| 9 | Finding coverage plan (62) | `evidence/13-traceability/EVD-F-04-finding-coverage-matrix.csv` (sha256 `055a52f15d9daafa8d76bc642da760ea3a404790ac7d0fcefbb9f76ba1016821`) |
| 10 | Final disposition of 62 findings | `evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv` (sha256 `24dc4df12754670d842a7f1d8fb2d8dfa03eb8214dd35758a7e26577a6e774d1`) |
| 11 | Authorisation record (unsigned) | `evidence/14-transformation/EVD-G-04-authorisation-record.txt` (sha256 `88f1b4321b2f75114ce9c1a23866a289757ac3f81358180c55b323d15d2e4679`) |
| 12 | Quick-start works after transformation | `evidence/15-modernization/EVD-H-02-quickstart-after.txt` (sha256 `253337ce0f1b3e20361e42b612628b9447c629ce33633ea48bd88696d8310c70`) |
| 13 | No secrets in tree; 10 in history | `evidence/15-modernization/EVD-H-03-secret-scan-history.json` (sha256 `473b47bb982b7ab65985c869a7f35068253b7c3719d610e9ad90ed8f85849a4c`) |
| 14 | Negative access tests | `evidence/15-modernization/EVD-H-04-negative-access-tests.txt` (sha256 `c724516d79f2e15cce8017516c2a82a30c2eb663c4fe08b5cc83b181213eb2eb`) |
| 15 | Before/after behaviour probes | `evidence/16-repo-validation/EVD-H-10-behaviour-diff.csv` (sha256 `c78a8433c06d9266db854f14d8ee3393ff348a4dd42dc5cdd032114fc0c92b58`) |
| 16 | Evaluation 192 cases 0 failures | `evidence/26-tevv/EVD-L-02-final-eval-run.json` (sha256 `dfdf29d208c4cdc05911c3fe8c76ba6ccfe66ccbd6d9a0677aee10d40c8ee54e`) |
| 17 | Red team baseline 10/12 | `evidence/26-tevv/EVD-L-03-redteam-baseline.json` (sha256 `690911c90695c307f620ac56aec88e8d0da9732b4f6405dbf9c381e38df9213f`) |
| 18 | Red team v2 0/12 | `evidence/26-tevv/EVD-L-03-redteam-v2.json` (sha256 `b6f65533d6d71145d1d98da52ee5886590871091c704bc514e07984327d03356`) |
| 19 | Human control tests | `evidence/23-human-control/EVD-K-01-human-control-tests.txt` (sha256 `ebd91a777fa2223e03d14f0f9a949ecafa3b80e17a0da4cf179519ccde821828`) |
| 20 | SBOM runtime | `evidence/27-hardening/EVD-M-01-sbom-runtime.cdx.json` (sha256 `7b6b270a171dbb86fec07b9dd599d04792188e95a3b08805269d0f15e4c34395`) |
| 21 | Failure drills 5/5 | `evidence/28-resilience/EVD-M-03-drills/summary.json` (sha256 `eec9e4e654674cf439c8ed4a888514c0e2485679fdd7f61bc513294b343f00ac`) |
| 22 | Tabletop (author-run) | `evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json` (sha256 `4b0a559a37a34090a95c38774c364d70c4b012dc734a41a55a2171aaaba8cb10`) |
| 23 | Backup restore | `evidence/30-release/EVD-N-03-backup-restore.json` (sha256 `a2bf3c55a72cf2c96b00ad4b938ef0f78edeee97df911f918e8e95a2b6a4268e`) |
| 24 | Observability as code validated | `evidence/31-observability/EVD-N-01-observability-validation.json` (sha256 `b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485`) |
| 25 | Event reconstruction | `evidence/31-observability/EVD-N-02-reconstruction.json` (sha256 `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241`) |
| 26 | FinOps measurements | `evidence/32-finops/EVD-N-04-finops-model.json` (sha256 `207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac`) |
| 27 | After-intervention KPIs unchanged | `evidence/34-after-kpis/EVD-O-01-after-kpis.json` (sha256 `3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717`) |
| 28 | Benefit model, NPV | `evidence/36-benefits/EVD-O-03-benefit-model.json` (sha256 `2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52`) |
| 29 | Operator exercises (author-run) | `evidence/38-handover/EVD-P-02-operator-exercises.json` (sha256 `0482bd0cf4b1edf59e04ea08f2b7ab4a6ba2d2d45fc2e423b430b1e3be6780ab`) |
| 30 | Drift check | `evidence/39-continuous-improvement/EVD-P-03-drift-check-drifted.json` (sha256 `702f90ca3f04232249f31c3dc207c67aee97f3e3afa0b9914b9f6df54adc29a4`) |
| 31 | Portability test pre-registered, not run | `evidence/40-scale/EVD-Q-01-preregistration.json` (sha256 `d050b98fe3a419f360f48be9edb646e952ccd3d08488cd5639d41556da875014`) |
| 32 | Demo rehearsal (author-run, 28 s) | `evidence/42-executive/EVD-Q-03-demo-rehearsal.txt` (sha256 `4d74a7e8920cbe67c5729cea0654984e84e1980bb9cf95ac3ed6c0f00f2d0be2`) |
| 33 | CI run 1 failed; run 2 green | `evidence/15-modernization/EVD-R-02-ci-run-2-green.txt` (sha256 `ecc80c2198e52f243b4fad863caae96b5c55ec8c2d8c9f451f5306e8222a6b28`) |
| 34 | Final verification 3.11 and 3.13 | `evidence/15-modernization/EVD-R-01-final-verification.txt` (sha256 `510e7971405b8f1f097dc385fcbe5cb700a6ed54d5011e7108a64bc83b7db92f`) |

Claims with **no evidence** (stated as such in the documents): any real-model behaviour; any deployment property; any business benefit; independent review; model portability; encryption in transit/at rest.
