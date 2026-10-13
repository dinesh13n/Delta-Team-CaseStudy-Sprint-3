// Build deliverables/04-Presenter-Guide-v1.0.docx: a short guide for presenting the case study to the CTO.
// Usage (repository root): NODE_PATH=$(npm root -g) node deliverables/_build/build_presenter_guide.js
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow, TableCell, WidthType,
  ShadingType, BorderStyle, LevelFormat, ImageRun, Footer, Header, PageNumber, PageBreak,
} = require("docx");

const OUT = path.join(__dirname, "..", "04-Presenter-Guide-v1.0.docx");
const DIAG = path.join(__dirname, "..", "diagrams");
const C = { petrol: "0B3C49", teal: "1F7A8C", amber: "F2A541", amberLight: "FFF4E0", light: "E8F1F2", green: "2E8B57", greenLight: "E5F3EB", red: "C0392B", redLight: "FCEBEA", grey: "5F6E71", ink: "1B2A2F", line: "C5D6DA" };
const FONT = "Calibri";
const PAGE_W = 11906, MARGIN = 1134, TEXT_W = PAGE_W - 2 * MARGIN; // A4, 2 cm margins

// "**bold**" and "==highlight==" inline markup
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|==[^=]+==)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), font: FONT, ...base }));
    const t = m[0];
    if (t.startsWith("**")) out.push(new TextRun({ text: t.slice(2, -2), bold: true, font: FONT, ...base }));
    else out.push(new TextRun({ text: t.slice(2, -2), bold: true, highlight: "yellow", font: FONT, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), font: FONT, ...base }));
  return out;
}
const P = (t, o = {}) => new Paragraph({ children: runs(t, o.run || {}), spacing: { after: 120, line: 276 }, ...o.para });
const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: t, font: FONT, bold: true, color: C.petrol, size: 32 })], spacing: { before: 280, after: 120 }, keepNext: true });
const H2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: t, font: FONT, bold: true, color: C.teal, size: 25 })], spacing: { before: 200, after: 80 }, keepNext: true });
const B = (t, level = 0) => new Paragraph({ children: runs(t), numbering: { reference: "bullets", level }, spacing: { after: 60, line: 264 } });
const N = (t) => new Paragraph({ children: runs(t), numbering: { reference: "steps", level: 0 }, spacing: { after: 60, line: 264 } });

function keyBox(title, lines, fill = C.amberLight, border = C.amber) {
  const cellChildren = [new Paragraph({ children: [new TextRun({ text: title, bold: true, font: FONT, color: C.petrol, size: 22 })], spacing: { after: 60 } })]
    .concat(lines.map((l) => new Paragraph({ children: runs(l), numbering: { reference: "bullets", level: 0 }, spacing: { after: 40 } })));
  const bd = { style: BorderStyle.SINGLE, size: 12, color: border };
  return new Table({
    width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: [TEXT_W],
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({ width: { size: TEXT_W, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, fill, color: "auto" },
      borders: { top: bd, bottom: bd, left: bd, right: bd }, margins: { top: 120, bottom: 120, left: 180, right: 180 }, children: cellChildren })] })],
  });
}
const spacer = () => new Paragraph({ children: [], spacing: { after: 80 } });

function table(headers, rows, widths, fills = {}) {
  const total = widths.reduce((a, b) => a + b, 0);
  const bd = { style: BorderStyle.SINGLE, size: 4, color: C.line };
  const borders = { top: bd, bottom: bd, left: bd, right: bd };
  const mk = (t, w, opts = {}) => new TableCell({
    width: { size: w, type: WidthType.DXA }, borders, margins: { top: 60, bottom: 60, left: 100, right: 100 },
    shading: opts.fill ? { type: ShadingType.CLEAR, fill: opts.fill, color: "auto" } : undefined,
    children: [new Paragraph({ children: runs(String(t), { size: 19, ...(opts.head ? { bold: true, color: "FFFFFF" } : {}) }) })],
  });
  return new Table({
    width: { size: total, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: headers.map((h, i) => mk(h, widths[i], { head: true, fill: C.petrol })) })]
      .concat(rows.map((r, ri) => new TableRow({ cantSplit: true, children: r.map((c, i) => mk(c, widths[i], { fill: (fills[`${ri},${i}`]) || (ri % 2 ? "F3F7F8" : undefined) })) }))),
  });
}

function img(file, caption) {
  const data = fs.readFileSync(path.join(DIAG, file));
  const w = 620, h = Math.round(w * 1568 / 2560);
  return [new Paragraph({ alignment: AlignmentType.CENTER, children: [new ImageRun({ type: "png", data, transformation: { width: w, height: h } })], spacing: { before: 80, after: 40 } }),
    new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: caption, italics: true, color: C.grey, size: 18, font: FONT })], spacing: { after: 160 } })];
}

const body = [];
// ---------- cover block
body.push(new Paragraph({ children: [new TextRun({ text: "PRESENTER'S GUIDE  ·  CTO BRIEFING", bold: true, color: C.teal, size: 20, font: FONT, characterSpacing: 40 })], spacing: { after: 80 } }));
body.push(new Paragraph({ children: [new TextRun({ text: "From Brownfield to Governed AI", bold: true, color: C.petrol, size: 52, font: FONT })], spacing: { after: 60 } }));
body.push(new Paragraph({ children: [new TextRun({ text: "How to present the Logistics Ops Repo 2.0 case study, in what order, and what to say", color: C.teal, size: 26, font: FONT })], spacing: { after: 160 } }));
body.push(table(["Item", "Detail"], [
  ["Team", "Team Delta: **Dinesh Naik (presenter)**, Hardik Trivedi, Nachiket Bordekar, Rama Vedula, Sudhir Kulkarni"],
  ["Use with", "02-CTO-Presentation-v2.1.pptx (29 slides) and 01-CTO-Briefing-v2.1.docx (full detail)"],
  ["Version and date", "v1.0, 13 October 2026"],
  ["Time", "15 minutes full talk, or 10 minutes with the cuts in section 1; then questions"],
], [2300, TEXT_W - 2300]));
body.push(spacer());
body.push(keyBox("The one message to land", [
  "==Controls are proven; business value and independent review are not yet.==",
  "Recommendation: **NO-GO for production on real data**, **CONDITIONAL GO for a controlled pilot on synthetic data**.",
  "The semantic layer rebuilt the behaviour (29 of 30 checks, 41 of 41 AI decisions) but **not an identical repository**.",
]));

// ---------- 1 sequence
body.push(H1("1. Where to start and the order to present"));
body.push(P("Start with the answer, not the history. A CTO wants the verdict first, then the proof. Follow the four parts of the deck in order; each part answers one question."));
body.push(table(["#", "Slides", "Time", "Topic", "Say this in one line"], [
  ["1", "1 to 3", "1:30", "Team, agenda, the answer", "Controls proven; value and independence not yet; NO-GO production, CONDITIONAL GO pilot"],
  ["2", "4", "1:00", "The journey", "20 stages in six phases, with evidence produced at every step"],
  ["3", "5 to 7", "1:30", "01 The starting point", "Three code generations, no control point; 62 findings, five root causes"],
  ["4", "8 to 11", "2:30", "02 What we built and proved", "One control point; Repo 1.0 vs 2.0 vs 3.0; 10 of 12 attacks worked before, 0 now"],
  ["5", "12 to 17", "4:00", "03 Can the knowledge travel?", "A blind rebuild from the semantic layer behaved the same but could not ingest the original data"],
  ["6", "18 to 21", "3:00", "04 Decision and asks", "6 of 12 gates pass; the rest need people and a platform; six asks"],
  ["7", "22", "0:30", "Close", "Thank the team; invite questions"],
  ["–", "23 to 29", "if asked", "Appendix", "AI request path, KPIs, earlier second-model test, evidence chain, rubric, file map"],
], [450, 1050, 900, 2300, TEXT_W - 4700]));
body.push(spacer());
body.push(keyBox("If you only have 10 minutes", [
  "Skip slide 6 (Repo 1.0 diagram), slide 9 (Repo 2.0 diagram) and slide 13 (semantic layer overview); describe them in one sentence each.",
  "On slide 15, speak only to the four number tiles.",
  "**Never skip slides 3, 10, 11, 19 and 21**: the answer, the comparison, the proof, the gates and the asks.",
], C.light, C.teal));

// ---------- 2 problem
body.push(H1("2. Problem statement"));
body.push(P("**Context.** The repository runs logistics operations: shipments, tracking events, vehicles, routes, carrier bookings and an AI assistant that summarises exceptions for dispatchers."));
body.push(P("**What we were handed (Repo 1.0).** Three engineering generations side by side, legacy batch scripts, a partly modernised FastAPI service and an AI gateway, with nothing controlling who could do what."));
body.push(B("The documented test command **failed** (exit 2), so nobody could prove anything worked."));
body.push(B("**Any caller could claim any role** by sending a request header."));
body.push(B("The AI endpoint answered **with no authorisation** and reported its own guardrail as not enforced."));
body.push(B("A lookup that missed **returned a different record**."));
body.push(B("The audit trail recorded time and action only, so **no one could reconstruct who did what**."));
body.push(B("Policy, Terraform and CI files existed but **did nothing**; the docs promised AI features that did not exist."));
body.push(P("**The task.** Turn it into a production-grade Repo 2.0 with evidence for every claim, and capture the business knowledge in a semantic layer that survives a change of AI model."));
body.push(keyBox("Key points to stress", [
  "==62 findings, 25 of them most severe (S1)==, traced to **five root causes**: no governance by design, identity not modelled, no data contracts, AI unguarded by design, no evidence produced.",
  "We **froze the old behaviour in tests first**, so every before-and-after claim is measured, not described.",
]));

// ---------- 3 architecture
body.push(H1("3. Architecture"));
body.push(H2("3.1 Before: Repo 1.0"));
body.push(...img("02-architecture-repo-1.0.png", "Repo 1.0: three generations side by side, no control point (slide 6)"));
body.push(H2("3.2 After: Repo 2.0"));
body.push(...img("03-architecture-repo-2.0.png", "Repo 2.0: a modular monolith with one control point and ports (slide 9)"));
body.push(P("**Style:** a modular monolith with ports, chosen over hardening the old code or splitting into microservices. The application is small enough that network boundaries would add more failure modes than they remove (ADR-0002 to ADR-0010)."));
body.push(table(["Layer", "What it does"], [
  ["API layer", "Routes (10 operations), correlation id on every request, bearer-token check, a safe error shape"],
  ["Control point", "**Policy engine, deny by default**: persona × entity × purpose, field masking; key-pattern check; rate limit; approvals"],
  ["AI gateway", "**Suggest-only**: allowed fields only, sanitised text, output checks, fallback then abstain"],
  ["Ports and adapters", "Curated data, hash-chained audit, metrics and KPIs, carrier booking saga"],
  ["Batch and definitions", "ETL intake with the same rules as the API, quarantine, **semantic layer** feeding policy, data and AI rules, generated Rego policy, CI gates"],
  ["Not built (owner decisions)", "Identity provider, real AI model, platform and infrastructure, tracing collector"],
], [2600, TEXT_W - 2600]));
body.push(spacer());
body.push(keyBox("Key points to stress", [
  "==Every request passes one control point==, and its rules come from the semantic layer, not from code.",
  "The AI can **only suggest**; a person approves or rejects, once.",
  "What is not built is **not built on purpose**: each item waits for a CTO-level decision.",
]));

// ---------- 4 functional flow
body.push(H1("4. Functional flow"));
body.push(P("**Personas:** dispatcher, warehouse operations, fleet manager, driver, customs agent, customer support, carrier partner, and the AI agent; plus two platform roles, ops (metrics) and auditor (audit verification)."));
body.push(H2("4.1 An AI summary request, end to end"));
body.push(...img("04-ai-request-path-v1-vs-v2.png", "One AI summary request, before and after (appendix slide 24)"));
body.push(N("**Authenticate:** verify the bearer token, otherwise **401**."));
body.push(N("**Authorise:** the policy engine checks persona, entity and purpose, otherwise **403**."));
body.push(N("**Validate:** the shipment id must match its key pattern, otherwise **422**; unknown records return **404** and are audited."));
body.push(N("**Throttle:** the AI endpoint is rate-limited, otherwise **429**."));
body.push(N("**Build context:** only allow-listed fields; untrusted text is sanitised; personal and location data never enter."));
body.push(N("**Produce and check:** the deterministic producer answers; the output is checked for schema, leaks and confidence; on failure it falls back, then **abstains** rather than return an invalid answer."));
body.push(N("**Register and decide:** the suggestion is stored with **requires_human_approval = true**; a person with write access approves or rejects it **once** (a repeat gets 409)."));
body.push(N("**Audit:** every step is written to a **hash-chained audit trail**: who, for which purpose, which data, which prompt version, what came back."));
body.push(H2("4.2 Other flows"));
body.push(B("**Look up shipments and records:** fields are masked or dropped per persona (for example, customer id masked for dispatchers, removed for warehouse staff)."));
body.push(B("**Data intake:** the ETL validates every row with the same rules as the API; bad rows go to quarantine with a run id; the raw data is never edited."));
body.push(B("**Audit verification:** the auditor role runs a verify call that finds the first tampered record."));
body.push(keyBox("Key points to stress", [
  "==Every check fails closed with its own status code== (401, 403, 422, 404, 429), and every step leaves evidence.",
  "The AI recommendation falls into one of three defined classes: review the exception, check booking retries, or no action; or it abstains.",
]));

// ---------- 5 technical implementation
body.push(H1("5. Technical implementation"));
body.push(table(["Area", "Implementation"], [
  ["Runtime", "Python 3.11+, FastAPI; CI green on Python 3.11 and 3.14"],
  ["Identity", "HS256 signed bearer tokens; alg-none and forged tokens rejected; JWKS verifier is a fail-closed stub until an identity provider is chosen"],
  ["Authorisation", "Policy engine reads **access-semantics.yaml** at run time; Rego policy generated from the same file and tested with OPA in CI"],
  ["Data", "ETL validation with quarantine and run ids; curated layer; raw synthetic fixture kept byte-identical"],
  ["AI gateway", "Deterministic provider (no external model by decision); allow-listed context, sanitising, JSON-schema output check, leak check, timeout and circuit breaker, fallback then abstain"],
  ["Audit and observability", "Hash-chained JSON-lines audit with verify endpoint; correlation ids; /metrics; KPI endpoint K1 to K10; no tracing yet"],
  ["Resilience", "Timeout, retry, circuit breaker; carrier booking saga (book, confirm, compensate); five failure drills pass"],
  ["Quality gates", "**181 tests, 97% coverage**, ruff, mypy, secret scan, policy tests, semantic-layer tests"],
  ["Supply chain", "Hash-pinned lockfiles; SBOM (21 runtime, 58 development components); **0 known vulnerabilities**"],
  ["Semantic layer", "Markdown, YAML definitions, JSON Schema, JSON contract and generated layer, 23 layer tests plus 5 app conformance tests"],
  ["Evidence", "146 SHA-256-hashed evidence files with manifests; 203 of 203 document citations verified by script"],
  ["Deployment", "Platform-neutral container recipe; nothing provisioned by decision"],
], [2400, TEXT_W - 2400]));
body.push(spacer());
body.push(keyBox("Proof points to quote", [
  "==10 of 12 attacks succeeded on Repo 1.0; 0 of 12 succeed on Repo 2.0.==",
  "==3 tests and 45% coverage became 181 tests and 97% coverage.==",
  "==146 evidence files, every hash verified; 203 of 203 citations verified.==",
], C.greenLight, C.green));

// ---------- 6 semantic layer & rebuild
body.push(H1("6. Semantic layer and the Repo 3.0 rebuild"));
body.push(P("The semantic layer holds the business meaning outside the code and the model. To test it, a separate agent rebuilt the system **from the 21 layer files only** (Repo 3.0), and we compared it with Repo 2.0."));
body.push(table(["Check", "Result"], [
  ["Same status code on 30 black-box checks", "**29 of 30**"],
  ["AI recommendation agrees, same data", "**41 of 41**"],
  ["Original shipment rows accepted", "**0 of 354** (Repo 2.0 keeps 349)"],
  ["Assumptions the builder had to make", "67, with 17 items not buildable"],
], [5200, TEXT_W - 5200], { "2,1": C.redLight }));
body.push(spacer());
body.push(keyBox("How to explain the 0 of 354", [
  "The layer says out-of-domain values are **rejected**; Repo 2.0's code only **flags** most of them. That rule lives only in the code.",
  "==Lesson: behaviour transferred; one data rule did not.== Adding intake severity to the layer is the first fix.",
]));

// ---------- 7 decision
body.push(H1("7. Decision, limits and the six asks"));
body.push(P("**Gates:** G1 to G6 pass, G7 is partial, G8 to G12 fail. The failing gates need **named owners, a platform and identity provider, an independent reviewer and a compliance decision**, not more engineering."));
body.push(P("**State the limits before anyone asks:** no real AI model was called; nothing is deployed; no business KPI moved; the same operator and agent built, tested and graded everything."));
body.push(table(["#", "Ask of the CTO", "Time"], [
  ["1", "Ratify the write authorisation (OQ-11)", "minutes"],
  ["2", "Name approvers; sign or reject the 12 risk acceptances (OQ-05)", "about an hour"],
  ["3", "Confirm the platform, model and egress decisions (OQ-01 to OQ-03)", "a conversation"],
  ["4", "Name a regulatory regime, or confirm none applies (OQ-04, OQ-21)", "a day of review"],
  ["5", "Confirm the proxy KPIs; say whether real figures exist (OQ-08, OQ-09)", "minutes"],
  ["6", "Appoint one independent reviewer (GOV-10)", "a few hours"],
], [450, TEXT_W - 2450, 2000]));

// ---------- 8 Q&A
body.push(H1("8. Likely questions and short answers"));
const qa = [
  ["Is it production ready?", "No. It is ready for a controlled pilot on synthetic data. Production needs the five failing gates closed, and those need people and a platform."],
  ["Why is there no real AI model?", "By decision (OQ-02, OQ-03): no model and no network egress. The gateway has a model slot; a model can be added behind the same checks."],
  ["Why a monolith and not microservices?", "The system is small; one control point is easier to secure and prove. Ports keep it splittable later."],
  ["What business value did it deliver?", "None is measured. KPIs come from a static synthetic dataset, so they cannot move. We say so rather than claim savings."],
  ["Can another team or model rebuild it from the semantic layer?", "Behaviour, yes: 29 of 30 checks and 41 of 41 AI decisions matched. An identical repository, not yet: six additions to the layer are listed."],
  ["Who checked your work?", "No one independent yet. That is ask 6."],
];
qa.forEach(([q, a]) => { body.push(new Paragraph({ children: [new TextRun({ text: q, bold: true, color: C.petrol, font: FONT })], spacing: { before: 80, after: 20 } })); body.push(P(a)); });

// ---------- 9 files
body.push(H1("9. Where everything is"));
body.push(table(["You need", "Open"], [
  ["Slides", "deliverables/02-CTO-Presentation-v2.1.pptx"],
  ["Full written story", "deliverables/01-CTO-Briefing-v2.1.docx"],
  ["Every evidence file, finding, gate, decision, risk", "deliverables/03-Evidence-Register.xlsx"],
  ["Editable diagrams", "deliverables/diagrams/*.drawio"],
  ["The Repo 3.0 rebuild and comparison", "Deliverables/semantic-layer-rebuild and semantic-layer-rebuild-comparison/COMPARISON.md"],
  ["CTO sign-off block", "docs/44-decisions/cto-signoff-pack.md"],
], [3600, TEXT_W - 3600]));

const doc = new Document({
  creator: "Team Delta",
  title: "Presenter's Guide: From Brownfield to Governed AI",
  styles: { default: { document: { run: { font: FONT, size: 21, color: C.ink } } } },
  numbering: { config: [
    { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 260 } } } }] },
    { reference: "steps", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 400, hanging: 300 } } } }] },
  ] },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
      new TextRun({ text: "Team Delta  ·  Presenter's Guide v1.0  ·  page ", color: C.grey, size: 16, font: FONT }),
      new TextRun({ children: [PageNumber.CURRENT], color: C.grey, size: 16, font: FONT })] })] }) },
    children: body,
  }],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log("wrote", OUT); });
