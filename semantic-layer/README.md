# Semantic Layer

| Field | Value |
|---|---|
| Stage | D: Semantic Layer Extraction |
| Runbook step | D1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL |
| Evidence sources | Semantic_Layer_capture.pdf |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

The model-independent definition of the logistics domain. Derived from the spec and from measured data, not from the product requirements, so a second model can regenerate the application from it (Stage Q).

| File | Role |
|---|---|
| glossary.md | human explanation of terms and fields |
| entities.yaml | entities, fields, types, units, keys, observed domains (source of truth) |
| status-taxonomy.yaml | legal values and reference types for categorical fields |
| enum-violations.md | observed violations with remedy |
| relationships.yaml | keys, cardinality, ordering and saga |
| business-rules.yaml | machine-evaluable invariants, including the six declared gaps |
| metrics.yaml | frozen KPI definitions |
| access-semantics.yaml | persona x entity x field x purpose |
| ai-context-policy.yaml | what may enter a prompt, limits, provenance, approval |
| schemas/ | JSON Schema for every YAML file |
| tests/ | conformance tests (run: `python -m pytest semantic-layer/tests`) |
| generated/semantic-layer.json | machine-consumable form; build output of `python semantic-layer/generate.py` |

Status: PROVISIONAL. Domains marked PROPOSED and data gaps (no position timestamp, no route override field) need Data Owner decisions (UNRESOLVED). Contains no vendor, framework or model-specific content (enforced by a test).
