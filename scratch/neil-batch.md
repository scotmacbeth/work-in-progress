# neil-batch — accumulating for the 2026-08-31 end-of-session email

## Lead with the REFRAME, not the theorem list
Your #1 priority question ("which bases C support the four monoidal structures on Fam(C^op)?")
has the WRONG SHAPE for the composition product `◁`, and I now have the theorem that shows it.

- **Theorem B.** C nontrivial + infinitary lextensive + cartesian closed + `◁`-admissible
  ⟹ the monoidal unit `I` is CONNECTED. So on the extensive pole admissibility ALREADY
  forces connectedness ⟹ `⟦−⟧` full+faithful (T1) ⟹ left adjoint to `(−)◁q` for EVERY q.
  The whole package is ONE BIT, and the pole is rigid: every base there behaves exactly
  like `Set`, or `◁` is not there at all.
- **Theorem D (the punchline).** Off that pole `◁` must be STIPULATED (`◁ := ⊗`), and
  `⟦−⟧` stops being injective on objects — over `Vec_fd`, `({*},k²)` and `({1,2},k)` both
  present `X ↦ X⊕X` and are non-isomorphic. So left-adjointness becomes a property of the
  CHOICE, not of `C`. Theorem 1's hypothesis is simultaneously what makes its converse TRUE
  and what makes its converse MEANINGFUL.
- **Trichotomy** replacing the old dichotomy: extensive pole / collapse pole / inadmissible.
  `Set×Set` and `Set_*` are both inadmissible, for DIFFERENT reasons — and `Set_*` REFUTES
  my own same-day dichotomy: it has a zero object and still has no `◁` (forced `a = −4`).
- **Real generality can only live in Gap 1** (admissible ∧ non-collapse ∧ non-cartesian).
  Named, currently empty. That is the honest answer to your question.

## Two lemmas turned out to be one
T1 (fullness of `⟦−⟧`) and the `◁`-coclosure are **one lemma applied twice** — the same map
`γ`, used at two different probes. I had recorded the load-bearing step of the `Set` proof as
Set-distributivity; it is not, it is unit-connectedness. That was my error and I found it by
running a falsifier I had named in advance.

## The Weber re-filing is DEAD, and I killed it deliberately
My "one functional, many probes" method is NOT Weber-style p.r.a. failure. Diagnosis:
**wrong adjoint side.** p.r.a. is about a LEFT adjoint (which `(−)◁q` has unconditionally
over `Set` — and this is known, Niu–Spivak Prop 6.57, I do NOT claim it); all three of my
probe instances test a RIGHT adjoint. The method survives as mine at `speculative`, three
instances, with extensivity as the fusion mechanism on the right side only.

## Machine-checked
`CompLeftAdjoint.lean` — the container library's first adjunction, sorry-free, `[Quot.sound]`
only. Both triangle identities, the hom-set bijection, plus unit/counit naturality and `L_q`
functoriality. Negative controls did real work: a perturbed counit passes the SHAPE leg and
fails the POSITION leg, and the SAME perturbation satisfies naturality exactly — so naturality
and the triangles are independent probes. The adjunction is a statement about positions.

## Questions for Neil
1. Gap 1 — is the middle region (admissible, non-collapse, non-cartesian-closed) empty?
   My lead: `I ≅ I₁ ⊔ I₂` in closed monoidal C gives `X ≅ (X⊗I₁) ⊔ (X⊗I₂)`, an
   idempotent-splitting shape; if `I_i ⊗ I_j ≅ 0` for `i ≠ j` then Theorem B runs verbatim
   WITHOUT cartesianness. Not attempted. Do you have an instinct for whether it is empty?
2. Given the reframe, is `◁`-generality still worth the effort, or should the Fam(C^op)
   effort go entirely to `⊗` (where the question IS graded and real)?

## Operational (mention briefly)
- Robin's new PROTOCOL landed; my three GitHub repos now exist and I made the first push.
- NOTE: under the protocol my only agent neighbour is Rick. I can no longer write to Clio.
