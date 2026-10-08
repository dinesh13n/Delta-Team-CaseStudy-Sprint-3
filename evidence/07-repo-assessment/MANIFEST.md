# Evidence manifest: evidence/07-repo-assessment

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-C-02-quickstart-transcript | `EVD-C-02-quickstart-transcript.txt` | 74e85bd8cec2ade87fc4ccf8a95b40552928010bfd689e761b21868fdf541581 | C2/C3 | see transcript | 2026-10-08T09:45:54Z | Claude agent for Dinesh | docs/07-repo-assessment/baseline-behaviour.md |
| EVD-C-03-transcript | `EVD-C-03-transcript.txt` | e00e2c43b291f1a06e7144f029873e2b4422672353800328fc2534d30060b743 | C2/C3 | see transcript | 2026-10-08T09:45:54Z | Claude agent for Dinesh | docs/07-repo-assessment/baseline-behaviour.md |
| EVD-C-03-junit | `EVD-C-03-junit.xml` | 1d96dc44eb81588a1155ba4566d8d87ab7ef22d62ba21b803f7835d3926ca8da | C2/C3 | see transcript | 2026-10-08T09:45:54Z | Claude agent for Dinesh | docs/07-repo-assessment/baseline-behaviour.md |
| EVD-C-03-coverage | `EVD-C-03-coverage.xml` | 85210479df1b835c07459cca3a26494695ede817d7399bc85133811e92b607e8 | C2/C3 | see transcript | 2026-10-08T09:45:54Z | Claude agent for Dinesh | docs/07-repo-assessment/baseline-behaviour.md |
| EVD-C-07-findings-index | `EVD-C-07-findings-index.json` | 6c387bfd6ea34ba4aca6464d7bcea97e164f439d89acc063516ecec85e016a98 | C7 | parsed from runbook/01 plus F-58..F-60 | 2026-10-08T09:47:28Z | Claude agent for Dinesh | docs/07-repo-assessment/technical-debt-register.md |
| EVD-C-08-characterization-junit | `EVD-C-08-characterization-junit.xml` | b35040581e79ee0e1b912f8399b855e60ef591ad76c24faa27eb7c0169ffd90e | C8 | pytest tests/characterization -m characterization (copy of baseline) | 2026-10-08T09:48:24Z | Claude agent for Dinesh | docs/07-repo-assessment/stage-c-gate.md |
| EVD-C-09-stage-c-exit-checks | `EVD-C-09-stage-c-exit-checks.txt` | 61b3292ae9002e9da7fbdc5d30c3074b8c983a2ac01c20c0fd1fdfadd44b9828 | C9 | bash checks | 2026-10-08T09:48:24Z | Claude agent for Dinesh | docs/07-repo-assessment/stage-c-gate.md |
