import csv,re,glob,os,hashlib,json,collections,sys
ROOT=sys.argv[1]; os.chdir(ROOT)
idx=list(csv.DictReader(open("evidence/EVIDENCE-INDEX.csv")))
res={}
# V1 hashes
bad=[r["File path"] for r in idx if not os.path.isfile("evidence/"+r["File path"]) or hashlib.sha256(open("evidence/"+r["File path"],"rb").read()).hexdigest()!=r["SHA-256"]]
res["V1_rows"]=len(idx); res["V1_hash_mismatch_or_missing"]=bad
# manifest rows == index rows
mrows=0
for m in glob.glob("evidence/*/MANIFEST.md"):
    for l in open(m,encoding="utf-8"):
        c=[x.strip() for x in l.strip().strip("|").split("|")]
        if len(c)>=8 and re.fullmatch(r"[0-9a-f]{64}",c[2]): mrows+=1
res["V1b_manifest_rows"]=mrows
# files on disk not in index (excluding manifests and the two index files)
ondisk={os.path.relpath(p,"evidence") for p in glob.glob("evidence/**/*",recursive=True) if os.path.isfile(p)}
inidx={r["File path"] for r in idx}
res["V1c_unindexed_files"]=sorted(f for f in ondisk-inidx if not f.endswith("MANIFEST.md") and f not in("EVIDENCE-INDEX.md","EVIDENCE-INDEX.csv") and "__pycache__" not in f)
# V2 citations
ids={r["Evidence ID"] for r in idx}; paths=inidx
unres=[];n=0
for f in glob.glob("docs/**/*.md",recursive=True)+glob.glob("README.md")+glob.glob("07-*/README.md"):
    t=open(f,encoding="utf-8").read()
    for p in set(re.findall(r"evidence/[A-Za-z0-9_./-]*[A-Za-z0-9_]",t)):
        p=p.rstrip(".")
        if not re.search(r"\.[a-z0-9]+$",p) and not os.path.isdir(p): continue
        if p=="evidence/" : continue
        n+=1
        rel=p[len("evidence/"):]
        ok=rel in paths or os.path.isdir(p) or rel in("EVIDENCE-INDEX.md","EVIDENCE-INDEX.csv") or rel.endswith("MANIFEST.md") or any(i.startswith(rel.rstrip("/")+"/") for i in paths)
        if not ok: unres.append((f,p))
res["V2_path_citations"]=n; res["V2_unresolved"]=unres[:40]; res["V2_unresolved_count"]=len(unres)
# V3 findings
disp={r["finding"]:r["final_disposition"] for r in csv.DictReader(open("evidence/13-traceability/EVD-F-04b-finding-disposition-final.csv"))}
inrows=set()
for r in idx: inrows|={x for x in r["Findings addressed"].split(";") if x}
miss=[f for f in disp if f not in inrows]
res["V3_findings"]=len(disp); res["V3_in_index_rows"]=len(inrows); res["V3_not_in_rows"]={f:disp[f] for f in miss}
res["V3_not_in_rows_and_not_deferred_or_accepted"]=[f for f in miss if disp[f] not in("DEFERRED","ACCEPTED-PROPOSED")]
# V4 rubric
c=collections.Counter()
for r in idx:
    for x in r["Rubric criteria"].split(";"):
        if x: c[x]+=1
res["V4_rows_per_criterion"]=dict(sorted(c.items()))
mat=collections.defaultdict(collections.Counter)
for r in csv.DictReader(open("evidence/43-rubric-traceability/EVD-S-01-coverage-matrix.csv")): mat[r["criterion"]][r["status"]]+=1
res["V4_matrix_status_rows"]={k:dict(v) for k,v in mat.items()}
res["V4_criteria_without_rows"]=[k for k in ("R1","R2","R3","R4","R5") if c[k]==0]
res["V4_basis_counts"]=dict(collections.Counter(r["Rubric basis"] for r in idx))
res["overall"]="PASS" if not bad and not res["V1c_unindexed_files"] and not res["V3_not_in_rows_and_not_deferred_or_accepted"] and not res["V4_criteria_without_rows"] and res["V1_rows"]==mrows and res["V2_unresolved_count"]==0 else "REVIEW"
json.dump(res,open(sys.argv[2],"w"),indent=1)
print(json.dumps({k:(v if not isinstance(v,(list,dict)) or len(str(v))<200 else f"<{len(v)} items>") for k,v in res.items()}))
