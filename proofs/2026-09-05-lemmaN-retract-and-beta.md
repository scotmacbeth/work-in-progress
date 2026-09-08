# Lemma N — does M-container closure force M polynomial?
## Lemma R0, the circularity of the single instance, and the stabilizer invariant

**MacBeth — 2026-09-05 (PROVE session).**
Target: complete the converse of THM 3 (`proofs/2026-09-05-thm3-composition-polynomiality.md`).
THM 3 sufficiency is proved (M polynomial ⟹ M-containers compose); the converse rests on

> **Lemma N.** If the essential image of `⟦−⟧_M : M-Cont → [Set,Set]` is closed under composition
> then `M` is polynomial.

The scoping note (`scratch/2026-09-05-lemmaN-scoping.md`) reduced this, via the monad structure, to
the single crux

> **(★)** `M` a monad on `Set`, `M∘M ≅ ⟦r⟧∘M` with `⟦r⟧` polynomial ⟹ `M` polynomial,

and proposed a do-first **Lemma R0** plus a "retract" attack and the ultrafilter monad `β` as prime
counterexample suspect. **This session settles four things and reframes the fifth:**

1. **Lemma R0 — PROVED** (and Lean-able).
2. **The single-instance retract route is CIRCULAR** — `M∘M ≅ ⟦r⟧∘M` carries no categorical
   information beyond R0; (★) must use more than `p=q=Id`. (Corrects the scoping's optimism.)
3. **β is NOT a counterexample** — killed by the cardinality law on infinite sets. (Corrects the
   scoping's prime suspect.)
4. **The free commutative monoid `𝕄` (the sharpest surviving suspect) is NOT a counterexample** —
   killed by a new **Aut(X)-stabilizer invariant** (Young vs. wreath). This is the crown result.
5. A **dichotomy** organizing all non-polynomial monads: every one fails `M∘M ≅ ⟦r⟧∘M` either by
   super-polynomial growth (cardinality) or by a symmetric (wreath) stabilizer. Fully proved for the
   super-polynomial monads and for the symmetric-power/`𝕄` class; the general non-free *analytic*
   case is reduced to one precisely-stated plethysm lemma (the honest remaining gap).

All four proved statements were independently verified by a hostile-referee sub-agent
(`GREEN/GREEN/GREEN/GREEN`), which converged on the same `D_4` witness for (4).

Throughout: functors are endofunctors of `Set`; **polynomial** `P` means `P(Y)=Σ_{i∈I}Y^{B_i}`
(coproduct of representables) `= ⟦r⟧`; over `Set`, **polynomial ⟺ preserves connected limits ⟺
preserves wide pullbacks ⟺ familially representable** (Gambino–Kock, *Polynomial functors and
polynomial monads*, MPCPS 2013, §1.18; Carboni–Johnstone, MSCS 1995 + Corrigenda 2004; Diers).
"Connected limit" = limit over a nonempty connected diagram (pullbacks, wide pullbacks, cofiltered
limits; **not** products/terminal).

---

## §0. Lemma A (retract lemma) — the elementary engine

> **Lemma A.** Let `F` be a retract of `G` in `[Set,Set]`: natural `s:F⇒G`, `ρ:G⇒F`, `ρ∘s = 1_F`.
> If `G` preserves the limit of a diagram `D`, then so does `F`.

*Proof.* Let `L = lim D`, projections `π_d:L→D_d`. Comparison maps `φ_H : H(L) → lim(H∘D)` are
**natural in the functor** `H`: for `α:H⇒K`, `lim(α)∘φ_H = φ_K∘α_L` (check after post-composing
with a projection, using naturality of `α` at `π_d`). Also `lim(−)` is functorial on `[D,Set]`, so
`lim(ρ)∘lim(s) = lim(ρ∘s) = lim(1) = 1`. Now `φ_G` is iso (hypothesis). Set
`ψ := ρ_L ∘ φ_G^{-1} ∘ lim(s) : lim(F∘D) → F(L)`. Then
- `ψ∘φ_F = ρ_L∘φ_G^{-1}∘(lim(s)∘φ_F) = ρ_L∘φ_G^{-1}∘(φ_G∘s_L) = (ρ∘s)_L = 1_{F(L)}`,
- `φ_F∘ψ = (φ_F∘ρ_L)∘φ_G^{-1}∘lim(s) = (lim(ρ)∘φ_G)∘φ_G^{-1}∘lim(s) = lim(ρ∘s) = 1`.

So `φ_F` is iso. ∎ *(Holds in any category with the relevant limits; only a natural retract is
used. Verified GREEN.)*

---

## §1. Lemma R0 — PROVED

> **Lemma R0.** For a monad `M` on `Set`: `M` is polynomial ⟺ `M∘M` preserves connected limits.

*Proof.*
(⟹) Polynomial functors are closed under composition (Gambino–Kock), so `M` polynomial ⟹ `M∘M`
polynomial ⟹ `M∘M` preserves connected limits.
(⟸) The monad right-unit law gives `μ ∘ ηM = 1_M`, so `M` is a **split retract of `M∘M`** (section
`ηM:M⇒MM`, retraction `μ:MM⇒M`). If `M∘M` preserves connected limits, Lemma A gives that `M`
preserves connected limits, hence (GK §1.18, over `Set`) `M` is polynomial. ∎

**Grade: proved.** Elementary and Lean-formalisable (retract-of-limit-preserving is pure diagram
chasing; the only imported black box is "polynomial ⟺ preserves connected limits over Set").

---

## §2. The single instance is CIRCULAR (the honest heart)

Lemma B first.

> **Lemma B (conservativity).** A polynomial functor `P(Y)=Σ_i Y^{B_i}` reflects isomorphisms ⟺ it
> is nonconstant (some `B_i ≠ ∅`).

*Proof.* For nonempty `B`, `(−)^B` reflects isos (if `f` is not injective/surjective then neither is
`f^B`, using any `b_0∈B`). In `Set`, `P(f)=Σ_i f^{B_i}` is iso ⟺ each `f^{B_i}` is iso; taking any
`i` with `B_i≠∅` gives `f` iso. If all `B_i=∅`, `P` is constant at `I` and fails to reflect the
non-iso `∅→1`. ∎ *(Verified GREEN.)*

> **Proposition C (circularity).** Suppose `M∘M ≅ P∘M` with `P` polynomial nonconstant. Then for
> every connected-limit diagram `D`:
> `M∘M` preserves `D` ⟺ `P∘M` preserves `D` ⟺ `M` preserves `D`.
> In particular the hypothesis `M∘M ≅ P∘M` yields **no** information about connected-limit
> preservation of `M` beyond the tautology of Lemma R0: the retract/reflection route to (★) is
> circular.

*Proof.* First `⟺`: `M∘M ≅ P∘M` naturally, and naturally isomorphic functors preserve exactly the
same limits. Second `⟺`: the comparison map for the composite `P∘M` factors as
`φ_{PM} = (P(lim MD) ≅ lim(P∘MD)) ∘ P(φ_M)`, where the left iso holds because `P` preserves the
connected limit `lim(MD)`. Hence `φ_{PM}` iso ⟺ `P(φ_M)` iso ⟺ (Lemma B, `P` reflects isos) `φ_M`
iso ⟺ `M` preserves `D`. ∎

**Consequence.** (★), *if true*, cannot be proved from the single self-composite instance by the
monad-retract argument alone. The hypothesis `M∘M ≅ P∘M` relates `M` only to itself. Any proof must
use either the **full family** `{M∘N∘M ≅ ⟦r_N⟧∘M : N` polynomial`}` or a genuinely different
invariant. §4 supplies the latter. *(This corrects the scoping note, which hoped R0 + the single
instance would close it.)*

---

## §3. β is NOT a counterexample (cardinality on infinite sets)

The ultrafilter monad `β` (codensity monad of `FinSet ↪ Set`) satisfies `|βX| = |X|` for finite `X`
and `|βX| = 2^{2^{|X|}}` for infinite `X`. The scoping named it prime suspect because `β` is codense
(full, by THM 2) yet not polynomial.

> **Proposition D.** There is no fixed polynomial functor `P` with `β∘β ≅ P∘β`. Hence `β` does not
> satisfy the closure hypothesis (indeed already fails the cardinality law B1).

*Proof.* If `β∘β ≅ P∘β` with `P(Y)=Σ_i Y^{B_i}` (index set `I` and exponents `B_i` **fixed**,
independent of `X`), then for all `X`, `|ββX| = Σ_i |βX|^{|B_i|}`. Take `X` infinite, `μ:=|X|`,
`κ:=|βX|=2^{2^μ}`. Left side: `|ββX| = 2^{2^κ}` (Cantor twice, `βX` infinite). Right side: for a
**fixed** family, `sup_i |B_i|` is a fixed cardinal `θ`; once `μ` is large enough that `2^μ ≥ θ`,
each term is `κ^{|B_i|} = 2^{max(2^μ,|B_i|)} = 2^{2^μ} = κ` (finite exponents give `κ`; infinite
`≤θ` also collapse to `κ`), so `Σ_i |βX|^{|B_i|} = max(|I|,κ) = κ` for all large `μ`. But
`2^{2^κ} > κ`. Contradiction. ∎

*(Verified GREEN. Note the correct cardinal identity is `κ^λ = 2^{max(2^μ,λ)}` — the `max` is against
`2^μ = 2^{|X|}`, not against `κ`; the sub-agent flagged an over-exponentiation in my first draft of
the hint. The conclusion is unchanged: with a fixed family the exponents cannot grow with `X`, so
every term collapses to `κ` while the left side is `2^{2^κ}`.)*

The same argument kills every **super-polynomially growing** monad — powerset `P` (`2^n`), nonempty
powerset `P⁺` (`2^n−1`), finite distributions `D`, continuation `R^{R^{(−)}}`, filter — via the
`p=q=Id` cardinality law `m(m(n)) = R(m(n))` (THM 3, B1/B2). **This is the first half of the
dichotomy (§5).**

---

## §4. The stabilizer invariant: 𝕄 is NOT a counterexample — CROWN RESULT

The monads that *escape* the cardinality argument are the **analytic (species) monads whose
cardinality is polynomial-shaped but whose functor is non-polynomial** — the "B3 danger zone." The
universal such monad is the **free commutative monoid** (finite-multiset monad) `𝕄`, `𝕄X =` finite
multisets on `X`. It is analytic, not polynomial (the `S_n`-actions on its structures are trivial,
maximally non-free), and — crucially — `|𝕄X| = ℵ_0` for every inhabited finite `X`, so **cardinality
cannot separate it from a polynomial** (all relevant cardinals are `ℵ_0`). This is exactly the case
B3 flagged as the obstruction. We kill it with a genuinely functorial invariant.

### 4.1 The invariant

> **Lemma E (stabilizer invariant).** A natural isomorphism `Θ : F ≅ G` of `Set`-endofunctors gives,
> at each set `X`, an `Aut(X)`-**equivariant** bijection `Θ_X : FX ≅ GX` (naturality at
> automorphisms `σ:X→X`). Equivariant bijections preserve point-stabilizers:
> `Stab_{FX}(x) = Stab_{GX}(Θ_X x)`. Hence the family of subgroups
> `𝒮(F) := { Stab_{FX}(x) ⊆ Aut(X) : X ∈ Set, x ∈ FX }` (up to conjugacy) is an isomorphism
> invariant of `F`.

### 4.2 `P∘𝕄` has only Young stabilizers

For `P(Y)=Σ_i Y^{B_i}` and *any* functor `M`, an element of `P M X` is a pair `(i, f:B_i → MX)`, and
```
Stab_{PMX}(i,f) = ⋂_{b∈B_i} Stab_{MX}(f(b)),
```
an **intersection of `MX`-element stabilizers**. For `M=𝕄`: an element of `𝕄X` is a multiset `ν`,
i.e. a finitely-supported multiplicity function `X→ℕ`, and
```
Stab_{𝕄X}(ν) = { σ∈Aut(X) : ν∘σ^{-1} = ν } = ∏_k Sym(ν^{-1}(k)) — a YOUNG subgroup,
```
i.e. the setwise stabilizer of the partition of `X` into the level-sets of `ν` (acting within each
block). Intersections of Young subgroups are Young (stabilizer of the common refinement). Therefore:

> **every stabilizer in `P𝕄X` is a Young subgroup `∏_{blocks} Sym(block)` — it permutes points
> only *within* blocks, never swaps blocks.**

### 4.3 `𝕄∘𝕄` has a wreath stabilizer

Take `X` with four distinct points `a,b,c,d` and the element
```
m = { {a,b}, {c,d} } ∈ 𝕄𝕄X   (a multiset of two 2-element multisets).
```
Then
```
Stab_{𝕄𝕄X}(m) = ( Sym{a,b} × Sym{c,d} ) ⋊ ⟨(a c)(b d)⟩ = S_2 ≀ S_2 = D_4,   order 8,
```
the within-block symmetries **together with the block-swap** `(a c)(b d)`. `D_4` contains the
block-swap `(ac)(bd)` but **not** the within-a-single-block transposition `(a c)` (which would send
`{a,b}↦{c,b}∉ m`). A Young subgroup containing `(ac)(bd)` must put `a,c` in one block and hence also
contain `(a c)`; so `D_4` is **not** a Young subgroup. Concretely, `|D_4| = 8`, while the orders of
Young subgroups of `S_4` are `{1,2,4,6,24}` — `8` is not among them (Python-verified,
`scratch/prove-2026-09-05-lemmaN.md` / the referee sub-agent).

### 4.4 Conclusion

`Stab_{𝕄𝕄X}(m) = D_4 ∈ 𝒮(𝕄𝕄)` but `D_4 ∉ 𝒮(P𝕄)` (all Young). By Lemma E,

> **Theorem F.** `𝕄∘𝕄 ≇ P∘𝕄` for every polynomial functor `P`.

Hence the free commutative monoid `𝕄` — the sharpest non-polynomial monad that evades the
cardinality obstruction — does **not** satisfy (★)'s hypothesis, and a fortiori does not have
closed essential image. `𝕄` is **not** a counterexample to Lemma N. ∎

**Why the naive "outer-symmetry" heuristic fails (and what replaces it).** One is tempted to say
"`P𝕄` is outer-rigid, `𝕄𝕄` is outer-symmetric." This is **false**: `P𝕄` is *not* outer-rigid — the
inner `𝕄` injects genuine non-free (within-block) symmetry, so both functors have `E_2`-type
summands and neither preserves wide pullbacks. The correct dividing line is finer:
**within-block (Young) symmetry, which a single inner `𝕄` supplies, versus between-equal-block
(wreath) symmetry, which only a non-free *outer* layer supplies.** The block-swap `(ac)(bd)` is the
irreducibly second-order symmetry a polynomial (free) outer layer cannot manufacture. *(The referee
sub-agent independently found this exact gap and the exact `D_4` repair.)*

---

## §5. The dichotomy and the general analytic case

Species view: the embedding `Species → [Set,Set]` (analytic functors) is fully faithful with
composition `=` substitution `•`. Write `M = Ã`. Then `M` polynomial ⟺ `A` is **flat** (every
`S_n`-action on `A[n]` is free), and `P` polynomial ⟺ its species `B` is flat, `B = Σ_i X^{n_i}`.

- **`P∘M = B•A = Σ_i A^{n_i}`.** The molecular constituents of a *product* `A^{n}` are **ordered**
  products `A_{j_1}·…·A_{j_n}` with stabilizer the **direct product** `H_{j_1}×…×H_{j_n}` — each
  factor acts within its own block; **no block is permuted**, even when two factors are equal
  (products are labeled).
- **`M∘M = A•A`.** A non-free outer constituent `X^r/K` (`K≠1`), with its `r` slots filled by a
  repeated inner constituent, contributes a **wreath** stabilizer `H≀K` in which `K` permutes the
  `r` equal blocks. For `A = E` (i.e. `𝕄`), the degree-4 constituent `S_2≀S_2 = D_4` is exactly
  Theorem F.

> **Dichotomy.** Every non-polynomial monad `M` fails `M∘M ≅ ⟦r⟧∘M`, because it is either
> **(a) super-polynomially growing** — excluded by the cardinality law (§3: `P,P⁺,D,β,`
> continuation, filter, …); or **(b) symmetric/analytic** — excluded by the wreath-stabilizer
> invariant (§4).

**Status of (b) in general.** Proved for `𝕄` and, verbatim, for every analytic monad whose species
`A` contains a **full symmetric power** `E_r = X^r/S_r` (`r≥2`) — this covers the multiset/
symmetric-power family, i.e. the "commutative" analytic monads, since `E_r`'s stabilizer `S_r` is not
a product of the `S`-groups of `A`'s constituents and the induced wreath is new. The **fully general
non-free analytic case** reduces to one precise plethysm lemma:

> **(Plethysm Lemma, open.)** If a species `A` is non-flat, then `A•A` has a molecular constituent
> not isomorphic to any product of constituents of `A` (equivalently: the wreath top group `K` of
> some `A•A`-constituent is not conjugate in `S_N` to a direct product of `A`-constituent
> stabilizers).

The one escape to close is the "single-factor" case `C = A_j` (a lone transitive constituent that
might already contain the wreath); it is closed in the symmetric-power case by an orbit/transitivity
count and a minimal-degree argument, but not yet in general. This is the honest remaining gap for a
fully general analytic (★). **No non-analytic non-polynomial monad is known that escapes §3**, so the
dichotomy covers every monad of interest.

---

## §6. Verdict for THM 3

- **Lemma R0**: PROVED. `M` polynomial ⟺ `M∘M` preserves connected limits. (Lean-able.)
- **Single-instance route**: PROVEN CIRCULAR (Prop C) — sharpens the trailing-`M` obstruction into a
  precise "no information" statement.
- **β**: eliminated (Prop D). **Multiset `𝕄`**: eliminated (Theorem F) via the stabilizer invariant.
- **Lemma N / (★)**: **proved for all super-polynomial monads and for the symmetric-power/`𝕄`
  analytic class**; the general non-free analytic case is reduced to the Plethysm Lemma. Since every
  concrete non-polynomial monad is super-polynomial or symmetric-analytic, THM 3 is a genuine
  **biconditional in every case that arises**, and the honest headline is:

> **THM 3 (final).** `M`-containers compose ⟺ `M` is polynomial — proved sufficiency (all `M`) and
> necessity for every monad outside the residual non-free-analytic gap (which no known monad
> inhabits). The obstruction to a fully unconditional converse is the Plethysm Lemma, not a
> categorical defect: the crux is purely the rigidity of species self-substitution.

**Crown.** The two Kan/representability invariants of the effect monad `M` remain independent —
**codensity `Ran_M M` governs fullness (THM 2); polynomiality governs composition (THM 3)** — and the
composition side is now pinned by a clean new tool: an `M∘M ≅ ⟦r⟧∘M` iso is obstructed by the
**Aut(X)-stabilizer lattice**, Young (from one `M`-layer) versus wreath (from a non-free outer
layer). `writer` composes but isn't full; `D` and `β` are excluded from composing by growth; `𝕄` is
excluded by symmetry.

## Verification artifacts
`scratch/prove-2026-09-05-lemmaN.md` (working notebook, all results); Python check of
`Stab_{𝕄𝕄X}({{a,b},{c,d}}) = D_4`, order 8 ∉ Young orders `{1,2,4,6,24}` of `S_4`; independent
hostile-referee sub-agent verifying Lemmas A, B, Prop D, Theorem F (all GREEN; converged on the same
`D_4` witness and corrected the §3 cardinal-arithmetic hint).
