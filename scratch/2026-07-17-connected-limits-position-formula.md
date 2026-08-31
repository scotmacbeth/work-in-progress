# Which functors are containers + the position-recovery formula (ALL CITATION — do not claim)
*2026-07-17, for Neil's containers chapter (uid 63). Research-agent citation hunt.*

## Theorem (omnibus). For `F : Set → Set`, TFAE:
- `F` is a container extension `⟦S,P⟧` (polynomial / coproduct of representables / familially representable);
- `F` **preserves connected limits** ≡ preserves wide pullbacks + cofiltered limits;
- `F` is a parametric right adjoint (local right adjoint); every slice of `el(F)` has an initial object (Girard normal form).

**Finiteness fork:** finite connected limits do NOT suffice — need cofiltered limits too (GK counterexample: an `F` preserving finite limits but not `∅` = empty cofiltered limit). So Neil's "preserves connected limits" is the correct complete phrasing; "wide pullbacks" is the finitary restatement.

## Position/shape recovery formula (Gambino–Kock Prop 1.22)
- **Shapes:** `S = F(1)`. ✓
- **Positions:** for `s ∈ F(1)`, `P(s)` = domain of the **generic element** = initial object of the
  `s`-component of `el(F)`. I.e. ∃ `g_s ∈ F(P(s))` over `s`, universal: ∀ `x∈F(X)` over `s`, unique
  `α:P(s)→X` with `F(α)(g_s)=x`. Gives `F(X) ≅ Σ_{s∈F(1)} X^{P(s)}`. (Componentwise Yoneda.)
- **Secondary:** total positions `Σ_s P(s) = (∂F)(1)` (derivative at 1); `P(s)` = its fibre over `s`.
  But `∂F` is derived, not a single evaluation — restatement, not shortcut.

## ★ CORRECTION for Neil (his conjectured formula is wrong — honest flag)
Neil hinted `P(s)` = fibre over `s` of `F(2)→F(1)` (induced by `2→1`). **That gives `2^{P(s)}` (the
POWERSET), not `P(s).`** Because `F(2)=Σ_{s'}2^{P(s')}` and the map to `F(1)` forgets the function, so
the fibre over `s` is `{φ:P(s)→2}=2^{P(s)}`. A plain evaluation-and-fibre cannot extract `P(s)` — the
recovery genuinely needs the generic-element/connected-limit universal property.

## Attribution ladder (cite precisely)
- (connected limits ⇔ familially representable): **Diers 1977** (thèse, Paris VI), clarified
  **Carboni–Johnstone, MSCS 5(4) 1995, 441–459** (+ **Corrigenda MSCS 14(1) 2004** — errors found by
  Leinster & Zawadowski, on the Artin-glueing/topos side, do NOT affect this equivalence).
- p.r.a. clarification: **Weber**; normal functors: **Girard**, **Lamarche**, **Paul Taylor**.
- omnibus + explicit formula: **Gambino–Kock, "Polynomial functors and polynomial monads",
  arXiv:0906.4931, §1.18 + Prop 1.22** ← cleanest single citation.
- embedding (full & faithful): **Abbott–Altenkirch–Ghani, TCS 342 (2005) Thm 3.4** — but does NOT
  state the recovery formula (uses `S=F(1)` implicitly).

## Terminology hazard to warn Neil about (Poly clash)
In Spivak's Poly, `p(1)` elements are called **"positions"** (= container SHAPES) and fibre `p[i]`
elements **"directions"** (= container POSITIONS). Opposite naming. Flag in the chapter.
