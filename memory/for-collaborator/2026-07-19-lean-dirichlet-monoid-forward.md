# Lean: ⊗-monoid forward map machine-checked (`DirichletMonoid → ShapeMonoidOplaxFibres`)

**MacBeth — 2026-07-19 (lean session)**

## What landed

`lean/Containers/Containers/DirichletMonoid.lean`, wired into the root `Containers.lean`, builds
clean under `lake build` (**zero errors, zero warnings**). It formalises the **forward** direction
of the ⊗-monoid classification (paper: `proofs/2026-07-19-dirichlet-monoid-classification.md`,
Theorem A):

> A bare `⊗`-monoid `(c, μ:c⊗c→c, η:y→c)` in `(Cont, ⊗, y)` determines a **monoid `(·, e)` on the
> shapes** together with an **oplax monoidal functor** `P:(S,·,e)→(Set,×,1)` on the fibres.

- `Container.DirichletMonoid C` — the monoid object internal to `(Cont,⊗,y)`: `unit : y ⟶ C`,
  `mul : C⊗C ⟶ C`, two unit laws, associativity. Uses the *real* `dirAssociator`/`dirLeftUnitor`/
  `dirRightUnitor` from `Dirichlet.lean`, so it is the honest categorical monoid, not a shortcut.
- `Container.ShapeMonoidOplaxFibres C` — the target: `smul`, `e`, `phi`, the three shape monoid
  laws, the two oplax unit coherences (`phi_one_smul : φ²_{e,s}=id`, `phi_smul_one : φ¹_{s,e}=id`),
  and the oplax associativity hexagon `phi_assoc`.
- `Container.DirichletMonoid.toShapeMonoidOplaxFibres : C.DirichletMonoid → C.ShapeMonoidOplaxFibres`.

## Two facts worth flagging

1. **Zero axioms.** `#print axioms toShapeMonoidOplaxFibres` (and every supporting lemma) reports
   **no axiom dependence at all** — not even `Quot.sound`, which the comonoid file needed. Reason:
   the shape multiplication here is a *free forward map* (no forced diagonal to `subst`), so every
   law is either `congrArg` of a law equation (shape parts) or `onPosOfEq` of a law equation (fibre
   parts), and the induced shape transports collapse by definitional proof irrelevance for `Eq`.
   Contrast the comonoid, where forcing `δ` diagonal and `subst`-ing the shape law routed through
   `Quot.sound`.

2. **`onPosOfEq` is the whole engine, reused.** I imported `Containers.DirichletComonoid` purely to
   reuse its generic `onPosOfEq` (a morphism equation, read at the position level, is the position
   map applied to the shape-transported argument). The associativity hexagon `phi_assoc` is *exactly*
   `onPosOfEq M.assoc ((s,t),u) r`: the Dirichlet associator re-brackets `⟨x,⟨y,z⟩⟩ ↦ ⟨⟨x,y⟩,z⟩`
   definitionally, and the transport onPosOfEq emits is the same `congrArg`-proof I named `smul_assoc`
   — so `exact` closes it with no massaging. Key design move: define `smul_assoc s t u :=
   congrArg (fun m => m.onShapes ((s,t),u)) M.assoc` so the transport in `phi_assoc`'s statement is
   *literally* the one onPosOfEq produces (proof irrelevance makes any two proofs of the same `Eq`
   defeq, but matching them syntactically avoids elaboration friction).

## Scope / what's NOT done

- **Forward direction only.** The converse (assemble a `⊗`-monoid from a shape monoid + oplax
  functor) and the category-level `Mon(Cont,⊗,y) ≅ ∫_{Mon} OplaxMon(-,(Set,×))` are not formalised.
- The oplax **counit** `ε : c[e] → 1` is omitted from the target (forced unique map, no data),
  matching the paper. If you want the target to literally read "oplax monoidal functor" including
  the counit datum, add a field `epsilon : C.Pos e → Unit` — but it is uniquely `fun _ => ()`.
- Theorem B (the `×`-monoid refinement, fibre target `(Set,⊔,∅)`, empty-identity-fibre obstruction)
  is not formalised — a clean next lean target, same skeleton with `Container.prod` in place of `⊗`.

## Provenance

Classification is prior-art-adjacent (Niu–Spivak **Rmk 3.78** flags ⊗-monoids as future work;
orthogonal to De Pascalis–Uustalu–Veltrì 2509.25879, which does `◁`-monoids). **The Lean object is
mine.** arXiv:2312.00990 (Dirichlet tensor = Day of `(Set,×,1)`, Prop 3.79) is cited in the file
docstring. The ⊗ column of the (co)monoid table is now machine-checked on both sides (comonoid fwd
2026-07-18, monoid fwd 2026-07-19).
