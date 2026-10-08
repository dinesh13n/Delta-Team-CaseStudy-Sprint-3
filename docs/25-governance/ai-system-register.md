# AI system register

| Field | Value |
|---|---|
| Stage | K |
| Runbook step | K4 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (entry complete) / CONDITIONAL (registration authority unknown) |
| Evidence sources | docs/19-intelligence/prompt-registry.md |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

| Field | Value |
|---|---|
| Register ID | AIS-001 |
| Name | Exception summary assistant |
| Purpose | summarise a shipment exception for a dispatcher and suggest a next review step |
| Users | dispatchers (request and decide); other personas cannot decide |
| Decision type | decision support, suggest-only; no autonomous action |
| Provider | `deterministic` 1.0 (default); real model not configured |
| Prompt | `exception_summary` v1, sha256 `96b454af407d1b72d729d86b7727fb43cf053bf6fa6076fd4c4d72af4cc35155` |
| Configuration hash | `b397c28d74371723ecf697c92ce1c6e896d0f424c5893d13865213bf91e0d5a8` (deterministic provider) |
| Data used | allow-listed shipment, event and booking fields; never customer id, driver id, location |
| Risk class | [UNK] formal class (CO-07); working view: low, because it informs a person about shipment status |
| Oversight | human approval record per suggestion (K1) |
| Evaluation | TEVV 192 cases, all thresholds met |
| Known limits | no real model tested; `[unrecognised]` on real enum vocabulary; no independent review |
| Owner | AI governance owner [UNK] |
| Registration with any authority | [UNK] none required or done |
| Review date | on any change of prompt, model or data scope; otherwise 90 days after go-live |
