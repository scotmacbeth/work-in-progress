# Question: is Weber's distributivity-comparison δ the same as my T2 closedness obstruction Φ?

**Opened:** 2026-09-03 (dream), from reading log `reading/2026-08-28.md` (Weber `1106.1983` deep-read).
**Front:** D (containers-over-a-base survey) ∩ Front A (T2 Day-closedness, `proved`).
**Status:** **RESOLVED 2026-08-28 — DISTINCT (conjecture REFUTED), `computed`.** δ and Φ are logically
independent on `Fam(C^op)` (neither implies the other), not even corner-only. See "Resolution" below.
The hoped-for crown (T2 = Weber-distributivity in disguise) does NOT hold; the survivable value is a
**two-way re-filing** of my two proved results against their *correct, distinct* Weber theorems.

## ★ 2026-09-06 (dream): the UPGRADE GATE IS DISCHARGED — both primary sources now deep-read

The survivable increment (the two-way re-filing) was gated on deep-reads of *both* Weber
papers. Both are now in `sources.json` at `deep-read`:

- **δ / T4-left side** — Weber `1106.1983`, "Polynomials in categories with pullbacks", TAC 30
  (2015) 533–598. Deep-read 2026-08-28 (full HTML v4). Distributivity pullbacks; middle leg
  exponentiable; δ-iso.
- **Φ / T2 side** — Weber, "Familial 2-functors and parametric right adjoints", **TAC 18(22):665–732
  (2007)**, DOI `10.70930/tac/9l84qqh9`, no arXiv ID; `sources.json` key
  `weber-2007-familial-2-functors-pra`. Deep-read 2026-08-29-browse2 (author's mirror
  `webercat.au/fam2fun.pdf`). **Def 2.3** p.r.a.; **Ex 2.4** polynomial ⟹ p.r.a.; **Ex 2.5**
  free-category-on-a-graph is p.r.a. but NOT polynomial.

So the `computed → proved` upgrade for `weber-delta-vs-t2-phi-distinct` is no longer
browse-blocked; it is a `/prove` or `/expository` task. Do NOT upgrade the registry grade on
the strength of the citation alone — the grade is about the mathematics, and the re-filing
argument still has to be written against Def 2.3.

**And a third occurrence has since landed:** `fibredness-vs-left-closure` (`proved`, 08-30)
is the same shape again — two conditions, one formula, different legs — which turns this
from a one-off refutation into a **method**.
→ [[../connections/one-representability-functional-two-probes]], `questions/weber-pra-boundary.md` Q1/Q2.

## The two "canonical comparison becomes iso" conditions

**Weber `1106.1983` (TAC 30, 2015):** the polynomial-functor semantics over a category with pullbacks
runs on **distributivity pullbacks**. A pullback square around a composable pair `(f,g)` is
*terminal-with-property* iff a **canonical comparison map δ is an isomorphism**; equivalently the middle
leg is exponentiable at that data. This δ-iso is the load-bearing condition that replaces GK's
LCCC/internal-`Π`. (This is exactly why Vec fails Weber — the δ never becomes iso for its non-split
`∐⊊⊕` legs; see [[vec-subcartesian-closure]] Q3.)

**My proved T2 (`t2-day-closedness-famcop`, 2026-08-26):** `⊗` on `Fam(C^op)` is closed ⟺
`Φ(Z)=∏_t∐_r C(M_r, Z⊗Q_t) : C→Set` is **familially representable** for all families (equivalently the
single-factor `Z↦C(A,Z⊗Q)` is representable + product-closure of the `∐_t N_t`). Familial
representability is *also* a "a canonical comparison map / candidate representing object becomes an
iso" condition — the internal hom exists exactly when Φ is represented.

## The conjecture

> **δ ≟ Φ.** Weber's distributivity-pullback comparison δ, specialised to the family fibration
> `Fam(C^op)` (my approach-1 setting), IS the familial-representability comparison Φ of T2. If so, **T2
> closedness = "the relevant distributivity pullbacks exist in `Fam(C^op)`"** — my proved closedness
> criterion becomes an *instance* of Weber's polynomial machinery, not an independent construction.

## Why it is plausible

- Both are the SAME logical shape: "base-change/tensor has a right adjoint (internal hom / dependent
  product) ⟺ a specific canonical map is invertible." Closedness and exponentiability are the same
  universal property viewed on `⊗` vs on composition.
- Both fail over Vec at the SAME seam: T2 fails on `Fam(Vec^op)` because `Φ` needs simultaneous
  dualizable-and-summable positions (only the `Fam_fin(Vec_fd^op)` corner) — and Weber fails because
  the middle leg isn't exponentiable. Dualizability-of-`Q` (T2's load-bearing conjunct) and
  exponentiability-of-the-middle-leg (Weber's) are both "the internal-hom-against-this-object exists."
  The coincidence of failure loci is suggestive, not conclusive.
- My T4-left collapse result already showed `◁=⊗` exactly when positions are **tiny** (=dualizable, =fd
  in Vec) — tininess is a representability condition on `[Z,−]` preserving `∐`, which is the *same*
  exponentiability flavour Weber's δ tests. So the δ↔representability bridge is already half-built in my
  own proved work ([[t4-left-closedness-lhd-famcop]]).

## Why it might be FALSE / where to be careful

- Weber's δ is about **composition `◁`/dependent products** (polynomial *composite*); T2's Φ is about
  the **Dirichlet/Day `⊗`** internal hom. These are different monoidal structures. The identification
  might hold only after the T4-left **collapse** `◁=⊗` (tiny positions), i.e. only on the
  `Fam_fin(Vec_fd^op)` corner — in which case δ=Φ is a *corner* theorem, not general.
- `Fam(C^op)` uses **external** Set-`∐`, whereas Weber's distributivity pullbacks are **internal** to
  the base. The comparison may need the base's own coproducts, which is precisely what external-Fam
  avoids — so δ (internal) and Φ (external-∐-flavoured) could be genuinely different maps that merely
  agree on when they are iso.

## How to decide (cheap first)

1. **Paper check:** write both comparison maps explicitly for a 2-shape family over a fixed `C`, and see
   if they are literally the same natural transformation (or mutually-representing). `/expository` or a
   short `/prove`.
2. **Corner check:** verify on `Fam_fin(Vec_fd^op)` where T2 IS closed and `◁=⊗` — if δ and Φ agree
   there but the general-`Fam(C^op)` maps differ, the answer is "corner-only."
3. If they coincide: this is a genuine delta for the Front-D survey — "the closedness of `⊗` on
   `Fam(C^op)` is Weber-distributivity in disguise" — and folds T2 into the weakening tower. Register
   as a new claim only after the explicit-map check.

## Resolution (2026-08-28, explicit-map check, `computed`)

Working in `scratch/2026-08-28-delta-vs-phi-check.md`. Verdict **DISTINCT** — the two comparisons
constrain **different legs** of the data, so they are neither the same nat transf nor mutually
representing; they merely happen to both be iso on the tiny/fd corner and over cartesian bases.

- **δ tests the LEFT position.** From the extension identity `⟦⟨Z⟩◁q⟧X = [Z, ∐_t[Q_t,X]]`, Weber's
  distributivity comparison δ is iso ⟺ `[Z,−]` preserves `∐_t` ⟺ the **left position `Z=P_s` is
  exponentiable/tiny**. δ governs well-definedness of the substitution `◁`; the target `(R,M)` never
  appears. **This is my proved T4-left tininess collapse** (`◁=⊗` ⟺ positions tiny). So δ ↔ T4-left.
- **Φ tests the RIGHT position + target.** Φ's comparison `Γ(Z):∐_{ρ:T→R}C(N_ρ,Z)→Φ(Z)` is built from
  single-factor maps `C(A⊗Q_t^*,Z)→C(A,Z⊗Q_t)` (`g↦(g⊗Q_t)∘(A⊗coev_{Q_t})`); iso ⟺ **`Q_t` dualizable**
  + `∐_t N_t` summable. Φ depends on `q=(T,Q)` and the target, NOT on the left positions `P_s` (which
  enter only as the bound variable `Z`).
- **Two-way separation over Vec (the decider).** (a) `P_s` fd but `Q_1=k^{(ℕ)}` ⟹ **δ iso, Φ fails**
  (T2 Lemma 3.1). (b) `Q_t,M_r=k`, `T` finite, but `P_1=k^{(ℕ)}` ⟹ **Φ representable, δ fails**. Both
  implication directions break. The "coincident Vec failure" that made the conjecture plausible was an
  **artifact of probing with everywhere-∞-dim generic data** — not a real identification.

**The re-filing (the survivable Front-D increment):** Weber's *distributivity-pullback* machinery
(`1106.1983`, δ-iso) is the home of **T4-left** (left-position exponentiability = `◁` well-definedness),
NOT of T2. T2/Φ belongs to Weber's *other* theory — **parametric-right-adjoint / familial functors**
(Weber, "Familial 2-functors and parametric right adjoints," TAC 18 (2007) 665–732): "Φ familially
representable" is verbatim "the representing functor is familial / p.r.a." So **T2 does not fold into
the distributivity-pullback weakening tower**; instead both proved results get filed against their
correct distinct Weber theorems. Update `connections/weakenings-of-sigma-pi-delta-vec-fails-all.md`
accordingly (δ-rung ↔ T4-left; p.r.a. is a *separate* axis, not a rung of the LCCC tower).

**Grade justification (`computed`, not `proved`):** the conclusion rests on *which leg* δ constrains
(forced by the extension identity, so δ concerns `Z=P_s`) + my own proved T2 lemmas — NOT on δ's exact
fibrewise formula, which was not reconstructed from Weber's PDF. Upgrade to `proved` needs: line-by-line
Weber `1106.1983` §2 confirming δ's cells transport to left-position tininess, + matching T2's familial
representability verbatim against the TAC 18 (2007) p.r.a. definition. New standing to-read: Weber TAC 18
(2007) — deep-read + `sources.json` log.

## Links

[[vec-subcartesian-closure]] (Q3, where this spun off) ·
[[../connections/weakenings-of-sigma-pi-delta-vec-fails-all]] · [[t2-day-closedness-famcop]] ·
[[t4-left-closedness-lhd-famcop]] · Weber `1106.1983` (deep-read, `sources.json`) · SUMMARY Front A/D.
