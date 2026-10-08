# Audit evidence index

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (index) / CONDITIONAL (manifest hashes verified in R2) |
| Evidence sources | evidence/31-observability/EVD-N-02-reconstruction.json (SHA-256 1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

"Where is the proof that …?" Updated in N2 with the reconstruction path and the observability evidence. Hash-level verification of every manifest is done once, in R2 (`evidence/EVIDENCE-INDEX.md`).

| Question an auditor asks | Evidence |
|---|---|
| Who changed access rules and when? | git history of `semantic-layer/access-semantics.yaml`; policy parity test |
| Who approved an AI suggestion? | audit event `ai.decision` (`approval_id`, `actor`); approval store (`kind: decision`) |
| Can the same person request and approve? | **Yes** (HC-R-01); shown in EVD-N-02 observations |
| Was the AI ever allowed to act? | `tests/test_human_control.py` (no mutating route besides the decision) |
| What prompt produced this output? | audit detail `prompt_version`; `prompts.lock.json` |
| Was the audit log tampered with? | `GET /audit/verify`; `scripts/reconstruct.py`; tamper test in EVD-N-02 |
| Which data version answered a request? | audit detail and `X-Data-Load-Id` (`data_load_id`) |
| Which data was excluded and why? | `data/quarantine/*.csv` reasons; `evidence/11-data-context/` |
| Were thresholds set before results? | `evaluation/thresholds.json`; git commit order (J-X2, L-X1) |
| What did the red team try? | `evidence/26-tevv/EVD-L-03-*` |
| Do the alerts and dashboards match the code? | `evidence/31-observability/EVD-N-01-observability-validation.json` |
| Can an incident be reconstructed? | `docs/31-observability/incident-reconstruction-example.md`, `EVD-N-02-reconstruction.json` |
| Can the system be restored from backup? | `evidence/30-release/EVD-N-03-backup-restore.json` (N3) |
| Did the AI incident playbook work? | `evidence/29-incident-bcdr/EVD-M-04-tabletop-simulation.json` (author-run) |
| Which evidence is intact? | each `evidence/<NN>/MANIFEST.md` + `evidence/EVIDENCE-INDEX.md` (R2) |

## Gaps an auditor will find
- The model's exact output text is not retained in audit.
- No independent reviewer has run any of the checks above (TEVV-R-01).
- Evidence was produced on one machine by one agent; there is no second system's copy of the audit tip hash.
