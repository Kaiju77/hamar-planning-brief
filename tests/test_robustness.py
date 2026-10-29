import copy
import json
from pathlib import Path
import tempfile
import unittest
import checks
import run

FX = Path(__file__).parent.parent / 'fixtures'

class Robustness(unittest.TestCase):
    def test_malformed_deadlines_are_rejected_without_crashing(self):
        base = json.loads((FX/'syn_ok.model.json').read_text(encoding='utf-8'))
        meta = json.loads((FX/'syn_ok.meta.json').read_text(encoding='utf-8'))
        text = (FX/'syn_ok.txt').read_text(encoding='utf-8')
        for value in [42, [], None, True, {}, '2026-02-30']:
            with self.subTest(value=value):
                facts = copy.deepcopy(base)
                facts['deadline']['value'] = value
                errors, _ = checks.check(facts, text, meta)
                self.assertTrue(errors)

    def test_status_boundaries_and_ambiguity(self):
        for check_date, expected in [('2026-11-17','open'), ('2026-11-18','open'), ('2026-11-19','closed')]:
            self.assertEqual(checks.deadline_status('2026-11-18', check_date), expected)
        self.assertEqual(checks.deadline_status('ambiguous', '2026-10-28'), 'unknown')

    def test_missing_input_creates_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run.run('missing-meta.json','missing.txt',out=tmp,checked_at='2026-10-28')
            self.assertEqual(result['status'], 'failed')
            self.assertEqual(len(list(Path(tmp).rglob('*.failure.json'))), 1)

    def test_repeated_runs_preserve_both(self):
        with tempfile.TemporaryDirectory() as tmp:
            for _ in range(2):
                run.run(FX/'syn_ok.meta.json',FX/'syn_ok.txt',out=tmp,checked_at='2026-10-28')
            self.assertEqual(len(list(Path(tmp).rglob('run.json'))), 2)
