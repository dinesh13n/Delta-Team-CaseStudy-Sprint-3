import json,sys,importlib.util,collections
spec=importlib.util.spec_from_file_location("ad",sys.argv[1]+"/app/adapter.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
def sem(r):
    r=(r or "").lower()
    if not r: return "abstain"
    if r.startswith("no action"): return "none"
    if "review" in r and "compensation" not in r: return "review"
    if "compensation" in r: return "compensation_referral"
    return "other"
tab=collections.Counter(); abst=collections.Counter()
for n in ["golden","edge","adversarial"]:
  for l in open("evaluation/datasets/%s.jsonl"%n):
    c=json.loads(l); e=c["expect"]
    o=m.summarize_case(json.loads(json.dumps(c)))
    if e.get("abstained"): abst[(n,bool(o["abstained"]),o.get("abstain_reason"))]+=1; continue
    if o["abstained"]: tab[(n,e["reco_class"],"ABSTAINED")]+=1; continue
    tab[(n,e.get("reco_class"),sem(o["recommendation"]))]+=1
print("expected-abstain cases:",dict(abst))
for k,v in sorted(tab.items()): print(v,k)
