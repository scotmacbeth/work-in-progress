# The Σ-lifting IS `M ◁ −` — container monads are the ◁-monoid partner of directed containers

**Crown of 2026-08-08 (PROVE).** The proof-relevant Σ-container lifting of a base monad `M`,
which I spent 08-07 verifying (in heavy coordinates) is a genuine monad for Reader and State,
turns out to be **left composition-multiplication by the container `M`**:

> **`T^Σ_M(C) = M ◁ C`** (left ◁-product). Hence `T^Σ_M` is a monad on `Cont` **iff `M` is a
> ◁-monoid in `(Cont, ◁, y)` = a *container monad***.

Proof `proofs/2026-08-08-sigma-monad-is-triangle-monoid.md`; node
`reverse-total-implies-coherent-section-OPEN` → **REFUTED**; collaborator note
`for-collaborator/2026-08-08-sigma-monad-is-triangle-monoid.md`.

## Why this is a crown jewel (bridges the whole grant spine)

The 08-07 ℤ/2 grading said the **Σ side survives** where the ∏ side (`T_M`, Ahman–Bauer) dies —
Reader/State DO have a proof-relevant monad lifting, the Σ one. But *why*, and *which* monads?
This cycle answers both with an **identity of endofunctors**, not a coincidence of sections:

- **Directed containers = ◁-*comonoids*** (the AU equivalence, grant Path 2).
- **Container monads = ◁-*monoids*** — the exact dual partner.
- Reader (= diagonal comonoid on `E`) and State (= store monad) are the two motivating ◁-monoids.

So the surviving half of the proof-relevance boundary is **not** off in some exotic corner — it
lands *precisely* on the composition-monoid spine the grant already runs on. The mysterious
"canonical section" `σ` of 08-07 is just `μ_M`'s backward position map; the three coherence
conditions (U1),(U2),(A) are the ◁-monoid unit/associativity laws read on positions — automatic
for any container monad. The 08-07 Reader/State proof is now *an example of a theorem*.

Mechanism of the identity: shapes of `T^Σ_M(S,P)` are `MS` (= `M` on the shape set); positions
`∐_{b∈lv(m)} P(x_b)` are exactly the composite-polynomial positions of `M ◁ (S,P)`; unit/mult are
`η_M ◁ (−)`, `μ_M ◁ (−)`. Via `Cont ≃ Poly ↪ [Set,Set]` (fully faithful, strong monoidal, `◁↦∘`),
"`A⊗−` is a monad ⟺ `A` is a monoid" specializes to the claim. The 08-07 "reduction lemma / Σ
faithful" was the shadow of this full faithfulness.

## The refutation — Bag — and why it recycles a July discriminator

`reverse-total ⟹ Σ-monad` is **FALSE**. Bag (finite multiset monad) is reverse-total in the
strongest way (`μ = union` is a leaf-*bijection*, `σ = id`), yet `T^Σ_Bag` is **not even a functor
on `Cont`**, because **Bag is not a container**: it fails the connected pullback `A→1←B`
(`|Bag(2×2)|₂ = 10 ≠ 9`; `{(0,0),(1,1)}` vs `{(0,1),(1,0)}` collide — Bag forgets the pairing).
`scratch/sigma-monad-coherence/bag_not_container.py` (List, a real container, passes via zip).

Community corroboration: **MO 302631**, Lumsdaine's accepted answer proves Bag is not polynomial by
the *same* pullback-non-preservation (Makkai–Zawadowski, Simpson cited); the second answer notes Bag
*is* polynomial over **groupoids** (Fiore et al., "Data Types with Symmetries and Polynomial
Functors over Groupoids") — the `Sₙ` symmetry is the obstruction, and it's exactly *analytic*.

**This recycles the July slogan [[polynomiality-is-provenance-is-coherence]]:** the real content
over reverse-total is **polynomial, not merely analytic**. reverse-total = the *pointwise / analytic*
shadow ("`μ_M` has *some* backward map"); ◁-monoid = the *coherent / polynomial* fact ("the backward
map is natural and unital/associative"). So:

> **reverse-total : ◁-monoid  ::  analytic : polynomial  ::  provenance-forgetting : provenance-tracking.**

Bag forgets which input each output element came from (no natural leaf assignment) — the precise way
a functor "loses provenance" that the July note said every monoidal axiom kills. Here it kills
functoriality of `T^Σ_Bag`.

## Both legs of the codomain fibration now have clean criteria

The codomain/`Cont` fibration (the non-thin, proof-relevant side, [[proof-relevance-is-the-fibration-flip]])
carries **two** leaf-liftings of `M`, and each now has a crisp lift-criterion:

| leaf-lifting | is a monad on `Cont` ⟺ | totality direction |
|---|---|---|
| `∏` (`T_M`, Ahman–Bauer) | `M` **cartesian** (forward-total `κ_μ`) | forward |
| `Σ` (`T^Σ_M = M◁−`) | `M` a **◁-monoid / container monad** | reverse |

Symmetry worth noting: cartesian ⊊ container-monad in general (List is both; but the criteria are
*independent* axes — cartesian is about `μ` merging leaves, ◁-monoid is about polynomial coherence
of `μ`'s backward map). Reader/State are container monads but non-cartesian ⟹ Σ-lift, no ∏-lift.

## The field only builds tools for the OTHER (thin) fibration

08-08 browse: **three independent literatures** confirm classical predicate/relation-lifting
technology (Hermida–Jacobs style) is structurally confined to **thin/faithful** fibrations —
- **Urbat**, "Higher-Order Behavioural Conformances via Fibrations", arXiv:2507.18509 (POPL 2026):
  CLat⊓-fibrations are **provably faithful** (Lemma 5.2(1)); grepped, zero `Cont`/proof-relevant hits.
- **Goncharov–Milius–Schröder–Tsampas–Urbat**, "Bialgebraic Reasoning on Stateful Languages",
  arXiv:2503.10955: Reader/Writer split, no proof-relevant fibration content.
- **Orestis's Agda** ([[orestis-agda-corroborates-drop-boundary]]): all-`Type`-valued but routes
  every drop-monad example through `∃`/`◇` (the thin/Σ side).

Thinness is *what makes a fibration propositional* in exactly my sense — so the classical literature
(built for logical relations / behavioural conformances, which *want* thin) never crosses to the
proof-relevant `T_M`/`Cont` side. **MacBeth's contribution is naming and proving the boundary at the
non-thin side** — and now (08-08) *both legs* of that non-thin side have monad-lift criteria
(cartesian for ∏, ◁-monoid for Σ). Book Ch7 remark candidate.

## Meta-pattern, 6th instance (now a reliable signal)

Conjecture a clean implication (`reverse-total ⟹ Σ-monad`); the structure hands back a finer
distinction (◁-monoid = polynomial, refuted by Bag). Prior five:
07-31 Atkey-graded→Boolean; 08-05 crown-TFAE→4-rung ladder; 08-06 census→trichotomy;
08-07 "no lifting"→ℤ/2 2×2; and the underlying free/generative-constructions-merge theme
([[fibration-stratifies-monad-zoo]]). **"Fair is foul"** — pre-plan the expository retreat every
time I conjecture a flat equivalence on this territory.

## Grant / book placement

- **Book Ch7** (asked Neil): lead with `T^Σ_M = M◁−`, present the 08-07 Reader/State proof as the
  ◁-monoid special case — shortens the chapter substantially.
- **Grant Path 2**: the surviving-Σ-lifting is *literally* the ◁-monoid partner of directed
  containers, welding the proof-relevance story to the composition-monoid spine as an identity.
- **LEAN next**: state `T^Σ_M = M◁−` + "◁-monoid ⟹ Σ-monad" once; Reader/State (both already
  Lean'd axiom-free, `reader_sigma_*`/`state_sigma_*`) become corollaries.

Links: [[polynomiality-is-provenance-is-coherence]] · [[proof-relevance-is-the-fibration-flip]] ·
[[fibration-stratifies-monad-zoo]] · [[orestis-agda-corroborates-drop-boundary]] ·
[[reader-state-outside-pi-mendler]] · [[position-op-turns-monads-into-comonads]]
