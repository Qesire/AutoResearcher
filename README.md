# CR/DF/CRL/MNG v2.1 — portable GPT-6 mechanism-first research workflow

A ready-to-copy **instruction + state-schema + validator + behavioral-evaluation** package for Codex and ChatGPT Projects. This bundle is an engineered starting point, **not** a proven improvement to GPT-6 and **not** an autonomous research service.

## Scientific operating model

1. **CR**: reconstruct input/output/state and a version-pinned source-linked computational graph before methods.
2. **DF**: derive exact structure, inequalities and counterexamples before expending experimental budget. Stop when a conditional proposition is proved.
3. **CRL**: important uncertainty → discriminatory research action, not disclaimers.
4. **MNG**: computation-derived causal hypothesis → independent constructive proposal → nearest-prior-art check → matched evaluator.
5. **Evidence ledger**: explicit, machine-readable hypothesis/experiment/claim status prevents passing a speculation off as a result.
6. **Adversarial evaluation**: test anti-DEP, anti-copycat, metric-gaming and real-blocker behavior on historical cases.

References and derivation: `core/OBJECT_RECONSTRUCTION.md`, `core/DEDUCTION_FIRST.md`, `core/RESEARCH_PROTOCOL.md`, `core/NOVELTY_GATE.md`. Cross-client handoff: `core/HANDOFF_FORMAT.md`.

## Package map

```
AGENTS.md                                 Codex repo-root always-on instructions
.agents/skills/mechanism-research/SKILL.md Codex/ChatGPT reusable skill content
chatgpt/PROJECT_INSTRUCTIONS.md          concise ChatGPT project instructions
core/OBJECT_RECONSTRUCTION.md           source-linked I/O and computational graph contract
core/DEDUCTION_FIRST.md                 mathematical derivation and no-redundant-experiment gate
core/RESEARCH_PROTOCOL.md                full adaptive research loop
core/NOVELTY_GATE.md                      mechanism-first literature / novelty guard
core/HANDOFF_FORMAT.md                    cross-client exchange specification
core/MIGRATION_v2_to_v21.md              versioned state migration rules
schemas/research_state.schema.json       machine-readable contract (JSON Schema)
examples/research_state.json             illustrative partial flow + conditional math + planned probe
examples/deduction_only_state.json        mathematically closed subquestion, no experiment
examples/HANDOFF.md                       illustrated handoff, zero runs claimed
scripts/validate.py                       structural and cross-reference validator
tests/test_validate.py                    automated schema regression checks
tests/BEHAVIOR_EVALUATION.md              manual model behavior regression fixtures
```

## Codex installation (recommended per repository)

From your repository root, copy:
- `AGENTS.md` to `<repo>/AGENTS.md` (merge if an AGENTS.md already exists; don't overwrite other repository safety/deployment rules).
- `.agents/skills/mechanism-research/` to `<repo>/.agents/skills/mechanism-research/`.
- `core/`, `schemas/`, `scripts/` to `<repo>`; keep paths intact. Optionally copy `tests/` and `examples/`.
- Copy `examples/research_state.json` to `<repo>/research_state.json` only as a **demonstration**, then replace its illustrative observations with actual sourced evidence. Never treat it as a completed experiment.

Codex loads a repository-root `AGENTS.md` as part of its standard instruction discovery and can discover `.agents/skills` in its path. Start a new session after changing `AGENTS.md`. Invoke the skill as `$mechanism-research` if necessary; otherwise it may be selected implicitly by matching the description. If a user-level policy is desired across repos, merge the two mandatory behaviors into `~/.codex/AGENTS.md`, **without** making every software task into speculative scientific discovery.

Check the active instructions using an ordinary Codex session; do not assume the file is in effect just because it exists. See https://learn.chatgpt.com/docs/agent-configuration/agents-md and https://learn.chatgpt.com/docs/build-skills.

## ChatGPT web installation

1. Create a dedicated ChatGPT Project for each research topic or laboratory workstream.
2. Open Project settings and paste the **contents** of `chatgpt/PROJECT_INSTRUCTIONS.md` into Project Instructions.
3. Upload `core/OBJECT_RECONSTRUCTION.md`, `core/DEDUCTION_FIRST.md`, `core/RESEARCH_PROTOCOL.md`, `core/NOVELTY_GATE.md`, `core/HANDOFF_FORMAT.md` and the **latest actual** `research_state.json`/`HANDOFF.md` as project files. The provided files under `examples/` are demonstrations only.
4. At each new analysis task, tell the model which state snapshot is current. For longer work, keep the running version in a repository and upload new snapshots when changed.

Projects **do not** automatically read or synchronize local Codex folders. ChatGPT web may reason and help plan experiments without having shell access to your cluster. See https://openai.com/academy/projects/ and https://learn.chatgpt.com/docs/projects.

## Validation

Python 3.9+ and `jsonschema` are required for the complete schema validator:

```
python -m pip install jsonschema
python scripts/validate.py examples/research_state.json
python scripts/validate.py examples/deduction_only_state.json
python -m unittest discover -s tests -p 'test_*.py'
```

For the actual project state (after you copy and edit it):

```
python scripts/validate.py research_state.json
```

State schema v2.1 is **not** backwards compatible with v2.0: follow `core/MIGRATION_v2_to_v21.md` to preserve prior evidence without inventing flow or proofs. Passing validates schema, references, computational-graph IDs, conditional termination, and a few other invariants. It **does not** validate scientific truth, citations, originality, experimental controls, or an LLM's behavior. Run `tests/BEHAVIOR_EVALUATION.md` as a paired evaluation before trusting the protocol.

## Research cycle and artifact discipline

1. **Reconstruct actual computation** from revisioned source: I/O, shapes, internal ops, gating, conditioning, state, numerical/runtime path. Record unknown edges instead of guessing.
2. **Derive** exact equivalent expressions, bounds, nullspaces, counterexamples and failure regimes; terminate the algebraic subquestion when resolved.
3. **Discriminate** only remaining empirical unknowns with the least costly causal probes and preregistered interpretations.
4. **Innovate** from the observed mathematical/causal structure, then review prior art, controls and novelty claims.
5. Run only authorized experiments, capture raw evidence, validate state, update handoff, checkpoint in Git, and explicitly sync to ChatGPT.

### Evidence authority

Raw artifacts / logs > validated machine-readable state grounded in artifacts > researcher-approved handoff > free-form chat summary > model inference. Never overwrite experimental records with plausible prose. Do not mark `completed` when a job was merely scheduled or submitted.

## What this package does not automate

- It does not create ChatGPT Projects, install a skill in your account, or sync files across ChatGPT and Codex.
- It does not schedule research tasks or run GPU jobs.
- It does not determine true research novelty without literature review.
- It does not mathematically verify arbitrary model-generated derivations, prove a research method works, or check that an uploaded code revision is genuine. It provides controls and a method for testing whether the model's behavior improves.

Version: v2.1, design date 2026-10-16. Published to Qesire/AutoResearcher.

## Repository

This repository is published at https://github.com/Qesire/AutoResearcher. Keep the research protocol and state changes versioned here. See `chatgpt/PROJECT_INSTRUCTIONS.md` for web deployment.
