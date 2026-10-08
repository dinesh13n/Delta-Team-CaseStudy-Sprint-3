# Evidence manifest: evidence/31-observability

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-N-01-full-suite | `EVD-N-01-full-suite.txt` | dcd4e5b0fa68b3dfb016e6b78802228458437b48d4f3d1de44da866debd0c916 | N1 | LATE REGISTRATION at R2: file produced earlier in step N1; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step N1 |
| EVD-N-01-observability-validation | `EVD-N-01-observability-validation.json` | b18c9aebb64f1dabeec34b6564f2d4e941468881eca1aa93229300a88af90485 | N1 | LATE REGISTRATION at R2: file produced earlier in step N1; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step N1 |
| EVD-N-01b-full-suite-after-p | `EVD-N-01b-full-suite-after-p.txt` | d05daff4a35eb0de4423bbce4f3887cd4c58c2116bfb10cfc36c642e4d19d842 | N1 | LATE REGISTRATION at R2: file produced earlier in step N1; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step N1 |
| EVD-N-02-reconstruction | `EVD-N-02-reconstruction.json` | 1eed65aa84641d9e7d564b91a99baa04006f1ba05ca26590cdae5a8181e6c241 | N2 | LATE REGISTRATION at R2: file produced earlier in step N2; hash taken 2026-10-08T12:12:48Z, so it proves the file is unchanged since R2, not since production | 2026-10-08T12:12:48Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs of step N2 |
