// Build deliverables/02-CTO-Presentation-v2.0.pptx (Team Delta, with the semantic-layer rebuild comparison).
// Diagrams are native PowerPoint shapes drawn from _build/diagrams.json (same source as the draw.io files).
// Usage (repository root): NODE_PATH=$(npm root -g) node deliverables/_build/build_deck_v2.js
const pptxgen = require("pptxgenjs");
const path = require("path");
const fs = require("fs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const Fa = require("react-icons/fa");
const { applyTheme } = require("/mnt/skills/public/pptx/scripts/apply_theme.js");

const VERSION = "v2.0";
const DATE = "13 October 2026";
const OUT = path.join(__dirname, "..", `02-CTO-Presentation-${VERSION}.pptx`);
const DIAG = JSON.parse(fs.readFileSync(path.join(__dirname, "diagrams.json"), "utf8"));
const D = Object.fromEntries(DIAG.map((d) => [d.name, d]));
const DECK_TITLE = "From Brownfield to Governed AI";
const DECK_SUB = "Logistics Ops Repo 2.0: an evidence-backed transformation of shipment, fleet, routing and exception operations";
const TEAM = [
  ["Dinesh Naik", "Dinesh.Naik@Birlasoft.Com", true],
  ["Hardik Trivedi", "Hardik.Trivedi@Birlasoft.Com", false],
  ["Nachiket Bordekar", "Nachiket.Bordekar@Birlasoft.Com", false],
  ["Rama Vedula", "Rama.Vedula@Birlasoft.Com", false],
  ["Sudhir Kulkarni", "Sudhir.Kulkarni@Birlasoft.Com", false],
];

const THEME = {
  name: "Team Delta",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1B2A2F", lt1: "FFFFFF", dk2: "0B3C49", lt2: "E8F1F2",
    accent1: "1F7A8C", accent2: "F2A541", accent3: "C0392B", accent4: "2E8B57",
    accent5: "5F6E71", accent6: "9AA5A8", hlink: "1F5FA8", folHlink: "6B4FA0",
  },
};
const HEX = { petrol: "0B3C49", petrol2: "134D5C", teal: "1F7A8C", amber: "F2A541", red: "C0392B", green: "2E8B57", light: "E8F1F2", grey: "5F6E71", ink: "1B2A2F", ice: "CFE3E7" };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5 in
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = `${DECK_TITLE}: CTO briefing ${VERSION}`;
pres.author = "Team Delta (presented by Dinesh Naik)";
pres.company = "Team Delta";
const C = pres.SchemeColor;

// ---------- icons
async function icon(Comp, color, px = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color: "#" + color, size: String(px) }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}
const ICONS = {};

// ---------- layouts
const FOOT = `Team Delta  ·  ${DECK_TITLE}  ·  CTO briefing ${VERSION}`;
pres.defineSlideMaster({ title: "DARK", background: { color: HEX.petrol }, objects: [] });
pres.defineSlideMaster({
  title: "CONTENT",
  background: { color: "FFFFFF" },
  margin: [0.5, 0.5, 0.6, 0.5],
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.42, w: 12.33, h: 0.66, fontSize: 28, bold: true, color: C.text2, valign: "middle", align: "left", margin: 0 }, text: "" } },
    { text: { text: FOOT, options: { x: 0.5, y: 7.05, w: 8, h: 0.3, fontSize: 10, color: HEX.grey, margin: 0 } } },
  ],
  slideNumber: { x: 12.3, y: 7.05, w: 0.6, h: 0.3, fontSize: 10, color: HEX.grey, align: "right" },
});
pres.defineSlideMaster({
  title: "DIAGRAM",
  background: { color: "FFFFFF" },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.36, w: 11.6, h: 0.6, fontSize: 25, bold: true, color: C.text2, valign: "middle", align: "left", margin: 0 }, text: "" } },
  ],
  slideNumber: { x: 12.3, y: 0.15, w: 0.6, h: 0.3, fontSize: 10, color: HEX.grey, align: "right" },
});

let n = 0;
function slide(master, section, kicker, title, notes) {
  const s = pres.addSlide({ masterName: master, sectionTitle: section });
  s.addText(kicker.toUpperCase(), { x: 0.5, y: 0.12, w: 9, h: 0.28, fontSize: 11, bold: true, color: HEX.teal, charSpacing: 2, margin: 0, isTextBox: true });
  s.addText(title, { placeholder: "title" });
  if (notes) s.addNotes(notes);
  n += 1;
  return s;
}

function divider(section, num, title, line, notes) {
  const s = pres.addSlide({ masterName: "DARK", sectionTitle: section });
  s.addShape(pres.shapes.OVAL, { x: 0.8, y: 2.1, w: 2.2, h: 2.2, fill: { color: HEX.amber }, line: { type: "none" } });
  s.addText(num, { x: 0.8, y: 2.1, w: 2.2, h: 2.2, fontSize: 60, bold: true, color: HEX.petrol, align: "center", valign: "middle", margin: 0, isTextBox: true });
  s.addText(title, { x: 3.5, y: 2.2, w: 9.0, h: 1.1, fontSize: 40, bold: true, color: "FFFFFF", margin: 0, valign: "bottom", isTextBox: true });
  s.addText(line, { x: 3.5, y: 3.4, w: 9.0, h: 1.0, fontSize: 20, color: HEX.ice, margin: 0, valign: "top", isTextBox: true });
  s.addShape(pres.shapes.OVAL, { x: 10.6, y: 5.2, w: 3.6, h: 3.6, fill: { color: HEX.petrol2 }, line: { type: "none" } });
  s.addShape(pres.shapes.OVAL, { x: 9.7, y: 6.3, w: 1.6, h: 1.6, fill: { color: HEX.teal, transparency: 40 }, line: { type: "none" } });
  if (notes) s.addNotes(notes);
  n += 1;
  return s;
}

// ---------- native diagram renderer
function drawDiagram(s, name, box = { x: 0.25, y: 1.05, w: 12.83, h: 6.3 }) {
  const d = D[name];
  const sx = box.w / d.W, sy = box.h / d.H;
  const pt = (fs) => Math.round(fs * sy * 72 * 1.15 * 10) / 10;
  for (const nd of d.nodes) {
    const [fill, stroke, col, dashed, boldFirst] = d.styles[nd.kind];
    const x = box.x + nd.x * sx, y = box.y + nd.y * sy, w = nd.w * sx, h = nd.h * sy;
    const lane = nd.kind === "lane";
    const runs = nd.lines.map((t, i) => ({ text: t, options: { bold: lane || (boldFirst && i === 0), breakLine: i < nd.lines.length - 1 } }));
    s.addText(runs, {
      shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: lane ? 0.03 : 0.06, x, y, w, h, isTextBox: true,
      fill: { color: fill },
      line: nd.kind === "note" ? { type: "none" } : { color: stroke, width: lane ? 0.75 : 1.25, dashType: dashed ? "dash" : "solid" },
      color: col, fontSize: pt(nd.fs), fontFace: "Calibri", align: lane ? "left" : nd.align, valign: lane ? "top" : "middle",
      margin: lane ? [4, 6, 2, 6] : [2, 4, 2, 4], paraSpaceAfter: 0, objectName: `${name}:${nd.id}`,
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

function tile(s, x, y, w, h, big, label, color, fill = "FFFFFF") {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.1, fill: { color: fill }, line: { color: "D5E3E6", width: 1 },
    shadow: { type: "outer", color: "9AA5A8", opacity: 0.25, blur: 6, offset: 2, angle: 90 } });
  s.addText(big, { x: x + 0.25, y: y + 0.2, w: w - 0.5, h: 0.95, fontSize: 40, bold: true, color, margin: 0, isTextBox: true, valign: "middle" });
  s.addText(label, { x: x + 0.25, y: y + 1.15, w: w - 0.5, h: h - 1.3, fontSize: 14, color: HEX.ink, margin: 0, valign: "top", isTextBox: true });
}

function card(s, x, y, w, h, head, body, opt = {}) {
  const fill = opt.fill || HEX.light, headColor = opt.headColor || HEX.petrol;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: fill }, line: { type: "none" } });
  let tx = x + 0.2;
  if (opt.icon) {
    s.addShape(pres.shapes.OVAL, { x: x + 0.2, y: y + 0.22, w: 0.62, h: 0.62, fill: { color: opt.iconBg || HEX.petrol }, line: { type: "none" } });
    s.addImage({ data: opt.icon, x: x + 0.34, y: y + 0.36, w: 0.34, h: 0.34 });
    tx = x + 1.0;
  }
  s.addText([{ text: head, options: { bold: true, fontSize: 17, color: headColor, breakLine: true } }, { text: body, options: { fontSize: 14, color: HEX.ink } }],
    { x: tx, y: y + 0.15, w: x + w - tx - 0.2, h: h - 0.3, valign: "top", margin: 0, isTextBox: true, paraSpaceAfter: 4 });
}

function table(s, rows, opts) {
  s.addTable(rows, Object.assign({ fontFace: "Calibri", fontSize: 12, color: HEX.ink, border: { type: "solid", pt: 0.5, color: "C5D6DA" }, valign: "middle", margin: [3, 5, 3, 5] }, opts));
}
const H = (t) => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: HEX.petrol } } });
const chip = (t) => {
  const f = /^(Fixed|PASS|MET|Same|Yes)/.test(t) ? "E5F3EB" : /^(Partial|Changed|PARTIAL)/.test(t) ? "FFF4E0" : "FCEBEA";
  return { text: t, options: { fill: { color: f }, bold: true } };
};

async function build() {
  for (const [k, comp, col] of [["robot", Fa.FaRobot, "FFFFFF"], ["server", Fa.FaServer, "FFFFFF"], ["chart", Fa.FaChartLine, "FFFFFF"], ["eye", Fa.FaUserCheck, "FFFFFF"],
    ["exchange", Fa.FaExchangeAlt, "FFFFFF"], ["key", Fa.FaKey, "FFFFFF"], ["pen", Fa.FaFileSignature, "FFFFFF"], ["users", Fa.FaUsers, "FFFFFF"],
    ["plug", Fa.FaPlug, "FFFFFF"], ["balance", Fa.FaBalanceScale, "FFFFFF"], ["check", Fa.FaClipboardCheck, "FFFFFF"], ["user", Fa.FaUserTie, "FFFFFF"],
    ["filter", Fa.FaFilter, "FFFFFF"], ["code", Fa.FaCode, "FFFFFF"], ["lock", Fa.FaLock, "FFFFFF"], ["db", Fa.FaDatabase, "FFFFFF"],
    ["link", Fa.FaProjectDiagram, "FFFFFF"], ["hash", Fa.FaSlidersH, "FFFFFF"]]) ICONS[k] = await icon(comp, col);

  // =========================== MAIN TALK
  const S1 = "Main talk";
  pres.addSection({ title: S1 });
  {
    const s = pres.addSlide({ masterName: "DARK", sectionTitle: S1 });
    s.addShape(pres.shapes.OVAL, { x: -1.4, y: 5.0, w: 4.2, h: 4.2, fill: { color: HEX.petrol2 }, line: { type: "none" } });
    s.addShape(pres.shapes.OVAL, { x: 2.1, y: 6.55, w: 1.3, h: 1.3, fill: { color: HEX.teal, transparency: 35 }, line: { type: "none" } });
    s.addText("AI-FDE SPRINT 3  ·  CASE STUDY 07  ·  CTO BRIEFING", { x: 0.7, y: 0.75, w: 7.4, h: 0.35, fontSize: 13, bold: true, color: HEX.amber, charSpacing: 2, margin: 0, isTextBox: true });
    s.addText(DECK_TITLE, { x: 0.7, y: 1.3, w: 7.3, h: 1.9, fontSize: 46, bold: true, color: "FFFFFF", margin: 0, valign: "top", isTextBox: true });
    s.addText(DECK_SUB, { x: 0.7, y: 3.3, w: 6.9, h: 1.2, fontSize: 19, color: HEX.ice, margin: 0, valign: "top", isTextBox: true });
    s.addText([{ text: "Presented by Dinesh Naik", options: { bold: true, color: "FFFFFF", breakLine: true } }, { text: `${DATE}  ·  ${VERSION}`, options: { color: HEX.ice } }],
      { x: 0.7, y: 4.75, w: 6.5, h: 0.8, fontSize: 15, margin: 0, valign: "top", isTextBox: true });
    // team panel
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 8.25, y: 0.75, w: 4.55, h: 6.0, rectRadius: 0.12, fill: { color: HEX.petrol2 }, line: { color: HEX.teal, width: 1 } });
    s.addShape(pres.shapes.OVAL, { x: 8.5, y: 1.0, w: 0.62, h: 0.62, fill: { color: HEX.amber }, line: { type: "none" } });
    s.addImage({ data: await icon(Fa.FaUsers, HEX.petrol), x: 8.64, y: 1.14, w: 0.34, h: 0.34 });
    s.addText("Team Delta", { x: 9.25, y: 1.0, w: 3.4, h: 0.62, fontSize: 24, bold: true, color: "FFFFFF", valign: "middle", margin: 0, isTextBox: true });
    TEAM.forEach(([name, mail, presenter], i) => {
      const y = 1.95 + i * 0.93;
      s.addShape(pres.shapes.LINE, { x: 8.5, y: y - 0.08, w: 4.05, h: 0, line: { color: "2C6675", width: 0.75 } });
      s.addText(name, { x: 8.5, y, w: presenter ? 2.55 : 4.05, h: 0.4, fontSize: 17, bold: true, color: "FFFFFF", margin: 0, valign: "middle", isTextBox: true });
      if (presenter) {
        s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 11.1, y: y + 0.05, w: 1.45, h: 0.32, rectRadius: 0.16, fill: { color: HEX.amber }, line: { type: "none" } });
        s.addText("PRESENTER", { x: 11.1, y: y + 0.05, w: 1.45, h: 0.32, fontSize: 10, bold: true, color: HEX.petrol, align: "center", valign: "middle", margin: 0, isTextBox: true });
      }
      s.addText(mail, { x: 8.5, y: y + 0.4, w: 4.05, h: 0.32, fontSize: 12, color: HEX.ice, margin: 0, valign: "top", isTextBox: true, hyperlink: { url: "mailto:" + mail } });
    });
    s.addNotes("Introduce Team Delta: Dinesh Naik (presenting), Hardik Trivedi, Nachiket Bordekar, Rama Vedula and Sudhir Kulkarni. Purpose: a readiness decision on a transformed logistics operations repository, the evidence behind it, and a test of whether the business knowledge survives without the code. Every number traces to a hashed file in the repository.");
    n += 1;
  }
  {
    const s = slide("CONTENT", S1, "Agenda", "Four questions, one evidence trail",
      "Walk the four parts. The first two are the transformation; the third is the portability test the capstone asks for; the fourth is what we need from the CTO.");
    const parts = [["01", "The starting point", "What we inherited and what was wrong with it"], ["02", "What we built and proved", "Repo 2.0, the side-by-side comparison, the red team"],
      ["03", "Can the knowledge travel?", "The semantic layer, and a blind rebuild from it alone"], ["04", "Decision and asks", "Readiness gates, limits, six asks"]];
    parts.forEach(([num, t, d], i) => {
      const x = 0.5 + i * 3.1;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.6, w: 2.9, h: 4.4, rectRadius: 0.12, fill: { color: i === 2 ? "FFF4E0" : HEX.light }, line: { type: "none" } });
      s.addShape(pres.shapes.OVAL, { x: x + 0.3, y: 1.95, w: 1.15, h: 1.15, fill: { color: i === 2 ? HEX.amber : HEX.petrol }, line: { type: "none" } });
      s.addText(num, { x: x + 0.3, y: 1.95, w: 1.15, h: 1.15, fontSize: 30, bold: true, color: i === 2 ? HEX.petrol : "FFFFFF", align: "center", valign: "middle", margin: 0, isTextBox: true });
      s.addText(t, { x: x + 0.3, y: 3.35, w: 2.4, h: 1.0, fontSize: 21, bold: true, color: HEX.petrol, margin: 0, valign: "top", isTextBox: true });
      s.addText(d, { x: x + 0.3, y: 4.4, w: 2.4, h: 1.4, fontSize: 15, color: HEX.ink, margin: 0, valign: "top", isTextBox: true });
    });
    s.addText("New in v2.0: part 03, the rebuild from the semantic layer alone", { x: 0.5, y: 6.3, w: 12.3, h: 0.4, fontSize: 14, italic: true, color: HEX.grey, margin: 0, isTextBox: true });
  }
  {
    const s = slide("CONTENT", S1, "The answer", "Controls are proven; value and independence are not yet",
      "Lead with the verdict. Three numbers carry it: the red team, engineering health, and the evidence discipline. Then the decision: no production on real data; a controlled pilot on synthetic data is supportable, with five conditions. Say plainly what is not proven before anyone asks.");
    tile(s, 0.5, 1.35, 3.95, 2.05, "10 → 0", "of the same 12 attacks succeed, against Repo 1.0 and then Repo 2.0", HEX.red);
    tile(s, 4.69, 1.35, 3.95, 2.05, "3 → 181", "tests passing; coverage 45% → 97% on application and ETL code", HEX.teal);
    tile(s, 8.88, 1.35, 3.95, 2.05, "146", "evidence files, each SHA-256 hashed; 203 of 203 document citations verified", HEX.petrol);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 3.7, w: 6.05, h: 1.55, rectRadius: 0.08, fill: { color: "FCEBEA" }, line: { type: "none" } });
    s.addText([{ text: "NO-GO", options: { bold: true, fontSize: 26, color: HEX.red, breakLine: true } },
      { text: "Production on real data: 5 of 12 readiness gates fail, and they need people and a platform, not more code", options: { fontSize: 14, color: HEX.ink } }],
      { x: 0.75, y: 3.8, w: 5.6, h: 1.35, margin: 0, valign: "top", isTextBox: true });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 6.78, y: 3.7, w: 6.05, h: 1.55, rectRadius: 0.08, fill: { color: "E5F3EB" }, line: { type: "none" } });
    s.addText([{ text: "CONDITIONAL GO", options: { bold: true, fontSize: 26, color: HEX.green, breakLine: true } },
      { text: "Controlled pilot on synthetic data, local or test environment: G1 to G6 pass, G7 partial, five conditions apply", options: { fontSize: 14, color: HEX.ink } }],
      { x: 7.03, y: 3.8, w: 5.6, h: 1.35, margin: 0, valign: "top", isTextBox: true });
    s.addText([{ text: "Not proven: ", options: { bold: true, color: HEX.red } },
      { text: "no real AI model was ever called; nothing is deployed; no business KPI moved; one operator and one agent built, tested and graded the work." }],
      { x: 0.5, y: 5.55, w: 12.3, h: 0.5, fontSize: 15, color: HEX.ink, margin: 0, isTextBox: true, valign: "top" });
    s.addText([{ text: "New: ", options: { bold: true, color: HEX.teal } },
      { text: "a blind rebuild from the semantic layer alone behaved the same on 29 of 30 checks, but could not ingest the original data (part 03)." }],
      { x: 0.5, y: 6.1, w: 12.3, h: 0.5, fontSize: 15, color: HEX.ink, margin: 0, isTextBox: true, valign: "top" });
  }
  {
    const s = slide("DIAGRAM", S1, "The journey", "20 stages, six phases, one evidence discipline",
      "Walk left to right. Start: the repository as delivered. Six phases: understand, define, build, prove, defend, close out. Underneath: the rules applied in every stage and the commits that recorded them. End: a defended decision, not a claim of production readiness.");
    drawDiagram(s, "01-journey-start-to-goal");
  }

  divider(S1, "01", "The starting point", "What we inherited, and why it could not be trusted", "Part one: the repository as delivered.");
  {
    const s = slide("DIAGRAM", S1, "01  The starting point", "What we inherited: three generations side by side, no control point",
      "Repo 1.0 had legacy batch scripts, a partly modernised API and an AI gateway next to each other. The API took the caller's role from a header it never checked; the AI endpoint had no authorisation and reported its own guardrail as not enforced; a lookup that missed returned a different record. Policy, Terraform and CI files existed but did nothing. About 140 lines of application code and 3 tests.");
    drawDiagram(s, "02-architecture-repo-1.0");
  }
  {
    const s = slide("CONTENT", S1, "01  The starting point", "62 findings, five root causes",
      "We froze the old behaviour with characterisation tests first, then catalogued 62 findings, 25 of them severity S1. 43 are fixed, 4 fixed in the tree (credentials stay in history), 10 partial, 2 changed by decision, 2 deferred, 1 proposed for acceptance. Four root causes are confirmed with high confidence; one needs an owner interview.");
    s.addChart(pres.charts.BAR, [{ name: "Findings", labels: ["Fixed", "Fixed in tree", "Partial", "Changed", "Deferred", "Proposed accept"], values: [43, 4, 10, 2, 2, 1] }], {
      x: 0.5, y: 1.3, w: 6.2, h: 5.0, barDir: "bar",
      chartColors: [HEX.teal], showValue: true, dataLabelPosition: "outEnd", dataLabelColor: HEX.ink, dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt",
      catAxisLabelColor: HEX.ink, catAxisLabelFontSize: 12, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true,
      valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false,
      showTitle: true, title: "Final disposition of the 62 findings (25 are severity S1)", titleFontSize: 14, titleColor: HEX.petrol, titleFontFace: "+mn-lt",
    });
    const rc = [["RC-1 No governance by design", "ADR-0001 kept legacy beside the API, never revisited (plausible; owner not interviewed)"],
      ["RC-2 Identity not modelled", "role from a header; lookup by any column"], ["RC-3 No data contracts", "defects in all six datasets, counted and discarded"],
      ["RC-4 AI unguarded by design", "no auth, no schema, guardrail not enforced"], ["RC-5 No evidence by-product", "CI ran nothing useful; quick-start failed"]];
    rc.forEach(([h, b], i) => card(s, 7.0, 1.3 + i * 1.07, 5.85, 0.97, h, b));
  }

  divider(S1, "02", "What we built and proved", "One control point, AI behind a gateway, and the same attacks run twice", "Part two: Repo 2.0 and the proof.");
  {
    const s = slide("DIAGRAM", S1, "02  What we built and proved", "Repo 2.0: one control point, ports, and AI behind a gateway",
      "A modular monolith with ports, chosen over hardening the old monolith or splitting into services. Every request passes the token check and the policy engine, which reads its rules from the semantic layer. The AI gateway only suggests, only sees allow-listed fields, and refuses rather than return an invalid answer. Grey boxes are not built because they need owner decisions.");
    drawDiagram(s, "03-architecture-repo-2.0");
  }
  {
    const s = slide("CONTENT", S1, "02  What we built and proved", "Repo 1.0 vs Repo 2.0 at a glance",
      "The full 20-row comparison, with findings and evidence for each row, is the 'Repo 1.0 vs 2.0' sheet of the evidence register. Read the status column honestly.");
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
    table(s, rows, { x: 0.5, y: 1.3, w: 12.33, colW: [2.1, 3.4, 5.03, 1.8], fontSize: 12, rowH: 0.5 });
  }
  {
    const s = slide("CONTENT", S1, "02  What we built and proved", "Proof: the same 12 attacks, before and after",
      "Same twelve attacks, same requests, against the delivered code and against Repo 2.0. Ten succeeded before; none succeed now. Two did not succeed even before (RT-08 and RT-10). Caveat: our own red team, not an independent one.");
    tile(s, 0.5, 1.35, 3.7, 2.15, "10 of 12", "succeeded against Repo 1.0", HEX.red);
    tile(s, 0.5, 3.75, 3.7, 2.15, "0 of 12", "succeed against Repo 2.0", HEX.green);
    s.addText("Run by the builder, not an independent team. Source: evidence/26-tevv/EVD-L-03-redteam-*.json", { x: 0.5, y: 6.1, w: 3.7, h: 0.8, fontSize: 11, color: HEX.grey, margin: 0, isTextBox: true, valign: "top" });
    const rt = [["RT-01", "Call the AI endpoint with no identity", 200, 1, 401], ["RT-02", "Claim admin with a header", 200, 1, 401], ["RT-03", "Use a persona from another domain", 200, 1, 401],
      ["RT-04", "Look up a record by a non-key column", 200, 1, 422], ["RT-05", "Ask for a record that does not exist", 200, 1, 422], ["RT-06", "Reach the planted colliding key", 200, 1, 422],
      ["RT-07", "Reflect attacker text through the AI", 200, 1, 422], ["RT-08", "Smuggle text via a category field", 200, 0, 200], ["RT-09", "Find the guardrail switched off", 200, 1, 200],
      ["RT-10", "Action a suggestion without approval", 404, 0, 401], ["RT-11", "Forge a token (alg none, admin)", 200, 1, 401], ["RT-12", "Exhaust the AI endpoint", 200, 1, 429]];
    const res = (ok) => ({ text: ok ? "succeeded" : "failed", options: { fill: { color: ok ? "FCEBEA" : "E5F3EB" }, bold: true } });
    const rows = [[H("Attack"), H("Goal"), H("Repo 1.0"), H("Result"), H("Repo 2.0"), H("Result")]].concat(
      rt.map(([id, g, s1, ok, s2]) => [id, g, String(s1), res(ok), String(s2), res(false)]));
    table(s, rows, { x: 4.5, y: 1.35, w: 8.33, colW: [0.8, 3.53, 0.95, 1.1, 0.95, 1.0], fontSize: 11, rowH: 0.39 });
  }

  divider(S1, "03", "Can the knowledge travel?", "We rebuilt the system from the semantic layer alone, then compared", "Part three, new in v2.0: the capstone portability test.");
  {
    const s = slide("DIAGRAM", S1, "03  Can the knowledge travel?", "Semantic layer v2.0: knowledge owned outside the code and the model",
      "The semantic layer holds the business meaning in portable files: Markdown for people, YAML for definitions, JSON Schema for validation, JSON for exchange, tests for integrity. The application reads it at run time for access, data rules and AI rules. It was extracted after the transformation, as the capstone requires.");
    drawDiagram(s, "06-semantic-layer");
  }
  {
    const s = slide("DIAGRAM", S1, "03  Can the knowledge travel?", "The rebuild: semantic layer in, application out, then compared",
      "Only the 21 files of semantic-layer/ were given to a separate builder agent, which read nothing else; all 57 of its actions were audited. It wrote a PRD, then the application, its own synthetic data, 175 passing tests and a gap report. We then sent the same probes to both applications, on each one's own data and on swapped data.");
    drawDiagram(s, "07-semantic-layer-rebuild");
  }
  {
    const s = slide("CONTENT", S1, "03  Can the knowledge travel?", "Same behaviour, not the same repository",
      "The headline: on 29 of 30 black-box checks the rebuild answered with the same status code, and on identical data its AI recommendation agreed for all 41 shipments. But fed the original dataset, it accepted none of the 354 shipment rows. The layer says an out-of-domain value is rejected; the original application only flags most of them. That rule lives in the original's code, not in the layer. 67 assumptions were needed to fill other gaps.");
    tile(s, 0.5, 1.35, 2.95, 2.3, "29 / 30", "black-box checks return the same status code", HEX.green);
    tile(s, 3.63, 1.35, 2.95, 2.3, "41 / 41", "AI recommendations agree when both run on the same data", HEX.green);
    tile(s, 6.76, 1.35, 2.95, 2.3, "0 / 354", "original shipment rows the rebuild accepts (original: 349)", HEX.red);
    tile(s, 9.89, 1.35, 2.95, 2.3, "67", "assumptions the builder had to make; 17 items not buildable", "B9770E");
    card(s, 0.5, 3.95, 6.05, 2.75, "Carried over exactly",
      "Access rules (persona, entity, purpose, masking), token checks, record lookup rules, the AI decision rules (classes, precedence, abstain), approval once only, the hash-chained audit, rate limiting. The rebuild read these from the layer at run time.",
      { fill: "E5F3EB", headColor: HEX.green, icon: ICONS.check, iconBg: HEX.green });
    card(s, 6.78, 3.95, 6.05, 2.75, "Did not carry over",
      "Data intake severity: the layer says reject; the original flags. Also missing: nested response shapes, token and audit formats, a dataset, links from shipments to routes and vehicles, and delivery assets (CI, Docker, policy file, web view).",
      { fill: "FCEBEA", headColor: HEX.red, icon: ICONS.filter, iconBg: HEX.red });
  }
  {
    const s = slide("CONTENT", S1, "03  Can the knowledge travel?", "The six capstone comparison areas",
      "These are the six areas the capstone requirement asks the final report to evaluate. Our evidence and its limits for each. One run, one builder model, same vendor family; the comparison was run by an agent that also helped build the original.");
    const rows = [[H("Area"), H("What we found"), H("Verdict")],
      ["PRD generation", "A PRD came from the layer alone: 13 API and 5 workflow requirements, each cited to a layer file and key", chip("Yes")],
      ["Application generation", "The 10 operations behave the same (29 of 30 checks; 41 of 41 AI decisions); intake rejects the original data", chip("Partial")],
      ["Context completeness", "67 assumptions, 17 items not buildable, 24 inconsistencies inside the layer", chip("Partial")],
      ["Model independence", "Shown for one builder, one run, same vendor family; not across vendors", chip("Partial")],
      ["Repository dependency", "Original code not needed to build; the layer's own tests still need the original data and KPI dictionary", chip("Partial")],
      ["Knowledge-transfer quality", "High for access, AI decisions and the domain model; low for wire formats, intake severity and relationships", chip("Partial")]];
    table(s, rows, { x: 0.5, y: 1.3, w: 12.33, colW: [2.9, 7.83, 1.6], fontSize: 14, rowH: 0.72 });
  }
  {
    const s = slide("CONTENT", S1, "03  Can the knowledge travel?", "What the layer needs for an identical rebuild",
      "Each of these closes a group of the builder's assumptions. The first one alone would have let the rebuild accept the original data. The next step we propose is to add these to the layer and run the blind rebuild again.");
    const items = [
      ["Intake severity per rule", "Which violations quarantine a row and which only flag it, including the BR-04 override and placeholder references", ICONS.filter],
      ["Wire-level API schema", "Nested response shapes, every status code per operation, error types, headers, rate-limit numbers", ICONS.code],
      ["Token and audit formats", "Algorithm, required claims, expiry; audit record schema and how the hash chain is computed", ICONS.lock],
      ["Data the layer stands on", "A small canonical dataset or generator spec, the event stream, the KPI dictionary inside the layer", ICONS.db],
      ["Relationships", "Link shipments to routes and vehicles, or state that no link exists", ICONS.link],
      ["Numbers in keys, not prose", "Thresholds and status lists as keys, one version number, contradictions resolved", ICONS.hash],
    ];
    items.forEach(([h, b, ic], i) => card(s, 0.5 + (i % 2) * 6.2, 1.3 + Math.floor(i / 2) * 1.85, 5.95, 1.65, h, b, { icon: ic, iconBg: HEX.teal }));
  }

  divider(S1, "04", "Decision and asks", "What is ready, what is not, and what only the CTO can give", "Part four: readiness, limits and the asks.");
  {
    const s = slide("CONTENT", S1, "04  Decision and asks", "Readiness: six gates pass; production gates need people and a platform",
      "Gates were fixed before the decision. G1 to G6 pass at repository level, G7 is partial. G8 to G12 fail, and none can be closed by more engineering from us. The pilot also carries five conditions: a sponsor accepts the operator in every role; credentials resolved; branch protection on (needs a paid GitHub plan for a private repository); no real data or hosted model; one independent reviewer reads the pack.");
    const g = [["G1", "Tests and coverage", "PASS"], ["G2", "Evaluation (deterministic provider only)", "PASS"], ["G3", "No original defect re-exploitable", "PASS"],
      ["G4", "No critical or high dependency vulnerability", "PASS"], ["G5", "Audit tamper-evident, reconstruction shown", "PASS"], ["G6", "Backup restore shown", "PASS"],
      ["G7", "Rollback defined and rehearsed", "PARTIAL"], ["G8", "Alerts routed to named people", "FAIL"], ["G9", "Named approver and risk owners", "FAIL"],
      ["G10", "Platform and identity provider exist", "FAIL"], ["G11", "Independent evidence review", "FAIL"], ["G12", "Compliance resolved for real data", "FAIL"]];
    g.forEach(([id, t, st], i) => {
      const col = i % 3, row = Math.floor(i / 3);
      const x = 0.5 + col * 4.15, y = 1.3 + row * 1.3;
      const fill = st === "PASS" ? "E5F3EB" : st === "PARTIAL" ? "FFF4E0" : "FCEBEA";
      const fc = st === "PASS" ? HEX.green : st === "PARTIAL" ? "B9770E" : HEX.red;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 3.95, h: 1.13, rectRadius: 0.08, fill: { color: fill }, line: { type: "none" } });
      s.addText([{ text: `${id}  ${st}`, options: { bold: true, fontSize: 16, color: fc, breakLine: true } }, { text: t, options: { fontSize: 15, color: HEX.ink } }],
        { x: x + 0.15, y: y + 0.08, w: 3.65, h: 0.97, margin: 0, valign: "top", isTextBox: true });
    });
    s.addText("Pilot needs G1 to G7 plus five conditions (sponsor, credentials, branch protection, no real data, one reviewer). Production needs all twelve.", { x: 0.5, y: 6.62, w: 12.3, h: 0.35, fontSize: 13, italic: true, color: HEX.grey, margin: 0, isTextBox: true });
  }
  {
    const s = slide("CONTENT", S1, "04  Decision and asks", "What is not proven, stated before anyone asks",
      "These are the limits of the evidence, each recorded in the residual-risk register with an owner role. They are the reason the verdict is a pilot, not production.");
    const items = [
      ["No real AI model", "All AI evidence uses the deterministic provider. No model by decision (OQ-02).", ICONS.robot],
      ["Nothing deployed", "Platform-neutral by decision (OQ-01). Terraform provisions nothing; the image was never built.", ICONS.server],
      ["No business value measured", "K1 to K8 come from a static synthetic fixture, so they cannot move.", ICONS.chart],
      ["No independent review", "One operator and one agent built, tested and graded everything.", ICONS.eye],
      ["Portability partly shown", "Two rebuilds: behaviour and safety carried over; data intake and AI-output detail did not.", ICONS.exchange],
      ["Secrets in history", "Removed from the tree; history kept; repository private; values treated as compromised.", ICONS.key],
    ];
    items.forEach(([h, b, ic], i) => card(s, 0.5 + (i % 2) * 6.2, 1.3 + Math.floor(i / 2) * 1.85, 5.95, 1.65, h, b, { fill: i < 4 ? "FCEBEA" : "FFF4E0", headColor: HEX.red, icon: ic, iconBg: i < 4 ? HEX.red : "B9770E" }));
  }
  {
    const s = slide("CONTENT", S1, "04  Decision and asks", "Six asks of the CTO",
      "The operator has decided all 23 open questions, but one person holds every role. What only the CTO or sponsor can add is independence. The signature block is in docs/44-decisions/cto-signoff-pack.md.");
    const asks = [
      ["1  Ratify the write authorisation", "Given by the operator to themselves (OQ-11). Minutes.", ICONS.pen],
      ["2  Name approvers; sign or reject 12 risk acceptances", "0 of 12 signed; the only NOT MET rubric row (OQ-05). About an hour.", ICONS.users],
      ["3  Confirm platform, model and egress", "Decides whether IaC and a working AI model can ever be met (OQ-01 to 03). A conversation.", ICONS.plug],
      ["4  Name a regulatory regime, or confirm none", "Validates the candidate obligations (OQ-04, OQ-21). A day of review.", ICONS.balance],
      ["5  Confirm proxy KPIs; say if real figures exist", "The sponsor owns the value argument (OQ-08, OQ-09). Minutes.", ICONS.check],
      ["6  Appoint one independent reviewer", "Every gate and grade was self-run (GOV-10). A few hours.", ICONS.user],
    ];
    asks.forEach(([h, b, ic], i) => card(s, 0.5 + (i % 2) * 6.2, 1.3 + Math.floor(i / 2) * 1.85, 5.95, 1.65, h, b, { icon: ic, iconBg: HEX.petrol }));
  }
  {
    const s = pres.addSlide({ masterName: "DARK", sectionTitle: S1 });
    s.addShape(pres.shapes.OVAL, { x: 10.2, y: -1.2, w: 4.2, h: 4.2, fill: { color: HEX.petrol2 }, line: { type: "none" } });
    s.addText("Thank you", { x: 0.8, y: 2.0, w: 9, h: 1.2, fontSize: 48, bold: true, color: "FFFFFF", margin: 0, isTextBox: true });
    s.addText("Questions, and the six asks", { x: 0.8, y: 3.2, w: 9, h: 0.7, fontSize: 22, color: HEX.amber, margin: 0, isTextBox: true });
    s.addText("Team Delta: Dinesh Naik (presenter), Hardik Trivedi, Nachiket Bordekar, Rama Vedula, Sudhir Kulkarni", { x: 0.8, y: 4.3, w: 11, h: 0.8, fontSize: 16, color: HEX.ice, margin: 0, isTextBox: true, valign: "top" });
    s.addNotes("Close on the asks. Appendix slides follow for questions.");
    n += 1;
  }

  // =========================== APPENDIX
  const S2 = "Appendix";
  pres.addSection({ title: S2 });
  divider(S2, "A", "Appendix", "Detail for questions", "Use these slides only if asked.");
  {
    const s = slide("DIAGRAM", S2, "Appendix", "One AI summary request, before and after",
      "Top row: Repo 1.0. Below: Repo 2.0. Each check fails closed with its own status code; the producer sees only allowed fields; the answer is checked, falls back, or abstains; the suggestion waits for a person; everything is audited.");
    drawDiagram(s, "04-ai-request-path-v1-vs-v2");
  }
  {
    const s = slide("CONTENT", S2, "Appendix", "Engineering health moved; business KPIs did not, by design",
      "K9 and K10 improved because tests were written. K1 to K8 come from a static synthetic fixture the intervention does not touch, so equal before and after is the honest result. No business benefit is claimed.");
    s.addChart(pres.charts.BAR, [{ name: "Repo 1.0", labels: ["Tests passing", "Coverage %"], values: [3, 45] }, { name: "Repo 2.0", labels: ["Tests passing", "Coverage %"], values: [181, 97] }], {
      x: 0.5, y: 1.3, w: 6.0, h: 5.2, barDir: "col", barGrouping: "clustered",
      chartColors: [HEX.red, HEX.teal], showValue: true, dataLabelPosition: "outEnd", dataLabelColor: HEX.ink, dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt",
      catAxisLabelColor: HEX.ink, catAxisLabelFontSize: 13, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
      showLegend: true, legendPos: "b", legendFontSize: 12, legendFontFace: "+mn-lt", legendColor: HEX.ink,
      showTitle: true, title: "K9 tests and K10 coverage (apps and etl)", titleFontSize: 14, titleColor: HEX.petrol, titleFontFace: "+mn-lt",
    });
    const rows = [[H("KPI"), H("Baseline"), H("After"), H("Why")],
      ["K1 latency p50 (ms)", "1667", "1667", "fixture column"], ["K2 cost per event", "2.2451", "2.2451", "static"], ["K3 severe-event share", "39.6%", "39.6%", "static"],
      ["K4 correlation completeness", "33.6%", "33.6%", "producer unchanged"], ["K6 retries max", "4995", "4995", "static"], ["K7 duplicate keys (raw)", "18", "18", "quarantined downstream"]];
    table(s, rows, { x: 6.9, y: 1.4, w: 5.93, colW: [2.33, 1.0, 1.0, 1.6], fontSize: 12, rowH: 0.45 });
    s.addText("K5 and K8 are also equal; the full table is the KPIs sheet of the evidence register.", { x: 6.9, y: 4.85, w: 5.93, h: 0.6, fontSize: 12, color: HEX.grey, margin: 0, isTextBox: true });
  }
  {
    const s = slide("CONTENT", S2, "Appendix", "Earlier second-model test (Stage Q): safety held; AI-output fidelity did not",
      "Before v2.0 of the layer, a smaller same-vendor model rebuilt a four-behaviour subset from the layer plus the PRD, specifications and a brief. Safety matched on this harness, though the 0 of 12 is partly vacuous: three AI-path attacks reached the AI only in a post-hoc re-run. Its eight specification gaps were then written into the layer (v2.0), which the new blind rebuild in part 03 tested.");
    const rows = [[H("Dimension"), H("Model A (built the system)"), H("Model B (blind rebuild)")],
      ["Scope", "Full system", "Four-behaviour subset"],
      ["Evaluation cases passing every strict check", "192 of 192", { text: "8 of 192", options: { fill: { color: "FCEBEA" }, bold: true } }],
      ["Safety gates (schema, claims, leaks, injection, approval)", chip("PASS 5 of 5"), chip("PASS 5 of 5")],
      ["Fidelity gates (abstention, recommendation class)", chip("PASS 2 of 2"), { text: "0 of 2 (0.875; 0.1667 vs 1.0)", options: { fill: { color: "FCEBEA" }, bold: true } }],
      ["Black-box API checks", "24 of 24", "21 of 24 (24 with an ai_agent token, post hoc)"],
      ["Original attacks that succeed", "0 of 12", "0 of 12 (3 AI-path attacks reached the AI only in a post-hoc re-run)"],
      ["Audit chain valid; tampering detected", "yes", "yes"]];
    table(s, rows, { x: 0.5, y: 1.3, w: 12.33, colW: [4.6, 3.6, 4.13], fontSize: 13, rowH: 0.5 });
    s.addText("Source: docs/40-scale/model-comparison.md; evidence/40-scale/EVD-Q-06-comparison.csv. Models: claude-sonnet-5-5 (A) and claude-haiku-5-5 (B).", { x: 0.5, y: 6.0, w: 12.3, h: 0.5, fontSize: 12, color: HEX.grey, margin: 0, isTextBox: true });
  }
  {
    const s = slide("DIAGRAM", S2, "Appendix", "How any claim traces to proof",
      "Any number in this deck can be followed to a file: the document cites the path and its hash, the folder manifest records how and when it was produced, and the index ties it to findings and rubric criteria.");
    drawDiagram(s, "05-evidence-chain");
  }
  {
    const s = slide("CONTENT", S2, "Appendix", "Rubric evidence coverage by criterion",
      "Counts of sub-dimensions by status. This measures how complete the evidence is, not how many marks an evaluator will give. In our judgement, R3 and R4 are held back by missing people and a missing model, not by missing work.");
    const lab = ["R1 As-Is (20)", "R2 Repo 2.0 (25)", "R3 Governance (20)", "R4 PRD and app (25)", "R5 Defence (10)"];
    s.addChart(pres.charts.BAR, [
      { name: "MET", labels: lab, values: [6, 5, 5, 4, 4] }, { name: "PARTIAL", labels: lab, values: [1, 4, 2, 1, 1] },
      { name: "NOT MET", labels: lab, values: [0, 0, 1, 0, 0] }, { name: "BLOCKED", labels: lab, values: [0, 0, 1, 1, 0] }], {
      x: 0.5, y: 1.3, w: 8.0, h: 5.3, barDir: "bar", barGrouping: "stacked",
      chartColors: [HEX.green, HEX.amber, HEX.red, "7B241C"], showValue: true, dataLabelPosition: "ctr", dataLabelFormatCode: "0;;;", dataLabelColor: "FFFFFF", dataLabelFontSize: 12, dataLabelFontFace: "+mn-lt",
      catAxisLabelColor: HEX.ink, catAxisLabelFontSize: 12, catAxisLabelFontFace: "+mn-lt", valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
      showLegend: true, legendPos: "b", legendFontSize: 12, legendFontFace: "+mn-lt", legendColor: HEX.ink,
      showTitle: true, title: "36 sub-dimensions by status", titleFontSize: 14, titleColor: HEX.petrol, titleFontFace: "+mn-lt",
    });
    const rows = [[H("Criterion"), H("Coverage index")], ["R1", "0.93"], ["R2", "0.78"], ["R3", "0.67"], ["R4", "0.75"], ["R5", "0.90"]];
    table(s, rows, { x: 8.9, y: 1.5, w: 3.9, colW: [1.9, 2.0], fontSize: 13, rowH: 0.45 });
    s.addText("Index = (MET + half of PARTIAL) ÷ sub-dimensions. Source: docs/43-rubric-traceability/readiness-assessment.md.", { x: 8.9, y: 4.5, w: 3.9, h: 1.0, fontSize: 12, color: HEX.grey, margin: 0, isTextBox: true, valign: "top" });
  }
  {
    const s = slide("CONTENT", S2, "Appendix", "Where to find everything",
      "Point the audience at the deliverables folder first, then the repository paths for depth.");
    const rows = [[H("You want"), H("Open")],
      ["The story in writing", "deliverables/01-CTO-Briefing-v2.0.docx (or .md)"],
      ["Every evidence file, finding, gate, decision and risk", "deliverables/03-Evidence-Register.xlsx"],
      ["Diagrams to edit", "deliverables/diagrams/*.drawio; shapes in this deck are native and editable"],
      ["The semantic-layer rebuild and its comparison", "Deliverables/semantic-layer-rebuild (repository) and semantic-layer-rebuild-comparison/COMPARISON.md"],
      ["The readiness decision", "docs/42-executive/production-readiness-decision.md"],
      ["The CTO sign-off block", "docs/44-decisions/cto-signoff-pack.md"],
      ["The semantic layer", "semantic-layer/ (start with README.md and SEMANTIC-COMPLETENESS.md)"],
      ["The runbooks that drove the work", "runbook/00 to 04 (Markdown and Word)"]];
    table(s, rows, { x: 0.5, y: 1.3, w: 12.33, colW: [4.2, 8.13], fontSize: 13, rowH: 0.52 });
  }

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT, "slides", n);
}
build();
