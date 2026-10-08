# Semantic Layer

| Field | Value |
|---|---|
| Stage | D: Semantic Layer Extraction |
| Runbook step | D1 (runbook/02-TRANSFORMATION-RUNBOOK.md), re-aligned to semantic-layer-build.txt |
| Version | v2.0 |
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
| workflow-semantics.yaml | lifecycle, exception handling, saga, AI decision semantics (recommendation classes, abstain, fallback, approval), validation rules, domain constraints, context dependencies |
| domain-knowledge.md | domain intelligence and knowledge derived during the transformation; states that no competitive knowledge exists |
| api-contract.json | behavioural contract of the operations interface, framework-free |
| SEMANTIC-COMPLETENESS.md | assessment of completeness and portability, with the remaining gaps |
| schemas/ | JSON Schema for every YAML file |
| tests/ | conformance tests (run: `python -m pytest semantic-layer/tests`) |
| generated/semantic-layer.json | machine-consumable form; build output of `python semantic-layer/generate.py` |

Status: PROVISIONAL. Domains marked PROPOSED and data gaps (no position timestamp, no route override field) need Data Owner decisions (UNRESOLVED). Contains no vendor, framework or model-specific content (enforced by a test).

## Mapping to the suggested structure (semantic-layer-build.txt)

| Suggested file | This layer | Why different |
|---|---|---|
| README.md, glossary.md | same names | none |
| entities.yaml, relationships.yaml, business-rules.yaml, metrics.yaml, access-semantics.yaml | same names | none |
| taxonomy.yaml | status-taxonomy.yaml | name set earlier; a copy would drift, so none is kept |
| validation-schema.json | schemas/semantic-layer.schema.json | one schema with a definition per file |
| api-contract.json | api-contract.json | same |
| tests/ | tests/ | same |

Added beyond the suggestion because the requirement lists them: workflow-semantics.yaml (workflow semantics, validation rules, domain constraints, context dependencies), domain-knowledge.md (domain intelligence), SEMANTIC-COMPLETENESS.md (final assessment).

Order of work followed: transformation first, extraction after. Changes in v2.0 close the specification gaps found by the portability test (IMP-Q04 to IMP-Q11); the v1.0 files are preserved in version control and their hashes in the pre-registration evidence.
