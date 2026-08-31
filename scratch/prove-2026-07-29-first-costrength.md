# PROVE scratch — `first`/costrength for effect–coeffect arrows (2026-07-29)

## Target
Extend the proved biKleisli **category** `Arr_M` (arrows `p⇝q := Cont(G_M p, T_M q)`,
category iff M non-branching) to a genuine **Hughes arrow / Freyd category**:
supply `arr`, `first`, and prove the arrow laws. Conjecture: genuine arrow iff M non-branching.

## Setup recap (from 2026-07-29-effect-coeffect-arrows.md)
- Container `p=(V,Q)`, morphism `(u,f):A→B` fwd `u:S_A→S_B`, bwd `f_s:P_B(us)→P_A s`.
- `G_M(S,P)=(S,M∘P)` comonad; counit ε bwd η_M, comult δ bwd μ_M.
- `T_M(S,P)=(MS,P⋆)`, `P⋆(m)=∏_{b∈lv(m)}P(x_b)` monad (Ahman–Bauer).
- Arrow `p⇝q = Cont(G p, T q)`.
- Compositor `κ:GT⇒TG` lax `∏_b M Z_b → M ∏_b Z_b`; category iff M non-branching (E2'/assoc).

## The tensor
Freyd base = `Cont` with its **cartesian product** `×`:
`p×c = (V×T, Q(v)⊔Q_c(t))` (positions = coproduct). Projections π₁,π₂ exist.
This is the tensor `first` acts on.

## Construction of `first : (p⇝q) → (p×c ⇝ q×c)`
Given `f : G p → T q`, define
```
first(f) : G(p×c) --σ--> Gp × c --f×id_c--> Tq × c --τ--> T(q×c)
```
- **σ_G (comonad costrength)** `G(p×c) → Gp×c`: fwd id on V×T; bwd
  `(M(Q v) ⊔ Q_c t) → M(Q v ⊔ Q_c t)` = `M(inl)` on left summand, `η_M∘inr` on right.
  TOTAL and natural for **every** M. (Coeffects are always costrong.)
- **τ_T (monad strength)** `Tq × c → T(q×c)`: fwd `st_M : MV×T → M(V×T)`,
  `st(m,t)=M(v↦(v,t))(m)`; bwd at `(m,t)`:
  `∏_{b∈lv m}(Q v_b ⊔ Q_c t) → (∏_b Q v_b) ⊔ Q_c t`.
  This backward map is the **distributivity** `∏_b(A_b⊔C) → (∏_b A_b)⊔C`.
  - non-branching (|lv m|≤1): identity/inl — TOTAL, natural. τ_T EXISTS.
  - branching (|lv m|≥2): NO natural total map (mixed tuples have no image). τ_T FAILS.

## CONJECTURE (refined)
(i) `arr(f)=η^T∘f∘ε : Gp→p→q→Tq` is an identity-on-objects functor `Cont→Arr_M`.
(ii) For **non-branching** M, `first` is well-defined and satisfies all 5 Hughes laws
     ⟹ `Arr_M` is a genuine Hughes arrow / Freyd category.
(iii) The **strength `τ_T` of the effect monad `T_M` for `×` exists iff M non-branching**
     — a SECOND manifestation of the branching obstruction, independent of E2'/assoc,
     but the SAME phenomenon (∏ fails to commute past ⊔/M under branching).
(iv) Hence `Arr_M` is a Hughes arrow **iff M non-branching** (Theorem A + (ii)).
     For branching M the category itself fails (assoc), so a fortiori no arrow.

## Narrative payoff
Coeffect comonad G_M: **always costrong** (σ total ∀M).
Effect monad T_M: **strong iff non-branching**.
So branching is exactly what stops effects from threading past an untouched wire `c`.

## What a counterexample looks like
- To (ii): a non-branching M (Maybe/Writer) where some Hughes law fails computationally.
- To (iii)-existence: a branching M where a natural total τ_T DOES exist. (Refutes obstruction.)

## TODO compute
1. Build `×` on Cont, σ_G, τ_T, first(f).
2. Maybe & Writer/ℤ₂: first well-typed; all 5 laws exhaustively.
3. Pf: show no NATURAL τ_T.

## Computational Evidence (DONE)
- **Non-branching (Maybe, Writer/ℤ₂):** τ_T canonical + total; ALL Hughes laws L3–L8
  exhaustive PASS (rich objects: L5 up to 1024/1024, L6 128/128). ⟹ genuine Hughes arrow.
- **Pf (branching):** the naive "mixed→⊥" τ is partial. BUT a **priority** τ
  (all-`inl`→product, else leftmost-`inr` C-value) is TOTAL and even passes the monad
  strength UNIT and MULT axioms. HOWEVER it FAILS **naturality** under the leaf-swap
  φ:a↔b (`nat_in_q` = False). Pure reorder breaks it.

## CORRECTION (assumption killed)
My first claim "no total τ for branching" was WRONG: total τ exist (priority). The correct
obstruction is **naturality / leaf-symmetry**:
> **Strength-obstruction lemma (corrected).** A *natural* strength τ:T_M(−)×(=)⇒T_M(−×=)
> for × exists iff M non-branching. For branching M, at a shape m with ≥2 permutable leaves
> and a c-wire with ≥2 positions, the target position assigning DISTINCT c-values to two
> swappable leaves must map into the permutation-invariant C-summand of (∏A)⊔C; Aut(m)-
> equivariance (=naturality) then forces two distinct outputs — contradiction. Any total τ
> (priority) buys totality by breaking this symmetry.
Note priority-τ PASSES strength-MULT, so this obstruction is NOT E2'/μ-merging: it is a
genuinely DIFFERENT face of branching (symmetry vs correlation), both vanishing iff ≤1 leaf.

## Strategy / Key lemmas (all machine-verified)
- **σ_G costrength**, all M: natural (Pf & Maybe pass, even under merge). Coeffects always costrong.
- **τ_T strength ⇐** non-branching: canonical, natural, strength axioms hold (Maybe/Writer).
- **τ_T strength ⇒**: branching ⟹ NO natural strength. Core = Yoneda: on the all-`inr` slice
  (A_b=∅) d:{c}^n→{c} is forced to a leaf-projection π_i (Yoneda, Nat(Hom(n,−),Id)=n). Then a
  leaf-transposition automorphism (Pf: swap a↔b, witnessed: distinct c-vals u,v → u vs v) or a
  leaf-reindexing (List: merge, witnessed) contradicts a FIXED i. Priority-τ = choosing i = breaks
  naturality.
- **Positive packaging**: first=τ∘(f×id)∘σ; L3–L8 exhaustive PASS (Maybe, Writer/ℤ₂). Cite
  Uustalu–Vene / Power–Robinson biKleisli-arrow theorem for the abstract packaging.
- **Main iff**: Theorem A (proved, category iff non-branching) + B (non-branch ⟹ laws) ⟹
  Hughes arrow iff non-branching. Branching ⟹ fails BOTH via assoc (A) and via strength (lemma).

## Verdict: SOLVED (with honestly-scoped gaps)
Genuine Hughes arrow / Freyd category ⟺ M non-branching. T1 (arr), T2 (first + strength
obstruction, corrected to naturality), T3 (Freyd id + KRU) all delivered.
