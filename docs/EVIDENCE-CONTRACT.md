# Evidence Contract

| Field | Value |
|---|---|
| Stage | A: Engagement Mobilisation (Spine 0A to 0C), runbook step A2 |
| Runbook step | A2 |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, pending Transformation Lead confirmation |
| Evidence sources | runbook/00-RUNBOOK-OVERVIEW.md section 3 and 4; Prompts-Guidlines/AI_FDE_End-to-End_Production_Delivery_Spine.pdf (Global Workshop Execution Contract) |
| Assumptions | Operator Dinesh holds all role slots provisionally (OQ-05 default) |
| Unresolved issues | OQ-10 (retention) defaulted, not owner-confirmed |
| Residual risks | Provisional authority on every gate until OQ-05 is answered |

## 1. Rule
Analyse or execute, generate the required artifacts, save to the defined path, cite evidence, record assumptions and unknowns, validate the completion gate, then proceed. Never claim completion when required evidence is missing.

## 2. Mandatory header
Every artifact begins with a table carrying: Stage, Runbook step, Version, Date, Author / Agent, Status (Draft, In Review, Approved, Superseded), Evidence sources, Assumptions, Unresolved issues, Residual risks. This file is the model.

## 3. Classification
Every material statement is one of: **Verified Fact** (observed, source cited), **Inference** (derived, reasoning stated), **Assumption** (adopted to proceed, invalidation trigger stated) or **Unknown** (raised into runbook/04-OPEN-QUESTIONS-REGISTER.md). Assumptions are never presented as facts.

## 4. Storage
| Tree | Content |
|---|---|
| docs/<NN-stage-folder>/ | Human-readable artifacts named exactly as the Delivery Spine mandates |
| evidence/<NN-stage-folder>/ | Machine-generated raw evidence: reports, transcripts, scans, exports, hashes |

- Raw evidence naming: EVD-<stage>-<nn>-<slug>.<ext>
- Each evidence directory has a MANIFEST.md listing file, SHA-256, producing step, command, UTC timestamp, operator and the citing artifact.
- Evidence is append-only. A re-run produces a new file with an incremented number. Earlier baselines are never overwritten.

## 5. Where the trees live
docs/, evidence/ and semantic-layer/ sit at the **wrapper repository root**, beside 07-logistics-shipment-fleet-routing-ops/, not inside it. This keeps the as-delivered subtree untouched so every before/after diff can be scoped to it:

    git diff <baseline-tag> -- 07-logistics-shipment-fleet-routing-ops/

## 6. Baseline tags
| Tag | Meaning |
|---|---|
| baseline/v0-as-delivered | Initial commit 7ba349e. 45 of 51 subtree files byte-exact; 6 CSVs line-ending converted (see decision D-003) |
| baseline/v0.1-as-delivered-bytes | To be created after the .gitattributes fix; byte-exact for all 51 files. Use this tag for A-X2 and later byte comparisons |
