# Evidence manifest: evidence/13-traceability

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-F-04-finding-coverage-matrix | `EVD-F-04-finding-coverage-matrix.csv` | 055a52f15d9daafa8d76bc642da760ea3a404790ac7d0fcefbb9f76ba1016821 | F4 | python gen_f4.py | 2026-10-08T10:03:32Z | Claude agent for Dinesh | stage-f-gate.md (F-X8) |
| EVD-F-05-stage-f-exit-checks | `EVD-F-05-stage-f-exit-checks.txt` | 1df22f4e7472cff0bdb6e7bf8948a79ac0ffb468ca210b1d70278c32fa003f4e | F5 | row count + git status | 2026-10-08T10:03:33Z | Claude agent for Dinesh | stage-f-gate.md |
| EVD-F-04b-finding-disposition-final | `EVD-F-04b-finding-disposition-final.csv` | 24dc4df12754670d842a7f1d8fb2d8dfa03eb8214dd35758a7e26577a6e774d1 | R5 | scratchpad/r_disp.py, from EVD-F-04 plus CI runs, tests and gate documents | 2026-10-08T12:27:21Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | final-gate.md; requirement-disposition-matrix.md |
