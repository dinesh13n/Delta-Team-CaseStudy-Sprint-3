import json,csv,sys,collections,glob
sys.path.insert(0,"/tmp/claude-0/-home-claude-delta-team-casestudy-sprint-3/7b5a429d-b1d0-5503-bea8-f837bfd1a87c/scratchpad/r3")
from common import *; from matrix_rows import ROWS
res=json.load(open("/tmp/r3_resolve.json"))
by=collections.defaultdict(list)
for r in res: by[(r["criterion"],r["sub"])]+= [(r["named"],f) for f in r["resolved"]]
fix={"ADR-00XX":sorted(glob.glob("docs/10-architecture/adrs/ADR-000[2-9]*")+glob.glob("docs/10-architecture/adrs/ADR-0010*")),
     "ADR-0001":["07-logistics-shipment-fleet-routing-ops/docs/ADR/0001-partial-modernization.md"],
     "semantic-layer/*":["semantic-layer/README.md","semantic-layer/entities.yaml","semantic-layer/access-semantics.yaml","semantic-layer/business-rules.yaml","semantic-layer/ai-context-policy.yaml"],
     "CODEOWNERS":[".github/CODEOWNERS"]}
import os; os.chdir(ROOT)
for r in res:
    if not r["resolved"] and r["named"] in fix: by[(r["criterion"],r["sub"])]+=[(r["named"],f) for f in fix[r["named"]]]
cnt=collections.Counter(r[2] for r in ROWS)
tot=collections.Counter((r[0],r[2]) for r in ROWS)
rows_csv=[]
md=[]
cur=None
for crit,sub,st,why in ROWS:
    ev=by[(crit,sub)]
    # de-dup paths
    seen=[];[seen.append(f) for _,f in ev if f not in seen]
    for f in seen: rows_csv.append([crit,sub,st,f,sha(f)])
    show=", ".join(f"`{f}`" for f in seen[:3])+(f" (+{len(seen)-3} more)" if len(seen)>3 else "")
    md.append(f"| {crit} | {sub} | **{st}** | {len(seen)} | {show} | {why} |")
assert all(by[(c,s)] for c,s,_,_ in ROWS), [ (c,s) for c,s,_,_ in ROWS if not by[(c,s)]]
csvp="evidence/43-rubric-traceability/EVD-S-01-coverage-matrix.csv"
with open(csvp,"w",newline="") as f:
    w=csv.writer(f,lineterminator="\n"); w.writerow(["criterion","sub_dimension","status","resolved_file","sha256"]); w.writerows(rows_csv)
summ="\n".join(f"| {c} | "+" | ".join(str(tot[(c,s)]) for s in ("MET","PARTIAL","NOT MET","BLOCKED"))+f" | {sum(tot[(c,s)] for s in ('MET','PARTIAL','NOT MET','BLOCKED'))} |" for c in ("R1","R2","R3","R4","R5"))
doc="# Rubric coverage matrix (verified)\n\n"+hdr("03-1 (Doc 03 section 2)","PROVISIONAL: every named artifact resolves; acceptance standards judged by the author","EVD-S-01-coverage-matrix.csv; docs/ and evidence/ trees at commit after ab37ec8","OQ-01..05, OQ-18, OQ-19 (see blocker-status.md)","Statuses are the author's judgement against the standard in Document 03; an independent reviewer may rate lower")+f"""
## Method
1. Every artifact named in the \"Primary evidence\" column of Document 03 section 2 (92 names, 36 sub-dimensions) was resolved to files in the repository by name or pattern. All 92 resolve; 4 needed a manual path (`ADR-00XX` is ADR-0002..0010, `ADR-0001` is in the app subtree, `semantic-layer/*` and `CODEOWNERS` are at repo paths). [VF] `EVD-S-01-coverage-matrix.csv` lists each resolved file with its SHA-256.
2. A name resolving is **not** the same as the standard being met. Each sub-dimension was then judged against its acceptance standard, using the stage gates and the checks quoted in the reason. Where a check was cheap to run, it was run in this step (debt register coverage of finding IDs; AI mentions in the problem statement).
3. Statuses: **MET** the standard is met by the evidence; **PARTIAL** met in part, the gap is stated; **NOT MET** the standard is not met and could be; **BLOCKED** an external decision prevents it (Document 03 section 3).

## Result
| Criterion | MET | PARTIAL | NOT MET | BLOCKED | Sub-dimensions |
|---|---|---|---|---|---|
{summ}
| **Total** | {cnt['MET']} | {cnt['PARTIAL']} | {cnt['NOT MET']} | {cnt['BLOCKED']} | {len(ROWS)} |

## Corrections made while resolving
- `docs/07-repo-assessment/technical-debt-register.md` covered 60 of 62 finding IDs; F-61 and F-62 were added so the Document 03 standard (\"cross-references all finding IDs\") holds. [VF]
- Document 03 says 12 discovery artifacts; there are 13. Document 03 says 57 findings; there are 62. Both are stated as found, not hidden.

## Matrix
| Rubric | Sub-dimension | Status | Files | Primary evidence (first 3) | Why |
|---|---|---|---|---|---|
"""+"\n".join(md)+"\n"
open("docs/43-rubric-traceability/rubric-coverage-matrix.md","w").write(doc)
print(cnt, len(rows_csv))
for c in ("R1","R2","R3","R4","R5"): print(c,{s:tot[(c,s)] for s in ("MET","PARTIAL","NOT MET","BLOCKED")})
