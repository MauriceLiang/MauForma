"""Generic semantic spacing relationships and intentionally connected exceptions."""
from __future__ import annotations
import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_spacing_rhythm import validate_plan,validate_repository
class SemanticSpacingTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.plan=json.loads((ROOT/"assets/spacing-rhythm-patterns.json").read_text("utf-8"))
 def clone(self):return copy.deepcopy(self.plan)
 def test_all_four_modes_and_repository(self):
  self.assertEqual(validate_repository(),[])
  self.assertEqual({x["mode"] for x in self.plan["profiles"]},{"Operate","Persuade","Read","Experience"})
 def test_rejects_missing_section_gap_role(self):
  d=self.clone();d["profiles"][0]["relationships"][0]["token"]="inside"
  self.assertTrue(any("matching semantic" in s for s in validate_plan(d)))
 def test_requires_reason_for_connected_zero_gap(self):
  d=self.clone()
  c=next(x for x in d["profiles"][0]["relationships"] if x["relation"]=="connected")
  c["reason"]=""
  self.assertTrue(any("intentional adjacency" in s for s in validate_plan(d)))
 def test_connected_does_not_force_spatial_separation(self):
  d=self.clone()
  c=next(x for x in d["profiles"][0]["relationships"] if x["relation"]=="connected")
  self.assertIsNone(c["token"])
  self.assertEqual(validate_plan(d),[])
 def test_rejects_fake_spacing_for_overlay(self):
  d=self.clone()
  o=next(x for x in d["profiles"][3]["relationships"] if x["relation"]=="anchored")
  o["token"]="section"
  self.assertTrue(any("connected/anchored" in s for s in validate_plan(d)))
 def test_requires_project_specific_tokens(self):
  d=self.clone();d["profiles"][1]["tokens"]["peer"]=""
  self.assertTrue(any("must map" in s for s in validate_plan(d)))
 def test_same_element_cannot_be_spaced_from_itself(self):
  d=self.clone();d["profiles"][2]["relationships"][0]["to"]="chapter"
  self.assertTrue(any("distinct semantic" in s for s in validate_plan(d)))
 def test_no_hardcoded_global_pixels_in_schema(self):
  self.assertFalse(any("px" in str(item.get("token","")) for p in self.plan["profiles"] for item in p["relationships"]))
  self.assertEqual(validate_plan(self.plan),[])
if __name__=="__main__":unittest.main()
