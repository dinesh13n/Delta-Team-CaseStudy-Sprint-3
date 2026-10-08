# Assumptions Register

| Field | Value |
|---|---|
| Stage | B: Problem Framing (Spine 3) |
| Runbook step | B3 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL approval (OQ-05) |
| Evidence sources | docs/00-preflight/discovery/*; docs/00-preflight/operating-contract/*; docs/00-preflight/stage-a-gate.md; docs/01-engagement/*; docs/domain-specific-spec.md (repo) |
| Assumptions | See assumptions in body |
| Unresolved issues | OQ-08, OQ-24 |
| Residual risks | Self-approved gate until named approvers exist |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| ID | Assumption | Invalidation trigger |
|---|---|---|
| AR-1 | Operator acts for all roles provisionally | named approvers appear (OQ-05) |
| AR-2 | Proxy KPIs are acceptable as baseline | sponsor rejects (OQ-08) |
| AR-3 | Data is synthetic and non-personal | evidence of real data |
| AR-4 | Local open-weights models are acceptable (OQ-02) | sponsor names models |
| AR-5 | Platform-neutral design is acceptable (OQ-01) | platform named |
| AR-6 | No egress available (OQ-03) | policy allows egress |
| AR-7 | Derived curated data layer for remediation (OQ-14) | owner chooses otherwise |
| AR-8 | Time budget is bounded but unknown (OQ-12) | deadline given |
