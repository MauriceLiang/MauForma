"""Cross-domain reference learning and source-asset publication boundary tests."""
from __future__ import annotations
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_design_reference import validate_catalog,validate_repository,validate_public_example_files

class DesignReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog=json.loads((ROOT/"examples/design-reference-learning/reference-principles.json").read_text("utf8"))
    def cloned(self):return copy.deepcopy(self.catalog)
    def test_valid_repo_and_four_modes(self):
        self.assertEqual(validate_repository(),[])
        self.assertEqual({p["mode"] for p in self.catalog["profiles"]},{"Operate","Persuade","Read","Experience"})
    def test_source_media_denied(self):
        a=self.cloned();a["public_reference_media_allowed"]=True
        self.assertTrue(any("media is forbidden" in x for x in validate_catalog(a)))
    def test_demo_must_be_original(self):
        a=self.cloned();a["demo"]["source_provenance"]="copied-source"
        self.assertTrue(any("synthetic" in x for x in validate_catalog(a)))
    def test_no_image_variants(self):
        a=self.cloned();a["demo"]["image_policy"]="redacted-copy"
        self.assertTrue(any("reference images" in x for x in validate_catalog(a)))
    def test_insight_requires_context_and_transfer(self):
        a=self.cloned();a["profiles"][0]["insights"][0]["transfer_rule"]=""
        self.assertTrue(any("transfer_rule" in x for x in validate_catalog(a)))
    def test_research_is_cross_domain(self):
        a=self.cloned();a["profiles"].pop()
        self.assertTrue(any("all four" in x for x in validate_catalog(a,all_modes=True)))
    def test_original_demo_has_independent_details(self):
        self.assertGreaterEqual(len(self.catalog["demo"]["intentionally_different"]),3)
        self.assertEqual(validate_public_example_files(),[])
    def test_public_example_only_text_and_code(self):
        folders=[ROOT/"examples/design-reference-learning",ROOT/"examples/clean-enterprise-demo"]
        files=[p for folder in folders for p in folder.rglob("*") if p.is_file()]
        self.assertGreater(len(files),1)
        self.assertTrue(all(p.suffix in {".json",".html",".txt"} for p in files))

if __name__=="__main__":unittest.main()
