# The U-corner of THM 3 is resolved: `U∘U ≇ ⟦r⟧∘U` — necessity holds, via a fixed-point-free swap

**MacBeth — 2026-09-07 (PROVE session).**
Target: the two-outcome question **(★)** left open by `2026-09-06-conjecture-V-refuted.md` §6 —
*decide whether `U∘U ≅ ⟦r⟧∘U` for some polynomial functor `⟦r⟧`*, where `U` is the free
commutative **unital** (non-associative) magma monad (`a_0=1`, `U[n]=(2n−3)!!`), the canonical
inhabitant of THM 3's last open corner (`a_0>0 ∧ unbounded wreath depth`).

**Verdict: NO.** There is no polynomial `⟦r⟧` with `U∘U ≅ ⟦r⟧∘U`. Hence the essential image of
`⟦−⟧_U` is *not* closed under composition, and **THM 3's necessity holds at `U`**: the sharpest
residual corner does *not* break the biconditional. The proof uses neither the plethysm engine
(dead at `a_0=1`) nor a wreath-depth bound (`W=∞` at `U`) — it uses the **`Aut(X)`-stabilizer
invariant** of `2026-09-05` §4, read on species components. The witness is minimal: an element of
`(U∘U)[4]` whose stabilizer is a **single fixed-point-free involution**.

**The punchline: the unit is the weapon.** The `a_0=1` unit — long treated as a harmless "absorbing"
element (indeed it is what refuted Conjecture V's vacuity by *absorbing*, `2026-09-06`) — is exactly
what lets `U∘U` build a **rigid** block with no internal symmetry, so that two equal copies can be
swapped with the swap as their *only* symmetry. A polynomial (rigid-position) outer layer can never
produce that lone swap. `a_0>0` does not save the corner; it *supplies the counterexample.*

All computations verified in `scratch/2026-09-07-C2-witness.py`, `-sep-fast.py`, `-Hstar.py`,
`-percomponent-confirm.py`.

---

## §0. Why the standard tools are blocked, and the one that is not

Write `M = Ũ`. If `Ũ∘Ũ ≅ ⟦r⟧∘Ũ` then both sides are analytic functors, so (Joyal) their species
agree componentwise. The two proven engines fail exactly here:

- **Plethysm right-cancellation (Theorem P, `2026-09-06-lemmaN`)** needs `Z_M` to have **zero
  constant term** for `(−)∘Z_M` to be injective. `Z_U` has constant term `a_0=1`; worse, `Z_U∘Z_U`
  does not **converge** (the unit feeds every degree). Dead.
- **Wreath-depth / degree gap (Theorem S/S′)** needs **bounded** wreath depth. `U` has `W=∞`; the
  inner `Ũ` already supplies unbounded depth to `⟦r⟧∘Ũ`, so there is no gap. Dead.

The surviving tool is purely functorial, indifferent to `a_0` and to convergence:

> **Lemma E (stabilizer invariant, `2026-09-05` §4.1).** A natural iso `Θ:F≅G` of analytic
> endofunctors gives, on each **species component** `m` (the each-label-once part), an `S_m`-set
> isomorphism `F[m]≅G[m]`, hence preserves the set of point-stabilizer conjugacy classes occurring in
> `F[m]`. So `𝒮(F)[m] := \{ \mathrm{Stab}_{F[m]}(x) : x∈F[m] \}` (up to conjugacy) is an
> isomorphism invariant of `F`, for each `m`.

`𝒮` never sums anything — it reads one subgroup per structure — so it is defined even though
`Ũ∘Ũ` has **infinite** species components. That is the crack in the wall.

---

## §1. Meta-theorem: `⟦r⟧∘M` carries **no swap of parts**

The engine is a single structural fact about *polynomial* outer layers.

> **Meta-theorem (rigidity of polynomial pre-composition).** Let `M` be any endofunctor of `Set` and
> `⟦r⟧(Y)=Σ_{s∈S}Y^{B_s}` any polynomial functor. Every point-stabilizer occurring in the each-label-
> once component `(⟦r⟧∘M)[m]` is a **block-fixing product**
> `∏_{β∈π}\mathrm{Stab}_{M[m]}(u_β)` of single-`M`-element stabilizers, on the partition `π` of `[m]`
> induced by the parts' contents. No two parts are ever permuted.

*Proof.* An element of `(⟦r⟧∘M)[m]` is `(s,\ φ:B_s→M[?])` with total content `[m]`, each label once.
For `σ∈S_m`, `(⟦r⟧∘M)(σ)(s,φ)=(s,\ Mσ∘φ)`, which equals `(s,φ)` iff `Mσ(φ(b))=φ(b)` for **every**
`b∈B_s` — a function is fixed iff fixed pointwise; there is no quotient on the positions `B_s`. So
`\mathrm{Stab}(s,φ)=⋂_{b}\mathrm{Stab}(φ(b))`. Each-label-once forces the parts `φ(b)` of nonempty
content to have **disjoint** supports `β` partitioning `[m]` (a shared label would be used twice). For
disjoint blocks, `⋂_β[\mathrm{Aut\ on\ }β × \mathrm{Sym}(\text{rest})] = ∏_β\mathrm{Aut\ on\ }β` —
every point lies in exactly one constraining block, killing all complement-freedoms. ∎

The whole content is *"a function is fixed iff fixed pointwise."* **Polynomiality of the outer layer =
rigidity of positions = no permutation of `M`-parts.** `⟦r⟧∘M` sees only symmetry *inside individual
parts*, assembled by direct product. This is the general form of the `2026-09-05` `𝕄`-argument (there
single-`𝕄`-stabilizers are Young; here they are whatever `M` supplies).

> **Corollary (composition test).** If some `(M∘M)[m]` realizes a point-stabilizer that is **not** a
> block-fixing product of single-`M`-element stabilizers, then `M∘M ≇ ⟦r⟧∘M` for every polynomial
> `⟦r⟧`: the `M`-containers do not compose. `a_0`-agnostic; convergence-free; any `M`.

> **Remark (the each-label-once caveat — why this is not circular).** It is *essential* to read `𝒮`
> on species components, not on the raw set `(⟦r⟧∘M)(X)`. On the raw set (labels may repeat), the
> stabilizer of `(s,φ)` is `⋂_b\mathrm{Stab}(φ(b))` with parts that may **share labels**, ranging over
> *all* finite intersections of single-`M`-stabilizers — a strictly larger class. The witness group of
> §2, `⟨(0\,1)(2\,3)⟩`, *is* such an intersection over overlapping-support `U`-trees
> (`scratch/2026-09-07-Hstar.py` shows this for the `n=8` analogue). But realizing it that way
> **reuses labels**, placing that `⟦r⟧∘U`-element in a *higher* species component (content a multiset),
> not in component `[4]`. On component `[4]`, each-label-once forces disjoint parts and collapses the
> intersection to a block-fixing product. This is precisely why the naïve "compare raw stabilizer sets"
> attempt fails (they coincide) while the per-component argument succeeds.

---

## §2. The witness: a rigid block-swap in `(U∘U)[4]`

Recall `ŨY` = free commutative unital magma on `Y`: elements are the unit `E`, or commutative binary
trees with leaves in `Y` (the unit is absorbed, `μ(t,E)=t`). Over `X=\{0,1,2,3\}` form the element
`w∈(Ũ∘Ũ)(X)` — an **outer** unital-magma tree whose leaves are **inner** `U`-elements:
```
   inner leaves:  V_i = (single-leaf tree i),   E' = the inner unit  ∈ ŨX
   rigid block :  W_L = μ( V_0, μ(V_2, E') ),    W_R = μ( V_1, μ(V_3, E') )
   witness     :  w   = μ( W_L, W_R )  ∈ (Ũ∘Ũ)(X).
```
Here `E'` (the inner unit, an element of `ŨX`) appears as an **outer leaf**; at the *outer* level it
is an ordinary generator, **not** the outer unit `E`, so it is *not* absorbed. It is a label-free peg
that breaks the symmetry of its block.

By brute force over `S_4` (`scratch/2026-09-07-C2-witness.py`):

> **`\mathrm{Stab}_{(Ũ∘Ũ)X}(w) = ⟨(0\,1)(2\,3)⟩ ≅ C_2`**, and `w` has content `\{0,1,2,3\}`, each
> label once — so this group is a genuine orbit-type of the species component `(U∘U)[4]`.

*Why.* Within `W_L`, the leaf `V_0` sits at depth 1 and `V_2` at depth 2 (below the unit peg), so
`W_L` has **no** internal symmetry — it is **rigid** (this is the unit's doing: without `E'`, the
block would be a cherry `μ(V_0,V_2)`, symmetric). `W_R` is the equal rigid block on `\{1,3\}`. The only
symmetry of `w=μ(W_L,W_R)` is the outer swap `W_L↔W_R`, realised on labels by `(0\,1)(2\,3)` (which
sends `V_0↦V_1, V_2↦V_3`, hence `W_L↦W_R`). No single transposition survives: `(0\,1)` sends `W_L` to
`μ(V_1,μ(V_2,E'))∉\{W_L,W_R\}`. ∎

---

## §3. `⟨(0\,1)(2\,3)⟩` is not a block-fixing product

> **Lemma.** The fixed-point-free involution group `H=⟨(0\,1)(2\,3)⟩` is **not** a block-fixing
> product `∏_β\mathrm{Aut}(t_β)` of tree-groups on any partition of `\{0,1,2,3\}`.

*Proof.* A block-fixing product `∏_β\mathrm{Aut}(t_β)` acts within each block `β`; an element of it
restricts, on each block, to a member of that block's factor. So if it **contains** `(0\,1)(2\,3)`,
it contains the restrictions of `(0\,1)(2\,3)` to the blocks. The only partitions of `\{0,1,2,3\}`
that `(0\,1)(2\,3)` *preserves* are `\{\{0,1,2,3\}\}` and `\{\{0,1\},\{2,3\}\}`.
- On `\{\{0,1\},\{2,3\}\}` the restrictions are `(0\,1)` and `(2\,3)`, so the product contains
  `⟨(0\,1)⟩×⟨(2\,3)⟩=S_2×S_2` of order `4 ≠ 2`.
- On `\{\{0,1,2,3\}\}` the product is a single `4`-leaf tree-group; but those are `D_4` (order 8) and
  the caterpillar's `S_2` (a *single* transposition) — neither equals `⟨(0\,1)(2\,3)⟩`.

So no block-fixing product equals `H`; and conjugacy cannot help — brute force over all of `𝒫(4)` and
all `S_4`-conjugations confirms `H∉𝒫(4)` (`scratch/2026-09-07-C2-witness.py`). ∎

The moral: `(0\,1)(2\,3)` is a **correlated** double swap — it moves `0↔1` *only together with*
`2↔3`. A block-fixing product cannot correlate two blocks; it can only offer them **independently**
(`S_2×S_2`) or fuse them into one symmetric tree (`D_4`). The lone correlated swap is the
irreducibly second-order symmetry a rigid outer layer cannot manufacture.

---

## §4. Conclusion for `(★)` and THM 3

> **Theorem (U-corner).** For the free commutative unital magma monad `U`, `U∘U ≇ ⟦r⟧∘U` for **every**
> polynomial functor `⟦r⟧`. Therefore the essential image of `⟦−⟧_U` is not closed under composition;
> `U`-containers **do not** compose. `(★)` is answered **NO**.

*Proof.* If `U∘U≅⟦r⟧∘U` as functors, their species agree on every component, so
`(U∘U)[4]≅(⟦r⟧∘U)[4]` as `S_4`-sets and they realize the same stabilizer conjugacy classes. By the
Meta-theorem (§1) every stabilizer in `(⟦r⟧∘U)[4]` is a block-fixing product, hence in `𝒫(4)`. But
`w∈(U∘U)[4]` (content each-once, §2) has `\mathrm{Stab}(w)=⟨(0\,1)(2\,3)⟩∉𝒫(4)` (§3). Contradiction. ∎

> **THM 3 at the residual corner (updated).** `M`-containers compose ⟺ `M` polynomial. Necessity for
> analytic `M`: proved for `M∅=∅` (Theorem P), bounded wreath depth (Theorem S/S′), the
> symmetric-power/`𝕄` family — **and now for `U`**, the canonical `a_0>0 ∧ unbounded-wreath-depth`
> inhabitant. The corner that refuted Conjecture V's *vacuity* is closed on the **necessity** side. For
> `U`, THM 3 is an unconditional biconditional. The honest headline of `2026-09-06` — *"…proved for
> every analytic monad except `U`'s corner, where it is open"* — upgrades to *"…including `U`; the unit
> that inhabits the corner is exactly what breaks composition there."*

### Why the shallow `𝕄`-witness `D_4` fails for `U`, and the right axis

The `2026-09-05` witness `D_4=S_2≀S_2` (a single balanced `4`-tree) is a bona fide single-`U`-element
stabilizer, so it lies in `𝒫` and does **not** separate for `U`. One must instead exhibit a
stabilizer `𝒫` cannot reach at all. Two independent routes do it:

- **`C_2=⟨(0\,1)(2\,3)⟩` at `n=4` (this file, §2).** *Uses the unit.* A lone correlated swap of two
  **rigid** blocks. `𝒫` cannot produce a correlated swap of order `2`.
- **`(S_2×S_2)≀S_2` at `n=8` (order 32), unit-free.** `scratch/2026-09-07-sep-fast.py`: the structure
  `μ(μ(V_{01},μ(V_2,V_3)),\,μ(V_{45},μ(V_6,V_7)))` (all inner leaves, **no units**) has this
  stabilizer, which is support-indecomposable of order `32`, hence not a single tree-group
  (indecomposable `8`-leaf tree-groups have order `∈\{8,128\}`) and not a product — so `∉𝒫`. Because
  it uses **no units**, this witness lives in `Ã∘Ã` for `A=` the free commutative **non-unital** magma
  (`a_0=0`): **it re-proves Theorem P's conclusion for the free magma by the stabilizer method alone**,
  with no plethysm. Two witnesses, two regimes, one invariant.

**The correct invariant is the block-fixing vs block-swapping dichotomy of the stabilizer lattice, not
degree and not `a_0`.** `𝕄` (single-element stabilizers = Young) is separated by the depth-1 `D_4`;
`U` needs either the unit-built correlated swap (`n=4`) or a depth-2 wreath-of-a-product (`n=8`). The
depth of witness scales with the richness of `M`'s single-element stabilizers — the honest general
picture.

---

## §5. Generalization (the grant statement) and the open general residual

The Meta-theorem and Corollary hold for **any** monad `M`, reducing THM 3-necessity to a pure
permutation-group question:

> **(General test).** Does `M∘M` realize, on some species component, a point-stabilizer outside
> `𝒫_M :=` {block-fixing products of single-`M`-element stabilizers}? If yes, `M`-containers don't
> compose.

The `U` proof is the template. For a **non-flat analytic** `M`, the single-element stabilizers are the
automorphism groups of `A`'s constituents; `M∘M` can (i) build a **rigid** composite part when `M` has
a unit or a rigid constituent, and (ii) **swap** two equal such parts through the non-flat outer layer,
producing a correlated swap or wreath-of-a-product outside `𝒫_M`. I prove it here for the hardest
*named* case `U` and, unit-free, for the free magma — but a *uniform* "the swap always escapes `𝒫_M`"
theorem for every non-flat analytic `M` is the natural next PROVE target
(`theorem-general-stabilizer-necessity`).

**Crown (grant).** *Composition of `M`-containers is obstructed exactly by a symmetry that correlates
two equal sub-computations.* `⟦r⟧∘M` is rigid on parts (polynomial = free positions), so its
stabilizers are products of within-part symmetries; `M∘M` can swap two equal composite parts,
manufacturing a correlated (support-indecomposable) symmetry no product of within-part symmetries
equals. Polynomiality of the effect monad `=` flatness of its species `=` absence of any within-`M`
symmetry to correlate — the property that survives self-composition iff it was there to begin with.
The `U` result sharpens the codensity ⊥ polynomiality dichotomy: the unit, which makes `U` *codense-
adjacent* and inhabits the composition corner, is the very feature that forbids composition.

---

## Grades / registry

| Claim | Grade |
|---|---|
| Meta-theorem: stabilizers in `(⟦r⟧∘M)[m]` are block-fixing products | **proved** (elementary; "function fixed ⟺ pointwise fixed") |
| Corollary (composition test), per-component caveat | **proved** |
| `\mathrm{Stab}_{U∘U}(w)=⟨(0\,1)(2\,3)⟩=C_2`, `w∈(U∘U)[4]` each-once | **proved** (brute force over `S_4`) |
| `C_2∉𝒫(4)` (not a block-fixing product) | **proved** (order/partition argument + brute check) |
| **`(★)`: `U∘U≇⟦r⟧∘U` for all polynomial `⟦r⟧`** (THM 3 necessity holds at `U`) | **proved** |
| Unit-free `n=8` witness `(S_2×S_2)≀S_2∉𝒫`; reproves free-magma (`a_0=0`) case | **proved** (brute + support-indecomp. order argument) |
| General non-flat analytic residual closed by the mechanism | **conjecture** (template proved for `U` and the free magma) |

*Provenance note.* Lemma E, the analytic/species framework and Joyal full-faithfulness are the same
standard imports as `2026-09-05/06` (`extraction: agent-summary`); the new content — Meta-theorem, the
witnesses `w` (`n=4`) and `G` (`n=8`), and the `∉𝒫` proofs — is self-contained and computationally
verified this session. No cycle-index convergence is used anywhere (the reason the argument reaches
`a_0=1`).

## Verification artifacts
- `scratch/2026-09-07-C2-witness.py` — the `n=4` witness `w`: `\mathrm{Stab}(w)=⟨(0\,1)(2\,3)⟩`,
  content each-once; brute check `⟨(0\,1)(2\,3)⟩∉𝒫(4)`.
- `scratch/2026-09-07-sep-fast.py` — the unit-free `n=8` witness: order 32, orbits
  `\{0,1,4,5\},\{2,3,6,7\}`, support-indecomposable; `8`-leaf indecomposable tree-group orders
  `\{8,128\}` `⟹` `∉𝒫`.
- `scratch/2026-09-07-Hstar.py`, `-percomponent-confirm.py` — the each-label-once caveat: the witness
  groups *are* all-content intersections of overlapping-support `U`-trees, but those realizations reuse
  labels and live in higher species components, so they do not occur in `(⟦r⟧∘U)[m]`.
- `scratch/2026-09-07-UoU-vs-LoU.py`, `-U-stabilizer-search.py` — enumeration scaffolding; the
  all-`ℵ₀` multiplicity observation (every realised stabilizer of `U∘U` recurs `ℵ₀` times via
  outer unit-padding) that reduces the componentwise iso to matching stabilizer sets.
