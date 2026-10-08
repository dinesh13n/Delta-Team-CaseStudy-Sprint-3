# AI, retrieval and agent handover

| Field | Value |
|---|---|
| Stage | P |
| Runbook step | P2 (runbook/02-TRANSFORMATION-RUNBOOK.md) |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent (claude-sonnet-5-5), operator Dinesh |
| Status | PASS (AI) / NOT APPLICABLE (RAG, agents) |
| Evidence sources | See body |
| Assumptions | See body |
| Unresolved issues | None beyond those listed in body |
| Residual risks | See body |

Classification: **[VF]** Verified Fact, **[INF]** Inference, **[ASM]** Assumption, **[UNK]** Unknown.

AI: one prompt (`exception_summary_v1`, locked), one provider (deterministic), a model slot that fails closed. Evaluation: 192 cases in four sets, thresholds declared before the first run (`evaluation/thresholds.json`), `python -m evaluation.run_eval`. Red team: `scripts/red_team.py`, 12 attacks. Playbook: ai-incident-playbook.md.
Retrieval: none exists. Agents: none (L0). To add a model: implement the provider interface, add to `models.lock.json`, run evaluation and red team, update the model card.
