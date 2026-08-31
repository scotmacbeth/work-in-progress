# The Dialectica tensors ⋉ / ⋊ on **Cont** are not closed — and the obstruction for ⋊ is directed

**Date:** 2026-07-18
**Author:** MacBeth
**Registry:** `other-cont-monoidal-tensors` → new child `ltimes-rtimes-non-closed`
(promotes / refines the `non-convolutional-non-closed` node).
**Depends on:** `2026-07-17-ltimes-rtimes-dialectica.md` (Def. A.1 of ⋉/⋊),
`2026-07-14-day-family-classification.md` (coproducts in Cont, Cont ≃ Poly).

---

## 0. Problem statement

Work in `Cont`, the category of containers, `Cont ≃ Poly` via the fully faithful extension
functor `⟦−⟧`. A container is `p = (S_p, p[-])`: a shape set `S_p` and, at each `s ∈ S_p`, a
direction set `p[s]`; `⟦p⟧X = ∐_{s∈S_p} X^{p[s]}`. Write `y = (1, *↦1)` for the unit
(`⟦y⟧ = Id`) and `y^n = (1, *↦n)` for the "one shape, `n` directions" container.

The two tensors of Dorta–Jarvis–Niu (arXiv:2305.05655 §6, at `C = 1`; Def. A.1 of the
companion note) — which I call the **Dialectica tensors**, an identification that is **mine, not
DJN's** (their §6 gives only the formulas and asks *"We would like to know if there are
interpretations or applications for these monoidal products"*) — have shape set `S_p × S_q` and directions

```
    (p ⋉ q)[(s,t)] = p[s]^{S_q} × q[t]^{S_p}        (symmetric; de Paiva's ⊗_Dial extended)
    (p ⋊ q)[(s,t)] = p[s]^{S_q} × q[t]              (directed: only the LEFT factor exponentiated)
```

with unit `y`. Here `X^S := Set(S, X)` is the function set; the exponent `S` is a **global shape
set of the other argument** — the feature that pushes ⋉/⋊ outside the Day (convolutional) family.

> **Theorem 1 (⋉ is biclosed-free).** `(Cont, ⋉, y)` is neither left- nor right-closed. Concretely,
> for `p = q = y²` the functors `p ⋉ (−)` and `(−) ⋉ q` fail to preserve binary coproducts, hence
> have no right adjoint.
>
> **Theorem 2 (⋊ is not right-closed; the obstruction is one-sided).** `(Cont, ⋊, y)` is **not
> right-closed**: for `p = y²` the functor `p ⋊ (−)` fails to preserve binary coproducts, hence has
> no right adjoint. **However**, for every `q` the functor `(−) ⋊ q` **does** preserve binary
> coproducts. So the coproduct obstruction to closure is *directed*: it appears only in the variable
> whose shape set sits in the exponent. Whether ⋊ is left-closed is not decided by this argument
> (Open Question 5).

Theorem 2 **corrects** the companion note (§A.3(ii), "the same computation kills ⋊"): the blanket
claim is false in the left variable. This one-sidedness is the new content of this session, and it
mirrors, at the level of closure, the directedness of ⋊ itself.

---

## 1. Three standard facts

**Fact 1.1 (coproducts in Cont, shapewise).** `Cont` has all small coproducts, computed on shape
sets: `q₁ + q₂ = (S_{q₁} ⊔ S_{q₂}, d)` with `d(inl s) = q₁[s]`, `d(inr t) = q₂[t]`. (Cont ≃
Fam(Set^op) is the free coproduct completion of Set^op; Lemma 1.2 of the day-family note. The
initial object is `0 = (∅, !)`.) In particular `(q₁+q₂)[·]` at a shape from the `qᵢ` summand is just
`qᵢ[·]`, and `S_{q₁+q₂} = S_{q₁} ⊔ S_{q₂}`.

**Fact 1.2 (isomorphism criterion for containers).** A morphism of containers
`(u, u^♯): (S,d) → (S',d')` is a shape map `u: S → S'` together with, for each `s`, a *backward*
direction map `u^♯_s : d'(u s) → d(s)`. Such a morphism is an isomorphism in `Cont` iff `u` is a
bijection and every `u^♯_s` is a bijection (Abbott–Altenkirch–Ghani, *Categories of Containers*,
FOSSACS 2003). Hence:

> `(S,d) ≅ (S',d')` in `Cont` ⟺ there is a bijection `φ: S ≅ S'` with `d(s) ≅ d'(φ s)` for all `s`.

**Corollary 1.3 (a numerical invariant).** For containers with finite direction sets, the multiset
`⟨ |d(s)| : s ∈ S ⟩` (the *direction-cardinality profile*) is an isomorphism invariant. Two
containers with different profiles are not isomorphic. *Proof.* A container iso is a shape bijection
matching direction sets, so it matches their cardinalities; a bijection of multisets of cardinals.
∎

**Fact 1.4 (a left adjoint preserves colimits).** If `F: 𝒜 → ℬ` has a right adjoint then `F`
preserves all colimits that exist in `𝒜`; in particular, for a binary coproduct `a₁ + a₂` the
canonical comparison `F a₁ + F a₂ → F(a₁ + a₂)` is an isomorphism (Mac Lane, *CWM*, V.5, Thm 1).
**Contrapositive (the tool we use):** if the objects `F a₁ + F a₂` and `F(a₁ + a₂)` are *not even
isomorphic*, then a fortiori the canonical comparison is not an isomorphism, so `F` does not preserve
this coproduct, so `F` has **no right adjoint**.

Note the logical shape: non-isomorphism of the two *objects* is **stronger** than "the comparison
map is not iso," and it is what we will establish — so we never need to analyse the comparison map
itself.

**Definition (closed).** A monoidal category `(𝒞, ⊗, I)` is **right-closed** if for every object `A`
the functor `A ⊗ (−)` has a right adjoint; **left-closed** if every `(−) ⊗ B` has a right adjoint;
**biclosed** if both. (For symmetric `⊗` the two notions coincide.) To refute right-closedness it
suffices to exhibit **one** `A` for which `A ⊗ (−)` has no right adjoint.

---

## 2. The witness and the four computations

Fix the witness containers
```
    p = y²   :   S_p = {∗},  p[∗] = 2 = {0,1};
    q₁ = q₂ = y :  single shape, single direction.
```
By Fact 1.1, `q₁ + q₂` has shape set `{L, R}` (two shapes), each direction a singleton, and
`S_{q₁+q₂} = {L,R}` has two elements. We compute each functor's value on the coproduct versus the
coproduct of values, and read off profiles (Cor. 1.3). All arithmetic is exponential-law arithmetic
`|X^S| = |X|^{|S|}`, `(X × Y)^S ≅ X^S × Y^S`.

**(a) `p ⋉ (−)`, varying the right variable.**
```
  p ⋉ (q₁+q₂):  shapes {∗}×{L,R},  |2 shapes|.
       dir at (∗,X) = p[∗]^{S_{q₁+q₂}} × (q₁+q₂)[X]^{S_p} = 2^{2} × 1^{1} = 4.
       profile = ⟨4, 4⟩.
  (p⋉q₁)+(p⋉q₂):  each p⋉qᵢ has 1 shape, dir = 2^{1} × 1^{1} = 2.
       profile = ⟨2, 2⟩.
```
`⟨4,4⟩ ≠ ⟨2,2⟩` ⟹ **not isomorphic** ⟹ `p ⋉ (−)` does not preserve this coproduct ⟹ (Fact 1.4)
**no right adjoint**. The obstruction is the *growing exponent* `p[∗]^{S_q}`: enlarging `q` to
`q₁+q₂` doubles the exponent (`2^{S_{q₁}+S_{q₂}} = 2^{S_{q₁}}·2^{S_{q₂}}`), turning a coproduct of
shape sets into a **product** of direction sets.

**(b) `(−) ⋉ q`, varying the left variable, `q = y²`.** By symmetry of ⋉ (Lemma A.2 of the
companion note), this is (a) with the roles of the arguments swapped; explicitly with `p₁ = p₂ = y`,
`q = y²`:
```
  (p₁+p₂) ⋉ q :  dir at (X,∗) = (p₁+p₂)[X]^{S_q} × q[∗]^{S_{p₁+p₂}} = 1^{1} × 2^{2} = 4.   profile ⟨4,4⟩.
  (p₁⋉q)+(p₂⋉q):  dir = 1^{1} × 2^{1} = 2.                                                 profile ⟨2,2⟩.
```
`⟨4,4⟩ ≠ ⟨2,2⟩` ⟹ **no right adjoint**. Now the growing exponent is `q[∗]^{S_p}` on the *right*
factor — again enlarged by the coproduct in the varied variable.

**(c) `p ⋊ (−)`, varying the right variable, `p = y²`.**
```
  p ⋊ (q₁+q₂):  dir at (∗,X) = p[∗]^{S_{q₁+q₂}} × (q₁+q₂)[X] = 2^{2} × 1 = 4.   profile ⟨4,4⟩.
  (p⋊q₁)+(p⋊q₂):  dir = 2^{1} × 1 = 2.                                          profile ⟨2,2⟩.
```
`⟨4,4⟩ ≠ ⟨2,2⟩` ⟹ **no right adjoint**. The surviving exponent is `p[∗]^{S_q}`: even though ⋊ does
*not* exponentiate the right factor `q[t]`, the **left** factor still carries the exponent `S_q`,
which the coproduct in `q` enlarges.

**(d) `(−) ⋊ q`, varying the left variable.** Here the growing exponent disappears. Take any
`q` and any `p = p₁ + p₂`:
```
  (p₁+p₂) ⋊ q :  shapes (S_{p₁} ⊔ S_{p₂}) × S_q;
                 dir at (s,t) = (p₁+p₂)[s]^{S_q} × q[t]
                 = pᵢ[s]^{S_q} × q[t]   for s in the pᵢ-summand    (Fact 1.1).
  (p₁⋊q)+(p₂⋊q):  shapes (S_{p₁}×S_q) ⊔ (S_{p₂}×S_q);
                 dir at pᵢ-shape (s,t) = pᵢ[s]^{S_q} × q[t].
```
The canonical distributivity bijection `(S_{p₁} ⊔ S_{p₂}) × S_q ≅ (S_{p₁}×S_q) ⊔ (S_{p₂}×S_q)` of
sets is a shape bijection under which the two direction assignments are **literally identical** —
`pᵢ[s]^{S_q} × q[t]` on both sides, with no exponent depending on the varied variable. By Fact 1.2
this is a container isomorphism, and it *is* the canonical comparison map (it is `(inl ⋊ q, inr ⋊ q)`
on shapes). Hence

> `(−) ⋊ q` **preserves binary coproducts** (and the initial object: `0 ⋊ q = 0`, since `∅ × S_q = ∅`).

The obstruction present in (a),(b),(c) is *absent* in (d): the exponent `S_q` does not involve the
varied container, and the fibre `p[s]` at a shape depends only on its summand, so it distributes over
the coproduct.

**Why `p[s]^{S_q}` distributes but `p[s]^{S_p'}` does not.** In (d) the exponent is the *fixed* set
`S_q`, and `(p₁+p₂)[s]` at a summand shape is just `pᵢ[s]` — a coproduct of shapes only relabels
which fibre you read, it does not fuse fibres. In (a)–(c) the exponent is the *varied* shape set, and
`X^{A ⊔ B} ≅ X^A × X^B` converts that coproduct into a product of direction sets, which is not a
coproduct of containers. This is exactly the "exponent-eats-the-coproduct" phenomenon.

---

## 3. Proofs of the theorems

**Proof of Theorem 1.** By §2(a), `p ⋉ (−)` with `p = y²` does not preserve the coproduct `y + y`,
so by Fact 1.4 it has no right adjoint; since right-closedness would require `A ⋉ (−)` to have a
right adjoint for *every* `A`, `⋉` is not right-closed. By §2(b), `(−) ⋉ q` with `q = y²` likewise
has no right adjoint, so `⋉` is not left-closed. (Either one suffices, since ⋉ is symmetric.) ∎

**Proof of Theorem 2.** By §2(c), `p ⋊ (−)` with `p = y²` does not preserve `y + y`, so by Fact 1.4
it has no right adjoint; hence `⋊` is not right-closed. By §2(d), `(−) ⋊ q` preserves binary
coproducts for every `q`, so the coproduct argument gives no obstruction in the left variable. ∎

**Corollary 3 (taxonomy).** `⋉` and `⋊` are monoidal structures on `Cont` that are neither
convolutional (companion note §A.3(i)) nor closed on the exponentiated side — the **first non-closed
monoidal structures** in the `Cont` story, sharply unlike `×` (cartesian-closed,
Altenkirch–Levy–Staton), `⊗` (closed, Niu–Spivak Ex 4.78), and `◁` (right-coclosed, Niu–Spivak
Prop 6.57). For `⋊` the failure is one-directional, matching the directedness of the tensor.

---

## 4. Reading: the closure obstruction inherits the directedness of ⋊

The companion note's Lemma A.3 shows the `n`-fold ⋊ exponentiates each factor by the shape sets of
the factors **to its right** — a triangular, one-directional dependency. Theorem 2 says the *failure
of closure* has the same handedness: `p ⋊ (−)` (the argument that the exponent `S_q` reaches into)
loses its right adjoint, while `(−) ⋊ q` (the base of the exponent, exponent fixed) keeps coproducts.

The mechanism is uniform across all four computations and can be stated as a slogan:

> **A tensor's left variable `(−) ⊙ q` fails to preserve coproducts exactly when the varied shape
> set `S_p` appears in an exponent of the direction formula.**

For the four `Cont` tensors: `×` (dir `p[s]+q[t]`) and `⊗` (dir `p[s]×q[t]`) have `S_p` in no
exponent — both closed. `◁` and the Dialectica pair put a shape set in an exponent — `◁` on one
side (left-coclosed only), `⋉` on both, `⋊` on exactly one. The presence of `S_{other}` in the
exponent is a single structural dial that reads off closure on each side.

---

## 5. Verification (computational)

`scratch/nonclosed_check.py` builds the actual **direction sets** (as sets of functions, not just
cardinalities) and tests container isomorphism by the Fact-1.2 criterion:

```
=== varying RIGHT variable, p = y², q₁=q₂=y ===
p ⋉(−):  profile ⟨4,4⟩ vs ⟨2,2⟩   preserves coproduct? False
p ⋊(−):  profile ⟨4,4⟩ vs ⟨2,2⟩   preserves coproduct? False
=== varying LEFT variable, q = y², p₁=p₂=y ===
(−)⋉q:  profile ⟨4,4⟩ vs ⟨2,2⟩    preserves coproduct? False
(−)⋊q:  profile ⟨2,2⟩ vs ⟨2,2⟩    preserves coproduct? True
=== deeper (−)⋊q check, nontrivial p₁,p₂,q (direction SETS, not just card) ===
(−)⋊q preserves coproduct? True   L ⟨4,4,8,8,9,18⟩  R ⟨4,4,8,8,9,18⟩
```

The deeper check uses `p₁` (dirs 2,3), `p₂` (dir 2), `q` (dirs 2,1) and confirms the `(−)⋊q`
preservation is a genuine matching of direction sets shape-by-shape (not a cardinality coincidence),
consistent with the canonical-distributivity iso of §2(d). All isomorphism tests use the
direction-cardinality profile (Cor. 1.3), which is sound for finite directions.

---

## 6. Novelty and honesty gate

**Prior art (not mine).** The tensors ⋉/⋊ are DJN §6. "A left adjoint preserves colimits" is
Mac Lane V.5. The container-iso criterion is Abbott–Altenkirch–Ghani (FOSSACS 2003). Coproducts in
Cont are standard (day-family note Lemma 1.2). The *assertion* that ⋉/⋊ are non-closed already
appears in the companion note (§A.3(iii)) at grade "proved" — but there the right-adjoint step is
compressed to one clause and the ⋊ claim is stated as a blanket.

**This session's delta (proved).**
1. The non-closure is given a **complete, self-contained proof**: explicit witness `y²`, the exact
   objects, the profile invariant (Cor. 1.3), and the adjoint-functor consequence spelled out
   (Fact 1.4, contrapositive via non-isomorphism of *objects* — strictly stronger than a
   comparison-map argument). This is exactly the "explicit witness + Lean-ready statement" the PROVE
   brief asked for.
2. **Correction:** the companion note's "the same computation kills ⋊" is **false in the left
   variable**. `(−) ⋊ q` preserves binary coproducts (§2(d)); the obstruction is **one-sided**,
   matching ⋊'s directedness (Theorem 2, §4). This refines the taxonomy: ⋉ fails closure on both
   sides, ⋊ only on the exponentiated side.

**Scoop check (offline).** I grepped `memory/` and `scratch/` for "non-closed"/"not closed"/
"closure": the only source stating ⋉/⋊ non-closed is my own companion note; nothing records the
one-sidedness for ⋊. External novelty of the *phrase* "⋉/⋊ non-closed" is bounded by the registry's
2026-07-17 live sweep, which found Lucatelli Nunes–Vákár (arXiv:2405.07724) and
Capucci–Gavranović–Malik–Rios–Weinberger (MFPS 2024) as neighbours that do **not** treat ⋉/⋊ as
tensors (LNV's Dialectica twist lives in an internal hom `⊸`; CGMRW is at the category level). The
non-closure lemma is elementary given DJN's tensors — its value is rigour + the one-sidedness, not a
deep new theorem. Grade: **proved** (the mathematics is a definitions-and-adjoints argument, fully
checked here and computationally). No novelty overclaim: I claim a *proof and a correction*, not a
new phenomenon.

---

## 7. Feedback into the chapter / note

- `four-monoidal-chapter.tex` §10: the non-closed Remark can now cite this proof; **replace** any
  blanket "⋊ is not closed" with "⋊ is not right-closed; `(−)⋊q` preserves coproducts, so left-
  closure is not refuted by cocontinuity" (Theorem 2).
- `2026-07-17-ltimes-rtimes-dialectica.md` §A.3(ii)–(iii): flag the erratum — the ⋊ left-variable
  computation `[8,8,16,16,16,16]`-style profile was done only for `(−)⋉q`; for `(−)⋊q` the profiles
  match. §A.3(iii)'s "neither ⋉ nor ⋊ is left-closed" should read "⋉ is not left-closed; ⋊ is not
  right-closed (left-closure open)."
- Registry: add child `ltimes-rtimes-non-closed` (proved); annotate the parent's
  `non-convolutional-non-closed` node with the ⋊ one-sidedness correction.

---

## Gaps (precisely stated)

1. **Left-closedness of ⋊ — OPEN (Open Question 5).** `(−) ⋊ q` preserves binary coproducts and the
   initial object (§2(d)), so the *coproduct* obstruction vanishes. This does **not** prove `(−)⋊q`
   has a right adjoint: that needs either (i) preservation of *all* small colimits (coequalizers/
   pushouts untested — colimits in `Cont ≃ Fam(Set^op)` beyond coproducts are not shapewise, so this
   is not automatic) plus a solution-set / accessibility condition, or (ii) an explicit construction
   of the internal hom `[p, −]_⋊`. Conjecture (speculative): ⋊ **is** left-closed, i.e. the closure
   obstruction is *exactly* one-sided — a genuinely directed-closed monoidal category. Settling this
   is the natural next PROVE target (build `[p,−]_⋊` or find a coequalizer `(−)⋊q` breaks).
2. **Lean.** Theorems 1–2 are Lean-ready: the witness is finite, and the only non-elementary input
   is Fact 1.4 (Mathlib: `CategoryTheory.Adjunction.rightAdjoint_preservesColimits` /
   `preservesColimit` on `Adjunction`). A formal statement would encode ⋉/⋊ on the existing
   `Container` type, the `y²`/`y` witnesses, and prove the profiles differ. Not attempted here.
