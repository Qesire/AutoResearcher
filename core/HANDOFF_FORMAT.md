# Codex ↔ ChatGPT Handoff

This GitHub repository is the canonical versioned source for the behavior protocol. Codex does not automatically synchronize its working tree or cluster state to ChatGPT web Projects.

After each meaningful iteration, provide an evidence-backed research_state.json and HANDOFF.md. A handoff includes source commit and configuration, question scope, computational-flow coverage, proved claims and assumptions, actual observed results with artifact locators, proposed vs queued vs completed work, failed pathways, remaining unknowns, novelty status and next action.

Source hierarchy: original code/logs/artifacts > pinned validated structured state > researcher-reviewed handoff > chat summaries > agent conjectures. Preserve immutable run identifiers and avoid overwriting concurrent updates. Never promote illustrative samples into claimed evidence.

Use a PR to reconcile concurrent changes and explicitly import the updated state on the ChatGPT side.
