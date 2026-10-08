# Workflow Overview

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation, Spine 0A pre-flight discovery |
| Runbook step | A4 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, pending Transformation Lead review |
| Evidence sources | EVD-A-04-repo-tree-annotated.txt; EVD-A-04b-data-profile.txt; direct file reads of the repository; docs/domain-specific-spec.md |
| Assumptions | See assumptions-unknowns.md |
| Unresolved issues | See assumptions-unknowns.md |
| Residual risks | Read-only discovery only; no behavioural run yet (Stage C) |

Classification key: **[VF]** Verified Fact (read in a cited file), **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown. Paths are relative to `07-logistics-shipment-fleet-routing-ops/`. This document makes no transformation recommendations (Spine 0A).

## 1. Declared business flows (`docs/domain-specific-spec.md`)
1. Booking to pickup
2. Hub scan to route assignment
3. Carrier booking saga
4. Exception investigation to delivery evidence

## 2. Declared personas
dispatcher, warehouse_ops, fleet_manager, driver, customs_agent, customer_support, carrier_partner, ai_agent.

## 3. What exists in code for each flow
| Flow | Implemented? | Evidence |
|---|---|---|
| Booking to pickup | No | no booking or pickup logic in `apps/`, `etl/`, `legacy/` |
| Hub scan to route assignment | No | no routing code |
| Carrier booking saga | No | no saga, retry or compensation logic; only data columns |
| Exception investigation | Partial | read-by-id plus simulated AI summary |

- [VF] The four flow names appear as `event_type` values in `events.jsonl` (counts 758, 715, 763, 764) and the eight personas as `actor` values (356-398 each, EVD-A-04b).
- [VF] The API role allow-list is `admin, operator, clinician, engineer, ai_agent` (`main.py` line 13); it shares only `ai_agent` with the declared personas.
- [INF] The role list appears to originate from another domain template (`clinician`).
- [UNK] How operators actually perform these flows today; who the real users are.
