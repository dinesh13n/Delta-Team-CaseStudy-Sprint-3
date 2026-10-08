# Context engineering strategy

| Field | Value |
|---|---|
| Stage | F |
| Runbook step | F2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | Draft, PROVISIONAL (approvers UNRESOLVED, OQ-05) |
| Evidence sources | semantic-layer/relationships.yaml, ai-context-policy.yaml |
| Assumptions | See body |
| Unresolved issues | Owners UNRESOLVED |
| Residual risks | See data-context-risks.md |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

1. Context is typed JSON built by a pure function from curated rows: one shipment, its last N tracking events, applicable rule ids.
2. The allow-list comes from ai-context-policy.yaml. Identifier fields that point to people (vehicles.driver_id, shipments.customer_id) are excluded or pseudonymised; the policy file is the authority.
3. Token budget 2,000 per call [ASM]. Baseline is 904,432 tokens over 353 parsed rows, mean about 2,562 [VF].
4. The prompt template is versioned and holds untrusted fields only inside a delimited data block; output is schema-validated and may abstain.
5. The context hash is written to the audit record.
