# For collaborator — ◁-comonoids over Vec = families of k-algebras (Part 3 PROVED)

**MacBeth, 2026-08-19 PROVE session.** Full proof: `proofs/2026-08-19-vec-comonoids-algebras.md`.
Verification: `scratch/vec-comonoids/verify.py`. Registry: `registry/linear-containers-vec.json`
node `part3-comonoid-algebras` (proved, validator OK).

## What got upgraded
Part 3 of the linear-containers program (Prop 4.2 of the 08-18 file) was **computed** — a sketch.
It is now **proved**, and the hypotheses came out **cleaner than PROVE.md guessed**.

## The theorem
In `(Fam(Vec_fd^op), ◁, I)` with `(S,P)◁(T,Q)=(S×T,(P_s⊗Q_t))`, `I=({∗},k)`:

> A ◁-comonoid on `(S,P)` = a family `(A_s)_{s∈S}` of unital associative k-algebras, one on
> each position space `P_s`, with no cross-shape composition. Functorially,
> **`Comon_◁(Fam(Vec_fd^op)) ≅ Fam(Alg_k^op)`** (cocommutative ↔ `Fam(CAlg_k^op)`).

This is the exact ◁/Vec analogue of my Set result `bare-dirichlet-comonoid`
(⊗-comonoid in Poly = family of monoids), one enrichment level up:
monoid ⤳ k-algebra, because positions are contravariant.

## The two things worth your eye

**1. Variance does the work.** A morphism in `Fam(Vec^op)` is forward on shapes, *backward*
(Vec-linear) on positions. So the comultiplication's position component is
`δ♯_s : P_s⊗P_s → P_s` — a **multiplication** `μ_s` — and the counit's is
`ε♯_s : k → P_s` — a **unit** `η_s`. A *co*monoid over Vec is an *algebra*, not a coalgebra.
Same fibrewise-op that runs my monad→comonad transfer.

**2. The algebroid guess is genuinely refuted in finite dim — and I can point at the exact
step.** The crown hope was "◁-comonoid over Vec = k-linear category (algebroid, Mitchell)."
FALSE for f.d. positions. The counit forces `δ_shape = diagonal` (S is the unique `(Set,×)`-
comonoid), so δ only ever lands in the diagonal block `P_s⊗P_s` — never an off-diagonal
`P_a⊗P_b`, `a≠b`. No hom between distinct objects ⟹ a disjoint family of *one-object*
k-linear categories = k-algebras. The mechanism is Prop 4.1: over Vec the composition's shape
set collapses to the **plain product** `S×S`, whereas the Set composition (`DCont≅Cat`) is the
**dependent sum** `Σ_s S^{P_s}` whose dependency is exactly what encodes composable arrows.
Linearity flattens the dependent sum (Lemma 1.3), and that is why the multi-object structure
dies. **Same biproduct/linearity collapse as Parts 1 and 2, now on comonoids — its third
face.** A real algebroid needs a different, dependency-carrying (lax/bimodule) ◁; that's the
stated sequel and the honest open target.

## Hypotheses, sharpened
Finite-dimensional positions only. **S arbitrary** — finite S is *not* needed (Prop 4.1's
composition formula needs only f.d. positions; the diagonal-forcing is pure Set-comonoid
uniqueness, cardinality-free). Char k unrestricted.

## Conviction
`verify.py` over F_2 brute-forces all comonoid data by direct `Fam(Vec^op)`-morphism
composition (no mention of "algebra") and compares to an independent enumeration of algebra
families. 4/4 cases: `#comonoids = ∏_s A(n_s)` (A(1)=1, A(2)=12 structures on F_2^n),
`δ_shape` forced diagonal in every survivor, zero off-diagonal survivors, no cocommutativity
forced.

## Grant framing
Theory pillar: this completes the ◁/Vec (co)monoid classification and gives a clean,
publishable "why the naive linear generalisation of `DCont≅Cat` fails, and precisely which
extensivity/biproduct step kills it." The `Comon_◁ ≅ Fam(Alg_k^op)` statement is a tidy
categorical headline; the algebroid-refutation-with-remedy is the honest research story and
sets up "lax/bimodule ◁ over Vec" as the next front.
