# Evidence retention policy (proposal, OQ-10)

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | CONDITIONAL |
| Evidence sources | docs/EVIDENCE-CONTRACT.md |
| Assumptions | See body |
| Unresolved issues | OQ-10 |
| Residual risks | P-07 |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Class | Examples | Proposed retention | Store | Integrity |
|---|---|---|---|---|
| Delivery evidence | `evidence/<NN>/` files | life of the repository + 1 year after retirement | git (this repo) | SHA-256 in each directory `MANIFEST.md`; append-only |
| Audit log | `logs/audit-v2.log` | [UNK] (record-keeping duty CO-09); proposal 1 year hot, 6 years archive | platform storage | hash chain, `/audit/verify` |
| AI trace | audit events with `retention_class: ai_trace` (input hash, model, prompt version) | 90 days | audit | same chain |
| Approvals | `logs/approvals.jsonl` | same as audit | file | referenced from audit |
| Quarantine | `data/quarantine/*.csv` | until remediated + 90 days | data store | n/a |
| Evaluation runs | `evidence/26-tevv/` | permanent in git | git | manifest |
| Personal data | customer and driver ids | [UNK] (P-06) | – | – |

Rules: evidence is never overwritten (a re-run is a new numbered file); a superseded file stays and is marked superseded in the manifest; deleting the audit log is a privileged, logged action by a person (never the system).
Conflict recorded: audit immutability vs deletion of personal data on request (P-07) needs the Compliance Owner (pseudonymise-in-place or crypto-erase options).
