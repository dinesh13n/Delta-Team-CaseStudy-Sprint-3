"""EVD-R-03 producer: verify every evidence MANIFEST row (file exists, sha256 matches) and list evidence files absent from manifests."""
import re, hashlib, sys, json, os
from pathlib import Path
R=Path(sys.argv[1]); ev=R/"evidence"
res={"manifests":0,"rows":0,"ok":0,"missing":[],"mismatch":[],"unmanifested":[],"duplicates":[]}
listed=set()
for m in sorted(ev.glob("*/MANIFEST.md")):
    res["manifests"]+=1; seen=set()
    for line in m.read_text(encoding="utf-8").splitlines():
        c=[x.strip() for x in line.strip().strip("|").split("|")]
        if len(c)<3 or not re.fullmatch(r"[0-9a-f]{64}",c[2]): continue
        res["rows"]+=1; f=c[1].strip("`"); p=m.parent/f; listed.add(p.resolve())
        if (m.parent.name,f) in seen: res["duplicates"].append(f"{m.parent.name}/{f}")
        seen.add((m.parent.name,f))
        if not p.is_file(): res["missing"].append(f"{m.parent.name}/{f}"); continue
        if hashlib.sha256(p.read_bytes()).hexdigest()==c[2]: res["ok"]+=1
        else: res["mismatch"].append(f"{m.parent.name}/{f}")
for p in ev.rglob("*"):
    if p.is_file() and p.name not in ("MANIFEST.md",".gitkeep") and p.resolve() not in listed and "__pycache__" not in str(p):
        res["unmanifested"].append(str(p.relative_to(ev)))
print(json.dumps({k:(v if not isinstance(v,list) else len(v)) for k,v in res.items()}))
json.dump(res,open(sys.argv[2],"w"),indent=1)
