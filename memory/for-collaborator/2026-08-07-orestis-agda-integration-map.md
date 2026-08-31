# Orestis's Agda ↔ MacBeth's container framework — integration map

**Date:** 2026-08-07. **For:** Neil, Robin. **Status:** arrived + read; one high-value test in flight.

## Arrival
Neil emailed `Effects.zip` (181 KB) directly (2026-08-06). Extracted to
`peers/orestis/Effects/`. Full file-by-file reading + dictionary in
`peers/orestis/READING-NOTES.md`. It IS the lifting-to-Cont story Neil has
been waiting on — his #1 priority.

## The dictionary (verified against the Agda source, not filenames)

| Orestis (Agda) | MacBeth | Match? |
|---|---|---|
| `Lift F (S◁P) = S ◁ (F∘P)`, `ε=id◁return`, `δ=id◁join` | **G_M** coeffect comonad | EXACT, in coordinates |
| `CoLift L (S◁P) = F S ◁ Λ P` | **T_M** effect monad (shapes) | matches at the □/∀ instance of `Λ` only |
| `_⇕_ := Lift F C ⇒ CoLift L D` | arrow object `p ⇝ q = Cont(G_M p, T_M q)` | EXACT |
| `dist : Λ(F∘P) → F(Λ P)`, glues `_⨾ⁿ_` | **κ** compositor `G_M T_M ⇒ T_M G_M` | EXACT (the reverse/hard direction) |
| `MonadicLenses.agda` (well-behaved, comp, spans) | G_M coKleisli arrows | EXACT, and FULLY PROVED by him |
| `ILift.agda` (indexed, base-change = F return/join) | G_M as vertical comonad over the base monad | genuinely fibrational — feeds Neil's fibrational steer |

## Three flags (skeptical reading)
1. **`CoLift` = a Λ-indexed family, not canonically the ∏-Mendler T_M.** He
   abstracts the position side into any `OplaxLifting Λ`; branching examples use
   **◇/∃ ("may")**, whereas my T_M / obstruction is the **□/∀ ("must")** ∏. So
   "CoLift = T_M" holds only at the □-instance.
2. **His `dist` is my κ (GT⇒TG), not λ.** The always-exists Beck–Chevalley
   entwining **λ (TG⇒GT) is ABSENT** (`BiLift′ = G∘T` is a functor only).
   Formalising λ is a clean joint target.
3. **The branching obstruction is UNPROVEN in his code — the #1 joint check.**
   He *builds* `_⨾ⁿ_` for List (`Nondet/BiLift.agda`) and validates only by
   `refl` on examples; he never proves associativity. My theorem predicts
   branching ⟹ non-associative — but for the □ lifting. Under his ◇ lifting it
   is genuinely open: (i) fails ⟹ obstruction extends to ◇; (ii) holds ⟹ the
   obstruction is □-specific, a refinement of my theorem. **Test in flight**
   (`scratch/orestis-integration/`).

## What each side uniquely has
- **Orestis has (formalisation):** κ as a runnable container morphism + biKleisli
  composition (Maybe/Writer/List/State); monadic lenses proved; `PredicateLiftings`
  abstraction; `ILift` fibrational base-change.
- **MacBeth has (not in his code):** the non-branching classification, the λ
  entwining/bialgebra face, all cartesian-preservation ("crown") results, ZS/H².

## Next steps
- **[in flight]** associativity of `_⨾ⁿ_` on a menu-of-2 List witness → (i) or (ii).
- Formalise λ (TG⇒GT) as the joint Beck–Chevalley target he lacks.
- Neil's bet to test: "cartesian-morphism preservation gives E2′/naturality for
  free" — my 4-rung ladder (non-branching ⊊ cartesian) suggests cartesian is too
  weak for E2′ (List splits it); worth pinning precisely against his `ILift`.
