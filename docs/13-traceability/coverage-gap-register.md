# Coverage gap register

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | EVD-E-03; EVD-F-04; acceptance-criteria.md |
| Assumptions | See body |
| Unresolved issues | Test files are PLANNED (written in Stage H/J/L); no test result is claimed here |
| Residual risks | See coverage-gap-register.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Orphan requirements: **0** (every FR-01..FR-20 has a spec, AC and planned test). Untested specs: **0** for FR; NFR-1/2/9 are only testable in a test environment. Unjustified implementation: **0** planned (H steps map to findings). Unverifiable criteria: see below.

| Gap | Item | Description | Explanation |
|---|---|---|---|
| GAP-01 | F-16 | Encryption posture has no testable criterion in MVP | Explained: TLS terminates at the platform, which is unknown (OQ-01). Becomes testable when a platform is chosen. Owner UNRESOLVED. |
| GAP-02 | F-48, F-07 | IaC and container requirements cannot be verified without a platform | Explained: CONDITIONAL until OQ-01 resolved. |
| GAP-03 | F-59 | Weight discrepancy meaning unknown | Explained: flagged only; business owner needed (OQ-05). |
| GAP-04 | F-29 | AI answer quality cannot be measured with a deterministic provider | Explained: needs real model (OQ-02); evaluation in J/L marked CONDITIONAL. |
| GAP-05 | NFR-1, NFR-2, NFR-9 | Performance targets lack production-like environment | Explained: measured on a test host only; labelled as such in L. |
| GAP-06 | F-56 | Incident runbook owner/on-call does not exist | Explained: tabletop in M4 with role slots; real on-call UNRESOLVED. |
| GAP-07 | AC-26 | Operations view has no tests until the view exists | Explained: built in J4; test planned. |
| GAP-08 | F-06 | Frontend lint gate cannot be fixed while there is no frontend build | Explained: portal deferred (OQ-06). |

All gaps are explained; none is unexplained and critical. The gate (F-X7) therefore holds, with the dependency on OQ-01/02/05.
