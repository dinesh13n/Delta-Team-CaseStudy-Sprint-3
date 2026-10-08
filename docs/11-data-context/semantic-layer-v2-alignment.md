# Semantic Layer v2.0 Alignment

| Field | Value |
|---|---|
| Stage | D: Semantic Layer Extraction (re-alignment) |
| Runbook step | D1, requirement from semantic-layer-build.txt |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL |
| Evidence sources | `semantic-layer-build.txt` (sha256 `f0052114bcf20188ca0099661ee8843ce8ab4eb3d549cf3d2f83a11f7ee18096`); `evidence/11-data-context/EVD-D-06-semantic-layer-v2-hashes.json` (sha256 `cffd158ffa517b9874ceb7b1e4ee15fc535273b9d437ad04a95bede40eb19fdf`); `evidence/11-data-context/EVD-D-06-semantic-v2-junit.xml` (sha256 `fc7501deca0483cf68eb7977ae3c6595f49e187be7338b691fcd27e051c55fd7`) |
| Assumptions | Recommendation classes, retry-check precedence and abstain mapping describe the application as built; they are not new business decisions |
| Unresolved issues | Owner decisions listed in semantic-layer/SEMANTIC-COMPLETENESS.md section 4 |
| Residual risks | v2.0 has not been re-tested with a second model |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## What the requirement asked for
A model-independent layer between application and model, built after the transformation, held as Markdown, YAML, JSON Schema, JSON and tests, with a final assessment of completeness and portability. [VF]

## What changed
| Change | File |
|---|---|
| Workflow semantics, AI decision semantics, validation rules, domain constraints, context dependencies | semantic-layer/workflow-semantics.yaml (new) |
| Domain intelligence, transformation-derived knowledge | semantic-layer/domain-knowledge.md (new) |
| API contract | semantic-layer/api-contract.json (new) |
| Platform roles, approver rule, summarise callers, purpose, mask, audit, scope, tenant | semantic-layer/access-semantics.yaml (extended) |
| Schema definitions, generator, README structure map | schemas, generate.py, README.md |
| Assessment | semantic-layer/SEMANTIC-COMPLETENESS.md (new) |
| Conformance of the application to the layer | 07-logistics-shipment-fleet-routing-ops/tests/test_semantic_conformance.py (new) |

No application code changed. Suite result: 28 passed for the layer and conformance tests (evidence above); full repository suite 181 passed, 1 skipped, 7 xfailed; lint, type check and the generated policy check pass. [VF]

## Integrity
The Stage Q pre-registration file is unchanged and still records the v1.0 hashes; the v2.0 hashes are in the new evidence file. Two earlier evidence files describe v1.0 (the JUnit file and the generated JSON copy in this folder); they are append-only and were not edited. The Stage D gate cites the old test name `test_nine_files_exist`, now `test_required_files_exist`. [VF]

## Not done
No second-model re-run of the portability test on v2.0, so closure of the eight gaps is by specification and by tests, not by observation. [INF]
