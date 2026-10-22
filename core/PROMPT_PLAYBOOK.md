# Task-adaptive prompt playbook

Use the short **resident instructions** in AGENTS.md or chatgpt/PROJECT_INSTRUCTIONS.md. Load **only one or two** prompts below when triggered. Sending every prompt on every turn causes rigidity and repeats the same audit instead of doing research. These are reusable text instructions, not claims of improved model behavior.

## G0 / North-star recovery (metric drift, after a long experiment sequence)

> State the project's original scientific question, terminal acceptance evidence, deployed cost and independent comparator. Classify today's metric as DIRECT_TERMINAL, NECESSARY_MECHANISM, DISCRIMINATING_EVIDENCE, PROXY_ONLY or NO_KNOWN_BRIDGE. Identify the weakest causal arrow from metric to the goal and the cheapest test of that arrow. Do not treat the most recent experiment as the new mission. Preserve every frozen acceptance rule.

## D1 / Interrupt defensive stalling

> You wrote "confounded", "insufficient evidence" or "not proven". Identify exactly which inference is threatened and its evidence. Provide the strongest valid conditional claim, two competing causes with different predictions if uncertainty remains, one minimal discriminator and the decision under each outcome. Do not inflate a caveat into a veto; do not invent observations.

## N2 / Expand after a negative result

> Precisely encode the rejected tuple: object, input, numerical path, intervention/action set, target, budget, comparator, split, result. List what is excluded and what remains open. Propose one genuinely different representation/information source/action/causal objective, explain which obstruction it changes, and identify the strongest simple counterexample that might still defeat it. Do not restart the same search with more seeds/rank/thresholds.

## M3 / First-principles structure discovery

> From actual version-locked source and tensor semantics, independently derive the object's identities, coupling, symmetries, nullspaces, noncommutativity, sensitivities and computational lower bounds. Identify one hidden structural degree of freedom and one adverse case. Derive an intervention *before* citing familiar recipes; then check nearest prior art and a matched simple baseline.

## B4 / Bridge proxy to deployment

> Identify where this improved proxy lies in the real causal/deployment computation graph. Compare oracle inputs against signals available before the intended skip/action. Include selection, quantization, layout and correction cost in an optimistic bound before larger experiments. Give one minimal bridge experiment and the outcome that would stop further proxy tuning.

## C5 / Distinguish explanations

> Construct at most three non-isomorphic mechanisms for the observed effect. For one shared controlled probe, give their differing mathematical/sign/shape/temporal predictions. Prefer an exact proof or replay of existing artifacts to expensive new work. Select based on decision value and resource cost; do not make up numeric information gain.

## T6 / Downstream harm and terminal quality

> Reconstruct how the local perturbation reaches the final output, including cross-element dependencies, state changes and nonlinearities. Contrast matched-magnitude perturbations with different directions/structures. Distinguish teacher-forced improvement from unconstrained deployment behavior. Propose an intervention that separates the most plausible causes of terminal degradation.

## P7 / Escape local optimum

> Identify whether three successive iterations changed only parameters of one method family. If so, compare its measured structural obstruction with at least one fundamentally different mathematical representation and one cheap baseline. State the condition under which the entire family should be stopped. Never reset a preregistered failure by changing labels.

## R8 / Rigorous stop without paralysis

> If the scoped question is mathematically settled, state the theorem, assumptions and boundary, then ACCEPT_CONDITIONAL. If empirical work is blocked by missing assets or authorization, DEFER that exact action and specify what can be concluded or analyzed now. Do not fabricate a new experiment simply to satisfy a "keep going" instruction.

## V9 / Final research handoff

> Report: north-star continuity; one strongest source/evidence-backed fact; exactly what changed in our mechanism beliefs; the selected cheapest decision-changing action or a rigorously closed question; limits on what was not observed; novelty and deployment status. Keep negative receipts and source links. Do not silently promote a proxy into a success claim.

## Routing

Source unclear -> CR. Algebra settles -> DF. Negative/uncertainty -> D1/N2/C5. Metric drift -> G0/B4/P7. New method -> M3. Terminal behavior -> T6. Blocked/closed -> R8. End of substantial research iteration -> V9.

Project-specific agents should extend these prompts with their *actual* object, observed failures, cost units, and acceptance gates; never rewrite the generic rules to match one checkpoint.