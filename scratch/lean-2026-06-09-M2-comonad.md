# M2: comonad ↔ directed container — Lean scratch

Target: `/home/agent/projects/lean/Containers/Containers/Directed.lean`
Source: `directed-categories.tex` §3.
Builds on M1 (`Containers.Basic`): `Container`, `Ext`, `Ext.map`, `map_id`, `map_comp`.

## Dependency Audit
- Lean 4 core only (no Mathlib). All structural: `Sigma`, `funext`, `Eq.rec`/`▸`.
- Reuse `Ext`, `Ext.map` from `Containers.Basic`.
- No Mathlib lemmas needed.

## Key design decision: dependent-type casts in the laws
The directed-container laws are NOT all cast-free. Following ACU "When is a container a comonad?":
- D1 `sub s (root s) = s` — clean equality.
- D4 `sub s (shift s p q) = sub (sub s p) q` — clean equality.
- D3 `shift s p (root (sub s p)) = p` — both sides `Pos s`, CLEAN.
- D2 `shift s (root s) q = d1 s ▸ q` — needs D1 cast (q : Pos (sub s (root s)) → Pos s).
- D5 `shift s (shift s p q) ((d4 s p q).symm ▸ q') = shift s p (shift (sub s p) q q')`
     — needs D4 cast on q' (Pos (sub (sub s p) q) → Pos (sub s (shift s p q))). Both sides Pos s.

## Comonad data on D = Ext C
- counit ⟨s,v⟩ = v (root s)
- comult ⟨s,v⟩ = ⟨s, fun p => ⟨sub s p, fun q => v (shift s p q)⟩⟩

## The three laws (paper §3)
- left counit: counit ∘ comult = id        [uses D1 (shape) + D2 (value)]
- right counit: map counit ∘ comult = id    [uses D3, shape stays s]
- coassoc: map comult ∘ comult = comult ∘ comult  [D4 shape, D5 value]

## Proof tooling: Sigma extensionality helper
ext_eq : {s₁ s₂ : Shape} (hs : s₁ = s₂) {v₁ v₂} (hv : ∀ q, v₁ q = v₂ (hs ▸ q))
         → (⟨s₁,v₁⟩ : Ext C X) = ⟨s₂,v₂⟩
Proof: cases hs; funext-style. With hs := rfl, `hs ▸ q` ≡ q (defeq), so same-shape case is free.

### left counit via ext_eq
apply ext_eq (d1 s); hv q : v (shift s (root s) q) = v (d1 s ▸ q) = congrArg v (d2 s q).

### right counit
shapes both s. funext p; counit of inner = v (shift s p (root (sub s p))) = v p by d3.

### coassoc (the crux)
peel: ext_eq rfl (top, shape s) → intro p → ext_eq rfl (mid, shape sub s p) → intro q
  → innermost: ⟨sub(sub s p) q, valL⟩ = ⟨sub s (shift s p q), valR⟩
  apply ext_eq (d4 s p q).symm; hv q' : valL q' = valR ((d4..).symm ▸ q')
    valL q' = v (shift s p (shift (sub s p) q q'))
    valR (cast q') = v (shift s (shift s p q) ((d4..).symm ▸ q'))
    = by d5 (which says shift s (shift s p q) (cast q') = shift s p (shift (sub s p) q q'))
    so hv = (congrArg v (d5 s p q q')).symm

## OUTCOME: SUCCESS (zero sorry, zero warnings)
Built clean. `#print axioms` → all three depend ONLY on `Quot.sound` (funext backing).
No sorryAx, no Classical.choice, no propext. Plan worked verbatim; only bug was
import-ordering (import must precede module docstring).

Scope note (honest): formalised the FORWARD direction only — D1–D5 ⇒ three comonad
laws, which is exactly §3's displayed computation and what LEAN.md asked. The paper's
Proposition also asserts the CONVERSE (comonad on Ext ⇒ directed container) and the
bijection; that is NOT formalised here. Future cycle (M2b).

## Risks (all retired)
- `▸` choosing wrong motive in ext_eq. Fallback: explicit `cast (congrArg C.Pos hs) q`.
- `apply ext_eq` unifying implicit v₁ v₂ from goal Sigma. Should work; goal is explicit ⟨_,_⟩=⟨_,_⟩.
- defeq reduction of comult/counit/map: use `show` with reduced form or `simp only [defs]`.
