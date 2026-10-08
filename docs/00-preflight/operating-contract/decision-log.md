# Decision Log (Stage A)

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation |
| Runbook step | A1, A2 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft |
| Evidence sources | evidence/00-preflight/EVD-A-01-*, EVD-A-02-spine-tree.txt; runbook/04-OPEN-QUESTIONS-REGISTER.md |
| Assumptions | Operator Dinesh acts as Transformation Lead with PROVISIONAL AUTHORITY (OQ-05 default) |
| Unresolved issues | D-002, D-003 await operator confirmation |
| Residual risks | All approvals provisional until named approvers exist |

| ID | Decision | Basis | Status |
|---|---|---|---|
| D-001 | **OQ-13 ruling.** The spine path docs/00-preflight/discovery/ is authoritative. The delivered 07-logistics-shipment-fleet-routing-ops/docs/discovery/README.md is left untouched, not converted to a pointer (runbook A2 suggested a pointer). Reason: editing it would alter the as-delivered subtree before write authorisation exists (OQ-11). The two paths no longer collide because the spine lives at the wrapper root. | Verified Fact: sanity_check.py does not require that file; runbook A2 | DECIDED (provisional) |
| D-002 | **OQ-10 default.** Evidence stays in-repository under evidence/, hash-manifested and version-controlled. Runtime audit records will go to an external append-only store (decided in Stage F). | Runbook 04, OQ-10 recommended default | DEFAULTED, awaiting owner |
| D-003 | **Baseline byte-exactness.** The six delivered CSVs had CRLF line endings; core.autocrlf converted them to LF at commit, so tag baseline/v0-as-delivered is not byte-exact for them. Content is identical after CR removal (Verified Fact). Remedy: add .gitattributes with -text for the subtree, renormalise, commit, tag baseline/v0.1-as-delivered-bytes. The v0 tag is not moved. The root README and the initial commit message call the baseline byte-identical; that wording is accurate only for the v0.1 tag. | EVD-A-01-delivered-vs-committed.csv | PROPOSED, operator action needed |
| D-004 | **Authorisation scope.** On 2026-10-08 the operator instructed execution of the runbook to begin. Treated as authorisation for read-only stages A to G (A1 and A2 add only new files outside the subtree). Write authorisation for Stage H (OQ-11, step G4) has NOT been given. | Operator instruction in session | RECORDED |
| D-005 | **Spine count.** Runbook A-X3 says 43 spine directories. The spine has 44 top-level folders (00 to 42 is 43, plus final-prd) and 5 nested ones, mirrored by 44 evidence folders. Criterion A-X3 should read 44 plus 5. | EVD-A-02-spine-tree.txt | NOTED, runbook text to be corrected |

## D-006 Runtime versions (2026-10-08)
- Operator requested Python 3.14 and latest Node. Probe EVD-A-03c shows pinned dependencies do not install on 3.14.
- Decision: baseline (Stage C) on Python 3.11; target runtime 3.14 plus upgraded pins from Stage H. Status: proposed, pending operator confirmation.

## D-007 Runbook correction: F-42 correlation-id figure (2026-10-08)
- Independent count (EVD-A-04b, file hash matches the A1 baseline): 983 of 3,000 events have null correlation_id (32.8%), not 1,992 (66.4%) as the runbook states in F-42, the Overview and the README.
- Decision: the discovery pack uses the measured figure. Runbook text (01, 00, README, 02 Stage C5) to be corrected after operator approval. Status: proposed.

## D-008 Runbook corrections applied (2026-10-08, operator-approved)
- Applied to runbook/00, 01, 02, 04 and README (md and docx): F-42 and all "two-thirds / 66.4% / 1,992" wording replaced by 983 of 3,000 (32.8%); tag references changed to `baseline/v0.1-as-delivered-bytes` with an execution note in Step A1; A-X3 now reads 44 top-level spine directories plus 5 nested (closes D-005); OQ-04 note covers both tags.
- Runbook step reference: this resolves the stale text noted under A1/A2 and the discrepancy logged in D-007 (found at Step A4). D-007 status: applied.
