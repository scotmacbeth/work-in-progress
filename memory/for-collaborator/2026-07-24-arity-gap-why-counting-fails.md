# Arity gap: why counting cannot close it (for Neil / dream cycle)

**Session:** 2026-07-24 PROVE (bounded attempt on `gap-infinite-arities`, per Neil's
"close Ch1–3, no moonshots" steer). **Outcome: honest Further Work, sharply characterized.**
Full note: `proofs/2026-07-24-arity-gap-further-work.md`.

## TL;DR
I did not close the gap (excluding infinite/unbounded arities from the closed-convolutional-tensor
classification). I now think it is a **genuine open problem** — real chance the conjecture is
FALSE — and I *proved why the past several sessions kept bouncing off it*: cardinality methods are
provably blind to it.

## Three new proved facts
1. **Affine = connected-colimit preservation** (Lemma A). "All arities ≤1" ⟺ `R_B` preserves
   connected colimits.
2. **Closure gives connected LIMITS only** (Prop B). The 2026-07-15 biconditional, read through
   `Cont ≅ Fam(Set^op)`, yields exactly connected-*limit* preservation of `R_B` and nothing about
   colimits. So affineness (a colimit condition) is genuinely independent of the closure
   hypothesis — no categorical shortcut. The bounded case worked *only* because of the cardinal
   count `κ² > κ`, which dies for infinite `κ`.
3. **The arity recursion is a fixed point at infinite arity** (Prop C, the real contribution).
   Associativity forces `A_{C⋆B,(b,φ)} = Σ_{i∈A_{B,b}} A_{C,φ(i)}`. Seed `R_2 = y + y^λ`
   (λ infinite) → `R_{2⋆2} = y + 2^λ·y^λ`, and the associator `(X⋆2)⋆2 ≅ X⋆(2⋆2)` is a genuine
   natural-in-X iso (both sides `= X + μ·y^λ`, μ=2^λ). No contradiction from cardinalities,
   arities, or one-variable naturality. Finite seed n≥2 instead grows n→n²→… (re-deriving the Key
   Lemma). Verified: `scratch/arity-gap/recursion_selfconsistency.py`.

## The precise remaining question (a clean Further Work target, NOT a moonshot to chase now)
Does the seed `R_2 = y + y^λ` extend to a symmetric monoidal `⋆` — i.e. an associator natural
*jointly in all variables* satisfying **pentagon** (+ hexagon)? Everything cardinal is consistent;
the only untested condition is element-level coherence. Either it extends (⟹ classification is
**bounded-arity only**, a new phenomenon: an infinite-arity closed convolutional tensor) or the
pentagon obstructs it (⟹ gap closed, theorem unconditional).

## For Ch3 (WRITE this cycle)
The classification ships as **unconditional on the uniformly-bounded-arity locus** (contains every
`×` and `∨_S` — conclusion families complete). §6 now carries the sharpened Further Work (limits vs
colimits + the pentagon target), replacing the old vague "killed by associator naturality" (which
was misleading: in the classification direction the associator is *given* and natural).

## Suggested next moves (if we ever return to it)
- A focused element-level pentagon computation for `R_2 = y + y^λ` (hard: infinite coherence; maybe
  a clever finite skeleton captures it).
- Or hunt the literature: "polynomial functors + symmetric monoidal + infinite arity" — is a
  commutative monoid in `(Poly, ∘)` with infinite arity known? (I have a strong-monoidal
  `R: (Set,⋆) → (Poly,∘)` framing that might connect to known operad/polynomial-monad results.)
