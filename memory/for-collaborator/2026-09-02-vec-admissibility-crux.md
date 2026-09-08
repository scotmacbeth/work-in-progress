# The crux of Conj 6.2 is ONE functor-category projectivity question — and I have the rigidity engine

**MacBeth → collaborator (Neil/Robin), 2026-09-02.**
Full write-up: `proofs/2026-09-02-vec-admissibility-rigidity.md`. Registry:
`left-adjoint-over-vec.json` node `conj-absorptive-dichotomy` (children added).

## Where we are
Conj 6.2 (absorptive dichotomy ⟺ no irreducible Gap-1 inhabitant) has collapsed, cleanly, to:

> **(Q)** Is `F(X) = Hom(E, ⊕_ℕ X) = ∏_ℕ(⊕_ℕ X)` a coproduct of representables `⊕_j Hom(N_j,−)`
> in `Add(Vec,Vec)`? (`E = k^{(ℕ)}`.) Equivalently: **is `F` a projective object of `Add(Vec,Vec)`?**

- **(Q) NO** ⟹ full `Vec` inadmissible ⟹ **Conj 6.2 holds**, no irreducible Gap-1 inhabitant.
- **(Q) YES** ⟹ **irreducible Gap-1 base** — a genuinely new base for Neil's #1 (bigger result).

Dimension, accessibility, exactness, and Lemma S ALL provably fail to decide (Q) (§1). So it is a
real, sharp problem, not a bookkeeping gap.

## What I proved (solid, new)
**Lemma R (Yoneda rigidity).** Every `α ∈ Nat(F, id)` kills the row-inclusions `in_n : A ⟹ F`
(`A = ⊕_ℕ id`) for all but finitely many `n`. The engine is that `∏_ℕ = Hom(E,−)` is representable
and `Nat(h_E, id) = E = k^{(ℕ)}` is **finite-support by Yoneda**. This is the point I most want to
flag: **Baer–Specker/slenderness rigidity is FALSE at the level of `Vec` (`Hom_k(k^ℕ,k)` is huge),
but TRUE in the functor category `Add(Vec,Vec)` for free, via Yoneda.** The proof probes infinitely
many rows with a single representable by a "diagonal-with-repeats" placement `Ξ` (columns may repeat;
only rows must be finite — exactly the slack that makes `Ξ` land in `F`).

**Lemma R′.** `⊕_n A` is not a natural retract of `F`: `F` is irreducibly the *product* `∏_n A`, not
a coproduct, of its rows. (Mechanics machine-checked, `scratch/verify-lemmaR.py`.)

## Why I could NOT finish (honest)
Lemma R is iso-invariant, so it cannot by itself contradict "`F` is an extension"; R′ kills only the
specific summand `⊕_n A`. Every single-hom-space invariant is consistent with `F` being an extension,
because `F(N_j) = Hom(E, ⊕_ℕ N_j)` genuinely has **infinite-row-support** elements — hypothetical
summands can spread across infinitely many rows, defeating every finite-support forcing (the natural
diagonalisation `α = ∑_n s·pr_n` fails to be well-defined for exactly this reason). **The obstruction,
if it exists, is global**, and I believe it lives in the homological algebra of `Add(Vec,Vec)`.

## Two concrete asks that would break the deadlock
1. **Is the "exotic part" of `Nat(F,id)` zero?** i.e. `Nat(F,id) = ⊕_n k^ℕ` exactly (Specker-clean,
   should be ZFC via the countable-product argument). Pins the coproduct-variance.
2. **Is `F` projective in `Add(Vec,Vec)`?** This is the functor-category, field-coefficient analogue
   of "is a countable product of a projective projective" — FALSE over non-perfect rings; the
   `ℤ`-analogue (`Add(Ab,Ab)`, Specker decisive) gives inadmissible cleanly. Do you know the answer
   for `Add(Vec,Vec)`, or a slender/cotorsion-theory reference (Eklof–Mekler; Auslander functor
   categories) that settles it? That single fact closes Conj 6.2.

My bet (unproved): **(A), `Vec` inadmissible**, on the *swapped-variance* asymmetry — every
extension has `Nat(id,G)` a coproduct and `Nat(G,id)` a product; `F` has them reversed.
</content>
