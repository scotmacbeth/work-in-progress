# DRAFT — The Day family on Poly, and the unique pointwise member

Working notes, 2026-07-14. Structure of the argument before I write it properly.

## The one idea

**Poly = Fam(Set^op), the free coproduct completion of Set^op.**

Everything follows. A container (S,P) *is* a family (P s)_{s∈S} of sets; a container
morphism (f, g) *is* a morphism of families in Set^op. Poly ≅ Fam(Set^op) on the nose,
not up to anything.

Free coproduct completion ⟹ a tensor on Poly preserving coproducts in each variable is
determined by what it does to corepresentables. Day convolution *is* that determination.
So:

    p ⊙_⋆ q  :=  ( S_p × S_q ,  (s,t) ↦ p[s] ⋆ q[t] )

Shapes always multiply. **The choice of monoidal structure on Set only ever shows up in
the positions.** That is the sentence.

    ⋆ = (+, ∅)   ↦  the categorical product ×   (positions p[s] + q[t])
    ⋆ = (×, 1)   ↦  the Dirichlet tensor ⊗      (positions p[s] × q[t])

## The two conditions

(D1) preserves coproducts in each variable
(D2) corepresentables closed under ⊙, and J corepresentable

Day ⟺ (D1) ∧ (D2).

Now look at Neil's four:

| structure | (D1) | (D2) | Day? |
|---|---|---|---|
| ×  | ✓ | ✓ | yes, of (+,∅) |
| ⊗  | ✓ | ✓ | yes, of (×,1) |
| +  | ✓ | ✗ (y^A + y^B has 2 shapes; unit 0 has 0 shapes) | no |
| ◁  | ✗ (right variable) | ✓ (y^A ◁ y^B = y^{A×B}, unit y) | no |

**The two non-Day structures fail *complementary* conditions.** That is the taxonomy.

And — the kicker — ◁ and ⊗ have the SAME restriction to corepresentables: both give
A × B, both have unit y. So ⊗ is the (D1)-completion of ◁. **dirToSeq is the counit of
that completion.** Theorem 2 falls out of Theorem A.

## Theorem 1

Pointwise := natural iso p ⊙ q ≅ p × q (naturally in p,q).

**TFAE:** (1) ⊙_⋆ pointwise; (2) ⋆ ≅ + as bifunctors; (3) (⋆,I) ≅ (+,∅) monoidally;
(4) ⊙_⋆ ≅ × monoidally.

Proof sketch:
- (1)⟹(2): restrict to corepresentables. y^A ⊙_⋆ y^B = y^{A⋆B}; y^A × y^B = y^{A+B};
  Yoneda (y^(−) : Set^op → Poly f.f.) gives A ⋆ B ≅ A + B naturally.
- (2)⟹(3): **rigidity of +.** Transport the monoidal structure along the iso; then show
  the coproduct admits *exactly one* natural associator. Nat(Id,Id) on Set is trivial,
  and a natural map out of a coproduct is its components ⟹ associator is forced.
  Unit: I ⋆ A ≅ A and ≅ I + A ⟹ I + 1 ≅ 1 ⟹ I = ∅.
- (3)⟹(4)⟹(1): formal.

### The unit already kills Dirichlet
Pointwise ⟹ ⟦J⟧X × ⟦p⟧X ≅ ⟦p⟧X. Put p = y: ⟦J⟧X × X ≅ X. At X=2: 2^{|J[*]|}·2 = 2 ⟹
J[*] = ∅ ⟹ J = y^∅ = 1 ⟹ I = ∅. Dirichlet's unit is y ≠ 1. One line.

**But** — see below — the ∨_S family ALL have unit ∅. So the unit is not enough in
general. Need κ.

## Theorem 1′ — the effective test

Any monoidal (⋆, I) on Set with **I initial** has a canonical natural map

    κ_{A,B} : A + B → A ⋆ B,   κ|_A = (A ≅ A⋆∅ → A⋆B),  κ|_B = (B ≅ ∅⋆B → A⋆B).

**⊙_⋆ is pointwise ⟺ I ≅ ∅ and κ is a bijection.**

This is the *test*. It computes.

## The family is a proper class (and unit-blind)

Spivak: A ∨_S B := A + A×S×B + B, unit ∅. Monoidal (normal form: the n-fold tensor is
⊔_{∅≠K⊆[n]} (Π_{i∈K} X_i) × S^{|K|−1} — strictly increasing subsequences with S-separators
— and every bracketing maps canonically onto it, so pentagon = id on the normal form).

- κ_{A,B} : A + B ↪ A + A×S×B + B is the inclusion of the outer two summands.
- Bijective ⟺ A×S×B = ∅ for all A,B ⟺ **S = ∅**.
- |1 ∨_S 1| = |S| + 2, so the ∨_S are pairwise non-isomorphic. A proper class.
- **Every ∨_S has unit ∅.** So every ⊙_{∨_S} has unit y^∅ = 1 — the SAME unit as the
  product. The unit invariant sees nothing. κ does all the work.

∨_∅ = +. So: a proper class of Day tensors on Poly, all sharing the product's unit,
**exactly one of which is the product.**

## Theorem 2 — dirToSeq is a coreflection

J : Set^op ↪ Poly the corepresentable inclusion. Fix C.

    C ⊗ −  ≅  Lan_J ( (C ◁ −) ∘ J )

because C ◁ y^B = C ⊗ y^B (both = Σ_s y^{C[s] × B}), and Lan along J into Poly is
"extend by coproducts". **dirToSeq is the counit of Lan_J ⊣ res_J.**

Universal property: for every coproduct-preserving F : Poly → Poly,

    (dirToSeq ∘ −) : Nat(F, C ⊗ −)  ≅  Nat(F, C ◁ −).

So **C ⊗ − is the coreflection of C ◁ − into coproduct-preserving endofunctors** —
the terminal coproduct-preserving approximation. This is the precise sense of "the
non-dependent part".

Slogan: **coproduct-preservation in the second variable = non-dependence of the inner
shape on the outer position.** In C ◁ D a shape is (s, f : C[s] → S_D); in C ⊗ D the f
is constant. dirToSeq is "include the constants".

### The counit is neither mono nor epi
- NOT surjective on shapes: dependent f's are unreachable. (⊗ has no dependency.)
- NOT injective either! C = 1 = y^∅ (one shape, no positions): 1 ⊗ D = S_D · y^∅ =
  const S_D, but 1 ◁ D = const 1. All the t's collapse. **When the outer shape has no
  positions, ◁ cannot see the inner choice but ⊗ still records it.**
  (PROVE.md only noted non-surjectivity. Non-injectivity is the other half.)

### Exactly when is dirToSeq iso?
Positions map is always a bijection (identity). So iso ⟺ shape map bijective ⟺
for every s ∈ S_C, const : S_D → S_D^{C[s]} is a bijection. Hence:

**dirToSeq_{C,D} iso ⟺ every C[s] is a singleton (C linear, C ≅ S·y), or D has exactly
one shape (D corepresentable).**

"A linear outer shape has exactly one position, so there is nothing for the inner shape
to depend on."

### Id is oplax monoidal
dirToSeq makes id_Poly an **oplax monoidal functor** (Poly, ⊗, y) → (Poly, ◁, y).
Both have unit y. Checked on the triple: (a⊗b)⊗c → (a◁b)◁c is (x,y,z) ↦ (x, const y,
const z), positions identity, same for both bracketings.

## What this closes

The dead-end node `dirichlet-strict-monoidal` said: "⟦–⟧ is strict monoidal for ⊗" —
category error. Theorem 1 explains the error *structurally*: ⟦–⟧ : (Poly, ⊙) →
([Set,Set], ×_ptwise) is strong monoidal **iff ⊙ = ×**. Dirichlet could never have done
it. The failure was forced, not accidental.

## TODO
- [ ] audit: is Thm 1 in Niu–Spivak? is ⊗ → ◁ in the duoidal paper?
- [ ] computation: pentagon for ∨_S elementwise
- [ ] size hypothesis: coend over Set is large — but Fam is a free construction, no coend
      needed. **The size worry in PROVE.md dissolves: I never form a coend.** Good.
</content>
