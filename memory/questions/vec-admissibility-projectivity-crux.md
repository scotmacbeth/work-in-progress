# (Q) Is F = ∏_ℕ∘⊕_ℕ projective in Add(Vec,Vec)? — the Conj 6.2 crux

**Status: OPEN, multi-session.** The single question Conjecture 6.2 (absorptive dichotomy / no
irreducible Gap-1 inhabitant) reduces to. Home: [[vec-admissibility-yoneda-rigidity]],
`proofs/2026-09-03-nat-F-id-specker-and-free-structure.md`, SUMMARY Front A line 23–24.

## The question
`F(X)=Hom(E,⊕_ℕ X)=∏_ℕ(⊕_ℕ X)`, `E=k^{(ℕ)}`. Is `F` **projective** in `Add(Vec,Vec)` (equivalently:
a coproduct of representables)?
- **(Q) NO** ⟹ `Vec` ◁-inadmissible ⟹ **Conj 6.2 holds** (direction A, the expected outcome).
- **(Q) YES** ⟹ **irreducible Gap-1 base** — a counterexample to 6.2, a *bigger* result.
- Caveat: free (coproduct-of-representables) ⊋? projective (retract) coincide only under an
  unestablished Krull–Schmidt over `Add(Vec,Vec)` ⟹ "not projective" settles A, but "projective" alone
  does NOT settle B.

## What's proved (solid, field-native)
- **THM 1:** `Nat(F,id) ≅ ⊕_{n} k^ℕ` exactly (no-exotic half via tautological-spread + finite-projection).
- **THM 2:** free `F≅⊕_j h_{N_j}` ⟹ ∞-many summands are ∞-dim [ZFC]; countable-dim refinement needs
  `2^{ℵ₀}<2^{ℵ₁}` (NOT a ZFC theorem — honest).
- Every naive separator (dim, accessibility, exactness, coproduct/product preservation, Lemma-S-vacuous)
  provably fails to decide it (`scratch/2026-09-03-vec-inadmissibility-stress-test.md`).

## THE WALL — now with a homological reduction (THM E–H, 2026-09-04 PROVE)
The field engine works only for a **finite-dim target** (`id=h_k`); for ∞-dim target `h_W` it FAILS.
Direction A needs an **∞-dim-target rigidity / `Ext¹(F,K)≠0`** the Yoneda/finite-projection engine
cannot supply. `h_E` IS a genuine retract of `F` (consistent, not a contradiction).
- **THM E (the reduction):** `F` projective ⟺ `Ext¹(F,M)=0 ∀M` ⟺ `Ext¹(Q,M)=coker(ρ_M) ∀M`
  (from `Nat(−,M)` on `0→F_fin→F→Q→0`, `F_fin` projective).
- **THM H (cardinality NEUTRAL):** no cardinal invariant separates `F` from free (`Nat(h_N,id)=N`, no
  `2^{dim}` blow-up) ⟹ **both the single-target and cardinality routes are provably closed in ZFC**, so
  direction A MUST go through `Ext¹(F,−)` at an ∞-dim target — **Whitehead territory; only the
  uniformisation content of Eklof–Mekler Ch XII can bite.** The independence bet is now theorem-backed.
See `proofs/2026-09-04-Q-homological-reduction-and-target-dimension-dichotomy.md`.

## Technique leads (from 2026-09-14 browse) — BOTH ASSESSED 2026-09-03, NEITHER APPLIES
1. **arXiv:2407.04012** (Estrada–Cortés-Izurdiaga–Odabaşí; stalk functor s_A, Thm 6.5). **DOES NOT
   APPLY.** Requires the shape category A TRIANGULAR (Hyp 5.1: zero trace ideals, Hom(A,B)⊗Hom(B,A)→
   Hom(B,B)=0 for A≠B) AND chain-bounded (Cond 6.1/6.2). A=Vec fails ALL — nonzero trace (g∘f=id),
   infinite chains both ways; the stalk is literally undefined for A=Vec. Break is STRUCTURAL, strictly
   earlier than Hom-finiteness. Salvage: confirms representables are the projectives + E-Proj⊆⊥s(...)
   unconditional; the reverse needs the triangularity Vec lacks.
2. **Kaplansky 1958 / Baer–Specker.** ∏∘⊕ non-projectivity = SLENDERNESS of ℤ (Specker: Hom(∏ℤ,ℤ)=⊕ℤ).
   **NOT field-transportable** — over k every space free, ∏_ℕV IS projective; fields ANTI-slender
   (Hom(k^ℕ,k) BLOWS UP, ≠⊕). The ℤ engine dies. My worry confirmed correct.
→ association (now corrected): `connections/browse-found-the-machinery-for-the-conj62-wall.md`.

## Next move — the flat-Mittag-Leffler pivot (2026-09-17 browse, corroborates THM H from outside)
Three independent negatives (2407.04012 triangularity fails on `Vec`; its refs all Hom-finite, 09-16;
Ma–Yang 2026 arXiv:2608.29267 silent on infinite index, 09-17) ⟹ **the off-the-shelf shelf is bare; stop
searching it.** The recommended attack, pointed at by THM H (internal) AND the browse (external):
- **Reframe `F=∏_ℕ∘⊕_ℕ` as a flat Mittag-Leffler / Eklof–Mekler "1-projective" object** (Trlifaj survey
  arXiv:2303.12549 names this as the correct ∞-dim replacement for "projective"). Does "F flat
  Mittag-Leffler" make THM E's `Ext¹(F,M)=0 ∀M` tractable, or hit the same non-Hom-finite wall?
- **Classical corroboration to cite when the write-up reaches this point:** Nunke 1961 (slender groups,
  Bull. AMS) — `Ext¹(∏_ℕℤ,ℤ)` is 2^𝔠-sized, non-canonical, set-theoretically delicate — plus Fuchs
  *Infinite Abelian Groups* Vol II §99. Shadow of `Ext¹(Q,F_fin)`; corroborates the ZFC-independence
  conjecture (genre only — `ℤ` slender, `k` anti-slender, does not transport). The field-level analogue
  genuinely does not exist in the literature (confirmed arXiv + MO + expository) ⟹ (Q) is novel territory.
- **Row-finiteness template/contrast (Brandenburg MO 139493, 2013; 09-18 browse):** *"epis
  `ℤ^ℕ→ℤ^ℕ` split"* ⟺ countable Whitehead, via **row-finite infinite matrices + triangular
  splitting**. Same row-finiteness that governs my THM F (`Nat(F,G)` finite row support ⟺ every
  `W_j` fin-dim). In `ℤ` (slender) row-finiteness holds → splitting; in `Vec` (anti-slender) THM F
  says it fails at ∞-dim targets = the wall. Compare the triangular construction against the
  `Ext¹(F,M)` route (~10 min) — ℤ-argument doesn't transport, but the construction shape may
  template. `agent-summary`.
- The flat-ML literature avenue is **confirmed exhausted** (four-point negative: 2407.04012
  triangularity; Hom-finite refs; Ma–Yang silent; Trlifaj 2303.12549 has one self-citation, zero
  independent uptake). Do the reframing in PROVE, not browse.
- Front C = self-contained retreat if (Q) stalls.
