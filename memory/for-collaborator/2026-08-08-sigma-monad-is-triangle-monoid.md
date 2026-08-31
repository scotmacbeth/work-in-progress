# For Neil/Robin — the Σ-lifting was `M ◁ −` all along; `reverse-total ⟹ Σ-monad` is FALSE (Bag)

**MacBeth, 2026-08-08 PROVE.** Full proof: `proofs/2026-08-08-sigma-monad-is-triangle-monoid.md`.
Resolves the open node `reverse-total-implies-coherent-section-OPEN`.

## The one sentence
`T^Σ_M(C) = M ◁ C` (left composition-product), so the Σ-lifting is a monad on `Cont`
**iff `M` is a ◁-monoid in `Cont` = a container monad** — and the meta-pattern holds a 6th time:
the hoped-for clean implication `reverse-total ⟹ Σ-monad` is **false**, refuted by **Bag**.

## What actually happened
Last cycle I proved (in heavy coordinates) that Reader and State have a proof-relevant **Σ**-monad
lifting, via a "canonical section" `σ` satisfying three conditions (U1),(U2),(A), and flagged the
general implication as open. This cycle the coordinates dissolved:

1. **`T^Σ_M = M ◁ −`.** The shapes of `T^Σ_M(S,P)` are `MS = M` applied to the shape set, and the
   positions `∐_{b∈lv(m)}P(x_b)` are exactly the composite-polynomial positions of `M ◁ (S,P)`.
   The unit/mult are `η_M ◁ (−)`, `μ_M ◁ (−)`. So the whole construction is *left ◁-multiplication
   by the container `M`* — nothing more.

2. **Hence Σ-monad ⟺ container-monad.** A monoid `A` in a monoidal category makes `A⊗−` a monad,
   and conversely. Via `Cont ≃ Poly ↪ [Set,Set]` (fully faithful, strong monoidal, `◁↦∘`):
   `T^Σ_M` monad ⟺ `M` a ◁-monoid in `Cont` ⟺ `M` a Set-monad with polynomial structure.
   The mysterious section `σ` is just **`μ_M`'s backward position map**, and (U1),(U2),(A) are the
   ◁-monoid unit/associativity laws read on positions — *automatic* for any container monad.
   Reader = the diagonal comonoid on `E`; State = the store monad. That's why they cohered.

3. **The refutation — Bag.** The finite multiset monad is leaf-supported and **reverse-total** in
   the strongest way (`μ = union` is a *bijection* on leaves, `σ = id`), yet `T^Σ_Bag` is **not a
   monad on `Cont` — not even a functor**, because **Bag is not a container**: it fails to preserve
   the connected pullback `A → 1 ← B`. Computed witness: `|Bag(2×2)|₂ = 10 ≠ 9`, and
   `{(0,0),(1,1)}` vs `{(0,1),(1,0)}` are distinct multisets with the same `(π_A,π_B)`-image — Bag
   forgets the pairing. Functoriality of `T^Σ_Bag` on `Cont` would force a natural label-preserving
   leaf assignment on Bag = a container structure, which Bag lacks. Verified & discriminator-checked
   (List, a real container, *passes* the same test via zip): `scratch/sigma-monad-coherence/bag_not_container.py`.

## Why this is the honest resolution, not a downgrade
- `reverse-total` is the **pointwise / object-level** shadow: "each `μ_M` has *some* label-preserving
  backward map." The genuine content over it is **naturality + coherence = ◁-monoid structure**
  (equivalently, *polynomial* not merely *analytic*). Bag is analytic-not-polynomial: the `Sₙ`
  symmetries are exactly the obstruction.
- The extra structure PROVE.md asked me to identify is **not** a bespoke directedness axiom — it is
  literally "`M` is a ◁-monoid in `Cont`". This welds the surviving-Σ-lifting to the
  directed-container / composition-monoid spine (grant Path 2) as an **identity of endofunctors**,
  not a coincidence of sections. Directed containers = ◁-*comonoids*; container monads = the
  ◁-*monoid* partner; Reader/State are the two motivating monoids.

## Grant hooks
- Sharpens the ℤ/2-graded lifting story: on the surviving (Σ) side, "does `M` lift to a **monad** on
  `Cont`?" has the crisp answer **"iff `M` is a container monad,"** parallel to the ∏ side's
  cartesian/forward-total criterion. Both halves are now clean fibrational statements.
- Reader/State's Σ-monads are now *examples of a theorem* (container monad ⟹ Σ-monad), and the 08-07
  Lean cert (`reader_sigma_*`, axiom-free) is a machine-checked instance of it.

## Open / next
- **LEAN:** state the identity `T^Σ_M = M◁−` and "◁-monoid ⟹ Σ-monad" once, deriving Reader/State as
  corollaries — replaces the bespoke per-monad Lean rungs.
- Still open (unchanged): exhaustiveness of the ∏/Σ parity dichotomy — is *every* proof-relevant
  monad lifting of Reader/State one of ∏, Σ, or a mix?
- Question for Neil: is this the framing you want in book Ch7 — lead with `T^Σ_M = M◁−` and present
  the 08-07 Reader/State proof as the ◁-monoid special case? It makes the chapter much shorter.
