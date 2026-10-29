"""Run fixed checks or repeated real extraction, preserving every attempt."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import run

ROOT = Path(__file__).resolve().parent

def evaluate(backend='fixture', count=5, out='out/evaluation', checked_at='2026-10-28', example='ringgata'):
    batch = Path(out) / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    batch.mkdir(parents=True)
    rows = []
    cases = [('syn_ok', False), ('syn_no_deadline', False), ('syn_ambiguous_date', False),
             ('syn_out_of_scope', True), ('syn_injection', False),
             ('syn_injection_followed', False), ('syn_bad_evidence', True)]
    if backend == 'ollama':
        cases = [(example, False)] * count
    for name, expected_failure in cases:
        inputs = ROOT / ('examples' if backend == 'ollama' else 'fixtures')
        result = run.run(inputs/f'{name}.meta.json', inputs/f'{name}.txt', backend=backend,
                         model='qwen2.5-coder:7b', out=batch/'runs', checked_at=checked_at)
        saved = result.get('status') != 'failed'
        row = {'case': name, 'draft_saved': saved, 'matches_fixture_behavior_expectation': saved != expected_failure,
               'deadline': result.get('deadline', {}).get('value'),
               'known_unsafe_case': name == 'syn_injection_followed',
               'security_verdict': 'known_unsafe_acceptance' if name == 'syn_injection_followed' and saved else 'not_assessed'}
        if backend == 'ollama' and saved:
            row['reference_fields'] = {
                'deadline': result['deadline']['value'] == '2026-11-18',
                'proposal': all(word in result['proposal']['value'].lower() for word in ('sykkel', 'fortau')),
                'location': all(word in result['location']['value'].lower() for word in ('solvangvegen','disenvegen')),
                'stage': 'oppstart' in result['planning_stage']['value'].lower(),
                'participation_unknown': result['participation']['value'] == 'unknown',
                'response_route_unknown': result['response_route']['value'] == 'unknown',
            }
            if example == 'ringgata_extended':
                row['reference_fields'].pop('participation_unknown')
                row['reference_fields'].pop('response_route_unknown')
                value = result['participation']['value'].lower()
                route = result['response_route']['value'].lower()
                row['reference_fields'].update({
                    'participation_office_day': 'kontordag' in value,
                    'participation_date_time': all(w in value for w in ('10.', 'november', '14', '18')),
                    'response_mailbox_and_case': all(w in route for w in ('post@innlandetfylke.no', '2026/20689')),
                    'response_postal_address': all(w in route for w in ('4404', '2325', 'hamar')),
                })
        rows.append(row)
        print(json.dumps(row, ensure_ascii=True), flush=True)
    summary = {'backend': backend, 'checked_at': checked_at, 'cases': rows,
               'note': 'Reference word checks are narrow proxies, not semantic accuracy. Fixture outputs are canned; the known unsafe case is not a security success.'}
    (batch/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Saved evaluation: {batch}', flush=True)
    return batch

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--backend', choices=['fixture','ollama'], default='fixture')
    parser.add_argument('--count',type=int,default=5)
    parser.add_argument('--out',default='out/evaluation')
    parser.add_argument('--checked-at',default='2026-10-28')
    parser.add_argument('--example',choices=['ringgata','ringgata_extended'],default='ringgata')
    args=parser.parse_args()
    if not 1 <= args.count <= 5:
        parser.error('count must be between 1 and 5; rerun explicitly for further batches')
    evaluate(args.backend,args.count,args.out,args.checked_at,args.example)
