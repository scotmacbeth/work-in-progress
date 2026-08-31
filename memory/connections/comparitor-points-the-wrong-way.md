# The comparitor points the wrong way — monoids ride it, comonoids cannot

**Found:** 2026-07-14 (dream), by colliding the day's PROVE result with the day's LEAN result.
**Status (updated 2026-07-15):** the transfer principle STANDS; the *degenerate-boundary conjecture*
below is **RESOLVED & REFUTED** — the boundary is **commutativity, not degeneracy**. Registry
`comparitor-comonoid-nogo` = **proved** (`proofs/2026-07-15-comparitor-double-comonoid.md`). Novelty
**audited** (`scratch/2026-07-15-comparitor-nogo-novelty-audit.md`): `Indep`/its iso-locus/the
⊗-comonoid "sets of monoids" fact are Spivak's; **MacBeth owns the Eckmann–Hilton reduction + the
corrected classification + the refutation.** See the boxed result in §"The sharp prediction — RESOLVED".

## The two facts that collided

1. **Thm C** (`proofs/2026-07-14-day-family-classification.md`, registry `comparitor-coreflection`):
   the comparitor `o_{p,q} : p ⊗ q → p ◁ q` is the **counit of a coreflection** —
   `p ⊗ − = Lan_J((p ◁ −)∘J)` along the representable embedding. So **`⊗` is the Day-ification of
   `◁`**: the terminal coproduct-preserving *approximation* to the sequential operator.
   *(The map itself is prior art — six statements; Spivak's `Indep`, arXiv:2202.00534 Eq. 32,
   derived from the `⊗`/`◁` duoidal interchange Eq. 29; Niu–Spivak `o_{p,q}` Ex. 6.85. The
   universal property is mine.)*
2. **M3** (`Comonoid.lean`, registry `m3-comonoid-forward`, `lean-verified`): a **directed container
   is a comonoid in `(Cont, ◁, I)`** — right counit = D3, left counit = D1+D2, coassoc = D4+D5.

Both units are `y`. So the identity functor carries a lax monoidal structure

> `Id : (Cont, ◁, y) ⟶ (Cont, ⊗, y)`,  structure map `φ_{A,B} = o_{A,B} : A ⊗ B ⟶ A ◁ B`

(the coherence of `φ` *is* the duoidal law, Spivak Eq. 29 — **check, don't assume**).

## The consequence, and it is asymmetric

Lax monoidal functors transport **monoids**. Oplax ones transport **comonoids**. We have lax only.

- **Monoids ride.** A monoid in `(Cont,◁,y)` is a **container/polynomial monad** `μ : A ◁ A → A`.
  Precompose with the comparitor: `A ⊗ A --o--> A ◁ A --μ--> A`. **Every container monad is a
  Dirichlet monoid.** Multiplication is a map *out of* the tensor, so an approximation *to* `◁`
  is exactly what you need.
- **Comonoids cannot.** A comonoid needs `δ : A → A ⊗ A`. Transporting M3's `δ : A → A ◁ A` would
  require `A ◁ A → A ⊗ A` — the comparitor **reversed**, and it is *not invertible*
  (machine-checked non-surjectivity: `y²⊗2` has 2 shapes, `y²◁2` has 4; registry
  `dirichlet-is-uniform-fragment-of-seq`).

> **The general lesson, and it is the reason this is a crown jewel:**
> **an approximation is a one-way street.** It lets you build maps *out of* a tensor and never
> *into* one. Whether a structure survives Day-ification is decided entirely by the *variance* of
> its structure map. Monoids multiply *inward*; comonoids emit *outward*; the comparitor has a
> direction; that single arrow decides both fates. This is why "`⊗` is the Day-ification of `◁`"
> is not a slogan but a *predictive* statement.

## The sharp prediction — RESOLVED (2026-07-15 PROVE)

The degeneracy conjecture I filed on 07-14 (survivors = `y^A` **or** `Ay`) was **FALSE in both
directions**, and the "the boundary is the two collapse points of the chain" story that made me
trust it was a decoy. **The Eq. 33 iso-locus was the wrong gate** — descent needs only the
constant-`j` image of `Indep`, not `Indep` invertible; the real obstruction sits one level deeper.

> **Theorem (double comonoids in the duoidal `(Poly, ◁, ⊗)`).** They are exactly the **sets of
> *commutative* monoids** — coproducts of one-object categories on commutative monoids. The
> `⊗`-comonoid structure is then **unique** (comultiplication = category composition).
> *Proof:* `⊗` lifts to `Cat#` as the product category (**Niu–Spivak Prop 8.79**); the counit +
> cofunctor codomain axiom force **every arrow to be an endomorphism** (a set of monoids); the
> cofunctor composition axiom makes each fibre map a homomorphism **from the product monoid**; and
> **Eckmann–Hilton** collapses it to `m = μ` with `M_I` **commutative**.
> `proofs/2026-07-15-comparitor-double-comonoid.md`.

**So the correct containment is `{degenerate} ⊊ {double comonoids} = {sets of commutative monoids}
⊊ {sets of monoids}`.** The old conjecture wrongly *admitted* `y^{S_3}` (needs the monoid
commutative) and wrongly *excluded* `2y² = {ℤ/2, ℤ/2}` (a perfectly good set of commutative
monoids). The `{sets of monoids}` right-hand class is the weaker "`δ^◁` factors through `Indep`"
condition; commutativity is the extra gate that transfer demands.

**The transfer principle itself (monoids ride, comonoids cannot) is untouched** — it is what makes
the *generic* directed container fail to descend. The refinement is only about *which* comonoids do
survive: not the degenerate ones, the **commutative** ones.

This is the **spine of the ⊗/◁ interaction section Neil requested** (email uid 53), and it answers a
concrete piece of **Niu–Spivak Ch. 9 Question 5** (`⊗`-comonoids in Poly). → [[day-family-classified]]

## Why this matters to the seed and the grant

It **joins Neil's two asks at a single point.** His Phase 1 is the four monoidal structures; his
Phase 2 is free monad / cofree comonad. This says the two phases *meet at the comparitor*: the free
**monad** (a ◁-monoid) passes to the Dirichlet world and the cofree **comonad** (a ◁-comonoid,
which is a directed container — [[free-cofree-containers-proved]]) does **not**. The monoidal census
stops being a list and starts *doing work*: it predicts which of the phase-2 objects survive
which tensor.

## Novelty audit — DONE (2026-07-15, `scratch/2026-07-15-comparitor-nogo-novelty-audit.md`)
Prior art (Spivak's, cite don't claim): `Indep` (arXiv:2202.00534 Eq. 32), its iso-locus (Eq. 33),
and the ⊗-comonoid "sets of monoids" classification. **MacBeth's delta:** the **Eckmann–Hilton
reduction** forcing commutativity, the **corrected classification** (sets of *commutative* monoids),
and the **refutation** of the degeneracy guess. The old "duoidal folklore might already have this"
worry was the right instinct — it *did* have the sets-of-monoids half; the commutativity gate is the
new piece.

Related: [[day-family-classified]], [[free-cofree-containers-proved]],
[[monoidal-coherence-four-structures]], [[circular-verification-and-reading-depth]].
