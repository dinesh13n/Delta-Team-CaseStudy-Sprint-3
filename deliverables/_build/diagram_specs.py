"""Single source for every diagram in the CTO pack.

Each diagram is drawn on a 1280 x 720 canvas. build_diagrams.py turns this into:
  diagrams/<name>.drawio  (editable in diagrams.net / draw.io desktop / VS Code Draw.io extension)
  diagrams/<name>.svg and .png  (for documents)
  _build/diagrams.json  (read by build_deck.js to draw the same diagram as native, editable PowerPoint shapes)
Facts in the boxes come from the repository's evidence; see deliverables/README.md for sources.
"""

W, H = 1280, 720

STYLES = {
    #        fill      stroke    text      dashed  bold-first-line
    "lane":  ("F3F7F8", "C5D6DA", "0B3C49", False, True),
    "box":   ("FFFFFF", "1F7A8C", "0B3C49", False, True),
    "core":  ("0B3C49", "0B3C49", "FFFFFF", False, True),
    "accent": ("F2A541", "C98118", "1B1B1B", False, True),
    "bad":   ("FCEBEA", "C0392B", "7B241C", False, True),
    "good":  ("E5F3EB", "2E8B57", "1E5631", False, True),
    "ghost": ("FFFFFF", "9AA5A8", "5F6E71", True, True),
    "note":  ("FFFFFF", "FFFFFF", "41545A", False, False),
    "start": ("C0392B", "C0392B", "FFFFFF", False, True),
    "goal":  ("2E8B57", "2E8B57", "FFFFFF", False, True),
    "chip":  ("1F7A8C", "1F7A8C", "FFFFFF", False, True),
}


def B(id, x, y, w, h, text, kind="box", fs=16, align="center"):
    return {"id": id, "x": x, "y": y, "w": w, "h": h, "text": text, "kind": kind, "fs": fs, "align": align}


def L(id, x, y, w, h, label):
    return {"id": id, "x": x, "y": y, "w": w, "h": h, "text": label, "kind": "lane", "fs": 16, "align": "left"}


def E(a, b, dashed=False):
    return {"from": a, "to": b, "dashed": dashed}


def journey():
    n, e = [], []
    n.append(B("start", 10, 40, 150, 330,
               "START\nRepo 1.0 as delivered\n\n• Quick-start fails\n• Any caller claims any role\n• AI answers unchecked\n• Wrong record on a miss\n• No usable audit",
               "start", 15, "left"))
    n.append(B("goal", 1120, 40, 150, 330,
               "GOAL\nA defended decision\n\n• Production on real data: NO-GO\n• Pilot on synthetic data: CONDITIONAL GO\n• Six asks of the CTO",
               "goal", 15, "left"))
    xs = [175, 332, 489, 645, 802, 959]
    heads = ["1 Understand\nStages A–C", "2 Define\nStages D–G", "3 Build\nStages H–J",
             "4 Prove\nStages K–N", "5 Defend\nStages O–R", "6 Close-out\nRunbooks 03–04"]
    cards = ["A Mobilise\nB Problem, value\nC Baseline, root cause",
             "D Semantic layer\nE AI choice, PRD\nF Architecture, specs\nG Migration plan",
             "H Repo 2.0\nI Delivery PRD\nJ AI core, app, integration",
             "K Controls\nL Tests, red team\nM Resilience\nN Release, operations",
             "O Outcomes\nP Handover\nQ Second-model test\nR Executive defence",
             "S Rubric traceability\nT 23 decisions\nSemantic layer v2.0"]
    outs = ["62 findings\n5 root causes\nBehaviour frozen in tests",
            "Layer v1 with tests\nADR-0002 to 0010\n48 requirements traced",
            "181 tests pass\n97% coverage\nCI green",
            "Red team 10/12 → 0/12\n5 drills pass\nHash-chained audit",
            "Proxy KPIs unchanged\nModel B safety 5/5\nNO-GO prod, GO pilot",
            "36 sub-dimensions\n146 evidence files\n22 decided, 1 deferred"]
    for i, x in enumerate(xs):
        n.append(B(f"h{i}", x, 40, 146, 62, heads[i], "core", 15))
        n.append(B(f"c{i}", x, 112, 146, 150, "Stages\n" + cards[i], "box", 14, "left"))
        n.append(B(f"o{i}", x, 272, 146, 98, outs[i], "good", 13, "left"))
    e.append(E("start", "c0"))
    for i in range(5):
        e.append(E(f"h{i}", f"h{i+1}"))
    e.append(E("c5", "goal"))
    n.append(L("ev", 10, 395, 1260, 175, "Evidence discipline applied in every stage"))
    evs = ["Header on every file\nstage, status, assumptions, risks",
           "SHA-256 manifest\nin every evidence folder",
           "Claims cite path + hash\n203 of 203 match",
           "Every claim tagged\n[VF] [INF] [ASM] [UNK]",
           "Exit gate\nbefore the next stage"]
    for i, t in enumerate(evs):
        n.append(B(f"ev{i}", 30 + i * 248, 440, 228, 105, t, "box", 15))
    n.append(L("tl", 10, 585, 1260, 125, "Milestones (git commits on main)"))
    tl = ["Plan\nRunbooks 00–04", "698e858\nStage A", "4c84af1\nStages A–P", "c7d94de\nStages Q–R",
          "ab37ec8\nSecond model", "1dcf6e8\nRunbook 03", "1cde803\nRunbook 04", "ad230eb\nLayer v2.0"]
    for i, t in enumerate(tl):
        n.append(B(f"t{i}", 30 + i * 154, 625, 136, 62, t, "chip", 14))
        if i:
            e.append(E(f"t{i-1}", f"t{i}"))
    return {"name": "01-journey-start-to-goal", "title": "Delivery journey: from the brownfield repository to a defended readiness decision", "nodes": n, "edges": e}


def arch_v1():
    n, e = [], []
    n.append(L("l_call", 10, 10, 180, 440, "Callers"))
    n.append(B("caller", 25, 60, 150, 110, "API caller\nsends an X-User-Role header", "bad", 15))
    n.append(B("portal", 25, 200, 150, 90, "Web portal\nscaffold only", "bad", 15))
    n.append(L("l_api", 205, 10, 430, 440, "Generations 2 and 3: API and AI (apps/api)"))
    n.append(B("main", 225, 55, 390, 90, "main.py: 3 routes\nrole taken from the header, never checked", "bad", 15))
    n.append(B("ai", 225, 190, 120, 160, "AI gateway\nno auth; guardrail not enforced", "bad", 14))
    n.append(B("audit", 360, 190, 120, 160, "Audit writer\nno actor, no correlation id", "bad", 14))
    n.append(B("dom", 495, 190, 120, 160, "Record lookup\nany column; a row even on a miss", "bad", 14))
    n.append(L("l_leg", 205, 465, 430, 245, "Generation 1: legacy batch"))
    n.append(B("rec", 225, 505, 390, 80, "reconcile_legacy.py\ncounts rows; hard-coded credential", "bad", 15))
    n.append(B("etl", 225, 605, 390, 80, "run_daily_batch.py\ncounts blanks; validates nothing", "bad", 15))
    n.append(L("l_data", 650, 10, 220, 700, "Data (data/synthetic)"))
    n.append(B("data", 665, 60, 190, 250, "7 synthetic files\nshipments, tracking events, vehicles, routes, bookings, AI calls, event stream", "box", 15))
    n.append(B("defects", 665, 330, 190, 200, "Seeded defects\nduplicates, bad keys, REC-0001 collision, placeholder values", "bad", 15))
    n.append(L("l_nc", 885, 10, 385, 700, "Present but not connected"))
    n.append(B("rego", 900, 55, 355, 70, "access.rego\nreferenced by no code", "ghost", 15))
    n.append(B("tf", 900, 140, 355, 70, "Terraform\none local_file resource", "ghost", 15))
    n.append(B("env", 900, 225, 355, 70, ".env.example\ncredential-shaped values", "bad", 15))
    n.append(B("ci", 900, 310, 355, 80, "CI and quick-start\npytest only and never run; quick-start fails", "bad", 15))
    n.append(B("docs", 900, 405, 355, 80, "Docs promise ETA, routing, copilot\nnone of it exists in code", "ghost", 15))
    n.append(B("legend", 900, 505, 355, 185,
               "Scale\nAbout 140 lines of application code and 3 tests.\nRed: defect confirmed at baseline (62 findings in all).\nGrey dashed: present, does nothing.",
               "note", 14, "left"))
    e += [E("caller", "main"), E("portal", "main", True), E("main", "ai"), E("main", "audit"), E("main", "dom"),
          E("dom", "data"), E("l_leg", "defects")]
    return {"name": "02-architecture-repo-1.0", "title": "Repo 1.0 as delivered: three generations side by side, no control point", "nodes": n, "edges": e}


def arch_v2():
    n, e = [], []
    n.append(L("l_call", 10, 10, 150, 470, "Callers"))
    n.append(B("ops", 22, 60, 126, 100, "Operations view\n/ops, read-only", "box", 14))
    n.append(B("cli", 22, 200, 126, 110, "API client\nbearer token: who, role, purpose", "box", 14))
    n.append(L("l_api", 172, 10, 200, 470, "API layer"))
    n.append(B("corr", 185, 240, 174, 80, "Correlation id\non every request", "box", 14))
    n.append(B("tok", 185, 145, 174, 80, "Token check\nHS256; JWKS stub", "box", 14))
    n.append(B("routes", 185, 50, 174, 80, "Routes\n10 operations", "box", 14))
    n.append(B("err", 185, 335, 174, 80, "Error shape\nno internals leak", "box", 14))
    n.append(L("l_ctl", 384, 10, 220, 470, "Control point"))
    n.append(B("appr", 397, 370, 194, 80, "Approvals\napprove or reject, once", "box", 14))
    n.append(B("key", 397, 200, 194, 70, "Key pattern check\nelse 422", "box", 14))
    n.append(B("rate", 397, 285, 194, 70, "Rate limit\nelse 429", "box", 14))
    n.append(B("pol", 397, 50, 194, 135, "Policy engine\ndeny by default; persona, entity, purpose; rules from the semantic layer", "core", 14))
    n.append(L("l_ai", 616, 10, 240, 470, "AI gateway (suggest-only)"))
    n.append(B("ctx", 629, 50, 214, 90, "Context\nallowed fields only; text sanitised", "box", 14))
    n.append(B("prod", 629, 155, 214, 90, "Producer\ndeterministic; model slot empty", "box", 14))
    n.append(B("chk", 629, 260, 214, 80, "Output checks\nschema, leaks, confidence", "box", 14))
    n.append(B("fb", 629, 355, 214, 95, "Fallback, then abstain\nnever an invalid answer", "box", 14))
    n.append(L("l_port", 868, 10, 402, 470, "Ports and adapters"))
    n.append(B("cur", 881, 50, 182, 95, "Curated data\nvalidated; fixture untouched", "box", 14))
    n.append(B("aud", 1075, 50, 182, 95, "Audit chain\nhash-linked; verify endpoint", "box", 14))
    n.append(B("met", 881, 160, 182, 80, "Metrics, KPIs\nK1 to K10", "box", 14))
    n.append(B("saga", 1075, 160, 182, 80, "Carrier saga\nbook, confirm, compensate", "box", 14))
    n.append(B("idp", 881, 255, 182, 60, "Identity provider", "ghost", 14))
    n.append(B("mdl", 1075, 255, 182, 60, "Real AI model", "ghost", 14))
    n.append(B("plat", 881, 330, 182, 60, "Platform, IaC", "ghost", 14))
    n.append(B("trc", 1075, 330, 182, 60, "Tracing collector", "ghost", 14))
    n.append(B("leg", 881, 400, 376, 60, "Grey dashed: not built (owner decisions)", "note", 13))
    n.append(L("l_low", 10, 495, 1260, 215, "Batch, definitions and gates"))
    n.append(B("etl", 25, 545, 165, 120, "ETL intake\nsame rules as the API", "box", 14))
    n.append(B("qua", 205, 545, 170, 120, "Curated layer + quarantine\nbad rows kept, never silently fixed", "box", 14))
    n.append(B("sem", 397, 545, 194, 120, "Semantic layer v2.0\nfeeds policy, ETL rules and AI rules", "accent", 14))
    n.append(B("rego", 629, 545, 214, 120, "Generated policy (Rego)\nbuilt from the layer, tested in CI", "box", 14))
    n.append(B("ci", 881, 545, 376, 120, "CI gates\nlint, types, 181 tests, 97% coverage, secret scan, policy and semantic tests", "good", 14))
    e += [E("ops", "routes"), E("cli", "tok"), E("tok", "pol"), E("pol", "ctx"), E("ctx", "prod"), E("prod", "chk"),
          E("chk", "fb"), E("etl", "qua"), E("sem", "rego")]
    return {"name": "03-architecture-repo-2.0", "title": "Repo 2.0 as built: a modular monolith with one control point and ports", "nodes": n, "edges": e}


def ai_path():
    n, e = [], []
    xs = [30, 276, 522, 768, 1014]
    n.append(L("l1", 10, 10, 1260, 165, "Repo 1.0"))
    v1 = ["Request\nno identity needed", "Summary\necho of the first column", "Guardrail\nnot_enforced",
          "Audit line\nno actor, no correlation id", "Response used\nno approval step"]
    for i, t in enumerate(v1):
        n.append(B(f"a{i}", xs[i], 50, 226, 100, t, "bad", 16))
        if i:
            e.append(E(f"a{i-1}", f"a{i}"))
    n.append(L("l2", 10, 190, 1260, 520, "Repo 2.0"))
    ra = ["Request\nwith a bearer token", "Verify token\nelse 401", "Policy check\npersona, entity, purpose; else 403",
          "Key pattern\nelse 422", "Rate limit\nelse 429"]
    for i, t in enumerate(ra):
        n.append(B(f"b{i}", xs[i], 230, 226, 100, t, "box", 16))
        if i:
            e.append(E(f"b{i-1}", f"b{i}"))
    rb = ["Build context\nallowed fields only, text sanitised", "Producer\ndeterministic by default",
          "Check output\nschema, leaks, confidence", "Fallback, then abstain\nnever an invalid answer",
          "Register suggestion\nhuman approval required"]
    for i, t in enumerate(rb):
        n.append(B(f"c{i}", xs[4 - i], 380, 226, 110, t, "box", 16))
        if i:
            e.append(E(f"c{i-1}", f"c{i}"))
    e.append(E("b4", "c0"))
    n.append(B("d0", 30, 545, 226, 110, "Audit event\nhash-chained", "box", 16))
    n.append(B("d1", 276, 545, 226, 110, "Person decides\napprove or reject, once", "good", 16))
    n.append(B("d2", 522, 545, 226, 110, "A second decision\nrefused (409)", "box", 16))
    n.append(B("d3", 768, 545, 472, 110,
               "Every step leaves evidence\nwho asked, for which purpose, which data, which prompt version, what came back",
               "note", 15, "left"))
    e += [E("c4", "d0"), E("d0", "d1"), E("d1", "d2")]
    return {"name": "04-ai-request-path-v1-vs-v2", "title": "One AI summary request, before and after", "nodes": n, "edges": e}


def evidence_chain():
    n, e = [], []
    row = ["Claim\nin a document", "Citation\npath + SHA-256", "Evidence file\nevidence/<stage>/EVD-…",
           "MANIFEST row\nstep, command, time, operator", "Evidence index\n146 rows", "Rubric matrix\n36 sub-dimensions",
           "Readiness\ndecision"]
    for i, t in enumerate(row):
        n.append(B(f"r{i}", 10 + i * 183, 40, 160, 120, t, "accent" if i == 6 else "box", 15))
        if i:
            e.append(E(f"r{i-1}", f"r{i}"))
    n.append(L("ex", 10, 195, 1260, 225, "Example: one finding, end to end"))
    ex = [("F-17 (severity S1)\nrole header trusted", "bad"), ("Fix\nsigned token + policy engine", "box"),
          ("Tests\nunit tests; red team RT-02, RT-11", "box"), ("Proof\nbaseline answered 200; now 401", "good")]
    for i, (t, k) in enumerate(ex):
        n.append(B(f"x{i}", 30 + i * 313, 245, 280, 140, t, k, 16))
        if i:
            e.append(E(f"x{i-1}", f"x{i}"))
    n.append(L("ck", 10, 440, 1260, 270, "Automatic checks, re-runnable from the repository"))
    ck = [("Manifest check\n146 of 146 hashes match", "good"), ("Citation check\n203 of 203 match", "good"),
          ("Traceability check\nPASS on all four tests", "good"), ("Append-only\nolder files are superseded, never edited", "box")]
    for i, (t, k) in enumerate(ck):
        n.append(B(f"k{i}", 30 + i * 313, 490, 280, 130, t, k, 16))
    n.append(B("knote", 30, 640, 1220, 50,
               "Scripts: evidence/42-executive/EVD-R-03-verify-manifests.py; evidence/43-rubric-traceability/EVD-S-04-verify-r3.py",
               "note", 14, "left"))
    return {"name": "05-evidence-chain", "title": "How any claim traces to proof", "nodes": n, "edges": e}


def semantic():
    n, e = [], []
    n.append(L("md", 10, 10, 820, 125, "Markdown: for people"))
    for i, t in enumerate(["README", "Glossary", "Domain knowledge", "Enum violations", "Completeness"]):
        n.append(B(f"m{i}", 25 + i * 160, 52, 148, 62, t, "box", 15))
    n.append(L("ym", 10, 150, 820, 230, "YAML: definitions (source of truth)"))
    ys = ["Entities\n56 of 56 columns", "Status taxonomy", "Relationships\nand saga", "Business rules\nBR-01 to BR-13",
          "Metrics\nK1 to K10", "Access semantics\n8 personas", "AI context policy", "Workflow semantics"]
    for i, t in enumerate(ys):
        n.append(B(f"y{i}", 25 + (i % 4) * 200, 192 + (i // 4) * 92, 188, 78, t, "accent", 15))
    n.append(L("js", 10, 395, 400, 120, "JSON Schema: validation"))
    n.append(B("js1", 25, 437, 370, 62, "semantic-layer.schema.json\none definition per file", "box", 14))
    n.append(L("jn", 420, 395, 410, 120, "JSON: exchange"))
    n.append(B("jn1", 435, 437, 185, 62, "api-contract.json", "box", 14))
    n.append(B("jn2", 632, 437, 185, 62, "Generated layer\nsemantic-layer.json", "box", 13))
    n.append(L("ts", 10, 530, 820, 100, "Tests: integrity"))
    n.append(B("ts1", 25, 570, 390, 48, "23 layer tests", "good", 15))
    n.append(B("ts2", 427, 570, 390, 48, "5 conformance tests: app matches layer", "good", 15))
    n.append(L("use", 850, 10, 420, 620, "Used by"))
    us = ["Policy engine\naccess decisions", "ETL validation\nrules and taxonomy", "AI gateway\ncontext and decision rules",
          "Generated policy (Rego)", "A second model\nrebuild from the layer (Stage Q)"]
    for i, t in enumerate(us):
        n.append(B(f"u{i}", 870, 55 + i * 112, 380, 90, t, "box", 15))
    e.append(E("ym", "use"))
    n.append(B("qn", 10, 645, 1260, 70,
               "Stage Q on v1.0: a second model rebuilt a four-behaviour subset; safety gates 5 of 5, fidelity gates 0 of 2. The 8 gaps it exposed are specified in v2.0 but not yet re-tested.",
               "note", 14, "left"))
    return {"name": "06-semantic-layer", "title": "Semantic layer v2.0: business knowledge owned outside the code and the model", "nodes": n, "edges": e}


DIAGRAMS = [journey(), arch_v1(), arch_v2(), ai_path(), evidence_chain(), semantic()]
