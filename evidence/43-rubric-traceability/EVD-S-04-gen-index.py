import re,csv,glob,os,hashlib,collections,sys
ROOT="/home/claude/delta-team-casestudy-sprint-3"; os.chdir(ROOT)
STAGE_DEFAULT={"A":"R1","B":"R1","C":"R1","D":"R2","E":"R4","F":"R4","G":"R3","H":"R2","I":"R4","J":"R2;R4","K":"R3","L":"R3;R4","M":"R2","N":"R3","O":"R1","P":"R3","Q":"R2;R5","R":"R5","S":"R5"}
# matrix-derived criteria per file
mat=collections.defaultdict(set)
for r in csv.DictReader(open("evidence/43-rubric-traceability/EVD-S-01-coverage-matrix.csv")):
    mat[r["resolved_file"]].add(r["criterion"])
# findings per evidence stem
tok=collections.defaultdict(set)
for fn,col in (("evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv","evidence"),("evidence/13-traceability/EVD-F-04-finding-coverage-matrix.csv","evidence")):
    for r in csv.DictReader(open(fn)):
        for t in re.findall(r"EVD-[A-Z]-\d+[a-z]?",r[col]): tok[t].add(r["finding"])
        for p in re.findall(r"evidence/[A-Za-z0-9_./-]+",r[col]): tok[p].add(r["finding"])
for r in csv.DictReader(open("evidence/43-rubric-traceability/EVD-S-03-finding-evidence-links.csv")):
    if r["link_type"]=="evidence-file": tok[r["file"]].add(r["finding"])
rows=[]
for m in sorted(glob.glob("evidence/*/MANIFEST.md")):
    folder=os.path.dirname(m)
    for line in open(m,encoding="utf-8"):
        c=[x.strip() for x in line.strip().strip("|").split("|")]
        if len(c)>=8 and re.fullmatch(r"[0-9a-f]{64}",c[2]):
            f=c[1].strip("`"); path=f"{folder}/{f}"
            stem=re.match(r"EVD-([A-Z])-(\d+)([a-z]?)",f)
            fnd=set()
            for t in tok:
                if t==path or (t.startswith("EVD-") and f.startswith(t)): fnd.add
            fnd=set()
            for t,v in tok.items():
                if t==path or (t.startswith("EVD-") and f.startswith(t) and (len(f)==len(t) or not f[len(t)].isalnum() or f[len(t)] in "-._")): fnd|=v
            crit=set(mat.get(path,set())); basis="matrix" if crit else ""
            if not crit:
                sl=stem.group(1) if stem else folder.split("/")[-1][:1]
                crit=set(STAGE_DEFAULT.get(sl,"").split(";")) - {""}; basis="stage-default"
            rows.append({"Evidence ID":c[0],"File path":path.replace("evidence/",""),"SHA-256":c[2],"Produced by":c[3],"Produced at":c[5],"Operator":c[6],"Command":c[4],"Findings addressed":";".join(sorted(fnd)),"Rubric criteria":";".join(sorted(crit)),"Cited by":c[7],"Rubric basis":basis})
cols=list(rows[0])
with open("evidence/EVIDENCE-INDEX.csv","w",newline="",encoding="utf-8") as fh:
    w=csv.DictWriter(fh,fieldnames=cols,lineterminator="\n"); w.writeheader(); w.writerows(rows)
allf=set()
for r in rows:
    for f in r["Findings addressed"].split(";"):
        if f: allf.add(f)
print(len(rows),"rows;",len(allf),"findings referenced;", collections.Counter(r["Rubric basis"] for r in rows))

import sys
sys.path.insert(0,"/tmp/claude-0/-home-claude-delta-team-casestudy-sprint-3/7b5a429d-b1d0-5503-bea8-f837bfd1a87c/scratchpad/r3")
from common import hdr
cols10=["Evidence ID","File path","SHA-256","Produced by","Produced at","Operator","Command","Findings addressed","Rubric criteria","Cited by","Rubric basis"]
esc=lambda x: x.replace("|","\\|")
body="\n".join("| "+" | ".join((("`"+r[c]+"`") if c in("SHA-256","File path") else esc(r[c])) for c in cols10)+" |" for r in rows)
doc="# Evidence index (hash-verified, rubric-aware)\n\n"+hdr("03-3 (Doc 03 section 5)","PROVISIONAL","evidence/*/MANIFEST.md; EVD-S-01; EVD-S-03; EVD-F-04b","See docs/43-rubric-traceability/evidence-index-notes.md","Findings and rubric columns are the author's linkage").replace("Stage S: Evidence index and rubric traceability (runbook/03-EVIDENCE-RUBRIC-TRACEABILITY.md)","S: Evidence index and rubric traceability (supersedes the Stage R2 index)")+f"""
{len(rows)} evidence files in {len(set(r['File path'].split('/')[0] for r in rows))} stage folders. Columns follow Document 03 section 5; the last column states how the rubric criteria were assigned (`matrix` = the file is named in the Document 03 coverage matrix; `stage-default` = assigned from its stage only). Machine-readable copy: `evidence/EVIDENCE-INDEX.csv`. Verification result: `docs/43-rubric-traceability/verification.md`.

| """+" | ".join(cols10)+" |\n|"+"---|"*len(cols10)+"\n"+body+"\n"
open("evidence/EVIDENCE-INDEX.md","w",encoding="utf-8").write(doc)
