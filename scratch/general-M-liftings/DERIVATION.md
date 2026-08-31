# State liftings — derivation (MacBeth, 2026-08-10 PROVE)

Target: classify polynomial fibred monad liftings of **State** `M=(S^S, S)` along `cod:Cont→Set`.

## 0. The reduction (Prop A′, proved 08-09)

Lifting ↔ family `(A_t : Set^S → Set)_{t∈S^S}`, one aggregator per shape (endofunction).
`L(S0,P)=(⟦M⟧S0, P̃)`, over `(t,x)∈⟦M⟧S0` (`x:S→S0`), `P̃(t,x)=A_t(P∘x)`.

## 1. Unit and multiplication (unwound at the generic object)

**Unit** over `η_M(s0)=(id, const_{s0})`:
  counit `ε : A_id(⟨V⟩) → V`, natural in V.  ONLY `A_id` gets a counit.

**Mult** over `μ_M`. With outer next-state `T∈S^S`, inner next-states `(t_s)_{s∈S}`,
  composite shape `σ(s)=t_s(T(s))`, and the position-reading `z(s)=x_s(T(s))`.
  Introduce `D:S×S→Set`, `D(s,r)=P(x_s(r))`. Then `P∘x_s=D(s,-)`, `P∘z=s↦D(s,T(s))`.
  Comultiplication = family (one per `(T,(t_s))`) of natural transformations in `D`:
```
    δ_{T,(t_s)} : A_σ( s↦D(s,T(s)) )  ⟶  A_T( s↦ A_{t_s}(D(s,-)) ),   σ(s)=t_s(T(s)).
```

### Σ = State◁− check.  A_t(Q)=∐_{s∈S}Q_s  for all t.  ε=fold; δ:(s,d)↦(s,T(s),d). ✓

## 2. Purity is forced

Write `A_t(Q)=∐_{j∈J_t} ∏_{r} Q_r^{n_t(j,r)}`, object `j` positions at state r: `n_t(j,r)`.

**(Inner purity, from naturality of δ.)**  Matching D-arguments naturally forces every RHS
position to read `D(s,T(s))`, i.e. inner objects `k` picked by δ have `n_{t_s}(k,r)=0` for
`r≠T(s)`: **inner objects are pure at T(s)**.  [Reader Step B analogue.]

**(Full purity, from LU.)**  LU = `μ^T∘η^T T`: outer `T=id`, outer object a unit object of `A_id`.
`σ(s)=t_s(s)`. δ decomposes `j∈J_σ`, outer counit selects marked position `e(j0)` at state
`s*=λ(j0)`, returns the single inner object at that slot, pure at `s*`; equality with id forces
that inner `= j`. Hence **`j` is pure at `s*=:ρ(j)`**.  Every object reads a single source state.

⟹ post-purity: `A_t(Q)=∐_{j∈J_t} Q_{ρ(j)}^{deg(j)}`, object `j` = (grade t, source ρ(j)∈S,
   deg(j) out-positions all at state ρ(j)); target τ(j)=t(ρ(j)).

## 3. Threading = composition in the action category 𝕊

`𝕊` := action category of the transformation monoid `S^S ↷ S`:
  objects S; morphisms `s→s'` = `{u∈S^S : u(s)=s'}`; comp `(u:s→s',v:s'→s'')↦v∘u`; id = `id_{S^S}`.

Threading `σ(s)=t_s(T(s))`: at source `s`, outer `T` is the morphism `s→T(s)`, inner `t_s` is
`T(s)→t_s(T(s))=σ(s)`; composite `t_s∘T : s→σ(s)`. **The shape threading is 𝕊-composition,
position by position.**  (Reader = `S_M=1`: `𝕊 = E_disc`, recovering E-indexed families.)

## 4. The candidate object (to be pinned by computation)

Post-purity, an object `j` is a "morphism-carrier" at `(source ρ(j), grade t)` with target `t(ρ(j))`,
i.e. it sits over the 𝕊-morphism `[t]_{ρ(j)}: ρ(j)→t(ρ(j))`. Comult = composition. Candidate:

  **liftings of State ↔ small categories 𝔻 with a functor 𝔻→𝕊 (+ fibration/discreteness cond).**

OPEN QUESTIONS to resolve by computing at |S|=2 (𝕊 = action cat of the 4-elt monoid S^S on 2 pts):
  (Q1) Is purity really forced?  — YES (LU), + inner-purity (naturality).
  (Q2) Does grade-redundancy collapse?  — see RESULT.
  (Q3) Fibration condition on 𝔻→𝕊?  — see RESULT.
  (Q4) Count liftings vs candidates.  — see RESULT.

## RESULT (computed, 2026-08-10). The threading is HOLONOMY-FREE; the grading COLLAPSES.

The naive "category over 𝕊 / discrete Conduché fibration" guess is **REFUTED**:
  * Σ = 𝕊 (identity functor) lifts (honest engine, all 3 laws).      [scratch honest.py]
  * 𝕊×C lifts for EVERY small category C — Z/2, Z/3, AND-monoid, walking-arrow, disc-3
    (units + certified sampling-assoc lean_assoc.py, cross-validated vs honest engine).
  * At profile [(2,0),(0,2)] (one object/state, degree 2) the liftings biject with the
    **4 monoids on 2 elements** — identical mechanism to Reader's B_0²→4.
  * REFUTED: ANY nontrivial 𝕊-action breaks associativity — representable copresheaves
    𝕊(0,-),𝕊(1,-), their sum, and a twisted constant action ALL fail assoc; only the
    TRIVIAL (constant-fibre = product) action survives.  [copresheaf.py]
  * REFUTED: per-state-different fibres cannot route across states (𝕊 is connected /
    S^S acts transitively on S), so a single GLOBAL C is forced.  [product_SxC.py]
  * Localising a category to one state (vertical-only) fails: the everywhere-defined
    condition forces filling every grade.  [honest probe]

CONJECTURE (strongly evidenced; completeness OPEN): the polynomial monad liftings of State
are exactly {𝕊×C : C a small category}, i.e. **State liftings ≅ Cat**.  The transformation
monoid S^S contributes ONLY its connectivity: S is ONE orbit ⟹ ONE global category, versus
Reader's E = π_0(E_disc) independent fibre-categories.  Unifying (conj.):
   liftings of M  ↔  (orbits of the position-threading)-indexed families of small categories,
with TRIVIAL transport (holonomy-free).  The predicted "finer" object is in fact COARSER —
the grading collapses.  This is the 8th-instance meta-pattern with the sign flipped.
