# Notebook — How far up the type hierarchy do stateful Workers go?

## Setup recap
Workers = (Set,×)-graded category, `Workers_S(p,q) = Cont(ΔS⊗p, q)`, ΔS=(S,s↦S)
codiscrete cat / store; ΔS⊗ΔT=Δ(S×T) strict (Lemma 3.1). Graded comonad S↦ΔS⊗(−).

Two candidate "monoidal descent" frameworks for an object-tensor ⋆∈{◁,⊗,×,+}:
- **(A) grade-multiplying / Para.** Tensor an S-worker with a T-worker → S×T-worker.
  Needs Φ^⋆: Δ(S×T)⊗(p⋆q) → (ΔS⊗p)⋆(ΔT⊗q). This is the *native* notion of a monoidal
  structure on a (Set,×)-graded category (tensor is a graded functor, grades combine by ×).
- **(B) shared-state / fixed-grade (diagonal).** Tensor two S-workers → S-worker (one shared
  register). Needs n^⋆_S: ΔS⊗(p⋆q) → (ΔS⊗p)⋆(ΔS⊗q), i.e. ΔS⊗(−) oplax monoidal for ⋆.
  = (A) precomposed with grade-diagonal S→S×S, then collapse S×S→S.

## Computational Evidence
All in `scratch/workers-type-hierarchy/`.

- **Framework A, existence & strictness of Φ^⋆** (`frameworkA.py`,`frameworkA_lhd.py`):
  - Φ^⊗ : **valid, ISO (strong)**.
  - Φ^× , Φ^+ , Φ^◁ : **valid, non-iso (oplax)**.
- **Framework A, INTERCHANGE law** for the Para tensor ⊗_W (`interchange_test.py`,
  256 tests each, multi-shape multi-position objects): **HOLDS for all four** ⊗,×,+,◁.
  ⟹ ⊗_W is a well-defined bifunctor on the graded category for every object-tensor.
- **Framework B, n^⋆_S** (`test_maps.py`): valid morphisms for all four; iso only for **+**
  (⊗ distributes over +, strict). counit coherence (`coherence.py`) holds for all four
  (both state-copies collapse to the current state at ε — so ε does NOT discriminate).
- **⊗ framework B needs a monoid** (hand + `bare-dirichlet-comonoid` classification):
  oplax structures on ΔS⊗(−) for ⊗ ↔ ⊗-comonoids on ΔS ↔ monoids on S; left/right unit
  law ⟺ e is a two-sided unit of the merge μ:S×S→S. No natural monoid on arbitrary S
  (∅ has none; for |S|≥3 the only bijection-equivariant μ are the projections, which have
  no unit). ⟹ ⊗ does NOT descend at fixed grade.
- **◁ framework B**: RHS position ((sp,b),(sq,d)) carries TWO independent states (outer sp,
  inner sq); LHS single state ⟹ backward must merge sp,sq → monoid, exactly as ⊗.
- **Closed structures** (`closed_probe.py`):
  - ⊗: ΔS⊗(r⊗p) ≅ (ΔS⊗r)⊗p (associator) ⟹ curry p out cleanly. **⊗-closed**, hom=[p,q]_⊗.
  - ×: |Work(r×p,q)| vs |Cont((ΔS⊗r)×p,q)| = 1296 vs 256, 5308416 vs 331776, 256 vs 16 —
    **DIFFER**. State entangles the product factor; naive CCC currying fails.

## Precise Statement (the theorem, graded honestly)
Framework A (grade-multiplying graded monoidal structure on Workers):
- ⊗ : **strong** monoidal graded category. PROVED (⊙ strong monoidal functor V×C→C).
- × : **oplax**. PROVED (cartesianness of (Set,×),(Cont,×) ⟹ ⊙ canonically oplax).
- + : **oplax** (framework A); **strict** at fixed grade (framework B). PROVED (⊗ cocont.)
- ◁ : **oplax**. COMPUTED (interchange verified; coherence via grade-cartesian projections).

Fixed-grade (shared register, framework B):
- + strict, × oplax (free); ⊗ & ◁ **obstructed** — require a monoid on the state S. PROVED (⊗).

Closed:
- ⊗ : **closed**, internal hom = Cont's [p,q]_⊗. PROVED.
- × , ◁ : **not closed** (state entanglement; count witness for ×). CONJECTURED + obstruction.

## The crown insight
Framework B = Framework A + grade-diagonal + collapse S×S→S. The collapse needs a monoid on
S **iff** the object-tensor forces the two state-copies onto the *same* position:
- +,× SEPARATE operands' positions (fibre Ba+Dc / summed) → each state stays with its operand
  → free (no monoid).
- ⊗,◁ MERGE positions (fibre Ba×Dc / nested) → the two states collide → monoid required.
Grade-multiplying (A) never collapses, so all four descend; ⊗ is strong there because its
fibre-product mirrors the ×-grade-product exactly. Closure follows the same fault line: state
curries past ⊗ (sits beside retained arg) but not past ×,◁ (lands on curried arg's positions).
