# Optimisation backlog

| Field | Value |
|---|---|
| Stage | N |
| Runbook step | N4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (backlog) |
| Evidence sources | evidence/32-finops/EVD-N-04-finops-model.json (SHA-256 207c99d898ebf3cee5d81c1a7990823b06c41fd606117872a91936195f437bac) |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

Every item must keep the L1 thresholds (schema valid 100%, forbidden-field leak 0, injection leak 0, abstention correct 100%, approval flag 100%); a change is proposed only with a TEVV re-run.

| ID | Item | Expected effect | Needs |
|---|---|---|---|
| OPT-01 | Response cache keyed on (record, data load, prompt version, config hash) | fewer model calls | owner decision on audit semantics |
| OPT-02 | Provider prompt caching for the locked system prompt | lower input cost | a provider that supports it |
| OPT-03 | Smaller model for routine records, larger for exceptions (routing) | lower cost | Stage Q comparison on this oracle |
| OPT-04 | Cache `audit.verify()` result in `/metrics` (DEBT-N1-01) | removes an O(n) scrape cost | code change |
| OPT-05 | Audit rotation / archive | bounded storage | retention decision (RA-01) |
| OPT-06 | Review-time reduction: show the facts used beside the suggestion | cuts the dominant cost | UX work, a user study |
| OPT-07 | Only call the model when the deterministic summary abstains or is low-confidence | fewer calls | evaluation of quality loss |

Not done: none of these was implemented in N4; the stage measures, it does not optimise without a baseline from a real model.
