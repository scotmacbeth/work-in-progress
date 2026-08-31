# DCont morphisms are COFUNCTORS, not functors — the dictionary completed

**For:** Neil, Robin (and the grant narrative)
**Result file:** `projects/proofs/2026-06-09-dcont-morphisms.tex` (compiles, 5pp)
**Verification:** `projects/scratch/dcont_morphisms_check.py` (36 ordered pairs, exhaustive)
**Status:** Main theorem airtight + computationally verified. One contrast claim
deliberately stated at the level I can prove (see "Honest scope" below).

## TL;DR — a broken assumption in our own roadmap
The SEED/SUMMARY "next step" read: *upgrade Theorem 4.1 to an equivalence
DCont ≃ Cat (directed-container morphisms ↔ **functors**)*. **That is false.**
The container morphism `(f, f♯)` has its position component
`f♯_s : P'(fs) → P(s)` **contravariant** on positions, while a functor is
**covariant** on morphisms. Opposite variance ⟹ container morphisms cannot be
functors.

**The correct theorem:**
> With the directed-structure compatibility conditions made explicit,
> `(f, f♯)` is exactly a **cofunctor** (retrofunctor) of the associated
> categories, and
> **DCont ≅ Cof  (isomorphism of categories)**,
> where Cof = small categories + cofunctors.

This is the Ahman–Uustalu fact, but now in our own terms, with the exact
morphism conditions written down and an independent combinatorial check.

## The exact morphism conditions (the deliverable PROVE.md asked for)
A morphism of directed containers `D → D'` is `(f, f♯)`, `f: S→S'`,
`f♯_s : P'(fs)→P(s)`, satisfying for `h ∈ P'(fs)`, `k ∈ P'(fs ↓' h)`:
- **(M0)** `f(s ↓ f♯_s(h)) = (fs) ↓' h`            (↓-compat = cofunctor codomain-lift C0)
- **(M1)** `f♯_s(o'(fs)) = o(s)`                     (root = cofunctor unit C1)
- **(M2)** `f♯_s(h ⊕' k) = f♯_s(h) ⊕ f♯_{s↓f♯_s(h)}(k)`  (shift hom = cofunctor comp C2)

Under the dictionary these are **literally** the cofunctor laws (C0,C1,C2).
Bijection on hom-sets (Φ full & faithful) + bijection on objects (Thm 4.1)
⟹ **isomorphism of categories** DCont ≅ Cof. Composition matches:
`(g∘f)♯ = f♯ ∘ g♯_{fs}` = cofunctor composite. All checked.

## The foil (makes the variance story complete)
The **opposite** variance — a *covariant* position map `φ_s : P(s) → P'(fs)`
with (N0,N1,N2) — recovers **functors exactly**. Verified: #such = #functors
in all 36 cases. So:
- contravariant positions (the genuine container morphism) = **cofunctors**;
- covariant positions (NOT a container morphism)          = **functors**.

## Computational evidence (decisive)
Over `{1, 2, 3-chain, ℤ/2, ℤ/3, idempotent-2-monoid}`, all 36 ordered pairs:
- `#DCont-morphisms == #cofunctors`  in **all 36** ✓
- `#covariant-morphisms == #functors` in **all 36** ✓
- `#functors != #cofunctors` in **20 of 36** — and not monotone:
  `1→2`: 2 fun / 1 cof;  `2→2`: 3 fun / 2 cof;  but `3→2`: 4 fun / **5** cof.
  Neither hom-set contains the other.

## Why this matters for the grant
The equivalence chain (containers ≃ directed containers ≃ poly comonoids ≃
small categories) is an equivalence **of objects**. At the morphism level it is
**DCont ≅ Cof**, *not* DCont ≅ Cat. In Poly this is the statement that
**comonoid morphisms in (Poly, ◁) are cofunctors**; functors are a *different*
structure (bicomodules / parametric right adjoints). Anywhere our applied notes
say "functor between directed containers" (agent meta-agents, supply-chain maps,
internal replacement), the correct map is a **cofunctor** — and as the counts
show, the choice even changes the *number* of maps. This is exactly the
compositional-correctness pitfall the grant promises to eliminate by
formalisation. **Action item:** audit the applied `.tex`/markdown for
"functor"→"cofunctor".

## Honest scope (what I did NOT over-claim)
- **Airtight:** DCont ≅ Cof; the (M0–M2)↔(C0–C2) bijection; functoriality;
  functors = covariant gadgets; the hom-count obstruction below.
- **Stated precisely, proven:** the object dictionary does **not** extend to a
  *full* functor DCont→Cat (a 1-element hom would map onto a 2-element hom),
  so "DCont ≃ Cat extending the dictionary" is false.
- **Flagged, NOT proven:** that Cof and Cat are inequivalent as *abstract*
  categories (relabeling-invariant separation). I sketched the route
  (adjoint profile of Hom(1,−): `ob` on Cat vs "sink-objects" on Cof) but did
  not complete it — it is not needed for the dictionary question. Open if anyone
  wants it.

## Next
- **Lean M4**: formalise Cof and DCont ≅ Cof (the (M0–M2) conditions are
  directly codable; builds on `lean/Containers/`).
- Decide whether to settle Cof ≄ Cat abstractly (low priority).
