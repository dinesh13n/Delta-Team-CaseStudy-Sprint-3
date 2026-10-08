# Semantic Completeness and Portability Assessment

| Field | Value |
|---|---|
| Stage | D (extraction) assessed against Stage Q (portability) |
| Runbook step | D1 and Q1 to Q4, aligned to semantic-layer-build.txt |
| Version | v2.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL |
| Evidence sources | docs/40-scale/semantic-layer-portability-test.md; evidence/40-scale/EVD-Q-06-comparison.csv; the layer's own tests |
| Assumptions | Items tagged [ASM] are owner decisions not yet taken |
| Unresolved issues | Listed in section 4 |
| Residual risks | v2.0 has not been re-tested with a second model |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## 1. Required content against what the layer holds
| Required (semantic-layer-build.txt) | Where | State |
|---|---|---|
| Business glossary | glossary.md | covered [VF] |
| Entities | entities.yaml (56 of 56 columns) | covered [VF] |
| Relationships | relationships.yaml | covered [VF] |
| Taxonomies and status definitions | status-taxonomy.yaml, enum-violations.md | covered; PROPOSED domains await owners [ASM] |
| Business rules | business-rules.yaml (BR-01 to BR-13) | covered; two rules cannot be evaluated for lack of data |
| Metrics and KPIs | metrics.yaml (K1 to K10) | covered |
| Access semantics | access-semantics.yaml | covered; v2.0 adds platform roles, approver rule, summarise callers, purpose, mask, audit, scope, tenant |
| Domain intelligence | domain-knowledge.md | covered from what the transformation measured |
| Competitive and market knowledge | domain-knowledge.md section 6 | NOT PRESENT [UNK]; none was supplied |
| Domain constraints, validation rules, workflow semantics, context dependencies | workflow-semantics.yaml | covered in v2.0 |
| Validation schema | schemas/semantic-layer.schema.json | covered for all YAML files and the API contract |
| API consumption JSON | api-contract.json, generated/semantic-layer.json | covered in v2.0 |
| Tests | tests/ (semantic-layer) and tests/test_semantic_conformance.py (application) | 23 layer tests and 5 conformance tests pass |

## 2. What the portability test found, and what v2.0 does about it
The v1.0 test (single run, Claude Haiku as Model B) rebuilt a four-behaviour subset of the application that passed its own tests, working from the layer plus the Implementation PRD, the Stage F specifications, the prompt registry, sample data and a build brief (not from the layer alone). The build differed from the original on eight points where the layer was silent or contradictory. v2.0 specifies each:

| Gap | Closed by |
|---|---|
| Recommendation classes undefined (IMP-Q04) | workflow-semantics.yaml: three classes, precedence, class-not-wording rule |
| Retry-check rule absent (IMP-Q05) | class check_booking_retries, ceiling 5 tied to BR-13 |
| Legacy status in the AI path (IMP-Q06) | abstain insufficient_context |
| Insufficient context, sources conflict (IMP-Q07) | defined; conflict detection recorded as a declared gap |
| Fallback against abstain contradiction (IMP-Q08) | order: fallback first, then abstain; low confidence abstains without fallback |
| Who may call the summary (IMP-Q09) | access-semantics.yaml ai_summarize; narrowing is an owner decision |
| Approver, reviewer, ops, auditor roles (IMP-Q10) | platform_roles and approver_rule; reviewer stays [UNK] |
| Purpose, mask, audit failure, 404 audit, scope, tenant (IMP-Q11) | operating_semantics |

## 3. The six comparison areas, as far as evidence goes
| Area | Assessment |
|---|---|
| PRD generation | not tested: Model B was given a PRD, not asked to produce one [VF]; v2.0 has not been re-run |
| Application generation | v1.0: a working four-behaviour subset, not the whole application; differences traced to the eight gaps above |
| Context completeness | eight gaps found and now specified; others may remain until a re-run |
| Model independence | one run, one vendor family; enforced neutrality in the YAML files by test; not proof of independence |
| Repository dependency | the original code was not given to Model B, but the PRD, specifications and brief (written by Model A) were; so the layer alone was not shown to suffice [VF] |
| Knowledge transfer quality | judged by one agent; independent review not done (IMP-Q13) |

## 4. Gaps that remain
1. v2.0 not re-tested; claims of closure are by specification and by conformance test, not by a second model [INF].
2. No competitive or market knowledge.
3. Shipment lifecycle transitions are an assumption.
4. Retry ceiling, PROPOSED domains, self-approval and summary callers are owner decisions.
5. Two rules (BR-03, BR-06) need data that does not exist.
6. Conflict detection at suggestion time is not implemented.
7. The layer is checked against the application by tests, but the application still holds the platform-role table in code; the test keeps them equal.

## 5. Conclusion
Complete for the elements the requirement lists, except competitive knowledge. Portable in the sense that a second model rebuilt a working application from it once; not yet shown to be portable at the v2.0 level.
