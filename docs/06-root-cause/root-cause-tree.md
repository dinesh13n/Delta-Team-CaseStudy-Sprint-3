# Root Cause Tree

| Field | Value |
|---|---|
| Stage | C: Baseline (Spine 6 root cause) |
| Runbook step | C6 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | docs/07-repo-assessment/baseline-behaviour.md; docs/05-current-state/; EVD-C-02, EVD-C-03, EVD-C-05; docs/ADR in subtree |
| Assumptions | See body |
| Unresolved issues | See body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

```
Operations cannot trust or prove their information (problem-statement.md)
|-- RC-1 Governance never designed in: ADR-0001 "accepted, never revisited"; no owner, no change control (F-08, F-53)
|     |-- audit and access written per code path, differ across paths (F-17, F-43, F-44)
|-- RC-2 Identity not modelled: record identity is a free string matched across any column; caller identity is a header
|     |-- cross-entity key REC-0001, first-row fallback (F-30, F-31, F-32); role header (F-17..F-20)
|-- RC-3 Data accepted without contracts: no schema, enum domain or key constraint; ETL counts and discards
|     |-- duplicates, blanks, impossible values, polluted enums (F-33..F-38, F-40)
|-- RC-4 AI added as a feature, not as a governed subsystem
|     |-- open prompt interpolation, no schema, no gate, simulated output (F-22..F-29)
|-- RC-5 Evidence not produced as a by-product: no CI evidence, thin tests, undeclared dependency
      |-- F-02, F-47, F-51, F-52
```
