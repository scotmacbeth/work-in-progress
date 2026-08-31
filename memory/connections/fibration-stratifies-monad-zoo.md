# The fibration STRATIFIES the monad zoo — it does not collapse it

**Crown of 2026-08-05 (heartbeat-2/3/4).** Neil's UID-89 fibrational steer hoped the
fibration `p:Cont→Set` would **weld** three cartesianness conditions onto the already-proved
arrow core into one grand equivalence (a "crown TFAE"). It does not. The welding **fails**,
and the failure is the result: the fibration resolves the effect–coeffect monad zoo into a
**strict 4-level refinement ladder**, each rung a checkable monad property.

## The conjectured collapse (FALSE)

> (1) `T_M` preserves cartesian morphisms ⟺ (2) `M` cartesian ⟺ (3) `λ:T_MG_M⇒G_MT_M`
> invertible (strict Beck–Chevalley) ⟺ (4) reverse `κ:G_MT_M⇒T_MG_M` exists ⟺ (5) `M`
> non-branching.

Only **(4)⟺(5)** holds (the arrow core, proved earlier — [[effect-coeffect-arrows-first-strength]]).
And **(1)⟺(2)** holds *within ∏-Mendler* (Thm 1). The rest are strict inclusions.

## The ladder (narrowest → widest)

```
(3) λ-invertible / strict-BC          ⊊  (5)=(4) non-branching           ⊊  (2)=(1) cartesian monad        ⊊  polynomial / ∏-Mendler
    = PURE WRITER   A×(−)                 = writer+exception E+A×(−)          = T_M preserves cart. morphisms    = T_M even exists (has support)
    Id, Writer                            +Maybe, Exception                  +List                              +Pf, +Bag
```

**MacBeth-verified splitters** (each demolishes one hoped ⟹):
- **List** (free-monoid monad): **cartesian** (no leaf-merge in `fmap` or `μ=concat`) yet
  **branching** (arity ℕ) ⟹ **(2)⇏(5)**. Cartesian ≠ non-branching.
- **Maybe** `X+1`: **non-branching** but `λ` **not** invertible — at the nullary shape,
  `str:M(1)→1=(1+1)→1` is not iso ⟹ **(5)⇏(3)**. Strict BC forces `M1≅1` ⟹ pure writer
  (arity ≡1, no nullary shape).
- **Pf** (non-cartesian μ=∪, merges leaves) and **Reader/State** (polynomial functor,
  non-cartesian μ, no `i_P`) and **Bag** (leaf-cartesian but *analytic*, fails a connected
  pullback) split the top rung — Reader from the "μ-merges" side, Bag from the
  "leaf-cartesian-but-not-polynomial" side. → [[crown-tfae-strict-chain]] for the full
  gap-closure incl. Lemma 1.4′ label-rigidity rescue.

## Why this REFINES the 08-05 00:02 "three faces" picture

The earlier dream ([[arr-profunctor-free-category-costs-branching]]) said the entwined
structure has **three faces**: profunctor (all `M`) / bialgebra `λ` (all `M`) / arrow `κ`
(non-branching). Tonight sharpens this: **"`λ` exists" ≠ "`λ` invertible."** `λ` exists for
all `M` (oplax BC mate), but `λ` **invertible** is a strictly *narrower* rung than `κ`-composition —
it is the pure-writer floor. So the honest count is **four rungs, not three coincident faces**:

| rung | condition | holds for | face |
|---|---|---|---|
| profunctor exists | none | all `M` | data |
| `λ` exists (oplax BC mate) | none | all `M` | bialgebra/Plotkin–Turi |
| `κ` composes (arrow category) | non-branching `E+A×(−)` | Maybe, Writer, Exc | Freyd |
| `λ` invertible (strict BC) | pure writer `A×(−)` | Writer, Id | **new floor** |

The fibration is exactly the lens that makes the rungs *visible* — each threshold is a
cartesianness/BC-strength condition (`str` iso? backward map bijective? `μ` merges leaves?),
which is a fibrewise statement you cannot see without `p:Cont→Set`.

## 2026-08-07 UPDATE — the ladder gains a SECOND axis (ℤ/2 leaf-grade)

The 08-05 ladder is *linear* (writer ⊊ non-branch ⊊ cartesian ⊊ ∏-Mendler). 08-07 crosses it
with a second, orthogonal grading. The same base `M` lifts along **two fibrations over Set** —
Sub(Set) (posetal → `□`) and Cont→Set (proof-relevant → `T_M`) — and the mult-laxator's totality
requirement flips direction by a **ℤ/2 parity**: `direction = (is-limit) XOR (is-proof-relevant)`
(`{∏,◇}`→forward, `{Σ,□}`→reverse; `fourfold.py`, zero mismatches). So the zoo is stratified
**both** up the cartesian ladder AND across which leaf-lifting survives. Reader/State DROP off the
`∏` (forward) rung but SIT on the `□`/`Σ` (reverse) rung — they *have* a predicate lifting, just
not the proof-relevant container monad. Full development: **[[proof-relevance-is-the-fibration-flip]]**.
(Σ-monad coherence still OPEN — laxator only.)

## 2026-08-08 UPDATE — the Σ leg now has its own lift-criterion (◁-monoid), completing the codomain side

08-07 left the codomain/`Cont` fibration with a known **∏** criterion but only a *laxator* for **Σ**.
08-08 closes it: **`T^Σ_M = M ◁ −`** (left ◁-product), so the Σ-lifting is a monad on `Cont` **iff
`M` is a ◁-monoid = a container monad** (`reverse-total ⟹ Σ-monad` REFUTED by Bag: reverse-total but
*analytic*, not a container). Both legs of the non-thin (proof-relevant) side now read crisply:

| leaf-lifting | monad on `Cont` ⟺ | totality |
|---|---|---|
| `∏` (`T_M`, Ahman–Bauer) | `M` **cartesian** | forward |
| `Σ` (`T^Σ_M = M◁−`) | `M` a **◁-monoid / container monad** | reverse |

This welds the surviving Σ side onto the directed-container spine (DCont = ◁-*comonoids*; container
monads = ◁-*monoids*), and recycles the July "polynomial not analytic" discriminator
([[polynomiality-is-provenance-is-coherence]]): reverse-total = analytic shadow, ◁-monoid = polynomial
coherence. Full development: **[[sigma-lifting-is-triangle-monoid]]** (6th meta-pattern instance).

## 2026-08-07 — the terminology verdicts (the word "fibred" bakes in the boundary)

Neil asked for Jacobs/Hermida citations + a skeptical match check (PDFs grepped,
`reading/2026-08-07-fibred-monad-citations.md`). Result: "fibred functor" ≡ "preserves Cartesian
morphisms", so:
- **`T_M`** = a *lifting* of `M` always (Street 1972, morphism of monads); a **fibred monad**
  (Hermida, PhD Edinburgh 1993, **Def 5.4.1**, over base `M`) **iff `M` Cartesian** — the crown
  boundary IS the content of "fibred". Cite Hermida 5.4.1, **not** Jacobs 1999 Ex 1.7.9 (that's
  vertical/base=id).
- **`G_M`** = **vertical fibred comonad ∀`M`** (Jacobs Ex 1.7.9 dual / Hermida vertical case) —
  clean, unconditional.
- **`λ`** = **mixed distributive law / entwining** (Beck, LNM 80, 1969), **NOT** Beck–Chevalley
  (Jacobs Def 1.9.4 = Σ/Π-vs-reindexing iso); and not iso off non-branching. Soften book's "λ is
  BC" → "λ invertible ⟺ M non-branching" (BC-*style*).

## What survives intact (the G_M side)

**`G_M` preserves cartesian morphisms for EVERY `M`** — the vertical fibred comonad fact,
now **Lean-certified** (`FibredTransfer.lean`, `onMor_cartesian`, `[Quot.sound]`-only, NO
cartesian-`M` hypothesis). Neil's fibred intuition is **correct on the `G_M`/positions side**;
the error was pushing it onto the **`T_M`/shapes side**, where cartesian-ness of `M` genuinely
bites. The two Lean certs bracket the crown:
- `FibredTransfer.lean` — `G_M` cartesian ∀`M` (positive, hypothesis-free).
- `TMCartesianBoundary.lean` — `T_Maybe` preserves cartesian ∀φ (Maybe's leaf map always
  bijective); `T_Pf` **fails** (merging `u:{a,a'}→{c}` ⟹ product map = diagonal Bool→Bool²,
  injective-not-surjective). Machine-checks (1)⟺(2) at the Maybe/Pf edge. →
  [[lean-tm-cartesian-boundary-done]].

## The meta-pattern (why "fair is foul" earns its keep)

This is the **second** time a hoped grand collapse became a more-informative stratification.
On 07-31 the "Atkey index carries a grading by branching degree" conjecture also died — but
into a **Boolean** dichotomy (index isn't graded; collapse-to-plain-Freyd = `M=Id` only,
[[atkey-index-degree-negative]]). Here the collapse dies into a **4-level chain**. Recurring
shape: *MacBeth conjectures an equivalence; the honest structure is a refinement ladder.* The
refutation is worth more than the equivalence would have been — it hands the grant a
**computable ladder of composition strength** (each rung a decidable monad property) in place
of one binary gate. Retracted from book+grant: the slogan "containers preserve cartesian
morphisms = M non-branching = strict BC" (conflated three rungs). Installed instead: the
stratification teachbox.

## Grant / book placement

- **Book** Monads-and-Comonads chapter: the payoff teachbox was rewritten from the false
  triple-equality to the ladder (08-05 write, honesty repair — the
  [[the-summary-is-what-gets-audited]] failure mode recurring: compressing "∏-Mendler" to
  "polynomial" for grant prose *manufactured* a false claim).
- **Grant Path-5**: "composition strength is stratified, not binary" — a computable refinement
  ladder over the effect–coeffect axis, complementing the directed axis `[ω]∈H²` and the
  state/Workers axis (no obstruction). → [[three-modes-of-composition]].

Proof `proofs/2026-08-05-cartesian-preservation-nonbranching.md` + `-crown-gap-closure.md`;
harness `scratch/fibrational-crown/`. Registry `effect-coeffect-arrows.json` node
`crown-tfae-splits-strict-chain` = **proved** (children `crown-boundary-table`,
`lambda-inv-implies-nonbranching-general` proved).

Links: [[crown-tfae-strict-chain]] · [[arr-profunctor-free-category-costs-branching]] ·
[[atkey-index-degree-negative]] · [[affine-classification-writer-exceptions]] ·
[[branching-obstruction-is-atkeys-index]] · [[lean-tm-cartesian-boundary-done]] ·
[[neil-steer-2026-08-05-fibrational-orestis]] · [[three-modes-of-composition]]
