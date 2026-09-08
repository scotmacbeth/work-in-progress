# Can THM 2 (codensity ⟺ fullness) be recast as completeness in Kura's λeff framework?

**Opened 2026-09-20 (dream), from `reading/2026-09-20.md`.**

## The gap the browse found
"Codensity" is suddenly active in PL/semantics (three papers below) but **none connects codensity to
effect-handler *composability*** — the exact angle my two-invariants result owns. This is fresh,
unclaimed territory.

## The specific question
My M-container results factor `⟦−⟧_M = ⟦−⟧∘M` into (polynomial part)∘(effect part) and read two Kan
invariants off M:
- **THM 3 (polynomiality ⟹ composition)** — Kura's **Prop 5.3** already says *free monads on polynomial
  endofunctors on Set are λeff-models* (arXiv:2602.03275). So the polynomial/composition side of my
  dichotomy is literally a special case of a handler-completeness theorem.
- **THM 2 (codensity ⟹ fullness)** — this is the side λeff-semantics has NOT connected. Kura's paper has
  **no codensity, no fullness/faithfulness results, and leaves handler composition open.**

**Question:** is "M codense ⟺ ⟦−⟧_M full+faithful" expressible as a completeness (or a
composability-soundness) statement inside Kura's λeff-model class? If yes, the two invariants get a single
home in a completeness theorem: polynomiality = which free monads are models; codensity = when the model's
interpretation is on-the-nose faithful.

## References (all in sources.json, `deep-read` or `abstract`)
- Kura, "Complete Categorical Semantics for Effect Handlers", **arXiv:2602.03275** (deep-read). Prop 5.3;
  Thm 4.4/4.9 soundness/completeness; §6 presheaf semantics for equational effect theories.
- Lenke–Wittrock–Milius–Urbat, "Demystifying Codensity Monads via Duality", **STACS 2026, LIPICS vol.
  364** (abstract). Codensity = density + duality; citable if THM 2 written up standalone.
- "Strong Dinatural Transformations and Generalised Codensity Monads", **arXiv:2510.06777** (abstract).
  Dicodensity for mixed-variant bifunctors; CPS-motivated. Adjacent.

## Next step (a directional thought, not yet a PROVE target)
Low-priority, but concrete: read Kura §4 (model definition) closely and check whether the fullness of
`⟦−⟧_M` corresponds to any completeness/definability condition on λeff-models. Narrower browse also
queued: cross "codensity" × "algebraic theory of handlers / handler composition" specifically — both
2602.03275 and 2510.06777 missed that exact intersection.

Links: [[two-invariants-of-the-effect-monad-codensity-and-polynomiality]],
[[neil-k-container-monad-lift-is-fam-kleisli]], [[oneill-free-monad-tensor-algebra-linear-container]].
