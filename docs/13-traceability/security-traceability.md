# Security and privacy traceability

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

| Control | Requirement | Finding | Spec | Test | Stage |
|---|---|---|---|---|---|
| F-09 control | FR-19, NFR-7 | F-09 | security-spec | AC-24; secret scan | H3 |
| F-10 control | FR-19, NFR-7 | F-10 | security-spec | secret scan | H3 |
| F-11 control | FR-19, NFR-7 | F-11 | security-spec | secret scan | H3 |
| F-12 control | FR-19, NFR-7 | F-12 | security-spec | secret scan | H3 |
| F-14 control | NFR-7 | F-14 | security-spec | pre-commit + CI secret scan | H1/H3 |
| F-17 control | FR-03 | F-17 | feat-02 | AC-04, AC-05 | H4 |
| F-18 control | FR-04 | F-18 | feat-02 | AC-06 | H4 |
| F-19 control | FR-04 | F-19 | feat-02 | AC-06 (persona allow-list from semantic layer) | H4 |
| F-20 control | FR-03, FR-04 | F-20 | feat-02 | AC-04 | H4/H7 |
| F-21 control | FR-04 | F-21 | ADR-0005 | Rego parity test | H4 |
| F-22 control | FR-10 | F-22 | feat-04 | AC-13 | H7 |
| F-23 control | FR-10 | F-23 | feat-04 | AC-14 | H7 |
| F-26 control | FR-12 | F-26 | feat-04 | AC-17 | H7 |

Privacy: allow-listed AI context and masking (FR-04, FR-10) trace to AC-06 and AC-13. Encryption posture (F-16) is DEFERRED with an explicit assumption.
