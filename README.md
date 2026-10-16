# AutoResearcher — GPT-6 mechanism-first research workflow

A portable, **research-methodology** package for Codex and ChatGPT Projects. Version **v2.1** (2026-10-16). This repository is the canonical source of the protocol. It is **not yet** an autonomous experiment executor or a demonstrated improvement to GPT-6.

## Four mandatory behaviors

| Layer | Purpose | Failure prevented |
| --- | --- | --- |
| CR — Computational Reconstruction | Rebuild the actual code-linked inputs, outputs, tensor semantics, operators, state, branches and downstream computation | Suggesting a method before understanding the object |
| DF — Deduction First | Derive exact structure, invariants, bounds and counterexamples before scheduling experiments | Redundant GPU experiments and low-information rejection |
| CRL — Constructive Resolution Loop | Turn decision-relevant uncertainty into proofs, counterexamples, inspections or discriminating experiments | Defensive epistemic paralysis |
| MNG — Mechanism-first Novelty Gate | Derive research candidates from the discovered mechanism, then compare with nearest prior work and classical controls | Defaulting to popular ready-made methods instead of discovery |

**Central invariant:** actual computational flow → mathematical structure → only residual empirical unknowns → mechanism-derived proposals → independent validation. A confounder is not a completed research task. Known techniques can serve as baselines or diagnostic tools, not unexamined novelty claims.

## Codex

Clone [Qesire/AutoResearcher](https://github.com/Qesire/AutoResearcher) and open it in Codex. Repository-root [AGENTS.md](AGENTS.md) supplies default instructions; [mechanism-research Skill](.agents/skills/mechanism-research/SKILL.md) supplies a repeatable task-specific workflow.

For another project, **merge rather than overwrite** the scientific parts of AGENTS.md and copy the skill and core/ files while preserving other project-specific build, resource and safety rules.

## ChatGPT web

In a dedicated ChatGPT Project, copy the contents of [chatgpt/PROJECT_INSTRUCTIONS.md](chatgpt/PROJECT_INSTRUCTIONS.md) into Project Instructions. Upload the relevant [core protocols](core) and the latest real state/handoff file. ChatGPT Projects **do not automatically sync** Codex's local workspace or cluster artifacts.

## Files

- [Computational reconstruction](core/OBJECT_RECONSTRUCTION.md), [deduction-first](core/DEDUCTION_FIRST.md), [constructive research loop](core/RESEARCH_PROTOCOL.md), [novelty guard](core/NOVELTY_GATE.md)
- [Cross-client handoff](core/HANDOFF_FORMAT.md), [v2.0 migration](core/MIGRATION_v2_to_v21.md)
- [Research state JSON Schema](schemas/research_state.schema.json) and [semantic validator](scripts/validate.py)
- [Illustrative planned-experiment state](examples/research_state.json), [illustrative deduction-only state](examples/deduction_only_state.json), [human handoff example](examples/HANDOFF.md)
- [Behavioral evaluation cases](tests/BEHAVIOR_EVALUATION.md), [unit tests](tests/test_validate.py), [CI workflow](.github/workflows/validate.yml)

## Local checks

Requires Python 3.9+.

~~~bash
python -m pip install -r requirements.txt
python scripts/validate.py examples/research_state.json examples/deduction_only_state.json
python -m unittest discover -s tests -p 'test_*.py' -v
~~~

The examples are **fictional illustrations, not real experiments**. Schema validation catches malformed records and selected false status transitions, not mathematical mistakes, literature novelty, unverified citations or actual AI research behavior. Evaluate GPT-6 with the cases in tests/BEHAVIOR_EVALUATION.md before relying on the protocol.

## Recommended usage

1. Pin actual source revision and reconstruct the full relevant computational path plus the focal subgraph.
2. Derive exact structure, conditional theorems and counterexamples, stopping solved subquestions without unnecessary experiments.
3. Keep at most a few falsifiable competing mechanisms and run minimal causal probes only for residual unknowns.
4. Independently derive an intervention, inspect nearest prior work, compare matched controls and instrument real outcome metrics.
5. Save provenance and failure paths in a project-specific research state, validate it, and version changes in Git.

This repository contains no private cluster credentials, proprietary datasets or actual FFN experimental measurements. Preserve provenance and obtain authorization before spending compute or modifying external systems.

## Research references

- Rethlas adaptive research trajectory in Appendix A: [arXiv:2610.05781](https://arxiv.org/abs/2610.05781)
- FunSearch: [Nature 2023](https://www.nature.com/articles/s41586-023-06924-6)
- AlphaEvolve: [Google DeepMind](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)

These references inspire workflow mechanisms; none establishes that this package alone improves GPT-6.
