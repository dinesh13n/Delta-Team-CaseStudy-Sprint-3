# Initial Product Requirements Document

| Field | Value |
|---|---|
| Stage | E: Intervention Qualification and Initial PRD (Spine 9) |
| Runbook step | E3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/03-problem-value/; docs/08-ai-qualification/; semantic-layer/ |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## 1. Problem
See docs/03-problem-value/problem-statement.md (technology-neutral).
## 2. Personas and journeys
Eight personas, reference journey: exception investigation (docs/03-problem-value/).
## 3. Capabilities
Trusted record access, contextual access control, validated data intake, governed exception summary, traceable decisions, operational telemetry (capability-map.md).
## 4. Functional requirements
20 requirements FR-01..FR-20 (functional-requirements.md), each traced to a business problem and evidence (initial-prd-traceability.md).
## 5. Non-functional requirements
NFR-1..NFR-10 (nfrs.md).
## 6. Scope
MVP in mvp-scope.md; exclusions in non-goals.md.
## 7. AI position
Only the exception summary uses a model, suggest-only (docs/08-ai-qualification/).
## 8. Constraints and dependencies
Platform, models, egress, approvers unresolved (open-product-decisions.md).
## 9. Success metrics (the frozen C1 KPI definitions, copied verbatim)

| ID | Name | Meaning | Formula | Unit | Owner (role) | Source | Period | Segmentation |
|---|---|---|---|---|---|---|---|---|
| K1 | Event latency | time recorded per event | percentile (index method, sorted[int(p/100*n)]) of `latency_ms` | ms | SRE Owner UNRESOLVED | events.jsonl | fixture, span unknown | by business_entity |
| K2 | Cost per event | declared cost units per event | sum(cost_units)/count(events) | cost units | Business Sponsor UNRESOLVED | events.jsonl | fixture | by business_entity |
| K3 | Severe-event share | share of events with severity error or critical | (error+critical)/total | % | SRE Owner UNRESOLVED | events.jsonl | fixture | by event_type |
| K4 | Correlation completeness | events with non-null correlation_id | non-null/total | % | Compliance Owner UNRESOLVED | events.jsonl | fixture | by actor |
| K5 | Declared AI tokens | token_count summed over invocations | sum(token_count), parseable rows | tokens | AI Governance Owner UNRESOLVED | ai_invocations.csv | fixture | by use_case |
| K6 | Carrier retry level | retry_count distribution | min/mean/max of retry_count | count | Operations Owner UNRESOLVED | carrier_bookings.csv | fixture | by carrier |
| K7 | Duplicate business keys | keys appearing more than once | count over all six datasets | keys | Data Owner UNRESOLVED | six CSVs | fixture | by dataset |
| K8 | Incomplete rows | rows with any blank field | count over six datasets | rows | Data Owner UNRESOLVED | six CSVs | fixture | by dataset |
| K9 | Baseline test result | passing tests / collected | pytest result | tests | Repository Owner UNRESOLVED | EVD-C-03 | run date | n/a |
| K10 | Baseline coverage | statement coverage of apps, etl, legacy, scripts | coverage.py | % | Repository Owner UNRESOLVED | EVD-C-03 | run date | by module |

## 10. Risks and open questions
product-risks.md, open-product-decisions.md.
