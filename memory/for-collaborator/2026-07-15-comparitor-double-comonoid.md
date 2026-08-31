# Double comonoids in (Poly, ◁, ⊗) = sets of COMMUTATIVE monoids — the target was wrong (2026-07-15)

**For Neil / Robin. Feeds the interaction section (email uid 53). PROVE session result.**

## One line
The PROVE target — "double comonoids in the duoidal `(Poly, ◁, ⊗)` are the degenerate polynomials
`y^A` or `Ay`" — is **false in both directions**. The correct theorem is:

> **A directed container is a double comonoid iff its underlying category is a coproduct of
> one-object categories on *commutative* monoids** (a *set of commutative monoids*), and then the
> `⊗`-comonoid structure is unique (comultiplication = category composition).

The gate is a **fibrewise Eckmann–Hilton collapse**, not the Eq. (33) invertibility locus.

## Why the target fails
- `y^A` is a double comonoid **iff `A` is commutative** — `y^{S_3}` is NOT one. (Target admits all.)
- Multi-object `2y² = {ℤ/2, ℤ/2}` IS a double comonoid. (Target excludes it.)
- So `{degenerate} ⊊ {double comonoids} = {sets of commutative monoids} ⊊ {sets of monoids}`.

## The three-line mechanism
1. **Structural (cited):** double comonoid = `⊗`-comonoid in `Cat# = Comon_◁(Poly)`, where `⊗` lifts
   to the **product of categories** (Niu–Spivak Prop 8.79; Aguiar–Mahajan comonoids-in-comonoids).
2. **Every arrow becomes an endo:** the counit forces `δ^⊗ : 𝓒 → 𝓒×𝓒` to be the diagonal on objects;
   the cofunctor cod-axiom then forces `cod(g) = I` for all arrows out of `I`. ⟹ **set of monoids.**
3. **Eckmann–Hilton:** the cofunctor composition axiom says the fibre map `m_I` is a monoid
   homomorphism **from the product monoid** `M_I × M_I → M_I`, sharing the unit with composition.
   Two unital ops, one a homomorphism of the other ⟹ `m_I = μ_I` and `M_I` **commutative**.

The same computation, read weakly (just "`δ^◁` factors through `Indep`"), gives *sets of monoids*
(any monoids). Commutativity is precisely the surcharge of the *full* double-comonoid axioms.

## Verified
Brute force over ℤ/2, ℤ/3, ℤ/4, V₄, min-monoid, `T_2`, `S_3`, order-3 left-zero: valid `m` exists
**iff** commutative, unique `m=μ`; associativity redundant. (One guardrail: the *same-pairing*
misreading of the interchange is a tautology — the crosswise/product grouping is the real one.)

## What I'd want your eyes on
The single load-bearing import is the standard duoidal fact in step 1 ("double comonoid = `⊗`-comonoid
internal to the `◁`-comonoids"). I cross-checked it by hand on `y^A` against the raw Aguiar–Mahajan
diagrams and it agrees, but if you know a slicker citation (or a reason it could fail for *normal*
duoidal with coinciding units) that's the place to push.

## Grant framing
This is a clean *interaction-of-two-tensors* theorem with a crisp slogan and an Eckmann–Hilton
punchline — good for the "compositional correctness has structure" narrative. It also models a
falsification done honestly: the audit said "only the converse is new"; the converse turned out to
refute the conjecture and hand back a better one.

Files: `proofs/2026-07-15-comparitor-double-comonoid.md`; registry
`proofs/registry/comparitor-comonoid-nogo.json` (validates, status `proved`).
