# Proof-relevance boundary — PROVED (Reader/State: □ lifts, T_M doesn't) + a ℤ/2 grading fell out

**MacBeth, 2026-08-07 PROVE session.** Answers Neil's UID-91.
Proof: `proofs/2026-08-07-proof-relevance-boundary.md`. Registry node
`proof-relevance-boundary` = **proved** under `state-reader-outside-pi-mendler`
(`effect-coeffect-arrows.json`; trustcheck clean).

## The result (all three PROVE.md parts, general — all E, all S, all leaf-supported M)

Let `R ⊆ I(mm) × lv(μ mm)` be the label-matching relation on a double element:
inner tokens vs surviving leaves, `(i,L)∈R ⟺ lab(i)=lab(L)`.

- **Part 1 (recap, proved):** the Ahman–Bauer **proof-relevant** `∏`-lifting `T_M` is a container
  monad ⟺ `R` **forward-total** (every inner token covered) — Yoneda, from the census.
- **Part 2 (NEW, the real work):** the **proof-irrelevant** `□`-predicate lifting
  `M̂(X,P)=(MX, ∀leaf.P)` on `Sub(Set)` is a genuine **monad lifting** ⟺ `R` **reverse-total**
  (every surviving leaf covered). Proof: `□=M(−)` direct image (functor lifting, Hermida–Jacobs);
  unit always lifts; multiplication condition `∀P.□□P(mm)⟹□P(μ mm)` ⟺ reverse-total by a **single
  test predicate** `P₀=Lab(I(mm))`. No `decide`, fully general.
- **Part 3 (proved):** Reader (μ=diagonal) and State (μ=threading) are **reverse-total for every
  mm** — each surviving leaf *is* a token (the diagonal `(e,e)` / the threaded `(s₀,h(s₀))`) — but
  **forward fails** (census witness). So **they have the □ predicate monad lifting but not the
  proof-relevant `T_M`-monad. The boundary is proof-relevance.**

## Why the direction flips (the crisp bit)

Same relation `R`, opposite end demanded, because **data is sourced at its codomain; entailment is
discharged at its conclusion.** `∏`'s multiplication is a *function* `j:∏_{lv(μ)}→∏_{I(mm)}` (a
backward container map) — Yoneda forces every codomain token `i` to be sourced → forward. `□`'s
multiplication is an *entailment* `∧_{I(mm)}⟹∧_{lv(μ)}` (a fibred inequality) — every conclusion
leaf `L` must be present in the hypotheses → reverse. Proof-relevance turns the property into data
and swaps which end must be covered. This is the Ch7 fibrational-layer punchline.

## The unexpected gift: a ℤ/2 grading (bonus, §4.3)

Doing all four canonical leaf-liftings, the monad-multiplication exists iff `R` is total in a
direction given by a **parity of two bits**:

> **direction = (is-limit) XOR (is-proof-relevant).**
> `{∏ (relevant ∀), ◇ (irrel ∃)}` → **forward**; `{Σ (relevant ∃), □ (irrel ∀)}` → **reverse**.

Verified brute-force over all predicates (`fourfold.py`): `□⟺reverse`, `◇⟺forward`, zero
mismatches. So proof-relevance is **not** the whole story — the finer invariant is the parity bit,
and it means **Reader/State DO admit a proof-relevant lifting after all: the `Σ`-container one**
(`P^Σ=∐_{leaves}P`), not the `∏` Ahman–Bauer singles out. "Fair is foul" — the meta-pattern struck
a fifth time: a flat refutation handed back a finer 2×2 structure.

## Honesty flags (do not overclaim)

- "`Σ` lifts" is **only multiplication-laxator existence** (dual of Lemma 1) — computed/peer-claimed
  level. The full `Σ`-monad coherence (unit direction + assoc pentagon) is **NOT verified**. Node
  `sigma-monad-coherence-open` = `in-progress`. Do **not** say "Reader has a proof-relevant monad
  lifting" until this is checked — a natural next PROVE + Lean target.
- Whether *every* proof-relevant lifting is `∏`/`Σ`/mixed (parity dichotomy exhaustive?) is open.

## For the book / grant
- Ch7 fibrational layer: the two liftings `T_M` (Cont) and `M̂` (Sub(Set)) over the same base `M`,
  with the proof-relevance flip as the organising diagram.
- Grant "internal replacement / stratification": the monad zoo is stratified not just by
  cartesian⊊∏-Mendler but by *which* leaf-lifting survives, graded by the ℤ/2 parity.

## Next triggers I'd suggest
- **LEAN**: `reader_box_unit` / `reader_box_mult` (the □ monad lifting for Reader₂) — certifies the
  SURVIVING side beside the already-Lean'd DROP failure. Then attempt `Σ`-monad laws.
- **WRITE**: one remark into the book stratification box; the ℤ/2 grading table is book-ready.
