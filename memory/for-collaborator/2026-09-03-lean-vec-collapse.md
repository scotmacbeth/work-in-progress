# LEAN 2026-09-03 — Theorem-D Vec_fd collapse, machine-checked (sorry-free)

**File:** `lean/Containers/Containers/VecCollapse.lean` — sorry-free, wired into
root (`Containers.lean`), full library build green (**61 jobs, 0 warnings, 0
sorry**). Lean 4 core, **ZERO Mathlib**.

## What this closes

This is the **worked Vec_fd instance** that the QpfCollapse note
(`2026-09-02-lean-qpf-collapse.md`) and SUMMARY line 27 flagged as *still open*:
the specific collapse `({∗},k²)` vs `({1,2},k)`. As the target `LEAN.md`
anticipated, the cleanest statement is **NOT a `Wequiv`/`Mcongr` quotient** but a
**natural isomorphism of the two extension functors** — because here `abs` is an
**iso**, not a proper quotient (contrast `Bag₂`, quotient by leaf-swap).

## The one idea

Over `Vec`, a finite coproduct is a **biproduct**, so its underlying type is the
**product**. Hence the *linear* container extension is the **Π-over-shapes**
```
  LExt (S,Pos) X = (s : S) → (Pos s → X)
```
— the ONLY change from the *set* extension `Ext (S,Pos) X = Σ s, (Pos s → X)` of
`Basic.lean` is `Σ ↝ Π`. **That single Σ→Π shift is the biproduct collapse.**
Positions are carried by their **basis types** (no Mathlib linear algebra):
`k²` ↦ `Bool` (two basis vectors), `k` ↦ `Unit` (one). Then

* `p  = ({∗}, k²)` is `Container.mk Unit (fun _ => Bool)`, `LExt p X = Unit → (Bool → X)`;
* `p' = ({1,2}, k)` is `Container.mk Bool (fun _ => Unit)`, `LExt p' X = Bool → (Unit → X)`;
* both are the two-power `Pow₂ X = Bool → X ≅ X ⊕ X`.

## What is certified

| declaration | statement | axioms |
|---|---|---|
| `collapseIso : LinNatIso p p'` | nat iso `LExt p ≅ LExt p'` (both triangles + naturality) | `[Quot.sound]` (funext) |
| `pIso`/`p'Iso` + `_left`/`_right`/`_natural` | both extensions ≅ the common cover `Pow₂`, `abs` **invertible** | `[Quot.sound]` |
| `collapse_factors_through_cover` | `collapseIso` factors through `Pow₂` (`p'Iso.inv ∘ pIso = toP'`) | none |
| `shapes_not_equiv` | **no bijection** `Unit ≃ Bool` ⟹ `p ≇ p'` as containers (Lemma 1.3) | **none** |

So: the two containers present the **same** linear functor `X ↦ X⊕X` yet are
**not isomorphic** — a machine-checked certificate for **Theorem D(ii)**'s
non-injectivity of `⟦−⟧` (`proofs/2026-08-30-admissibility-and-the-connectedness-converse.md`
§6). The choice "`◁ := ⊗`" on the collapse locus is a *choice of presentation*.

## QPF framing (honest scope)

`abs` here is an **iso** (exact identification, degenerate quotient) — the
`pIso`/`p'Iso` witnesses. This is the anticipated contrast with `Bag₂` where
`abs` is a proper non-injective quotient by leaf-swap. The full `Wequiv`/`Mcongr`
*cover* of Avigad–Carneiro–Hudon (ITP 2019, `10.4230/LIPIcs.ITP.2019.6`) would
add nothing here because the identification is already an iso; it is genuinely
needed only for proper (co)inductive quotients. **No gap in the math** — the
nat-iso is the right object, delivered.

## Registry

`linear-containers-vec.json` → `part1-finite-collapse` gains a `lean-verified`
child `lean-theorem-D-collapse-witness` (`lean: Containers.VecCollapse.collapseIso`).
The parent Thm 2.1 node is untouched; the Bag₂ node
(`lean-qpf-collapse-abs-repr`) is untouched. `registry_validate.py` reports only
4 **pre-existing** advisory boundary issues on unrelated nodes (my child is
`lean-verified` under a `proved` parent — no violation).
