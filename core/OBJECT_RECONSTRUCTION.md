# Computational Reconstruction (CR)

Research begins with the **actual implementation**, not a familiar textbook approximation.

Record exact repository commit, model/checkpoint, configuration, entrypoint, execution mode; inputs and outputs (shape, dimension meaning, dtype/device, numerical ranges when known); all research-relevant intermediate tensors and operators; mask, proxy, residual and nonlinear ordering; branches, conditioning, state, cache and randomness; and downstream path to the measured outcome.

Every relevant edge must have a source locator (file/symbol/line or trace), a validated equation, or an explicit UNKNOWN status. For large models, map the complete relevant end-to-end path and close the focal subgraph; do not falsely claim the whole model is mapped. Do not infer the implementation from model-family familiarity.

Write a minimal mathematically equivalent computation and verify dimensions and operation ordering. Distinguish selection logic from numerical computation and distinguish local error from later system-level consequences.

Deliver: pinned object identity, scoped computational graph, verified and unresolved edges, equivalent equations, and cheapest code inspection needed to close any decision-critical gap.
