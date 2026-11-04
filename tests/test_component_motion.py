"""Generic component motion coverage regression tests."""
from __future__ import annotations
import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_component_motion import validate_plan,validate_repository

class ComponentMotionTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.sample=json.loads((ROOT/"assets/component-motion-patterns.json").read_text("utf-8"))
 def clone(self):return copy.deepcopy(self.sample)
 def test_repository(self):self.assertEqual(validate_repository(),[])
 def test_four_modes_and_selected_none(self):
  self.assertEqual({p["mode"] for p in self.sample["profiles"]},{"Operate","Persuade","Read","Experience"})
  self.assertIn("none",{p["motion_level"] for p in self.sample["profiles"]})
 def test_route_only_is_not_component_motion(self):
  a=self.clone();p=a["profiles"][0];p["interactions"]=[x for x in p["interactions"] if x["component"]=="page"]
  p["interactions"][0]["mode"]="motion";p["interactions"][0]["mechanism"]="page-transition"
  self.assertTrue(any("page-only motion" in e for e in validate_plan(a)))
 def test_rejects_generic_fade_for_all_components(self):
  a=self.clone()
  for x in a["profiles"][0]["interactions"]:
   if x["mode"]=="motion":x["mechanism"]="fade"
  self.assertTrue(any("single-mechanism" in e for e in validate_plan(a)))
 def test_rejects_missing_valuable_component(self):
  a=self.clone()
  for x in a["profiles"][0]["interactions"]:
   if x["priority"]=="high":
    x["mode"]="feedback";x["mechanism"]="none";x["reason"]="Temporarily immediate"
  self.assertTrue(any("high-value components" in e for e in validate_plan(a)))
 def test_static_requires_justification(self):
  a=self.clone();a["profiles"][2]["interactions"][-1]["reason"]=""
  self.assertTrue(any("intentionally non-animated" in e for e in validate_plan(a)))
 def test_user_none_motion_respected(self):
  a=self.clone();a["profiles"][4]["interactions"][0]["mode"]="motion";a["profiles"][4]["interactions"][0]["mechanism"]="fade"
  self.assertTrue(any("none policy" in e for e in validate_plan(a)))
 def test_no_fake_component_required_when_not_present(self):
  a=self.clone();a["profiles"][3]["interactions"].pop(3)
  self.assertEqual(validate_plan(a),[])
 def test_alternative_required(self):
  a=self.clone();a["profiles"][1]["interactions"][0]["alternative"]=""
  self.assertTrue(any("no-motion alternative" in e for e in validate_plan(a)))
if __name__=="__main__":unittest.main()
