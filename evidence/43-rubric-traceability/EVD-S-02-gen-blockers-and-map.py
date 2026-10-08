import sys,re,csv,collections,os
sys.path.insert(0,"/tmp/claude-0/-home-claude-delta-team-casestudy-sprint-3/7b5a429d-b1d0-5503-bea8-f837bfd1a87c/scratchpad/r3")
from common import *; os.chdir(ROOT)
B=[
("B-1","R4","Working AI capabilities","OPEN (blocked)","OQ-02, OQ-03 open","Fallback only partly applied: the governed AI workflow is built and scored (192 of 192 cases, deterministic provider). The fallback asked for a locally runnable open-weights model; none was run. Stated, not hidden.","evidence/26-tevv/EVD-L-02-final-eval-run.json; docs/42-executive/ai-decision-defence.md"),
("B-2","R2, R4","Second-model comparison","PARTLY ADDRESSED","OQ-02 open","Performed once as a *builder* comparison (claude-sonnet-5-5 vs claude-haiku-5-5, same vendor, subset, one run), not simulated. Model B fails 2 of 8 pre-registered gates. A second model *provider* comparison is not possible: no provider is configured.","docs/40-scale/model-comparison.md; evidence/40-scale/EVD-Q-06-comparison.csv"),
("B-3","R3","Compliance obligations mapping","OPEN; fallback applied","OQ-04 open","Candidate obligations set written and labelled an unvalidated assumption, with a validation plan; recorded as risk acceptance RA-01, unsigned.","docs/25-governance/compliance-obligations.md; docs/42-executive/residual-risks.md"),
("B-4","R2, R3","IaC, identity, secrets, deployment","OPEN; fallback partly applied","OQ-01, OQ-07 open","Platform-neutral design (ADR-0009), container image, compose file and HS256 interim identity (ADR-0004). `infra/terraform` provisions nothing (M-X2 NOT MET). No worked reference implementation on a named platform.","docs/10-architecture/adrs/ADR-0009-platform-neutral-deployment.md; docs/28-resilience/stage-m-gate.md"),
("B-5","R1, R4","Business KPI baseline","OPEN; fallback applied","OQ-08 ASSUMED","Declared proxies from `events.jsonl` and `ai_invocations.csv`, each labelled a proxy with limits; the sponsor never confirmed them. No business metric moved.","docs/04-baseline-kpis/; docs/34-after-kpis/"),
("B-6","R4","ROI / NPV / benefits","OPEN; fallback applied","OQ-09 open","Parameterised model in analyst-hours with sensitivity: NPV -970 h expected, +5,525 h optimistic, -2,466 h downside. Verified monetary benefit is nil. No single ROI figure is presented as a measurement.","docs/36-benefits/"),
("B-7","R4","End-to-end workflow with a UI","RESOLVED (provisional)","OQ-06 resolved provisionally","A thin read-only operations view was built and passes 10 of 10 browser checks. The Angular portal was rejected. The end-to-end demonstration is correspondingly lighter.","runbook/04-OPEN-QUESTIONS-FINAL-REVISION.md; docs/20-application/"),
("B-8","R3","Named approvers for every gate","OPEN","OQ-05 open","Every gate is self-signed and PROVISIONAL; 0 of 12 risk acceptances signed; owners are roles. Gate G9 FAIL.","docs/42-executive/final-gate.md; docs/42-executive/residual-risks.md"),
("B-9","R3","Vendor and concentration risk","PARTLY ADDRESSED","OQ-01, OQ-02 open","Vendor scorecards, concentration and portability assessments exist, but there is no contracted vendor; they describe candidates. Portability now has one same-vendor test behind it.","docs/33-vendor-risk/"),
("B-10","R5","Demonstration","PARTLY ADDRESSED","OQ-16, OQ-17 PROPOSED","Local, offline, deterministic demo (28 s of beats); proposed 10 minutes plus 5 questions. Rehearsed by the author only; no audience, no recording of a person.","docs/42-executive/demo-day-script.md; evidence/42-executive/EVD-Q-03-demo-rehearsal.txt"),
("B-11","R2","Data remediation","RESOLVED (provisional)","OQ-14 provisional; OQ-22 resolved","A derived curated layer with quarantine; the fixture stays immutable and the original `sanity_check.py` assertions are retained.","docs/11-data-context/; docs/16-repo-validation/"),
("B-12","R3","Agentic engineering","OPEN; decision recorded","OQ-18 open","Step J6 recorded as not applicable: no agent runtime was built; the `ai_agent` persona is a read-only suggester.","docs/22-agentic-engineering/"),
("B-13","R1, R3","Secret history exposure","OPEN","OQ-19 open","History was not rewritten and nothing was revoked. The repository is now private, which narrows exposure but does not remove the credentials from history or from any earlier clone. 4 findings are FIXED-IN-TREE only.","docs/42-executive/residual-risks.md (GOV-07)"),
]
for b in B:
    for p in [x.strip() for x in b[6].replace("","").split(";")]:
        q=p.split(" (")[0]
        assert os.path.exists(q), (b[0],q)
cnt=collections.Counter(b[3].split(";")[0].split(" (")[0] for b in B)
rows="\n".join(f"| {b[0]} | {b[1]} | {b[2]} | **{b[3]}** | {b[4]} | {b[5]} | {b[6]} |" for b in B)
doc="# Blocker status (Document 03 section 3, re-stated)\n\n"+hdr("03-2 (Doc 03 section 3)","PROVISIONAL","runbook/04-OPEN-QUESTIONS-FINAL-REVISION.md; docs/42-executive/final-gate.md; stage gates","13 open questions, 0 formally accepted","Statuses reflect the state on 2026-10-08; none of the open questions has an owner decision")+f"""
Document 03 listed 13 things the artifacts could not satisfy without an outside decision. This is where each stands after Runbooks 01 and 02. Counts: {dict(cnt)}.

| ID | Rubric | Blocker | Status now | Governing OQ | What was done and what was not | Evidence |
|---|---|---|---|---|---|---|
{rows}

## What changed since Document 03 was written
- **Resolved provisionally (2):** B-7 (thin view), B-11 (derived layer). Provisional means the operator decided; no business owner confirmed.
- **Partly addressed (3):** B-2, B-9, B-10.
- **Fallback applied but blocker remains (5):** B-3, B-4, B-5, B-6, B-1 (partly).
- **Untouched by anything we can do alone (3):** B-8 (named approvers), B-12, B-13. These need a person with authority.

## What would move the score most
Document 03 section 3.3 says R1, most of R2, most of R3 and R5 can be satisfied from the delivered artifacts alone. The blockers that still cost marks are B-1 (R4), B-8 and B-3 (R3), B-4 (R2). Only B-8 is cheap: naming approvers and signing the existing 12 risk acceptances needs people, not work.
"""
open("docs/43-rubric-traceability/blocker-status.md","w").write(doc)

# finding -> rubric map
disp={r["finding"]:r for r in csv.DictReader(open("evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv"))}
reg={}
for l in open("docs/07-repo-assessment/technical-debt-register.md"):
    c=[x.strip() for x in l.strip().strip("|").split("|")]
    if len(c)>=4 and re.fullmatch(r"F-\d\d",c[0]): reg[c[0]]=["R"+n for n in re.findall(r"(\d)",c[3])]
assert len(reg)==62==len(disp)
cnt=collections.Counter(); dd=collections.defaultdict(collections.Counter)
for f,rs in reg.items():
    for r in rs: cnt[r]+=1; dd[r][disp[f]["final_disposition"]]+=1
order=["FIXED","FIXED-IN-TREE","PARTIAL","CHANGED","DEFERRED","ACCEPTED-PROPOSED"]
t="\n".join(f"| {r} | {cnt[r]} | "+" | ".join(str(dd[r][o]) for o in order)+" |" for r in ("R1","R2","R3","R4"))
lst="\n".join(f"| {f} | {disp[f]['severity']} | {', '.join(reg[f])} | {disp[f]['final_disposition']} | {disp[f]['title']} |" for f in sorted(reg))
with open("evidence/43-rubric-traceability/EVD-S-02-finding-rubric-map.csv","w",newline="") as fh:
    w=csv.writer(fh,lineterminator="\n"); w.writerow(["finding","severity","rubric_criteria","final_disposition","title"])
    for f in sorted(reg): w.writerow([f,disp[f]["severity"],";".join(reg[f]),disp[f]["final_disposition"],disp[f]["title"]])
doc2="# Finding to rubric map (62 findings)\n\n"+hdr("03-2 (Doc 03 section 4)","PROVISIONAL","docs/07-repo-assessment/technical-debt-register.md (rubric column); EVD-F-04b; EVD-S-02-finding-rubric-map.csv","None beyond the open questions","The rubric column is the author's own assignment from Stage C")+f"""
Document 03 section 4 gave counts for 57 findings (R1 19, R2 20, R3 31, R4 7). The register now has 62 findings (F-58..F-62 were found later). Counts below are from the register's own rubric column; a finding can serve more than one criterion. R5 has no findings: its evidence is the presentation of R1 to R4.

| Rubric | Findings | FIXED | FIXED-IN-TREE | PARTIAL | CHANGED | DEFERRED | ACCEPTED-PROPOSED |
|---|---|---|---|---|---|---|---|
{t}

**The observation in Document 03 still holds, more strongly.** 31 findings feed R3 (20 marks) and 6 feed R4 (25 marks). The defects are in governance; the marks are in execution. The repository ended with the governance findings mostly fixed (the R3 row above) but with R4's weak points being the two things that need outside input: a real model (B-1) and an end-to-end workflow a person has watched (B-7, B-10). [INF]

The numbers differ from Document 03 because it listed IDs per criterion by hand and the register assigns a criterion per finding; both are stated so neither is silently preferred. [VF]

## All 62
| Finding | Sev | Rubric | Final disposition | Title |
|---|---|---|---|---|
{lst}
"""
open("docs/43-rubric-traceability/finding-rubric-map.md","w").write(doc2)
print(dict(cnt))
