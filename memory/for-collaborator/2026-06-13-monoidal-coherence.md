# Monoidal coherence of the four structures, in explicit container language (2026-06-13)

**For:** Neil / Robin. **Proof:** `projects/proofs/2026-06-13-monoidal-coherence-four-structures.tex` (5pp, compiles).
**Verifier:** `~/.claude/scratch/verify_coherence.py` (120 random + stress, all exact).
**Backs:** PR #16 (`papers/category-of-containers.tex`), which currently *cites* Spivak for the coherence.

## What was asked (PROVE 2026-06-13)
Replace the citation with self-contained, container-level verification of:
(A) associator + unitors for the sequential operator `(Cont,◁,y)`, with **pentagon + triangle**
as explicit shape/position bijection equalities; (B) the strong-monoidal comparison `φ` for the
Dirichlet tensor `⊗`, with its coherence, and `y ↦ Id`.

## What I proved

### (A) Sequential `(Cont, ◁, y)`
- **Associator** `α_{C₁,C₂,C₃}: (C₁◁C₂)◁C₃ ≅ C₁◁(C₂◁C₃)`:
  shape map = **currying** `((s₁,f),g) ↦ (s₁, λp₁.(f p₁, λp₂.g(p₁,p₂)))`;
  position map = **Σ-reassociation** `(p₁,(p₂,p₃)) ↦ ((p₁,p₂),p₃)`. Transport-free — matches
  the Composition.lean associator (PR #13).
- **Unitors** `λ,ρ`: trivial relabelings (`g↦g•`, `(s,!)↦s`).
- **Pentagon (proved).** A shape of the 4-fold `((C₁◁C₂)◁C₃)◁C₄` is a tuple `(s₁,f,g,j)`.
  Both legs `c∘b∘a` and `e∘d` compute to the **same** flattened normal form
  `(s₁, K)`, `K p₁ = (f p₁, λp₂.(g(p₁,p₂), λp₃. j((p₁,p₂),p₃)))`. On positions, every
  elementary `α` and every whiskering is the **identity on the underlying flat tuple
  `(p₁,p₂,p₃,p₄)`** and merely rebrackets; source bracket `(((··)·)·)`, target `(·(·(··)))`;
  both legs are the unique order-preserving rebracket, hence equal.
- **Triangle (proved).** `(C₁◁λ_{C₂})∘α_{C₁,y,C₂} = ρ_{C₁}◁C₂`; both sides `= (s₁, λp₁.g(p₁,•))`,
  positions `(p₁,p₂) ↦ ((p₁,•),p₂)`.
- Coherence (all diagrams) then follows by Mac Lane.

### (B) Dirichlet `⊗`
- `α^⊗` = Cartesian reassociation on shapes **and** positions; its pentagon/triangle are
  literally `(Set,×,1)`'s pentagon/triangle applied to shape sets and position sets.
- **`φ_{C₁,C₂}` is the IDENTITY.** `⟦C₁⊗C₂⟧X = Σ_{(s₁,s₂)}(P₁s₁×P₂s₂→X)` equals
  `⟦C₁⟧⊗_Dir⟦C₂⟧` on the nose, because `⊗_Dir` on `Poly` is defined by the coefficient formula
  `(Σ_s y^{Ps})⊗_Dir(Σ_t y^{Qt}) = Σ_{(s,t)} y^{Ps×Qt}`, and the container `(S,P)` *is* that
  presentation. So `⟦–⟧` is **strict** monoidal for `⊗`, `⟦y⟧=Id`. (Coherence square reduces to
  `⟦α^⊗⟧ = a^Dir`, both Cartesian reassoc.)

## Two honesty flags (please read)
1. **The PROVE/PR-#16 framing "⊗ is the one needing an explicit iso" is gentler than the truth.**
   With `⊗_Dir` in its native polynomial presentation, the comparison is the *identity* and the
   functor is *strict*, not merely strong. I wrote it up as strict and explained why.
2. **The genuine subtlety of `⊗` is presentation-dependence, not a nontrivial φ.** `⊗_Dir` is the
   only one of the four whose target is **not** a pointwise/compositional operation on bare functors
   (`+`=pointwise ⊔, `×`=pointwise ×, `◁`=composition are all intrinsic). `⟦C₁⟧⊗_Dir⟦C₂⟧` can't be
   recovered from the values `⟦Cᵢ⟧X` — it reads the position exponents. That's the real reason it's
   "the subtle one." I put this in Remark (Why ⊗ is the subtle one).

## Suggested next steps (not done in this session)
- **LEAN:** (A)'s explicit `α` (currying + Σ-reassoc, transport-free) is ready-made for a
  pentagon/triangle Lean target on `Composition.lean`. I'd suggest writing `LEAN.md` for it.
- **BOOK:** fold the coherence statements into `papers/category-of-containers.tex`, upgrading the
  `\prov{}` tags on the four propositions from "Cited: Spivak" to "MacBeth-verified (container-level
  pentagon/triangle)". I did **not** touch the shared repo this session (deep-work prove session).
  Worth a small PR — and the Remark on presentation-dependence is, I think, genuinely book-worthy.

— MacBeth
