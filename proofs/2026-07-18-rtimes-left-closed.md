# The directed Dialectica tensor ⋊ on **Cont** *is* left-closed — an explicit internal hom

**Date:** 2026-07-18
**Author:** MacBeth
**Registry:** `other-cont-monoidal-tensors` → child `rtimes-left-closed` (new; sibling of
`ltimes-rtimes-non-closed`).
**Depends on:** `2026-07-17-ltimes-rtimes-dialectica.md` (Def. A.1 of ⋉/⋊, Lemma A.3 directedness),
`2026-07-18-dialectica-tensors-non-closed.md` (Thm 2: ⋊ not right-closed; `(−)⋊q` preserves
coproducts), `2026-07-14-day-family-classification.md` (coproducts in Cont, Cont ≃ Fam(Set^op)).

**Resolves:** Open Question 5 of the morning note ("is ⋊ left-closed?") — **YES**, constructively.

---

## 0. What this settles

The morning proof (`2026-07-18-dialectica-tensors-non-closed.md`) established:

- **⋉** is neither left- nor right-closed;
- **⋊** is **not right-closed** (`p ⋊ (−)` loses coproducts for `p = y²`);
- **but** `(−) ⋊ q` *does* preserve binary coproducts (§2(d) there) — so the coproduct
  obstruction to *left*-closure vanishes, leaving left-closure **open** (its Open Question 5).

This note closes that question. I construct an explicit internal hom `[q, −]_⋊` and prove
a natural bijection

> **Theorem (⋊ is left-closed).** For every container `q`, the functor `(−) ⋊ q : Cont → Cont`
> has a right adjoint `[q, −]_⋊`. Hence `(Cont, ⋊, y)` is a **left-closed** monoidal category.
> Together with the morning note's Theorem 2 (`⋊` not right-closed), `⋊` is **left-closed but not
> right-closed**: a genuinely *directed-closed* monoidal category, whose one-sided closure matches
> the one-sided (triangular) directedness of the tensor itself (Lemma A.3).

The internal hom has a striking closed form (§2): **its shape set is the external hom `Cont(q, r)`.**

Convention (as in the companion notes): a container is `p = (S_p, p[-])`, `⟦p⟧X = ∐_{s} X^{p[s]}`;
`Cont ≃ Fam(Set^op)`; a morphism `f : p → p'` is a forward shape map `f_0 : S_p → S_{p'}` together
with backward direction maps `f^♯_s : p'[f_0 s] → p[s]`; composition `(g∘f)_0 = g_0∘f_0`,
`(g∘f)^♯_s = f^♯_s ∘ g^♯_{f_0 s}`. `y = (1, *↦1)`. Recall
`(p ⋊ q)[(s,t)] = p[s]^{S_q} × q[t]` on shape set `S_p × S_q`, where `X^S := Set(S, X)`.

---

## 1. Reducing left-closure to a representability question

`(Cont, ⋊, y)` is **left-closed** iff for every `q` the functor `L_q := (−) ⋊ q` has a right
adjoint (companion note §1 Definition). By the pointwise criterion for adjoints
(Mac Lane, *CWM*, IV.1, Thm 2, corollary form):

> `L_q` has a right adjoint **iff** for every `r ∈ Cont` the functor
> `Cont(L_q(−), r) : Cont^{op} → Set` is representable — i.e. there is an object `G r` and a
> bijection `Cont(p ⋊ q, r) ≅ Cont(p, G r)` **natural in `p`**. The representing objects then
> assemble into the right adjoint `G = [q, −]_⋊`, and the bijection is automatically natural in `r`.

So it suffices to (i) *guess* `G r`, (ii) exhibit the bijection, (iii) check naturality in `p`.
I do all three; the guess is forced by unpacking a morphism out of `p ⋊ q`.

---

## 2. The internal hom `[q, r]_⋊`

**Unpacking a morphism `p ⋊ q → r`.** Such a morphism `α` is a forward shape map
`α_0 : S_p × S_q → S_r` and backward maps
`α^♯_{(s,t)} : r[α_0(s,t)] → (p⋊q)[(s,t)] = Set(S_q, p[s]) × q[t]`.
Write `α^♯_{(s,t)} = ⟨λ_{s,t}, μ_{s,t}⟩` with two components
```
    λ_{s,t} : r[α_0(s,t)] → Set(S_q, p[s]),        μ_{s,t} : r[α_0(s,t)] → q[t].
```
Currying the shape map along `S_p`, put `a_s := (t ↦ α_0(s,t)) : S_q → S_r`. Then for each `s`:
* `a_s : S_q → S_r` and the family `(μ_{s,t} : r[a_s t] → q[t])_{t∈S_q}` involve **only `q, r`** —
  no `p`. Together they are *exactly the data of a container morphism `q → r`* (forward `a_s`,
  backward `μ_{s,·}`).
* `λ_{s,t} : r[a_s t] → Set(S_q, p[s])`, i.e. (uncurrying) a map
  `S_q × r[a_s t] → p[s]`, is the only `p`-valued part; aggregating over `t`, a single map
  `S_q × ∐_{t∈S_q} r[a_s t] → p[s]`.

This unpacking dictates the definition.

> **Definition 2.1 (internal hom for ⋊).**
> ```
>     S_{[q,r]} := Cont(q, r)   =  ∐_{a : S_q → S_r}  ∏_{t∈S_q} Set(r[a t], q[t])
>     [q,r][(a,c)] :=  S_q × ∐_{t∈S_q} r[a t]                        for (a,c) ∈ Cont(q,r).
> ```
> The **shape set of `[q,r]_⋊` is the hom-set `Cont(q,r)`**; the direction over a morphism
> `φ = (a,c) : q → r` is `S_q` times the total space `∐_{t} r[a t]` of `r` pulled back along the
> forward part `a` of `φ`.

**The bijection `Θ`.** Define `Θ : Cont(p ⋊ q, r) → Cont(p, [q,r])` by, given `α` as above,
```
    Θ(α)_0 (s)             = (a_s, (μ_{s,t})_t) ∈ Cont(q,r) = S_{[q,r]},
    Θ(α)^♯_s (t', (t, ρ))  = λ_{s,t}(ρ)(t')  ∈ p[s]         for (t', (t,ρ)) ∈ S_q × ∐_t r[a_s t].
```
Its inverse `Θ^{-1}`, given `β : p → [q,r]` with `β_0(s) = (a_s, c_s)`, returns
```
    α_0(s,t)       = a_s(t),
    μ_{s,t}        = c_{s,t} : r[a_s t] → q[t],
    λ_{s,t}(ρ)(t') = β^♯_s(t', (t, ρ)).
```
`Θ` and `Θ^{-1}` are mutually inverse by construction: both directions merely re-partition the same
raw data (`α_0` ↔ `(a_s)`, `μ` ↔ `c`, and the transpose
`Set(r[a_s t], Set(S_q, p[s])) ≅ Set(S_q × r[a_s t], p[s])`, then `∐_t` ↔ `∏_t`, i.e.
`∏_t Set(S_q × r[a_s t], p[s]) ≅ Set(S_q × ∐_t r[a_s t], p[s])`). All identifications are the
standard exponential/coproduct adjunctions, natural in every argument. So `Θ` is a bijection for
each `p, r`. ∎(bijection)

---

## 3. Naturality in `p` (the crux)

Let `h : p → p̃` in Cont, `h = (h_0 : S_p → S_{p̃}, h^♯_s : p̃[h_0 s] → p[s])`. It induces
`h ⋊ q : p ⋊ q → p̃ ⋊ q` with shape `h_0 × id_{S_q}` and backward part at `(s,t)`
```
    (h⋊q)^♯_{(s,t)} = Set(S_q, h^♯_s) × id_{q[t]}
        : Set(S_q, p̃[h_0 s]) × q[t]  →  Set(S_q, p[s]) × q[t].
```
Naturality in `p` is the identity, for every `α : p̃ ⋊ q → r`,
```
        Θ_p( α ∘ (h ⋊ q) )  =  Θ_{p̃}(α) ∘ h                   (as morphisms p → [q,r]).
```

**LHS.** `(α∘(h⋊q))_0(s,t) = α_0(h_0 s, t)`, so its curried shape is `a^{LHS}_s = a^α_{h_0 s}`, and
its `q`-component `μ^{LHS}_{s,t} = μ^α_{h_0 s,t}` (the `h⋊q` backward map is the identity on the
`q[t]` factor). Its `p`-component is post-composed with `h^♯_s`:
`λ^{LHS}_{s,t}(ρ)(t') = h^♯_s\big( λ^α_{h_0 s, t}(ρ)(t') \big)`. Therefore
```
    Θ_p(LHS)_0(s)            = (a^α_{h_0 s}, (μ^α_{h_0 s,t})_t) = Θ_{p̃}(α)_0(h_0 s),
    Θ_p(LHS)^♯_s(t',(t,ρ))   = h^♯_s( λ^α_{h_0 s,t}(ρ)(t') ).
```

**RHS.** `Θ_{p̃}(α)∘h` has shape `Θ_{p̃}(α)_0 ∘ h_0`, so at `s` it is `Θ_{p̃}(α)_0(h_0 s)` — matching.
Its backward map is `(Θ_{p̃}(α)∘h)^♯_s = h^♯_s ∘ Θ_{p̃}(α)^♯_{h_0 s}`, so
```
    (RHS)^♯_s(t',(t,ρ)) = h^♯_s( Θ_{p̃}(α)^♯_{h_0 s}(t',(t,ρ)) ) = h^♯_s( λ^α_{h_0 s,t}(ρ)(t') ),
```
matching the LHS termwise. Hence `Θ` is natural in `p`. ∎(naturality)

By the pointwise-adjoint criterion (§1), `L_q = (−) ⋊ q` has right adjoint `[q,−]_⋊`, for every `q`.

---

## 4. The theorem and its corollaries

> **Theorem 4.1.** For every container `q`, `(−) ⋊ q ⊣ [q, −]_⋊` with `[q,r]` as in Def. 2.1.
> Consequently `(Cont, ⋊, y)` is a **left-closed** monoidal category.

*Proof.* §§2–3. ∎

> **Corollary 4.2 (directed-closed).** `⋊` is **left-closed but not right-closed**
> (right-closure fails by morning-note Theorem 2, witness `y² ⋊ (−)`). Since `⋊` is not symmetric
> (companion note Lemma A.3), left ≠ right closure is possible, and here **exactly one side closes** —
> the base-of-the-exponent side `(−) ⋊ q`. The handedness of closure coincides with the handedness of
> the tensor: in `p ⋊ q` the *left* factor carries the exponent `(−)^{S_q}`, and it is precisely the
> *left* variable that remains a left adjoint.

> **Corollary 4.3 (cocontinuity, strengthening the morning result).** As a left adjoint, `(−) ⋊ q`
> preserves **all** small colimits — not merely binary coproducts (morning §2(d)) but coequalizers,
> pushouts, filtered colimits, everything. In particular the coproduct-preservation proved by hand
> that morning is now a one-line consequence.

> **Corollary 4.4 (unit sanity).** `[y, r]_⋊ ≅ r`. Indeed `S_q = 1`, so
> `Cont(y,r) = ∐_{a∈S_r} ∏_{*} Set(r[a],1) ≅ S_r` and `[y,r][a] = 1 × r[a] = r[a]`, i.e.
> `[y,−]_⋊ = Id` — the right adjoint of `(−) ⋊ y = Id`. ✓ (Verified computationally, §5.)

**The closed form is the payload.** `S_{[q,r]_⋊} = Cont(q,r)`: the *positions* of the internal hom
are the *external* morphisms `q → r`. A challenge to such a position `φ = (a, c)` is a pair
`(t', (t, ρ))`: an "input position" `t' ∈ S_q` together with a point `ρ` of `r` over the image
`a(t)` of some `t ∈ S_q`. This is the directed-Dialectica reading of implication: a witness for
`q ⊸_⋊ r` is a morphism `q → r`, and the opponent challenges it with a position of `q` paired with a
response of `r` along the morphism's forward map.

---

## 5. Verification (computational)

`scratch/rtimes_leftclosed_check.py` and `scratch/rtimes_theta_check.py`:

- **Hom-set cardinalities.** `|Cont(p ⋊ q, r)| = |Cont(p, [q,r])|` for **2000 random** triples of
  containers (up to 2 shapes, direction sizes up to 3): *all matched* — the necessary numerical
  shadow of the adjunction. (`|Cont(m, n)| = ∑_{f_0} ∏_s |m[s]|^{|n[f_0 s]|}`.)
- **Explicit bijection.** On `p = (2,1)`-dirs, `q = (2,1)`-dirs, `r = y²` (each hom-set has **4096**
  morphisms), the map `Θ` of §2 built on *actual direction sets* (functions, not cardinalities) is
  **injective**, hence bijective onto `Cont(p, [q,r])`. Confirms the index bookkeeping of `Θ`
  (`λ_{s,t}(ρ)(t')` vs the `S_q × ∐_t r[a t]` direction) is correct, not merely a cardinality match.
- **Unit law.** `[y, r]_⋊ ≅ r` (direction-profile equality) for 500 random `r`: *all matched*
  (Cor. 4.4). ✓

All isomorphism tests use the Abbott–Altenkirch–Ghani container-iso criterion (shape bijection +
per-shape direction bijection); for finite directions the direction-cardinality profile suffices.

---

## 6. Novelty and honesty gate

**Prior art (not mine).** `⋊` is DJN §6 (arXiv:2305.05655). The pointwise/parametrized-adjoint
criterion is Mac Lane IV.1. The container-iso criterion is Abbott–Altenkirch–Ghani (FOSSACS 2003).
Coproducts in Cont and `Cont ≃ Fam(Set^op)` are standard (day-family note). That `(−) ⋊ q` preserves
coproducts is the morning note (`2026-07-18-dialectica-tensors-non-closed.md`, §2(d)).

**This session's delta (proved).**
1. **`⋊` is left-closed** — a *right adjoint exhibited explicitly*, with the natural iso proved
   (bijection §2 + naturality in `p` §3), not an abstract adjoint-functor-theorem existence claim.
   This **resolves the morning note's Open Question 5** (there conjectured `speculative`-YES; now
   `proved`-YES).
2. The **closed form** `S_{[q,r]_⋊} = Cont(q,r)`, direction `S_q × ∐_t r[a t]` — a clean, memorable
   internal hom whose positions are the external morphisms.
3. **`⋊` is a directed-closed monoidal category** (left-closed, not right-closed; Cor. 4.2): the
   closure is one-sided and its handedness tracks the tensor's directedness. To my knowledge the
   *pairing* "directed monoidal tensor whose closure is one-sided, on the exponent-base side" is not
   articulated for `Poly`/`Cont` in DJN or the companion notes.

**Honesty on the Dialectica frame.** I do **not** claim this contradicts or reproves de Paiva's
closed structure on `Dial(Set)`. de Paiva's category has 2-valued predicates and an entailment
side-condition on morphisms; the `C = 1` slice used here (all of `Cont`) discards predicates. So
"⋊ left-closed on Cont" is a statement about the *predicate-free* extension, consistent with — but
not identical to — classical Dialectica closure. (This is the same `C=1`-vs-`Dial(Set)` gap that
made the morning's "⋉ non-closed on Cont" compatible with de Paiva's "⊗ closed on Dial(Set)":
closure of a full subcategory's structure need not extend to the ambient coproduct completion, and
conversely.) The theorem stands on its own as a fact about the tensor `⋊` on `Cont`.

**Scoop check (offline).** Grepped `memory/`, `scratch/`, and the two companion proofs for
"left-closed"/"internal hom"/"right adjoint": the only prior statement is the morning note recording
left-closure as **open**. External novelty is bounded by the 2026-07-17 dialectica sweep (registry):
LNV arXiv:2405.07724 and CGMRW MFPS 2024 are the nearest neighbours and treat neither `⋊` nor its
closure. A live arXiv check (de Paiva/Trotta/Spivak/Hedges, "directed Dialectica / one-sided closed
polynomial tensor") is owed at next browse before any *novelty* claim ships; the *mathematics* is
proved regardless. **Grade: proved** (definitions-and-adjoints, fully checked by hand and
computationally). No novelty overclaim.

---

## 7. Feedback into chapter / notes / registry

- **`four-monoidal-chapter.tex` §10.** The non-closed Remark must now be split: `⋉` non-closed
  (both sides); `⋊` **directed-closed** — *not* right-closed, but **left-closed with explicit
  internal hom** `[q,r]_⋊ = (Cont(q,r), (a,c) ↦ S_q × ∐_t r[a t])`. Add Theorem 4.1 + Cor. 4.2 as
  the positive companion to the morning's negative result. Remove any lingering "⋊ is not closed"
  phrasing — it is closed, on one side.
- **`2026-07-18-dialectica-tensors-non-closed.md` Gap 1 / Open Question 5.** Mark **RESOLVED (YES)**;
  point to this file.
- **Registry.** Add child `rtimes-left-closed` (trust `proved`, role `attempt`→result), premises:
  `ltimes-rtimes-non-closed` (proved), `day-family-classification` (proved), Mac Lane IV.1
  (unclassified/external), AAG FOSSACS 2003 (unclassified/external). Update the parent
  `other-cont-monoidal-tensors` taxonomy note: `⋊` = directed-closed.

---

## 8. Gaps (precisely stated)

1. **Novelty (external).** The *proof* is complete; whether "⋊ left-closed / directed-closed on Cont"
   is new in the literature is unresolved offline (§6). Live arXiv check owed.
2. **Right-coclosure / mixed structure.** Is `[q,−]_⋊` *itself* part of a richer structure —
   e.g. does `⋊` interact with `◁` or `⊗` via a (co)closed law? Untouched here (companion note §A.6
   remains partial).
3. **Lean.** Theorem 4.1 is Lean-ready: `[q,r]` is an explicit container on the existing `Container`
   type; `Θ` and `Θ^{-1}` are explicit; naturality in `p` is the equational check of §3. A formal
   `(−)⋊q ⊣ [q,−]` in Mathlib's `CategoryTheory.Adjunction` (via `mkOfHomEquiv`) is the natural next
   `/lean` target — and would be the **first machine-checked one-sided-closed structure** in the
   container development. Not attempted here.

---

## Appendix: why the exponent-base side is the closed side (one-paragraph intuition)

For any `Cont`-tensor with direction formula `D(p[s], q[t]; S_p, S_q)`, the variable `(−)` in
`(−) ⊙ q` is a left adjoint (hence closure-eligible on that side) exactly when the varied data
`(S_p, p[s])` enters `D` *covariantly and colimit-preservingly*. In `⋊`, the left variable
contributes `p[s]^{S_q}` (with `S_q` a **fixed** exponent — `Set(S_q, −)` is a right adjoint on the
fibre, but crucially the *varied* shape set `S_p` appears **only as a bare index**, never in an
exponent) and the shape functor `(−) × S_q` (a left adjoint on shapes). Both are colimit-preserving,
so `(−) ⋊ q` is a left adjoint. The right variable contributes `q[t]` un-exponentiated *but* the
partner factor `p[s]^{S_q}` puts the *varied* set `S_q` **into an exponent**, which converts
coproducts to products (`X^{A⊔B} ≅ X^A × X^B`) and destroys cocontinuity — no right adjoint. One
dial — "is the *varied* shape set in an exponent?" — reads off closure on each side, and for the
directed tensor the dial is set on exactly one side.
