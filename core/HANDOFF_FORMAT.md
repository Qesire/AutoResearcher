# Codex ↔ ChatGPT Handoff

This GitHub repository is the canonical versioned source for the behavior protocol. Codex does not automatically synchronize its working tree or cluster state to ChatGPT web Projects.

After each meaningful iteration, provide an evidence-backed research_state.json and HANDOFF.md. A handoff includes source commit and configuration, question scope, computational-flow coverage, proved claims and assumptions, actual observed results with artifact locators, proposed vs queued vs completed work, failed pathways, remaining unknowns, novelty status and next action.

Source hierarchy: original code/logs/artifacts > pinned validated structured state > researcher-reviewed handoff > chat summaries > agent conjectures. Preserve immutable run identifiers and avoid overwriting concurrent updates. Never promote illustrative samples into claimed evidence.

Use a PR to reconcile concurrent changes and explicitly import the updated state on the ChatGPT side.

## Goal and expansion handoff (optional v2.1-compatible)

For sustained work, include the north-star scientific question, immutable project acceptance criteria, known proxy metrics and their missing terminal bridges. Record any newly rejected branch with exact action/input/numerical/goal/cost/data scope, and any distinct exploration proposal with its structural delta, competing predictions, cheapest discriminator and negative-outcome decision. Use optional research_state goal_contract/research_moves objects if useful; legacy research_state v2.1 files remain supported. Never treat a proposed discriminating test as an observation.

## Optional PRD handoff

When a genuinely reusable problem reformulation was discovered, reference an optional representation_ledger.json alongside (not inside or instead of) research_state.json. For each rewrite record relation type (EXACT / CONDITIONAL / APPROXIMATE / TASK_REDUCTION / ANALOGY), mathematical scope, current-input and time dependencies, provenance, freed design variable, and cheapest discriminator. A mechanism taxonomy or literature relationship is a source of ideas, not an automatically validated novelty claim. Validate with python scripts/validate_representation.py examples/representation_ledger.json. Neither the ledger nor its fictional example changes research_state schema v2.1 or constitutes measured model evidence.

## Task-local context and prompt-version handoff

Provide [a compact evidence packet](../examples/RESEARCH_CONTEXT_PACKET.md) with the latest source/run locators and the one decision still open. If prompt experiments were run, preserve prompt revision, tool/model setting, representative traces and *actual* reviewer scores separately; see [paired prompt evaluation](PROMPT_EVALUATION.md). The handoff should allow direct continuation without repeatedly loading the entire project history.
