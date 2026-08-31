# The arity gap: why closure and counting cannot close it, and what a counterexample must be

MacBeth — 2026-07-24. Deep-work session (bounded attempt, per `state/PROVE.md` and Neil's
2026-07-22 steer: close Ch1–3; an honest *Further Work* is a full win). Continues
`2026-07-23-closed-convolutional-tensors-classification.md` (§6 gap) and
`2026-07-22-vacuity-resolved-collapse-tensor.md`. Registry: `closed-tensor-classification`,
node `gap-infinite-arities`.

## Verdict of the session

I did **not** close the gap, and I now believe it is a **genuine open problem**, not a
technicality — with meaningful probability that the conjecture is *false* (an infinite-arity
closed convolutional tensor may exist). What I *did* prove is a sharp explanation of why the gap
has resisted several sessions, and exactly what any resolution must engage:

1. **Reformulation (Lemma A).** "All arities `≤ 1`" (= `R_B` affine) is equivalent to
   "`R_B` preserves **connected colimits**." So the Main Theorem's missing step is:
   *every `R_B` preserves connected colimits.*
2. **The closure biconditional buys only limits (Prop B).** Left-closedness of `⊙_⋆` on `Cont`
   is equivalent to "`R_B` preserves connected **limits**" — and that is *all* it gives.
   Connected-limit and connected-colimit preservation are logically independent for polynomial
   functors. Hence there is no "free" colimit preservation to exploit; the bounded case was
   closed purely by the *cardinal* inequality `κ² > κ` (Prop 2 / Key Lemma), which is vacuous for
   infinite `κ`.
3. **Counting and the arity recursion provably cannot see the obstruction (Prop C).** The
   associativity-forced arity recursion is a *fixed point* at an infinite seed arity: the
   candidate `R_2 = y + y^λ` (`λ` infinite) propagates coherently to `R_{2⋆2} = y + 2^λ · y^λ`,
   with the associator iso `(X⋆2)⋆2 ≅ X⋆(2⋆2)` a genuine natural (in `X`) isomorphism of
   polynomial functors — *no* contradiction at the level of cardinalities, arities, or
   one-variable naturality. Any real obstruction must live in the *element-level* associator +
   pentagon coherence jointly in all variables (or there is none).

This corrects the earlier §6 heuristic ("conjectured killed by associator naturality"): in the
classification direction the associator is *given* and perfectly natural. The live question is
purely about a hypothetical *construction*.

---

## 1. Lemma A — affine = connected-colimit preservation

**Lemma A.** A polynomial functor `P = Σ_{i∈I} y^{A_i} : Set → Set` preserves connected colimits
iff every arity satisfies `|A_i| ≤ 1`.

*Proof.* `y^A = (−)^A` has left adjoint `A × (−)`, so it preserves all limits. For colimits:
- `A = ∅`: `y^∅ = 1` (constant); a connected colimit of a constant diagram is that constant, so
  preserved.
- `A = 1`: `y^1 = Id`; preserved.
- `|A| ≥ 2`: consider the pushout `2 = 1 +_∅ 1` (a connected diagram, apex span `1 ← ∅ → 1`).
  `y^A` sends it to `1 ← ∅ → 1` with pushout `2`, but `y^A(2) = 2^{|A|} ≥ 4 ≠ 2`. Not preserved.

Coproducts `Σ_I` commute with all colimits, and in the extensive category `Set` connected
colimits commute with coproducts, so `Σ_i y^{A_i}` preserves connected colimits iff each `y^{A_i}`
does, iff each `|A_i| ≤ 1`. ∎

Thus the Main Theorem's missing step "every `R_B` is affine" **is** "every `R_B` preserves
connected colimits." Together with the hypothesis (`R_B` polynomial = preserves connected limits),
the target is: *each `R_B` bipreserves connected limits and colimits.*

## 2. Prop B — the closure biconditional gives connected LIMITS only, and tightly

**Prop B.** For a Day-convolutional `⊙_⋆` on `Cont ≅ Fam(Set^op)`, left-closedness is equivalent
to "`R_B` preserves connected limits for all `B`", and unwinding the closure yields *exactly* this
— nothing about colimits.

*Proof sketch (the tight direction).* `(−) ⊙_⋆ y^B : Cont → Cont` has a right adjoint (closure),
so preserves all `Cont`-colimits. `Cont ≅ Fam(Set^op)` is the free coproduct completion of
`Set^op`; a **connected** colimit of representables `y^{X_j}` (`j ∈ J` connected) is computed in
`Set^op`: `colim_J^{Cont} y^{X_j} = y^{\lim_J^{Set} X_j}`. Since `(−)⊙_⋆y^B` acts on representables
as `y^X ↦ y^{X⋆B} = y^{R_B(X)}`,
```
  y^{R_B(lim_J X_j)} = (−)⊙_⋆y^B(colim_J y^{X_j}) = colim_J y^{R_B(X_j)} = y^{lim_J R_B(X_j)},
```
and `y` faithful gives `R_B(lim_J X_j) = lim_J R_B(X_j)` (connected `J`) = `R_B` preserves
connected limits. Non-connected colimits (coproducts in `Cont`) probe `R_B` only "shape-wise"
(`(y^{X_1}+y^{X_2})⊙_⋆y^B = y^{X_1⋆B} + y^{X_2⋆B}`), giving no interaction and no colimit
information about `R_B`. So closure ⟺ connected-limit preservation, and no more. ∎

**Consequence.** By Lemma A the target is connected-*colimit* preservation, which Prop B shows is
**not** implied by closure. For polynomial functors, connected-limit and connected-colimit
preservation are independent (e.g. `y^2` preserves the former, not the latter). The only lever
that forced affine in the bounded case was the cardinal count `κ² > κ`, which fails for infinite
`κ`. There is no categorical shortcut hiding in the closure hypothesis.

## 3. Prop C — cardinality and the arity recursion are blind to the gap

Work in the case `I = 1` (the `I = ∅` case is analogous; see §5). Here `1⋆B = B` is the index set
of `R_B`, `R_B(∅) = ∅⋆B = ∅` (all arities nonempty), `R_1 = Id`, so `A_{1,*} = 1`.
Associativity `R_B ∘ R_C ≅ R_{C⋆B}` forces, on the polynomial data, the **arity recursion**
```
  A_{C⋆B,\,(b,φ)} = Σ_{i ∈ A_{B,b}} A_{C,\,φ(i)},   b ∈ B,  φ : A_{B,b} → C = 1⋆C.   (R)
```

**Prop C.** The recursion (R), together with the unit seed `A_{1,*} = 1` and one-variable
naturality, is satisfied by an infinite seed arity, with no cardinality contradiction.

*Computation (`scratch/arity-gap/recursion_selfconsistency.py`).* Seed `R_2 = y^{a_0} + y^{a_1}`
(index set `1⋆2 = 2`). Then:
- **Finite seed `a_1 = n ≥ 2`:** (R) produces a composite arity `n²  >  n` (take `b=1`, `φ ≡ 1`),
  so degrees grow `n → n² → n⁴ → …` without bound. This *re-derives* Prop 2 / the Key Lemma:
  a finite arity `≥ 2` forces `κ = ∞`; a *finite* `κ` is contradicted. (Confirmed numerically:
  `(a_0,a_1)=(1,2)` gives composite arities `{1,2,3,4}`; `(1,3)` gives `{1,3,5,7,9}`.)
- **Infinite seed `a_1 = λ`:** every composite arity for `b=1` is `Σ_{i∈λ} A_{2,φ(i)} = λ`
  (sum of `λ`-many arities each `≥1`), and there are `2^λ` such `φ`. So
  `R_2 ∘ R_2 = R_{2⋆2}` has one arity-`1` index and `μ := 2^λ` arity-`λ` indices, i.e.
  `R_{2⋆2} = y + μ·y^λ`. This is a **fixed point**: `λ² = λ`, no growth, no contradiction.

Moreover the element-level associator is naturally iso *in `X`*: both
`(X⋆2)⋆2 = (X+X^λ)+(X+X^λ)^λ` and `X⋆(2⋆2) = X + μ·X^λ` equal `X + μ·y^λ(X)` as polynomial
functors of `X`, because `(X+X^λ)^λ = Σ_{f:λ→2} X^{|f^{-1}0| + λ·|f^{-1}1|} = μ·X^λ` (every
exponent collapses to `λ`). So naturality-in-one-variable, cardinality, and the arity recursion
are *all* satisfied. ∎

**Interpretation.** The three tools exhausted across prior sessions — degree growth (Prop 2),
constant-index counting, two-sided cardinality probes — are exactly the tools that (R) and Prop C
show to be blind. The obstruction to an infinite-arity tensor, *if it exists*, is a genuine
element-level coherence phenomenon (naturality of `α` jointly in all three variables + pentagon +
symmetry hexagon), invisible to cardinal bookkeeping. This is why the gap has been stubborn: it is
the first question in this program not decidable by counting.

## 4. Computational corroboration (this session)

Search agent, scripts in `scratch/arity-gap/` (`task1_*.py`, `task2_constructions.py`):

- **No finite/bounded arity-≥2 monoidal `⋆` exists**, reconfirmed *with the multiplication
  structure* (not only cardinalities): the only symmetric unital associative bivariate
  nonneg-integer polynomials are `a·b` (unit 1, `×`) and `a+b+s·ab` (unit 0, `∨_S`, `s=|S|`;
  verified for `s ≤ 11`); max per-variable degree `= 1` in every solution.
- Exhaustive over 376 finite commutative-monoid tables on `{0,1,2,3}`: **zero** columns are a
  genuine degree-≥2 polynomial functor (an `X²` shape forces `2⋆B ≥ 4`, off the table; naïve
  "arity-2" flags are value-capping artifacts that fail wide-pullback preservation, i.e. are not
  polynomial).
- Every explicit arity-2 deformation (`X+B+X²B+XB²`, `X+B+X²B²`, `X+B+XB+X²B²`, `X+B+(XB)²`) fails
  **cardinality-associativity at the smallest triple `(1,1,2)`** — so no subtle pentagon square is
  even reached; the obstruction bites earlier, exactly as Prop C predicts for *finite* arity.
- No unbounded/infinite construction survived {unit, symmetry, functor-associativity}: free monoid
  on `X+B` lacks a unit; `X×List(B)` is arity-1 but non-symmetric and non-associative;
  `X^{f(B)}` is not separately polynomial. **None was proven impossible.**

The data narrows any counterexample to: **infinite-valued on finite sets, non-jointly-polynomial,
with degree function `d(B) = sup_u |A_{B,u}|` an *unbounded* multiplicative homomorphism
`(Set,⋆) → (Card,·)` and per-column constant term `= B` (case `I=∅`).**

## 5. What a counterexample must be (Further Work statement for Ch3 §6)

A closed convolutional tensor outside `{⊗} ∪ {▷_S}` — equivalently a symmetric monoidal
`(Set,⋆,I)` with every `R_B` polynomial but some `|A_{B,u}| ≥ 2` — must satisfy **all** of:

1. `I ∈ {∅,1}` (Lemma 1, unaffected);
2. some arity infinite, `κ = sup_B d(B)` infinite (Key Lemma: finite `κ` ⟹ `κ ≤ 1`);
3. `d : (Set,⋆) → (Card,·,1)` a multiplicative homomorphism, unbounded (Prop 2);
4. each `R_B = Σ_{u∈1⋆B} y^{A_{B,u}}` preserving connected **limits** but *not* connected
   **colimits** (Lemma A + Prop B): `R_B` bipreserves neither;
5. arities generated by recursion (R) from an infinite seed — cardinally consistent (Prop C);
6. an element-level associator `α`, natural jointly in all variables, satisfying **pentagon**,
   **triangle**, and the symmetry **hexagon** — the sole remaining condition, and the only one
   *not* reducible to cardinality.

**The one square to check.** Fix the seed `R_2 = y + y^λ` (`λ` infinite). Cardinality, arities,
and one-variable naturality are all consistent (Prop C). The decisive test is whether the
associator `α_{X,2,2} : (X⋆2)⋆2 → X⋆(2⋆2)` can be chosen *simultaneously* natural in `X` **and**
in the two `2`-slots (functoriality of `⋆` in all arguments) while satisfying the **pentagon**
`α_{X,2,2}` ⋈ `α_{X⋆2,2,2}` … — an infinite element-level coherence not settled here. Either it
can (counterexample: the classification is genuinely *bounded-arity only*), or pentagon obstructs
it (gap closed). **This is the precise next target; it is a coherence computation, not a counting
one.**

## 6. Grade discipline

- `proved` (new this session): Lemma A (affine = connected-colimit preservation); Prop B (closure
  ⟺ connected-limit preservation, tight); Prop C (arity recursion self-consistent at infinite
  seed — cardinality/recursion/one-variable-naturality cannot obstruct).
- `computed`: the finite reconfirmation and construction attempts (§4).
- `conjecture` / **open**: `gap-infinite-arities` remains open. The Main Theorem stands
  **unconditionally on the uniformly-bounded-arity locus** (which contains every `×` and every
  `∨_S`, so the conclusion families are complete); exhaustiveness against infinite-arity
  structures is the open problem, now sharply characterized (§5). No proof was manufactured.

## 7. Provenance / novelty

- Lemma A (linear = connected-colimit-preserving polynomial functors) is essentially folklore in
  polynomial-functor theory; stated here for the reframing, not claimed as new.
- Prop B (closure ⟺ connected-limit preservation) is the 2026-07-15 biconditional read through the
  free-coproduct-completion structure of `Cont`; the *tightness* observation (limits, never
  colimits) is the useful new emphasis.
- Prop C (infinite-arity fixed point of the arity recursion; the `R_2 = y+y^λ` witness) is new and
  is the session's main contribution: it *proves* that the multi-session stuckness is structural,
  not a missing trick — cardinality methods are provably insufficient.
