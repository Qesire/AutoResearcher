"""Static links/skill wiring for v2.4 research search; not live browsing or agent grading."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class WebResearchDiscoveryTests(unittest.TestCase):
    def test_default_research_routes_to_web_discovery(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        project = (ROOT / "chatgpt/PROJECT_INSTRUCTIONS.md").read_text(encoding="utf-8")
        for doc in (agents, project):
            self.assertIn("WEB_RESEARCH_DISCOVERY.md", doc)
            self.assertIn("web-research-discovery/SKILL.md", doc)

    def test_all_science_skills_route_to_deep_search(self):
        for name in ("mechanism-research", "research-expansion", "problem-reformulation"):
            content = (ROOT / ".agents/skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("../web-research-discovery/SKILL.md", content)
        skill = (ROOT / ".agents/skills/web-research-discovery/SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(skill, r"\A---\nname: web-research-discovery\ndescription: [^\n]+\n---\n")
        for phrase in ("BROAD SEARCH", "DEEP READ", "CHASE CITATIONS", "COMPARE"):
            self.assertIn(phrase, skill)

    def test_protocol_has_breadth_depth_counterexamples_and_offline_mode(self):
        p = (ROOT / "core/WEB_RESEARCH_DISCOVERY.md").read_text(encoding="utf-8")
        for phrase in ("backward", "forward", "primary", "counterexample", "Browsing unavailable", "actual"):
            self.assertIn(phrase.lower(), p.lower())
        eval_doc = (ROOT / "tests/BEHAVIOR_EVALUATION.md").read_text(encoding="utf-8")
        for case in ("WARD-A", "WARD-B", "WARD-C", "WARD-D"):
            self.assertIn(case, eval_doc)

    def test_research_schema_intact(self):
        schema = (ROOT / "schemas/research_state.schema.json").read_text(encoding="utf-8")
        self.assertIn("research_object", schema)


if __name__ == "__main__":
    unittest.main()
