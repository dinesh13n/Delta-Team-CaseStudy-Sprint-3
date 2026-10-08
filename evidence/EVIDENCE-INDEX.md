# Evidence index (hash-verified)

| Field | Value |
|---|---|
| Stage | R |
| Runbook step | R2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | evidence/*/MANIFEST.md |
| Assumptions | See assumptions in body |
| Unresolved issues | See open questions |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

134 evidence files in 32 stage folders (113 verified in R2 and recorded in `EVD-R-03-manifest-verification.json`; 21 added by the Stage Q portability run, EVD-Q-04 to -07; re-running `EVD-R-03-verify-manifests.py` gave `EVD-Q-07-manifest-reverification.json`: 133 of 133 manifest rows matched at that time, 0 duplicates, 0 missing; this index is the only file not in a manifest). Files registered late (stages H-P) carry a note in their manifest row: their hash proves the file is unchanged since 2026-10-08 (R2), not since it was produced.

| File | SHA-256 | Step | Cited by |
|---|---|---|---|
| 00-preflight/EVD-A-01-baseline-file-manifest.sha256 | `8eb89d1ff2dd835d78f823662e6dca0713b94034f71263504653d0cabba3fac2` | A1 | docs/00-preflight/operating-contract/decision-log.md |
| 00-preflight/EVD-A-01-delivered-vs-committed.csv | `dd2382a160a0c7586ca6ed393b90ec26b4113f6bb28e106fa2c1bcdeeb6ca30c` | A1 | docs/00-preflight/operating-contract/decision-log.md |
| 00-preflight/EVD-A-01-tag-verification.txt | `a507d3d45cee3dd0598ca179c229ae213ef15c999ada6eb1353c4eea4be4b70b` | A1 | docs/00-preflight/operating-contract/decision-log.md |
| 00-preflight/EVD-A-02-spine-tree.txt | `38db5b75d91b98521a40d52a5b623280bb9d038890ab23574a0ece327e2b0406` | A2 | docs/00-preflight/operating-contract/decision-log.md |
| 00-preflight/EVD-A-03-toolchain-snapshot.txt | `b9bc4bf6585621edcdd934895f923a0e2d4a643e0c5fed30c418715993b3231f` | A3 | docs/00-preflight/discovery/environment-snapshot.md |
| 00-preflight/EVD-A-03c-runtime-upgrade-compat.txt | `4c48b3c48ba51da41bc0c7ef2a42b75002ab8738bffa9cedda85b2271aa6901a` | A3 | docs/00-preflight/discovery/environment-snapshot.md |
| 00-preflight/EVD-A-03b-windows-host-snapshot.txt | `7e61ec7eb27d9126ac1ab9fa137a8eb0c009e5609ab3c56b8ab9d1340a82f345` | A3 | docs/00-preflight/discovery/environment-snapshot.md |
| 00-preflight/EVD-A-03d-windows-host-snapshot-2.txt | `7569293ca130291d004dbb8cbfef68dd2dcb83cfcdad29c85b1197ad5ca135f6` | A3 | docs/00-preflight/discovery/environment-snapshot.md |
| 00-preflight/EVD-A-03e-operator-statement.txt | `328cdba5fb736a07f1af70c99fd01588b56e8b0ca4d5d8500c859f5c90ae0d18` | A3 | docs/00-preflight/discovery/environment-snapshot.md |
| 00-preflight/EVD-A-04-repo-tree-annotated.txt | `6dd1c997087a9a453650d2228a2a9a01aa075d9ba810905e3e0f83705c457347` | A4 | docs/00-preflight/discovery/ |
| 00-preflight/EVD-A-04b-data-profile.txt | `b81c7055f0bad40deeb41ff0b76a0cb6b037420a5a4a575e5152d7c12e14d37e` | A4 | docs/00-preflight/discovery/ |
| 00-preflight/EVD-A-05-confirmation-items.txt | `8c5b0b96519512cf2c80b94b9b92f167671669fcb6629cb32f8fe3ac6f6ec16c` | A5 | docs/00-preflight/operating-contract/operating-contract-readiness.md |
| 00-preflight/EVD-A-06-ai-economics-profile.json | `d38d6c61ea774cf11348a9a7c5a497c5eb77c04e78dfed773252fe9ca8d664d5` | A6 | docs/00-preflight/ai-economics/ |
| 00-preflight/EVD-A-07-stage-a-exit-checks.txt | `f71de9f9325e9e14cd2def90df779de5e577db84683bf803e9720bf246fbf194` | A7 | docs/00-preflight/stage-a-gate.md |
| 00-preflight/EVD-A-04c-correlation-recount.txt | `c2600111796cca839e726d805f30ac37f26904872fdff92ceaebd1663716707c` | A4 (re-opened by D-012) | decision-log D-012 |
| 01-engagement/EVD-B-01-stage-b-checks.txt | `05f19134a27092776e4755f4e359dcb27afa0c23ab67821f2c9cf5ab6a638ee3` | B4 | docs/03-problem-value/stage-b-gate.md |
| 04-baseline-kpis/EVD-C-05-data-profile.json | `6314f00faa1df6c781714c3be2e946cae1b323858f1b435868989a8f4dced202` | C1/C5 | docs/04-baseline-kpis/ |
| 04-baseline-kpis/EVD-C-05-profile.py | `7c6f7f2b4fd3b69f6dc6b980a65d2f530219d69e9e53a2657e9d70ff34f0247a` | C1/C5 | docs/04-baseline-kpis/ |
| 05-current-state/EVD-C-04-flow-to-code-trace.md | `4ddd2316209f21774efc175f323585b52c0363bda79b040be3515c3fbd7559f1` | C4 | docs/05-current-state/business-workflow-map.md |
| 07-repo-assessment/EVD-C-02-quickstart-transcript.txt | `74e85bd8cec2ade87fc4ccf8a95b40552928010bfd689e761b21868fdf541581` | C2/C3 | docs/07-repo-assessment/baseline-behaviour.md |
| 07-repo-assessment/EVD-C-03-transcript.txt | `e00e2c43b291f1a06e7144f029873e2b4422672353800328fc2534d30060b743` | C2/C3 | docs/07-repo-assessment/baseline-behaviour.md |
| 07-repo-assessment/EVD-C-03-junit.xml | `1d96dc44eb81588a1155ba4566d8d87ab7ef22d62ba21b803f7835d3926ca8da` | C2/C3 | docs/07-repo-assessment/baseline-behaviour.md |
| 07-repo-assessment/EVD-C-03-coverage.xml | `85210479df1b835c07459cca3a26494695ede817d7399bc85133811e92b607e8` | C2/C3 | docs/07-repo-assessment/baseline-behaviour.md |
| 07-repo-assessment/EVD-C-07-findings-index.json | `6c387bfd6ea34ba4aca6464d7bcea97e164f439d89acc063516ecec85e016a98` | C7 | docs/07-repo-assessment/technical-debt-register.md |
| 07-repo-assessment/EVD-C-08-characterization-junit.xml | `b35040581e79ee0e1b912f8399b855e60ef591ad76c24faa27eb7c0169ffd90e` | C8 | docs/07-repo-assessment/stage-c-gate.md |
| 07-repo-assessment/EVD-C-09-stage-c-exit-checks.txt | `61b3292ae9002e9da7fbdc5d30c3074b8c983a2ac01c20c0fd1fdfadd44b9828` | C9 | docs/07-repo-assessment/stage-c-gate.md |
| 08-ai-qualification/EVD-E-04-stage-e-checks.txt | `56b7058b10ff961bc3091af9007b241a45b7f3ccc649790a6345f1f640e069c6` | E4 | docs/09-initial-prd/stage-e-gate.md |
| 09-initial-prd/EVD-E-03-requirement-trace.csv | `079f95fb2f36f6dc60697bafebf6720ebb4696699722d19f7335786cb4a00453` | E3 | docs/09-initial-prd/initial-prd-traceability.md |
| 10-architecture/EVD-F-01-adr-index.txt | `4cae717c359d65180ef203aeda719971c6f37e405a160e033495cc8bcf5d450d` | F1 | stage-f-gate.md (F-X1) |
| 11-data-context/EVD-D-01-field-coverage.csv | `298054a6d5c07cc41202e4816df2e3f90438d03b9e8044747e3c06828fce293c` | D1-D5 | docs/11-data-context/stage-d-gate.md |
| 11-data-context/EVD-D-02-enum-violations.csv | `358e7392b8fad0b672ac5a4ee4b0e352b863e544f23a1ba9a637aac1c51f2ea7` | D1-D5 | docs/11-data-context/stage-d-gate.md |
| 11-data-context/EVD-D-03-rule-to-gap-trace.csv | `5388fb6ad5f0454598a0488454a4012d3de54936d2defb84bbce6134f3c5a582` | D1-D5 | docs/11-data-context/stage-d-gate.md |
| 11-data-context/EVD-D-04-access-semantics-matrix.csv | `f95609856b8284299d323c48befa7e688f60c55d31c5ef508581d05121b005c8` | D1-D5 | docs/11-data-context/stage-d-gate.md |
| 11-data-context/EVD-D-05-rule-baseline.json | `d44af9df668fa79e00af0ee2da9c0cdad84ff6e6bf9ac1c8b225d9d085132d55` | D1-D5 | docs/11-data-context/stage-d-gate.md |
| 11-data-context/EVD-D-05-semantic-layer-junit.xml | `cb1fc7cbbef53af7b1e21ab6a657e65dcc0b84dcfe178ca91dad5ebb127dae45` | D1-D5 | docs/11-data-context/stage-d-gate.md |
| 11-data-context/EVD-D-05-generated-semantic-layer.json | `edf62772dc55687db93dd20f3e520331db0e5f247d936c0ced401cee79083bf2` | D1-D5 | docs/11-data-context/stage-d-gate.md |
| 12-specs/EVD-F-03-openapi.yaml | `6016a47d34dccadb44c6f7237cd3077f44edce88f5029801d5d1249272215c87` | F3 | docs/12-specs/spec-readiness.md; stage-f-gate.md |
| 12-specs/EVD-F-03-openapi-validation.txt | `0633960f82600f6fbf80d68cd7b6e60e9f2d87242ec53df855af06b55a35cd1a` | F3 | docs/12-specs/spec-readiness.md; stage-f-gate.md |
| 12-specs/EVD-F-03-schema-checks.txt | `8690d9106e92bc96d0d4c207a2bc2f377185076fab46e868a6e37d0ad708b26d` | F3 | docs/12-specs/spec-readiness.md; stage-f-gate.md |
| 12-specs/EVD-F-03-route-coverage-diff.txt | `9dbd1b3c0b3b193b3bb934a5ed36415c2b524817950f82f7f385bb18822a41f3` | F3 | docs/12-specs/spec-readiness.md; stage-f-gate.md |
| 13-traceability/EVD-F-04-finding-coverage-matrix.csv | `055a52f15d9daafa8d76bc642da760ea3a404790ac7d0fcefbb9f76ba1016821` | F4 | stage-f-gate.md (F-X8) |
| 13-traceability/EVD-F-05-stage-f-exit-checks.txt | `1df22f4e7472cff0bdb6e7bf8948a79ac0ffb468ca210b1d70278c32fa003f4e` | F5 | stage-f-gate.md |
| 13-traceability/EVD-F-04b-finding-disposition-final.csv | `24dc4df12754670d842a7f1d8fb2d8dfa03eb8214dd35758a7e26577a6e774d1` | R5 | final-gate.md; requirement-disposition-matrix.md |
| 14-transformation/EVD-G-01-backlog-finding-coverage.txt | `f64b2b4c088a555f2f8092bff98371c1073f4215504b19a776bae50aeadcbc95` | G1/G4 | stage-g-gate.md |
| 14-transformation/EVD-G-04-authorisation-record.txt | `88f1b4321b2f75114ce9c1a23866a289757ac3f81358180c55b323d15d2e4679` | G1/G4 | stage-g-gate.md |
| 14-transformation/EVD-G-05-stage-g-exit-checks.txt | `2821273226c7a28d49e897479703bdf974cf8c160f04beb8dc6055d8c55397ad` | G5 | stage-g-gate.md |
| 15-modernization/EVD-H-01-pipeline-run.txt | `943f500b2da991e6bfcf1bba9740cfe8839bde806197ba9ac03d98cad007bd2b` | H1 | docs of step H1 |
| 15-modernization/EVD-H-02-quickstart-after.txt | `253337ce0f1b3e20361e42b612628b9447c629ce33633ea48bd88696d8310c70` | H2 | docs of step H2 |
| 15-modernization/EVD-H-03-secret-scan-history.json | `473b47bb982b7ab65985c869a7f35068253b7c3719d610e9ad90ed8f85849a4c` | H3 | docs of step H3 |
| 15-modernization/EVD-H-03-secret-scan.json | `9be399823ccf9be244917852a3f19b4ee67b5e5d2c813fae5b7f4c4fd20c4dab` | H3 | docs of step H3 |
| 15-modernization/EVD-H-04-negative-access-tests.txt | `c724516d79f2e15cce8017516c2a82a30c2eb663c4fe08b5cc83b181213eb2eb` | H4 | docs of step H4 |
| 15-modernization/EVD-H-04-policy-allow-deny-matrix.csv | `f838baffa93da9043a972b23f70f36a84f9442848d2805d4a2d029f4a96ad25a` | H4 | docs of step H4 |
| 15-modernization/EVD-H-05-behaviour-change.md | `cd41c7f450672e8dcb52cf26938be81a1df6c6df40a6527761e07202370b2f23` | H5 | docs of step H5 |
| 15-modernization/EVD-H-06-etl-dq-report.json | `1f091a63cc2100d80f936f5d6649fd30561f2f009820ef1e63c79f81f9520ed7` | H6 | docs of step H6 |
| 15-modernization/EVD-H-07-ai-gateway-results.json | `38fe45eb845bc0d5c3aebbc45d155f9d0a2997ee758cf39c497312d245b1aec6` | H7 | docs of step H7 |
| 15-modernization/EVD-H-08-trace-sample.json | `5b79ef4cf9cc76f6b5d6e39dd9300d709b0e7633f933e1c21029adc4b07a1e88` | H8 | docs of step H8 |
| 15-modernization/EVD-R-02-ci-run-1-failed.txt | `23711892040269c52df2765ce8ae5dfa695369196cf274543ce27f000826a70c` | R2 | residual-risks.md; lessons-learned.md |
| 15-modernization/EVD-R-01-final-verification.txt | `510e7971405b8f1f097dc385fcbe5cb700a6ed54d5011e7108a64bc83b7db92f` | R2 | production-readiness-decision.md |
| 15-modernization/EVD-R-02-ci-run-2-green.txt | `ecc80c2198e52f243b4fad863caae96b5c55ec8c2d8c9f451f5306e8222a6b28` | R2 | production-readiness-decision.md |
| 16-repo-validation/EVD-H-09-smoke.txt | `e3d44aec2bed164620555f0b9ae4deafa1d4a35c62eecdf6e14cb4417681b80f` | H9 | docs of step H9 |
| 16-repo-validation/EVD-H-10-behaviour-diff.csv | `c78a8433c06d9266db854f14d8ee3393ff348a4dd42dc5cdd032114fc0c92b58` | H10 | docs of step H10 |
| 16-repo-validation/EVD-H-11-architecture-imports.txt | `cf22df29cba03e3f711d476afbc4a1e74862bdb09cdfb53982ac28f9dcc7634e` | H11 | docs of step H11 |
| 16-repo-validation/EVD-H-11-dependency-audit.json | `97b9424c9b9bdb1905993a93f0557a2705afc63f2c4421c46d1079d3e24d756d` | H11 | docs of step H11 |
| 16-repo-validation/EVD-H-11-pytest-coverage.txt | `4c4904decbe976b76f17e0b2520d1911bee730985864868e999a12a875dafc46` | H11 | docs of step H11 |
| 16-repo-validation/EVD-H-11-static-analysis.txt | `a133801206f5d18f1b8a2a73b357919ecee21be91088555fcfe65cc6f14ee960` | H11 | docs of step H11 |
| 16-repo-validation/EVD-H-11-tg5-tg6.txt | `9d4ebee480f60ba0c0a21d28ec290582e585d54b6b7b71e630d88151374fa030` | H11 | docs of step H11 |
| 19-intelligence/EVD-J-02-dataset-manifest.json | `12f6d1e61249453395f330787076dddd9376797833fe8a27632fd34e3c444479` | J2 | docs of step J2 |
| 19-intelligence/EVD-J-03-eval-run1.json | `831889be4bda61a9bdd8ed338a22318145df97be03376e7d7587985c4126e937` | J3 | docs of step J3 |
| 19-intelligence/EVD-J-03-eval-run2-after-remediation.json | `3f729728c7e621fc037ceb2cbe9c829882f019fa74ba8119302bc8bc46bd5f3d` | J3 | docs of step J3 |
| 20-application/EVD-J-04-browser-e2e-script.py.txt | `532ea7c45747e07453e50bb5fe116d96c223507d924c4444fa0656e51854f8f3` | J4 | docs of step J4 |
| 20-application/EVD-J-04-browser-e2e.json | `79064bd7b6b0df59ac517e1d2bed3e32087836a44e8bdecb781b8b2fbb3c49bd` | J4 | docs of step J4 |
| 20-application/EVD-J-04-screenshot-decision.png | `e8176a1a476d499d1c1f6bba62a09d0ad0d468db368e65aef74a6fb8eee19cbb` | J4 | docs of step J4 |
| 20-application/EVD-J-04-screenshot-suggestion.png | `4b8ef6b6919d7688e98f0104a1f978a3e86c503fdacad4f5c2d41e227c3956b2` | J4 | docs of step J4 |
| 21-integration/EVD-J-05-saga-simulation.json | `66c0a6ef457835fb26ed61804acde5eff5cc78e3e9272c0beeb9e183ef863fe7` | J5 | docs of step J5 |
| 21-integration/EVD-J-05-saga-tests.txt | `cd8eadbda2dd4ee54ccf1325e3fdd59fc09ec71d6c1b15a27534027975beab06` | J5 | docs of step J5 |
| 23-human-control/EVD-K-01-human-control-tests.txt | `ebd91a777fa2223e03d14f0f9a949ecafa3b80e17a0da4cf179519ccde821828` | K1 | docs of step K1 |
| 24-security-privacy/EVD-K-02-security-suite.txt | `9e84ddad8bd61c9cdf38f4948b387358b44c5f5e0ff8ee88b85f23c6aa1fd537` | K2 | docs of step K2 |
| 24-security-privacy/EVD-K-02b-security-suite-after-m1.txt | `deebe2780f9a2931192922f3af183473ca9c1b1a2da63e1869a64b6ae1f43859` | K2 | docs of step K2 |
| 26-tevv/EVD-L-02-final-eval-run.json | `dfdf29d208c4cdc05911c3fe8c76ba6ccfe66ccbd6d9a0677aee10d40c8ee54e` | L2 | docs of step L2 |
| 26-tevv/EVD-L-03-redteam-baseline.json | `690911c90695c307f620ac56aec88e8d0da9732b4f6405dbf9c381e38df9213f` | L3 | docs of step L3 |
| 26-tevv/EVD-L-03-redteam-v2.json | `b6f65533d6d71145d1d98da52ee5886590871091c704bc514e07984327d03356` | L3 | docs of step L3 |
| 27-hardening/EVD-M-01-bandit.json | `8a6e8b7670108e14cfedbe5432c7dc3a7b9b94fa189a5ede434b50772e32baa6` | M1 | docs of step M1 |
| 27-hardening/EVD-M-01-pip-audit-dev.json | `70ef1b6fa497f5d480a0f3ea6e5841f0434f7d16c4d23be138e086f178b54abf` | M1 | docs of step M1 |
| 27-hardening/EVD-M-01-pip-audit-runtime.json | `97b9424c9b9bdb1905993a93f0557a2705afc63f2c4421c46d1079d3e24d756d` | M1 | docs of step M1 |
| 27-hardening/EVD-M-01-sbom-dev.cdx.json | `34d4a0df90df63d0c2ae3cd90a86f0db75f78f3b8ec90b219cdf11a35316cf1d` | M1 | docs of step M1 |
| 27-hardening/EVD-M-01-sbom-runtime.cdx.json | `7b6b270a171dbb86fec07b9dd599d04792188e95a3b08805269d0f15e4c34395` | M1 | docs of step M1 |
| 28-resilience/EVD-M-02-load-probe.json | `fe069284369b402e6ad264b65bcec643eafb054804d6877036f375ae34d212af` | M2 | docs of step M2 |
| 28-resilience/EVD-M-02-resilience-tests.txt | `c6191583172113272d2031f3ed399ca7461a0dfc6ed23de62e9c8d1e17ce2c3e` | M2 | docs of step M2 |
| 28-resilience/EVD-M-03-drills/drill-1-correlation-ids.json | `2678bb9b1575124a32cc31db1c307f5b7be08ff6036af728a55099bcd06c7bc2` | ? | docs of step ? |
| 28-resilience/EVD-M-03-drills/drill-2-ai-gateway-timeout.json | `50001fe1c3022b876dcd94b1e7c511b7d99c7297dfb1378ccb1017df3a331def` | ? | docs of step ? |
| 28-resilience/EVD-M-03-drills/drill-3-duplicate-replay.json | `2e780ff9b4b749a1918f0754dd988271dd3de16de8a3a765f9f03513f388ba6b` | ? | docs of step ? |
| 28-resilience/EVD-M-03-drills/drill-4-stale-master-data.json | `8f8f3e35a1bc319fd0c88b56313934cb59126d16f944f3a0899c884bc09bf9be` | ? | docs of step ? |
| 28-resilience/EVD-M-03-drills/drill-5-legacy-partial-failure.json | `9d7180652d755931ed94dfd855a33587ac1d8d1dc5012715d3769f0de39c0355` | ? | docs of step ? |
| 28-resilience/EVD-M-03-drills/summary.json | `eec9e4e654674cf439c8ed4a888514c0e2485679fdd7f61bc513294b343f00ac` | ? | docs of step ? |
| 28-resilience/EVD-M-03-resilience-tests-after-drills.txt | `9c509bda36ef6a69faa52ede33666646c59e27907c5e1c8e1027767115c4b8a8` | M3 | docs of step M3 |
| 29-incident-bcdr/EVD-M-04-tabletop-simulation.json | `4b0a559a37a34090a95c38774c364d70c4b012dc734a41a55a2171aaaba8cb10` | M4 | docs of step M4 |
| 30-release/EVD-N-03-backup-restore.json | `a2bf3c55a72cf2c96b00ad4b938ef0f78edeee97df911f918e8e95a2b6a4268e` | N3 | docs of step N3 |
| 31-observability/EVD-N-01-full-suite.txt | `dcd4e5b0fa68b3dfb016e6b78802228458437b48d4f3d1de44da866debd0c916` | N1 | docs of step N1 |
| 31-observability/EVD-N-01-observability-validation.json | `b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485` | N1 | docs of step N1 |
| 31-observability/EVD-N-01b-full-suite-after-p.txt | `d05daff4a35eb0de4423bbce4f3887cd4c58c2116bfb10cfc36c642e4d19d842` | N1 | docs of step N1 |
| 31-observability/EVD-N-02-reconstruction.json | `1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241` | N2 | docs of step N2 |
| 32-finops/EVD-N-04-finops-model.json | `207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac` | N4 | docs of step N4 |
| 34-after-kpis/EVD-O-01-after-kpis.json | `3708e637ef8963bda70458efcea4a75f6521f9972ce5610e4ffc73a7b2dea717` | O1 | docs of step O1 |
| 36-benefits/EVD-O-03-benefit-model.json | `2afe6092b217cb967a19100ba71c32fb09eadc66e7fdd0bfe0112e7cbffc7e52` | O3 | docs of step O3 |
| 38-handover/EVD-P-02-operator-exercises.json | `0482bd0cf4b1edf59e04ea08f2b7ab4a6ba2d2d45fc2e423b430b1e3be6780ab` | P2 | docs of step P2 |
| 39-continuous-improvement/EVD-P-03-drift-check-clean.json | `68b946cf2f1147b84059905b7a80e23bdaeea3e6bc06eca8a3492b7a59d8258f` | P3 | docs of step P3 |
| 39-continuous-improvement/EVD-P-03-drift-check-drifted.json | `702f90ca3f04232249f31c3dc207c67aee97f3e3afa0b9914b9f6df54adc29a4` | P3 | docs of step P3 |
| 40-scale/EVD-Q-01-preregistration.json | `d050b98fe3a419f360f48be9edb646e952ccd3d08488cd5639d41556da875014` | Q1 | semantic-layer-portability-test.md |
| 40-scale/EVD-Q-02-comparison.csv | `25b4aaddc9c676a3d13545292d79e791d6b3296d750047d7eae28ed004b32656` | Q2 | model-comparison.md |
| 40-scale/EVD-Q-04-harness-accept.py | `65f2ebc3273aeb575ca6b1d1551fcf12293d567872c79d48e6e4d5347341c433` | Q1 | semantic-layer-portability-test.md |
| 40-scale/EVD-Q-04-adapter-a.py | `ec136b28fef0c35ad0f1279b7fba6db491ecfa33d27e0a7770fab7af8d7098da` | Q1 | semantic-layer-portability-test.md |
| 40-scale/EVD-Q-04-build-brief.md | `9756dedad564cf4092e4f784cd961cfcb610f4f1c61f73c37f0b0393dd3afb6c` | Q1 | semantic-layer-portability-test.md |
| 40-scale/EVD-Q-04-bundle-sha256.txt | `57868ce78c130e64db6e1cca9dc0e1d425a51c060df3eca101991ddaca1b9cc2` | Q1 | semantic-layer-portability-test.md |
| 40-scale/EVD-Q-04-control-A-eval.json | `ca535583e1339ad66c87fc97de620f2616eb82276dea42417d98b9925e98fb79` | Q1 | semantic-layer-portability-test.md |
| 40-scale/EVD-Q-04-control-A-http.json | `82350bea067346789f169cb4e3669209320f17a6ac8f12fa062c8901e058217b` | Q1 | semantic-layer-portability-test.md |
| 40-scale/EVD-Q-04-harness-preregistration.json | `8b622a5c88105d75963a352b0007f06a023a32970947beb42d32f395047c2e9b` | Q1 | semantic-layer-portability-test.md |
| 40-scale/EVD-Q-05-model-b-transcript.jsonl | `7fb1472046dfee8e3edb03cd87e5574d592b085a9ef7e65c69d4885f2c17412d` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-model-b-meta.json | `a3f23119b8f49abb20c467029423b67a2b0d071f82b935a351304e2986295afa` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-model-b-build.tar.gz | `14d503b12422353fb7c1a0f1bff5166c02c6cfca3570023e89bf3e9bd61f2801` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-model-b-notes.md | `86af3789f56bc6fe86c83e69501187c89fe7bf97fcd2040004e247f251939e7f` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-model-b-eval.json | `d1c521804b2171cc9f7c091da0e71a90fa93c7c02fa9ea3aa1afbb92de46984e` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-model-b-http.json | `8d57a3f6a79ebed41c9ffa07a01882326f4a4dbe1973440463f7c971900eb6d3` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-model-b-http-supp-ai_agent.json | `89b7630c1722771b4621d39212412b42718c3d5e4226b98207378a21216eb93f` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-harness-accept-supp.py | `e6344f3f760bb854600cd8d53a8f996ab7f4541dd45bd349938c8dc8890ff0a2` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-posthoc-recommendation-class.txt | `f23bff6e2a539d6609202c0b259581e08a3c5fbc82503554e3b75ffe9804faa3` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-posthoc-recommendation-class.py | `5c7b388638b6d8216d983ef0de2f87ad8e6d674513b224de70f661e4e76f449b` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-model-b-prompt.md | `7fa9ab4ea1864e497629ab86ceb56d18a5125b245d5b71ef3b0fcd6fe98c3f6b` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-05-blindness-check.txt | `d46562a75311829ba853d7d34130692d7684676fc33613179fb7c47465ec30c7` | Q1-Q2 | semantic-layer-portability-test.md; model-comparison.md |
| 40-scale/EVD-Q-06-comparison.csv | `5a4971acea3e7d7ceb035d17f2c959d34b61202864fba88ef997b41aaa985b3e` | Q2 | model-comparison.md |
| 40-scale/EVD-Q-07-manifest-reverification.json | `16fa19c6acfce1e404efcc596f3ca6271f01fdc064369e0ff3e2176b073bf557` | Q4 | stage-q-gate.md; EVIDENCE-INDEX.md |
| 42-executive/EVD-Q-03-demo-rehearsal.txt | `4d74a7e8920cbe67c5729cea0654984e84e1980bb9cf95ac3ed6c0f00f2d0be2` | Q3 | demo-day-script.md |
| 42-executive/EVD-Q-03-rehearsal-script.sh | `0b5366ba424272f5f658e48bd9bf195e0a523b5989067c1d24c2278c9606866b` | Q3 | demo-day-script.md |
| 42-executive/EVD-R-03-manifest-verification.json | `067f226daad1e9de98d1631b12e6699c79e901256545e34efeb138aa2d8c4b1c` | R2 | final-gate.md |
| 42-executive/EVD-R-03-verify-manifests.py | `83aa911e01ab3607b99199cd97b7b602cdfa265c279e4e9572c2cbd981c3081c` | R2 | final-gate.md |
