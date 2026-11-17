"""Mutation regression tests for universal card-edge accent style policy."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_surface_edge_accent import validate_cases, validate_repo


class SurfaceEdgeAccentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(
            (ROOT / "assets/surface-edge-accent-cases.json").read_text(encoding="utf-8")
        )

    def test_repo_contract(self) -> None:
        self.assertEqual(validate_repo(), [])

    def test_synthetic_cases(self) -> None:
        self.assertEqual(validate_cases(self.fixture), [])

    def mutate(self, cid: str, **updates) -> list[str]:
        data = copy.deepcopy(self.fixture)
        case = next(c for c in data["cases"] if c["id"] == cid)
        case.update(updates)
        return validate_cases(data)

    def test_legacy_attached_border_cannot_be_grandfathered(self) -> None:
        self.assertTrue(self.mutate("legacy-panel-left-border", expected="accept"))

    def test_pseudo_element_cannot_bypass_rejection(self) -> None:
        self.assertTrue(self.mutate("new-card-pseudo-before", expected="accept"))

    def test_inset_shadow_cannot_bypass_rejection(self) -> None:
        self.assertTrue(self.mutate("legacy-card-inset-shadow", expected="accept"))

    def test_adjacent_external_node_cannot_bypass_rejection(self) -> None:
        self.assertTrue(self.mutate("legacy-panel-external-node-overlap", expected="accept"))

    def test_rail_needs_visible_gap(self) -> None:
        self.assertTrue(self.mutate("new-card-external-gap", gap_px=0))
        self.assertTrue(self.mutate("new-card-external-gap", gap_px=2))

    def test_rail_needs_purpose(self) -> None:
        self.assertTrue(self.mutate("new-card-external-gap", meaningful=False))

    def test_legitimate_focus_outline_is_not_deleted(self) -> None:
        self.assertTrue(self.mutate("new-card-focus-outline", expected="reject"))

    def test_data_chart_is_not_card_edge_decoration(self) -> None:
        self.assertTrue(self.mutate("semantic-chart-bar", expected="reject"))

    def test_status_cannot_excuse_attached_card_border(self) -> None:
        self.assertTrue(self.mutate("new-panel-status-flush", expected="accept"))

    def test_both_lifecycles_are_required(self) -> None:
        data = copy.deepcopy(self.fixture)
        data["cases"] = [c for c in data["cases"] if c["lifecycle"] == "new"]
        self.assertTrue(validate_cases(data))


if __name__ == "__main__":
    unittest.main()
