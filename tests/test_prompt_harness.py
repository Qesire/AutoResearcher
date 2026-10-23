"""Static harness contracts and review aggregator tests; not live agent behavior evals."""
import copy
from pathlib import Path
import unittest

from scripts.compare_prompt_reviews import ReviewError, compare

ROOT = Path(__file__).resolve().parents[1]
D = {"mechanism": 3, "math": 4, "decision": 3, "evidence": 4, "efficiency": 2}


class PromptHarnessTests(unittest.TestCase):
    def test_entrypoint_is_compact_and_links_to_protocol(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertLess(len(agents), 4500)
        for path in ("core/AGENT_HARNESS.md", "core/PROMPT_PLAYBOOK.md",
                     ".agents/skills/problem-reformulation/SKILL.md"):
            self.assertIn(path, agents)
            self.assertTrue((ROOT / path).is_file())

    def test_packet_example_and_evaluation_refs_exist(self):
        for name in ("core/AGENT_HARNESS.md", "core/PROMPT_EVALUATION.md",
                     "examples/RESEARCH_CONTEXT_PACKET.md"):
            self.assertTrue((ROOT / name).is_file())
        text = (ROOT / "core/PROMPT_PLAYBOOK.md").read_text(encoding="utf-8")
        self.assertIn("## Context assembly", text)
        self.assertIn("## Two contrastive examples", text)

    def test_paired_review_report(self):
        data = {"reviews": [
            {"case_id": "A", "baseline": D,
             "candidate": {**D, "mechanism": 5, "decision": 4},
             "critical_regression": False},
            {"case_id": "B", "baseline": D, "candidate": D,
             "critical_regression": True},
        ]}
        r = compare(data)
        self.assertEqual(r["case_count"], 2)
        self.assertEqual(r["case_score_wins"]["candidate"], 1)
        self.assertEqual(r["case_score_wins"]["tie"], 1)
        self.assertEqual(r["critical_regression_case_ids"], ["B"])

    def test_duplicate_case_rejected(self):
        one = {"case_id": "A", "baseline": D, "candidate": D}
        with self.assertRaisesRegex(ReviewError, "duplicate"):
            compare({"reviews": [one, copy.deepcopy(one)]})

    def test_invalid_score_rejected(self):
        bad = {"reviews": [{"case_id": "A", "baseline": D,
                            "candidate": {**D, "math": 6}}]}
        with self.assertRaisesRegex(ReviewError, "from 0 to 5"):
            compare(bad)

    def test_boolean_score_not_number(self):
        bad = {"reviews": [{"case_id": "A", "baseline": D,
                            "candidate": {**D, "math": True}}]}
        with self.assertRaises(ReviewError):
            compare(bad)


if __name__ == "__main__":
    unittest.main()
