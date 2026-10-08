// Build deliverables/02-CTO-Presentation.pptx. Diagrams are drawn as native PowerPoint shapes from
// _build/diagrams.json (same source as the draw.io files), so every box and arrow is editable.
// Usage (repository root): NODE_PATH=$(npm root -g) node deliverables/_build/build_deck.js
const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");
const { applyTheme } = require("/mnt/skills/public/pptx/scripts/apply_theme.js");

const OUT = path.join(__dirname, "..", "02-CTO-Presentation.pptx");
const DIAG = JSON.parse(fs.readFileSync(path.join(__dirname, "diagrams.json"), "utf8"));
const D = Object.fromEntries(DIAG.map((d) => [d.name, d]));

const THEME = {
  name: "Delta Logistics",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1B2A2F", lt1: "FFFFFF", dk2: "0B3C49", lt2: "E8F1F2",
    accent1: "1F7A8C", accent2: "F2A541", accent3: "C0392B", accent4: "2E8B57",
    accent5: "5F6E71", accent6: "9AA5A8", hlink: "1F5FA8", folHlink: "6B4FA0",
  },
};
const HEX = { petrol: "0B3C49", teal: "1F7A8C", amber: "F2A541", red: "C0392B", green: "2E8B57", light: "E8F1F2", grey: "5F6E71", ink: "1B2A2F" };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5 in
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "Brownfield to Repo 2.0: CTO briefing";
pres.author = "Delta-Team (operator Dinesh, with Claude)";
pres.company = "Delta-Team";
const C = pres.SchemeColor;

// ---------- layouts
pres.defineSlideMaster({
  title: "TITLE_DARK",
  background: { color: HEX.petrol },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.8, y: 2.1, w: 11.7, h: 1.5, fontSize: 44, bold: true, color: C.background1, valign: "bottom", align: "left", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.8, y: 3.8, w: 11.7, h: 1.6, fontSize: 20, color: C.background2, valign: "top", align: "left", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTENT",
  background: { color: "FFFFFF" },
  margin: [0.5, 0.5, 0.6, 0.5],
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.3, w: 12.33, h: 0.7, fontSize: 28, bold: true, color: C.text2, valign: "middle", align: "left", margin: 0 }, text: "" } },
    { text: { text: "Delta-Team  ·  Brownfield to Repo 2.0  ·  CTO briefing", options: { x: 0.5, y: 7.05, w: 8, h: 0.3, fontSize: 10, color: HEX.grey, margin: 0 } } },
  ],
  slideNumber: { x: 12.3, y: 7.05, w: 0.6, h: 0.3, fontSize: 10, color: HEX.grey, align: "right" },
});
pres.defineSlideMaster({
  title: "DIAGRAM",
  background: { color: "FFFFFF" },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.25, w: 11.6, h: 0.65, fontSize: 26, bold: true, color: C.text2, valign: "middle", align: "left", margin: 0 }, text: "" } },
  ],
  slideNumber: { x: 12.3, y: 0.4, w: 0.6, h: 0.3, fontSize: 10, color: HEX.grey, align: "right" },
});

let n = 0;
function slide(master, section, title, notes) {
  const s = pres.addSlide({ masterName: master, sectionTitle: section });
  s.addText(title, { placeholder: "title" });
  if (notes) s.addNotes(notes);
  n += 1;
  return s;
}

// ---------- native diagram renderer
function drawDiagram(s, name, box = { x: 0.25, y: 1.0, w: 12.83, h: 6.35 }) {
  const d = D[name];
  const sx = box.w / d.W, sy = box.h / d.H;
  const pt = (fs) => Math.round(fs * sy * 72 * 1.15 * 10) / 10;
  for (const nd of d.nodes) {
    const [fill, stroke, col, dashed, boldFirst] = d.styles[nd.kind];
    const x = box.x + nd.x * sx, y = box.y + nd.y * sy, w = nd.w * sx, h = nd.h * sy;
    const lane = nd.kind === "lane";
    const runs = nd.lines.map((t, i) => ({
      text: t,
      options: { bold: lane || (boldFirst && i === 0), breakLine: i < nd.lines.length - 1 },
    }));
    s.addText(runs, {
      shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: lane ? 0.03 : 0.06,
      x, y, w, h, isTextBox: true,
      fill: { color: fill },
      line: nd.kind === "note" ? { type: "none" } : { color: stroke, width: lane ? 0.75 : 1.25, dashType: dashed ? "dash" : "solid" },
      color: col, fontSize: pt(nd.fs), fontFace: "Calibri",
      align: lane ? "left" : nd.align, valign: lane ? "top" : "middle",
      margin: lane ? [4, 6, 2, 6] : [2, 4, 2, 4], paraSpaceAfter: 0,
      objectName: `${name}:${nd.id}`,
    });
  }
  for (const e of d.edges) {
    const x1 = box.x + e.x1 * sx, y1 = box.y + e.y1 * sy, x2 = box.x + e.x2 * sx, y2 = box.y + e.y2 * sy;
    s.addShape(pres.shapes.LINE, {
      x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.max(Math.abs(x2 - x1), 0.001), h: Math.max(Math.abs(y2 - y1), 0.001),
      flipH: x2 < x1, flipV: y2 < y1,
      line: { color: "41545A", width: 1.5, endArrowType: "triangle", dashType: e.dashed ? "dash" : "solid" },
      objectName: `${name}:edge:${e.from}->${e.to}`,
    });
  }
}

function stat(s, x, y, w, big, label, color) {
  s.addText(big, { x, y, w, h: 0.95, fontSize: 40, bold: true, color, margin: 0, isTextBox: true, fit: "none" });
  s.addText(label, { x, y: y + 0.95, w, h: 0.75, fontSize: 14, color: HEX.ink, margin: 0, valign: "top", isTextBox: true });
}

function card(s, x, y, w, h, head, body, fill = HEX.light, headColor = HEX.petrol) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: fill }, line: { type: "none" } });
  s.addText(
    [{ text: head, options: { bold: true, fontSize: 17, color: headColor, breakLine: true } },
     { text: body, options: { fontSize: 15, color: HEX.ink } }],
    { x: x + 0.15, y: y + 0.1, w: w - 0.3, h: h - 0.2, valign: "top", margin: 0, isTextBox: true, paraSpaceAfter: 4 });
}

function table(s, rows, opts) {
  s.addTable(rows, Object.assign({ fontFace: "Calibri", fontSize: 12, color: HEX.ink, border: { type: "solid", pt: 0.5, color: "C5D6DA" }, valign: "middle", margin: [3, 5, 3, 5] }, opts));
}
const H = (t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: HEX.petrol } } });
const chip = (t) => {
  const f = /^(Fixed|PASS|MET)/.test(t) ? "E5F3EB" : /^(Partial|Changed|PARTIAL)/.test(t) ? "FFF4E0" : "FCEBEA";
  return { text: t, options: { fill: { color: f }, bold: true } };
};

// =========================== MAIN TALK
const S1 = "Main talk (10 minutes)";
pres.addSection({ title: S1 });
{
  const s = pres.addSlide({ masterName: "TITLE_DARK", sectionTitle: S1 });
  s.addText("Brownfield to Repo 2.0", { placeholder: "title" });
  s.addText([
    { text: "Logistics shipment, fleet, routing and exception operations", options: { breakLine: true } },
    { text: "What we found, what we changed, how we proved it, and what we need from you", options: { breakLine: true } },
    { text: "Delta-Team  ·  AI-FDE Sprint 3  ·  8 October 2026", options: { fontSize: 16 } },
  ], { placeholder: "body" });
  s.addNotes("Open with the purpose: a readiness decision on a transformed logistics operations repository, with the evidence behind it. Ten minutes of talk, five of questions. Everything shown is in the deliverables folder, and every number traces to a hashed file in the repository.");
  n += 1;
}
{
  const s = slide("CONTENT", S1, "The answer: controls are proven; value and independence are not yet",
    "Lead with the verdict. Three numbers carry it: the red team result, the engineering health, and the evidence discipline. Then the decision itself: no production on real data; a controlled pilot on synthetic data is supportable. Say plainly what is not proven before anyone asks: no real model, no deployment, no business benefit measured, no independent reviewer.");
  stat(s, 0.6, 1.35, 3.9, "10 → 0", "of the same 12 attacks succeed, against Repo 1.0 and then Repo 2.0", HEX.red);
  stat(s, 4.75, 1.35, 3.9, "3 → 181", "tests passing; coverage 45% → 97% on application and ETL code", HEX.teal);
  stat(s, 8.9, 1.35, 3.9, "146", "evidence files, each SHA-256 hashed; 203 of 203 document citations verified", HEX.petrol);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 3.65, w: 5.95, h: 1.45, rectRadius: 0.08, fill: { color: "FCEBEA" }, line: { type: "none" } });
  s.addText([{ text: "NO-GO", options: { bold: true, fontSize: 24, color: HEX.red, breakLine: true } },
             { text: "Production on real data: 5 of 12 readiness gates fail, and they need people and a platform, not more code", options: { fontSize: 14, color: HEX.ink } }],
            { x: 0.8, y: 3.75, w: 5.6, h: 1.25, margin: 0, valign: "top", isTextBox: true });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 6.85, y: 3.65, w: 5.95, h: 1.45, rectRadius: 0.08, fill: { color: "E5F3EB" }, line: { type: "none" } });
  s.addText([{ text: "CONDITIONAL GO", options: { bold: true, fontSize: 24, color: HEX.green, breakLine: true } },
             { text: "Controlled pilot on synthetic data, local or test environment: G1 to G6 pass, G7 partial, and five conditions apply (slide 9)", options: { fontSize: 14, color: HEX.ink } }],
            { x: 7.05, y: 3.75, w: 5.6, h: 1.25, margin: 0, valign: "top", isTextBox: true });
  s.addText([{ text: "Not proven: ", options: { bold: true, color: HEX.red } },
             { text: "no real AI model was ever called; nothing is deployed; no business KPI moved; one operator and one agent built, tested and graded the work." }],
            { x: 0.6, y: 5.45, w: 12.2, h: 0.8, fontSize: 15, color: HEX.ink, margin: 0, isTextBox: true, valign: "top" });
}
{
  const s = slide("DIAGRAM", S1, "The journey: 20 stages, six phases, one evidence discipline",
    "Walk left to right. Start: the repository as delivered. Six phases: understand, define, build, prove, defend, close out. Each phase box shows its stages and the main result. Underneath: the rules applied in every stage (headers, hashes, citations, tags, exit gates) and the commits that recorded them. End: a defended decision, not a claim of production readiness.");
  drawDiagram(s, "01-journey-start-to-goal");
}
{
  const s = slide("DIAGRAM", S1, "What we inherited: three generations side by side, no control point",
    "Repo 1.0 had legacy batch scripts, a partly modernised API and an AI gateway living next to each other. The API took the caller's role from a header it never checked; the AI endpoint had no authorisation and reported its own guardrail as not enforced; a lookup that missed returned a different record. Policy, Terraform and CI files existed but did nothing. About 140 lines of application code and 3 tests.");
  drawDiagram(s, "02-architecture-repo-1.0");
}
{
  const s = slide("CONTENT", S1, "62 findings, five root causes",
    "We froze the old behaviour with characterisation tests first, then catalogued 62 findings. 25 are severity S1. 43 are fixed, 4 fixed in the tree (the credentials stay in history), 10 partial, 2 changed by decision, 2 deferred, 1 proposed for acceptance. The five root causes explain why the defects existed; four are confirmed with high confidence, one needs an owner interview.");
  s.addChart(pres.charts.BAR, [{ name: "Findings", labels: ["Fixed", "Fixed in tree", "Partial", "Changed", "Deferred", "Proposed accept"], values: [43, 4, 10, 2, 2, 1] }], {
    x: 0.5, y: 1.2, w: 6.2, h: 5.0, barDir: "bar",
    chartColors: [HEX.teal], showValue: true, dataLabelPosition: "outEnd", dataLabelColor: HEX.ink, dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt",
    catAxisLabelColor: HEX.ink, catAxisLabelFontSize: 12, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true,
    valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false,
    showTitle: true, title: "Final disposition of the 62 findings (25 are severity S1)", titleFontSize: 14, titleColor: HEX.petrol, titleFontFace: "+mn-lt",
  });
  const rc = [
    ["RC-1 No governance by design", "ADR-0001 kept legacy beside the API and was never revisited (plausible; owner not interviewed)"],
    ["RC-2 Identity not modelled", "role from a header; lookup by any column"],
    ["RC-3 No data contracts", "defects in all six datasets, counted and discarded"],
    ["RC-4 AI unguarded by design", "no auth, no schema, guardrail not enforced"],
    ["RC-5 No evidence by-product", "CI ran nothing useful; quick-start failed"],
  ];
  rc.forEach(([h, b], i) => card(s, 7.0, 1.2 + i * 1.02, 5.85, 0.92, h, b));
}
{
  const s = slide("DIAGRAM", S1, "Repo 2.0: one control point, ports, and AI behind a gateway",
    "Repo 2.0 is a modular monolith with ports, chosen over hardening the old monolith or splitting into services; the whole system is too small for network boundaries to pay. Every request passes the token check and the policy engine, which reads its rules from the semantic layer. The AI gateway only suggests, only sees allow-listed fields, and refuses rather than returning an invalid answer. Grey boxes are not built because they need owner decisions.");
  drawDiagram(s, "03-architecture-repo-2.0");
}
{
  const s = slide("CONTENT", S1, "Repo 1.0 vs Repo 2.0 at a glance",
    "The full 20-row comparison, with findings and evidence for each row, is the 'Repo 1.0 vs 2.0' sheet of the evidence register. Read the status column honestly: identity is fixed with an interim scheme; audit is tamper-evident but still a local file; infrastructure is deferred by decision.");
  const rows = [
    [H("Area"), H("Repo 1.0 (as delivered)"), H("Repo 2.0 (as built)"), H("Status")],
    ["Quick-start and tests", "Test command fails; 3 tests; 45% coverage", "Works; 181 tests; 97% coverage; CI green on 3.11 and 3.14", chip("Fixed")],
    ["Identity", "Role taken from a request header", "Signed token; forged tokens rejected; no identity provider yet", chip("Fixed (interim)")],
    ["Authorisation", "Flat allow-list; policy file unused", "Deny by default; persona, entity, purpose; policy generated and tested; scope not narrowed", chip("Fixed (scope partial)")],
    ["Record lookup", "Any column; wrong record on a miss", "Key pattern enforced; 404 on a miss; collisions quarantined", chip("Fixed")],
    ["AI endpoint", "No auth; guardrail off; no schema", "Authorised, rate-limited, allow-listed context, checked output, suggest-only", chip("Fixed (no model)")],
    ["Human approval", "None", "Approve or reject once; self-approval still possible", chip("Fixed (no four-eyes)")],
    ["Audit", "Time and action only", "Hash-chained: who, purpose, decision; tampering detected; local file", chip("Partial")],
    ["Data quality", "Defects counted, then discarded", "Validated, quarantined, curated layer; raw fixture untouched", chip("Fixed")],
    ["Infrastructure", "Terraform writes one local file", "Container recipe; nothing provisioned; platform-neutral by decision", chip("Deferred")],
  ];
  table(s, rows, { x: 0.5, y: 1.15, w: 12.33, colW: [2.1, 3.4, 5.13, 1.7], fontSize: 12, rowH: 0.5 });
}
{
  const s = slide("CONTENT", S1, "Proof: the same 12 attacks, before and after",
    "Same twelve attacks, same requests, run against the delivered code and against Repo 2.0. Ten succeeded before; none succeed now. Two did not succeed even before (RT-08 and RT-10), and we report them as such. Caveat: our own red team, not an independent one.");
  s.addText("10 of 12", { x: 0.6, y: 1.4, w: 3.6, h: 0.9, fontSize: 44, bold: true, color: HEX.red, margin: 0, isTextBox: true });
  s.addText("succeeded against Repo 1.0", { x: 0.6, y: 2.3, w: 3.6, h: 0.5, fontSize: 15, color: HEX.ink, margin: 0, isTextBox: true });
  s.addText("0 of 12", { x: 0.6, y: 3.2, w: 3.6, h: 0.9, fontSize: 44, bold: true, color: HEX.green, margin: 0, isTextBox: true });
  s.addText("succeed against Repo 2.0", { x: 0.6, y: 4.1, w: 3.6, h: 0.5, fontSize: 15, color: HEX.ink, margin: 0, isTextBox: true });
  s.addText("Run by the builder, not an independent team. Source: evidence/26-tevv/EVD-L-03-redteam-*.json", { x: 0.6, y: 5.0, w: 3.6, h: 1.0, fontSize: 11, color: HEX.grey, margin: 0, isTextBox: true, valign: "top" });
  const rt = [["RT-01", "Call the AI endpoint with no identity", 200, 1, 401], ["RT-02", "Claim admin with a header", 200, 1, 401], ["RT-03", "Use a persona from another domain", 200, 1, 401],
    ["RT-04", "Look up a record by a non-key column", 200, 1, 422], ["RT-05", "Ask for a record that does not exist", 200, 1, 422], ["RT-06", "Reach the planted colliding key", 200, 1, 422],
    ["RT-07", "Reflect attacker text through the AI", 200, 1, 422], ["RT-08", "Smuggle text via a category field", 200, 0, 200], ["RT-09", "Find the guardrail switched off", 200, 1, 200],
    ["RT-10", "Action a suggestion without approval", 404, 0, 401], ["RT-11", "Forge a token (alg none, admin)", 200, 1, 401], ["RT-12", "Exhaust the AI endpoint", 200, 1, 429]];
  const res = (ok) => ({ text: ok ? "succeeded" : "failed", options: { fill: { color: ok ? "FCEBEA" : "E5F3EB" }, bold: true } });
  const rows = [[H("Attack"), H("Goal"), H("Repo 1.0"), H("Result"), H("Repo 2.0"), H("Result")]].concat(
    rt.map(([id, g, s1, ok, s2]) => [id, g, String(s1), res(ok), String(s2), res(false)]));
  table(s, rows, { x: 4.5, y: 1.15, w: 8.33, colW: [0.8, 3.53, 0.95, 1.1, 0.95, 1.0], fontSize: 11, rowH: 0.39 });
}
{
  const s = slide("CONTENT", S1, "Readiness: six gates pass; production gates need people and a platform",
    "Gates were fixed before the decision. G1 to G6 pass at repository level, G7 is partial. G8 to G12 fail, and none of them can be closed by more engineering from us: they need named owners, a platform and identity provider, an independent reviewer and a compliance call. The pilot also carries five conditions: a sponsor accepts the operator in every role; credentials resolved; branch protection on (needs a paid GitHub plan for a private repository); no real data or hosted model; one independent reviewer reads the pack.");
  const g = [["G1", "Tests and coverage", "PASS"], ["G2", "Evaluation (deterministic provider only)", "PASS"], ["G3", "No original defect re-exploitable", "PASS"],
    ["G4", "No critical or high dependency vulnerability", "PASS"], ["G5", "Audit tamper-evident, reconstruction shown", "PASS"], ["G6", "Backup restore shown", "PASS"],
    ["G7", "Rollback defined and rehearsed", "PARTIAL"], ["G8", "Alerts routed to named people", "FAIL"], ["G9", "Named approver and risk owners", "FAIL"],
    ["G10", "Platform and identity provider exist", "FAIL"], ["G11", "Independent evidence review", "FAIL"], ["G12", "Compliance resolved for real data", "FAIL"]];
  g.forEach(([id, t, st], i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.5 + col * 4.15, y = 1.2 + row * 1.35;
    const fill = st === "PASS" ? "E5F3EB" : st === "PARTIAL" ? "FFF4E0" : "FCEBEA";
    const fc = st === "PASS" ? HEX.green : st === "PARTIAL" ? "B9770E" : HEX.red;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 3.95, h: 1.18, rectRadius: 0.08, fill: { color: fill }, line: { type: "none" } });
    s.addText([{ text: `${id}  ${st}`, options: { bold: true, fontSize: 16, color: fc, breakLine: true } }, { text: t, options: { fontSize: 15, color: HEX.ink } }],
      { x: x + 0.15, y: y + 0.08, w: 3.65, h: 1.02, margin: 0, valign: "top", isTextBox: true });
  });
  s.addText("Pilot needs G1 to G7 plus five conditions (sponsor, credentials, branch protection, no real data, one reviewer). Production needs all twelve.", { x: 0.5, y: 6.65, w: 12.3, h: 0.35, fontSize: 13, italic: true, color: HEX.grey, margin: 0, isTextBox: true });
}
{
  const s = slide("CONTENT", S1, "What is not proven, stated before anyone asks",
    "These are the limits of the evidence. Each one is also recorded in the residual-risk register with an owner role. None is hidden in a footnote; they are the reason the verdict is a pilot, not production.");
  const items = [
    ["No real AI model", "All AI evidence uses the deterministic provider. No model by decision (OQ-02); thresholds are valid only for that provider."],
    ["Nothing deployed", "Platform-neutral by decision (OQ-01). Terraform provisions nothing; the container image was never built."],
    ["No business value measured", "K1 to K8 come from a static synthetic fixture, so they cannot move. No monetary benefit is verified."],
    ["No independent review", "One operator and one agent built, tested and graded everything. Red team and gates are self-run."],
    ["Portability partly shown", "A second model rebuilt a subset once: safety held (5 of 5), AI-output fidelity did not (0 of 2). Gaps now specified, not re-tested."],
    ["Secrets in history", "Removed from the tree; history kept; repository private; values treated as compromised (OQ-19)."],
  ];
  items.forEach(([h, b], i) => card(s, 0.5 + (i % 2) * 6.2, 1.2 + Math.floor(i / 2) * 1.85, 5.95, 1.65, h, b, i < 4 ? "FCEBEA" : "FFF4E0", HEX.red));
}
{
  const s = slide("CONTENT", S1, "Six asks of the CTO",
    "The operator has decided all 23 open questions, but one person holds every role. What only the CTO or sponsor can add is independence. These six asks, in order of value, are what moves the readiness gates. The signature block is in docs/44-decisions/cto-signoff-pack.md.");
  const asks = [
    ["1  Ratify the write authorisation", "Given by the operator to themselves (OQ-11). Minutes."],
    ["2  Name approvers; sign or reject 12 risk acceptances", "0 of 12 signed; the only NOT MET rubric row (OQ-05). About an hour."],
    ["3  Confirm platform, model and egress decisions", "Decide whether IaC and a working AI model can ever be met (OQ-01 to 03). A conversation."],
    ["4  Name a regulatory regime, or confirm none", "Validates the candidate obligations (OQ-04, OQ-21). A day of review."],
    ["5  Confirm proxy KPIs; say if real figures exist", "The sponsor owns the value argument (OQ-08, OQ-09). Minutes."],
    ["6  Appoint one independent reviewer", "Every gate and grade was self-run (GOV-10). A few hours."],
  ];
  asks.forEach(([h, b], i) => card(s, 0.5 + (i % 2) * 6.2, 1.2 + Math.floor(i / 2) * 1.85, 5.95, 1.65, h, b, HEX.light, HEX.petrol));
}

// =========================== APPENDIX
const S2 = "Appendix (detail for questions)";
pres.addSection({ title: S2 });
{
  const s = pres.addSlide({ masterName: "TITLE_DARK", sectionTitle: S2 });
  s.addText("Appendix", { placeholder: "title" });
  s.addText("Detail for questions: the AI request path, engineering health and KPIs, the semantic layer, the second-model test, the evidence chain, rubric coverage, and where everything lives.", { placeholder: "body" });
  s.addNotes("Use these slides only if asked.");
  n += 1;
}
{
  const s = slide("DIAGRAM", S2, "One AI summary request, before and after",
    "Top row: what happened in Repo 1.0. Below: the same request in Repo 2.0. Each check fails closed with its own status code; the model step only sees allowed fields; the answer is checked, falls back, or abstains; the suggestion waits for a person; everything is audited in a hash chain.");
  drawDiagram(s, "04-ai-request-path-v1-vs-v2");
}
{
  const s = slide("CONTENT", S2, "Engineering health moved; business KPIs did not, by design",
    "K9 and K10 measure engineering health and improved because tests were written. K1 to K8 are computed from a static synthetic fixture the intervention does not touch, so equal before and after is the expected and honest result. No business benefit is claimed.");
  s.addChart(pres.charts.BAR, [{ name: "Repo 1.0", labels: ["Tests passing", "Coverage %"], values: [3, 45] }, { name: "Repo 2.0", labels: ["Tests passing", "Coverage %"], values: [181, 97] }], {
    x: 0.5, y: 1.2, w: 6.0, h: 5.2, barDir: "col", barGrouping: "clustered",
    chartColors: [HEX.red, HEX.teal], showValue: true, dataLabelPosition: "outEnd", dataLabelColor: HEX.ink, dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt",
    catAxisLabelColor: HEX.ink, catAxisLabelFontSize: 13, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
    showLegend: true, legendPos: "b", legendFontSize: 12, legendFontFace: "+mn-lt", legendColor: HEX.ink,
    showTitle: true, title: "K9 tests and K10 coverage (apps and etl)", titleFontSize: 14, titleColor: HEX.petrol, titleFontFace: "+mn-lt",
  });
  const rows = [[H("KPI"), H("Baseline"), H("After"), H("Why")],
    ["K1 latency p50 (ms)", "1667", "1667", "fixture column"], ["K2 cost per event", "2.2451", "2.2451", "static"], ["K3 severe-event share", "39.6%", "39.6%", "static"],
    ["K4 correlation completeness", "33.6%", "33.6%", "producer unchanged"], ["K6 retries max", "4995", "4995", "static"], ["K7 duplicate keys (raw)", "18", "18", "quarantined downstream"]];
  table(s, rows, { x: 6.9, y: 1.3, w: 5.93, colW: [2.33, 1.0, 1.0, 1.6], fontSize: 12, rowH: 0.45 });
  s.addText("K5 and K8 are also equal; the full table is the KPIs sheet of the evidence register.", { x: 6.9, y: 4.75, w: 5.93, h: 0.6, fontSize: 12, color: HEX.grey, margin: 0, isTextBox: true });
}
{
  const s = slide("DIAGRAM", S2, "Semantic layer v2.0: knowledge owned outside the code and the model",
    "The semantic layer holds the business meaning in portable files: Markdown for people, YAML for definitions, JSON Schema for validation, JSON for exchange, tests for integrity. The application reads it at run time for access, data rules and AI rules. Version 2.0 was aligned to the capstone requirement after the transformation, as the brief asks.");
  drawDiagram(s, "06-semantic-layer");
}
{
  const s = slide("CONTENT", S2, "Second-model test: safety held on this harness; AI-output fidelity did not",
    "A smaller model of the same vendor rebuilt a four-behaviour subset from the layer plus the PRD, specifications and a brief, in one blind attempt. On the safety behaviours this harness measures, the builds matched; but the 0 of 12 is partly vacuous, because three AI-path attacks reached the AI only in a post-hoc re-run with an ai_agent token, and Model B left scope and tenant filtering unenforced. They differ where the specification was silent; those eight gaps are now written into the layer but not re-tested. One run, same vendor family, harness written around the first build.");
  const rows = [[H("Dimension"), H("Model A (built the system)"), H("Model B (blind rebuild)")],
    ["Scope", "Full system", "Four-behaviour subset"],
    ["Evaluation cases passing every strict check", "192 of 192", { text: "8 of 192", options: { fill: { color: "FCEBEA" }, bold: true } }],
    ["Safety gates (schema, claims, leaks, injection, approval)", chip("PASS 5 of 5"), chip("PASS 5 of 5")],
    ["Fidelity gates (abstention, recommendation class)", chip("PASS 2 of 2"), { text: "0 of 2 (0.875; 0.1667 vs 1.0)", options: { fill: { color: "FCEBEA" }, bold: true } }],
    ["Black-box API checks", "24 of 24", "21 of 24 (24 with an ai_agent token, post hoc)"],
    ["Original attacks that succeed", "0 of 12", "0 of 12 (3 AI-path attacks reached the AI only in a post-hoc re-run)"],
    ["Audit chain valid; tampering detected", "yes", "yes"]];
  table(s, rows, { x: 0.5, y: 1.2, w: 12.33, colW: [4.6, 3.6, 4.13], fontSize: 13, rowH: 0.5 });
  s.addText("Source: docs/40-scale/model-comparison.md; evidence/40-scale/EVD-Q-06-comparison.csv. Models: claude-sonnet-5-5 (A) and claude-haiku-5-5 (B).", { x: 0.5, y: 5.9, w: 12.3, h: 0.5, fontSize: 12, color: HEX.grey, margin: 0, isTextBox: true });
}
{
  const s = slide("DIAGRAM", S2, "How any claim traces to proof",
    "Any number in this deck can be followed to a file: the document cites the path and its hash, the folder manifest records how and when it was produced, and the index ties it to findings and rubric criteria. Three scripts re-check all of it from the repository.");
  drawDiagram(s, "05-evidence-chain");
}
{
  const s = slide("CONTENT", S2, "Rubric evidence coverage by criterion",
    "Counts of sub-dimensions by status, from the rubric coverage matrix. This measures how complete the evidence is, not how many marks an evaluator will give. In our judgement, R3 and R4 are held back by missing people and a missing model, not by missing work.");
  const lab = ["R1 As-Is (20)", "R2 Repo 2.0 (25)", "R3 Governance (20)", "R4 PRD and app (25)", "R5 Defence (10)"];
  s.addChart(pres.charts.BAR, [
    { name: "MET", labels: lab, values: [6, 5, 5, 4, 4] }, { name: "PARTIAL", labels: lab, values: [1, 4, 2, 1, 1] },
    { name: "NOT MET", labels: lab, values: [0, 0, 1, 0, 0] }, { name: "BLOCKED", labels: lab, values: [0, 0, 1, 1, 0] }], {
    x: 0.5, y: 1.2, w: 8.0, h: 5.3, barDir: "bar", barGrouping: "stacked",
    chartColors: [HEX.green, HEX.amber, HEX.red, "7B241C"], showValue: true, dataLabelPosition: "ctr", dataLabelFormatCode: "0;;;", dataLabelColor: "FFFFFF", dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt",
    catAxisLabelColor: HEX.ink, catAxisLabelFontSize: 12, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
    showLegend: true, legendPos: "b", legendFontSize: 12, legendFontFace: "+mn-lt", legendColor: HEX.ink,
    showTitle: true, title: "36 sub-dimensions by status", titleFontSize: 14, titleColor: HEX.petrol, titleFontFace: "+mn-lt",
  });
  const rows = [[H("Criterion"), H("Coverage index")], ["R1", "0.93"], ["R2", "0.78"], ["R3", "0.67"], ["R4", "0.75"], ["R5", "0.90"]];
  table(s, rows, { x: 8.9, y: 1.4, w: 3.9, colW: [1.9, 2.0], fontSize: 13, rowH: 0.45 });
  s.addText("Index = (MET + half of PARTIAL) ÷ sub-dimensions. Source: docs/43-rubric-traceability/readiness-assessment.md.", { x: 8.9, y: 4.4, w: 3.9, h: 1.0, fontSize: 12, color: HEX.grey, margin: 0, isTextBox: true, valign: "top" });
}
{
  const s = slide("CONTENT", S2, "Where to find everything",
    "Point the audience at the deliverables folder first, then the repository paths for depth. The evidence register is the single index of every hashed file.");
  const rows = [[H("You want"), H("Open")],
    ["The story in writing", "deliverables/01-CTO-Briefing.docx (or .md)"],
    ["Every evidence file, finding, gate, decision and risk", "deliverables/03-Evidence-Register.xlsx"],
    ["Diagrams to edit", "deliverables/diagrams/*.drawio (diagrams.net, draw.io desktop, VS Code); shapes in this deck are native and editable"],
    ["The readiness decision", "docs/42-executive/production-readiness-decision.md"],
    ["The CTO sign-off block", "docs/44-decisions/cto-signoff-pack.md"],
    ["The rubric mapping", "docs/43-rubric-traceability/rubric-coverage-matrix.md"],
    ["The semantic layer", "semantic-layer/ (start with README.md and SEMANTIC-COMPLETENESS.md)"],
    ["The runbooks that drove the work", "runbook/00 to 04 (Markdown and Word)"]];
  table(s, rows, { x: 0.5, y: 1.2, w: 12.33, colW: [4.2, 8.13], fontSize: 13, rowH: 0.52 });
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT, "slides", n);
})();
