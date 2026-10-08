# Transformation backlog and do-not-change register

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-F-04; Document 01 section 7; docs/13-traceability |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Item | Finding IDs | Spec / AC | Step | Sequence class |
|---|---|---|---|---|---|
| TB-01 | Repository governance files, CODEOWNERS, PR template, CONTRIBUTING, SECURITY, LICENSE | F-08 | nfr-spec | H1 | 1 |
| TB-02 | Quality gates: ruff, mypy, pytest-cov, pre-commit, CI evidence artefacts | F-06 (py), F-14, F-47, F-55 | nfr-spec | H1 | 1 |
| TB-03 | Reproducible install: httpx declared, hashed lock, README run command | F-02, F-03, F-04 | feat-06 AC-25 | H2 | 1 |
| TB-04 | Remove hardcoded secrets, sanitise .env.example and IaC output, secret scanning | F-09, F-10, F-11, F-12, F-13, F-14, F-15 | security-spec AC-24 | H3 | 2 |
| TB-05 | Replace header role with verified token; persona policy engine from access-semantics; Rego parity | F-17, F-18, F-19, F-20, F-21 | feat-02 AC-04..07 | H4 | 2 |
| TB-06 | Exact-key lookup, 404, id pattern validation | F-30, F-31, F-32 | feat-01 AC-01..03 | H5 | 3 |
| TB-07 | ETL validation, quarantine, curated layer, run id, report, exit code | F-33..F-41, F-54, F-58, F-59, F-61, F-62 | feat-03 AC-08..11 | H6 | 3 |
| TB-08 | AI gateway: allow-listed context, safe prompt, schema output, abstention, fallback, approval record, honest token accounting | F-22..F-29 | feat-04 AC-12..17 | H7 | 4 |
| TB-09 | Audit v2 with correlation id, UTC timestamps, hash chain, verify endpoint | F-42, F-43, F-44, F-45 | feat-05 AC-18..20 | H8 | 5 |
| TB-10 | Ready, metrics, JSON logs | F-46 | feat-06 AC-21, AC-23 | H8/H9 | 5 |
| TB-11 | Contract completion, route-coverage gate, test replacement for fake tests | F-50, F-51, F-52 | AC-22 | H9 | 5 |
| TB-12 | Behaviour-difference report and ADR-0001 supersession note, doc corrections (portal claim, injection payload claim) | F-05, F-53, F-60 | ADR-0002 | H10/H12 | 5 |
| TB-13 | Thin read-only operations view | F-05, F-52 | feat-01 AC-26 | J4 | 6 |
| TB-14 | Supply chain: SBOM, provenance, container-neutral recipe, IaC validation | F-07, F-48, F-49 | ADR-0009 | M1 | 5 |
| TB-15 | Resilience: retry/backoff, circuit breaker, failure injection, incident playbook, BC/DR | F-39, F-44, F-56 | resilience-traceability | M2..M4 | 5 |
| TB-16 | Observability dashboards and alerts as code, SLOs | F-46 | observability-spec | N1 | 5 |
| TB-17 | After-intervention KPIs and ROI | F-57 | metrics.yaml | O1..O3 | 6 |
| TB-18 | Encryption posture statement and key management plan | F-16 | security-architecture | K3 | 2 |

Sequence classes: 1 controls that make later work provable; 2 S1 security and identity; 3 data and semantic correctness; 4 AI boundary; 5 resilience and observability; 6 feature work (G1 ordering rule).

## Finding coverage
Every one of the 62 findings is attached to at least one backlog item or is already DONE (F-01, F-37, F-51 DONE in earlier stages; F-51 gets a diff step in H10). Check: see EVD-G-01.

## Do-not-change register
The eight assets in Document 01 section 7 stay unchanged unless a named finding forces a minimal edit.
| # | Asset | Why it stays | Exception |
|---|---|---|---|
| DNC-1 | scripts/sanity_check.py | smoke oracle | F-55: only if its hard-coded doc paths move; prefer keeping the paths |
| DNC-2 | data/manifest.json | fixture manifest | none |
| DNC-3 | docs/domain-specific-spec.md | domain oracle | none (additions go to docs/12-specs) |
| DNC-4 | docs/architecture/known-gaps.md | gap oracle | append-only status notes |
| DNC-5 | docs/runbooks/failure-injection-drills.md | M3 oracle | none |
| DNC-6 | observability/otel-notes.md | telemetry requirements, binding in F3 | none |
| DNC-7 | PRODUCTION_EVIDENCE_PACK_TEMPLATE.md | R2 template | none |
| DNC-8 | docs/architecture/target-state-principles.md | principles | none |
Also unchanged: data/synthetic/* (immutable fixture, OQ-14), legacy/reconcile_legacy.py behaviour until its retirement trigger (coexistence-strategy.md).
