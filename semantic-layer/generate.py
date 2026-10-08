"""Generate generated/semantic-layer.json from the YAML sources. Build artifact: do not edit by hand.
Usage: python semantic-layer/generate.py"""
import hashlib, json, pathlib, yaml
HERE = pathlib.Path(__file__).resolve().parent
FILES = ["entities", "status-taxonomy", "relationships", "business-rules", "metrics", "access-semantics", "ai-context-policy"]

def build():
    out = {"generated_from": {}, "layer": {}}
    for n in FILES:
        raw = (HERE / (n + ".yaml")).read_bytes()
        out["generated_from"][n + ".yaml"] = hashlib.sha256(raw).hexdigest()
        out["layer"][n] = yaml.safe_load(raw)
    return out

if __name__ == "__main__":
    target = HERE / "generated" / "semantic-layer.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(build(), indent=1, sort_keys=True) + "\n")
    print("wrote", target)
