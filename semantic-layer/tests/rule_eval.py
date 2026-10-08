"""Neutral evaluator for business-rules.yaml over CSV rows. Returns violation counts."""
import collections, re

def _blank(v):
    return v is None or str(v).strip() == ""

def evaluate(rule, data):
    t, e = rule["type"], rule["entity"]
    rows = data.get(e, [])
    if rule.get("data_gap"):
        return {"status": "data_gap", "violations": None}
    if t == "unique":
        c = collections.Counter(tuple(r.get(f) for f in rule["fields"]) for r in rows)
        return {"status": "evaluated", "violations": sum(n for n in c.values() if n > 1)}
    if t == "pattern":
        p = re.compile(rule["pattern"])
        return {"status": "evaluated", "violations": sum(1 for r in rows if not p.fullmatch(r.get(rule["field"]) or ""))}
    if t == "range":
        bad = 0
        for r in rows:
            try:
                v = float(r[rule["field"]])
            except (ValueError, KeyError):
                continue
            if v < rule["min"] or v > rule["max"]:
                bad += 1
        return {"status": "evaluated", "violations": bad}
    if t == "not_blank":
        return {"status": "evaluated", "violations": sum(1 for r in rows if any(_blank(r.get(f)) for f in rule["fields"]))}
    if t == "timestamp_after":
        return {"status": "evaluated", "violations": sum(1 for r in rows if r.get(rule["field"]) and r[rule["field"]] <= rule["after"])}
    if t == "reference_exists":
        te, tf = rule["to"].split(".")
        keys = {r[tf] for r in data.get(te, [])}
        return {"status": "evaluated", "violations": sum(1 for r in rows if r.get(rule["field"]) not in keys)}
    if t == "at_most_one_active":
        c = collections.Counter(r[rule["group_by"]] for r in rows if r.get("status") not in rule["inactive_statuses"] and r.get(rule["group_by"]))
        return {"status": "evaluated", "violations": sum(n - 1 for n in c.values() if n > 1)}
    if t == "enum_or_reference":
        p = re.compile(r"[A-Za-z_]+/[A-Za-z_]+")
        return {"status": "evaluated", "violations": sum(1 for r in rows if not p.fullmatch(r.get(rule["field"]) or ""))}
    if t == "field_exposure":
        return {"status": "static", "violations": None}
    raise ValueError("unsupported rule type " + t)
