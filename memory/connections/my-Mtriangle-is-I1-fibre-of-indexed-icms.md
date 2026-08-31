# My T^Σ_M = M◁− classification IS the trivial-index fibre of De Pascalis–Uustalu–Veltrì ICMS

**Date:** 2026-08-27 (WAKE, Front C). **Grade of the positioning:** `computed`/recognition — the
specialization argument is elementary and I can verify it; the identification with my side rests on my
own `proved` classification [[lifting-general-M-and-monoid-comonoid-unification]] + Uustalu's non-indexed
characterization. Source: sub-agent full-text extraction of De Pascalis–Uustalu–Veltrì, "Monoid Structures
on Indexed Containers," LSFA 2025, **arXiv:2509.25879** (PDF at `/home/agent/papers/depascalis_indexed_containers.pdf`).
NB: the paper has **no "Theorem 3.5"** — the content is **Definition 3.3 (ICMS)** + **Lemma 3.2**
(monoids in `(IC_I,⊗,I)` ≃ ICMS), assembled with Lemmas 2.1/2.3/3.1 into "monads on `Set^I` with
container-extent underlying functor ≃ ICMS." (My old SUMMARY Front-C bullet mis-cited "Thm 3.5" — corrected here.)

## The recognition

Indexed container = `S : I→Set`, `P : (∏_i S i)→I→Set`; extent `⟦S◁P⟧X i = Σ_{s:S i} ∏_j (P_i s j → X j)`.
ICMS data (Def 3.3): unit shape `e`, shape-mult `•`, **`Pe_≡`** (unit positions live only at own index),
**`↑`** (index of the outer/middle position), `↖` (outer position), `↗` (inner position) + unit/assoc eqns.

**At I = 𝟙:** `Set^I = Set`, `IC_I` = ordinary containers, and
- `Pe_≡ : P e j → (⋆≡⋆)` → codomain contractible ⟹ **TRIVIALIZES** (this is the datum the authors flag as
  having *no non-indexed analogue*);
- `↑ : P(s•s') → 𝟙` → constant ⟹ **TRIVIALIZES**, killing its two index-coherences (↑-↗-assoc, ↖-↑-↑-assoc);
- what SURVIVES: `(S, P, e∈S, •:(s:S)→(Ps→S)→S, ↖:P(s•s')→Ps, ↗:(p)→P(s'(↖p)))` + unit + `•`-assoc + ↖-↖ + ↗-↗.

That surviving data is **Uustalu's non-indexed "container carrying a monad" characterization** = **a ◁-monoid
on `(S,P)`, acting by `⟦S◁P⟧∘(−) = M◁(−)`** — exactly my `T^Σ_M = M◁−`. The paper says so explicitly ("every
piece of data and equation reappears with indices added"). Dictionary:
`•` = my ◁-monoid multiplication; `↖/↗` = the two components of the ◁ Σ-decomposition (outer shape / inner
positions); `e` = my unit; the three monad laws = the ◁-monoid laws.

## Why this is worth recording (the honest delta — NOT new mathematics)

1. **Positioning, not a theorem.** My `M◁−` classification is *literally the I=1 fibre* of a known LSFA 2025
   result. Do NOT re-claim it. This is the honest inverse of the [[the-summary-is-what-gets-audited]]
   novelty-manufacturing failure mode: I checked the source before claiming generality.
2. **Their generality over Gambino–Kock = dropping cartesianness.** GK characterize only *cartesian* monads
   (η, μ cartesian nat transfs = backward position maps are isos); ICMS allows `↑,↖,↗` (and `↖,↗` at I=1) to be
   **arbitrary functions**. That "cartesian vs general" axis is **exactly my branching/non-branching boundary**
   [[branching-full-morphism-lift]], [[crown-tfae-strict-chain]]. So the LSFA paper's one-step generalization
   (cartesian → general) is the *coarse* version of my **strict 4-level chain** `λ-inv ⊊ non-branch ⊊ cartesian
   ⊊ ∏-Mendler`. **They do NOT stratify inside "general"; I do.** ← candidate genuine delta.
3. **The real open question (Front C proper):** does my 4-level branching stratification **lift index-wise** to
   ICMS? I.e. is there an indexed refinement `λ-inv_I ⊊ non-branch_I ⊊ cartesian_I(=GK) ⊊ ICMS` on `IC_I`, and
   do the index-tracking data `↑/Pe_≡` interact with branching (leaf-symmetry) nontrivially? This is a concrete
   `/prove` or `/expository` target — and it is Neil's "prompts vary" = index-by-context/prompt-type generality
   [[feedback_neil_vcont_uses_first_notes]].

## Caveats
- Extraction is sub-agent, not my own read of the Agda. Letter-perfect subscripts on the 6 assoc eqns → authoritative
  source is the Cubical Agda formalization (github.com/mikidep/indexed-monads, `lsfa2025`). Enough verified for the
  I=1 specialization, which only needs the *types* of Pe_≡ and ↑.
- This is the **monoid-structure** indexed-container notion. Neil's UID 125 "indexed container `I←P→S→O` with
  Σ-Π-Δ over an LCCC" is a *different* (though related) angle — about the BASE and closedness, not the composition
  monoid. Both feed the three-approaches survey; keep them distinct. See [[three-approaches-containers-in-category]].
</content>
</invoke>
