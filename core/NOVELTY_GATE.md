# Mechanism-first Novelty Gate (MNG)

A frequently seen failure is to select internet-famous solutions (smoothing, EMA, regularization, distillation, classic sparsity) immediately after observing an anomaly. This bypasses the computation-specific mechanism that could yield a genuinely new method.

Required ordering:
1. Reconstruct true computational structure and isolate an empirical phenomenon.
2. Extract algebraic constraints, invariants, sensitivity or dependency patterns.
3. **Independently construct** candidate interventions that follow from the mechanism.
4. Predict when each intervention must work, fail or differ from a simpler alternative.
5. Search nearest prior art and negative results, inspect official code where needed, and set matched known-method baselines.
6. Verify that the proposed difference lies in the operator, causal pathway, regime, or falsifiable behavior—not merely a renamed combination.
7. Require ablation, null-mechanism control and equal-budget comparison before claiming a useful new contribution.

Statuses: DIAGNOSTIC, BASELINE, CANDIDATE, DISTINCT_PREDICTION, AUDITED, VALIDATED. Neither a high metric nor a self-awarded novelty score alone establishes scientific contribution. If the prior-art search is incomplete, use CANDIDATE rather than invent originality.

Existing techniques remain legitimate as controls, building blocks and sometimes the best deployment solution. They simply must not replace mechanism discovery by reflex.
