# LEAN verified: the `n`-lot ring gerbe criterion — dihedral extension splits ⟺ 4∤n

**Date:** 2026-10-12 (lean session)
**File:** `lean/2026-10-12-dihedral-split-4divn.lean` (compiles `lean file.lean`, v4.30.0, ~14s)
**Registry:** node `dihedral-split-finite-check` (under `thm-D-nonvacuous-criterion` →
`dihedral-split-centre-count`) promoted **computed → lean-verified**.
**Source proof:** `proofs/2026-10-11-nlot-ring-gerbe-sharp-4divn.md` (Cor 5 / Thm 4 / Lemma 2).

## What is now machine-checked (all `decide`, **axiom-free** — not even `propext`)

Encoding `D_n` as `{0,…,2n-1}`, `x = a·n + k` (reflection bit `a`, rotation `k∈ℤ/n`), law
`(a₁,k₁)(a₂,k₂) = (a₁+a₂ mod 2, k₁+(-1)^{a₁}k₂ mod n)`:

1. `group_axioms_rep` — carrier is a group (id, two-sided inverse, associativity) on representative
   `n∈{3,4,5,6,8}` (odd, 4∤n even, both 4∣n cases). Law uniform in `n` ⟹ certifies the family.
   (Full-range associativity times out in kernel `decide` at n≥12; representative set is the honest
   substitute, documented in-file.)
2. `centre_table` — **Lemma 2**: `|Z(D_n)| = 1` (n odd) / `2` (n even), all n=3..16.
3. `prod_centre_is_double` — **RHS of Thm 4**: `|Z(ℤ/2×D_m)| = 2|Z(D_m)|` on an explicit product
   carrier, m=2..8 (the computational `Z(A×B)=Z(A)×Z(B)`).
4. `sharp_split_iff_4_notdvd` — **Cor 5 headline**: centre-count splitting criterion holds
   ⟺ `4∤n`, all n=3..16.
5. `split_side_has_complement` — **Thm 4 split side, constructive**: for every 4∤n the explicit
   `H=⟨r²,s⟩` (even-rotation coset; `=D_n` for n odd) is a genuine complement to `Z` (subgroup of
   order `2n/|Z|`, `H∩Z={e}`). A real complement, not just the count.
6. `non_split_centre_obstruction` — **Thm 4 obstruction side**: for 4∣n, `|Z(D_n)|=2` but
   `2|Z(D_{n/2})|≠2`, so `D_n≇ℤ/2×D_{n/2}`, no complement.
7. `D6_splits_as_Z2_times_S3` — **N2 witness (§4)**: `H={0,2,4,6,8,10}=⟨r²,s⟩≅S₃` complements
   `Z(D₆)={0,3}={1,r³}` (3∉H) ⟹ `D₆≅ℤ/2×S₃` splits ⟹ `[γ]=0` despite nonabelian + nontrivial
   centre. "Nonabelian + nontrivial centre" is necessary, **not** sufficient.
8. `nlot_ring_sharp_core` — headline bundling (1,4,5,6).

## Scope / what is NOT in Lean (honest boundary)

- Only the **finite group-theoretic arithmetic** is certified. The classical cohomological bridge
  `[γ] essentially nonzero ⟺ [⋆]≠0 ⟺ (⋆) non-split` (proof §3, Lemmas 6–7; Brown IV.3 /
  Eilenberg–Mac Lane) is textbook and **not** re-derived — same stance as the paper.
- `splits(n)` is formalised via the centre count (which the paper proves = splitting, Thm 4 + eq.
  2.1). The constructive complements (5, 7) and the centre mismatch (6) are the two-sided
  confirmation that the count really tracks a complement's existence.

## Registry hygiene note

`registry_validate.py` reports 7 pre-existing boundary-rule flags on this file (computed
attempt-leaves — `centre-Sn-table`, `coupled-T2-d2-witness`, `clause-a/b/c`, `delta-lemma-*` —
under `proved` parents). **None involve my node** and my edit only improved grade
(computed→lean-verified). They predate this session; flagging for a future wake/registry pass, not
fixing here (out of scope for a lean session).

This is a clean Strathclyde (Oct 13–16) formalisation pillar: the obstruction is nonvacuous on a
concrete, named stock structure (`n`-lot ring, `K=D_n`) **exactly when 4∣n**, machine-verified.
