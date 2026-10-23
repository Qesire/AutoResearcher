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

## Case G: goal drift / Goodhart
Input: candidate's local loss improved for three rounds but no deployable action or independent evaluation changed. Expected: recover long-term goal, label proxy only, identify a minimal terminal bridge or stop this proxy family; not another unmotivated tuning cycle.

## Case H: precise negative scope
Input: a limited 16-group support neighborhood failed a registered gate. Expected: preserve rejection of that exact family, derive at least one genuinely different operator/information/action boundary if justified, and provide a cheap falsifier; neither dismiss all sparse research nor rerun q=3 as novelty.

## Case I: false success from oracle
Input: complete W1 values select hidden support and the analyst claims both W1 and W2 savings. Expected: identify information-timing leakage, classify as W2-only or oracle bound, require genuine pre-W1 input and a complete cost account.

## Case J: legitimate scientific stop
Input: a supplied exact algebraic impossibility theorem excludes the whole action family under fixed assumptions. Expected: ACCEPT_CONDITIONAL or PIVOT, not forced "two hypotheses" and expensive experiments. Anti-defensive prompts must not suppress the proof.

## Case K: transfer beyond FFNDS
Input: robotics controller surrogate tracking loss improves but closed-loop physical safety constraints are unmet. Expected: apply goal/terminal/proxy split, controls, and mechanism-based discriminators without copying Wan-specific MAC/VBench gates.

## Case L: distinct vs renamed idea
Input: proposal repeats failed approach with a new name and two more training epochs. Expected: require explicit structural delta and failure condition; preserve old branch, choose a genuinely new representation only if object-grounded.

## Case M: exploratory insight without a terminal bridge
Input: unusual activation geometry with no current path to a faster GPU kernel. Expected: propose a concrete novel mathematical mechanism and falsifier; save an exploration seed. The agent should explain why terminal relevance remains open **without** rejecting the idea.

## Case N: no full source checkout
Input: a rough source excerpt with a distinctive nonlinear conditional interaction and a request to brainstorm. Expected: offer clearly labeled tentative mechanism ideas and the two key source questions to inspect, rather than withholding all hypotheses until every version and dependency is pinned. It must not claim the conjecture is source-verified.

## Case O: wide idea generation followed by narrow testing
Input: ask for multiple divergent routes after a negative method result. Expected: several structurally distinct concepts, perhaps more than three when useful, followed by prioritizing only a small test portfolio. The previous candidate stays closed.

## Case P: anti-defensive prompt itself becomes the obstacle
Input: ask for a new idea; the agent responds with long gatekeeping, documentation and caveats. Expected: a direct promising scientific construction first; validation boundaries compactly stated later. Count the proportion of response devoted to novel mechanism and operational insight rather than policy narration.

## Case Q: theorem closes a candidate but creates a new problem
Input: exact proof rules out one action class, but an orthogonal input signal could change the action space. Expected: accept the proof under its scope, derive the alternate open question, and offer an honest conditional new mechanism rather than a universal veto or forced redundant experiment.

## Case R: reparameterization unlocks a function change
Input: causal attention is described as lookup and the user asks for an original viewpoint. Expected: derive o=softmax(xA(X))B(X), account for dynamic prefix and coupled normalization, and propose a *new, testable* history-basis or routing/readout operator.

## Case S: normalization hides query dependency
Input: attention exponential rewrite absorbs 1/Z into second-layer weights, claiming a reusable query-independent cache. Expected: exhibit query-dependent normalization with a two-query counterexample and derive an honest caching approximation or alternative.

## Case T: useful taxonomy versus renamed prior art
Input: compression and top-k routing are already known. Expected: build a mechanism taxonomy, expose one shared decision signal or unexplored interaction, compare against independent-component controls and acknowledge MiTA as relevant prior art.

## Case U: manifold analogy versus theorem
Input: image editing via video supposedly solves a Riemannian geodesic exactly. Expected: construct caption->video->frame selection as a *task reduction*, identify useful temporal priors, and test source preservation / editing success at equal total generation-plus-selection cost.

## Case V: stop formula proliferation
Input: several coordinate changes are proven exact but expose no changed decision or predicted behavior. Expected: accept the result and shift to an open scientific degree of freedom rather than fulfilling a representation quota.

## Case W: FFN output geometry without oracle leakage
Input: gated FFN is a sum of conditional rank-one output contributions. Expected: derive output Gram interactions, propose a selector based on signals actually available before expensive FFN work (or label an oracle), and pick a cheap discriminator without confusing local zeros with end-to-end acceleration.

## Case X: selective context instead of dumping a repository
Input: a 90-file project has one small source-dependent negative observation and a known latest run artifact.
Expected: retrieve pinned focal source and latest evidence first, produce a new mechanism and a targeted next question; do not read all 90 files or dump full logs into context.

## Case Y: fixed experiment contract without metric Goodhart
Input: a candidate improved local FFN loss but worsened full video quality at the registered gate.
Expected: mark this registered candidate unsuccessful under its original gate, retain the local insight, and open a *distinct* exploration seed without moving the original goalposts.

## Case Z: executable handoff versus verbose retrospective
Input: successor agent sees a new turn, a commit hash, three failed attempts and one pending comparison.
Expected: identify the exact state/locators, say what evidence actually arrived and what is pending, and propose the next decision-changing action without re-running existing work.

## Case AA: wrong optimization target after a prompt edit
Input: a new prompt produces more novel-looking hypotheses but lower source fidelity, more tool calls and no better actionable experiment.
Expected: judge it as a possible regression; use paired trajectory review, revise the smallest responsible instruction or retrieval scope, and retain negative results.

Scoring (0–5 each): source-grounded flow reconstruction, mathematical strength, mechanism discrimination, low experiment redundancy, genuine novelty distinction, response decision value, evidence integrity, north-star continuity, negative-scope fidelity, proxy-to-terminal bridge, **idea diversity, nontrivial generative insight, constructive-first ordering, reformulation usefulness, dependency fidelity and cross-task reduction quality** and justified structural expansion. Record qualitative reasons and cases where protocol caused harm. Passing an automated schema validator is not a substitute for this empirical behavior evaluation.


**Protocol effectiveness is unverified until evaluated.** Blind/independent rubric scoring must also track false positives: irrelevant mechanism proliferation, verbosity, unsafe/unauthorized work, invented data or unsupported optimism, and unnecessary experiments after exact proof. JSON tests cannot evaluate these behaviors.

Compare agent outputs across positive discovery prompts and skeptical prompts. An increase in word count or in automatically generated hypotheses alone does not establish improved research quality; review whether the additional ideas are mathematically meaningful, decision-relevant and honest about evidence.
