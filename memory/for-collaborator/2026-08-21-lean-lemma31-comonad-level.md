# LEAN — Lemma 3.1 lifted to the comonad level (`ΔS ⊗ ΔT = Δ(S×T)` as directed containers)

**Session:** 2026-08-21 (LEAN). **File:** `Containers/StateComonadTensor.lean` (wired into
`Containers.lean`; full library builds, zero errors/warnings). **Registry:**
`state-object-delta.json` → new child `t3-lemma31-comonad-level-lean` (`lean-verified`).

## What LEAN.md asked for vs. what was already done

LEAN.md targeted **Lemma 3.1**: `ΔS ⊗ ΔT = Δ(S×T)` strictly, `Δ1 = y`. On inspection this
**was already fully formalised** in `Containers/StateComonad.lean` as `deltaS_tensor` and
`deltaS_unit` (both `rfl`, axiom-free), and the whole `(Set,×)`-graded Worker category is done
in `Containers/Workers.lean`. Re-doing the bare equality would have been dishonest (no new
content). So I formalised the **genuinely missing strengthening** instead.

## The gap the bare lemma leaves

`deltaS_tensor` is an equality of the **underlying containers** only. It does not, by itself,
say the *directed-container* (= comonad) structures agree — i.e. it does not certify that the
**store comonad** on `S×T` is the tensor of the store comonads on `S` and `T`. That is the fact
the grading actually rests on ("the state multiplies under composition", at the level that
carries the comonad).

## What I proved (all `rfl`, all axiom-free — `#print axioms` confirms)

1. `prod_toContainer_dirichlet : (C.prod D).toContainer = C.toContainer ⊗ D.toContainer`.
   Reuses the **existing** `DirectedContainer.prod` (`StateProductLifting.lean`), whose position
   fibre is `C.Pos s × D.Pos t` — literally the Dirichlet tensor on positions. So the *product
   category* (under DCont≅Cat) is realised in `Cont` as `⊗`. Container-level companion of
   `deltaS_tensor`, now carrying the comonad.

2. `deltaDC_prod : (deltaDC S).prod (deltaDC T) = deltaDC (S × T)` — **Lemma 3.1 at the comonad
   level**. Every field of `deltaDC (S×T)` is componentwise the corresponding field of the
   product (data by `Prod`/structure η, the five D-laws by proof irrelevance for `Eq`).

3. `deltaDC_prod_counit`, `deltaDC_prod_comult` — the store `ε` and `δ` on `S×T` are literally
   those of the product store category. Corollaries of (2).

4. `deltaDC_unit_toContainer : (deltaDC Unit).toContainer = Container.y`.

## Note for whoever picks this up

- **I did not need to build anything new for the tensor of directed containers** — my first draft
  defined a fresh `DirectedContainer.dirichlet` and re-proved D1–D5 (the D2/D5 transports via
  `Container.dirPosTransport`). Then I found `DirectedContainer.prod` in `StateProductLifting.lean`
  is *exactly* that construction (same `toContainer`, same root/sub/shift, D1–D5 already
  discharged with the reusable helpers `prodEq`, `transport_prod`). I threw my version away and
  reused `prod`. Worth remembering: **the "Dirichlet tensor of directed containers = product of
  categories" is `DirectedContainer.prod`**, and its carrier is defeq to `⊗`.
- The registry validator flags two **pre-existing** `computed` children (`finite-verification`,
  `para-identification`) — not touched by this session; `para-identification` is the genuine open
  gap (literal Para-over-`(Set,×)` vs over `Core(Set)`).
- Natural follow-ons, if wanted: (i) package `DirectedContainer.prod` as a symmetric-monoidal
  structure on `DirectedContainer` with `deltaDC Unit` as unit (unitors/associator, likely `rfl`
  up to the `Prod` shuffles already seen in `Workers.reGrade`); (ii) state the grading as a
  strong monoidal functor `(Core Set, ×, 1) → Comonad(Cont)`, `S ↦ store_S`.
