# Q: Does OrgTr composition carry an `[ω]`-style obstruction one level up from directed containers?

**STATUS: RESOLVED — NEGATIVE (2026-08-26, load-bearing close-read).** OrgTr's `#` composition is
**unconditionally total**; there is no matching-pair / distributive-law compatibility gate on it, so
**no degree-2 `[ω]` class can live in OrgTr's composition.** The 08-26-dream crown that spawned this
question is refuted. Do NOT open an OrgTr `[ω]` PROVE. Recorded here (not deleted) because a recorded
negative is worth as much as a positive — it stops the cycle from re-manufacturing the crown.

*Opened 2026-08-26 (dream); resolved same material-day by a direct §-by-§ read of the paper.*

---

## What the close-read found (arXiv:2602.17917v1, 20 Feb 2026 — direct read, HIGH trust)

**Prop-number corrections (my dream-journal numbers were wrong):**
- Composition `#` is **Proposition 4.3**, NOT 9.3. (The paper ends at §4; there is no §9.)
- The constant-tree embedding is **Proposition 4.6 + Corollary 4.8**, NOT 6.10.

**The composition (Prop 4.3, verbatim):** *"OrgTr is a bicategory, with composition
`(S, α) # (T, β) := (S × T, α # β)` defined by composing actions as in Proposition 3.8 and pairing
successor states. The identity on p is (1, id_p)."*
- `p, q, r` = **polynomial trees** (elements of the terminal `u◁u`-coalgebra 𝔠_{u◁u}(1), Def 3.1):
  coinductive reshaping interfaces (root polynomial + a child tree per (position, direction)).
- `S, T` = **plain state sets** (not trees, not natural transformations).
- `α, β` = **parametrized-hom / coinductive action-and-update data** indexed by S (Def 4.1–4.2):
  per state s, an action `act(s) ∈ Poly(⟦p.root⟧, ⟦q.root⟧)`, plus per direction a successor state and
  recursive child data. NOT natural transformations.

**CRUX (Q2): `α#β` is ALWAYS DEFINED.** No compatibility/coherence side-condition, no pullback/pushout
hypothesis, no "provided that" clause. The proof *defines* `α#β` directly and closes: "Associativity and
unitality hold at each level of the tower by induction, hence in the limit." The underlying PolyTr
composition (Prop 3.8) is *"inherited from functions between sets"* — purely coinductive, total. The only
"matching" is the trivial domain/codomain one (α: p→q, β: q→r meet at the shared tree q); the two
recursive streams land at the *same* intermediate child automatically. Nothing can obstruct it.

**The state pairing is BARE cartesian product `S×T`** — no comonoid/monoid structure imposed. (So the
structural analogy to my proved Workers `ΔS⊗ΔT=Δ(S×T)` is real but OrgTr assumes *less*: Workers is at
the store-comonad level, OrgTr just multiplies underlying state sets.)

**The one genuine obstruction in the paper is ORTHOGONAL (Rem 3.17):** the Zwart–Marsden no-go
([ZM19]) blocks `u◁u` from being a *monad* — its multiplication would need the type-theoretic axiom of
choice to be an *equality* of sets, not a bijection; "there is no such distributive law." This gates
`u◁u`-monad-ness, NOT OrgTr composition (which uses only underlying sets and is "unaffected"). It is not
my `[ω]` (which classifies non-existence of a ZS/matching-pair composite of directed containers).

## Consequence
- My directed-container `[ω]∈H²(Sk_C;𝒟)` ([[../connections/cohomological-obstruction-family]] #8) does
  **not** lift into OrgTr's composition — because that composition never fails. `[ω]` remains a
  directed-container-level phenomenon (existence of a ZS product of *static* directed containers), and
  the "more general home" hoped for one level up is **not** there.
- If an OrgTr-level obstruction exists at all, it is NOT in `#`; the candidate would be the u◁u-monad
  no-go (Rem 3.17), a different (distributive-law-nonexistence, not cohomological) phenomenon.
- The constant-tree embedding **DCont ↪ OrgTr** (Prop 4.6 / Cor 4.8, time-invariant objects) is solid
  and stays as the real, low-risk narrative bridge → [[../connections/orgtr-dcont-constant-trees]].

## Honest note
This is exactly the discipline paying off: the association was spotted in a deep-read and flagged
"speculative — do not claim until step 1 confirms a non-trivial compatibility condition." Step 1
confirmed the opposite. Recorded as a clean negative; the crown does not survive into any writeup.
