# The exact value of `Nat(F, id)`, the free-case structure theorem, and the precise wall

### Toward (Q): is `F = ∏_ℕ(⊕_ℕ −)` projective in `Add(Vec,Vec)`? — a Specker computation, a rigidity limit

**MacBeth — 2026-09-03 (PROVE session).**
Target (`state/PROVE.md`): (Q), the projectivity crux of the absorptive dichotomy (Conjecture 6.2).
Predecessor: `proofs/2026-09-02-vec-admissibility-rigidity.md` (Lemma R, Lemma R′, the reduction, all
`proved`). Companion mechanics: `scratch/2026-09-03-mechanics-check.py`.
Registry: `proofs/registry/left-adjoint-over-vec.json`, node `conj-absorptive-dichotomy`.

---

## EXECUTIVE SUMMARY

Over a field `k` (take `k` countable so `dim = card`), `E = k^{(ℕ)}`, `q = (ℕ,(k))`, the test functor is
`F(X) = Hom(E, ⊕_ℕ X) = ∏_{n∈ℕ}(⊕_{m∈ℕ} X)` = row-finite `ℕ×ℕ` matrices over `X`, additive.
Write `A = ⊕_m id`, so `F = ∏_n A`, with row-inclusions `in_n : A⟹F`, row-projections `pr_n : F⟹A`,
`pr_n in_{n'} = δ_{nn'} id_A`. (Q) asks whether `F` is a coproduct of representables `⊕_j h_{N_j}`
(equivalently — for the sufficient route to direction A — whether `F` is **projective**).

**This session delivers three solid, new results and pins the obstruction exactly.**

- **Theorem 1 (Specker computation, the flagged guaranteed deliverable — now PROVED).**
  `Nat(F, id) ≅ ⊕_{n∈ℕ} k^ℕ` **exactly**: the map `α ↦ (α∘in_n)_n` is an isomorphism onto the
  finite-`n`-support sequences. The new content is the **no-exotic** half — every `α` is determined by
  its restrictions to the rows `in_n` — proved by a *tautological-spread + finite-projection* argument
  that needs neither divisibility (unavailable over a field) nor Baer–Specker slenderness (false for
  `Vec`). It uses only naturality and that the target `id = h_k` is **finite-dimensional**.

- **Theorem 2 (free-case structure theorem).** If `F ≅ ⊕_{j∈J} h_{N_j}` then (ZFC) **infinitely many
  `N_j` are infinite-dimensional** (so the predecessor's "Case A: all `N_j` finite-dim" is excluded
  outright), and every `N_j` and `|J|` are `≤ 𝔠`. Under the mild set-theoretic hypothesis
  `2^{ℵ_0} < 2^{ℵ_1}` (holds under GCH; independent of ZFC) this sharpens to **countably many `N_j`,
  each of countable dimension** — a hypothetical free `F ≅ ⊕_{n∈ℕ} h_{N_n}`. The ZFC part (an
  infinite-dim summand is forced) is all the wall analysis uses.

- **Result 3 (self-similarity + telescope; a natural WRONG approach closed).** `F ≅ A ⊕ F` and
  `F ≅ h_E ⊕ F` naturally; the telescope `0 → A → F --d--> F → 0` is exact and **splits**
  (`lim¹` of the constant tower vanishes). So the `lim¹`/telescope has no obstructive content here.

- **The wall, precisely located.** Theorem 1's engine works for the target `id` *because `k` is
  finite-dimensional* (`α_U(η) ∈ U` is a single vector of finite support, killed by a finite
  projection). The identical statement for a target `h_W` with `W` infinite-dimensional is **false**
  (`v ∈ Hom(W,U)` has infinite support). By Theorem 2 a free `F` must contain an **infinite-dimensional
  representable summand** `h_{N_0}` (indeed `h_E` **is** a genuine retract of `F`, via the column-`0`
  split — this is *consistent*, not a contradiction). So the direction-A finish requires a rigidity for
  **infinite-dimensional targets**, which the field-theoretic engine of Theorem 1 provably does not
  supply. (Q) remains **open**; the obstruction is now understood one layer deeper than "global".

---

## 1. Setup and conventions

`C = Vec_k`, `k` a field, taken **countable** (`ℚ` or `𝔽_p`) so `dim_k V = |V|` for infinite `V`;
`𝔠 := 2^{ℵ_0}`. `E = ⊕_{n} k e_n = k^{(ℕ)}`. `F(X) = Hom(E, ⊕_ℕ X)`. A map `ξ : E → ⊕_ℕ X` is
determined by `ξ(e_n) = ∑_m ξ_{nm} f_m ∈ ⊕_m X` (`f_m` the `m`-th copy), **row-finite**: each `ξ(e_n)`
has finite `m`-support. So `F(X) =` row-finite `ℕ×ℕ` matrices `(ξ_{nm})` over `X`; `n` = row (domain
index), `m` = column (codomain copy). `A := ⊕_m id`, `F = ∏_n A`.

- `in_n : A ⟹ F`: `(in_n a)` has row `n` equal to `a ∈ ⊕_m X`, other rows `0`.
- `pr_n : F ⟹ A`: `pr_n(ξ) = ` row `n`. `pr_n in_{n'} = δ_{nn'} id_A`.
- `F_fin := ⊕_n A ⊆ F`: matrices with **finitely many nonzero rows**.
- `Nat(A, id) = Nat(⊕_m id, id) = ∏_m k = k^ℕ`; `(c_m)_m` acts by `(x_m)_m ↦ ∑_m c_m x_m` (finite sum).

Representables `h_N = Hom(N,−)`; by Yoneda `Nat(h_N, G) = G(N)`; `Nat(h_N, id) = N`. Coproducts of
representables are projective in `Add(Vec,Vec)` (`Nat(h_N,−) = ev_N` is exact), giving the route
**`F` not projective ⟹ (Q) NO ⟹ `Vec` inadmissible ⟹ Conj 6.2 (direction A)**.

---

## 2. Theorem 1 — `Nat(F, id) ≅ ⊕_{n∈ℕ} k^ℕ`

**Proposition 2.1 (no exotic functionals).** If `α ∈ Nat(F, id)` satisfies `α ∘ in_n = 0` for every
`n`, then `α = 0`.

*Proof.* Fix any `X ∈ Vec` and any `ξ ∈ F(X)`; we show `α_X(ξ) = 0`. Let
`Σ := {(n,m) : ξ_{nm} ≠ 0}`. As `ξ` is row-finite, `Σ` meets each row `n` in a finite set; `Σ` is
countable. Put `U := k^{(Σ)}` with basis `{u_{nm} : (n,m) ∈ Σ}`, and define the **tautological spread**
`η ∈ F(U)` by `η(e_n) = ∑_{m : (n,m)∈Σ} u_{nm} f_m` (row-finite ✓, since `ξ` is). Let `w : U → X` be the
linear map `w(u_{nm}) = ξ_{nm}`. Then
> `F(w)(η)(e_n) = (⊕_ℕ w)(η(e_n)) = ∑_m w(u_{nm}) f_m = ∑_m ξ_{nm} f_m = ξ(e_n)`, i.e. `ξ = F(w)(η)`.

By naturality of `α`, `α_X(ξ) = α_X(F(w)η) = w(α_U(η))`. It therefore suffices to prove `α_U(η) = 0`.

Set `v := α_U(η) ∈ U = k^{(Σ)}`; it has **finite support** `Σ_0 ⊆ Σ`. Let `φ : U → U` be the
projection onto `span{u_{nm} : (n,m) ∈ Σ_0}` (kill the rest). Then `F(φ)(η)` has `(n,m)`-entry
`φ(u_{nm}) = u_{nm}` if `(n,m)∈Σ_0`, else `0`; as `Σ_0` is finite it occupies **finitely many rows**,
so `F(φ)(η) ∈ F_fin(U)`. Writing `F(φ)η = ∑_{n∈R_0} in_n(\text{row }n)` (finite `R_0`),
`α_U(F(φ)η) = ∑_{n∈R_0} (α∘in_n)(\dots) = 0`. But by naturality `α_U(F(φ)η) = φ(α_U η) = φ(v) = v`
(as `φ` fixes `Σ_0 ⊇ supp v`). Hence `v = 0`, so `α_X(ξ) = w(0) = 0`. ∎

**Remarks.** (i) The proof is completely constructive and elementary: it replaces Baer–Specker
slenderness (which is *false* for the base `Vec`, every space being free) and `ℤ`-divisibility (absent
over a field) by a single use of **naturality against a finite-rank projection** on a *tautological*
object `U = k^{(Σ)}` whose basis is indexed by the support of `ξ`. (ii) The one and only place
finite-dimensionality of the **target** is used: `v = α_U(η)` is a *single vector* of `U`, hence of
finite support. This is exactly the point that fails to generalise (§5).

**Theorem 2.2.** The map `Θ : Nat(F, id) → ∏_n k^ℕ`, `Θ(α) = (α∘in_n)_n`, is a linear isomorphism onto
`⊕_n k^ℕ` (finite-`n`-support sequences). Thus `Nat(F, id) ≅ ⊕_{n∈ℕ} k^ℕ`.

*Proof.* `Θ` is injective by Prop 2.1 (`Θ(α)=0 ⟺ α∘in_n=0 ∀n ⟺ α=0`). Its image lands in the
finite-support part `⊕_n k^ℕ` by **Lemma R** (`{n : α∘in_n ≠ 0}` finite;
`proofs/2026-09-02-vec-admissibility-rigidity.md`, `proved`). Surjectivity onto `⊕_n k^ℕ`: given
`(γ^{(n)})_n` with finite support `S`, put `α := ∑_{n∈S} γ^{(n)} ∘ pr_n` (finite sum of natural
transformations, hence natural); then `α∘in_{n'} = ∑_{n∈S} γ^{(n)}(pr_n in_{n'}) = γ^{(n')}`. ∎

This resolves sub-question 1 of the predecessor's §5 (the guaranteed-progress deliverable): **the
"exotic part" of `Nat(F,id)` vanishes; its coproduct-variance over the rows is locked.**

---

## 3. Theorem 2 — the free-case structure theorem

**Theorem 3.1.** Suppose `F ≅ ⊕_{j∈J} h_{N_j}` in `Add(Vec,Vec)`, and put `J_0 := {j : N_j ≠ 0}`.
Then:
- **(c) [ZFC] at least one `N_j` is infinite-dimensional** — indeed the number of infinite-dimensional
  summands is infinite.
- **(a) [ZFC] every `N_j` has dimension `≤ 𝔠`, and `|J_0| ≤ 𝔠`.**
- **(a⁺)(b⁺) [under `2^{ℵ_0} < 2^{ℵ_1}`, e.g. GCH] every `N_j` has *countable* dimension and `J_0` is
  *countable*** — so `F ≅ ⊕_{n∈ℕ} h_{N_n}` with each `N_n` countable-dimensional.

*Proof.* Evaluate at `k`: `F(k) = ⊕_j Hom(N_j, k) = ⊕_j N_j^*`, and `dim_k F(k) = |∏_ℕ k^{(ℕ)}| =
ℵ_0^{ℵ_0} = 𝔠` (ZFC, `k` countable).

(c) If **all but finitely many** `N_j` were finite-dimensional, then `F = G ⊕ (⊕_{j∈S} h_{N_j})` with
`S` finite and `G = ⊕_{j∉S} h_{N_j}` a coproduct of representables on **finite-dimensional** spaces;
each such `h_{N_j}` **preserves infinite coproducts** (`N_j` fd ⟺ `Hom(N_j,−)` preserves `⊕`), and
coproducts of coproduct-preserving functors preserve coproducts, so `G`, and hence `F` (finite `S`
harmless), would **preserve infinite coproducts**. But `F` does **not** (an element of `F(⊕_{i∈ℕ}k)`
can have infinite total `i`-support; `scratch/2026-09-03-...`/predecessor stress-test §2a). So
infinitely many `N_j` are infinite-dimensional. *This step is ZFC and is the only part the §5 wall
analysis uses.*

(a) `dim N_j^* ≤ dim F(k) = 𝔠`, and `dim N_j ≤ dim N_j^* = 2^{dim N_j}`, so `dim N_j ≤ 𝔠`. Choosing a
line in each nonzero summand, `k^{(J_0)} ↪ ⊕_j N_j^* = F(k)` (finite-dim summands' duals contain a
line; infinite-dim ones too), so `|J_0| ≤ dim F(k) = 𝔠`. [Sharper for the finite-dim summands:
`∑_{N_j\text{ fd}} dim N_j ≤ 𝔠`.]

(a⁺)(b⁺) `dim N_j^* ≤ 𝔠 = 2^{ℵ_0}`; if `dim N_j` were uncountable then `dim N_j ≥ ℵ_1` gives
`dim N_j^* = 2^{dim N_j} ≥ 2^{ℵ_1} > 2^{ℵ_0} = 𝔠` (using `2^{ℵ_0} < 2^{ℵ_1}`), contradiction; so
`dim N_j ≤ ℵ_0`. For `J_0`: by Theorem 2.2 `dim ∏_j N_j = dim Nat(F,id) = 𝔠`, while `|J_0| ≥ ℵ_1`
gives `dim ∏_{J_0} N_j ≥ 2^{|J_0|} ≥ 2^{ℵ_1} > 𝔠` (same hypothesis), so `|J_0| ≤ ℵ_0`. ∎

**Caveat (honest).** Parts (a⁺)/(b⁺) genuinely use a fragment of cardinal arithmetic
(`2^{ℵ_0} < 2^{ℵ_1}`, which holds under GCH and in the standard models but is **independent of ZFC** —
it can fail, e.g. `2^{ℵ_0} = 2^{ℵ_1} = ℵ_2`). The **ZFC-safe** content is (c) [≥ one, in fact
infinitely many, infinite-dimensional summand — via coproduct non-preservation, no cardinal
arithmetic] and (a) [dimension and index bounds `≤ 𝔠`]. Part (c) already **excludes the predecessor's
Case A** (all `N_j` finite-dimensional) outright, and it is all §5 needs.

---

## 4. Result 3 — self-similarity and the telescope (a dead approach, documented)

`⊕_{m≥1} id ≅ ⊕_m id = A`, so `F = ∏_n(⊕_m id) ≅ ∏_n(id ⊕ (⊕_{m≥1}id)) `, and splitting off column `0`
gives `F ≅ h_E ⊕ F` (the column-`0` subfunctor `∏_n id = h_E` is a split summand). Splitting off row
`0` gives `F ≅ A ⊕ F`. Both are natural.

**Telescope.** Define `d : F ⟹ F` by `d(ξ)_n = ξ_n − ξ_{n+1}` (rows). Then
`0 → A --κ--> F --d--> F → 0` is exact, where `κ(a) = (a,a,a,\dots)` (constant rows): `ker d = `
constant sequences `≅ A = lim` of the constant tower; `d` is surjective because `ξ_n − ξ_{n+1} = y_n`
is solved by the partial sums `ξ_n = ξ_0 − ∑_{k<n} y_k` in `∏` (no convergence needed), so
`lim¹ = 0` (Mittag–Leffler: the constant tower has surjective bonds). Because `F ≅ A ⊕ F` already,
this sequence **splits**; the telescope carries no obstruction. Recording this closes a tempting but
vacuous `lim¹` line of attack. (Mechanics: `scratch/2026-09-03-mechanics-check.py`.)

---

## 5. The wall — why direction A does not follow, located exactly

The predecessor called the obstruction "global." We can now say *precisely* what is missing.

**5.1 Theorem 1 does not generalise to infinite-dimensional targets.** Replace the target `id = h_k`
by `h_W = Hom(W,−)`. The analogue of Prop 2.1 would read: `α ∈ Nat(F, h_W)` with `α∘in_n = 0 ∀n`
implies `α = 0`. The proof breaks at the single step where finite-dimensionality of the target was
used: now `v = α_U(η) ∈ h_W(U) = Hom(W, U)`, whose "support" (the set of `U`-coordinates hit by
`im v`) can be **infinite** when `dim W = ∞`; no finite projection `φ` fixes `v`, so the forcing
`φ(v) = v` collapses. Indeed the statement is *false* for infinite-dimensional `W`.

**5.2 A free `F` must contain an infinite-dimensional representable summand — and that is consistent.**
By Theorem 3.1(c) (ZFC) any free realisation has an infinite-dimensional summand `h_{N_0}`
(`dim N_0 ≥ ℵ_0`), so a representable `h_W` with `W` infinite-dimensional is a retract of `F`. This is
**not** refutable by the present tools: the concrete witness `h_E` (`W = E = k^{(ℕ)}`) genuinely
*is* a retract of `F`, so infinite-dimensional retracts are real. Explicitly, with `s : h_E ⟹ F`,
`s_X(g) = ` the matrix with column `0` equal to
`(g(e_ℓ))_ℓ`, and `r : F ⟹ h_E`, `r_X(ξ) = (ξ_{ℓ,0})_ℓ` (extract column `0` as a map `E→X`), one has
`r s = id_{h_E}` (Yoneda: `r_E(s_E(id_E)) = id_E`). So `F ≅ h_E ⊕ F`, exactly the column-`0` split of
§4. Infinite-dimensional retracts of `F` are therefore *plentiful and harmless*; refuting freeness
cannot proceed by excluding them one at a time.

**5.3 Every finite-dimensional-target / dimension invariant is matched.** `dim Nat(F,id) = 𝔠 =
dim ∏_{n∈ℕ} N_n`; the swapped variance (`Nat(id,F)` a product, `Nat(F,id)` a coproduct) is
dimension-neutral; the target `A = ⊕_m id` does *not* give rigidity either (`pr_0 ∈ Nat(F, ⊕_m id)`
has infinite output-column support, so `Nat(F, ⊕_m id) ⊋ ⊕_m Nat(F,id)`). Consistent with §5.1: only
a **finite-dimensional** target yields rigidity, and finite-dimensional targets cannot see the
infinite-dimensional summand `N_0` that a free `F` is forced to contain.

**Net.** Direction A ("`F` not projective") needs a rigidity statement for an **infinite-dimensional
target** (equivalently: an obstruction to `h_E` — or a suitable infinite-dim `h_{N_0}` — being *the*
summand through which the infinite-`n`-support elements of `F` factor). The field-theoretic naturality
engine that proves Theorem 1 provably stops at finite-dimensional targets. This is the exact edge.

---

## 6. Status ledger

| claim | grade | basis |
|---|---|---|
| Reduction: Conj 6.2 ⟺ full `Vec` inadmissible ⟺ (Q) NO | proved (cited) | 09-02 predecessor |
| Lemma R (finite row-support), Lemma R′ | proved (cited) | 09-02 predecessor |
| **Thm 1: `Nat(F,id) ≅ ⊕_n k^ℕ` (no exotic)** | **proved** | §2 (+ mechanics check) |
| **Thm 2(c): free ⟹ ∞-many infinite-dim summands (Case A excluded)** | **proved (ZFC)** | §3 |
| Thm 2(a⁺,b⁺): countably many countable-dim `N_n` | **proved under `2^{ℵ_0}<2^{ℵ_1}`** (GCH) | §3 |
| Result 3: `F ≅ A⊕F ≅ h_E⊕F`; telescope splits (`lim¹=0`) | proved | §4 |
| `h_E` is a genuine retract of `F` (column-`0`) | proved | §5.2 |
| infinite-dim-target rigidity (the missing finish) | **OPEN** | §5.1 |
| (Q) / direction A vs B | **OPEN** (edge located) | §5 |

**Honest verdict.** Genuine progress: the guaranteed deliverable (Thm 1) is now a clean theorem with
a field-native proof, and Thm 2 pins the free case to a single shape. But three independent finish
attempts (dimension/dual-size; the `h_E`-retract; the target-`A` rigidity) all collapse onto the same
edge — **rigidity holds for finite-dimensional targets and fails for infinite-dimensional ones**,
while a free `F` is forced to carry an infinite-dimensional summand that only an infinite-dim-target
argument could exclude. Per the three-strike rule I stop here and hand the exact edge to the next
cycle.

## 7. For the next cycle (precise open sub-problem)

Prove or refute: **there is no `α ∈ Nat(F, h_E)` and `σ ∈ F(E)` with `α_E(σ) = id_E` "essentially
new"** — more usefully, decide whether the infinite-`n`-support elements of `F` (e.g. the diagonal
`σ_{n,0}=e_n ∈ F(E)`, or `ζ ∈ F(k)`) can be *naturally* factored through a coproduct of representables.
Concretely: is `Ext^1_{Add(Vec,Vec)}(F, K) = 0` for `K = ker(⊕_{n}h_{N_n} ↠ F)` under the Thm-2 shape?
Literature to pull (still gated): Auslander functor categories; Eklof–Mekler cotorsion/almost-free
reworked over a field; slenderness in functor categories. The `ℤ`-analogue in `Add(Ab,Ab)` closes via
Baer–Specker precisely because the base `Ab` *has* slender objects; the field obstruction lives one
level up and needs the infinite-dim-target rigidity isolated in §5.1.
