"""Generate report measurements from the preserved final five-run batch."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BATCH=ROOT/'evidence/evaluation-final/20261028T180115288510Z'
rows=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((BATCH/'runs').glob('*/run.json'))]
if len(rows)!=5:
    raise ValueError('Expected the recorded five-run batch')
table=[]
for i,row in enumerate(rows,1):
    raw=row['raw_model_response']
    table.append(f"{i} & {raw['prompt_eval_count']} & {raw['eval_count']} & {row['elapsed_seconds']:.3f} & Saved "+r'\\')
(ROOT/'report/results-rows.tex').write_text(r'\newcommand{\ResultRows}{'+'\n'+'\n'.join(table)+'\n}\n',encoding='utf-8')
total=sum(r['raw_model_response']['prompt_eval_count']+r['raw_model_response']['eval_count'] for r in rows)
elapsed=sum(r['elapsed_seconds'] for r in rows)
summary=json.loads((BATCH/'summary.json').read_text(encoding='utf-8'))
metric={key:sum(c.get('reference_fields',{}).get(key,False) for c in summary['cases'])
        for key in summary['cases'][0]['reference_fields']}
report={'batch':str(BATCH.relative_to(ROOT)), 'runs':len(rows),'total_tokens':total,
        'wall_seconds_sum':round(elapsed,3),'reference_proxy_counts':metric}
(ROOT/'evidence/final-metrics.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
(ROOT/'report/results-macros.tex').write_text(
    r'\newcommand{\TotalTokens}{'+str(total)+'}\n'+
    r'\newcommand{\TotalSeconds}{'+f'{elapsed:.3f}'+'}\n',encoding='utf-8')
print(json.dumps(report,indent=2))

# Keep the first measured batch fixed and add the second without replacing it.
EXTENDED=ROOT/'evidence/evaluation-extended/20261029T210826845602Z'
extrows=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((EXTENDED/'runs').glob('*/run.json'))]
extsummary=json.loads((EXTENDED/'summary.json').read_text(encoding='utf-8'))
if len(extrows)!=5:
    raise ValueError('Expected all five preserved extended-input attempts')
combined=[]
for label, group, cases in [('A', rows, summary['cases']), ('B', extrows, extsummary['cases'])]:
    for i,(row,case) in enumerate(zip(group,cases),1):
        raw=row['raw_model_response']
        outcome='Saved' if row['extracted_facts'] and row['extracted_facts']['in_scope'] else 'Failed'
        content='Met' if all(case['reference_fields'].values()) else 'Missed'
        combined.append(f"{label} & {i} & {raw.get('prompt_eval_count',0)} & {raw.get('eval_count',0)} & {row['elapsed_seconds']:.3f} & {outcome} & {content} "+r'\\')
# The checks have saved five drafts, but required participation/route content is missing.
counts={key:sum(c.get('reference_fields',{}).get(key,False) for c in extsummary['cases'])
        for key in extsummary['cases'][0]['reference_fields']}
saved=sum(c['draft_saved'] for c in extsummary['cases'])
token_total=sum(r['raw_model_response'].get('prompt_eval_count',0)+r['raw_model_response'].get('eval_count',0) for r in extrows)
seconds=round(sum(r['elapsed_seconds'] for r in extrows),3)
extended_report={'batch':EXTENDED.relative_to(ROOT).as_posix(),'runs':len(extrows),
                 'drafts_saved':saved,'total_tokens':token_total,'wall_seconds_sum':seconds,
                 'reference_proxy_counts':counts}
(ROOT/'evidence/extended-metrics.json').write_text(json.dumps(extended_report,indent=2)+'\n',encoding='utf-8')
findings=(f'Batch B used {token_total:,} tokens and {seconds:.3f} seconds. '
          f'All {saved} attempts saved drafts and passed the code checks. '
          f"The office-day check passed in {counts['participation_office_day']}/5 runs, "
          f"and the route mailbox/case check passed in {counts['response_mailbox_and_case']}/5. "
          'The submission details appeared under participation, while response route stayed unknown. '
          'We count all five drafts as incomplete.\n\n'
          'A likely cause is our own prompt. It says the official submission route may go under '
          'participation, it never defines participation as events such as an office day, and it '
          'does not mention office days. Our prompt allowed this. '
          'We have not changed the prompt or rerun, so we cannot say how much a clearer prompt '
          'would help. The saved Norwegian drafts also contradict themselves: the line on what '
          'a resident can do contains the mailbox and address, while the next line says the '
          'official route is not given. The office day does not appear at all.\n')
(ROOT/'report/results-rows.tex').write_text(
    r'\newcommand{\ResultRows}{'+'\n'+'\n'.join(table)+'\n}\n'+
    r'\newcommand{\CombinedRows}{'+'\n'+'\n'.join(combined)+'\n}\n'+
    r'\newcommand{\ExtendedFindings}{'+findings+'}\n',encoding='utf-8')
# Include a raw complete five-attempt evaluation summary, not a rewritten example.
(ROOT/'report/evaluation-log.json').write_bytes((EXTENDED/'summary.json').read_bytes())
(ROOT/'report/evaluation-path.tex').write_text(
    'Saved batch: '+r'\path{'+EXTENDED.relative_to(ROOT).as_posix()+'}.\n',encoding='utf-8')
print(json.dumps(extended_report,indent=2))
