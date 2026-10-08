import csv, json, pathlib, re, sys
import jsonschema, pytest, yaml

HERE = pathlib.Path(__file__).resolve().parent
SL = HERE.parent
REPO = SL.parent
DATA = REPO / "07-logistics-shipment-fleet-routing-ops" / "data" / "synthetic"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(SL))
import rule_eval, generate  # noqa: E402

SCHEMA = json.loads((SL / "schemas" / "semantic-layer.schema.json").read_text())
MAP = {
    "entities": "entities",
    "status-taxonomy": "status_taxonomy",
    "relationships": "relationships",
    "business-rules": "business_rules",
    "metrics": "metrics",
    "access-semantics": "access_semantics",
    "ai-context-policy": "ai_context_policy",
    "workflow-semantics": "workflow_semantics",
}
REQUIRED = [
    "README.md",
    "glossary.md",
    "domain-knowledge.md",
    "entities.yaml",
    "status-taxonomy.yaml",
    "relationships.yaml",
    "business-rules.yaml",
    "metrics.yaml",
    "access-semantics.yaml",
    "ai-context-policy.yaml",
    "workflow-semantics.yaml",
    "api-contract.json",
    "schemas/semantic-layer.schema.json",
    "SEMANTIC-COMPLETENESS.md",
]


def load(n):
    return yaml.safe_load((SL / (n + ".yaml")).read_text())


def rows(dataset):
    with (DATA / dataset).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_required_files_exist():
    assert [n for n in REQUIRED if not (SL / n).exists()] == []


@pytest.mark.parametrize("name", list(MAP))
def test_yaml_validates_against_schema(name):
    schema = {"$ref": "#/$defs/" + MAP[name], "$defs": SCHEMA["$defs"]}
    jsonschema.validate(load(name), schema)


def test_entity_fields_match_csv_headers_both_ways():
    ent = load("entities")["entities"]
    for e, spec in ent.items():
        header = list(rows(spec["dataset"])[0])
        assert set(header) == set(spec["fields"]), e


def test_every_categorical_field_has_declared_domain():
    ent = load("entities")["entities"]
    tax = load("status-taxonomy")
    for e, spec in ent.items():
        for f, d in spec["fields"].items():
            if d["type"] == "enum":
                assert d.get("domain") in tax["enums"], (e, f)
            if d["type"] in ("location_ref", "carrier_ref", "model_ref", "timezone"):
                assert d.get("reference") in tax["references"], (e, f)


def test_every_business_rule_is_machine_evaluable():
    data = {e: rows(s["dataset"]) for e, s in load("entities")["entities"].items()}
    results = {}
    for r in load("business-rules")["rules"]:
        out = rule_eval.evaluate(r, data)
        assert out["status"] in ("evaluated", "data_gap", "static"), r["id"]
        results[r["id"]] = out
    assert sum(1 for o in results.values() if o["status"] == "evaluated") >= 20


def test_six_declared_gaps_are_expressed_as_rules():
    gaps = {
        "duplicate_tracking_events",
        "stale_gps",
        "timezone_mismatch",
        "duplicate_carrier_booking",
        "route_ignores_restrictions",
        "location_data_overexposure",
    }
    assert gaps <= {r["gap"] for r in load("business-rules")["rules"]}


def test_metrics_match_frozen_kpi_dictionary():
    text = (REPO / "docs" / "04-baseline-kpis" / "kpi-dictionary.md").read_text()
    frozen = {}
    for line in text.splitlines():
        m = re.match(r"^\| (K[0-9]+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|", line)
        if m:
            frozen[m.group(1)] = (m.group(2), m.group(3), m.group(4), m.group(5))
    got = {m["id"]: (m["name"], m["meaning"], m["formula"], m["unit"]) for m in load("metrics")["metrics"]}
    assert got == frozen and len(got) == 10


def test_access_semantics_covers_eight_personas_and_six_entities():
    p = load("access-semantics")["personas"]
    assert len(p) == 8 and all(len(v) == 6 for v in p.values())


def test_generated_json_is_current():
    target = SL / "generated" / "semantic-layer.json"
    assert json.loads(target.read_text()) == json.loads(json.dumps(generate.build(), sort_keys=True))


def test_layer_is_vendor_framework_and_model_neutral():
    banned = [
        "fastapi",
        "pydantic",
        "openai",
        "anthropic",
        "claude",
        "gpt",
        "gemini",
        "azure",
        "aws",
        "opa",
        "rego",
        "terraform",
        "django",
        "flask",
        "langchain",
    ]
    text = " ".join(p.read_text().lower() for p in SL.glob("*.yaml"))
    assert [b for b in banned if re.search(r"\b" + b + r"\b", text)] == []


def test_workflow_states_are_the_canonical_statuses():
    wf = load("workflow-semantics")["workflows"]["shipment_lifecycle"]
    canon = set(load("status-taxonomy")["enums"]["shipment_status"]["values"])
    used = set(wf["states"]) | {t["from"] for t in wf["transitions"]} | {x for t in wf["transitions"] for x in t["to"]}
    assert used == canon and set(wf["terminal"]) <= canon


def test_recommendation_classes_and_precedence_agree_and_retry_ceiling_matches_br13():
    ws = load("workflow-semantics")["ai_decision_semantics"]
    assert [c["id"] for c in ws["recommendation_classes"]] == ws["precedence"]
    assert all(c["action_taken"] == "none" for c in ws["recommendation_classes"])
    br13 = next(r for r in load("business-rules")["rules"] if r["id"] == "BR-13")
    assert (
        ws["retry_ceiling"]["value"]
        == br13["max"]
        == load("workflow-semantics")["workflows"]["carrier_booking_saga"]["retry_ceiling"]
    )


def test_abstain_reasons_are_declared_and_legacy_status_abstains():
    ab = load("workflow-semantics")["ai_decision_semantics"]["abstain"]
    assert {r["id"] for r in ab["reasons"]} == {"insufficient_context", "low_confidence", "schema_violation"}
    legacy = {x["value"] for x in load("status-taxonomy")["legacy_tolerance"]}
    canon = set(load("status-taxonomy")["enums"]["shipment_status"]["values"])
    assert legacy and not (legacy & canon)


def test_platform_roles_are_not_personas_and_summarize_callers_match_the_matrix():
    a = load("access-semantics")
    assert set(a["platform_roles"]).isdisjoint(a["personas"])
    readers = sorted(p for p, v in a["personas"].items() if v["shipments"]["access"] in ("read", "write"))
    assert sorted(a["ai_summarize"]["callers_allowed_by_matrix"]) == readers


def test_api_contract_is_valid_and_operations_are_unique():
    c = json.loads((SL / "api-contract.json").read_text())
    jsonschema.validate(c, {**SCHEMA["$defs"]["api_contract"], "$defs": SCHEMA["$defs"]})
    keys = [(o["method"], o["path"]) for o in c["operations"]]
    assert len(keys) == len(set(keys))
    entities = set(load("entities")["entities"])
    assert {o["entity"] for o in c["operations"] if o.get("entity")} <= entities


def test_documentation_names_every_required_file():
    text = (SL / "README.md").read_text()
    assert [n for n in REQUIRED if n.split("/")[-1] not in text] == []
