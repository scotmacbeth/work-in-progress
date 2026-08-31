# Lean: free-monad MULT-backward — inputs landed, node step remaining

**MacBeth, 2026-07-24 (lean session).**
File: `projects/lean/Containers/Containers/FreeUniversal.lean`. Companion proof:
`projects/proofs/2026-07-24-free-monad-universal-property.md` §4.3.

## What landed this session (sorry-free, `Quot.sound`-only)

Two backward-half extractions of `M`'s monoid laws — the exact duals of the already-shipped
`mult_left_unit` / `mult_assoc_shape`, extracted from `Mon.left_unit` / `Mon.assoc` via
`ContainerMorphism.onPos_congr`:

- `Container.mult_left_unit_pos` — `(μ_M.onPos ⟨ε, fun _ => c⟩ p).2 = mult_left_unit ▸ p`.
- `Container.mult_assoc_pos` — M-associativity backward: the two ways of splitting a target
  position of the (left-/right-)associated shape agree as a regrouped triple
  `⟨⟨q,q'⟩, x⟩ ∈ Σ_q Σ_{q'} M.Pos (C⟨q,q'⟩)`, the transport being *literally*
  `mult_assoc_shape` (same `congrFun (congrArg onShapes Mon.assoc)` term).

Key trick that made `mult_assoc_pos` a one-liner: I wrote the LHS/RHS in fully-computed
coordinate form and closed it with `:= onPos_congr Mon.assoc ⟨⟨a,b⟩,C⟩ r`. All the
`comp`/`seq₂`/`associator` layers reduce **definitionally** to those coordinates, so no
tactic work was needed — Lean accepted the defeq. Same discipline as `mult_assoc_shape`.

## The target theorem `freeExtPos_mult` (removed from the file, kept here)

Statement (position half of `μ ; ĝ = (ĝ ◁ ĝ) ; μ_M`, by recursion on `t`):

```
∀ (t) (u) (p : M.Pos (freeExtShape Mon g (graft t u))),
  split t u (freeExtPos Mon g (graft t u) p)
    = ⟨freeExtPos Mon g t          (μ_M.onPos ⟨a₀, B⟩ (freeExtShape_mult Mon g t u ▸ p)).1,
       freeExtPos Mon g (u (…same…)) (μ_M.onPos ⟨a₀, B⟩ (freeExtShape_mult Mon g t u ▸ p)).2⟩
```
with `a₀ = freeExtShape Mon g t`, `B = fun q' => freeExtShape Mon g (u (freeExtPos Mon g t q'))`.
This is *exactly* the `ContainerMorphism.ext_eq` position obligation of the packaged morphism
equation `(X.freeMult).comp (freeExtend Mon g) = (Container.seq₂ (freeExtend Mon g)
(freeExtend Mon g)).comp Mon.mult`, with `hs ⟨t,u⟩ = freeExtShape_mult Mon g t u`. (I verified
both sides' onShapes/onPos compute to these forms by hand.)

### BASE CASE `t = lf` — DONE, verified (paste-ready)

```lean
  | .lf, u, p => by
      have hkey : ((Mon.mult.onPos ⟨Mon.unit.onShapes (), fun _ =>
            Container.freeExtShape Mon g (u ())⟩
          ((Container.mult_left_unit Mon (Container.freeExtShape Mon g (u ()))).symm ▸ p)).2)
          = p := by
        rw [Container.mult_left_unit_pos Mon (Container.freeExtShape Mon g (u ()))]
        exact Container.cast_symm_cast
          (Container.mult_left_unit Mon (Container.freeExtShape Mon g (u ()))).symm p
      exact congrArg
        (fun w => (⟨(), w⟩ : (ℓ : leaves (PTree.lf : PTree X)) × leaves (u ℓ)))
        (congrArg (Container.freeExtPos Mon g (u ())) hkey.symm)
```
`split lf`, `graft lf`, `freeExtPos lf` all reduce definitionally; the only content is
`qρ.2 = p`, which is `mult_left_unit_pos` then `cast_symm_cast` (note: pass `h.symm`, proof
irrelevance collapses the double-symm).

### NODE STEP `t = nd s κ` — REMAINING (this is the hard half)

Let `head := g.onShapes s`, `b₀' := fun q => freeExtShape Mon g (κ (g.onPos s q))`,
`κ' := fun p_ => graft (κ p_) (fun r => u ⟨p_, r⟩)` (so `graft (nd s κ) u = nd s κ'`), and
`C := fun (qq : Σ q:M.Pos head, M.Pos (b₀' q)) =>
        freeExtShape Mon g (u ⟨g.onPos s qq.1, freeExtPos Mon g (κ (g.onPos s qq.1)) qq.2⟩)`.
Then `C = ` the very family `mult_assoc_shape`/`freeExtShape_mult`(nd) already use.

Three propositional bridges, everything else defeq:

1. **forward-IH (family transport).** `freeExtShape_mult Mon g (κ (g.onPos s q)) (fun r => u ⟨g.onPos s q, r⟩)`
   gives, childwise, `freeExtShape Mon g (κ' (g.onPos s q)) = μ_M.onShapes ⟨b₀' q, fun q' => C ⟨q,q'⟩⟩`.
   `funext` over `q` ⇒ the inner family of the outer split in `freeExtPos Mon g (nd s κ') p`
   (namely `fun q => freeExtShape Mon g (κ' (g.onPos s q))`) equals `b₂ := fun q => μ_M.onShapes ⟨b₀' q, fun q' => C⟨q,q'⟩⟩`.
   This turns the outer split `w := μ_M.onPos ⟨head, fun q => freeExtShape g (κ' …)⟩ p` into the
   RHS-way `qy := μ_M.onPos ⟨head, b₂⟩ (hfam ▸ p)` of `mult_assoc_pos`, at the cost of one
   `hfam ▸` transport (`hfam : ⟨head, fun q => …⟩ = ⟨head, b₂⟩`).

2. **mult_assoc_pos** at `(head, b₀', C)` bridges `qy` (RHS-way) to the statement's
   `qρ := μ_M.onPos ⟨a₀, B⟩ p'` (LHS-way; note `a₀ = μ_M.onShapes ⟨head,b₀'⟩` defeq and
   `B q' = C (μ_M.onPos ⟨head,b₀'⟩ q')` defeq, so the statement split **is** the LHS-way).
   Gives `q = qy.1`, and the inner residuals match up to the regrouping triple.

3. **backward-IH** `freeExtPos_mult Mon g (κ (g.onPos s w.1)) (fun r => u ⟨g.onPos s w.1, r⟩) w.2`
   for the inner `split (κ z.1) …` produced by `split (nd s κ) u`'s `nd`-clause
   (`⟨⟨z.1, rec'.1⟩, rec'.2⟩`, `z = freeExtPos Mon g (nd s κ') p`, `z.1 = g.onPos s w.1`,
   `z.2 = freeExtPos Mon g (κ'(g.onPos s w.1)) w.2` = a `graft` shape ⇒ IH applies).

**Difficulty**: reconciling the three transports (`hfam ▸`, `mult_assoc_shape ▸` inside
`mult_assoc_pos`, and `freeExtShape_mult ▸` inside the inner IH). Structurally it mirrors
`Free.split_assoc` (which used `generalize` + `leaves_nd_transport`) **plus** the associativity
reconciliation. Budget it like `split_assoc` × ~1.5. Recommend: `generalize` the outer split
`w`, rewrite the family with `hfam` first (so `mult_assoc_pos` applies syntactically), then
`leaves_nd_transport` at the node, then the inner IH. NO new infra needed — all three inputs
exist and are verified.

## Uniqueness (companion §6) — separate, also remaining
Needs `cat`/`split` bijectivity in `Free.lean` (not yet there). Independent of the above.
Do MULT-backward first; uniqueness reuses `split`-bijectivity which is its own lemma.
