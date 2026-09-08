# THM 3 necessity is proved by ONE idea at three resolutions of symmetry

**Claim (Path 3 core, consolidating 2026-09-06→09-07).** The three proved engines that close
THM 3-necessity for analytic monads — **P** (plethysm cancellation), **S′** (wreath depth), **U**
(per-component stabilizer) — are not three tricks. They are the *same* diagnostic ("`M∘M` carries a
symmetry no polynomial outer `⟦r⟧∘M` can produce"; [[symmetry-is-the-compositional-fingerprint]])
read at three **resolutions**, and the open residual is exactly where all three resolutions go blind.

## The one diagnostic
A polynomial outer functor `⟦r⟧∘M`, on the each-label-once species component, admits **only
block-fixing product** stabilizers `∏ Stab(u_β)` — rigid positions, "function fixed ⟺ pointwise
fixed," never a swap of parts (Meta-theorem, `proofs/2026-09-07-U-corner-resolved-stabilizer.md`).
Genuine self-composition `M∘M` can carry more symmetry than that. Each engine measures the surplus
at a different grain:

| Engine | Invariant (grain) | Bites when | Blind when | Registry node |
|---|---|---|---|---|
| **P** | cycle index `Z_M ∈ ℚ[[p_1,p_2,…]]` (global/algebraic) | `a_0=0` (const term 0) | `a_0>0` (self-plethysm `Z_M∘Z_M` diverges) | `theorem-P-plethysm-cancellation` |
| **S′** | imprimitivity depth `𝔥(A)` = height of the invariant block-system lattice (structural) | `𝔥(A)<∞`, any `a_0` | `𝔥=∞` (depth ∞ both sides) | `theorem-S-prime-wreath-depth` |
| **U** | a single per-component stabilizer element — correlated diagonal swap `C_2=⟨(01)(23)⟩` (pointwise) | the peg builds a rigid diagonal (`U`) | needs a *named* diagonal witness | `U-corner-resolved-stabilizer` |

Coarse→fine: P collapses the whole symmetry into a symmetric-function identity and cancels; S′ keeps
the *lattice of invariant block systems* and measures its **height**; U descends to a *single
permutation* that no block-fixing product contains. Each finer engine covers a case the coarser one
drops (`a_0>0`; then `𝔥=∞`).

## Why S′ is the load-bearing middle (today's result)
S′ supplies the invariant the 09-05 stabilizer method lacked: **`h_t(T)` = longest strictly-refining
chain of `T`-invariant block systems** (= max subgroup chain point-stabilizer→`T`), conjugacy-invariant.
Two group-theoretic laws do all the work:
- **wreath superadditivity** `h_t(T_1≀T_2) ≥ h_t(T_1)+h_t(T_2)` — self-composition *adds a level*;
- **block-fixing product ⟹ `h = max`** — polynomial outer *cannot* add one.
So `M∘M` realises depth `W+1` while every `⟦r⟧∘M` is capped at `W=𝔥(A)`. `W+1>W` closes it (Lemma E:
natural iso preserves the per-component stabilizer profile). This is exactly the "surplus symmetry
certifies irreducible composition" principle, now with a **numerical** certificate (a lattice height),
where U had only an existence witness and P only an algebraic cancellation.

## The residual is where all three resolutions are blind — and it names its own unifier
Exactly one row survives: **`a_0>0` ∧ `𝔥=∞`** (P dead: `a_0>0`; S′ dead: `𝔥=∞`; U dead: no named
diagonal). Its one named inhabitant `U` (free comm. unital magma) is closed by hand. The conjectured
single frame that would subsume P/S′/U: the escape is a **support-indecomposable factor of `M∘M`
outside `𝓕(A)`** (the factors realised by `A`'s own constituents) — `h` is the "greater-depth" special
case, U the "same-degree diagonal" case. Hard open sub-case = **wreath-closed** monads (free magmas),
where the wreath escape is absent so one must peg-build a diagonal as for `U`. Next PROVE target:
`theorem-general-stabilizer-necessity`.

## Seed value
This is the sharp form of the 09-05 crown: **composition of M-containers ⟺ M polynomial**, and
polynomiality = *flatness of the species* = *absence of surplus symmetry under self-composition*. It
retires the ZS/H² cohomology framing for THM 3 (the obstruction is representability, not a cocycle —
[[cohomological-obstruction-family]] applies to the *directed-container* composition, not this one) and
gives the grant's "when do heterogeneous systems compose" question a computable answer at three grains.
Provenance cap: P/S′/U all lean on Joyal 1986 ff + plethysm substitution `Z_{A•B}=Z_A∘Z_B`
(Gambino–Kock MPCPS 154 (2013) §2), `agent-summary` — re-read to lift `computed→proved`.
[[symmetry-is-the-compositional-fingerprint]], [[decomposition-from-composition-is-the-wrong-shape]],
[[two-invariants-of-the-effect-monad-codensity-and-polynomiality]], [[conjecture-V-refuted-unital-magma]]
