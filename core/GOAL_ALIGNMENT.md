# Goal Alignment and Proxy Integrity (GAPI)

This protocol complements CR/DF/CRL/MNG. It is **domain-independent**: the owning project supplies scientific objectives and operational acceptance rules. A local experiment is never allowed to redefine the project's ultimate objective by default.

## The three-level goal contract

1. **North-star scientific question**: what causal/mechanistic fact or capability would matter if every current implementation were discarded?
2. **Terminal deliverables**: the real-world/evaluable outcome, deployment constraints, quality, cost, originality, robustness and independent evidence required. Record each denominator, comparator, and evaluation distribution.
3. **Diagnostic proxies and phase gates**: convenient metrics and preregistered thresholds that determine what to study next. Record why each proxy is insufficient as terminal evidence.

A phase-specific gate is binding **for that preregistered experiment/candidate**. Failing it may close that instance. It does **not** establish universal impossibility or silently change the north-star objective. Project-level terminal constraints remain binding unless the user explicitly changes them.

For any new task, derive a goal-to-evidence chain:
scientific question -> necessary mechanism -> available pre-action information -> proposed action/algorithm -> actual execution cost -> downstream/terminal outcome -> novelty and external validity.
Mark every unverified arrow. Only the links relevant to the user's present question need deep analysis; do not turn this into a mandatory long essay.

## Proxy-to-goal firewall

Before interpreting an improved metric, answer:

- Which *arrow* of the goal-to-evidence chain did this metric actually measure?
- Was the comparator matched in information, compute, data exposure, architecture and hardware?
- Would the terminal objective improve if this local metric improved by another factor of two? State a reason or falsifier, not intuition.
- Is this teacher-forced, local, simulated, oracle, prior-exposed development, or genuinely free deployment behavior?
- What is the cheapest **bridge experiment** that would establish whether this proxy transfers? If no credible bridge exists, stop tuning the proxy and pivot representation/objective.

Use a **goal impact label**: DIRECT_TERMINAL, NECESSARY_MECHANISM, DISCRIMINATING_EVIDENCE, PROXY_ONLY, or NO_KNOWN_BRIDGE. These are reasoning labels, not measurements.

### Progress is not equivalent to improved metrics

Progress can be (a) a theorem or counterexample that removes a large search family, (b) a discovered source-level computation, (c) a genuinely discriminating negative experiment, (d) a mechanism-driven new candidate with a falsifiable distinction, or (e) deployment evidence. It is *not* additional seeds, longer tuning, a prettier loss plot, or larger documentation absent a changed decision.

## Dual-loop research

**Discovery loop:** CR -> DF -> competing mechanisms -> minimum discriminator -> search for a different mathematical representation or operator. Can continue after a registered method is closed without modifying its status.

**Delivery loop:** preregister a candidate -> equal-budget controls -> native validation -> independent terminal validation -> audit novelty. This loop preserves hard gates and failure receipts.

At every iteration ask whether the discovery loop's highest-impact unknown changed. If not, the delivery loop's recent local target must not automatically become the next north star.

## Anti-drift checkpoints

Trigger a goal audit on:
- a negative registered test;
- a large proxy improvement without terminal corroboration;
- repeated tuning of the same method family;
- a candidate that changes the measured denominator, comparator, or source split;
- a refocus from mechanism research to compensation or engineering convenience;
- a paper review which tempts an unexamined recipe copy.

Output one sentence for goal continuity, one for what the evidence actually changed, one for the next decisive branch. Extensive audits are for genuine scope changes, not every answer.

## Boundaries

Anti-defensiveness is **not** optimism bias. Do not fabricate counterfactual measurements, lift a limited negative result into a theorem, bypass original controls, or relax a frozen gate after seeing the outcome. If the mathematical question is already conditionally solved, use ACCEPT_CONDITIONAL instead of inventing experiments. If resources, access, legality or user authorization block action, use DEFER with an exact dependency and feasible analysis that remains; never covertly spend resources.

The research_state optional goal_contract/research_moves extension can log this protocol. Older v2.1 states without it remain valid.