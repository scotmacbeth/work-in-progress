# LEAN handoff — free-monad universal property (PARTIAL) + cofree comonad BLOCKED

**2026-07-24 lean session.** MacBeth.

## Two findings up front

1. **The cofree comonad (LEAN.md's named target) is NOT honestly formalisable in this project.**
   `lean/Containers` is **Lean 4 core, no Mathlib** (`leanprover/lean4:v4.30.0`, zero `import
   Mathlib` anywhere). The cofree comonad's carrier is the final coalgebra `νY.(S × ∏_P Y)` =
   `PFunctor.M` — a **coinductive M-type**. Lean 4 **core has no coinductive types** and no
   `PFunctor.M`. LEAN.md flagged this exact risk ("does `lean/Containers/` import Mathlib?"); the
   answer is no, so fallback rung 3 fires. The sanctioned fallback (bounded-depth truncation
   `C^{≤n}`) is low-value and awkward — a depth-`n` truncation is *not a comonad on the nose*
   (comultiplication re-roots and changes depth), so "the comonad laws up to depth n" is not a
   clean statement. **Decision:** I did not force it. To get a genuine Lean cofree comonad, the
   project needs Mathlib added (then `C^∞ := PFunctor.M ⟨S,P⟩`, laws by `PFunctor.M.bisim`) — a
   Robin infrastructure call, not a one-hour in-session move.

2. **Instead I formalised (partially) the free-monad universal property** — the 2026-07-24 proof
   (`proofs/2026-07-24-free-monad-universal-property.md`), which post-dates LEAN.md and explicitly
   nominates itself as "the next LEAN target" (§9.4). It is a **W-type** target (inductive, core-
   tractable) that extends the already-verified `Free.lean`, and it is the honest dual-relevant
   Chapter-4 artifact. This is a deliberate, documented deviation from LEAN.md's named object,
   forced by finding #1.

## What is machine-checked — `Containers/FreeUniversal.lean` (in root lib, `lake build` green, 0 warnings)

All results below `#print axioms`-clean: **`[Quot.sound]` only** — no `sorry`, no `Classical`.

- `Container.freeInsert X : X ⟶ X.free` — the insertion of generators `α_X`
  (`α₁ s = nd s (fun _ => lf)`, `α♯` = first projection).
- `Container.freeExtShape Mon g : PTree X → M.Shape` = `ĝ₁` by tree recursion
  (`lf ↦ ε`, `nd s κ ↦ μ_M(g s, fun q ↦ ĝ₁(κ (g♯_s q)))`).
- `Container.freeExtPos Mon g : (t) → M.Pos(ĝ₁ t) → leaves t` = `ĝ♯` (mirrored via `μ_M♯`).
- `Container.freeExtend Mon g : X.free ⟶ M` = **`ĝ` packaged as a full morphism** (both components).
- **`Container.freeExtend_triangle`** = the **FULL adjunction triangle `α ; ĝ = g`**, BOTH shape
  and position halves (the universal-arrow / existence condition). Position half uses the new
  `Container.mult_right_unit_pos` (M's right-unit backward law), itself extracted through the
  generic **`ContainerMorphism.onPos_congr`**.
- **`Container.freeExtend_unit`** = `ĝ` preserves the monoid **unit** (full morphism eq).
- **`Container.freeExtShape_unique`** = **object-level uniqueness**: any recursion-consistent shape
  map is `ĝ₁` (transport-free structural induction).
- `Container.mult_left_unit` / `mult_right_unit` = M's forward unit laws in coordinates.

### Reusable trick
`ContainerMorphism.onPos_congr : (φ = ψ) → φ.onPos s p = ψ.onPos s (congr ▸ p)` — `cases` on the
morphism equality collapses the transport to `rfl`. This is the **projection** direction of
`ext'`/`ext_eq` (which only go the *construction* way) and turns any packaged monoid/comonoid law
into its backward/position coordinate fact. It is what made `mult_right_unit_pos` (hence the full
triangle position half) a two-liner. Likely reusable for the remaining MULT-backward.

## What remains (NOT yet Lean — honest gap, for a follow-up prove/lean pass)

- **The homomorphism MULT law** `freeMult ; ĝ = (ĝ ◁ ĝ) ; μ_M` (companion §4). Its forward half
  needs **M-associativity forward** (I did not derive `mult_assoc` from `Mon.assoc` — the
  associator makes it heavier than the unit projections); its backward half is the
  **`split_assoc`-level** position identity threading M-assoc through the leaf-path split.
- **Backward half of uniqueness among monoid morphisms** (companion §6) — needs the MULT law +
  `split` bijectivity (Lemma A) to force `h♯ = ĝ♯`.

So the registry node `free-monad-universal-property` stays **`proved`, NOT `lean-verified`**: I
added a `lean_status` recording exactly the above. Do not upgrade the grade until the MULT law is
in Lean.

## Suggested next steps
1. First derive `Container.mult_assoc` (forward) from `Mon.assoc` by evaluating `congrArg onShapes
   Mon.assoc` at an associator shape — the analogue of `mult_left/right_unit` but with the
   associator's currying. Then MULT-forward is a clean induction (base = `mult_left_unit`).
2. MULT-backward via `onPos_congr` on `Mon.assoc` + the `Free.split_assoc` machinery.
3. Separately: decide whether to add Mathlib so the **cofree comonad** (LEAN.md's original target)
   can be done via `PFunctor.M` + `bisim`. That is the real Chapter-4 comonad-side artifact and is
   simply out of reach in core Lean.
