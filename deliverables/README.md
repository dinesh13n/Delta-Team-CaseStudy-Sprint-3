# Deliverables: CTO pack

| Field | Value |
|---|---|
| Purpose | Everything the CTO needs to understand the engagement and to present it, in one folder |
| Version | v1.0 |
| Date | 2026-10-08 |
| Author / Agent | Claude Code agent, operator Dinesh |
| Status | Final draft for CTO review |

## Read in this order

| # | File | What it is | Open with |
|---|---|---|---|
| 1 | `01-CTO-Briefing.docx` (and `.md`) | The whole story in about ten pages, with all six diagrams | Word, or any Markdown viewer |
| 2 | `02-CTO-Presentation.pptx` | 19 slides: an 11-slide main talk (10 minutes) and an 8-slide appendix for questions. Speaker notes on every slide. Diagrams are native, editable PowerPoint shapes | PowerPoint, Keynote, Google Slides |
| 3 | `03-Evidence-Register.xlsx` | The central evidence workbook: dashboard plus 12 detail sheets (all 146 evidence files with links and SHA-256, 62 findings, Repo 1.0 vs 2.0, red team, KPIs, rubric, gates, decisions, risks, journey, semantic layer) | Excel, LibreOffice |
| 4 | `diagrams/` | Six diagrams, each as `.drawio` (editable), `.svg` and `.png`; `all-diagrams.drawio` holds all six as pages | diagrams.net, draw.io desktop, or the VS Code Draw.io Integration extension |

## The diagrams

| File | Shows |
|---|---|
| `01-journey-start-to-goal` | From the delivered repository to the readiness decision: six phases, 20 stages, the evidence rules, the commits |
| `02-architecture-repo-1.0` | The repository as delivered: three generations, no control point, defects marked |
| `03-architecture-repo-2.0` | The repository as built: one control point, AI gateway, ports, what is not built |
| `04-ai-request-path-v1-vs-v2` | One AI summary request, before and after |
| `05-evidence-chain` | How a claim traces to a hashed file, with a worked example (F-17) |
| `06-semantic-layer` | The semantic layer by format, and what uses it |

## Rebuilding the pack

Everything is generated from the repository by the scripts in `_build/`, so the numbers can be refreshed after any change. Run these from the repository root:

```
python deliverables/_build/build_diagrams.py                         # .drawio, .svg, diagrams.json
NODE_PATH=$(npm root -g) node deliverables/_build/render_png.js       # .png
python deliverables/_build/build_workbook.py                          # 03-Evidence-Register.xlsx
NODE_PATH=$(npm root -g) node deliverables/_build/build_deck.js       # 02-CTO-Presentation.pptx
pandoc deliverables/01-CTO-Briefing.md -o deliverables/01-CTO-Briefing.docx --resource-path=deliverables
```

Edit diagram content in `_build/diagram_specs.py`, so the draw.io files, images and slides stay identical. Alternatively, edit the `.drawio` or the slide directly and accept that the copies will differ.

## What this pack does not claim

- No real AI model was called.
- Nothing is deployed.
- No business KPI moved.
- No independent review was done.

These limits are on slide 10 of the deck and in section 10 of the briefing.
