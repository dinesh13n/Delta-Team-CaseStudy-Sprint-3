# Finding to rubric map (62 findings)

| Field | Value |
|---|---|
| Stage | S: Evidence index and rubric traceability (runbook/03-EVIDENCE-RUBRIC-TRACEABILITY.md) |
| Runbook step | 03-2 (Doc 03 section 4) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PROVISIONAL |
| Evidence sources | docs/07-repo-assessment/technical-debt-register.md (rubric column); EVD-F-04b; EVD-S-02-finding-rubric-map.csv |
| Assumptions | Self-assessment by the same agent that built the evidence; no independent reviewer |
| Unresolved issues | None beyond the open questions |
| Residual risks | The rubric column is the author's own assignment from Stage C |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Document 03 section 4 gave counts for 57 findings (R1 19, R2 20, R3 31, R4 7). The register now has 62 findings (F-58..F-62 were found later). Counts below are from the register's own rubric column; a finding can serve more than one criterion. R5 has no findings: its evidence is the presentation of R1 to R4.

| Rubric | Findings | FIXED | FIXED-IN-TREE | PARTIAL | CHANGED | DEFERRED | ACCEPTED-PROPOSED |
|---|---|---|---|---|---|---|---|
| R1 | 24 | 19 | 0 | 3 | 1 | 0 | 1 |
| R2 | 22 | 17 | 0 | 4 | 0 | 1 | 0 |
| R3 | 31 | 20 | 4 | 6 | 0 | 1 | 0 |
| R4 | 6 | 2 | 0 | 2 | 2 | 0 | 0 |

**The observation in Document 03 still holds, more strongly.** 31 findings feed R3 (20 marks) and 6 feed R4 (25 marks). The defects are in governance; the marks are in execution. The repository ended with the governance findings mostly fixed (the R3 row above) but with R4's weak points being the two things that need outside input: a real model (B-1) and an end-to-end workflow a person has watched (B-7, B-10). [INF]

The numbers differ from Document 03 because it listed IDs per criterion by hand and the register assigns a criterion per finding; both are stated so neither is silently preferred. [VF]

## All 62
| Finding | Sev | Rubric | Final disposition | Title |
|---|---|---|---|---|
| F-01 | S1 | R1, R3 | FIXED | The repository is not under version control |
| F-02 | S2 | R1, R4 | FIXED | The documented test command cannot run |
| F-03 | S3 | R1 | FIXED | The documented run command is wrong |
| F-04 | S2 | R2 | FIXED | No dependency lockfile for either stack |
| F-05 | S2 | R1, R4 | CHANGED | Documentation claims a portal that does not exist |
| F-06 | S3 | R2 | PARTIAL | The frontend lint gate is "lint": "echo scaffold" — a no-op that reports success. |
| F-07 | S2 | R2 | PARTIAL | No containerisation or environment definition: no Dockerfile, no compose file, no devconta |
| F-08 | S2 | R3 | PARTIAL | No change-control surface: no CONTRIBUTING.md, no PR template, no CODEOWNERS, no branch-pr |
| F-09 | S1 | R3 | FIXED-IN-TREE | A database password is hardcoded in source |
| F-10 | S1 | R3 | FIXED-IN-TREE | .env.example ships a complete DSN with embedded credentials: postgresql://app_shared:Welco |
| F-11 | S2 | R3 | FIXED-IN-TREE | .env.example ships AI_GATEWAY_KEY=sk-workshop-hardcoded-example — a key-shaped literal in  |
| F-12 | S1 | R3 | FIXED-IN-TREE | .env.example ships OT_VENDOR_TOKEN=replace-me-but-currently-shared — the comment itself do |
| F-13 | S2 | R3 | FIXED | .env.example sets LOG_LEVEL=DEBUG as the default, meaning verbose logging of operational p |
| F-14 | S1 | R3 | FIXED | No secret detection anywhere: no scanner in CI, no pre-commit hooks, no rotation policy |
| F-15 | S2 | R3 | FIXED | The IaC emits a credential artifact |
| F-16 | S2 | R3 | DEFERRED | No encryption posture exists: no TLS configuration, no at-rest statement, no key managemen |
| F-17 | S1 | R3 | FIXED | Authorisation is a client-supplied HTTP header |
| F-18 | S1 | R3 | FIXED | The role check is a flat five-element allow-list with no resource, tenant, facility, purpo |
| F-19 | S1 | R1, R3 | FIXED | The allow-list contains a persona from another domain |
| F-20 | S1 | R3 | FIXED | The AI endpoint has no authorisation check whatsoever |
| F-21 | S1 | R3 | FIXED | policy/opa/access.rego is role-only (admin → all, operator → read) |
| F-22 | S1 | R3 | FIXED | Prompt injection surface |
| F-23 | S2 | R3 | FIXED | Using str.format() on attacker-influenceable content is additionally a format-string injec |
| F-24 | S1 | R3 | FIXED | The system self-reports that no guardrail exists: the response literal is "guardrail_statu |
| F-25 | S1 | R3 | FIXED | No output schema validation |
| F-26 | S1 | R3 | FIXED | No human approval gate |
| F-27 | S1 | R3 | FIXED | Model provenance is a module constant (MODEL_VERSION = "local-sim-v1") |
| F-28 | S2 | R2, R3 | PARTIAL | Token accounting is fabricated: token_estimate = len(prompt.split()) * 2 |
| F-29 | S1 | R1, R4 | PARTIAL | The AI output is not derived from the record's meaning |
| F-30 | S1 | R1, R2 | FIXED | Cross-entity primary-key collision |
| F-31 | S1 | R2 | FIXED | Record lookup scans every column, not the key |
| F-32 | S1 | R1, R2 | FIXED | A missed lookup silently returns the wrong record |
| F-33 | S2 | R1 | FIXED | Three duplicate business keys in every dataset, at a consistent *-00004, *-00013, *-00019  |
| F-34 | S2 | R1 | FIXED | One fully-blank mandatory row in every dataset — every non-key column empty (10 blank colu |
| F-35 | S2 | R1 | FIXED | One impossible timestamp per timestamped dataset: 1900-01-01T00:00:00 in shipments.promise |
| F-36 | S2 | R1, R2 | FIXED | tracking_events.confidence spans 0.001–1.42 |
| F-37 | S1 | R1, R2 | FIXED | No semantic layer: categorical columns are polluted with workflow-status vocabulary |
| F-38 | S2 | R1, R2 | FIXED | Referential integrity is unenforced |
| F-39 | S1 | R2 | FIXED | A retry storm is already visible in the data |
| F-40 | S2 | R2 | FIXED | ETL counts defects and discards them |
| F-41 | S2 | R2 | FIXED | The ETL has no run identifier, watermark or idempotency key |
| F-42 | S1 | R1, R3 | PARTIAL | About one third of the event stream cannot be correlated |
| F-43 | S1 | R3 | FIXED | The audit event records only ts, action and details |
| F-44 | S1 | R3 | PARTIAL | The audit sink is a local file written by the application itself — <repo>/logs/audit.log,  |
| F-45 | S2 | R3 | FIXED | datetime.utcnow() yields a naive timestamp with no timezone marker |
| F-46 | S1 | R3 | PARTIAL | No tracing, no metrics, no SLOs, no dashboards-as-code, no alerting, no error budget |
| F-47 | S2 | R2, R3 | PARTIAL | CI executes commands but produces no evidence |
| F-48 | S2 | R2 | DEFERRED | The Terraform is a local_file resource with no provider, no backend, no state management a |
| F-49 | S2 | R2, R3 | FIXED | supply-chain/dependency-risk-register.md correctly names "no SBOM" and "no provenance" as  |
| F-50 | S2 | R2, R4 | FIXED | The API contract omits both business endpoints |
| F-51 | S2 | R1 | FIXED | The characterization test characterises nothing |
| F-52 | S2 | R4 | CHANGED | tests/playwright/operations.spec.ts asserts that body is visible against an application th |
| F-53 | S2 | R1, R2 | FIXED | A known architectural divergence is documented and unmanaged |
| F-54 | S2 | R1, R2 | FIXED | Data remediation will break the repository's own contract test |
| F-55 | S3 | R2 | FIXED | scripts/sanity_check.py hard-requires the paths docs/transformation-roadmap.md, docs/domai |
| F-56 | S2 | R3 | FIXED | The incident runbook declares itself *"intentionally incomplete"* |
| F-57 | S2 | R1, R4 | PARTIAL | No business KPI data exists |
| F-58 | S3 | R1 | FIXED | ai_invocations.csv also has an orphan shipment reference (REC-0001 row); not in the origin |
| F-59 | S3 | R1 | ACCEPTED-PROPOSED | 171 of 351 shipments have actual weight above declared weight (meaning unknown) |
| F-60 | S2 | R1, R3 | FIXED | data/README.md claims untrusted text payloads for prompt-injection testing; no free-text f |
| F-61 | S3 | R1, R2 | FIXED | routes.weather_risk holds numeric 1.42 in a categorical field |
| F-62 | S3 | R1, R2 | FIXED | Every dataset has one malformed key *-BAD1 |
