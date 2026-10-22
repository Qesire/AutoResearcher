"""GAPI/MEAR state invariants. These tests do not evaluate model research quality."""
import copy
import json
import unittest
from pathlib import Path

from scripts.validate import ResearchStateError, validate_state

ROOT = Path(__file__).resolve().parents[1]


def fixture():
    return json.loads((ROOT / "examples" / "research_state.json").read_text(encoding="utf-8"))


class ExpansionStateTests(unittest.TestCase):
    def test_optional_extension_backwards_compatible(self):
        state = fixture()
        state.pop("goal_contract")
        state.pop("research_moves")
        validate_state(state)

    def test_extended_illustrative_example_passes(self):
        validate_state(fixture())

    def test_move_needs_goal(self):
        state = fixture()
        state.pop("goal_contract")
        with self.assertRaisesRegex(ResearchStateError, "require a goal_contract"):
            validate_state(state)

    def test_unlinked_terminal_criterion(self):
        state = fixture()
        state["research_moves"][0]["goal_criterion_ids"] = ["imaginary"]
        with self.assertRaisesRegex(ResearchStateError, "unknown terminal"):
            validate_state(state)

    def test_duplicate_goal_criterion(self):
        state = fixture()
        state["goal_contract"]["terminal_criteria"].append(
            copy.deepcopy(state["goal_contract"]["terminal_criteria"][0]))
        with self.assertRaisesRegex(ResearchStateError, "duplicate terminal criterion"):
            validate_state(state)

    def test_duplicate_research_move(self):
        state = fixture()
        state["research_moves"].append(copy.deepcopy(state["research_moves"][0]))
        with self.assertRaisesRegex(ResearchStateError, "duplicate research move"):
            validate_state(state)

    def test_proxy_improvement_requires_proxy_link(self):
        state = fixture()
        state["research_moves"][0].pop("proxy_metric_id")
        with self.assertRaisesRegex(ResearchStateError, "requires a proxy"):
            validate_state(state)

    def test_proxy_reference_must_exist(self):
        state = fixture()
        state["research_moves"][0]["proxy_metric_id"] = "unknown-proxy"
        with self.assertRaisesRegex(ResearchStateError, "unknown proxy"):
            validate_state(state)

    def test_negative_requires_precise_branch_scope(self):
        state = fixture()
        move = state["research_moves"][0]
        move["trigger"] = "NEGATIVE_RESULT"
        move.pop("proxy_metric_id")
        with self.assertRaisesRegex(ResearchStateError, "rejection scope"):
            validate_state(state)

    def test_negative_must_reference_existing_branch(self):
        state = fixture()
        move = state["research_moves"][0]
        move["trigger"] = "NEGATIVE_RESULT"
        move["prior_branch_id"] = "missing-branch"
        move["rejected_scope"] = "hypothetical limited mask"
        with self.assertRaisesRegex(ResearchStateError, "unknown rejected branch"):
            validate_state(state)

    def test_scoped_negative_can_open_distinct_research_move(self):
        state = fixture()
        state["branches"].append({
            "id": "closed-local", "failure": "Old fixed subset failed",
            "lesson": "Does not decide alternative representation"})
        move = state["research_moves"][0]
        move["trigger"] = "NEGATIVE_RESULT"
        move.pop("proxy_metric_id")
        move["prior_branch_id"] = "closed-local"
        move["rejected_scope"] = "specific fixed support on this symbolic W"
        validate_state(state)

    def test_distinguish_competing_mechanism_predictions(self):
        state = fixture()
        move = state["research_moves"][0]
        move["competing_mechanisms"][1]["prediction"] = move["competing_mechanisms"][0]["prediction"].upper()
        with self.assertRaisesRegex(ResearchStateError, "indistinguishable"):
            validate_state(state)

    def test_do_not_promote_proposal_to_observation(self):
        state = fixture()
        state["research_moves"][0]["status"] = "OBSERVED"
        with self.assertRaisesRegex(ResearchStateError, "trace/artifact"):
            validate_state(state)

    def test_observed_requires_relevant_evidence(self):
        state = fixture()
        move = state["research_moves"][0]
        move["status"] = "OBSERVED"
        move["evidence"] = [{"kind": "REFERENCE", "locator": "paper reference"}]
        with self.assertRaisesRegex(ResearchStateError, "trace/artifact"):
            validate_state(state)
        move["evidence"].append({"kind": "TRACE", "locator": "illustrative trace placeholder"})
        validate_state(state)


if __name__ == "__main__":
    unittest.main()
