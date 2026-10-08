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

## D-007 Runbook correction: F-42 correlation-id figure (2026-10-08) [SUPERSEDED by D-012]
- Independent count (EVD-A-04b, file hash matches the A1 baseline): 983 of 3,000 events have null correlation_id (32.8%), not 1,992 (66.4%) as the runbook states in F-42, the Overview and the README.
- Decision: the discovery pack uses the measured figure. Runbook text (01, 00, README, 02 Stage C5) to be corrected after operator approval. Status: proposed.

## D-008 Runbook corrections applied (2026-10-08, operator-approved)
- Applied to runbook/00, 01, 02, 04 and README (md and docx): F-42 and all "two-thirds / 66.4% / 1,992" wording replaced by 983 of 3,000 (32.8%); tag references changed to `baseline/v0.1-as-delivered-bytes` with an execution note in Step A1; A-X3 now reads 44 top-level spine directories plus 5 nested (closes D-005); OQ-04 note covers both tags.
- Runbook step reference: this resolves the stale text noted under A1/A2 and the discrepancy logged in D-007 (found at Step A4). D-007 status: applied.

## D-009 Stage H authorisation by operator instruction (2026-10-08)
- On 2026-10-08 the operator instructed the agent to complete runbook 02 end to end and push the result. This is recorded as operator authorisation to execute Stages B to R, including writes to the delivered subtree from Stage H (runbook Step G4 / OQ-11).
- Limits: it is the operator's authorisation, not the CTO's. It is flagged for CTO ratification (GOV-02). Stop conditions in stop-conditions.md still apply. Status: RECORDED, awaiting ratification.

## D-010 Runbook deviations found during Stage C (2026-10-08) [C1 item SUPERSEDED by D-012]
- C1 text: correlation completeness 33.6% should read 67.2% (follows from D-007).
- F-38: ai_invocations.csv also has one orphan shipment reference; register extended with F-58, F-59, F-60 (EVD-C-07-findings-index.json).
- Document 01 section 6.3 and F-22 claim the data holds injection payloads; none exist (max field length 19).
- Decision: runbook text corrections batched into one pass at the end of execution (step reference: runbook C1, C5, Doc 01 6.3). Status: PROPOSED.

## D-011 New findings from Stage D (2026-10-08)
- F-61: routes.weather_risk holds the numeric value 1.42 in a categorical field (EVD-D-02).
- F-62: every dataset has one malformed key `*-BAD1` (EVD-D-05 BR-P rules report 2 pattern violations per dataset: REC-0001 and the BAD1 key).
- Status: RECORDED; to be added to the findings register in the end-of-run runbook correction pass.

## D-012 Reversal of the F-42 correction (2026-10-08, found during Stage H8)
- Error: D-007, D-008 and D-010 said the runbook's F-42 figure (1,992 of 3,000 events, 66.4%) was wrong and "corrected" it to 983 (32.8%). That count looked only at JSON `null`. EVD-A-04c shows 983 null AND 1,009 events with an empty-string `correlation_id`, so 1,992 events (66.4%) carry no usable id and 1,008 (33.6%) do.
- Decision: the runbook figures (F-42 66.4%, C1 33.6%) were right. The F-42 wording in runbook 01, 02 and README is restored to "about two thirds, 1,992 of 3,000". D-007 and the F-42 and C1 parts of D-008 and D-010 are SUPERSEDED. The tag-reference and A-X3 corrections in D-008 stand.
- KPI K4 is amended (not to improve results; the baseline gets worse): usable share = non-null AND non-empty. Baseline restated to 33.6%; the literal non-null share (67.2%) is kept as a secondary figure in the KPI sheet. NFR-3 and DQ-06 mean non-empty.
- Other statements affected were updated in docs 00, 01, 04, 07, 11, 12 and in the runbook docx. Evidence files are not edited; EVD-A-04c is added and EVD-A-04b is superseded for this figure only.
- Lesson recorded: a one-pattern grep is not an independent count; profile by value class (null, empty, present).
- Status: APPLIED.

## D-013 (2026-10-08)
- Defect found at Stage R verification and confirmed by the first real GitHub Actions run (run 37774970836): the CI and `make cov` gate `--cov --cov-fail-under=80` measured 51% because `[tool.coverage.run] source` also listed `scripts` and `legacy`, which are evidence tooling and a legacy shim with little unit coverage. Every earlier gate document quoted 96-97% for `apps` + `etl`. The gate had never run (DEBT-01), so the mismatch was invisible.
- Decision: set `source = ["apps","etl"]` (the definition used in H11, I1 and the go/no-go criteria). Scripts are exercised by their own tests and by the evidence runs but are not part of the 80% gate. This narrows what the gate measures; it is disclosed, not hidden.
- Lesson: a gate that has not been executed in its real environment is not evidence. Status: APPLIED (commit following 4c84af1).
