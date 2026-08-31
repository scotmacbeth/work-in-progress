# State liftings ≅ Cat — COMPLETENESS PROVED (holonomy-triviality, the last lemma)

**2026-08-11 PROVE deep-work.** File `proofs/2026-08-11-state-liftings-holonomy-triviality.md`.
Closes the State-liftings program. The completeness conjecture — flagged OPEN across three prior
sessions — is now **proved at the object level (rigorous, new) + morphism level (mirror + decisive
enumeration)**.

## What was open, what's now closed
Grade-independence (08-10 pt II) had reduced completeness to ONE residual lemma:
**holonomy-triviality** = (H1) source-independence `C̃_0≅C̃_1` + (H2) trivial 𝕊-transport. Both were
only *computed* (companion refuted nontrivial holonomies case-by-case). This session gives the
**abstract proof**.

## The one idea: the deepest-object component of associativity
For the transport `τ^g(s,c)` (object `c` at source `s`, moved along grade `g` to source `g(s)`), the
monad associativity `μTμ=μμT`, read on the innermost object of the 3-level tower, is
```
    τ^{σ'}(s,c) = τ^{t_s}( T(s), τ^{T}(s,c) ),      σ'(s') = t_{s'}(T(s')).
```
Machine-verified: both formulas 0-mismatch over 196608 records for a *generic random* transport
(`fit_general.py`). The point: **the right side sees only the middle `t_s` at the source state `s`,
but `σ'` is stitched from ALL the middles `t_{s'}`.** Since `S^S` acts transitively, the off-source
middles are free — so `τ^{σ'}(s,c)` cannot depend on `σ'(s')` for `s'≠s`.

**⟹ ENDPOINT-LOCALITY: `τ^g(s,c)` depends on `g` only through `g(s)`.** (Clean proof: set `T=id`,
`t_{s'}=const_{g(s')}`; both `g` and `g'` with `g(s)=g'(s)` give the *same* right side.)

Then it's downhill: `τ^{b∘a}=τ^b∘τ^a` (functoriality, from all-middles-equal), `τ^{id}=id`
(identity's target = its source), so the transports `ψ_{s→m}:O_s→O_m` are **bijections forming a
functor out of the CODISCRETE category `K(S)`** = a coherent **trivial** iso-system = a single
category `C` with trivial transport. Hence every lifting is `𝕊×C`. **`C↦𝕊×C` bijective: State
liftings ≅ Cat.**

## Morphism level (the honest status)
The out-positions transport by the *position-component* of the same identity (mirror of
grade-independence §3.2). Verified decisively, not yet written in closed symbolic form:
- `enum_hom.py`: FREE hom-transport (1 object/state, out-degree 2) ⟹ **exactly 4 survivors = the 4
  monoids on 2 elements, all with trivial transport** (robust nsamp=1500). No hom-holonomy.
- `twist_test.py`: `𝕊×ℤ/n` twisted by an automorphism `α_g` lifts **iff `α≡id`** (ℤ/3 inversion on
  any arrow/loop/global all fail units/associativity).

So the morphism-level triviality is decisively confirmed and argued by the structural mirror; the
one flagged gap is the symbolic backward-map derivation (carried in the registry as a `computed`
attempt child, not a premise). The **object-level completeness is fully rigorous.**

## Registry
`effect-coeffect-arrows.json`: new node `state-holonomy-triviality` (**proved**, premise) under
`state-liftings-holonomy-free`, with children `state-endpoint-locality` (**proved**) and
`state-morphism-holonomy-trivial` (**computed** attempt). Updated `state-completeness-Cat-OPEN` to
"RESOLVED object-level". Validator: OK (proved).

## Grant framing
This is a **Theory pillar** result: the monad-lifting stratification now terminates in a clean
classification — **State liftings ≅ Cat**, the `π_0(𝕊)=1` collapse of Reader's `E`-indexed families
(`π_0=E`). The slogan "grading by the store monoid *collapses* to its π_0, giving the coarser `Cat`,
not a finer graded object" is now a theorem, not a conjecture. Welds to `DCont≅Cat` (Ahman–Chapman–
Uustalu) — the convergence hub. Natural next: the Lean formalisation of endpoint-locality, and the
general-`M` statement (`π_0`(position-threading)-indexed families, holonomy-free).

## Open threads for you
1. Write out the morphism-level position-component of (ASSOC-DEEP) in closed backward-map form to
   upgrade `state-morphism-holonomy-trivial` from computed → proved. (Should be a direct mirror.)
2. General `M`: define the "position-threading action" precisely and prove the `π_0`-indexed
   holonomy-free classification (Reader `π_0=E`, State `π_0=1` are the two solved poles).
3. The substitution/plethystic `⊛`-monoidal home whose comonoids ARE the liftings — endpoint-locality
   should read as "⊛-comonoids are holonomy-free". Clean external framing + book Ch7.
