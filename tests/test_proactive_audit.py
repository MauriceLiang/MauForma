"""Intent routing tests: vague prompts cannot bypass full defect-first discovery."""
from __future__ import annotations
import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_proactive_audit import validate,validate_repo
class IntentTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.raw=json.loads((ROOT/"assets/proactive-audit-trigger-cases.json").read_text("utf-8"))
 def cloned(self):return copy.deepcopy(self.raw)
 def test_repository(self):self.assertEqual(validate_repo(),[])
 def test_four_modes(self):
  self.assertEqual({x["mode"] for x in self.raw["cases"] if x["expected_path"]=="discover-repair-verify"},{"Operate","Persuade","Read","Experience"})
 def test_vague_must_scan_spacing(self):
  c=self.cloned();c["cases"][0]["scan"].remove("spacing")
  self.assertTrue(any("full visual" in s for s in validate(c)))
 def test_vague_must_scan_other_components(self):
  c=self.cloned();c["cases"][0]["scan"]=["spacing"]
  self.assertTrue(any("full visual" in s for s in validate(c)))
 def test_bounded_functional_bug(self):
  self.assertEqual(validate(self.cloned()),[])
  self.assertEqual(next(c["expected_path"] for c in self.raw["cases"] if c["id"]=="bug-only"),"scoped-functional-fix")
 def test_review_only(self):
  self.assertEqual(next(c["expected_path"] for c in self.raw["cases"] if c["id"]=="analysis-only"),"diagnose-report-only")
if __name__=="__main__":unittest.main()
