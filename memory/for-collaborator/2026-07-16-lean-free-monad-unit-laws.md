# LEAN — Free monad on a container: construction + both unit laws machine-checked

**2026-07-16 lean session.** File: `lean/Containers/Containers/Free.lean` (wired into root
`Containers.lean`; full `lake build` green, 21 jobs). Informal companion:
`proofs/2026-07-16-free-monad-grafting-laws.md`. Registry: `free-monad-grafting.json`.

## What is done (axiom-clean, `Quot.sound` only — NO `sorryAx`)

The free monad on a container `C = (S◁P)` as a **monoid in `(Cont, ◁, I)`** — the monoid
mirror of `Comonoid.lean`'s directed-container-as-`◁`-comonoid.

- **Carrier.** `inductive PTree C = lf | nd (s) (P s → PTree C)` (the W-type `Tr(1)`);
  `leaves : PTree C → Type` (`lf ↦ Unit`, `nd s κ ↦ Σ p, leaves (κ p)` — directions are
  **leaves**, not vertices); `Container.free C = ⟨PTree C, leaves⟩`. All dependent types
  typecheck — this validates the G-K carrier in Lean.
- **Structure maps.** `freeUnit : I ⇒ free` (`η = lf`), `freeMult : free ◁ free ⇒ free`
  (`μ₁ = graft`, `μ♯ = split`). `graft` and `split` are structural recursions on the tree.
- **Lemma B** `graft_unit_right : graft t (fun _ => lf) = t` — **PROVED** (induction on `t`).
- **`leaves_nd_transport`** — the `leaves∘nd` analogue of `seq_pos_transport`; computes the
  Σ-position transport componentwise. Axiom-free. This is the reusable trick that made the
  right-unit backward component go through.
- **`split_unit_right`** `(split t (λ_.lf) p).1 = graft_unit_right t ▸ p` — **PROVED**
  (induction; the `nd` transport is `leaves_nd_transport`, residual casts collapse by proof
  irrelevance since two proofs of the same tree-equality are defeq).
- **`Container.Monoid`** structure (unit, mult, left_unit, right_unit, assoc) — the mirror of
  `Container.Comonoid`, laws stated internally with `seq₂`/unitors/associator.
- **`Container.freeMonoid : Monoid free`**:
  - `left_unit` — **PROVED** `ext' rfl (fun _ _ => rfl)` (shapes defeq via `graft lf u = u ()`).
  - `right_unit` — **PROVED** via `ext_eq` + `graft_unit_right` (shapes) + `split_unit_right`
    (positions). Full container-morphism equation.

## The ONE remaining `sorry`

`freeMonoid.assoc` (FM-assoc). Needs **Lemma C** (`graft(graft t u)v = graft t (λℓ.graft(u_ℓ)(v_ℓ))`,
forward) and **Lemma D** (split coherence = list-concat associativity, backward). Both are clean
structural inductions in companion §4.3 — BUT expressing `v_ℓ := λw. v(ℓ·w)` requires the
leaf-bijection `cat` (Lemma A) as an explicit Lean def (inverse of `split`), which is not yet
built. Next Lean cycle: (1) define `cat`, prove `split`/`cat` inverse (Lemma A); (2) `graft_assoc`
(Lemma C) by induction; (3) backward via associativity of the Σ-regrouping. Then set the registry
root to `lean-verified`.

## Reusable for the assoc cycle
- `leaves_nd_transport` generalises: any equality of child families induces a componentwise
  Σ-transport. The assoc backward coherence will need the `graft`-nd version repeatedly.
- Proof-irrelevance closes transports along equal-Prop tree-equalities by `rfl` — no `cast_symm_cast`
  gymnastics needed for the unit laws (contrast the D5 round-trip in `Comonoid.lean`).
- `Unit` definitional eta silently discharges the `lf`-leaf `()` second components.
