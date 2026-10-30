"""Replay preserved extracted facts through current checks; no model calls."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import checks

rows = []
for relative in ('evidence/evaluation-final/20261028T180115288510Z',
                 'evidence/evaluation-extended/20261029T210826845602Z'):
    for path in sorted((ROOT/relative/'runs').glob('*/run.json')):
        run = json.loads(path.read_text(encoding='utf-8'))
        snap = json.loads((path.parent/'input-snapshot.json').read_text(encoding='utf-8'))
        errors, warnings = checks.check(run['extracted_facts'], snap['input_text'], snap['source_metadata'])
        rows.append({'saved_run':path.relative_to(ROOT).as_posix(),
                     'errors':errors,'warnings':warnings})
result = {'operation':'recheck saved facts, not new model runs',
          'checker_sha256':hashlib.sha256((ROOT/'checks.py').read_bytes()).hexdigest(),
          'runs_checked':len(rows),'checks_passed':sum(not r['errors'] for r in rows),
          'note':'Mechanical acceptance does not establish content completeness or safety.',
          'results':rows}
(ROOT/'evidence/saved-facts-recheck-20261030.json').write_text(
    json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'runs_checked':result['runs_checked'],'checks_passed':result['checks_passed']}))
if len(rows)!=10 or any(r['errors'] for r in rows):
    raise SystemExit(1)
