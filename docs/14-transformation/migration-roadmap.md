# Migration roadmap

| Field | Value |
|---|---|
| Stage | G |
| Runbook step | G1 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/10-architecture; docs/11-data-context; docs/12-specs |
| Assumptions | See body |
| Unresolved issues | Approvers UNRESOLVED; platform OQ-01 |
| Residual risks | See transformation-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Increment | Content | Backlog | Exit evidence |
|---|---|---|---|
| INC-0 | Baseline frozen (done) | | tags, hash manifest |
| INC-1 | Governance and gates | TB-01, TB-02 | CI green, pre-commit |
| INC-2 | Reproducibility | TB-03 | clean-checkout run |
| INC-3 | Secrets | TB-04 | secret scan 0 |
| INC-4 | Identity and policy | TB-05 | AC-04..07 |
| INC-5 | Lookup semantics | TB-06 | AC-01..03 |
| INC-6 | Data intake | TB-07 | AC-08..11 |
| INC-7 | AI gateway | TB-08 | AC-12..17 |
| INC-8 | Audit, correlation, observability | TB-09, TB-10 | AC-18..21, 23 |
| INC-9 | Contract and tests | TB-11, TB-12 | AC-22, behaviour-difference report |
| INC-10 | Validation gate | | H11 report |
Later stages (I..R) add the intelligence evaluation, thin view, supply chain, resilience, release and value work. Each increment is one reviewable commit group with finding IDs in the message.
