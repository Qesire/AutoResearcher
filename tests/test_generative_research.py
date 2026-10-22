"""Generative-first state affordances. No LLM creativity claims are inferred."""
import copy
import json
import unittest
from pathlib import Path

from scripts.validate import ResearchStateError, validate_state

ROOT = Path(__file__).resolve().parents[1]


def example():
    return json.loads((ROOT / "examples" / "research_state.json").read_text(encoding="utf-8"))


class GenerativeResearchTests(unittest.TestCase):
    def test_four_or_more_early_ideas_are_valid(self):
        s = example()
        self.assertGreater(len(s["exploration_seeds"]), 3)
        self.assertTrue(all("goal_criterion_ids" not in item for item in s["exploration_seeds"]))
        validate_state(s)

    def test_sketches_do_not_require_goal_contract_or_formal_move(self):
        s = example()
        s.pop("goal_contract")
        s.pop("research_moves")
        self.assertGreater(len(s["exploration_seeds"]), 3)
        validate_state(s)

    def test_single_brief_hypothesis_is_enough_for_sketch(self):
        s = example()
        s.pop("goal_contract")
        s.pop("research_moves")
        s["exploration_seeds"] = [{"id":"idea", "question":"Could a different representation work?",
                                   "possible_mechanism":"A signed output decomposition changes the action."}]
        validate_state(s)

    def test_exploration_can_be_refined_without_registered_experiment(self):
        s = example()
        s.pop("goal_contract")
        s.pop("research_moves")
        s["exploration_seeds"][0]["status"] = "REFINED"
        s["exploration_seeds"][0]["next_inspection"] = "Inspect the exact operator graph"
        validate_state(s)

    def test_duplicate_idea_identity_rejected(self):
        s = example()
        s["exploration_seeds"].append(copy.deepcopy(s["exploration_seeds"][0]))
        with self.assertRaisesRegex(ResearchStateError, "duplicate exploration seed"):
            validate_state(s)

    def test_sketch_cannot_claim_measured_status(self):
        s = example()
        s["exploration_seeds"][0]["status"] = "OBSERVED"
        with self.assertRaises(ResearchStateError):
            validate_state(s)

    def test_registered_observed_move_still_requires_evidence(self):
        s = example()
        s["research_moves"][0]["status"] = "OBSERVED"
        with self.assertRaisesRegex(ResearchStateError, "trace/artifact"):
            validate_state(s)

    def test_project_prompt_has_explicit_exploration_and_claim_stages(self):
        agent = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        prompt = (ROOT / "chatgpt" / "PROJECT_INSTRUCTIONS.md").read_text(encoding="utf-8")
        playbook = (ROOT / "core" / "PROMPT_PLAYBOOK.md").read_text(encoding="utf-8")
        self.assertIn("EXPLORE", agent)
        self.assertIn("CLAIM", agent)
        self.assertIn("自由发散", prompt)
        self.assertIn("验证与宣称", prompt)
        self.assertIn("S0 / Generate an original mechanism", playbook)
        self.assertIn("X1 / Expand the mathematical action space", playbook)


if __name__ == "__main__":
    unittest.main()
