import json, pathlib, sys, tempfile, unittest
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import run

FX = pathlib.Path(__file__).parent.parent / "fixtures"


def go(n):
    with tempfile.TemporaryDirectory() as d:
        return run.run(FX / f"{n}.meta.json", FX / f"{n}.txt", "fixture", out=d, checked_at="2026-10-28")


class T(unittest.TestCase):
    def test_ok(self):
        r = go("syn_ok")
        self.assertEqual(r["deadline"]["value"], "2026-11-18")
        self.assertEqual(r["deadline_status"], "open")
        self.assertEqual(r["review_status"], "needs_human_review")

    def test_no_deadline_stays_unknown(self):
        r = go("syn_no_deadline")
        self.assertEqual(r["deadline"]["value"], "unknown")
        self.assertEqual(r["deadline_status"], "unknown")

    def test_ambiguous_date_preserved(self):
        self.assertEqual(go("syn_ambiguous_date")["deadline"]["value"], "ambiguous")

    def test_out_of_scope_rejected(self):
        r = go("syn_out_of_scope")
        self.assertEqual(r["status"], "failed")
        self.assertIn("out of scope", r["failed_checks"][0])

    def test_injection_absorbed_when_model_resists(self):
        self.assertEqual(go("syn_injection")["deadline"]["value"], "2026-11-20")

    def test_known_gap_injection_followed_passes_exact_match(self):
        # The injected date is in the extract, so exact matching cannot catch it.
        # Only a warning is raised. A human must review. Not solved.
        r = go("syn_injection_followed")
        self.assertEqual(r["deadline"]["value"], "2027-01-01")
        self.assertTrue(r["warnings"])

    def test_altered_evidence_fails(self):
        r = go("syn_bad_evidence")
        self.assertEqual(r["status"], "failed")
        self.assertTrue(any("evidence not found" in e for e in r["failed_checks"]))


if __name__ == "__main__":
    unittest.main()
