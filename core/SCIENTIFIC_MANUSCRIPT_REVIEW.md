# Scientific manuscript composition and reviewer-grade QA

Use with [scientific-writing Skill](../.agents/skills/scientific-writing/SKILL.md) and [constructive scientific expression](CONSTRUCTIVE_SCIENTIFIC_EXPRESSION.md). Scientific validity and narrative argument take priority; typographical checks complete the manuscript. Review against the target venue's author instructions, article class and reference style. When no venue is set, use internally consistent scholarly defaults and mark venue-specific choices for final verification.

## 1. Scientific argument and credible contribution

**R03 — Actual application.** In the abstract of application-motivated work, identify the real task, system/user, relevant operating conditions and why the proposed intervention matters. Verify that the combined constraints describe a plausible or documented setting; do not create artificial conjunctions merely to imply a new gap. A purely theoretical paper can lead with its mathematical problem instead.

**R04 — Gap and novelty.** The introduction should establish the field's current capability, the *nearest* relevant methods, a precise missing mechanism/condition/evidence, and the contribution that addresses it. Distinguish a new principle or representation, a legitimate new setting, a careful synthesis/integration, and a performance improvement. Analyze whether the proposed change alters a computation, assumption or predicted phenomenon rather than declaring novelty from wording or keywords. A useful integration should state what the combination enables and why separate components did not already demonstrate it.

**R05 — Experimental architecture.** Each study must answer an identifiable part of the central claim. Organize the sequence as a chain (feasibility → mechanism → ablation → robustness/terminal outcome) or as independent dimensions with a clear purpose. For each result, recover: research question → intervention and control → metric and statistical unit → observation → inference. Compare with matched budgets and relevant prior methods; tie local proxies to terminal outcomes when the paper makes such claims.

**R06 — Explanation and evidence boundaries.** Explain which mechanism or design assumption the data supports, which alternatives remain, where effects vary, and what negative results teach. Report magnitude, dispersion/uncertainty and practical meaning when available. Avoid a paragraph that repeats table numbers without interpretation. Use possibility language for a real hypothesis; describe directly measured results without unnecessary hedging. Keep failure modes and unsupportable extrapolations visible.

## 2. Mathematics and technical readability

**R01 — First-use formula notation.** In a formula-rich paper, explain every symbol the first time it occurs in a displayed formula using an adjacent `where` clause; include the relevant index ranges, object type, shape/domain and physical units as needed. Explain operators or nonstandard notation as well. Do not let a symbol silently change meaning in a later section. Keep the explanation compact: a clear first-use definition is preferable to repeating the same glossary below every equation.

For example:

```latex
\begin{equation}
  y_t = \sum_{j=1}^{K} \alpha_{t,j} W_j x_t .
\end{equation}
\noindent where $x_t\in\mathbb{R}^{p}$ is the input at step $t$;
$W_j\in\mathbb{R}^{d\times p}$ is the $j$-th component matrix;
$\alpha_{t,j}$ is its mixing weight; $K$ is the component count;
$j\in\{1,\ldots,K\}$ indexes components; and
$y_t\in\mathbb{R}^{d}$ is the output.
```

Also identify the range/meaning of (t) at its first use when the surrounding text has not already done so. In a real manuscript, match notation, punctuation and spacing to the template; `where` may be integrated into a sentence, but the first-use explanation must remain adjacent and explicit.

**R02 — First-use abbreviations.** Expand first occurrence as "full term (ACRONYM)" unless the venue prescribes a different convention. Check abstract and main text independently when each is read as a standalone entry. Avoid abbreviations that appear only once, except conventional notation required by the field.

**R09 — Shared equation numbers.** When a single number identifies a semantically unified system or collection of ordered relations, group the lines visibly; a left brace with an aligned environment is a useful default when it expresses one coupled system. If the lines are distinct sequential assignments, use an aligned derivation with arrows/step interpretation or separate equation numbers when a brace would imply a simultaneous system. Preserve true mathematical meaning over visual uniformity.

**R10 — Cross-media notation.** Match the exact variables, superscripts, subscripts, coordinate axes, dimensions, tensor shapes and definitions across formulas, body text, figures, captions, pseudocode and tables. Verify an apparent match refers to the same mathematical quantity, not just the same glyph.

## 3. Visual evidence and typesetting

**R07 — Figures.** Use consistent open/closed axis boxes, background/grid strength, fonts, line weight, ticks and color semantics for comparable figures. Prefer a color-blind-friendly palette and additionally distinguish method curves by markers or line styles. Use Times New Roman for figure text when the manuscript/template uses it; honor venue exceptions. Keep text sizes consistent and legible at final one- or two-column reproduction size. A legend should identify the actual method/metric and explain meaningful symbols, not merely say "Ours"/"Other" with ambiguous colors. Define unexplained legend terms in the caption or nearby text. Visual QA requires inspecting the exported figure/page.

**R08 — Units.** Use a single unit convention for comparable quantities. Insert proper spacing between numbers and unit symbols (e.g., `12 ms`, `3.5 GB`, `2.0 GHz`; in LaTeX, `12\,\mathrm{ms}`). Follow the target style for percent signs, angles, temperature and other exceptions. Check axis labels, table headings, captions and equations alongside prose.

**R13 — Headings and subfigures.** Select title case or sentence case according to the target style, then use it consistently at the same heading level. For multi-panel figures, put visible (a), (b), (c), etc. tags on the panels and match their exact order in the caption. Use one punctuation scheme for repeated subcaption descriptions (commas/semicolons) as appropriate; keep semantic clarity primary.

## 4. Source and language integrity

**R11 — Reference formatting.** Apply one actual journal/conference bibliography style consistently: author order/name initials, whether all authors or "et al." appear, title capitalization, journal name as abbreviation or full title, year, volume, issue, pages/article number and DOI/URL where required. Verify bibliographic fields against original publications; do not fabricate missing entries.

**R12 — Relevant, credible citations.** Each citation must support the claim it accompanies. General background can cite an appropriate survey; a gap/novelty assertion should be checked against strong, direct primary works and the nearest competing methods. Judge evidence by relevance, quality of the actual study, version and reproducibility, rather than venue label alone. A weak or unrelated citation cannot establish that no prior method exists.

**R14 — Hyphens and artificial phrasing.** Examine gratuitous hyphens, em dashes, templated AI phrases, overlong nominal compounds, formulaic hedging and repeated contrast structures. Replace them with plain grammatical relations where that clarifies meaning. Preserve legitimate compound modifiers, technical nomenclature, numeric ranges and mathematical signs.

**R15 — Tense and discourse flow.** Use present for established facts, equations and the interpretation of figures; past for the conduct of completed experiments; conditional/future for hypotheses and plans. Audit abrupt tense changes that obscure which action has been performed. A paragraph may legitimately alternate tenses when its propositions refer to different times.

## 5. Deliverables and priorities

Review in descending order of consequence:

1. **Scientific integrity:** unsupported claims, imagined application, weak gap, invalid inference, missing decisive comparison or measurement, mismatched mathematical semantics.
2. **Argument clarity:** contribution definition, experiment structure, result explanation, figure-to-text support.
3. **Technical clarity:** first-use symbols and acronyms, notation/units, reproducible method detail, meaningful visual/caption labels.
4. **Submission polish:** references, capitalization, title/subcaption punctuation, spacing, font, line work, hyphenation and tense.

For each material defect, give the exact passage/figure, what it prevents the reader from understanding or verifying, and a concrete revision. When asked to rewrite, provide the revised text itself rather than only a review checklist. For review-only tasks, distinguish **observed defect**, **inference**, and **needs original file/venue verification**.

Use the final publication PDF or figures for visual judgments; text extraction alone cannot certify axis-box style, grid weight, fonts, actual color differentiation or panel placement. Retain negative scientific evidence and valid mathematical exclusions when rewriting to reduce defensive language.
