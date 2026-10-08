# Evidence manifest: evidence/00-preflight

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-A-01-baseline-file-manifest | `EVD-A-01-baseline-file-manifest.sha256` | 8eb89d1ff2dd835d78f823662e6dca0713b94034f71263504653d0cabba3fac2 | A1 | see file / runbook step A1 | 2026-10-08T08:42:57Z | Claude agent for Dinesh | docs/00-preflight/operating-contract/decision-log.md |
| EVD-A-01-delivered-vs-committed | `EVD-A-01-delivered-vs-committed.csv` | dd2382a160a0c7586ca6ed393b90ec26b4113f6bb28e106fa2c1bcdeeb6ca30c | A1 | see file / runbook step A1 | 2026-10-08T08:42:57Z | Claude agent for Dinesh | docs/00-preflight/operating-contract/decision-log.md |
| EVD-A-01-tag-verification | `EVD-A-01-tag-verification.txt` | a507d3d45cee3dd0598ca179c229ae213ef15c999ada6eb1353c4eea4be4b70b | A1 | see file / runbook step A1 | 2026-10-08T08:42:57Z | Claude agent for Dinesh | docs/00-preflight/operating-contract/decision-log.md |
| EVD-A-02-spine-tree | `EVD-A-02-spine-tree.txt` | 38db5b75d91b98521a40d52a5b623280bb9d038890ab23574a0ece327e2b0406 | A2 | see file / runbook step A2 | 2026-10-08T08:42:57Z | Claude agent for Dinesh | docs/00-preflight/operating-contract/decision-log.md |
