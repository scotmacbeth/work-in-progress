# Lean M2 — comonad from directed container (forward direction): DONE

**PR #3** (RaggedR/ghani-containers), branch `lean-m2-comonad`.
File: `lean/Containers/Containers/Directed.lean`. Builds on M1 (`Basic`).
Formalises `directed-categories.tex` §3 (the comonad computation).

## What is proved
`DirectedContainer extends Container` with `root`, `sub` (`s↓p`), `shift` (`p⊕q`)
and laws D1–D5. Comonad data `counit`, `comult` on `Ext`. Three theorems:
- `left_counit`  : `counit ∘ comult = id`        (from D1 shapes, D2 values)
- `right_counit` : `Ext.map counit ∘ comult = id` (from D3)
- `coassoc`      : `Ext.map comult ∘ comult = comult ∘ comult` (D4 shapes, D5 values)

Zero `sorry`, zero warnings. `#print axioms` on all three → `{Quot.sound}` only
(the funext backing) — no `sorryAx`, no `Classical.choice`, no `propext`.

## The one design decision worth knowing
The laws are genuinely dependently typed (the paper's remark predicted this):
- **D2** `shift s (root s) q = d1 s ▸ q` — `q : Pos (sub s (root s))`, transported
  to `Pos s` along D1.
- **D5** `shift s (shift s p q) ((d4 s p q).symm ▸ q') = shift s p (shift (sub s p) q q')`
  — `q'` transported along D4 (this is why D5's well-typedness needs D4).
D1, D3, D4 are cast-free.

All the dependent-`Sigma` pain is isolated in ONE helper,
`Ext.ext_eq (hs : s₁=s₂) (hv : ∀ q, v₁ q = v₂ (hs ▸ q)) : ⟨s₁,v₁⟩ = ⟨s₂,v₂⟩`
(proof: `subst hs; funext`). With `hs := rfl` it also handles the equal-shape
layers, so `coassoc` is just: peel two `ext_eq rfl` layers, then `ext_eq (d4 …).symm`
with `(congrArg v (d5 …)).symm`. Clean — no `Eq.mpr`/`HEq` gymnastics needed.

## Honest scope limit — for whoever runs the next prove/lean cycle
This is the **forward** direction only (D1–D5 ⇒ comonad laws), which is exactly
the displayed calculation in §3. The Proposition in `directed-categories.tex` ALSO
claims the **converse** ("every comonad on `Ext` arises this way, the computations
run backwards") and hence a **bijection** between directed-container structures and
comonad structures on `Ext`. That converse is **not formalised**. To do it properly
(M2b) we'd want to: (i) bundle a `Comonad` structure on `Ext C` (counit/comult +
3 laws), (ii) extract `root := counit ⟨s,id⟩`-style data via the M1 Yoneda probe,
(iii) show the two constructions are mutually inverse. Worth a `/prove` pass first
to pin the probe for `comult` (it lands in `Ext (Ext (Pos s)))`, slightly fiddlier
than M1's single probe). Linking: see [[dcont-morphisms-are-cofunctors]] — the
morphism-level story (DCont ≅ Cof) is the next milestone after the object-level
bijection.
