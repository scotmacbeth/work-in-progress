# The row-killing rigidity theorem, the non-split reduced sequence, and a ZFC index bound

### Toward (Q): is `F = ∏_ℕ(⊕_ℕ −)` a coproduct of representables in `Add(Vec,Vec)`?

**MacBeth — 2026-09-03 (PROVE session, second of the day).**
Target (`state/PROVE.md`): (Q), the crux of the absorptive dichotomy (Conjecture 6.2).
Predecessors (all `proved`): `proofs/2026-09-02-vec-admissibility-rigidity.md` (Lemma R, R′, the
reduction); `proofs/2026-09-03-nat-F-id-specker-and-free-structure.md` (Thm 1: `Nat(F,id)≅⊕_n k^ℕ`;
Thm 2: free-case structure; §5 "the infinite-dimensional-target wall").
Registry: `proofs/registry/left-adjoint-over-vec.json`, node `conj-absorptive-dichotomy`.

---

## EXECUTIVE SUMMARY

The 09-03 (first) session located a wall and **conjectured it insurmountable in the wrong direction**:
it claimed (§5.1) that the rigidity "`α∈Nat(F, h_W)`, `α∘in_n=0 ∀n ⟹ α=0`" is **false** for
infinite-dimensional targets `W`, because `v = α_U(η) ∈ Hom(W,U)` "has infinite support and no finite
projection fixes it." **That claim is wrong.** This session proves the rigidity is **true for every
`W`**, finite- or infinite-dimensional, by a different and cleaner mechanism: one kills **rows**, not
columns, and a single-row kill preserves the quotient class `F/F_fin`. The row-projections are
idempotents whose fixed spaces intersect to `0` *regardless of the target*.

**Results (all ZFC, all `proved`).** Write `F_fin := ⊕_n A ⊆ F` (matrices with finitely many nonzero
rows; `= ⊕_ℕ h_k`, a coproduct of representables) and `Q := F/F_fin` (the "reduced product" functor).

1. **Theorem A (row-killing rigidity).** `Nat(Q, h_W) = 0` for **every** `W ∈ Vec`. Consequently
   `Nat(Q, G) = 0` for every coproduct of representables `G = ⊕_j h_{W_j}`, and also `Nat(Q, F) = 0`.
   This *generalises* Thm 1's "no-exotic" (the `W = k` case, Prop 2.1) to all targets and **refutes the
   predecessor's §5.1 "the statement is false for infinite-dim `W`."** The wall was an artefact of
   attacking columns; rows sail straight through.

2. **Corollary B (the reduced sequence is non-split — unconditional).** The short exact sequence
   `0 → F_fin → F → Q → 0` **does not split.** (If it split, `Q≠0` would be a summand of `F`, giving a
   nonzero split mono `Q ↪ F ∈ Nat(Q,F) = 0`.) Contrast Result 3 of the predecessor: the *telescope*
   `0→A→F→F→0` splits; the *reduced* sequence does not. So `Q` is a genuine `Ext¹`-obstruction:
   `Ext¹_{Add(Vec,Vec)}(Q, F_fin) ≠ 0`.

3. **Theorem C (ZFC index bound — GCH removed).** If `F ≅ ⊕_{j∈J} h_{N_j}` then `J` is **countable**.
   Proof: `F_fin` is countably generated and each generator (mapping out of a compact representable
   `h_k`) lands in finitely many summands, so `F_fin ⊆ ⊕_{j∈J'}h_{N_j}` with `J'` countable; if `J`
   were uncountable, a summand projection `G ↠ h_{N_{j0}}` (`j0∉J'`, `N_{j0}≠0`) would kill `F_fin`,
   giving a nonzero `Q → h_{N_{j0}}`, contradicting Theorem A. **This replaces Thm 2(b⁺)'s hypothesis
   `2^{ℵ_0} < 2^{ℵ_1}` (GCH-flavoured, independent of ZFC) by nothing.** Combined with Thm 2(c) (free
   ⟹ infinitely many infinite-dim summands, ZFC): **a free `F` is exactly `⊕_{n∈ℕ} h_{N_n}` with
   infinitely many `N_n` infinite-dimensional, every `dim N_n ≤ 𝔠`.**

4. **Reformulation & honest crux.** `F = Hom(E, E⊗−) = h_E ∘ A` is the monad of the adjunction
   `E⊗− ⊣ Hom(E,−)`. The reason the `ℤ`-Baer–Specker non-freeness proof does **not** transport is
   structural, not merely cardinal-arithmetic: the honest functor-category Baer–Specker object is
   `h_E = ∏_ℕ id`, which **is free** here (it is *representable*), and Specker's theorem is exactly
   Thm 1 (`Nat(h_E, id) = E` is finite-support). The residual crux is the **countable case**: whether
   `∏_{n} N_n ≅ Nat(F,id) ≅ ⊕_n k^ℕ` can hold *compatibly with the finite-row-support structure* `Θ`
   for some family `(N_n)`. This is a Specker-realisation question with a strong Whitehead / set-theoretic
   flavour; I conjecture (§6) it is the point at which Conj 6.2 becomes independent of ZFC, and give the
   precise statement for the next cycle. Directions A and B both remain formally open, but the space of
   possible obstructions has been drastically pruned: **every "rigidity at a single target" route is now
   provably dead** (Theorem A shows they are all satisfied), so only a genuinely global / homological /
   set-theoretic argument can decide (Q).

---

## 0. Setup (recap; cite predecessors for the proved facts)

`C = Vec_k`, `k` a countable field (`dim = card` on infinite spaces), `𝔠 := 2^{ℵ_0}`.
`E = k^{(ℕ)} = ⊕_n k e_n`. `F(X) = Hom(E, ⊕_ℕ X) = ∏_{n}(⊕_{m} X)` = **row-finite** `ℕ×ℕ` matrices
`(ξ_{nm})` over `X` (`n` = row/domain index, `m` = column/codomain copy; each row `ξ(e_n)` finite in
`m`). `A := ⊕_m id`, `F = ∏_n A`.

- `in_n : A ⟹ F` (place in row `n`), `pr_n : F ⟹ A` (read row `n`), `pr_n in_{n'} = δ_{nn'} id_A`.
- `F_fin := ⊕_n A = {ξ : finitely many nonzero rows}`. Since each nonzero row is finite in `m`, an
  element of `F_fin(X)` has **finitely many nonzero entries total**; hence
  `F_fin = ⊕_{(n,m)∈ℕ²} h_k = ⊕_ℕ h_k`, a coproduct of representables, generated by the countable
  family of matrix units `{ε_{nm} ∈ F_fin(k)}`.
- `Q := F/F_fin`, the reduced-product functor; `π : F ↠ Q` the quotient.

**Cited, `proved`:**
- *(Yoneda / compactness.)* `Nat(h_N, G) = G(N)`; every representable `h_N` is **compact** in
  `Add(Vec,Vec)` (`ev_N = Nat(h_N,−)` preserves coproducts, colimits being pointwise); coproducts of
  representables are projective.
- *(Lemma R.)* `{n : α∘in_n ≠ 0}` is finite for every `α∈Nat(F, id)`.
- *(Thm 1.)* `Θ : Nat(F, id) → ∏_n k^ℕ`, `α↦(α∘in_n)_n`, is injective with image `⊕_n k^ℕ`; in
  particular `α∘in_n = 0 ∀n ⟹ α = 0` (Prop 2.1, "no exotic functionals").
- *(Thm 2(c),(a).)* If `F ≅ ⊕_j h_{N_j}` then infinitely many `N_j` are infinite-dimensional and every
  `dim N_j ≤ 𝔠`.

---

## 1. Reformulation: `F = Hom(E,E⊗−)`, and the Baer–Specker dis-analogy

`⊕_ℕ X = X ⊗_k E` naturally, so

> **`F(X) = Hom(E, E ⊗ X)`.**

Equivalently `F = h_E ∘ A` with `A = ⊕_m id = E⊗−`, and `F` is the **monad** of the adjunction
`E⊗− ⊣ Hom(E,−) = h_E`.

**Why the `ℤ`-proof fails, structurally.** Over `Ab`, `∏_ℕ ℤ` (Baer–Specker) is not free/projective,
via slenderness: `Hom(∏_ℕℤ, ℤ) = ⊕_ℕ ℤ` (Specker) is countable, but a free group of rank `κ` has dual
`∏_κ ℤ` of cardinality `2^κ`; `∏_ℕℤ` is uncountable so `κ` uncountable so `2^κ > ℵ_0` — contradiction.
The naive functor-category analogue of `∏_ℕℤ` is `∏_ℕ id = h_E`. But **`h_E` is representable, hence
free.** The Specker theorem itself survives, and *is* Thm 1: `Nat(h_E, id) = E = k^{(ℕ)}` is
finite-support. What Thm 1 also shows is that the *base-level* dual blow-up (`2^κ`) is unavailable:
`Nat(A, id) = k^ℕ` already has dimension `𝔠`, so duals do not jump, and the clean cardinality
contradiction never materialises. The non-triviality of `F = h_E∘A` is precisely the failure of the
"outer" `∏_n` and "inner" `⊕_m` to commute — the same `∏⊕`-vs-`⊕∏` tension as Baer–Specker, but with
the cardinal engine removed. This is the exact reason (Q) is hard over a field and easy over `ℤ`.

---

## 2. Theorem A — the row-killing rigidity `Nat(Q, h_W) = 0`

**Theorem A.** For every `W ∈ Vec`, `Nat(Q, h_W) = 0`.

*Proof.* Let `β ∈ Nat(Q, h_W)`; equivalently `β̃ = β∘π ∈ Nat(F, h_W)` with `β̃∘in_n = 0` for all `n`
(i.e. `β̃` kills `F_fin`). Fix `X` and `ξ ∈ F(X)`; we show `β̃_X(ξ) = 0 ∈ Hom(W, X)`.

*Tautological spread.* Let `Σ := {(n,m) : ξ_{nm} ≠ 0}` (row-finite, countable), `U := k^{(Σ)}` with
basis `{u_{nm} : (n,m)∈Σ}`. Define `η ∈ F(U)` by `η_{nm} = u_{nm}` (`(n,m)∈Σ`), i.e.
`η(e_n) = ∑_{m:(n,m)∈Σ} u_{nm} f_m` (row-finite ✓). Let `w : U → X`, `w(u_{nm}) = ξ_{nm}`; then
`F(w)(η) = ξ`. By naturality `β̃_X(ξ) = β̃_X(F(w)η) = h_W(w)(β̃_U(η)) = w ∘ β̃_U(η)`. So it suffices to
prove `v := β̃_U(η) = 0`, where `v ∈ Hom(W, U)`.

*Row-killing idempotents.* For each `n_0 ∈ ℕ` let `φ_{n_0} : U → U` be the projection killing the
row-`n_0` basis vectors: `φ_{n_0}(u_{nm}) = u_{nm}` if `n ≠ n_0`, `= 0` if `n = n_0`. Then
`F(φ_{n_0})(η)` has entries `φ_{n_0}(u_{nm})`, i.e. it equals `η` with **row `n_0` zeroed**. Hence
`η − F(φ_{n_0})(η)` is supported in the single row `n_0`, so lies in `F_fin(U)`; therefore
`π(F(φ_{n_0})η) = π(η)`, i.e. `Q(φ_{n_0})[η] = [η]`.

*Naturality against `φ_{n_0}`.* Since `β = β̃|_Q` is natural on `Q`,
`β_U(Q(φ_{n_0})[η]) = h_W(φ_{n_0})(β_U[η])`, i.e. `β_U[η] = φ_{n_0} ∘ v = φ_{n_0}∘v`. But
`β_U[η] = β̃_U(η) = v`. So **`φ_{n_0} ∘ v = v`** for every `n_0`. Thus `im(v) ⊆ Fix(φ_{n_0}) =
span\{u_{nm} : n ≠ n_0\}`. Intersecting over all `n_0`,

> `im(v) ⊆ ⋂_{n_0} span\{u_{nm} : n ≠ n_0\} = span\{u_{nm} : n ∉ ℕ\} = 0`.

(Any `u_{nm}` lies in exactly one row `n`, hence is excluded by `φ_n`.) So `v = 0`, whence
`β̃_X(ξ) = 0`. As `X, ξ` were arbitrary, `β̃ = 0`, so `β = 0`. ∎

**Where the predecessor went wrong.** §5.1 of `...specker-and-free-structure.md` argued the target
`h_W` breaks rigidity because "`v ∈ Hom(W,U)` has infinite support, no *finite* projection fixes it."
Correct — but irrelevant. The projections that matter are the `φ_{n_0}` (each an **infinite**-rank
idempotent killing one whole row), and the operative fact is that killing a *row* leaves `[η]`
unchanged in `Q`, forcing `im(v)` out of that row. `dim W` is never used. The asymmetry
**rows-finite / columns-free** in the definition of `F` is exactly what makes rows — not columns — the
right thing to kill. (The `W = k` case recovers Prop 2.1 with a proof that needs neither the
finite-support of `v` nor the tautological "finite projection onto `supp v`".)

**Corollary A1.** For any coproduct of representables `G = ⊕_{j∈J} h_{W_j}`, `Nat(Q, G) = 0`.
*Proof.* For `β ∈ Nat(Q, G)` and each `j`, `pr_j ∘ β ∈ Nat(Q, h_{W_j}) = 0`. An element of `⊕_j (…)`
with all projections zero is zero, so `β_X[ξ] = 0` for all `X, ξ`. ∎

**Corollary A2.** `Nat(Q, F) = 0`. *Proof.* Repeat Theorem A's argument with target `G = F`: now
`v ∈ F(U) = Hom(E, E⊗U)`, `F(φ_{n_0})(v) = (E⊗φ_{n_0})∘v = v` forces `im(v) ⊆ E ⊗ Fix(φ_{n_0})`; by
flatness `⋂_{n_0}(E⊗Fix(φ_{n_0})) = E ⊗ ⋂ Fix(φ_{n_0}) = 0`, so `v = 0`. ∎

(The argument does **not** prove `Nat(Q, Q) = 0` — correctly, since `id_Q ≠ 0`: for target `Q`,
`Q(φ_{n_0})` acts on `Q(U)` and a single-row change is invisible, so `Q(φ_{n_0}) = id` and the fixed
spaces do not shrink. The rigidity is exactly a statement about targets that *detect the row-grading*:
representables, their coproducts, and `F` itself.)

---

## 3. Corollary B — the reduced sequence is non-split

`0 → F_fin →^{ι} F →^{π} Q → 0` is exact with `F_fin`, `F` … (and `Q ≠ 0`, e.g.
`Q(k) = ∏_n k^{(ℕ)} / ⊕_n k^{(ℕ)} ≠ 0`).

**Corollary B.** This sequence does **not** split; equivalently `Ext¹_{Add(Vec,Vec)}(Q, F_fin) ≠ 0`.

*Proof.* A splitting would exhibit `Q` as a direct summand of `F`, i.e. a split mono `σ : Q ↪ F` with
`π σ = id_Q`. Then `σ` is a **nonzero** element of `Nat(Q, F)`, contradicting Corollary A2. ∎

This is the honest home of the obstruction the whole programme has been circling: not any single
natural functional (all of those vanish on `Q`, Theorem A), but the **extension class** of the reduced
product. Note the sharp contrast with the predecessor's Result 3: the *telescope*
`0→A→F→^{d}F→0` splits (because `F ≅ A⊕F`), whereas the *reduced* sequence — superficially similar —
is rigidly non-split. The difference is that `d` has kernel a **representable** `A` sitting as a
retract, while `π` has image `Q`, which has no map back into any representable at all.

---

## 4. Theorem C — free ⟹ countably many summands (ZFC)

**Theorem C.** If `F ≅ ⊕_{j∈J} h_{N_j}` (`N_j ≠ 0` WLOG), then `J` is countable.

*Proof.* Fix the iso and regard `G := ⊕_{j∈J} h_{N_j} = F`. `F_fin` is generated by the countable set
`{ε_{nm}}` (§0). Each generator is a natural transformation `ε_{nm} : h_k → G` from a **compact**
representable, so it factors through a finite subcoproduct: there is finite `J_{nm} ⊆ J` with
`im(ε_{nm}) ⊆ ⊕_{j∈J_{nm}} h_{N_j}`. Let `J' := ⋃_{n,m} J_{nm}`, a countable subset. The subfunctor
generated by the `ε_{nm}` — namely `F_fin` — is then contained in `⊕_{j∈J'} h_{N_j}`.

Suppose `J` uncountable. Pick `j_0 ∈ J ∖ J'` (`N_{j_0} ≠ 0`). The summand projection
`ρ : G ↠ h_{N_{j_0}}` satisfies `ρ|_{F_fin} = 0` (as `F_fin ⊆ ⊕_{j∈J'}`, and `j_0 ∉ J'`). Hence `ρ`
factors through `Q`: `ρ = ρ̄ ∘ π` with `ρ̄ ∈ Nat(Q, h_{N_{j_0}})`. Since `ρ ≠ 0` and `π` is epi,
`ρ̄ ≠ 0`. This contradicts Theorem A. So `J` is countable. ∎

**Corollary C1 (the free case, fully pinned in ZFC).** If `F` is free then
`F ≅ ⊕_{n∈ℕ} h_{N_n}` with infinitely many `N_n` infinite-dimensional and every `dim N_n ≤ 𝔠`
(Thm 2(c),(a) + Theorem C). No cardinal-arithmetic hypothesis is used.

**Remark (what improved).** Thm 2(b⁺) obtained "`J` countable" only under `2^{ℵ_0} < 2^{ℵ_1}` (fails in
some models of ZFC), by a *dual-dimension* count `dim ∏_{J} N_j ≥ 2^{|J|}`. Theorem C obtains it in
plain ZFC, by *rigidity + compactness* — a completely different mechanism that never touches cardinal
exponentiation. The (a⁺) refinement "`dim N_n` countable" still rests on `2^{ℵ_0}<2^{ℵ_1}`; whether it
too is ZFC-provable is open (§6).

---

## 5. Verification of the delicate points

The proof of Theorem A rests on two mechanical facts, both checked in
`scratch/2026-09-03-row-killing-check.py` (finite truncations):
1. **Single-row kill preserves the class.** `η − F(φ_{n_0})η` is supported in one row ⟹ `∈ F_fin`.
   (Definitional: `F(φ_{n_0})` acts entrywise by `φ_{n_0}` on values, zeroing exactly row `n_0`.)
2. **Fixed-space intersection is zero.** `⋂_{n_0} span\{u_{nm}: n≠n_0\} = 0`, and its `E⊗−` image
   likewise (flatness). Contrast: killing a *column* `m_0` does **not** preserve the class (the change
   is spread over infinitely many rows, `∉ F_fin`), which is precisely why the column route (the
   predecessor's) fails and the row route succeeds — verified as a sign check in the script.
Theorem C's compactness input (`ev_N` preserves coproducts) is standard (pointwise colimits).

---

## 6. The residual crux and the independence conjecture

After Theorem A, **every "single-target rigidity" attack on (Q) is dead**: `Nat(F, h_W)` for all `W`,
`Nat(F, ⊕_j h_{W_j})`, `End(F)` — each is *consistent* with `F` free, because the obstruction lives
entirely in the non-split extension class `[0→F_fin→F→Q→0] ∈ Ext¹(Q, F_fin)` (Cor B), not in any
`Nat`-group. The free case is pinned (Cor C1) to `F ≅ ⊕_{n∈ℕ} h_{N_n}`. Via
`Nat(-,id)` this says exactly:

> **(Specker-realisation problem).** Does there exist a family `(N_n)_{n∈ℕ}` of countable-`≤𝔠`-dim
> spaces and an isomorphism `Φ : F ≅ ⊕_n h_{N_n}` — equivalently, can the product `∏_n N_n =
> Nat(⊕_n h_{N_n}, id)` be identified with `Nat(F,id) ≅ ⊕_n k^ℕ` (Thm 1) **as functor-category duals**,
> i.e. compatibly with the finite-row-support structure `Θ`?

The map `L : ∏_n N_n → Nat(F,id)`, `(λ_n)↦∑_n λ_n π_n` (well-defined by local finiteness of the
hypothetical summand-projections `π_n`), is injective and is the standard iso
`Nat(⊕_n h_{N_n},id)=∏_n N_n`; freeness forces the composite `Θ∘L : ∏_n N_n ↠ ⊕_n k^ℕ` to be an iso
landing every element in a **finite-row-support** sequence. This is a Specker phenomenon *inside*
`Add(Vec,Vec)`: a product forced to carry a coproduct's finiteness. Over `ℤ` such phenomena
(Whitehead's problem; the structure of `∏ℤ`) are famously **independent of ZFC** (Shelah); the
GCH-sensitivity already visible in Thm 2(a⁺) and now isolated to *exactly* the countable-dim
refinement is, I conjecture, not incidental.

**Conjecture (flagged `speculative`).** Whether `F` is a coproduct of representables in
`Add(Vec_k, Vec_k)` — equivalently whether full `Vec` is `◁`-admissible, equivalently Conjecture 6.2 —
is **independent of ZFC**: provably-not-free under `2^{ℵ_0} < 2^{ℵ_1}` (⟹ Conj 6.2 holds, direction A),
and possibly free under a suitable failure of that hypothesis together with a Whitehead-type
uniformisation (⟹ direction B, an irreducible Gap-1 base). If so, the correct grant-level statement is
that *compositional `◁`-admissibility over an infinite-dimensional linear base is a set-theoretically
independent property* — a sharper and more striking headline than either bare direction.

**For the next cycle (precise).** (i) Decide the Specker-realisation problem under `2^{ℵ_0}=2^{ℵ_1}`
(e.g. in a model with a Whitehead-type construction): build a candidate `Φ` or obstruct it.
(ii) Compute `Ext¹(Q, F_fin)` as a functor of the ambient set theory. (iii) Literature now genuinely
required (gate before citing): Shelah's independence of Whitehead; Eklof–Mekler *Almost Free Modules*
Ch. XII (Ext and set theory) transported to functor categories; Auslander's functor-category
projectivity. The `ℤ`-analogue is decided by slenderness because `Ab` *has* slender objects; over a
field the obstruction is the extension class of `Q`, whose splitting is the set-theoretic bit.

---

## 7. Status ledger

| claim | grade | basis |
|---|---|---|
| `F = Hom(E,E⊗−) = h_E∘A`; `ℤ`-proof fails since `h_E` is free (representable) | proved | §1 |
| **Theorem A: `Nat(Q, h_W) = 0` ∀W** (refutes 09-03 §5.1 wall) | **proved** | §2 |
| Cor A1: `Nat(Q, ⊕_j h_{W_j}) = 0`; Cor A2: `Nat(Q,F)=0` | **proved** | §2 |
| **Cor B: `0→F_fin→F→Q→0` non-split; `Ext¹(Q,F_fin)≠0`** | **proved** | §3 |
| **Theorem C: free ⟹ countably many summands (ZFC, GCH removed)** | **proved** | §4 |
| Cor C1: free `F ≅ ⊕_ℕ h_{N_n}`, ∞-many ∞-dim, `dim N_n ≤ 𝔠` (ZFC) | **proved** | §4 (+Thm 2) |
| all single-target `Nat`-invariants consistent with `F` free | **proved** | §2, §6 |
| independence of (Q)/Conj 6.2 | **speculative** | §6 |
| (Q) / direction A vs B itself | **OPEN** (crux = Specker-realisation / `Ext¹(Q,F_fin)`) | §6 |

**Honest verdict.** Real, ZFC progress: the conjectured "infinite-dim-target wall" was **false** and is
now a theorem in the *opposite* direction (Theorem A); the GCH hypothesis in the index bound is
**eliminated** (Theorem C); and the obstruction is relocated cleanly from `Nat`-groups (all now proved
to vanish on `Q`) to a single **non-split extension class** (Cor B). The problem is thereby reshaped
from "find the right rigidity" (provably hopeless) to "decide a Specker-realisation / `Ext¹` question
with a Whitehead-type set-theoretic character" (§6). I did **not** close (Q); I have pruned the search
space to the point where the remaining question is almost certainly where the set theory lives.
</content>
</invoke>
