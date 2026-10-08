import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'README.md',
    'requirements.txt',
    'apps/api/main.py',
    'docs/transformation-roadmap.md',
    'docs/domain-specific-spec.md',
    'PRODUCTION_EVIDENCE_PACK_TEMPLATE.md'
]
forbidden = [
    'docs/PARTICIPANT_BRIEF.md',
    'docs/discovery/prompt-pack.md',
    'docs/challenges/moonshot-tasks.md',
    'docs/workshop-scorecard.md'
]
missing = [p for p in required if not (ROOT / p).exists()]
forbidden_present = [p for p in forbidden if (ROOT / p).exists()]
manifest = json.loads((ROOT / 'data' / 'manifest.json').read_text())
row_failures = []
for name, expected in manifest['csv_files'].items():
    path = ROOT / 'data' / 'synthetic' / name
    with path.open(newline='', encoding='utf-8') as f:
        actual = sum(1 for _ in csv.DictReader(f))
    if actual != expected:
        row_failures.append((name, expected, actual))
event_count = sum(1 for _ in (ROOT / 'data' / 'synthetic' / 'events.jsonl').open(encoding='utf-8'))
if missing or forbidden_present or row_failures or event_count != manifest['jsonl_events']:
    print({'missing': missing, 'forbidden_present': forbidden_present, 'row_failures': row_failures, 'event_count': event_count})
    sys.exit(1)

# ---- Extended assertions (runbook step H9, F-50, F-54, F-55). The assertions above are preserved unchanged. ----
sys.path.insert(0, str(ROOT))
extra = {}


def extended_checks():
    problems = []
    # 1. the semantic layer validates (only when the monorepo layout provides it)
    from apps.api.config import _semantic_dir
    sem = _semantic_dir()
    gen = sem / 'generated' / 'semantic-layer.json'
    schema = sem / 'schemas' / 'semantic-layer.schema.json'
    if gen.exists() and schema.exists():
        import jsonschema
        errs = list(jsonschema.Draft202012Validator(json.loads(schema.read_text())).iter_errors(json.loads(gen.read_text())))
        extra['semantic_layer'] = 'valid' if not errs else f'{len(errs)} errors'
        if errs:
            problems.append('semantic layer invalid')
    else:
        extra['semantic_layer'] = 'not present in this layout'
        problems.append('semantic layer missing')
    # 2. required evidence directories (monorepo layout only)
    ev = ROOT.parent / 'evidence'
    if ev.is_dir():
        need = ['00-preflight', '12-specs', '13-traceability']
        gone = [n for n in need if not (ev / n).is_dir()]
        extra['evidence_dirs'] = 'ok' if not gone else gone
        if gone:
            problems.append('evidence dirs missing')
    # 3. no secret-shaped literal in the working tree
    from scripts.secret_scan import scan_tree
    secrets_found = scan_tree(ROOT)
    extra['secret_findings'] = len(secrets_found)
    if secrets_found:
        problems.append('secret-shaped literal present')
    # 4. the OpenAPI contract matches the live routes
    import yaml

    from apps.api.main import app
    contract = yaml.safe_load((ROOT / 'data' / 'contracts' / 'openapi.yaml').read_text())
    ops = {'get', 'post', 'put', 'patch', 'delete'}
    want = {(m.upper(), p) for p, v in contract['paths'].items() for m in v if m in ops}
    live = {(m.upper(), p) for p, v in app.openapi()['paths'].items() for m in v if m in ops}
    extra['openapi_route_diff'] = 'clean' if want == live else {'only_contract': sorted(want - live), 'only_live': sorted(live - want)}
    if want != live:
        problems.append('openapi drift')
    # 5. generated Rego is current
    import subprocess
    ok = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'generate_rego.py'), '--check']).returncode == 0
    extra['rego_current'] = ok
    if not ok:
        problems.append('rego out of date')
    return problems


issues = extended_checks()
if issues:
    print({'issues': issues, **extra})
    sys.exit(1)
print({'status': 'ok', 'repo': manifest['repo'], 'csv_files': len(manifest['csv_files']), 'events': event_count, 'clean_repo_contract': True, **extra})
