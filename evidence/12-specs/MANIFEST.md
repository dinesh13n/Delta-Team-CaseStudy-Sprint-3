# Evidence manifest: evidence/12-specs

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-F-03-openapi | `EVD-F-03-openapi.yaml` | 6016a47d34dccadb44c6f7237cd3077f44edce88f5029801d5d1249272215c87 | F3 | copy of docs/12-specs/api-contracts/openapi.yaml | 2026-10-08T10:02:44Z | Claude agent for Dinesh | docs/12-specs/spec-readiness.md; stage-f-gate.md |
| EVD-F-03-openapi-validation | `EVD-F-03-openapi-validation.txt` | 0633960f82600f6fbf80d68cd7b6e60e9f2d87242ec53df855af06b55a35cd1a | F3 | openapi_spec_validator.validate | 2026-10-08T10:02:44Z | Claude agent for Dinesh | docs/12-specs/spec-readiness.md; stage-f-gate.md |
| EVD-F-03-schema-checks | `EVD-F-03-schema-checks.txt` | 8690d9106e92bc96d0d4c207a2bc2f377185076fab46e868a6e37d0ad708b26d | F3 | jsonschema Draft 2020-12 positive and negative instances | 2026-10-08T10:02:44Z | Claude agent for Dinesh | docs/12-specs/spec-readiness.md; stage-f-gate.md |
| EVD-F-03-route-coverage-diff | `EVD-F-03-route-coverage-diff.txt` | 9dbd1b3c0b3b193b3bb934a5ed36415c2b524817950f82f7f385bb18822a41f3 | F3 | python routediff.py | 2026-10-08T10:02:44Z | Claude agent for Dinesh | docs/12-specs/spec-readiness.md; stage-f-gate.md |
