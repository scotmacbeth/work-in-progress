# Lean: QPF `abs`/`repr` as the constructive presentation of a collapse locus (2026-09-02)

**File:** `lean/Containers/Containers/QpfCollapse.lean` — sorry-free, wired into root
(`Containers.lean`), full library build green (60 jobs, 0 warnings, 0 sorry).

## What was formalised
The **abs/repr (QPF) pattern** from `connections/qpf-is-the-tool-for-collapse-loci.md`, demonstrated on
the smallest genuine collapse locus: the **two-leaf bag** (unordered pair) functor
`Bag₂ X = (X × X)/swap = Sym²X`.

- `pairC : Container` — the two-position container (`Shape = Unit`, `Pos _ = Bool`); its extension is
  the polynomial functor `Poly X = X × X`. Round-trips `polyOfExt`/`extOfPoly` machine-check
  `Ext pairC X ≅ Poly X`, so the polynomial functor really is a container extension.
- `swap` = the **leaf-symmetry**; `swap_swap`/`map_swap` (involution, natural). `Rel` = "identified with
  your swap"; `Rel.equivalence`; `setoid`; `Bag₂ X := Quotient (setoid X)`.
- **QPF data:** `abs = Quotient.mk`; `repr` = a `Classical.choose` section (core Lean has **no**
  `Quotient.out`, so I built the section from `Quotient.exists_rep`); **`abs_repr : abs (repr y) = y`**
  = `Classical.choose_spec` — the split-surjection law.
- `Bag₂.map` (lift of `Poly.map`, well-defined because `Poly.map` commutes with `swap`); **`abs_map`**
  naturality holds by `rfl`; `Bag₂.map_id` functor law.
- `MinimalQPF` record bundling `(P : Container, abs, repr, abs_repr)`; `bag₂QPF : MinimalQPF Bag₂`
  presents `Bag₂` via `pairC`.

`#print axioms`: `abs_repr`, `bag₂QPF` → `[Classical.choice]`; `abs_map`, `abs_swap`, `Bag₂.map_id`,
`extOfPoly_polyOfExt` → `[Quot.sound]`. No `sorryAx`. (Choice is intrinsic to any QPF `repr`; `Quot.sound`
is intrinsic to quotients — both expected.)

## Why it matters (grant / Theorem D)
Turns the standing IDENTIFICATION caveat — "over a disconnected unit `⟦−⟧` is not injective on objects,
so `◁ := ⊗` is a *choice of presentation*" (Theorem D,
`proofs/2026-08-30-admissibility-and-the-connectedness-converse.md`) — from a disclaimer into a
*constructive Lean pattern*: work in the QPF, not the naive container. The quotiented symmetry is
**exactly** the leaf-swap that obstructs `Arr_M` being a category
([[effect-coeffect-arrows-first-strength]]), so the QPF quotient is tied to an obstruction already proved.

## Two things I corrected vs the brief
1. **No Mathlib.** This project has **zero** Mathlib dependency (pure Lean 4 core, all `Containers.*`).
   The brief's primary plan (Mathlib `MvQPF`) was off-table; I took the explicit **fallback** — hand-roll
   a minimal QPF in core. `Quotient.out`/`out_eq` are Mathlib-only, so `repr` is built from core
   `Quotient.exists_rep` + `Classical.choose`.
2. **Citation DOI.** LEAN.md said `10.4230/LIPIcs.ITP.2019.17`. Per the connection file that is an
   unrelated Forster–Kunze paper; the correct ACH DOI is **`10.4230/LIPIcs.ITP.2019.6`** (LIPIcs 141,
   pp. 6:1–6:19). Fixed in the Lean docstring. Worth correcting wherever `.17` was propagated.

## What is NOT claimed
This is the *proof-of-concept* target, not the specific `Vec_fd` `({∗},k²) ≅ ({1,2},k)` identification via
ACH's `Wequiv`/`Mcongr` machinery — that heavier check (their initial-algebra quotient relation on a real
collapse container) is still open and is what the connection file listed as the deciding experiment. What
is demonstrated: the abs/repr retraction is a concrete, sorry-free, container-native pattern, and the
quotiented symmetry is a proved obstruction, not a toy.

No registry node covers this (it formalises a connection + the Theorem-D *pattern*, not a single registry
proof), so I left the registry untouched.
