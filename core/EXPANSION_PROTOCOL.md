# Mechanism Expansion and Anti-Defensive Research (MEAR)

MEAR augments CR/DF/CRL/MNG and GAPI. Its purpose is to prevent (1) epistemic paralysis, (2) hyperparameter micro-optimization inside a failed mechanism, and (3) indiscriminate novelty churn. **It is not a license to override evidence or constraints.**

## A. Turn a real obstacle into a testable split

When someone says "cannot determine", "confounded", "too many risks", or "failed":

1. Name the **exact inference** endangered, and its evidence scope.
2. Preserve the **strongest established positive/negative fact**; derive what remains possible *within stated conditions*. Do not re-list generic caveats.
3. Generate two or three **causally distinct** explanations, not synonyms. Each must predict an observable divergence under the same controlled probe. If no two defensible explanations exist, state a conditional bound/counterexample and close that scoped question.
4. Identify the cheapest decision-changing action: algebra -> source/config inspection -> static/CPU test -> reuse existing artifacts -> minimal native probe -> large controlled experiment. Never insist on GPU if a theorem settles it.
5. Supply an A/B decision map: what will be built, rejected or redefined under each outcome. Avoid fabricated numerical information-gain scores.

A caveat becomes actionable only if it changes a claim, experiment or next decision. Otherwise omit it from the lead.

## B. Scope-precise negative memory

A closed branch is a tuple:
(object/version, input regime, action family and granularity, numerical operator and state, target and comparator, cost/quality gates, data split, evidence and conclusion).

- Retain and respect the tuple. A simple change in rank, q, pooling, kernel name or random seed does not constitute a new mechanism unless it demonstrably changes a binding constraint.
- Distinguish **rejected instance**, **rejected action family under a proved bound**, and **open scientific question**.
- A new proposal must expose a **structural delta** versus the nearest failed branch: information available before action; representation; action space; error geometry; objective; causal intervention; deployment primitive. Say which prior obstruction this changes and how a cheap test could show it fails anyway.
- Negative evidence narrows the search space. It does not automatically transfer across checkpoints, precisions, kernels, condition regimes, or distinct action families.

## C. Expansion axes (choose, do not enumerate blindly)

When the current mechanism stagnates, explore one or two axes with the strongest object-derived rationale:

- **Information timing:** can a previously computed signal predict the decision *before* the costly operation? An oracle with privileged information is not a deployable policy.
- **Mathematical representation:** signed sums/cancellation, nullspaces, noncommutative quantization, equivalence classes, spectral or geometric coordinates, structured approximate operators. Propose only structures supported by the object.
- **Action granularity:** token, group, tile, channel, layer, step or operator; distinguish mathematical zeros from hardware-elided work.
- **Causal horizon:** local loss vs downstream dynamics, feedback and terminal outcome; teacher forcing vs free rollout.
- **Environment:** dtype, checkpoint/lineage, conditioning, data distributions, hardware shape and bandwidth; isolate confounds rather than asserting a cause.
- **Learning intervention:** zero-shot, static calibration, small post-training, reparameterization or full training; account for training assumptions and inference cost.
- **Competing primitive:** equal-budget static baseline, functional compression, cache, fused kernel or other simpler alternative.

If none of the axes changes a necessary condition, stop proliferating candidates. Return to object reconstruction or report a rigorous boundary.

## D. Minimum-mechanism portfolio

Maintain at most three live, **non-isomorphic** hypotheses: not three versions of the same mask/regularizer. For each give:
observed anomaly -> causal model/equation -> distinguishing prediction -> cheapest falsifier -> deployment information and cost -> nearest historical failure and prior art.
Rank by expected ability to change the scientific decision, not an invented numeric score. Explicitly consider a simple baseline that may defeat the new idea.

Portfolio action is **not** necessarily EXPERIMENT. Derivation, static inspection and ACCEPT_CONDITIONAL are first-class outcomes. When results show a representation cannot meet a lower bound, PIVOT rather than widening its tuning grid.

## E. Prohibit common failure patterns

- **Defensive veto:** "uncertainty exists, so wait for more evidence." Replace with the exact blocked inference and a feasible discriminator; if inaccessible, DEFER precisely.
- **Local Goodhart loop:** "proxy score rose, so iterate." Show the bridge to terminal action; if absent, change metric or mechanism.
- **Sunk-cost rescue:** "old method almost passed." Respect its original failure and require a structural change before reopening it.
- **Shallow method recombination:** "use smoothing + distillation + LoRA." Derive necessity from actual computation, then test closest prior art.
- **Oracle leakage:** using future/full-compute values to justify savings from earlier compute. Mark as upper bound and identify what is online-observable.
- **Premature universal negative:** one checkpoint, limited support set or one quality axis fails -> all sparsity/training/caching fails. State exact quantified scope.
- **False dynamism:** fixed schedules or changed weight width called input-conditioned routing. Report structural category honestly.
- **Perpetual exploration:** always invent another mechanism even after a valid conclusion. Respect terminal proofs, irreducible cost bounds, and authorization.

## F. Output for a live investigation

Use a short, decision-oriented response:
**Goal and current scope -> strongest verified result -> precise obstruction -> 2 discriminable mechanisms (when needed) -> lowest-cost decisive action with conditional next decisions -> candidate/novelty/evidence level**.

Use a fuller portfolio only when the user requests a comprehensive plan. No obligatory boilerplate table. No pretending the agent has run tests it only proposed.

## G. Explicit pass/fail examples

**Bad:** "Local reconstruction loss improved; perhaps tune for another 100 epochs."
**Better:** "Local loss improved under fixed teacher input only. The goal bridge is free rollout. A one-source rollout with matched compute differentiates optimization headroom from rollout mismatch. Do not change the frozen held-out set after seeing it."

**Bad:** "A packed tile was almost fully occupied; dynamic sparsity is futile."
**Better:** "This tile closure was ineffective for this action granularity. Compare at equal cost an alternative operator representation or group placement justified by measured contribution geometry. Re-running the same tile with another threshold is not new evidence."

**Bad:** "A confounder prevents conclusions."
**Better:** "That confounder affects causal attribution of A versus B, not the observed result. Hold it fixed or use a common-input probe and state the OOD limitation; the outcome will choose between the two mechanisms."

**Bad:** "The study can never be conclusive."
**Better:** "The registered instance is conclusively rejected under its gate. The broader claim requires another distinct test; its cheapest action is ..."

## H. Evidence discipline

Keep observed, source-verified, proved conditional, simulated, and proposed status separate. Prior exposure of evaluation samples makes them development data. Keep claims traceable, preserve all negative receipts, and require independent validation for deployment/novelty. If the user did not authorize edits, compute, network writes or access, do not perform them.

This protocol is project-agnostic. See examples/FFNDS_GOAL_EXPANSION.md for a **non-executed** domain-specific example.