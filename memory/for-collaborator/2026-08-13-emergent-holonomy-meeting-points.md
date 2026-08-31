# For Robin/Neil — emergent holonomy has a one-number geometric diagnostic

**MacBeth, 2026-08-13 (PROVE).** Full write-up: `proofs/2026-08-13-emergent-holonomy-meeting-points.md`.
Upgrades the 448-check backbone of the 08-12 cross-mode bridge into a general theorem.

## The result in one breath
For an exact factorisation `G = P·P'` (= internal Zappa–Szép product) acting on a set `S`, and any
point `s`, the *emergent holonomy* synthesised by orchestration — the reentrancy the composite has but
neither factor does — is measured by a single positive integer:
```
    h(s) = |Stab_P(s) \ Stab_G(s) / Stab_{P'}(s)|
         = |Stab_G(s)| / (|Stab_P(s)|·|Stab_{P'}(s)|)          ← the naive ratio, now proved an integer
         = |(P·s) ∩ (P'·s)|                                     ← geometry: crossings of the two orbits
```
and `h(s) = 1` **iff** the two factor orbits meet only at `s` (**iff** `s` is "aligned" **iff** the
part-(c') `[ω]∈H²` analysis even applies).

## Why it's clean (two lemmas)
1. **Disjointness Lemma:** `P ∩ gP'g⁻¹ = {e}` for *every* `g ∈ G`. Three lines — write `g = pp'`, then
   `p⁻¹ a p = p'p''p'⁻¹ ∈ P ∩ P' = {e}`. Uses nothing but "subgroups, trivial intersection." It forces
   every `(A,B)`-double coset in the stabiliser to have the *uniform* size `|A||B|`, which is exactly
   what makes the naive ratio an integer (I had worried it might not be — it always is, and this is why).
2. **Intermediate-point bijection:** a composite `s`-fixing move `g = pp'` is a loop
   `s ─p'→ t ─p→ s` with waypoint `t = p'·s`. The map `g ↦ t` induces a bijection
   `Stab_P(s)\Stab_G(s)/Stab_{P'}(s) ≅ (P·s)∩(P'·s)`. Emergent loops are exactly those with `t ≠ s` —
   neither leg fixes `s`, yet the round trip does.

## Why you two care
- **Neil:** this is the honest closure of the 08-12 gap — the (c') "aligned" hypothesis is no longer an
  assumption; it is `h(s)=1`, a computable geometric condition. Alignment ⟹ `U = A⋈B` is automatically
  an internal ZS sub-product of the vertex group, so the `H²(B;A)` extension story is well-posed exactly
  there and nowhere else. The `[ω]` entanglement dichotomy lives *inside* the `h=1` fibre; `h>1` is a
  strictly earlier, combinatorial phenomenon. Two invariants, cleanly separated. Good for the theory
  section of the grant, and it makes the "orchestration synthesises holonomy" slogan quantitative.
- **Robin (infra/impact):** `h(s)` is *cheap* — no cohomology to detect emergence, just intersect two
  orbits. An auditor for composed agents (supply chain, smart contract, GA pipeline) computes `h` from
  the two agents' state actions directly: `h(s)>1` flags exactly which states carry synthesised
  reentrancy and how much. Natural `/lean` target and a clean figure for a talk (two orbits crossing).

## Verification
`scratch/general-M-liftings/zs_holonomy_L3.py`: bijection + alignment + the L2 biconditional over
S₃,S₄,A₄,D₄,ℤ/2²,D₆,A₅ (2594 point-checks, 0 mismatches); disjointness `P∩gP'g⁻¹={e}` over all `g`
(41064 checks, 0 violations). Registry `holonomy-composition-zs-bridge` updated, validator green.

## Open threads (for the dream cycle)
- **Lean:** `int`-bijection or at least the Disjointness Lemma + `h(S₃,1)=2` witness — mechanical, the
  group-theory API is standard. Pairs with the already-verified `HolonomyWitness.lean`.
- Is `h(s)` a *character* of anything? It's `⟨1_A ↑^U, 1_B ↑^U⟩` (Mackey inner product of the two
  induced trivial characters) — worth chasing: does the emergent-holonomy *representation* decompose
  along the meeting points? That would upgrade `h` from a count to a full rep-theoretic decomposition.
