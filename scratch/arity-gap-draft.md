# Arity-gap working notes — 2026-07-24

## The reframing (robust, independent of the search)

**Lemma (affine = connected-colimit-preservation).** A polynomial functor
`P = Σ_{i∈I} y^{A_i} : Set → Set` preserves connected colimits **iff** every arity
`A_i` has `|A_i| ≤ 1`. (So "affine" = "linear" = "arity ≤ 1" = "preserves connected colimits".)

*Proof.* `y^A = (−)^A` has left adjoint `A×(−)`, so preserves all limits; it preserves
connected colimits iff `A ≤ 1`: for `A=∅` it is constant `1` (preserves connected colimits,
a connected colimit of a constant diagram is that constant); `A=1` it is `Id`; for `|A|≥2`
it fails the pushout `2 = 1 +_∅ 1` (a connected diagram), since `2^A = |A|... ` `> 2`.
Coproducts `Σ_I` commute with all colimits, and connected colimits commute with coproducts
in the extensive category Set, so `Σ_i y^{A_i}` preserves connected colimits iff each `y^{A_i}`
does, iff each `A_i ≤ 1`. ∎

So the target theorem "every `R_B` is affine" is exactly "every `R_B` preserves connected
**colimits**."

**The closure biconditional buys only LIMITS.** The 2026-07-15 biconditional says
`(Cont, ⊙_⋆)` left-closed ⟺ `R_B` polynomial ⟺ `R_B` preserves connected **limits**, for all B.
And this is *tight*: unwinding closure gives exactly limit-preservation, nothing about colimits.

Explicitly: `(−) ⊙_⋆ y^B : Cont → Cont` has a right adjoint (closure), so preserves Cont-colimits.
Cont ≅ Fam(Set^op) is the free coproduct completion of Set^op; a **connected** colimit of
representables `y^{X_j}` (j∈ connected J) is computed in Set^op, i.e.
`colim_J^{Cont} y^{X_j} = y^{lim_J^{Set} X_j}`. Applying `(−)⊙_⋆ y^B` (which acts as
`y^X ↦ y^{X⋆B} = y^{R_B(X)}`) and using colimit-preservation:
```
  y^{R_B(lim_J X_j)} = (−)⊙_⋆y^B(colim_J y^{X_j}) = colim_J y^{R_B(X_j)} = y^{lim_J R_B(X_j)}.
```
y faithful ⟹ `R_B(lim_J X_j) = lim_J R_B(X_j)` (connected J) = **R_B preserves connected limits**.
That is all closure gives. It says nothing about `R_B` preserving connected *colimits* (= affine).

**Consequence — why the gap is genuinely hard.** Connected-limit and connected-colimit
preservation are logically independent conditions on a polynomial functor. The ONLY thing that
forced affine in the bounded case was the *cardinal* counting of Prop 2 + Key Lemma
(`κ² > κ`), which evaporates for infinite κ. There is no "free" colimit preservation to exploit:
the monoidal closure gives limits only. So closing the gap requires showing that symmetric
monoidal coherence *itself* forces connected-colimit preservation — a genuinely different lever
than the ones tried.

This corrects the earlier §6 story ("conjectured killed by associator naturality"): the associator
IS given (⋆ is monoidal by hypothesis) and is perfectly natural — no contradiction arises there in
the classification direction. The real question is the coherence *of a hypothetical construction*.

## The associativity recursion (shape of any counterexample), case I=1

For I=1: `1⋆B = B` (index set of R_B is B), `R_B(∅)=∅⋆B=∅` (all arities nonempty),
`R_1 = Id`. Associativity `R_B∘R_C ≅ R_{C⋆B}` forces, on arities:
```
  A_{C⋆B, (b,φ)} = Σ_{i ∈ A_{B,b}} A_{C, φ(i)},     b∈B=1⋆B, φ: A_{B,b} → C = 1⋆C.
```
Seeded by `A_{1,*}=1`. For `× `: `A_{B,b}=1` ∀b. A hypothetical infinite-arity example needs
some `A_{2,u}` infinite; then `2⋆2 = 2^{A_{2,0}}+2^{A_{2,1}}` is INFINITE, so any counterexample
is infinite-valued on finite sets. The recursion is cardinally self-consistent for infinite
arities (Σ over an infinite index of infinite arities stays that cardinal); the open question is
whether a *natural, functorial, pentagon-coherent* such assignment exists.

## Honest status of the finite classification (§7)
`cardinality-classification.py` is a genuine SymPy solve, but only over **bounded total degree**
D≤4. Under symmetry, bounded joint degree = bounded arity = exactly the Key Lemma's hypothesis.
So §7 is the finite *shadow* of the Key Lemma and adds nothing beyond it; it does NOT reach the
unbounded/infinite-arity gap. (Corrects any impression that §7 independently narrows the gap.)
