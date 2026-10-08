# Privacy impact assessment (incl. location data)

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | semantic-layer/access-semantics.yaml, ai-context-policy.yaml, EVD-K-02 |
| Assumptions | See body |
| Unresolved issues | OQ-04, OQ-21 retention and rights |
| Residual risks | P-06..P-09 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

## 1. Scope and legal basis
[UNK] No jurisdiction or regime is named (OQ-04, OQ-21). The assessment is by data category, not by statute. Applicability of any law is **not asserted**.

## 2. Personal and sensitive data in scope
| Data | Where | Category | Purpose | Retention |
|---|---|---|---|---|
| `customer_id` (CUS-nnnnn) | shipments | pseudonymous identifier | dispatch, support | [UNK] |
| `driver_id` | vehicles | pseudonymous identifier of a worker | fleet ops | [UNK] |
| `current_location` | vehicles | **location of an identifiable worker** | live assignment | [UNK] |
| `location` | tracking_events | shipment position (indirectly a driver position) | tracking | [UNK] |
| `origin` / `destination` | routes | place data | routing | [UNK] |
[VF] All values in the repository are synthetic. No real person's data exists. The assessment is written for a real deployment.

## 3. Findings
| ID | Risk | Rating | Mitigation |
|---|---|---|---|
| P-01 | worker location visible to every persona | High (original) | persona and purpose policy; only fleet roles with an operational purpose see it |
| P-02 | location or driver identity in AI prompts | High (original) | forbidden fields; sanitiser; leak check; eval `forbidden_field_leak_rate` 0.0 |
| P-03 | location in logs (F-13 DEBUG default) | Medium | default INFO; logs carry ids and statuses, not locations |
| P-04 | `customer_id` shown to dispatchers | Low | masked `***` for dispatcher; unmasked for customer_support by field override |
| P-05 | stale or wrong position used to act | Medium | none possible (no timestamp); no assignment code |
| P-06 | retention undefined | Medium | OPEN; evidence-retention-policy proposes classes |
| P-07 | data subject rights (access, deletion) | Medium | OPEN: no deletion path; audit chain is append-only by design (conflict to resolve with the owner) |
| P-08 | cross-border transfer (customs persona, hosted model) | Medium | OPEN until OQ-02/OQ-01 |
| P-09 | purpose limitation weak when purpose is defaulted | Medium | RL-02 accepted |

## 4. Minimisation by default
Following the recommended default for OQ-21: location fields are excluded from prompts and from logs, and masked for personas without an operational purpose. Over-protecting is recoverable; under-protecting is not.

## 5. Decision
CONDITIONAL: the technical controls are in place and tested; retention, subject rights and legal basis need an owner (Compliance Owner, UNRESOLVED).
