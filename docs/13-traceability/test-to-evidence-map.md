# Test to evidence map

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

| Test group | Evidence it will produce | Evidence ID (planned) | Stage |
|---|---|---|---|
| tests/unit/test_record_lookup.py | pytest junit XML + coverage | EVD-H-01 | H |
| tests/unit/test_identity_policy.py | pytest junit XML + coverage | EVD-H-02 | H |
| tests/unit/test_etl_quarantine.py | pytest junit XML + coverage | EVD-H-03 | H |
| tests/unit/test_ai_gateway.py | pytest junit XML + coverage | EVD-H-04 | H |
| tests/unit/test_audit_chain.py | pytest junit XML + coverage | EVD-H-05 | H |
| tests/integration/test_contract_ops.py | pytest junit XML + coverage | EVD-H-06 | H |
| characterization tests (exist) | junit | EVD-C-08 | C (done), H10 (diff) |
| semantic-layer tests (exist) | pytest output | EVD-D-0x | D (done) |
| performance, load | latency report | EVD-L | L |
| AI eval set | eval report | EVD-J | J |
| red-team | findings log | EVD-L | L |

Every evidence file is registered in its folder MANIFEST.md with SHA-256 at creation (spine rule).
