# LEAN 2026-07-30 — Writer/ℤ₂ biKleisli arrow category, machine-checked

**File:** `lean/Containers/Containers/BiKleisliWriter.lean` (imported in the root
`Containers.lean`). Sorry-free, zero warnings, whole library builds (42 jobs).
`arr_assoc_Z2` depends on `[propext, Quot.sound]`; `Tright_unit`/`Tassoc` on
`[Quot.sound]` only. Registry: node `bikleisli-writer-lean` under
`theoremA-forward-noncrossbranch`, `trust=lean-verified`,
`lean=Containers.BiKleisliWriter.arr_assoc`.

## What it delivers (the LEAN target)

The second concrete instance of the abstract biKleisli skeleton
(`Containers.BiKleisli`), after Maybe: **M := Writer over a monoid**, the writer
generator `A×(−)` of the affine class `E+A×(−)`. Discharges **all four**
mixed-DL axioms E1′–E4′ — in particular the branching-obstructed **E2′** — so
`MixedDistrib.acomp_assoc` gives a machine-checked *associative* effect–coeffect
arrow category. With Maybe (`E+(−)`) the pair now spans the two generators of the
affine classification, both in Lean.

## Design decisions worth knowing

- **Generalised past the ask.** LEAN.md asked for ℤ/2 concretely; I did it over an
  **arbitrary monoid** `Mon` (bare Mathlib-free carrier + `one`/`mul` + 3 laws),
  then instantiated at `Z2` (`Bool`/`xor`) for the concrete witness `arr_assoc_Z2`.
  Confirms the skeleton is genuinely monoid-generic, not ℤ/2-specific.
- **κ is literally the identity morphism.** Unlike Maybe (whose κ has the
  empty-product `η`-padding `1→Option 1` over the nullary `none`), Writer has **no
  nullary leaf**, so `G_W(T_W X)` and `T_W(G_W X)` are *definitionally* the same
  container (shape `A×S`, fibre `A×P s`). So `kappa := {onShapes:=id, onPos:=fun _=>id}`
  and all four axioms close by `funext m; rfl` / `intro m p; rfl`. Even cleaner than
  Maybe.

## The one subtlety (the transport, for future writer-of-general-effects work)

Only three declarations are non-`rfl`: the T-monad laws `Tright_unit`/`Tleft_unit`/
`Tassoc`, whose **shape** map rearranges monoid multiplication (`one_mul`/`mul_one`/
`mul_assoc`), so the `ContainerMorphism.ext'` shape hypothesis `hs` is not `rfl`.
Because the position fibre `P s` is independent of the mutated `A`-coordinate, the
ext' transport `congrFun hs s ▸ p` is trivial — but it is *not* `rfl`-reducible
(`Eq.rec` on a non-`rfl` proof stays stuck even when the two Pos types are defeq).

Maybe dodged this entirely: its shape maps `Option.join ∘ some` reduce to `id`
*definitionally*, so `hs = rfl` and no transport appears. For a general monoid,
`mul one a` is not defeq to `a`, so the transport is unavoidable — and it can't be
dodged by a clever concrete monoid either (matching `mul` on the first arg makes
`one_mul` definitional but leaves `mul_one` stuck, and vice versa; exactly one of
the two unit laws always stays stuck).

**The fix** (reusable): a two-line helper
```
theorem heq_pos {α} {motive : α → Type} {a b : α} (h : a = b) (p : motive a) :
    HEq (h ▸ p) p := by subst h; rfl
```
then the ext' position goal (`φ.onPos s p = ψ.onPos s (congrFun hs s ▸ p)` with both
onPos = id, i.e. `p = congrFun hs s ▸ p`) closes with
`exact (eq_of_heq (heq_pos (congrFun hs s) p)).symm`. No Mathlib, no `Classical`
(`eq_of_heq` is choice-free core). This is the pattern to lift for **any** effect
monad on `Cont` whose T mutates shapes non-definitionally — noted here because the
next instances (List/Pf on the *bialgebra* side, or the general affine `E+A×X`) will
hit the same wall.

## Not done (intended)

Branching (Pf) side of Theorem A stays computed-only (`scratch/.../bikleisli.py`) —
it is *provably* not an arrow category, so there is nothing to formalise as an
instance. The general affine monad `E+A×X` (both generators fused) is a natural next
Lean increment but was out of scope for this single-target session.
