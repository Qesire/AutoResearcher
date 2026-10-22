---
name: mechanism-research
description: Reconstruct actual model computation, derive structural results and investigate remaining unknowns before proposing novel interventions.
---
# Mechanism Research (CR / DF / CRL / MNG)

1. MAP_FLOW: inspect version-pinned source code, configurations, tensor I/O, shapes and semantics, operator ordering, branches, state, nonlinearities, residuals and downstream consumers. Explicitly mark unknown edges.
2. DERIVE: translate verified flow to equations. Work out exact identities, conditions, bounds, nullspaces, sensitivities, counterexamples and constraints. A mathematical answer terminates the scoped subquestion; do not spend GPU experiments restating it.
3. DISCRIMINATE: for genuine empirical unknowns, propose distinct mechanisms with concrete predictions and choose the cheapest decisive intervention, static check or experiment. Identify controls, measurements and possible next decisions.
4. INNOVATE: independently derive methods from observed computational structure *before* defaulting to standard smoothing, regularization, pruning, EMA or distillation recipes. Audit nearest prior work to establish any genuine contribution. Known approaches remain appropriate baselines or diagnostic probes.
5. VERIFY: criticism must identify an inference at risk and provide a test, counterexample or repair. Do not terminate on unverified caveats. Do not suppress real contradictions.
6. RECORD: preserve proof assumptions, source locators, raw evidence, negative branch lessons, novelty status and next action.
7. GOAL_CHECK: when a local metric improves, or a registered candidate fails, verify that the project's true scientific question and terminal evaluation have not been replaced by this metric. Distinguish scoped closure from general mechanism rejection. On drift, invoke research-expansion skill (GAPI/MEAR) and the task-specific prompt playbook. Never confuse planned experiments with observed runs.

Adaptive routes: MAP_FLOW, DERIVE, STATIC_CHECK, EXPERIMENT, DESIGN, REPAIR, PIVOT, ACCEPT_CONDITIONAL, DEFER.

Output: verified object and scope -> strongest mathematical/mechanistic result -> remaining unknown -> cheapest resolving action with predicted decision impact. Do not invent data, formal proof status or literature novelty.

On negative evidence, repeated parameter tuning, unclear causal attribution, or missing proxy-to-deployment bridge, read core/GOAL_ALIGNMENT.md and core/EXPANSION_PROTOCOL.md and use .agents/skills/research-expansion/SKILL.md. The mechanism skill remains the authority for source-grounded math and code reconstruction. The expansion skill does not authorize new model runs or modify frozen gates.
