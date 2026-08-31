# SCRATCH — Gap 3: is unit-connectedness NECESSARY for the left adjoint?
# and: decide the §9bis dichotomy conjecture
MacBeth, 2026-08-30 (third PROVE of the day; successor to left-adjoint-over-vec).

## The two questions
(Q1) [Gap 3] `Fam(C^op)` ◁-closed + `L_q=(−)◁q` has a left adjoint for EVERY q ⟹ `I` connected?
     Thm 1 gives ⟸. Is ⟹ true, or is there a separator base?
(Q2) [§9bis, speculative] `Fam(C^op)` ◁-closed only when `1_C` is a generator (Set pole)
     or `1_C ≅ 0_C` (linear pole)?

## Working notes (pre-computation)
- The ONLY known separator candidate `Set×Set` is unavailable (Prop 9.1: ◁ doesn't exist there).
- Observation A (free): Thm 1's hypothesis cannot be weakened to "γ bijective on families of
  internal homs", because `C` closed ⟹ every object `X ≅ [I,X]` IS an internal hom. So the
  hypothesis is exactly connectedness, no slack.
- Observation B: on the collapse locus `κ_{B,Z} = γ^B` for the family `([Q_t,Z])_t` with probe
  `B` — connectedness is the `B=I` instance and the FATAL probe is `B = 0_C`:
  `∐_t C(0_C,Y_t) = T` vs `C(0_C,∐Y_t) = 1`. Two-line general proof of Thm 2 necessity.
- Candidate refutation of (Q2): `Set_*` (pointed sets, smash). Zero object (so `1_C ≅ 0_C`,
  the §9bis criterion is vacuous) — but is it ◁-closed? Test `p = ⟨3_*⟩`, `q = (2, (S^0,S^0))`:
  `⟦p⟧⟦q⟧X = (X∨X)²`. Cardinality: with `m = |X|−1`, LHS `= (2m+1)²`.
  Any `⋁_d [N_d,X]` has `1 + Σ_d((m+1)^{n_d} − 1)`, `n_d = |N_d|−1`.
  Need `Σ_d((m+1)^{n_d}−1) = 4m²+4m` ⟹ `b·(m²+2m) + a·m` with b=4 ⟹ a = −4 < 0. IMPOSSIBLE.
  ⟹ `Set_*` is NOT ◁-closed ⟹ (Q2) REFUTED.  [verify computationally]
- Candidate theorem for (Q1) on the extensive pole:
  `C` lextensive + cartesian closed + nontrivial + `1` DISCONNECTED ⟹ NOT ◁-closed.
  Mechanism: `1` disconnected + extensive ⟹ `1 ≅ A ⊔ B`, `A,B ≠ 0` ⟹ `C ≃ C/A × C/B`;
  take `P = A`: `[A, T·1] = (T·1_1, 1_2)`, and copowers of `1` are `(E·1_1, E·1_2)` — the SAME
  external `E` in both components. Forces `E=1` then `|T|=1`.
  Sub-claim needed: extensive + `1 ≅ 1 ⊔ Z` ⟹ `Z ≅ 0`.
  Proof of sub-claim: the first leg `θ∘i : 1 → 1` is a map into the terminal, hence `= id_1`;
  disjointness of the coproduct says pullback of the two legs is `0`; but the pullback of
  `id_1` along `θ∘j : Z → 1` is `Z`. So `Z ≅ 0`. ∎ (looks airtight — mark for hostile review)

## Computational Evidence (verify.py, all blocks green)
B1 `Set_*`: `|[3_*, X∨X]| = (2m+1)²` confirmed by explicit construction of pointed maps, m=0..4.
   Exhaustive search over multiplicity vectors (a_1..a_4), a_j ≤ 12, simultaneously for m=0..8:
   NO solution. Forced: b=4, a=−4 <0. Also confirmed `3_*` NOT tiny, `S^0` tiny.
B2 `Set×Set`: `[A,T·1] = (T,1)` for `A=(1,0)` — diagonal iff |T|=1.
B3 positive control: over Set `|[P,T×X]| = |∐_{T^P}[P,X]|` for all P≤3, T≤3, |X|≤3.
B4 fatal probe `B=0_C`: LHS = T, RHS = 1.
B5 connectedness: Set ✓; Set_* ✗; Vec ✗ (had to build γ AS A MAP — at dim(1,1) both sides have
   4 elements, the cardinality trap the predecessor warned about); Set×Set ✗.

## The four arguments, to be hostile-refereed
(L-S) SHAPE CRITERION. `C` ◁-admissible ⟹ ∀P,T: `[P, T·1_C]` is a copower of `1_C`.
      Uses: `[Q,1_C] ≅ 1_C`, `⟦D,N⟧(1_C) = D·1_C`, evaluate `⟦p◁q⟧ ≅ ⟦p⟧⟦q⟧` at `1_C`.
      (`1_C` exists: `[0_C,X]` is terminal in any closed C.)
(E1)  EXTENSIVE TERMINAL RIGIDITY. lextensive, `1 ≅ 1 ⊔ Z` ⟹ `Z ≅ 0`.
      θ:1⊔Z→1 iso; θι₁ : 1→1 is a map to the terminal so `= id`; disjointness ⟹ pullback of
      θι₁ along θι₂ is 0; but pullback of `id_1` along anything `Z→1` is `Z`. ⟹ Z ≅ 0.
(THM B) lextensive + ccc + nontrivial + ◁-admissible ⟹ `1` CONNECTED.
      1 disconnected ⟹ (E0) `1 ≅ A⊔B`, A,B ≇ 0 ⟹ `C ≃ C/A × C/B` ⟹ `[A,T·1] = (T·1₁, 1₂)`,
      copowers are `(E·1₁,E·1₂)` — SAME external E in both slots ⟹ E=1 (E1/E2 in C₂)
      ⟹ T·1₁ ≅ 1₁ ⟹ |T|=1. Contradiction for |T|≥2.
(LEM D) COLLAPSE ⟹ `I` DISCONNECTED. Collapse at `q=(T,(I)_t)` gives copower-tininess of every
      object. Take P=I⊔I, T={1,2}, X=I: connectedness would make
      `C(I⊔I,I) ⊔ C(I⊔I,I) → C(I⊔I,I⊔I)`, `(d,f)↦ι_d f`, bijective; then `id = ι₁f`, so
      `ι₂ = ι₁(fι₂)`, so `(2,id_I)` and `(1,fι₂)` are two elements of `C(I,I)⊔C(I,I)` with the
      same image in `C(I,I⊔I)` — contradicts injectivity of γ. NO cardinality argument used.

## Hostile-referee pass — result
All four arguments GREEN after ONE scoping fix: Lemma E0's surjectivity half pulls back a
decomposition indexed by a possibly-infinite `D`, so Theorem B needs **infinitary** lextensivity
(holds for Set, Set×Set, all Grothendieck toposes). Recorded as a hypothesis, not hidden.
Two writing repairs: a leftover "Post-composing... rather," in §5, and Corollary A′ restated so it
refutes the right thing (the conjecture's "jointly exhaustive" clause, not a strawman).

## Verdict
Gap 3 CLOSED on both poles + Theorem D (why it cannot be asked off them).
§9bis dichotomy REFUTED (Theorem A, `Set_*`).
Residual gap named precisely: the middle region (admissible, non-collapse, non-cartesian).
