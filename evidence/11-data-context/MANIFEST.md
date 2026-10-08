# Evidence manifest: evidence/11-data-context

Every raw evidence file in this directory must be listed here (see docs/EVIDENCE-CONTRACT.md section 4).
Evidence is append-only: a re-run creates a new file with an incremented number, never an overwrite.

| Evidence ID | File | SHA-256 | Producing step | Command | UTC timestamp | Operator | Cited by |
|---|---|---|---|---|---|---|---|
| EVD-D-01-field-coverage | `EVD-D-01-field-coverage.csv` | 298054a6d5c07cc41202e4816df2e3f90438d03b9e8044747e3c06828fce293c | D1-D5 | python gen_d12.py (from entities.yaml sources) | 2026-10-08T09:53:26Z | Claude agent for Dinesh | docs/11-data-context/stage-d-gate.md |
| EVD-D-02-enum-violations | `EVD-D-02-enum-violations.csv` | 358e7392b8fad0b672ac5a4ee4b0e352b863e544f23a1ba9a637aac1c51f2ea7 | D1-D5 | python gen_d2.py | 2026-10-08T09:53:26Z | Claude agent for Dinesh | docs/11-data-context/stage-d-gate.md |
| EVD-D-03-rule-to-gap-trace | `EVD-D-03-rule-to-gap-trace.csv` | 5388fb6ad5f0454598a0488454a4012d3de54936d2defb84bbce6134f3c5a582 | D1-D5 | python gen_d3.py | 2026-10-08T09:53:26Z | Claude agent for Dinesh | docs/11-data-context/stage-d-gate.md |
| EVD-D-04-access-semantics-matrix | `EVD-D-04-access-semantics-matrix.csv` | f95609856b8284299d323c48befa7e688f60c55d31c5ef508581d05121b005c8 | D1-D5 | python gen_d4.py | 2026-10-08T09:53:26Z | Claude agent for Dinesh | docs/11-data-context/stage-d-gate.md |
| EVD-D-05-rule-baseline | `EVD-D-05-rule-baseline.json` | d44af9df668fa79e00af0ee2da9c0cdad84ff6e6bf9ac1c8b225d9d085132d55 | D1-D5 | rule_eval over baseline data | 2026-10-08T09:53:26Z | Claude agent for Dinesh | docs/11-data-context/stage-d-gate.md |
| EVD-D-05-semantic-layer-junit | `EVD-D-05-semantic-layer-junit.xml` | cb1fc7cbbef53af7b1e21ab6a657e65dcc0b84dcfe178ca91dad5ebb127dae45 | D1-D5 | pytest semantic-layer/tests | 2026-10-08T09:53:26Z | Claude agent for Dinesh | docs/11-data-context/stage-d-gate.md |
| EVD-D-05-generated-semantic-layer | `EVD-D-05-generated-semantic-layer.json` | edf62772dc55687db93dd20f3e520331db0e5f247d936c0ced401cee79083bf2 | D1-D5 | python semantic-layer/generate.py (generated, not hand-written) | 2026-10-08T09:53:26Z | Claude agent for Dinesh | docs/11-data-context/stage-d-gate.md |
| EVD-D-06-semantic-v2-junit | `EVD-D-06-semantic-v2-junit.xml` | fc7501deca0483cf68eb7977ae3c6595f49e187be7338b691fcd27e051c55fd7 | D6 | pytest semantic-layer/tests tests/test_semantic_conformance.py; hash listing of semantic-layer/ | 2026-10-08T16:53:46Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs/11-data-context/semantic-layer-v2-alignment.md |
| EVD-D-06-semantic-layer-v2-hashes | `EVD-D-06-semantic-layer-v2-hashes.json` | cffd158ffa517b9874ceb7b1e4ee15fc535273b9d437ad04a95bede40eb19fdf | D6 | pytest semantic-layer/tests tests/test_semantic_conformance.py; hash listing of semantic-layer/ | 2026-10-08T16:53:46Z | Claude Code agent (claude-sonnet-5-5), operator Dinesh | docs/11-data-context/semantic-layer-v2-alignment.md |
