"""Cross-domain icon semantic and source verification regression checks."""
from __future__ import annotations
import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_icon_curation import validate_plan,validate_repository
class IconCurationTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.plan=json.loads((ROOT/"assets/icon-curation-patterns.json").read_text("utf8"))
 def clone(self):return copy.deepcopy(self.plan)
 def test_repository_and_modes(self):
  self.assertEqual(validate_repository(),[])
  self.assertEqual({p["mode"] for p in self.plan["profiles"]},{"Operate","Persuade","Read","Experience"})
 def test_candidate_must_be_verified(self):
  p=self.clone();p["profiles"][0]["icons"][0]["candidates"][0]["verified"]=False
  self.assertTrue(any("confirmed" in x for x in validate_plan(p)))
 def test_distinct_navigation_semantics(self):
  p=self.clone();p["profiles"][0]["icons"][1]["chosen"]=p["profiles"][0]["icons"][0]["chosen"]
  self.assertTrue(any("repeated symbol" in x for x in validate_plan(p)))
 def test_a_real_alternative_is_required(self):
  p=self.clone();p["profiles"][0]["icons"][0]["candidates"]=p["profiles"][0]["icons"][0]["candidates"][:1]
  self.assertTrue(any("at least two" in x for x in validate_plan(p)))
 def test_no_invented_icon_name(self):
  p=self.clone();p["profiles"][0]["icons"][0]["chosen"]="ai-magical-dashboard-perfect"
  self.assertTrue(any("not in shortlist" in x for x in validate_plan(p)))
 def test_icon_only_needs_label(self):
  p=self.clone();p["profiles"][2]["icons"][0]["presentation"]="icon-only"
  self.assertTrue(any("accessible name" in x for x in validate_plan(p)))
 def test_choices_are_contextual_not_fixed_website_default(self):
  p=self.clone()
  self.assertEqual(validate_plan(p),[])
  self.assertEqual(p["profiles"][0]["icons"][2]["chosen"],"arrow-left-right")
  self.assertEqual(p["exceptions"][1]["policy"],"text-only")
if __name__=="__main__":unittest.main()
