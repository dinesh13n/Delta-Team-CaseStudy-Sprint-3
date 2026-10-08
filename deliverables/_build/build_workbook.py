"""Build deliverables/03-Evidence-Register.xlsx from the repository's evidence (run from the repository root).
Every figure is read from a repository file or stated with its source in the sheet."""

import csv
import pathlib
import re
import subprocess

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = pathlib.Path(".").resolve()
OUT = ROOT / "deliverables" / "03-Evidence-Register.xlsx"
GH = "https://github.com/dinesh13n/Delta-Team-CaseStudy-Sprint-3/blob/main/"
AS_OF = "2026-10-08"

PETROL, TEAL, LIGHT, AMBER = "0B3C49", "1F7A8C", "E8F1F2", "F2A541"
F = "Arial"
HDR_FILL = PatternFill("solid", fgColor=PETROL)
HDR_FONT = Font(name=F, bold=True, color="FFFFFF", size=10)
BODY = Font(name=F, size=10)
LINK = Font(name=F, size=10, color="1F5FA8", underline="single")
THIN = Side(style="thin", color="C5D6DA")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
GOOD = PatternFill("solid", fgColor="E5F3EB")
BAD = PatternFill("solid", fgColor="FCEBEA")
MID = PatternFill("solid", fgColor="FFF4E0")
GREY = PatternFill("solid", fgColor="EEF1F2")

STAGES = {
    "A": ("1 Understand", "Engagement mobilisation and read-only orientation"),
    "B": ("1 Understand", "Qualification, stakeholders and problem framing"),
    "C": ("1 Understand", "Baseline: KPIs, current state, root cause, behaviour"),
    "D": ("2 Define", "Semantic layer extraction"),
    "E": ("2 Define", "Intervention qualification and initial PRD"),
    "F": ("2 Define", "Target architecture, data and context, specs, traceability"),
    "G": ("2 Define", "Transformation and migration planning"),
    "H": ("3 Build", "Repo 2.0 modernisation and validation"),
    "I": ("3 Build", "Implementation PRD and delivery planning"),
    "J": ("3 Build", "Intelligence core, application, integration and agents"),
    "K": ("4 Prove", "Human control, security, privacy, responsible AI, governance"),
    "L": ("4 Prove", "TEVV and AI red teaming"),
    "M": ("4 Prove", "Hardening, resilience, incident response, BC/DR"),
    "N": ("4 Prove", "Release, observability, FinOps, vendor risk"),
    "O": ("5 Defend", "Outcome measurement, value leakage, benefits"),
    "P": ("5 Defend", "Operating model, handover, drift, scale, retirement"),
    "Q": ("5 Defend", "Model portability validation and demonstration"),
    "R": ("5 Defend", "Executive defence, as-built PRD, production evidence pack"),
    "S": ("6 Close-out", "Rubric traceability (Runbook 03)"),
    "T": ("6 Close-out", "Open questions and decisions (Runbook 04)"),
}


def sheet(wb, name, title, note, headers, rows, widths, link_col=None):
    ws = wb.create_sheet(name)
    ws["A1"] = title
    ws["A1"].font = Font(name=F, bold=True, size=14, color=PETROL)
    ws["A2"] = note
    ws["A2"].font = Font(name=F, italic=True, size=9, color="41545A")
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=3, column=c, value=h)
        cell.font, cell.fill, cell.border = HDR_FONT, HDR_FILL, BORDER
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    for r, row in enumerate(rows, 4):
        for c, v in enumerate(row, 1):
            cell = ws.cell(row=r, column=c, value=v)
            cell.font, cell.border, cell.alignment = BODY, BORDER, WRAP
            if link_col and c == link_col and isinstance(v, str) and v.startswith("http"):
                cell.hyperlink, cell.font, cell.value = v, LINK, "open"
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "B4"
    if rows:
        ws.auto_filter.ref = f"A3:{get_column_letter(len(headers))}{3 + len(rows)}"
    ws.row_dimensions[3].height = 30
    return ws


def colour_status(ws, col, first, last):
    rng = f"{col}{first}:{col}{last}"
    for words, fill in ((["FIXED", "PASS", "MET", "DECIDED", "RATIFIED", "Fixed"], GOOD),
                        (["PARTIAL", "CHANGED", "FIXED-IN-TREE", "Partial", "Changed", "ACCEPTED-PROPOSED"], MID),
                        (["FAIL", "NOT MET", "BLOCKED", "Not built", "Deferred", "DEFERRED"], BAD)):
        for w in words:
            ws.conditional_formatting.add(rng, FormulaRule(formula=[f'LEFT({col}{first},{len(w)})="{w}"'], fill=fill, stopIfTrue=True))


def md_rows(path, prefix):
    out = []
    for line in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("| " + prefix):
            out.append([c.strip().replace("**", "") for c in line.strip().strip("|").split("|")])
    return out


def git_counts(ref):
    files = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", "07-logistics-shipment-fleet-routing-ops"],
                           capture_output=True, text=True, check=True).stdout.split()
    areas = ["apps/api", "apps/web", "etl", "legacy", "tests", "scripts", "evaluation", "policy", "data", "docs",
             "observability", "infra", ".github"]
    f, lines = {}, {}
    for x in files:
        rel = x.split("/", 1)[1]
        a = next((a for a in areas if rel.startswith(a)), "other (root files)")
        f[a] = f.get(a, 0) + 1
        if x.endswith((".py", ".ts", ".rego", ".js", ".tf", ".sh")):
            n = subprocess.run(["git", "show", f"{ref}:{x}"], capture_output=True, text=True).stdout.count("\n")
            lines[a] = lines.get(a, 0) + n
    return f, lines


def main():
    wb = Workbook()
    wb.remove(wb.active)

    # ---------------- Read Me
    ws = wb.create_sheet("Read Me")
    rm = [
        ("Evidence Register: Brownfield to Repo 2.0 (logistics shipment, fleet, routing ops)", 14, True),
        (f"Delta-Team, AI-FDE Sprint 3. As of {AS_OF}. Built from the repository by deliverables/_build/build_workbook.py.", 10, False),
        ("", 10, False),
        ("How to use this workbook", 12, True),
        ("Start on Dashboard for the headline numbers. Every other sheet is the detail behind one tile.", 10, False),
        ("Each evidence row links to the file on GitHub (private repository; sign in to open). SHA-256 lets anyone check the file is unchanged.", 10, False),
        ("Filters are on every table. Green = done, amber = partial or changed, red = not met, blocked or deferred.", 10, False),
        ("", 10, False),
        ("Sheets", 12, True),
        ("Dashboard: headline numbers, all computed by formula from the sheets below.", 10, False),
        ("Repo 1.0 vs 2.0: capability by capability, what was delivered and what exists now, with findings and evidence.", 10, False),
        ("File Inventory: files and code lines per area, delivered commit 698e858 vs current main.", 10, False),
        ("Evidence Register: all 146 hash-registered evidence files, with stage, findings addressed, rubric criteria and link.", 10, False),
        ("Findings: the 62 baseline findings with severity, final disposition and rubric criteria.", 10, False),
        ("Red Team: the 12 attacks run against the delivered code and against Repo 2.0.", 10, False),
        ("KPIs: K1 to K10 before and after, with the honest reading.", 10, False),
        ("Rubric Coverage: per criterion summary and the 119 file-level matrix rows.", 10, False),
        ("Go-No-Go: the 12 readiness gates and their state today.", 10, False),
        ("Decisions: the 23 open questions and the operator's decision on each (Runbook 04).", 10, False),
        ("Risks: residual risks; none is accepted by a named person.", 10, False),
        ("Journey: the 20 stages (A to T) in six phases, with the commit that recorded them.", 10, False),
        ("Semantic Layer: every file in semantic-layer/ with its format and role.", 10, False),
        ("", 10, False),
        ("Evidence tags used in the source documents", 12, True),
        ("[VF] verified fact, read in a cited file   [INF] inference   [ASM] assumption   [UNK] unknown", 10, False),
        ("", 10, False),
        ("Limits stated up front", 12, True),
        ("No real AI model was called; all AI evidence uses the deterministic provider. Nothing is deployed. No business KPI moved; "
         "K1 to K8 are computed from a static synthetic fixture. One operator plus one agent built, tested and graded the work: no independent review.", 10, False),
    ]
    for i, (t, s, b) in enumerate(rm, 1):
        c = ws.cell(row=i, column=1, value=t)
        c.font = Font(name=F, size=s, bold=b, color=PETROL if b else "1B1B1B")
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.column_dimensions["A"].width = 140

    # ---------------- Repo 1.0 vs 2.0
    cmp_rows = [
        ("Version control and quick-start", "Not under version control; documented test command fails (exit 2, missing httpx); run command wrong",
         "Git with baseline tags; quick-start works; 181 passed, 1 skipped, 7 expected xfail", "Fixed", "F-01, F-02, F-03",
         "evidence/07-repo-assessment/EVD-C-02-quickstart-transcript.txt; evidence/15-modernization/EVD-H-02-quickstart-after.txt"),
        ("Tests and coverage", "3 tests (0 collected without httpx); coverage 45%", "181 tests plus 7 characterisation tests that pin old behaviour; 97% coverage (apps and etl)",
         "Fixed", "F-51", "evidence/34-after-kpis/EVD-O-01-after-kpis.json"),
        ("Dependencies and supply chain", "Versions pinned but no lockfile or hashes; no SBOM", "Hash-pinned lockfiles; SBOM (runtime 21, dev 58 components); 0 known vulnerabilities",
         "Fixed", "F-04, F-49", "evidence/27-hardening/EVD-M-01-pip-audit-runtime.json"),
        ("Identity", "Role read from a client-supplied X-User-Role header", "Signed bearer token (HS256, alg none rejected); JWKS verifier is a fail-closed stub; no identity provider",
         "Fixed (interim scheme)", "F-17", "evidence/26-tevv/EVD-L-03-redteam-v2.json (RT-02, RT-11)"),
        ("Authorisation", "Flat five-role allow-list including a persona from another domain; Rego file used by no code",
         "Deny-by-default policy engine driven by access-semantics.yaml (persona x entity x purpose, field mask or drop); Rego generated from it and tested in CI; scope narrowing declared but not enforced",
         "Fixed (scope partial)", "F-18, F-19, F-21", "evidence/26-tevv/EVD-L-03-redteam-v2.json (RT-03)"),
        ("Record lookup", "Scans every column; a miss returns the wrong record; REC-0001 key collides across entities",
         "Identifier must match the entity key pattern (422); a miss is 404 and audited; colliding rows quarantined", "Fixed", "F-30, F-31, F-32",
         "evidence/26-tevv/EVD-L-03-redteam-v2.json (RT-04 to RT-06)"),
        ("AI endpoint", "No authorisation; guardrail_status not_enforced; no output schema; str.format on untrusted text; output echoes the first column",
         "Authorised and rate-limited; allow-listed, sanitised context; schema and leak checks; fallback then abstain; suggest-only. Deterministic provider only",
         "Fixed (no real model)", "F-20, F-22, F-23, F-24, F-25, F-29", "evidence/26-tevv/EVD-L-02-final-eval-run.json; EVD-L-03 RT-01, RT-07 to RT-09, RT-12"),
        ("Human approval", "None", "Every suggestion registered; approve or reject once (409 on repeat); requester may approve their own (RA-04)",
         "Fixed (no four-eyes)", "F-26", "evidence/26-tevv/EVD-L-03-redteam-v2.json (RT-10)"),
        ("Model provenance and tokens", "Model id is a constant; token count fabricated", "Model, version, prompt version and config hash on every answer; token count labelled as an estimate",
         "Partial", "F-27, F-28", "docs/final-prd/final-ai-agent-baseline.md"),
        ("Audit", "Records time, action, details only; naive timestamps; local file", "Hash-chained events with actor, correlation id, tenant, resource and policy decision; verify endpoint; tampering detected; still a local file sink",
         "Partial", "F-43, F-44, F-45", "evidence/31-observability/EVD-N-02-reconstruction.json"),
        ("Data quality", "Duplicates, blank rows, impossible timestamps, polluted categories; ETL counts defects and discards them",
         "ETL validates with the API's rules; bad rows quarantined with a run id; curated layer; raw fixture left byte-identical", "Fixed",
         "F-33 to F-41, F-58, F-61, F-62", "evidence/11-data-context/EVD-D-02-enum-violations.csv"),
        ("Semantic layer", "None", "v2.0: 8 YAML definition files, JSON Schema, API contract, generated JSON, 23 layer tests and 5 conformance tests",
         "Fixed", "F-37", "evidence/11-data-context/EVD-D-06-semantic-layer-v2-hashes.json"),
        ("Observability", "Notes only; a third of events cannot be correlated", "Correlation id on every request; /metrics; KPI endpoint; no tracing, no collector, no alert recipients",
         "Partial", "F-42, F-46", "docs/31-observability"),
        ("CI and change control", "CI runs pytest only and had never run; no CONTRIBUTING, PR template or CODEOWNERS",
         "CI green on Python 3.11 and 3.14 (lint, types, coverage, secret scan, policy tests); PR template and CODEOWNERS; branch protection not enabled (GitHub reports it needs Pro for a private repository)",
         "Partial", "F-08, F-14, F-47", "evidence/15-modernization/EVD-R-02-ci-run-2-green.txt"),
        ("Secrets", "Password in source; credential-shaped values in .env.example", "Removed from the tree; secret scan in CI; history kept; repository private; values treated as compromised (OQ-19)",
         "Fixed in tree", "F-09, F-10, F-11, F-12, F-13", "evidence/15-modernization/EVD-H-03-secret-scan-history.json"),
        ("Infrastructure", "Terraform with one local_file resource that emits a credential", "Container recipe (Dockerfile, compose); Terraform provisions nothing; image never built; platform-neutral by decision (OQ-01)",
         "Deferred", "F-07, F-15, F-48", "docs/10-architecture/deployment-architecture.md"),
        ("Resilience", "No timeouts, retries or drills; incident runbook declares itself incomplete", "Timeout, retry, circuit breaker; 5 failure drills pass; backup restore shown on the fixture",
         "Fixed (repository level)", "F-56", "evidence/28-resilience/EVD-M-03-drills/summary.json"),
        ("Front end", "Portal claimed in docs; scaffold with a no-op lint", "Thin read-only operations view (OQ-06); browser test rewritten for it",
         "Changed", "F-05, F-06, F-52", "docs/20-application"),
        ("Business value", "No KPI data", "Proxy KPIs frozen and re-measured; unchanged by design; no monetary benefit verified",
         "Partial", "F-57", "evidence/34-after-kpis/EVD-O-01-after-kpis.json"),
        ("Encryption", "No TLS, at-rest or key management statement", "Unchanged; deferred until a platform exists", "Deferred", "F-16", "docs/42-executive/residual-risks.md"),
    ]
    ws = sheet(wb, "Repo 1.0 vs 2.0", "Repo 1.0 (as delivered) vs Repo 2.0 (as built)",
               "Repo 1.0 = commit 698e858 (delivered bytes). Repo 2.0 = main today. Status is the agent's reading of the finding dispositions; see Findings.",
               ["Area", "Repo 1.0 (as delivered)", "Repo 2.0 (as built)", "Status", "Findings", "Evidence"],
               cmp_rows, [24, 48, 60, 18, 20, 52])
    colour_status(ws, "D", 4, 3 + len(cmp_rows))

    # ---------------- File inventory
    f1, l1 = git_counts("698e858")
    f2, l2 = git_counts("HEAD")
    areas = sorted(set(f1) | set(f2), key=lambda a: -f2.get(a, 0))
    inv = [[a, f1.get(a, 0), f2.get(a, 0), None, l1.get(a, 0), l2.get(a, 0), None] for a in areas]
    ws = sheet(wb, "File Inventory", "Files and code lines per area: Repo 1.0 vs Repo 2.0",
               "Tracked files under 07-logistics-shipment-fleet-routing-ops/. Code lines = .py .ts .rego .js .tf .sh. Counted with git at build time.",
               ["Area", "Files 1.0", "Files 2.0", "Files change", "Code lines 1.0", "Code lines 2.0", "Lines change"], inv,
               [26, 12, 12, 13, 15, 15, 13])
    last = 3 + len(inv)
    for r in range(4, last + 1):
        ws[f"D{r}"] = f"=C{r}-B{r}"
        ws[f"G{r}"] = f"=F{r}-E{r}"
        for c in "DG":
            ws[f"{c}{r}"].font, ws[f"{c}{r}"].border = BODY, BORDER
    t = last + 1
    ws[f"A{t}"] = "Total"
    for c in "BCDEFG":
        ws[f"{c}{t}"] = f"=SUM({c}4:{c}{last})"
    for c in "ABCDEFG":
        ws[f"{c}{t}"].font, ws[f"{c}{t}"].fill, ws[f"{c}{t}"].border = Font(name=F, bold=True, size=10), GREY, BORDER
    ws.auto_filter.ref = None

    # ---------------- Evidence register
    idx = list(csv.DictReader(open(ROOT / "evidence/EVIDENCE-INDEX.csv", encoding="utf-8")))
    ev = []
    for r in idx:
        m = re.match(r"EVD-([A-Z])-", r["Evidence ID"])
        st = m.group(1) if m else "?"
        ph, sname = STAGES.get(st, ("?", "?"))
        ext = pathlib.Path(r["File path"]).suffix.lstrip(".") or "file"
        ev.append([r["Evidence ID"], st, sname, ph, r["File path"].split("/")[0], ext, r["Produced at"], r["Findings addressed"],
                   r["Rubric criteria"], r["Cited by"], r["SHA-256"], GH + "evidence/" + r["File path"]])
    ws = sheet(wb, "Evidence Register", f"Evidence register: {len(ev)} hash-registered files",
               "Source: evidence/EVIDENCE-INDEX.csv (derived from the per-folder MANIFEST.md files). Verified: every SHA-256 matches the file (EVD-R-03 verifier).",
               ["Evidence ID", "Stage", "Stage name", "Phase", "Folder", "Type", "Produced (UTC)", "Findings addressed", "Rubric criteria",
                "Cited by", "SHA-256", "Link"], ev, [44, 7, 34, 13, 22, 7, 20, 22, 12, 40, 22, 8], link_col=12)
    for r in range(4, 4 + len(ev)):
        ws[f"K{r}"].alignment = Alignment(vertical="top")

    # ---------------- Findings
    disp = {r["finding"]: r for r in csv.DictReader(open(ROOT / "evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv", encoding="utf-8"))}
    rub = {r["finding"]: r["rubric_criteria"] for r in csv.DictReader(open(ROOT / "evidence/43-rubric-traceability/EVD-S-02-finding-rubric-map.csv", encoding="utf-8"))}
    fr = [[k, v["severity"], v["title"], v["final_disposition"], rub.get(k, ""), v["evidence"], v["owner_role"], v["note"]] for k, v in disp.items()]
    ws = sheet(wb, "Findings", "62 baseline findings and their final disposition",
               "Source: evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv; rubric criteria from EVD-S-02. S1 = most severe.",
               ["Finding", "Severity", "Title", "Final disposition", "Rubric criteria", "Evidence", "Owner role", "Note"], fr,
               [9, 9, 60, 18, 12, 50, 14, 36])
    colour_status(ws, "D", 4, 3 + len(fr))

    # ---------------- Red team
    import json
    b = json.load(open(ROOT / "evidence/26-tevv/EVD-L-03-redteam-baseline.json"))
    v = json.load(open(ROOT / "evidence/26-tevv/EVD-L-03-redteam-v2.json"))
    vv = {a["id"]: a for a in v["attacks"]}
    rt = [[a["id"], a["finding"], a["goal"], a["response"]["status"], "Succeeded" if a["attack_succeeded"] else "Failed",
           vv[a["id"]]["response"]["status"], "Succeeded" if vv[a["id"]]["attack_succeeded"] else "Failed"] for a in b["attacks"]]
    ws = sheet(wb, "Red Team", "Red team: the same 12 attacks against Repo 1.0 and Repo 2.0",
               "Source: evidence/26-tevv/EVD-L-03-redteam-baseline.json and EVD-L-03-redteam-v2.json. Run by the builder, not an independent team.",
               ["Attack", "Finding", "Goal", "Repo 1.0 HTTP", "Repo 1.0 result", "Repo 2.0 HTTP", "Repo 2.0 result"], rt,
               [9, 11, 52, 13, 15, 13, 15])
    n = 3 + len(rt)
    for col in "EG":
        ws.conditional_formatting.add(f"{col}4:{col}{n}", CellIsRule(operator="equal", formula=['"Succeeded"'], fill=BAD))
        ws.conditional_formatting.add(f"{col}4:{col}{n}", CellIsRule(operator="equal", formula=['"Failed"'], fill=GOOD))
    ws[f"C{n+1}"] = "Attacks that succeeded"
    ws[f"E{n+1}"] = f'=COUNTIF(E4:E{n},"Succeeded")'
    ws[f"G{n+1}"] = f'=COUNTIF(G4:G{n},"Succeeded")'
    for c in "CEG":
        ws[f"{c}{n+1}"].font = Font(name=F, bold=True, size=10)

    # ---------------- KPIs
    kp = [("K1", "Latency p50 / p95 / max (ms)", "1667 / 13709 / 14999", "1667 / 13709 / 14999", "yes", "A column of the static fixture, not a service measurement"),
          ("K2", "Cost per event", "2.2451", "2.2451", "yes", "Static fixture"),
          ("K3", "Severe-event share", "39.6%", "39.6%", "yes", "Static fixture"),
          ("K4", "Correlation completeness (source stream)", "33.6%", "33.6%", "yes", "The producer still emits no id (F-42)"),
          ("K5", "Declared AI tokens", "904,432", "904,432", "yes", "Declared by the dataset"),
          ("K6", "Retries min / mean / max", "51 / 2508.5 / 4995", "51 / 2508.5 / 4995", "yes", "Static fixture"),
          ("K7", "Duplicate keys (raw layer)", "18", "18", "yes", "Seeded defects stay in the raw files; quarantined downstream"),
          ("K8", "Incomplete rows (raw layer)", "6", "6", "yes", "Seeded defects stay in the raw files; quarantined downstream"),
          ("K9", "Tests", "3 of 3 pass (0 collected without httpx)", "181 passed, 7 expected xfail (170 at Stage O)", "n/a", "Engineering health, not operations"),
          ("K10", "Coverage", "45%", "97% (apps and etl)", "n/a", "Engineering health")]
    ws = sheet(wb, "KPIs", "KPIs K1 to K10: before and after",
               "Source: docs/34-after-kpis/after-intervention-kpi-sheet.md; evidence/34-after-kpis/EVD-O-01-after-kpis.json. K9 re-run on 2026-10-08. None of this is a business outcome.",
               ["KPI", "Measure", "Baseline", "After", "Equal?", "Reading"], [list(x) for x in kp], [7, 38, 30, 34, 9, 56])

    # ---------------- Rubric
    summ = [("R1", "As-Is understanding", 20, 6, 1, 0, 0), ("R2", "Repo 2.0 design", 25, 5, 4, 0, 0),
            ("R3", "Governance, risk, security", 20, 5, 2, 1, 1), ("R4", "PRD and working application", 25, 4, 1, 0, 1),
            ("R5", "Presentation and defence", 10, 4, 1, 0, 0)]
    mat = list(csv.DictReader(open(ROOT / "evidence/43-rubric-traceability/EVD-S-01-coverage-matrix.csv", encoding="utf-8")))
    ws = sheet(wb, "Rubric Coverage", "Rubric coverage: sub-dimensions per criterion",
               "Source: docs/43-rubric-traceability/readiness-assessment.md (counts) and EVD-S-01-coverage-matrix.csv (rows below). Index = (MET + 0.5 x PARTIAL) / sub-dimensions. It measures evidence completeness, not marks.",
               ["Criterion", "Name", "Marks", "MET", "PARTIAL", "NOT MET", "BLOCKED", "Sub-dimensions", "Coverage index"],
               [list(x) + [None, None] for x in summ], [11, 30, 8, 8, 9, 9, 10, 15, 15])
    for r in range(4, 9):
        ws[f"H{r}"] = f"=SUM(D{r}:G{r})"
        ws[f"I{r}"] = f"=IF(H{r}=0,0,(D{r}+0.5*E{r})/H{r})"
        ws[f"I{r}"].number_format = "0.00"
        for c in "HI":
            ws[f"{c}{r}"].font, ws[f"{c}{r}"].border = BODY, BORDER
    ws["A9"] = "Total"
    for c in "CDEFGH":
        ws[f"{c}9"] = f"=SUM({c}4:{c}8)"
    for c in "ABCDEFGHI":
        ws[f"{c}9"].font, ws[f"{c}9"].fill = Font(name=F, bold=True, size=10), GREY
    ws.auto_filter.ref = None
    ws["A11"] = "File-level matrix rows (each row: a sub-dimension, its status, and one file that evidences it)"
    ws["A11"].font = Font(name=F, bold=True, size=11, color=PETROL)
    for c, h in enumerate(["Criterion", "Sub-dimension", "Status", "Evidence file", "SHA-256"], 1):
        cell = ws.cell(row=12, column=c, value=h)
        cell.font, cell.fill, cell.border = HDR_FONT, HDR_FILL, BORDER
    for i, r in enumerate(mat, 13):
        for c, val in enumerate([r["criterion"], r["sub_dimension"], r["status"], r["resolved_file"], r["sha256"]], 1):
            cell = ws.cell(row=i, column=c, value=val)
            cell.font, cell.border, cell.alignment = BODY, BORDER, WRAP
    colour_status(ws, "C", 13, 12 + len(mat))
    ws.column_dimensions["D"].width = 60
    ws.column_dimensions["E"].width = 22

    # ---------------- Go / no-go
    gates = [("G1", "Tests pass, coverage at or above floor", "yes", "PASS", "181 passed, 97% (apps and etl); CI green on 3.11 and 3.14"),
             ("G2", "Evaluation at thresholds", "yes", "PASS (deterministic provider only)", "192 cases, 0 failures; real model untested"),
             ("G3", "No original defect re-exploitable", "yes", "PASS", "0 of 12 attacks succeed"),
             ("G4", "No known critical or high dependency vulnerability", "yes", "PASS", "pip-audit: 0"),
             ("G5", "Audit tamper-evident; reconstruction shown", "yes", "PASS (author-run)", "EVD-N-02"),
             ("G6", "Backup restore shown", "yes", "PASS (repository level)", "EVD-N-03"),
             ("G7", "Rollback defined and rehearsed", "yes", "PARTIAL", "Defined; no cutover exists"),
             ("G8", "Alerts routed to named humans", "yes", "FAIL", "No collector, no recipients"),
             ("G9", "Named approver and risk owners", "yes", "FAIL", "Operator approves under provisional authority (OQ-05); 0 of 12 risk acceptances signed"),
             ("G10", "Platform and identity provider exist", "production", "FAIL", "Platform-neutral by decision (OQ-01); IdP deferred (OQ-07)"),
             ("G11", "Independent evidence review", "yes", "FAIL", "Builder and grader are the same agent"),
             ("G12", "Compliance resolved", "real data", "FAIL", "No regime named (OQ-04); candidate obligations unvalidated")]
    ws = sheet(wb, "Go-No-Go", "Readiness gates G1 to G12",
               "Source: docs/30-release/go-no-go-criteria.md (fixed before the decision) and docs/42-executive/production-readiness-decision.md; G1 and G9 updated to today. Pilot needs G1-G7; production needs G8-G12 as well.",
               ["Gate", "Criterion", "Mandatory for", "State", "Basis"], [list(g) for g in gates], [8, 46, 14, 30, 64])
    colour_status(ws, "D", 4, 15)

    # ---------------- Decisions
    dec = [r[:4] + [r[5] if len(r) > 5 else ""] for r in md_rows(ROOT / "docs/44-decisions/open-questions-register-v2.md", "OQ-")]
    ws = sheet(wb, "Decisions", "23 open questions: the operator's decisions (Runbook 04)",
               "Source: docs/44-decisions/open-questions-register-v2.md; record evidence/44-decisions/EVD-T-01-operator-decision-record.json. One person holds every role, so these are provisional.",
               ["Question", "Subject", "Status", "Decision", "What it means now"], dec, [9, 26, 12, 62, 62])
    colour_status(ws, "C", 4, 3 + len(dec))

    # ---------------- Risks
    risks = [("RA-07 / DEBT-11", "Credential-shaped values remain in git history", "High", "Repository owner + Security", "Repository private; values treated as compromised; history not rewritten (OQ-19)"),
             ("RA-01", "Regulatory scope unresolved", "High for real data", "Sponsor + Compliance", "No regime named (OQ-04); pilot on synthetic data only"),
             ("RA-06 / TEVV-R-01", "Builder and grader are the same agent; no independent review", "High", "Release approver", "Blocks an unconditional GO; ask 6 to the CTO"),
             ("RA-02", "HS256 shared-secret identity; JWKS stub", "High if networked", "Security", "Interim scheme kept (OQ-07 deferred)"),
             ("RA-09 / TEVV-R-02", "Real model untested; thresholds valid only for the deterministic provider", "High before a model", "AI governance", "No model by decision (OQ-02)"),
             ("Stage Q", "Model portability partly shown: safety yes, AI-output fidelity no", "Medium", "AI governance", "8 gaps specified in semantic layer v2.0; not re-tested"),
             ("RA-04 / HC-R-01", "No four-eyes: requester can approve their own suggestion", "Medium", "Product", "Before any action integration"),
             ("RA-12 / DEBT-01", "Branch protection not enabled on main", "Medium", "Repository owner", "GitHub reports the feature needs Pro for a private repository"),
             ("DEBT-06 / F-48", "Terraform provisions nothing; image never built", "Medium", "Platform", "Platform-neutral by decision (OQ-01)"),
             ("N-R", "No tracing; collector and alerts never run; no recipients", "Medium", "SRE", "Before deployment"),
             ("DEBT-04", "Audit sink is a local file; deletion of the tip cannot be prevented", "Medium", "Platform", "Needs a platform"),
             ("DEBT-08 / DEBT-09", "BR-04 violated by 354 of 354 rows; actual above declared weight on 171 rows", "Medium", "Business owner", "Meaning unknown"),
             ("F-42", "1,992 of 3,000 historical events lack a usable correlation id", "Low (history)", "Data owner", "New requests carry an id"),
             ("Value", "No business KPI measurable; NPV negative at fixture volume", "Medium", "Sponsor", "Measure review time first"),
             ("RA-03, 05, 08, 10, 11", "Purpose defaulting; approvals never expire; stale GPS undetectable; retention undefined; in-memory rate limit", "Low to Medium", "See risk-acceptance register", "")]
    ws = sheet(wb, "Risks", "Residual risks (none accepted by a named person)",
               "Source: docs/42-executive/residual-risks.md and docs/25-governance/risk-acceptance-register.md, with the Runbook 04 decisions applied. Owners are roles.",
               ["ID", "Risk", "Severity (agent view)", "Owner role", "Current position"], [list(x) for x in risks], [20, 60, 18, 26, 56])

    # ---------------- Journey
    commit = {"A": "698e858, f1b7809", "B": "f1b7809", **{k: "4c84af1" for k in "CDEFGHIJKLMNOP"}, "Q": "217afc5, e13758b, ab37ec8",
              "R": "c7d94de, 96d5522", "S": "1dcf6e8", "T": "1cde803"}
    count = {}
    for r in ev:
        count[r[1]] = count.get(r[1], 0) + 1
    jr = [[k, v[0], v[1], commit.get(k, ""), count.get(k, 0)] for k, v in STAGES.items()]
    jr.append(["D (v2)", "6 Close-out", "Semantic layer aligned to semantic-layer-build.txt", "ad230eb", "(in D)"])
    ws = sheet(wb, "Journey", "Delivery journey: 20 stages in six phases",
               "Stages A to R come from runbook/02-TRANSFORMATION-RUNBOOK.md; S and T are Runbooks 03 and 04. Evidence count = rows in the Evidence Register for that stage letter.",
               ["Stage", "Phase", "Stage name", "Commit(s)", "Evidence files"], jr, [10, 14, 60, 26, 14])

    # ---------------- Semantic layer
    sl = []
    roles = {".md": "Markdown: for people", ".yaml": "YAML: definition", ".json": "JSON / JSON Schema", ".py": "Generator or test"}
    for p in sorted((ROOT / "semantic-layer").rglob("*")):
        if p.is_file() and "__pycache__" not in p.parts and p.name != ".gitkeep":
            rel = str(p.relative_to(ROOT))
            sl.append([rel, roles.get(p.suffix, p.suffix), p.stat().st_size, GH + rel])
    ws = sheet(wb, "Semantic Layer", "Semantic layer v2.0: files",
               "The model-independent definition of the domain. Hashes recorded in evidence/11-data-context/EVD-D-06-semantic-layer-v2-hashes.json.",
               ["File", "Format and role", "Bytes", "Link"], sl, [60, 26, 10, 8], link_col=4)

    # ---------------- Dashboard (first sheet)
    ds = wb.create_sheet("Dashboard", 1)
    ds["A1"] = "Dashboard: Repo 1.0 → Repo 2.0, in numbers"
    ds["A1"].font = Font(name=F, bold=True, size=16, color=PETROL)
    ds["A2"] = f"Every value below is a formula over the detail sheets. As of {AS_OF}."
    ds["A2"].font = Font(name=F, italic=True, size=9, color="41545A")
    nev, nfi = 3 + len(ev), 3 + len(fr)
    tiles = [
        ("Evidence", [("Hash-registered evidence files", f"=COUNTA('Evidence Register'!A4:A{nev})"),
                      ("Files touching R1", f"=COUNTIF('Evidence Register'!I4:I{nev},\"*R1*\")"),
                      ("Files touching R2", f"=COUNTIF('Evidence Register'!I4:I{nev},\"*R2*\")"),
                      ("Files touching R3", f"=COUNTIF('Evidence Register'!I4:I{nev},\"*R3*\")"),
                      ("Files touching R4", f"=COUNTIF('Evidence Register'!I4:I{nev},\"*R4*\")"),
                      ("Files touching R5", f"=COUNTIF('Evidence Register'!I4:I{nev},\"*R5*\")")]),
        ("Findings", [("Baseline findings", f"=COUNTA(Findings!A4:A{nfi})"),
                      ("Severity S1", f"=COUNTIF(Findings!B4:B{nfi},\"S1\")"),
                      ("FIXED", f"=COUNTIF(Findings!D4:D{nfi},\"FIXED\")"),
                      ("FIXED-IN-TREE", f"=COUNTIF(Findings!D4:D{nfi},\"FIXED-IN-TREE\")"),
                      ("PARTIAL", f"=COUNTIF(Findings!D4:D{nfi},\"PARTIAL\")"),
                      ("CHANGED", f"=COUNTIF(Findings!D4:D{nfi},\"CHANGED\")"),
                      ("DEFERRED", f"=COUNTIF(Findings!D4:D{nfi},\"DEFERRED\")"),
                      ("ACCEPTED-PROPOSED", f"=COUNTIF(Findings!D4:D{nfi},\"ACCEPTED-PROPOSED\")")]),
        ("Proof", [("Attacks that succeed on Repo 1.0 (of 12)", "=COUNTIF('Red Team'!E4:E15,\"Succeeded\")"),
                   ("Attacks that succeed on Repo 2.0 (of 12)", "=COUNTIF('Red Team'!G4:G15,\"Succeeded\")"),
                   ("Readiness gates passed (of 12)", "=COUNTIF('Go-No-Go'!D4:D15,\"PASS*\")"),
                   ("Readiness gates failed", "=COUNTIF('Go-No-Go'!D4:D15,\"FAIL*\")"),
                   ("Tracked files in the application folder, 1.0 → 2.0", "=TEXT('File Inventory'!B" + str(4 + len(inv)) + ",\"0\")&\" → \"&TEXT('File Inventory'!C" + str(4 + len(inv)) + ",\"0\")")]),
        ("Governance", [("Open questions decided or ratified", f"=COUNTIF(Decisions!C4:C{3 + len(dec)},\"DECIDED\")+COUNTIF(Decisions!C4:C{3 + len(dec)},\"RATIFIED\")"),
                        ("Open questions deferred", f"=COUNTIF(Decisions!C4:C{3 + len(dec)},\"DEFERRED\")"),
                        ("Rubric sub-dimensions", "='Rubric Coverage'!H9"),
                        ("Sub-dimensions MET", "='Rubric Coverage'!D9"),
                        ("Sub-dimensions NOT MET or BLOCKED", "='Rubric Coverage'!F9+'Rubric Coverage'!G9"),
                        ("Risk acceptances signed by a named person", 0)]),
    ]
    row = 4
    for head, items in tiles:
        ds.cell(row=row, column=1, value=head).font = Font(name=F, bold=True, size=12, color="FFFFFF")
        ds.cell(row=row, column=1).fill = PatternFill("solid", fgColor=TEAL)
        ds.cell(row=row, column=2).fill = PatternFill("solid", fgColor=TEAL)
        row += 1
        for label, f in items:
            a = ds.cell(row=row, column=1, value=label)
            b = ds.cell(row=row, column=2, value=f)
            a.font, b.font = BODY, Font(name=F, bold=True, size=12, color=PETROL)
            a.border = b.border = BORDER
            b.alignment = Alignment(horizontal="right")
            if label.startswith("Risk acceptances"):
                ds.cell(row=row, column=3, value="Input: 0 of 12 (docs/25-governance/risk-acceptance-register.md)").font = Font(name=F, italic=True, size=9, color="41545A")
            row += 1
        row += 1
    ds.column_dimensions["A"].width = 46
    ds.column_dimensions["B"].width = 16
    ds.column_dimensions["C"].width = 60
    wb.move_sheet("Dashboard", offset=-(wb.sheetnames.index("Dashboard") - 1))
    for w in wb.worksheets:
        w.sheet_view.showGridLines = False if w.title in ("Read Me", "Dashboard") else True
    wb.save(OUT)
    print("wrote", OUT, "evidence rows", len(ev), "findings", len(fr), "decisions", len(dec))


if __name__ == "__main__":
    main()
