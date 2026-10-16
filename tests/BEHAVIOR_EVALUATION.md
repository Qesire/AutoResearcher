# GPT-6 behavior regression evaluation

Use the same model configuration, input evidence and effort budget in control (no protocol) and intervention (AGENTS/Skill) runs. Review outputs blind where feasible and use independent reviewers. Report both wins and regressions.

## Case A: anti-DEP
Input: sparse video FFN stabilizes subjects but background light flickers. Expected: actual mechanism alternatives, one smallest discriminating intervention, A/B interpretations; not a list of generic confounders.

## Case B: computation-first
Input: propose optimization for an unfamiliar conditional FFN. Expected: asks to inspect/pins real source graph and tensor semantics before assuming textbook implementations.

## Case C: deduction-only
Input: masked projection y_m=W(m elementwise-multiplied h). Expected: exact error decomposition/condition and no redundant GPU experiment.

## Case D: negative result
Input: a channel proxy has poor selection correlation. Expected: identify which necessary relation failed, derive bounds or counterexample and propose a more constrained viable question; not an uninformative rejection.

## Case E: anti-copycat novelty
Input: high-frequency video light flicker in sparse generation. Expected: structural mechanisms and derived interventions before routine EMA/smoothing/distillation; known options may appear only as controls.

## Case F: verification
Input: reviewer suggests unspecified distribution shift. Expected: challenge the exact threatened inference and propose a targeted check; do not ignore confirmed counterexamples.

Scoring (0–5 each): source-grounded flow reconstruction, mathematical strength, mechanism discrimination, low experiment redundancy, genuine novelty distinction, response decision value, evidence integrity. Record qualitative reasons and cases where protocol caused harm. Passing an automated schema validator is not a substitute for this empirical behavior evaluation.
