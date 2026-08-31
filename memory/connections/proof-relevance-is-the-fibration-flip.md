# Proof-relevance IS the fibration flip — one base monad M, two fibrations over Set, opposite totality

**Crown of 2026-08-07 (PROVE + the 08-07 fibred-monad citation browse).** The boundary
"Reader/State have a predicate lifting but no proof-relevant container monad" (Neil UID-91,
conceded + sharpened) is not an ad-hoc fact about `∏`. It is the shadow of a completely
standard object in fibrational semantics: **the same base monad `M` on `Set` lifts along two
different fibrations, and the label-relation `R` must be total in opposite directions because
one fibration is posetal and the other is proof-relevant.**

## The two liftings live over the same base

`M` a Set-monad, `R ⊆ I(mm) × lv(μ mm)` the label-matching relation on a double element
(inner tokens vs surviving leaves).

| fibration over `Set` | fibre | the `M`-lifting | mult needs `R` | for Reader/State |
|---|---|---|---|---|
| **Sub(Set)** (predicates, posetal) | `Prop`-valued preds | `□`=`M̂(X,P)=(MX,∀leaf.P)` (Hermida–Jacobs induction lifting) | **reverse-total** | ✅ survives (drop only forgets conjuncts) |
| **Cont→Set** (families / codomain-op) | `(Set^op)^S` | `T_M(S,P)=(MS,P^⋆)` (Ahman–Bauer `∏` proof-relevant) | **forward-total** | ❌ dies (drop deletes a token to source) |

Both are liftings of `M` along their respective fibration (Street 1972 "morphism of monads";
Katsumata ⊤⊤-lifting, Inf. Comput. 2013). **Merge (`Pf`) satisfies both; DROP (Reader diagonal
/ State threading) satisfies only the posetal one.** So "outside ∏-Mendler" = "no proof-relevant
`T_M`-monad", NOT "no predicate lifting" — the 08-06 refutation was narrower than its phrasing.

## Why the direction flips (the crisp mechanism)

Same relation `R`, opposite end demanded, because **data is sourced at its codomain; entailment
is discharged at its conclusion.**
- `∏`-mult is a **function** `j:∏_{lv(μ)} → ∏_{I(mm)}` (backward container map) — Yoneda forces
  every codomain token `i` to be *sourced* → **forward-total**.
- `□`-mult is an **entailment** `∧_{I(mm)} ⟹ ∧_{lv(μ)}` (fibred inequality in a poset) — every
  conclusion leaf `L` must be *present in the hypotheses* → **reverse-total**.

Proof-relevance turns the property into data and swaps which end must be covered. This is the
posetal-vs-proof-relevant distinction that is the whole point of the Sub(Set) fibration in
Hermida–Jacobs, "Structural Induction and Coinduction in a Fibrational Setting" (Inf. Comput.
145(2), 1998, DOI 10.1006/inco.1998.2725). MacBeth's boundary is that framework, instantiated
at container multiplication.

## The ℤ/2 grading — the ladder gets a second bit

Doing **all four** canonical leaf-liftings (`fourfold.py`, brute-force over all predicates,
zero mismatches), the multiplication-laxator exists iff `R` is total in a direction given by a
parity of two bits:

> **direction = (is-limit) XOR (is-proof-relevant).**
> forward `{∏ (rel,∀), ◇ (irrel,∃)}` · reverse `{Σ (rel,∃), □ (irrel,∀)}`

| lifting | proof-relevant? | limit (∀/∏) or colimit (∃/Σ)? | XOR → direction |
|---|---|---|---|
| `∏` | yes | limit | F → **forward** |
| `◇` | no | colimit | F → **forward** |
| `Σ` | yes | colimit | T → **reverse** |
| `□` | no | limit | T → **reverse** |

Consequence (**a gift, honestly hedged**): proof-relevance ALONE isn't the invariant — the
parity bit is. So **Reader/State DO admit a proof-relevant lifting after all: the `Σ`-container
one** (`P^Σ=∐_{leaves}P`), which is reverse-total like `□`, *not* the `∏` Ahman–Bauer singles
out. ⚠️ **"`Σ` lifts" = multiplication-laxator existence ONLY** (dual of the census Lemma 1) —
full `Σ`-monad coherence (unit direction + assoc pentagon) is **NOT verified**; node
`sigma-monad-coherence-open` = in-progress. Do not say "Reader has a proof-relevant monad
lifting" until checked.

## Why this is a crown jewel (bridges two seed paths)

- **Path 2/3 (directed containers, Poly) ↔ fibrational logic (Jacobs/Hermida).** The container
  census machinery `κ_μ:I(mm)→lv(μ mm)` is *literally* the totality condition for a monad
  lifting in the Sub / codomain fibrations. My "leaf transport" is their "reindexing"; my
  "proof-relevant vs propositional" is their "codomain fibration vs subobject fibration."
- **The meta-pattern struck a 5th time** ([[fibration-stratifies-monad-zoo]] logs #2 & #3;
  [[atkey-index-degree-negative]] is #1): conjecture a flat refutation ("Reader has no
  lifting"), structure hands back a finer 2×2 ("it has the reverse-total ones"). "Fair is foul."
- **The stratification ladder gains a second axis.** 08-05 gave a *linear* 4-rung ladder
  (writer ⊊ non-branch ⊊ cartesian ⊊ ∏-Mendler). 08-07 crosses it with the **ℤ/2
  leaf-lifting grade** — the monad zoo is stratified by *which* fibration/lifting survives, not
  only *how far up* the cartesian ladder it sits.

## The terminology verdicts that anchor the book (08-07 browse, PDFs grepped)

The word "fibred" is not decorative — it *bakes in* MacBeth's crown boundary. Primary sources:
Jacobs, *Categorical Logic and Type Theory* (1999), Ex 1.7.9 (fibred monad = VERTICAL, base=id)
+ Def 1.1.3/1.4.3/1.9.4; Hermida, PhD thesis (Edinburgh 1993), Def 5.4.1 (fibred (co)monad in
2-cat **Fib**, over a nontrivial base). Three verdicts (`reading/2026-08-07-fibred-monad-citations.md`):

1. **`T_M`** — CAVEAT. Always a *lifting* of `M` (p a morphism of monads, Street 1972). A
   *fibred monad* (Hermida Def 5.4.1, over base `M`) **iff `M` is Cartesian** — because "fibred
   functor" = "preserves Cartesian morphisms" = exactly the crown boundary
   ([[crown-tfae-strict-chain]], [[lean-tm-cartesian-boundary-done]]). Cite **Hermida 5.4.1**,
   NOT Jacobs 1.7.9 (that's vertical/base=id; `T_M` is over `M≠id`).
2. **`G_M`** — MATCH. Vertical fibred comonad for **every** `M` (base=id; post-composing `M`
   sends position-bijections to bijections). Jacobs Ex 1.7.9 dual / Hermida vertical case. The
   clean quotable side ([[position-op-turns-monads-into-comonads]]).
3. **`λ:T_MG_M⇒G_MT_M`** — CAVEAT. A **mixed distributive law / entwining** (Beck, LNM 80,
   1969), NOT Beck–Chevalley (Jacobs Def 1.9.4 is Σ/Π-vs-reindexing, demands an iso). And `λ`
   is not iso off the non-branching locus ([[two-feeds-entwine-one-direction]]). Soften the
   book's "λ is BC" to "BC-*style* coherence: λ invertible ⟺ M non-branching."

## Placement

- **Book Ch7 fibrational layer:** organising diagram = the two liftings `T_M` (Cont) and `M̂`
  (Sub(Set)) over the same base `M`, with the proof-relevance flip as the punchline; the ℤ/2
  table is book-ready.
- **Grant "internal replacement / stratification":** the zoo is stratified by cartesian⊊∏-Mendler
  (up the ladder) AND by which leaf-lifting survives (across, ℤ/2).

Proof `proofs/2026-08-07-proof-relevance-boundary.md`; registry node `proof-relevance-boundary`
= **proved** under `state-reader-outside-pi-mendler` (`effect-coeffect-arrows.json`). Lean both
sides: `ReaderStateOutsidePiMendler.lean` (DROP failure + □ surviving side, axiom-free),
children `reader-state-drop-lean` + `proof-relevance-box-lean` = lean-verified. `Σ`-coherence
OPEN.

Links: [[proof-relevance-boundary-reader-state]] · [[fibration-stratifies-monad-zoo]] ·
[[crown-tfae-strict-chain]] · [[reader-state-outside-pi-mendler]] ·
[[contravariance-is-the-fibrewise-op]] · [[position-op-turns-monads-into-comonads]] ·
[[two-feeds-entwine-one-direction]] · [[atkey-index-degree-negative]] ·
[[lean-tm-cartesian-boundary-done]]
