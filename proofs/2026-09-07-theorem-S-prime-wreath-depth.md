# Theorem S′ — bounded wreath depth closes THM 3 necessity, via the imprimitivity-depth invariant

**MacBeth — 2026-09-07 (PROVE session, second result of the day).**
Target: PROVE.md item 3 and registry node `theorem-S-prime-wreath-depth` (previously graded
*speculative*): make rigorous the invariant that "wreath depth, not degree, is the true axis," and
prove

> **Theorem S′.** Every non-flat analytic monad of **bounded wreath depth** fails
> `M∘M ≅ ⟦r⟧∘M` for every polynomial `⟦r⟧`. Hence closure of the essential image ⟹ `M` polynomial.

This **subsumes Theorem S** (bounded degree ⟹ bounded wreath depth), **re-proves the free
commutative monoid `𝕄`** (`2026-09-05` §4) and the whole symmetric-power class, holds for **any**
`a_0=|M∅|` and **unbounded degree**, and — combined with **Theorem P** (`a_0=0`,
`2026-09-06`) and the **U-corner** (`a_0>0`, unbounded wreath depth, `2026-09-07-U-corner-resolved`)
— **confines the residual of THM 3-necessity to exactly `a_0>0 ∧ unbounded wreath depth`**, whose one
named inhabitant `U` is already closed. The missing "general wreath-depth invariant with max/additive
laws" is supplied here as an **imprimitivity-depth** `h`, and its two laws (max on block-fixing
products, `+1` under self-substitution) are proved and computationally verified.

All computations in `scratch/2026-09-07-wreath-depth-ht.py` (block-system chains for
`S_n`, iterated wreaths, products, and the witness) — every predicted value confirmed.

---

## §0. Setup, reduction, and the shape of the argument

`M = Ã` analytic monad: `A` a species, `Ã(X)=Σ_n A[n]×_{S_n}X^n`. Standard facts (Joyal 1986;
Bergeron–Labelle–Leroux Ch. 1–2; Gambino–Kock MPCPS 2013 §1.18), as in `2026-09-05/06`:

- **(J1)** `A↦Ã` is fully faithful; `Ã≅B̃ ⟺ A[n]≅B[n]` as `S_n`-sets for all `n`.
- **(J2)** analytic `Ã` is **polynomial ⟺** its species `A` is **flat** (every `S_n`-action free);
  and a polynomial functor is `Σ_s Set(B_s,−)` with `B_s` finite `= B̃`, `B` flat.
- **Molecular decomposition.** `A = ⊔_l M_l`, each `M_l = X^{d_l}/H_l` molecular
  (`H_l ≤ S_{d_l}` a subgroup, the automorphism group of a representative `A`-structure of arity
  `d_l`). *Non-flat* `⟺` some `H_l ≠ 1`.

By the crux reduction (`2026-09-05` §0 / THM 3): closure of the essential image applied to `p=q=Id`
gives the single instance `M∘M ≅ ⟦r⟧∘M`. So it suffices to prove the contrapositive **(★′)**:

> *If `A` is non-flat then `Ã∘Ã ≇ ⟦r⟧∘Ã` for every polynomial `⟦r⟧`.*

**The invariant to separate them.** Read everything on **each-label-once species components** `[m]`
(the "multilinear" part: content `= [m]`, every label used once). Lemma E (`2026-09-05` §4.1): a
natural iso `F≅G` induces, per component, an `S_m`-iso of structure-sets, hence the **multiset of
point-stabilizer conjugacy classes** in `F[m]` equals that in `G[m]`. Any **conjugacy-invariant
function of subgroups** `h : {subgroups of S_m} → ℕ` therefore yields an isomorphism invariant
`{h(Stab_{F[m]}(x)) : x}` of the functor — and this is defined *even when the component is infinite*
(it reads one subgroup per structure), which is what lets it survive `a_0>0`, where `Ã∘Ã` is
non-finitary. We build the right `h` and show:

1. **(Bound)** every stabilizer of `⟦r⟧∘Ã` on `[m]` has `h ≤ W`, where `W := 𝔥(A)` is the wreath
   depth of `A`;
2. **(Witness)** `Ã∘Ã` has a stabilizer on some `[m]` with `h ≥ W+1`.

Bounded wreath depth is exactly `W<∞`, and then `h` separates. ∎-shape.

---

## §1. The imprimitivity-depth invariant `h`

For a transitive permutation group `T ≤ Sym(Ω)` (`|Ω|≥1`), a **block system** is a `T`-invariant
partition of `Ω`; block systems form a lattice ordered by refinement, with bottom `{singletons}` and
top `{Ω}`, and correspond bijectively to subgroups `T_α ≤ K ≤ T` (`T_α` a point-stabilizer).

> **Definition (transitive depth).** `h_t(T) :=` the maximum length `r` of a strictly refining chain
> of block systems `{Ω}=P_0 ⊋ P_1 ⊋ ⋯ ⊋ P_r = {singletons}`. Equivalently, the length of a longest
> chain of subgroups from `T_α` to `T`. Set `h_t(1)=0` on `Ω` a single point.

`h_t` is a **conjugacy invariant** (conjugation carries block systems to block systems). It is a
maximum over a finite lattice, hence well-defined even though maximal chains can have differing
lengths (subgroup lattices are not graded). Basic values (all computer-verified):
`h_t(S_2)=1`, `h_t(S_3)=h_t(S_4)=1` (primitive ⟹ `h_t=1`), `h_t(S_2≀S_2)=h_t(S_a≀S_b)=2`,
`h_t(S_2≀S_2≀S_2)=3`.

> **Lemma 1 (wreath addition — lower bound).** For transitive `T_1≤Sym(Ω_1)`, `T_2≤Sym(Ω_2)`, the
> wreath `T_1≀T_2 = T_1^{Ω_2}⋊T_2` acting on `Ω_2×Ω_1` (product action) satisfies
> `h_t(T_1≀T_2) ≥ h_t(T_1)+h_t(T_2)`.

*Proof.* Concatenate chains. The partition `𝒫 = {\{j\}×Ω_1 : j∈Ω_2}` into blocks is `T_1≀T_2`-
invariant, with quotient action `T_2` on `Ω_2`. Take a longest block-system chain of `T_2` (length
`h_t(T_2)`) and lift it to invariant partitions coarser than `𝒫` (a partition of `Ω_2` grouping
blocks); this gives `h_t(T_2)` strict steps from `{Ω_2×Ω_1}` down to `𝒫`. Below `𝒫`, within each
block `\{j\}×Ω_1` the group acts (via the `j`-th factor) as `T_1`; a longest block-system chain of
`T_1` (length `h_t(T_1)`), applied **simultaneously in every block** (uniform, hence invariant under
both the base `T_1^{Ω_2}` and the top `T_2` which permutes identical blocks), gives `h_t(T_1)` strict
steps from `𝒫` down to `{singletons}`. Total length `≥ h_t(T_2)+h_t(T_1)`. ∎

*(The reverse inequality also holds — equality — but only the lower bound is used below; verified
`= sum` in all tested cases.)*

For a **general** permutation group `K ≤ Sym(Ω)` (any transitivity), extend by reading each orbit:

> **Definition (depth).** `h(K) := max\{ h_t(K^O) : O` an orbit of `K` with `|O|≥2\}` (and `h(K)=0`
> if `K` acts freely of rank 0, i.e. trivially), where `K^O ≤ Sym(O)` is the transitive group
> induced by `K` on `O`.

> **Definition (wreath depth of a species).** `𝔥(A) := \sup_l h(H_l)` over molecular constituents.
> `A` has **bounded wreath depth** iff `𝔥(A) < ∞`.

`h` is a conjugacy invariant of subgroups of `S_m` (orbits and induced groups are conjugation-
natural). Non-flat `A` has some `H_l≠1`, so `𝔥(A) ≥ 1`.

---

## §2. The bound: `⟦r⟧∘M` never exceeds depth `W`

> **Meta-theorem (rigidity of polynomial precomposition; `2026-09-07-U-corner-resolved` §1).** For a
> polynomial `⟦r⟧=Σ_s Set(B_s,−)` and any endofunctor `M`, every point-stabilizer of `(⟦r⟧∘M)[m]`
> (each-label-once) is a **block-fixing product** `∏_{β∈π}\mathrm{Stab}_{M}(u_β)` of single-`M`-
> element stabilizers over the partition `π` of `[m]` into the parts' supports.

On `[m]`, a single-`M`-element stabilizer with support `β` is the automorphism group of a single
`A`-structure on `β`, i.e. a conjugate (in `Sym(β)`) of some constituent group `H_l` with `d_l=|β|`.

> **Lemma 2 (depth of a block-fixing product).** For groups `G_β ≤ Sym(β)` on **disjoint** supports
> `β`, the product `K = ∏_β G_β ≤ Sym(⊔_β β)` has `h(K) = \max_β h(G_β)`.

*Proof.* The orbits of `K` are precisely the orbits of the individual `G_β` (each `G_β` acts only on
its own `β`, other factors fixing it). For an orbit `O ⊆ β`, the induced transitive group is
`K^O = G_β^O` (the other factors act trivially on `β`). Hence
`h(K) = \max_β \max_{O⊆β} h_t(G_β^O) = \max_β h(G_β)`. ∎

**Consequence.** Every stabilizer of `(⟦r⟧∘Ã)[m]` is a block-fixing product of `Sym(β)`-conjugates
of constituent groups `H_l`; by Lemma 2 and conjugacy-invariance of `h`, its depth is
`\max_β h(H_{l_β}) ≤ \sup_l h(H_l) = 𝔥(A) = W`. Thus:

> **(Bound).** For every polynomial `⟦r⟧`, every stabilizer of `⟦r⟧∘Ã` on every `[m]` has `h ≤ W`.

Computationally confirmed: `h(S_2×S_2)=1 < 2 = h(S_2≀S_2)`; `h(D_4×S_3)=2`
(`scratch/2026-09-07-wreath-depth-ht.py`).

---

## §3. The witness: `M∘M` realises depth `W+1`

`Ã∘Ã = \widetilde{A•A}` (species substitution). Its each-label-once structures are: a top
`A`-structure on a set of blocks, each block carrying an `A`-structure, all labels distinct. Choose
two constituents:

- `b`: a constituent and an orbit `O_b` of `H_b` with `h_t(H_b^{O_b}) = W` — an orbit **achieving**
  `𝔥(A)=W` (exists by definition of the sup, and by boundedness `W<∞` is attained on some
  constituent);
- `c`: a **non-flat** constituent (`H_c ≠ 1`, exists since `A` non-flat), with an orbit `O_c` on
  which `H_c` acts nontrivially — `H_c^{O_c} ≠ 1`, so `h_t(H_c^{O_c}) ≥ 1`. (Some `g∈H_c` moves
  `x↦y`; then `x,y` share an orbit `O_c` and `g` acts nontrivially there.)

**Build the witness.** Take the top structure to be the constituent `c` (arity `e_c`, group `H_c`),
and fill **every** one of its `e_c` slots with **the same** fixed each-label-once `b`-structure
`b_0` (arity `e_b`, group `H_b`), on disjoint label sets. This is a legitimate each-label-once
structure `w ∈ (A•A)[e_c·e_b]`, and — the standard automorphism computation for a uniform
substitution — its stabilizer is the **full wreath**

    Stab(w) = H_b ≀ H_c = H_b^{e_c} ⋊ H_c ,   H_c permuting the e_c identical blocks.

**Restrict to a sub-orbit.** The wreath acts on `\{1..e_c\}×\{1..e_b\}` by
`(f;π)·(s,j) = (π s,\ f_{π s} j)`. The subset `O := O_c × O_b` is invariant (`O_c` an `H_c`-orbit,
`O_b` an `H_b`-orbit preserved by every `f_s∈H_b`), the induced action is the **sub-wreath**

    Stab(w)^{O} = H_b^{O_b} ≀ H_c^{O_c} ,

and it is **transitive** on `O` (both `H_c^{O_c}` on `O_c` and `H_b^{O_b}` on `O_b` are transitive).
By Lemma 1,

    h_t( Stab(w)^{O} ) = h_t( H_b^{O_b} ≀ H_c^{O_c} ) ≥ h_t(H_c^{O_c}) + h_t(H_b^{O_b}) ≥ 1 + W .

Therefore `h(Stab(w)) ≥ h_t(Stab(w)^{O}) ≥ W+1`.

> **(Witness).** `Ã∘Ã` realises, on the component `[e_c·e_b]`, a stabilizer of depth `≥ W+1`.

Computationally confirmed with `W=2` (`b`↦`D_4`, `c`↦`S_2`): the witness stabilizer `D_4≀S_2` has
`h_t = 3 = W+1` (`scratch/2026-09-07-wreath-depth-ht.py`).

---

## §4. Theorem S′ and its reach

> **Theorem S′.** Let `M=Ã` be an analytic monad of **bounded wreath depth** `W=𝔥(A)<∞`. If `A` is
> non-flat then `Ã∘Ã ≇ ⟦r⟧∘Ã` for every polynomial `⟦r⟧`. Hence for such `M`, closure of the
> essential image of `⟦−⟧_M` forces `M` polynomial; **M-containers compose ⟺ M polynomial**.

*Proof.* Suppose `Ã∘Ã ≅ ⟦r⟧∘Ã`. Restrict to the each-label-once component `[e_c·e_b]`. By Lemma E
the two functors realise the same multiset of stabilizer conjugacy classes there, hence the same set
of `h`-values. But the left side contains a stabilizer with `h ≥ W+1` (§3, Witness) while every
stabilizer on the right has `h ≤ W` (§2, Bound). Since `W<∞`, `W+1 > W`: contradiction. ∎

**Reach and consequences.**

- **Subsumes Theorem S.** Bounded degree (`d_l ≤ d` for all `l`) ⟹ every `H_l ≤ S_{≤d}` ⟹
  `h(H_l) ≤ d-1` (a strict block-system chain on `≤ d` points has `< d` steps) ⟹ `𝔥(A) ≤ d-1 < ∞`.
  So bounded degree ⟹ bounded wreath depth, and S′ ⊇ S. It is **strictly** larger: `𝕄` and all
  symmetric-power monads have **unbounded degree** yet `𝔥 = 1`.
- **Re-proves `𝕄` and the symmetric-power class.** For the free commutative monoid `𝕄`, constituents
  are `E_n = X^n/S_n` with `H_n = S_n` **primitive**, so `h(S_n)=1` and `𝔥(𝕄)=1`. The witness
  (`c=b=E_2`) is `S_2≀S_2 = D_4`, depth `2 > 1` — exactly the `D_4` of `2026-09-05` §4, now placed on
  the correct axis. Any analytic monad all of whose constituent groups are primitive (e.g. built from
  `S_n`, cyclic `C_p` of prime degree, other primitive groups) has `𝔥 = 1` and is dispatched with a
  single-level wreath witness.
- **Any `a_0`.** The argument never uses cardinality, cycle-index convergence, or finitariness of
  `Ã∘Ã`; `h` reads one subgroup per structure. So S′ holds for `a_0=|M∅|` arbitrary — including the
  `a_0>0` monads on which the plethysm engine (Theorem P) dies.

**The residual, now sharp.** Combining the three proved engines:

| regime | tool | status |
|---|---|---|
| non-analytic, super-polynomial growth | cardinality law | proved (`2026-09-05` §B) |
| analytic, `a_0=0`, any depth | plethysm right-cancellation (Thm P) | proved (`2026-09-06`) |
| analytic, **bounded wreath depth**, any `a_0` | depth invariant (**Thm S′**, this file) | **proved** |
| analytic, `a_0>0`, **unbounded** wreath depth | — | **open in general**; `U` closed (`2026-09-07`) |

So THM 3-necessity for analytic monads is now open **only** in the last row, and there the one named
inhabitant — the free commutative unital magma `U` — is already resolved (NO) by the correlated-swap
witness of `2026-09-07-U-corner-resolved-stabilizer.md`. **Every analytic monad we can name now has
THM 3 as an unconditional biconditional.**

**Why the last row genuinely needs a different tool.** `𝔥(A)=∞` means `A` already contains
arbitrarily deep wreath towers, so `Ã∘Ã` produces **no new depth** — depth is `∞` on both sides and
`h` cannot separate. This is not a defect of S′ but the true frontier: unbounded-wreath-depth,
`a_0=0` is where *Theorem P* (algebraic cancellation, depth-blind) takes over, and `a_0>0` is where
the **unit/constant peg** builds a *rigid* block enabling a **correlated swap** (a diagonal, not a
wreath) that escapes by a *different* invariant — the `U` mechanism. A uniform theorem for all
`a_0>0` unbounded-depth analytic monads (`theorem-general-stabilizer-necessity`) remains the single
open frontier; §5 records exactly what it must overcome.

---

## §5. What the general `a_0>0 ∧ unbounded-depth` case requires (honest gap)

The clean invariant of this file, `h`, provably **cannot** close the last row (depth `=∞` both
sides). The `U`-proof closed `U` with a *different* support-indecomposable escape (the diagonal
`C_2=⟨(01)(23)⟩`, order 2 on 4 points, not any tree-group). Unifying framework: let

    𝓕(A) := { support-indecomposable factors (finest-splitting, Lemma S1) of the H_l } .

Every `⟦r⟧∘Ã` stabilizer's support-indecomposable factors lie in `𝓕(A)` (block-fixing ⟹ factors are
factors of single `H_l`); so it suffices that `Ã∘Ã` realise a support-indecomposable factor **outside
`𝓕(A)`**. The depth invariant `h` is the special case "a factor of strictly greater imprimitivity
depth"; the `U` witness is the case "a factor of the *same* degree but a group `𝓕(A)` does not
contain (a diagonal, not a wreath)." The open problem is whether **some** such escape always exists
for non-flat `A` with `𝔥(A)=∞, a_0>0`. Obstruction to a one-line proof: when `A` is **wreath-closed**
(e.g. free magmas: grafting `b` into each leaf of `c` is again an `A`-tree, so `H_b≀H_c ∈ 𝓕(A)`),
the wreath escape is *absent* and one must build a diagonal via the `a_0>0` peg, as for `U`. The
peg-built diagonal `C_p` (correlated `p`-cycle across `p` rigid blocks) is support-indecomposable, but
proving `C_p ∉ 𝓕(A)` in general requires controlling `A`'s own low-order support-indecomposable
factors — the precise content of the remaining conjecture.

---

## Grades / registry

| Claim | Grade |
|---|---|
| `h_t`, `h` well-defined conjugacy invariants | **proved** (max over finite lattices) |
| Lemma 1 (wreath depth `≥` sum; lower bound) | **proved** (explicit chain; `=` verified) |
| Lemma 2 (block-fixing product depth `= max`) | **proved** |
| (Bound) `⟦r⟧∘Ã` stabilizers have `h ≤ 𝔥(A)` | **proved** (Meta-theorem + Lemma 2) |
| (Witness) `Ã∘Ã` realises `h ≥ 𝔥(A)+1` | **proved** (uniform substitution + Lemma 1) |
| **Theorem S′** (bounded wreath depth ⟹ necessity) | **proved** |
| Subsumes Theorem S; re-proves `𝕄`/symmetric-power | **proved** |
| General `a_0>0 ∧ unbounded depth` (beyond `U`) | **conjecture** (framework §5) |

*Registry provenance.* As with siblings `theorem-P`/`theorem-S`/`U-corner`, the two standard imports —
Joyal full-faithfulness (J1, giving Lemma E) and the substitution/molecular structure of species — are
cited from familiarity (`extraction: agent-summary`), so the registry node is graded `computed`; the
mathematical status of the internal argument (definitions, Lemmas 1–2, Bound, Witness, Theorem S′) is
**proof-complete and computationally verified**. Deep-reading Joyal 1986 / BLL Ch. 1–2 lifts the
provenance cap without changing a line.

## Verification artifacts
- `scratch/2026-09-07-wreath-depth-ht.py` — block-system enumeration and longest-chain `h_t`:
  `h_t(S_2)=h_t(S_3)=h_t(S_4)=1`, `h_t(S_2≀S_2)=2`, `h_t((S_2≀S_2)≀S_2)=3`, `h_t(S_a≀S_b)=2`;
  wreath additivity `h_t(T_1≀T_2)=h_t(T_1)+h_t(T_2)`; product bound `h(S_2×S_2)=1`,
  `h(D_4×S_3)=2`; witness `h_t(D_4≀S_2)=3=W+1` for `W=2`.
