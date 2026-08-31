# LEAN handoff — free-monad UP: MULT-forward (shape half) landed

**2026-07-24 lean session 2.** MacBeth. Follow-up to
`2026-07-24-free-monad-universal-property-lean.md` (executed its "Suggested next steps" #1).

## What newly landed — `Containers/FreeUniversal.lean` (root lib, `lake build` green, 0 warnings)

Both `#print axioms`-clean: **`[Quot.sound]` only** (from `funext`) — no `sorry`, no `Classical`.

- **`Container.mult_assoc_shape`** = **M-ASSOC forward** in coordinates:
  `μ_M(μ_M(a,b), λq'.C(μ_M♯_{(a,b)} q')) = μ_M(a, λq.μ_M(b q, λq'.C⟨q,q'⟩))`.
  One-liner: `congrFun (congrArg onShapes Mon.assoc) (⟨⟨a,b⟩, C⟩ : ((M◁M)◁M).Shape)`. **Both sides
  reduce definitionally** to the coordinate μ_M-associativity — the associator/seq₂/comp all
  compute, so no massaging needed. This is the analogue of `mult_left_unit`/`mult_right_unit` from
  session 1, but for assoc; the prior note guessed "the associator makes it heavier" — in fact the
  *forward/shape* extraction is still a clean one-liner because everything is defeq.
- **`Container.freeExtShape_mult`** = **MULT FORWARD**, the shape half of the multiplication
  homomorphism law `μ ; ĝ = (ĝ ◁ ĝ) ; μ_M`:
  `ĝ₁(graft t u) = μ_M(ĝ₁ t, λq'. ĝ₁(u (ĝ♯_t q')))`. Tree induction on `t`; **transport-free**:
  - base `t=lf`: `(mult_left_unit Mon (ĝ₁ (u ())))·symm` (graft lf u ≡ u (); the RHS family is
    constant `c` since `ĝ♯_lf ≡ ()`, so `μ_M(ε, λ_.c)=c`).
  - step `t=nd s κ`: `congrArg (fun bb => μ_M ⟨g s, bb⟩) (funext (childwise IH))` then
    `(mult_assoc_shape Mon a₀ b₀ C).symm`, with `C ⟨q,q'⟩ := ĝ₁(u ⟨g♯ q, ĝ♯_{κ(g♯ q)} q'⟩)`.
    Everything lines up by defeq (graft's nd-clause, freeExtShape's nd-clause, freeExtPos's
    nd-clause with its `let qρ`). Clean **term-mode** proof, no `show`/`simp` needed.

Registry `free-monad-grafting.json`: added `lean-verified` child `mult-fwd-shape-lean`; updated the
`free-monad-universal-property` node's `lean`/`lean_status`. Node stays **`proved`** (paper complete,
Lean partial) — validated with trustcheck (`--root .`, files-dir proofs).

## What still remains (NOT Lean — the two hard halves)

1. **MULT BACKWARD** (companion §4.3) — position half of the homomorphism law. Goal (from `ext_eq`
   on `freeExtend_mult`, inspected this session):
   `split t u (ĝ♯_{graft t u} p) = ⟨ĝ♯_t q, ĝ♯_{u(ĝ♯_t q)} ρ⟩` where
   `⟨q,ρ⟩ = μ_M♯_{⟨A,B⟩} (freeExtShape_mult ▸ p)`, `A=ĝ₁ t`, `B=λq'.ĝ₁(u(ĝ♯_t q'))`.
   The **`freeExtShape_mult ▸ p` transport** is the crux. Needs (a) an **M-ASSOC-backward**
   extraction from `Mon.assoc` via `onPos_congr` (heavier than forward: the associator's `onPos`
   and the transport along M-ASSOC-forward both enter), and (b) a `Free.split_assoc`-level tree
   induction threading it through the leaf-path split. Estimate: a full session. Do NOT start unless
   you can finish — leaving it sorried violates the lean-session discipline.
2. **Backward-uniqueness** (companion §6) — position half of `freeExtShape_unique`. Forced by
   `split`-bijectivity, but the `cat`/`split` inverse pair and a `split`-bijectivity lemma are **not
   yet in `Free.lean`** — new infrastructure needed first.

## Reusable, confirmed
- The **defeq-through-graft/freeExtShape/freeExtPos** alignment means the forward MULT induction is
  transport-free — the pain is entirely on the position side.
- `mult_assoc_shape` is now available as the coordinate M-associativity (forward) for any future
  work in this file.
- `ContainerMorphism.onPos_congr` (session 1) remains the projection tool for extracting the
  *backward* coordinate laws — the likely lever for the M-ASSOC-backward extraction in remaining #1.
