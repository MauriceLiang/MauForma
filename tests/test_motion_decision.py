"""MauForma universal motion ownership, interaction and accessibility regression tests."""
from __future__ import annotations
import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_motion_decision import validate_plan,validate_repository

class MotionChoiceTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.sample=json.loads((ROOT/"assets/motion-decision-patterns.json").read_text("utf-8"))

 def test_repository_contract(self):self.assertEqual(validate_repository(),[])
 def test_four_modes_and_provenance(self):
  self.assertEqual({p["mode"] for p in self.sample["profiles"]},{"Operate","Persuade","Read","Experience"})
  self.assertEqual({p["decision"]["source"] for p in self.sample["profiles"]},{"unresolved","confirmed","delegated","inherited"})
 def mutated(self):return copy.deepcopy(self.sample)
 def test_unresolved_is_not_silently_none(self):
  d=self.mutated();d["profiles"][0]["decision"]["level"]="none"
  self.assertTrue(any("unresolved motion cannot" in e for e in validate_plan(d)))
 def test_new_design_must_ask_user(self):
  d=self.mutated();d["profiles"][0]["decision"]["question_asked"]=False
  self.assertTrue(any("requires user-facing" in e for e in validate_plan(d)))
 def test_cannot_start_optional_motion_before_answer(self):
  d=self.mutated();d["profiles"][0]["decision"]["optional_motion_started"]=True
  self.assertTrue(any("cannot start optional" in e for e in validate_plan(d)))
 def test_proposals_need_concrete_visual_effects(self):
  d=self.mutated();d["profiles"][0]["decision"]["proposals"][1]["preview"]="nice"
  self.assertTrue(any("visible behavior" in e for e in validate_plan(d)))
 def test_delegation_needs_explicit_user_authorization(self):
  d=self.mutated();d["profiles"][2]["decision"]["user_evidence"]=None
  self.assertTrue(any("cite user's explicit statement" in e for e in validate_plan(d)))
 def test_selected_no_motion_still_has_feedback(self):
  d=self.mutated();d["profiles"][3]["feedback_baseline"]=[]
  self.assertTrue(any("essential visible feedback" in e for e in validate_plan(d)))
 def test_reduced_motion_cannot_be_omitted(self):
  d=self.mutated();d["profiles"][1]["interactions"][0]["reduced_motion"]=""
  self.assertTrue(any("reduced-motion" in e for e in validate_plan(d)))
 def test_interactions_are_interruptible(self):
  d=self.mutated();d["profiles"][2]["interactions"][0]["interruptible"]=False
  self.assertTrue(any("interruptible" in e for e in validate_plan(d)))
 def test_existing_policy_does_not_force_reconfirmation(self):
  p=next(p for p in self.sample["profiles"] if p["decision"]["source"]=="inherited")
  self.assertFalse(p["decision"]["question_asked"])
  self.assertEqual(validate_plan(self.sample),[])

if __name__=="__main__":unittest.main()
