"""Executable semantic gates for the v2.1 research state; no scientific claims."""
import copy
import json
import unittest
from pathlib import Path

from scripts.validate import ResearchStateError, validate_state

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((ROOT / "examples" / name).read_text(encoding="utf-8"))


class StateTests(unittest.TestCase):
    def test_deduction_only_no_gpu(self):
        data = read("deduction_only_state.json")
        self.assertEqual(data["experiments"], [])
        validate_state(data)

    def test_planned_not_observed(self):
        data = read("research_state.json")
        self.assertEqual(data["experiments"][0]["status"], "PLANNED")
        validate_state(data)

    def test_observed_requires_artifact(self):
        data = read("research_state.json")
        data["experiments"][0]["status"] = "OBSERVED"
        with self.assertRaises(ResearchStateError):
            validate_state(data)

    def test_flow_must_have_nodes(self):
        data = read("research_state.json")
        data["research_object"]["edges"][0]["to"] = "unknown-node"
        with self.assertRaises(ResearchStateError):
            validate_state(data)

    def test_decision_cannot_cite_unknown_proof(self):
        data = read("deduction_only_state.json")
        data["decisions"][0]["derivation_ids"] = ["absent"]
        with self.assertRaises(ResearchStateError):
            validate_state(data)

    def test_unverified_source_cannot_claim_verified(self):
        data = read("deduction_only_state.json")
        data["research_object"]["nodes"][0]["verification"] = "SOURCE_VERIFIED"
        with self.assertRaises(ResearchStateError):
            validate_state(data)

    def test_novelty_audit_requires_prior_art(self):
        data = read("research_state.json")
        data["novelty"]["status"] = "AUDITED"
        with self.assertRaises(ResearchStateError):
            validate_state(data)

    def test_no_unresolved_critical_edge_in_closed_slice(self):
        data = read("deduction_only_state.json")
        data["research_object"]["unknown_edges"].append({
            "description": "missing residual path", "decision_relevant": True,
            "resolving_action": "inspect source"})
        with self.assertRaises(ResearchStateError):
            validate_state(data)


if __name__ == "__main__":
    unittest.main()
