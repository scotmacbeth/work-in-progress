# The logic of containers: Cont(cod) is a bifibration, and its quantifiers are the A/E liftings — dualised (Neil UID-132)

**For Neil / Robin. 2026-08-28 PROVE. Full proof:
`proofs/2026-08-28-cont-cod-fibration.md`. Registry `cont-cod-predicate-fibration.json`
(proved, validator-clean). Verification: `.claude/scratch/verify_cont_cod.py`,
`verify_bc_frob.py` (all pass).**

## The one-line answer to "turn cod into a logic of containers"
**Done — and the payoff is a dualisation theorem: the hyperdoctrine of containers is the
*fibrewise opposite* of the standard Set-family hyperdoctrine.** `Cont(cod) = Fam(cod^op)` is a
bifibration; its fibred quantifiers are exactly Neil's proved A/E liftings; and because the fibres
are `(Set/P_s)^op`, the op swaps ∃↔∀, ∧↔∨, ⊤↔⊥. The container's ∃ is Set's ∀ (Π); its ∀ is Set's ∃ (Σ).

## The construction (rigorous)
1. **Fam preserves fibrations (Lemma 2.1, written in full, not cited).** `(u,{φ_i})` is
   `Fam(p)`-cartesian ⟺ **each `φ_i` is `p`-cartesian** — both directions, via a singleton-family
   test and componentwise unique factorisation (freeness of the coproduct completion). Hence `Fam`
   preserves fibrations, opfibrations, and bifibrations, componentwise. This is the load-bearing
   fact and it's now airtight.
2. `cod` is an **opfibration** (post-composition) ⟹ `cod^op` is a **fibration**; `cod` is a
   bifibration (Set has pullbacks) ⟹ **`Cont(cod) = Fam(cod^op)` is a bifibration** (Thm 3.1).
3. Fibre over `(S,{P_s})` = `∏_s (Set/P_s)^op` = proof-relevant predicates on positions,
   fibrewise-dualised. (I derive the op from the vertical-morphism direction directly — it matches
   von Glehn's `Cont = ∫_Set cod^op`, cited as ancestor not re-claimed.)

## THE TRAP — and I fell for the orientation's version first
The orientation said "reindexing = base-change `ρ_s^*` carrying `Σ_ρ ⊣ ρ^* ⊣ Π_ρ`." **That's the
naive reading and it's wrong.** The genuine cartesian reindexing of `Cont(cod)` is **`(Σ_ρ)^op`** —
dualised *post-composition* — because `cod^op`-cartesian = `cod`-**co**cartesian = Σ. The pullback
`ρ^*` reappears, but as the **opfibration weakening** `Δ_c`, one rung over in the adjoint string. The
fibrewise op is exactly what moves it. This is the whole subtlety Neil flagged ("watch the op").

## Quantifiers = the A/E liftings (Thm 5.1)
Both liftings quantify along the position-**collapse** `! : P_s → 1`. The one canonical base morphism
is `η : (S,{1}) → (S,{P_s})` (backward map `= !`). Then:
- `E = Exists = η^* = (Σ_!)^op = ◁` — the **cartesian reindexing itself** (total space).
- `Δ_c = η_! = (!^*)^op` — **weakening** (position-independent predicate).
- `A = All = (Π_!)^op`.
Adjoint string **`A ⊣ Δ_c ⊣ E`** = the literal op of Set's `Σ_! ⊣ !^* ⊣ Π_!`.

## The dualisation theorem (Thm 5.2 — the increment)
Relative to the common weakening `Δ_c`:
- container-**∃** (left adjoint) = **All** = built from Set's **Π**;
- container-**∀** (right adjoint) = **Exists** = built from Set's **Σ**.
The op swaps the *role* against the *operation*. It also swaps **∧↔∨** (container-∧ = fibre coproduct
= fibrewise disjoint union of witnesses) and **⊤↔⊥** (⊤ = empty-witness predicate; ⊥ = full
predicate). The proof-relevant fibre is a **co-topos**: its internal logic is co-intuitionistic /
subtractive. (This is invisible at the crude Boolean truncation `2^{P_s}` — subtractivity is a
witness-level phenomenon, which is a good reason to keep the proof-relevant reading you asked about.)

**Beck–Chevalley** (Prop 6.1) and **Frobenius** (Prop 6.2) hold, dualised — Frobenius becomes
*co-Frobenius*, pairing the quantifier with the fibre **coproduct**. Set instances brute-force
verified; op+Fam transport is formal.

## Clean general statement (for the grant / survey)
> **`Cont` is the fibrewise-opposite endofunctor on the 2-category of Set-family hyperdoctrines.**

This populates the previously-empty **fibrational leg (approach 3)** of the Front D survey.

## Your fork (proof-relevant vs subobject) — my answer
Keep **proof-relevant** as primary: the subtractive/co-topos structure only exists at the
witness level; the position-only propositional truncation is Boolean and hides the phenomenon.
The faithful propositional shadow is `Sub(Set^→) → Set` (co-Heyting fibres), which I state but did
not develop.

## Honest gaps
- **Shape-level quantifiers** (Fam Kan extensions along `u:S→S'`) exist componentwise, but I did
  **not** verify the combined shape×position hyperdoctrine satisfies BC/Frobenius jointly.
- Propositional-truncation preservation not developed; intrinsic characterisation of the BC square
  class left open.
None of these touch Thms 3.1 / 5.1 / 5.2 or Props 6.1–6.2.

## What I'd want from you
1. Is the **shape-level** first-order structure worth chasing next (toward a full internal-language
   statement), or is the fibrewise dualisation theorem the right stopping point for the survey?
2. The **co-topos / subtractive logic** reading — is that a grant thread you want me to push (it
   connects to "compositional correctness": positions flowing backward = a subtractive predicate
   logic), or a curiosity to park?
