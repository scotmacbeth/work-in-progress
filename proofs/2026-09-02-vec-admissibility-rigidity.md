# Is full `Vec` `◁`-admissible? — Yoneda rigidity, the finite-row-support lemma, and the precise gap

### The absorptive dichotomy (Conj 6.2) reduces to one functor; two solid new lemmas; the crux isolated

**MacBeth — 2026-09-02 (PROVE session).**
Target (`state/PROVE.md`): the absorptive dichotomy / Conjecture 6.2, which the 09-02 WAKE scoping
collapsed to the single question **"is full (∞-dim) `Vec_k` `◁`-admissible?"**
Predecessors: `proofs/2026-09-01-gap1-setxvec-proved.md` (Prop 6.1: admissibility ⟺ every object
absorptive; the two sources of absorptivity), `proofs/2026-08-30-admissibility-and-the-connectedness-
converse.md` (Lemma S; §9.3 flags exactly this functor as undecided),
`proofs/2026-08-26-t2-day-closedness-famcop.md` (Lemma 3.1: the Set-valued cousin).
Companion code: `scratch/verify-lemmaR.py` (natural-transformation mechanics, green).
Registry: `proofs/registry/left-adjoint-over-vec.json`, node `conj-absorptive-dichotomy`.

---

## EXECUTIVE SUMMARY

**The reduction (recorded, `proved` upstream).** By Prop 6.1, `Fam(Vec^op)` is `◁`-admissible ⟺ every
object of `Vec` is **absorptive**. The structural lemma (09-02 WAKE): every (semi)additive base is
non-extensive, so an admissible additive base is either all-copower-tiny (collapse, reducible) or
carries a genuinely non-tiny absorptive object; and every candidate additive family funnels to full
`Vec`. Hence **Conj 6.2 holds (dichotomy, no irreducible Gap-1 inhabitant) ⟺ full `Vec` is
INADMISSIBLE**; its negation gives an irreducible inhabitant. The whole conjecture is this one bit.

**The one bit, made concrete.** Absorptivity fails for `Vec` iff some object `P` and some
`q = (T,(Q_t))` make `X ↦ Hom(P, ⟦q⟧X)` fail to be a coproduct of representables. The sharpest test
object is `P = E := k^{(ℕ)}` (countable-dim, free, non-copower-tiny) with `q = (ℕ,(Q_t = k))`, so
`⟦q⟧X = ⊕_ℕ X`. The question becomes exactly:

> **(Q)** Is `F(X) := Hom(E, ⊕_ℕ X) = ∏_ℕ(⊕_ℕ X)` naturally isomorphic to a coproduct of
> representables `⊕_{j∈J} Hom(N_j, −)` in the additive functor category `Add(Vec, Vec)`?

**(Q) YES ⟹ irreducible Gap-1 inhabitant (bigger result). (Q) NO ⟹ Conj 6.2 holds.**

**What this session PROVES (two new lemmas, both `proved`).**

- **Lemma R (finite-row-support rigidity).** Writing `A := ⊕_ℕ id`, `F = ∏_ℕ A` (row-finite `ℕ×ℕ`
  matrices), with row-inclusions `in_n : A ⟹ F` and row-projections `pr_n : F ⟹ A`
  (`pr_n in_{n'} = δ_{nn'}id_A`): **every `α ∈ Nat(F, id)` has `α∘in_n = 0` for all but finitely
  many `n`.** The engine is *Yoneda*: `∏_ℕ = Hom(E,−) = h_E` and `Nat(h_E, id) = id(E) = k^{(ℕ)}` is
  **finite-support**. This resurrects Baer–Specker-type rigidity **over a field**, where naive
  module slenderness fails (`Hom_k(k^ℕ, k)` is huge). The proof probes infinitely many rows at once
  with a *single* representable `h_E` via a diagonal-with-repeats placement `Ξ`.

- **Lemma R′.** Consequently **`⊕_n A` is not a natural direct summand of `F`**: the inclusion
  `⊕_n A ↪ F` has no natural retraction. So `F` is a genuine *product* `∏_n A`, not a coproduct, of
  its rows — the natural biproduct system `{in_n, pr_n}` does not assemble into a coproduct.

**What this session does NOT settle (honest).** (Q) itself. Lemma R is **iso-invariant**, hence
inherited by any `G ≅ F`, so it cannot by itself contradict "`F` is an extension"; and R′ obstructs
only the *specific* summand `⊕_n A`, which an extension need not contain. Every single-hom-space
invariant I computed (`Nat(id,F)`, `Nat(F,id)`, `Nat(h_M,F)`, `End F`) is **consistent** with `F`
being an extension, because `F(N_j) = Hom(E, ⊕_ℕ N_j)` genuinely carries infinite-row-support
elements that let hypothetical summands spread across infinitely many rows, evading every
finite-support forcing. **The obstruction, if it exists, is global.** Direction assessment below
leans (A) `Vec` inadmissible, on the *swapped-variance* phenomenon, but this is **not a proof**.

---

## 1. Setting and the reduction to (Q)

`C = Vec_k`, closed symmetric monoidal cocomplete: `⊗_k`, `[V,W] = Hom_k(V,W)`, unit `k`,
coproduct `⊕`. `Fam(Vec^op)`: `q = (T,(Q_t)_{t∈T})`, extension `⟦q⟧X = ⊕_{t∈T} Hom(Q_t, X)`. These
are **additive** functors `Vec → Vec` (each `Hom(Q_t,−)` is `k`-linear; `⊕` of additive is additive).
An **extension** is a functor of the form `⊕_{d} Hom(R_d, −)` — a **coproduct of representables** in
`Add(Vec,Vec)`.

**Prop 6.1 (cited, `proved`).** `Fam(Vec^op)` `◁`-admissible ⟺ every `P ∈ Vec` is absorptive, i.e.
`X ↦ Hom(P, ⟦q⟧X)` is an extension for every `q`.

Single-shape `q = ({t}, Q)` is always fine: `Hom(P, Hom(Q,X)) = Hom(P⊗Q, X)`, one representable. The
obstruction requires a coproduct `⟦q⟧X = ⊕_t Hom(Q_t,X)`, i.e. `Hom(P, ⊕_t(−))` vs `⊕_t Hom(P,−)`;
it bites exactly when `P` is **not copower-tiny**, i.e. `P` infinite-dimensional. The extreme test
case `P = E := k^{(ℕ)}`, `q = (ℕ,(k))` gives **(Q)** with

> `F(X) = Hom(E, ⊕_ℕ X)`,   equivalently (all identifications natural in `X`):
> `F(X) = ∏_ℕ(⊕_ℕ X) = { row-finite ℕ×ℕ matrices over X } = ∏_{n∈ℕ} A(X)`, `A := ⊕_{m∈ℕ}\,\mathrm{id}`.

`Hom(E, Y) = ∏_ℕ Y` because `E = ⊕_ℕ k` and `Hom(⊕_ℕ k, Y) = ∏_ℕ Y`. A map `E → ⊕_ℕ X` is a
sequence `(φ(e_n))_n`, each `φ(e_n) ∈ ⊕_m X` of finite `m`-support (a *row*), unrestricted across
`n` — the row-finite-matrix model.

**Why dimension/accessibility cannot decide (Q)** (recorded, all checked): `F` and every extension
`G = ⊕_j Hom(N_j,−)` are both additive, **exact** (every `N∈Vec` is free ⟹ projective ⟹ `Hom(N,−)`
exact), and **accessible** (`F` is `ℵ_1`-accessible: `∏_ℕ` = `ℵ_1`-small limit commutes with
`ℵ_1`-filtered colimits; `⊕_ℕ` preserves filtered colimits). Dimensions coincide:
`dim F(k^d) = 2^{ℵ_0}` for all finite `d ≥ 1` and `dim F(k^{(κ)}) = κ^{ℵ_0}`, all matchable by a
suitable family `(N_j)`. **Lemma S is vacuous over `Vec`**: `[P, T·1_C] = Hom(P, k^{(T)})` is a
vector space, hence automatically a copower of the unit `k` (every space is free). So the general
necessary condition contributes nothing here; (Q) is the full content.

---

## 2. Lemma R — the finite-row-support rigidity

`A := ⊕_{m∈ℕ} \mathrm{id} = ⊕_m h_k` (`h_k = \mathrm{id}`). `F := ∏_{n∈ℕ} A`. Natural transformations:
- **row-inclusion** `in_n : A ⟹ F`, `(in_n a)` has row `n` equal to `a ∈ A(X)=⊕_m X`, other rows `0`;
- **row-projection** `pr_n : F ⟹ A`, `pr_n((w_{n'})_{n'}) = w_n`. Then `pr_n in_{n'} = δ_{nn'}\,id_A`.

`Nat(A, id) = Nat(⊕_m h_k, id) = ∏_m Nat(h_k, id) = ∏_m id(k) = k^{ℕ}` (unrestricted; maps out of a
coproduct form a product). For `α ∈ Nat(F, id)` write `γ^{(n)} := α∘in_n ∈ Nat(A,id) = k^ℕ`.

**Lemma R.** `S := \{ n : γ^{(n)} ≠ 0 \}` is **finite**, for every `α ∈ Nat(F, id)`.

*Proof.* Suppose `S` infinite. For each `n ∈ S` pick `m(n)` with `γ^{(n)}_{m(n)} ≠ 0` (`m(n)` may
repeat across `n`). Define `Ξ : h_E ⟹ F` on `h_E(X) = Hom(E,X) = ∏_n X` by

> `Ξ_X((x_n)_n) = ` the matrix with entry `x_n` at position `(n, m(n))`, zero elsewhere.

Each row has at most one nonzero entry, so `Ξ_X((x_n)) ∈ F(X)` (row-finite); `Ξ` is natural
(entrywise in `X`). Now `α∘Ξ ∈ Nat(h_E, id)`. **By Yoneda**, `Nat(h_E, id) = id(E) = E = k^{(ℕ)}`,
which is **finite-support**: `(α∘Ξ)_X((x_n)) = ∑_{n∈\,\mathrm{fin}} λ_n x_n` with `λ ∈ k^{(ℕ)}`.
But for finitely-supported `(x_n)`, `Ξ((x_n)) = ∑_n in_n(x_n·δ_{·,m(n)})`, so

> `α(Ξ((x_n))) = ∑_n γ^{(n)}_{m(n)}\, x_n`,  hence  `λ_n = γ^{(n)}_{m(n)}`.

By choice `γ^{(n)}_{m(n)} ≠ 0` for all `n ∈ S`; but `λ` has finite support, so `S` is finite —
contradiction. ∎

**The crux insight.** The rigidity over a field lives in the *functor* category, not the base: the
representable `h_E = ∏_ℕ` has `Nat(h_E, id) = k^{(ℕ)}` finite-support by pure Yoneda, whereas
`Hom_k(k^ℕ, k)` in `Vec` is enormous. The placement `Ξ` (a single natural transformation out of one
representable `h_E`) probes infinitely many rows simultaneously; columns may repeat because only
*rows* are constrained to be finite, and that is exactly the freedom that makes `Ξ` land in `F`.
Lemma R generalises verbatim to any target `T` for which `Nat(h_E, T) = T(E)` has finite support in
the relevant index (e.g. any coproduct of representables), used next.

---

## 3. Lemma R′ — `⊕_n A` is not a natural retract of `F`

**Lemma R′.** There is no natural `ρ : F ⟹ ⊕_n A` with `ρ∘in_{n'} = ι_{n'}` for all `n'`, where
`ι_{n'} : A ↪ ⊕_n A` is the coproduct injection. Equivalently, the inclusion `⊕_n A ↪ F` has no
natural retraction, so **`F ≇ (⊕_n A) ⊕ (\text{anything})`.**

*Proof.* Let `s : ⊕_n A ⟹ id` be the total-sum `s((a_{nm})) = ∑_{n,m} a_{nm}` (a finite sum on any
element of the coproduct; natural). If `ρ` existed, then `s∘ρ ∈ Nat(F, id)` and Lemma R forces
`(s∘ρ)∘in_{n'} = 0` for almost all `n'`. But

> `(s∘ρ)∘in_{n'} = s∘(ρ∘in_{n'}) = s∘ι_{n'} = Σ_A`,

the row-sum `Σ_A : A = ⊕_m id ⟹ id` (the element `(1,1,1,\dots) ∈ k^ℕ = Nat(A,id)`), which is
**nonzero for every `n'`**. Contradiction. ∎

**Reading.** The natural "biproduct system" `{in_n, pr_n}` with `pr_n in_{n'} = δ_{nn'}` looks like it
could split `F` as a coproduct `⊕_n A`, but it does not: `F` is irreducibly the *product* `∏_n A`.
This is the first concrete structural obstruction distinguishing `F` from the coproduct one might
naively hope realises it. (Verified mechanics: `scratch/verify-lemmaR.py` — `pr_n in_{n'}=δ`,
`s∘ι_{n'}=Σ_A` independent of `n'` and nonzero, and `α(Ξ(x))=∑_n γ^{(n)}_{m(n)}x_n`, all green.)

---

## 4. Why (Q) is not thereby settled — the honest boundary

Lemma R is a true property of `F`, but it is **isomorphism-invariant**: any `G ≅ F` satisfies it too.
So R cannot by itself refute "`F` is an extension." Lemma R′ rules out the *particular* summand
`⊕_n A`, but a coproduct of representables need not contain `⊕_n A` as a summand. I verified that
**every single-hom-space invariant is consistent with `F` being an extension**:

- `Nat(\mathrm{id}, F) = F(k) = ∏_n k^{(ℕ)}` (a **product** over `n`; has infinite-row-support
  elements, e.g. `ζ = ` column-`0`-all-ones). For an extension `Nat(\mathrm{id}, G) = ⊕_j N_j^*` (a
  **coproduct**, finite `j`-support). As *plain* vector spaces both have dimension `2^{ℵ_0}` and are
  abstractly isomorphic — the finite-support structure is basis-dependent, so no contradiction.
- Every single `η : h_M ⟹ F` factors through a product-preserving subfunctor (e.g. the "diagonal"
  `η_δ : h_E ⟹ F`, `δ(e_n) = ι_n(e_n)`, has image `≅ h_E` sitting as diagonal matrices). `\mathrm{id}`
  is simple, so `\mathrm{id} ⟹ F` factors through `\mathrm{id}`. No single map obstructs.
- The coproduct property "every `ξ ∈ F(X)` has finite support" is satisfiable elementwise: each `ξ`
  I tested factors through a finite coproduct of representables. The obstruction is **global**.

**Root cause.** `Nat(h_{N_j}, F) = F(N_j) = Hom(E, ⊕_ℕ N_j)` genuinely contains **infinite-row-
support** elements (diagonal-type maps). So hypothetical summands `h_{N_j} ⟹ F` can spread across
infinitely many rows, defeating every attempt to force a fixed `α ∈ Nat(F,id)` to detect infinitely
many rows (the diagonalisation `α := ∑_n s\,pr_n` fails to be well-defined for exactly this reason:
`{n : (s\,pr_n)_j ≠ 0}` can be infinite). This is precisely the wall recorded in §9.3 of the 08-30
file, now understood mechanistically.

**Direction assessment (`speculative`, NOT proved).** I lean **(A) `Vec` is inadmissible** ⟹ Conj
6.2 holds, on the **swapped-variance** phenomenon: for every extension `G`, `Nat(\mathrm{id},G)` is a
coproduct `⊕_j N_j^*` and `Nat(G,\mathrm{id})` a product `∏_j N_j`; for `F` these variances are
**reversed** (`Nat(\mathrm{id},F) = ∏_n k^{(ℕ)}` a product, `Nat(F,\mathrm{id})` a coproduct by Lemma
R). An extension's `Nat(\mathrm{id},−)` "is a coproduct" canonically via its summand projections;
`F`'s is canonically a product. Turning "canonically" into a basis-free contradiction is the missing
step. I did not find it, and I flag that (B) — `F` *is* an extension, giving a genuinely new
irreducible Gap-1 base — remains formally open and would be the larger result.

---

## 5. Precise gap for the collaborator / dream cycle

**(Q)** Is `F = Hom(E, ⊕_ℕ −) = ∏_ℕ(⊕_ℕ −)` a coproduct of representables in `Add(Vec, Vec)`?
Equivalently: is `F` a **projective object** of `Add(Vec, Vec)`? (Coproducts of representables are
projective there — `Nat(h_N,−) = ev_N` is exact; so **(Q) NO ⟸ `F` not projective**, a clean
sufficient route to direction (A).)

Two concrete sub-questions that would break the deadlock:
1. **Specker-clean value of `Nat(F, id)`.** Does the "exotic part" vanish, i.e. is
   `Nat(F, id) = ⊕_n Nat(A, id) = ⊕_n k^ℕ` exactly (no natural functional supported only on
   infinite-row-support elements)? Lemma R gives finite support on the dense sub `⊕_n A`; the
   countable-product Specker argument should close it in ZFC. This pins the coproduct-variance of
   `Nat(F,id)`.
2. **Is `F` projective?** Compute `Ext^1(F, H)` for a well-chosen additive `H`, or exhibit a
   non-split epi `P ↠ F` from a coprod. of representables. This is the field-analogue, in the functor
   category `Add(Vec,Vec)`, of "is a countable product of a projective projective" — false over
   non-perfect rings, and `Add(Vec,Vec)` is the relevant non-semisimple category.

The `ℤ`-analogue (`Add(Ab,Ab)`, where Specker/slenderness is ZFC-decisive) resolves cleanly to (A);
the field case is subtle precisely because base-level slenderness is unavailable and only the
functor-category Yoneda rigidity (Lemma R) survives.

---

## 6. Status ledger

| claim | grade | basis |
|---|---|---|
| Reduction: Conj 6.2 ⟺ full `Vec` inadmissible | **proved (cited)** | 09-02 WAKE scoping + Prop 6.1 |
| (Q) is the concrete form; single-shape fine; dim/accessibility/Lemma-S don't decide | **proved** | §1 |
| **Lemma R** (finite-row-support rigidity, via Yoneda) | **proved** | §2 (+ mechanics `scratch/verify-lemmaR.py`) |
| **Lemma R′** (`⊕_n A` not a natural retract of `F`) | **proved** | §3 |
| every single-hom-space invariant consistent with `F` an extension | **proved (obstruction analysis)** | §4 |
| direction (A) `Vec` inadmissible (swapped variance) | **speculative** | §4 |
| (Q) / Conj 6.2 itself | **OPEN (precisely stated)** | §5 |

**Novelty.** Lemma R (Yoneda rigidity giving finite-support in `Add(Vec,Vec)` over a field, where
module slenderness fails) I have not seen stated; it is the functor-category shadow of Baer–Specker.
The reduction and the swapped-variance framing are the programme's own. Gate against the additive-
functor-category / slender-module literature (Eklof–Mekler; functor categories à la Auslander) before
any external claim — flagged, not cleared.

## 7. Grant framing

The composition calculus `◁` exists on a resource base exactly when the base's objects **absorb**
external shape. Over a linear base this is copower-tininess = finite-dimensionality; the question of
whether *infinite-dimensional* linear resources can still absorb shape is governed by a **rigidity of
natural transformations** (Lemma R): finitely-supported "read-outs" are all you get, resurrected over
any field by Yoneda even though the underlying spaces are enormous. Whether that rigidity is *fatal*
to composition over full `Vec` — the last bit of the dichotomy — is the crux now precisely isolated
for the next cycle.
</content>
