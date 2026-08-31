# Monad→comonad transfer on Cont — PROVED (Neil's Ch4 item 2)

**For Robin & Neil. Full proof: `proofs/2026-07-25-monad-comonad-transfer.md`. Registry validates at `proved`.**

## What Neil asked (2026-07-24 email, item 2)
A monad `M=(M,η,μ)` on Set should transfer to a comonad `G(S,P)=(S,M∘P)` on Cont, with the comonad
laws being `M`'s monad laws read through the position-contravariance. He conjectured `G` is "a left Kan
extension from the ◁-**left**-coclosure." **All confirmed and proved.**

## The result, in one breath
`G(S,P)=(S,M∘P)`, counit's backward map `=η`, comult's backward map `=μ`. Because `ε,δ` are identity on
shapes, every comonad law is an equation of *backward* maps in Set, and backward maps compose in reverse
— so **reversing the arrows turns each monad law into the correspondingly named comonad law**:

| comonad law of G | monad law of M |
|---|---|
| counit-left `ε_G∘δ=id` | right unit `μ∘ηM=id` |
| counit-right `Gε∘δ=id` | left unit `μ∘Mη=id` |
| coassoc `Gδ∘δ=δ_G∘δ` | assoc `μ∘Mμ=μ∘μM` |

It's a genuine **biconditional** (the single-shape container `(1,A)` realises every set `A` as a fibre),
and negative controls fire exactly (wrong `η` kills only the counit laws, non-assoc `μ` only coassoc).

## Neil's "why" — he was exactly right
Meyers' left coclosure of ◁ (Niu–Spivak **Prop 6.57**, formula 6.59) is `{q/p}=Σ_{i∈p(1)} y^{q(p[i])}`.
Put the **monad in the numerator** (`q=M`) and `p=(S,P)`:
```
{M/(S,P)} = Σ_{s∈S} y^{M(Ps)} = (S, M∘P) = G(S,P).
```
So **G IS the ◁-left-coclosure with M on top.** I proved the universal property for arbitrary `M` by
Yoneda: `Poly(Gp, r) ≅ [Set,Set](⟦p⟧, r◁M)` (counting-verified). By Trimble (Ex 6.63) the coclosure is a
left Kan extension, so `G(S,P)=Lan_{(S,P)} M` — **precisely Neil's phrasing.** (Companion: since
Cont=Fam(Set^op), G is also `Lan_y(y∘M^op)`, the coproduct-preserving extension of `y^A↦y^{MA}`.)

## The mechanism (the one-line reason)
The fibration `Cont→Set` has fibre `(Set^op)^S`. `G` is fibrewise postcomposition by `M`, i.e. the
pushforward of `M^op`. A **monad on Set = a comonad on Set^op**; "positions are contravariant" is that op.
Same construction `M↦(M^op)_*` gives the dual: a comonad `W` on Set → monad `H(S,P)=(S,W∘P)` on Cont.

## Poly descent (Neil's item 2b)
`⟦G(S,P)⟧(A) = Σ_s (M(Ps) → A)`; transported to Poly, `Ĝ` = "apply M to the fibres of the direction
bundle," counit/comult = re-exponentiate the position sets along `η`/`μ`.

## Novelty — cleared
NOT in Ahman–Uustalu (they cointerpret Cont^op→[Set,Set], the *opposite* direction), NOT in Purdy–Damato
(horizontal distributive laws between given monadic containers), NOT a named Niu–Spivak construction (their
nearest named object is the very coclosure the proof uses). It's an instance of standard **fibred-category
folklore** (a (co)monad on the fibre induces a fibrewise one on the total category); the contribution is
the container-coordinate proof, the fibred mechanism, the coclosure identity confirming Neil's Kan-extension
picture, and the Ch4 exposition.

## Next
1. **Lean** — the transfer comonad is elementary and core (no Mathlib), a clean mirror of
   `DirichletComonoid.lean`; the three comonad laws reduce to `M`'s three monad laws.
2. **Write** — this is a ready Ch4 "Monads and Comonads" section: state `G`, the coordinate proof, the
   coclosure/Lan characterisation as the "why," the dual `H`, and the Poly descent.
3. Two thematic neighbours worth a glance before publication (different mechanism, cite-and-distinguish):
   Hinze "Monads from Comonads"; the Topos PLTL blog map `λ:MP→PI^op`.

— MacBeth
