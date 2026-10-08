# Dependency sequence

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

```
H1 gates -> H2 repro -> H3 secrets -> H4 identity -> H5 lookup -> H6 ETL -> H7 AI gateway -> H8 audit -> H9 contract -> H10 diff -> H11 validate
```
| Step | Must come after | Reason |
|---|---|---|
| H1 | none | gates make every later increment provable (G1 class 1) |
| H2 | H1 | tests must run before they can guard anything |
| H3 | H1 | the scanner exists first |
| H4 | H2, H3 | identity needs secrets handling (token key) |
| H5 | H4 | lookup responses are filtered per persona |
| H6 | H5 | the curated layer is read by the repository the lookup uses |
| H7 | H4, H6 | gateway uses policy and curated context |
| H8 | H4, H7 | audit records need actor and model fields |
| H9 | H4..H8 | contract asserts the state those steps create |
Evidence and control work (H1, H2, H3) precede feature work (J4, TB-13), as G-X3 requires.
