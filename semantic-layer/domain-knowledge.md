# Domain Knowledge (capstone: domain intelligence and transformation-derived knowledge)

| Field | Value |
|---|---|
| Stage | D: Semantic Layer Extraction (re-aligned after transformation) |
| Runbook step | D1 (runbook/02-TRANSFORMATION-RUNBOOK.md), aligned to semantic-layer-build.txt |
| Version | v2.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL |
| Evidence sources | enum-violations.md; business-rules.yaml; workflow-semantics.yaml; docs/40-scale/semantic-layer-portability-test.md |
| Assumptions | Items tagged [ASM] need a business-owner decision |
| Unresolved issues | See the end of this file |
| Residual risks | The layer carries no competitor or market knowledge |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

This file holds knowledge that is not a field, rule or metric but that a person (or a model) needs to rebuild the system correctly. It is written without reference to any product, framework or model.

## 1. What the business does [VF]
Moves shipments from an origin to a destination under a service tier, using vehicles on routes, booked with carriers. Exceptions (delay, failure, hold) are the main operational pain: a person must notice, decide and act.

## 2. What the data taught us [VF]
Measured on the delivered fixture (full counts in enum-violations.md):
- Many categorical fields hold unrelated workflow words (fourteen interchangeable tokens). A field's name is therefore not proof that its value is meaningful. Every value is checked against a declared domain.
- 47 shipments and 37 bookings carry the status `approved`, which is not a lifecycle state. It is tolerated and flagged until an owner rules.
- Location, time zone, carrier, model and customer references are placeholders; real references are not in the data.
- Retry counts were observed from 51 to 4995, so the ceiling of 5 is an assumption, not a measured limit.
- There is no position timestamp and no route override field, so two rules (BR-03, BR-06) are declared but cannot be evaluated.

## 3. Domain intelligence worth keeping [INF]
- A shipment with an exception signal is the unit of work. Everything else (route, booking, vehicle) is context for deciding about it.
- Retries beyond the ceiling are a symptom to check, not something to repeat.
- Personal data (customer, driver, live location) is the reason access is by persona and purpose, and the reason an AI component sees none of it.
- A suggestion that changes anything must be approved by a person; the model is advisory by design.

## 4. Domain constraints
See `workflow-semantics.yaml` (domain_constraints DC-01 to DC-05) and `business-rules.yaml` (BR-01 to BR-13).

## 5. Context dependencies
See `workflow-semantics.yaml` (context_dependencies CD-01 to CD-05). In short: customer and driver masters are external; hub, fleet and customer attributes are absent; business-owner decisions on PROPOSED domains are open.

## 6. Competitive and market knowledge [UNK]
The transformation did not produce any. No competitor, benchmark or market data was supplied or researched, and none is claimed. If the capstone needs it, it must be added as a separate, sourced file.

## 7. Workflow semantics
See `workflow-semantics.yaml`: shipment lifecycle (an [ASM], not verifiable from single-status data), exception handling, the carrier booking saga, and how a suggestion is produced, bounded and approved.

## 8. Open items
1. Owner decisions on PROPOSED domains and the retry ceiling.
2. Whether approval may be self-approval (currently allowed).
3. Which personas may request a suggestion (currently every persona with shipments read).
4. Conflict detection at suggestion time (declared gap).
