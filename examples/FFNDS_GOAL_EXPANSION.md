# FFNDS example: separating scientific scope from an experimental failure

**Pedagogical example only:** this file does not import live FFNDS run artifacts, override its state, or claim a newly tested method. All real metrics, closed IDs and decisions must be verified against FFNDS's pinned current evidence.

## Goal contract

**Scientific question:** in Wan2.2 four-step distilled video generation with native HiF4/W4A4 FFN execution, what input/state-dependent calculations can be avoided, with what inexpensive advance information, under what operator format and with what downstream visual consequences?

**Terminal comparator:** the exact same distilled, quantized dense runtime and independent sources, matched steps, conditioning and evaluation.

**Illustrative historical target gates (must check the actual project contract):** main GEMM MAC at most half of same D-Q dense, all scoped complete FFN calls accelerated at least 1.5x in aggregate, independently measured video aesthetics/imaging/motion no worse than 2% relative per metric. Separate official acceptance from additional background-flicker quality investigation. Passing gates cannot prove novelty.

## Distinct evidence types

- Fixed per-step widths are an engineering **static control**, not input-conditioned prediction.
- A hidden-support oracle computed after W1 cannot prove W1 was skipped.
- A local or frozen-state flow metric, including a true native output, cannot certify free student rollout/video quality.
- QDQ nonlinearities and rounding can defeat mask-before/after reordering; original BF16 and quantized distilled models need separate evidence.
- A particular masked tile layout's failure only closes that layout under its measured conditions.

## Example decision after a local proxy improves but terminal evidence fails

Observed (historical illustrative framing, not a new run): a fixed-flow proxy improves while the candidate is ineligible to advance.

**Not warranted:** "increase the number of updates until the proxy gate passes" or "all trajectory-level training is useless."

**Live alternatives:** (A) terminal mismatch is caused by state-feedback/recovery dynamics; (B) the particular candidate support/action space has too little freedom even under a better target; (C) quantization or GPU work negates the information gain. A vs B may be separated by evaluating free-vs-fixed trajectories with unchanged compute and an oracle upper bound on the existing action set. If an exact structural bound already rules out B's action set, close it without new GPU work. If the source lacks free rollout access, document that dependency.

**Structural expansion:** signed output subset geometry, differently executable supports, or an earlier low-cost predictor could change a binding obstruction. This is an agenda for falsification, not evidence these alternatives succeed.

**Research loop:** pin FFNDS and AutoResearcher revisions -> rebuild exact FFN boundary -> separate static/oracle/predictable/native paths -> minimum distinguishing checks -> real action/cost -> free rollout/quality -> nearest competing papers.

## How to use

Apply generic GAPI/MEAR to a different domain by substituting its own question, proxy-to-terminal graph, closed family and execution limits; do not import FFN-specific thresholds as AutoResearcher defaults.
