# Paper drafted: "DCont morphisms are cofunctors, not functors" (DCont ≅ Cof)

**For:** Neil, Robin (and the grant — Theory + Applications strands)
**Status:** Complete draft, 7pp, compiles clean. Pushed + PR open for review.

## Links
- **PR:** https://github.com/scotmacbeth/ghani-containers/pull/1
- **Source:** https://github.com/scotmacbeth/ghani-containers/blob/paper-dcont-cof/papers/dcont-cof.tex
- **PDF:** https://github.com/scotmacbeth/ghani-containers/blob/paper-dcont-cof/papers/dcont-cof.pdf

## What it is
A short arXiv/ACT-extended-abstract note writing up the proved + 36-pair-verified result:
a morphism of directed containers is a **cofunctor**, not a functor, because its position
map `f♯_s : P'(fs) → P(s)` is contravariant. Conditions (M0)–(M2) are *literally* the
cofunctor laws (C0)–(C2); the assignment is an **isomorphism of categories DCont ≅ Cof**.
Framed as a CORRECTION to the roadmap slogan "morphisms ↔ functors" + a bridge: the
contravariant variance is exactly the **Put of a delta lens** (Clarke), which is what makes
the bidirectional/update applications (supply chains, agent orchestration) land. Functors
are the opposite (covariant) variance; the dictionary does NOT extend to Cat.

## Two things I corrected while writing (please back-port to the proof note)
The proof note `proofs/2026-06-09-dcont-morphisms.tex` and the earlier for-collaborator
memo both need two fixes; the paper already has them right:

1. **Count: 17, not 20.** "#functors ≠ #cofunctors" holds in **17** of the 36 ordered
   pairs, not 20. This is the actual output of `scratch/dcont_morphisms_check.py`
   (`grep -c differs` = 17; hand-checked from the count columns). The headline 36/36
   equalities (#DCont = #cofunctors, #covariant = #functors) are unaffected and both hold.
   → The .tex (§ "Computational verification") and the 2026-06-09 memo say 20; fix to 17.

2. **Put cofunctor direction.** The Put of a delta lens `(f,φ): A⇌B` is a cofunctor
   `A ⇸ B` (lifts land in the source A), carried by Φ⁻¹ to a DCont-morphism `D_A → D_B`.
   (An earlier draft slogan had `B⇸A`/`D_B→D_A`; that's the Clarke-2020 internal arrow
   convention, opposite to ours and to Clarke-2022 Def. 3. The paper uses our convention
   consistently: a cofunctor `C⇸D` has object map ob C→ob D and lifts in C.)

## Out of scope (stated as outlook only)
- Lean formalisation of Cof + Theorem 3.5 (the M4 lean branch is the place — `lean-m4-cofunctor`).
- A speculative "δ-diversity" invariant of a directed-container morphism (how much it
  rewrites as it propagates an update). Mentioned in the conclusion only; NOT claimed.

## Grant hook
This is the morphism-level half of the equivalence-chain story: objects equivalence is
old (Ahman–Uustalu), but the morphism level is DCont ≅ Cof, and getting the variance right
is precisely a compositional-correctness payoff — the lens/Put reading is the application
bridge to supply chains and agent orchestration. See [[cofunctors-are-update-lenses]] and
[[dcont-morphisms-are-cofunctors]].
