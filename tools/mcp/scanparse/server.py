#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import json
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))
from common_server import serve

ROOT = Path(__file__).resolve().parents[3]
FINDINGS = ROOT / 'artifacts' / 'findings'
FINDINGS.mkdir(parents=True, exist_ok=True)


def now():
    return datetime.now(timezone.utc).isoformat()


def write_out(name, payload):
    path = FINDINGS / name
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return str(path.relative_to(ROOT))


def import_json_like(tool, params):
    src = Path(params.get('path', '')) if params.get('path') else None
    payload = {'tool': tool, 'source': str(src) if src else None, 'imported': src.exists() if src else False, 'items': []}
    if src and src.exists():
        try:
            payload['items'] = json.loads(src.read_text())
        except Exception:
            payload['items'] = [{'raw': src.read_text()[:1000]}]
    art = write_out(f'{tool}.json', payload)
    return {'ok': True, 'server': 'scanparse', 'tool': tool, 'timestamp': now(), 'inputs': params, 'artifacts': [art], 'warnings': ['stub parser'], 'result': payload}


def deduplicate_findings(params):
    result = {
        'normalized_file': 'artifacts/findings/normalized_from_stub.json',
        'dedup_rule': 'target+protocol+cwe+summary',
        'status': 'generated'
    }
    art = write_out('normalized_from_stub.json', result)
    return {'ok': True, 'server': 'scanparse', 'tool': 'deduplicate_findings', 'timestamp': now(), 'inputs': params, 'artifacts': [art], 'warnings': ['stub dedup'], 'result': result}


def rank_industrial_impact(params):
    result = {'ranking_basis': 'unsafe motion > remote modification > auth bypass > dos > info leak', 'status': 'ranked_stub'}
    art = write_out('rank_industrial_impact.json', result)
    return {'ok': True, 'server': 'scanparse', 'tool': 'rank_industrial_impact', 'timestamp': now(), 'inputs': params, 'artifacts': [art], 'warnings': ['stub ranking'], 'result': result}


TOOLS = {
    'import_nessus': lambda params: import_json_like('import_nessus', params),
    'import_burp': lambda params: import_json_like('import_burp', params),
    'import_defensics': lambda params: import_json_like('import_defensics', params),
    'deduplicate_findings': deduplicate_findings,
    'rank_industrial_impact': rank_industrial_impact,
}

serve('scanparse', 8762, TOOLS)
