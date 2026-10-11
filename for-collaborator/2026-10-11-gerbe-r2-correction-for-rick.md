# Covering note to Rick — inventory gerbe, round-2 corrections (N1, N2)

**To:** Rick (grandparick20@gmail.com) · **CC:** Robin Langer · **From:** MacBeth
**Re:** "A classical H² obstruction … the inventory gerbe and its band" — your round-2 report of 2026-10-11
**Status:** QUEUED for WAKE delivery (WRITE cannot email). Do not re-send if already delivered.

Rick — thank you for the round-2 report. Both new must-fixes are landed in the note
(`papers/supply-chain-inventory-gerbe.tex`, content commit to be stamped; supersedes `4e7264d`).

**N1 (Corollary 17 — two definitions; false under D1).** Fixed as you prescribed. The note now carries
a single definition of global inventory — your **(D2)**: a pair (µ, T) with a gauge µ: Ob C → Aut K
and a strict T : C → BK satisfying µ(y)·α(f)·µ(x)⁻¹ = conj(T f) (eq. (D2) in Def. 6). I made the
strictness / 2-cell hypothesis explicit and load-bearing in §2.3 (the transport is a strict functor
α : C → B(Aut K) carrying the comparison data k_{g,f}), so the step "β=0 ⇒ α = conj∘ρ with ρ a genuine
functor" in the proof of Cor. 17 is now justified — and I flag that without the k_{g,f} the up-to-inner
slack is empty and ρ (hence [g]) is undefined, exactly your D1 counterexample (D4, α(g)=conj(s)). Added
a remark that [g] is well-defined only modulo the Aut(Z)-action while its *vanishing* is gauge-invariant
(your "λ ranges over Out K" point), deleted the "section realised on the nose" phrasing (the band is part
of the gerbe data, following Giraud), and reframed Cor. 17 as the classical two-stage crossed-module /
Postnikov obstruction (π₁=Out K, π₂=Z; primary β, secondary [g]) with the EM/Giraud/Breen attribution
(N4). N3 (α̃ "cocycle") is resolved by the standing strictness.

**N2 (retract the biconditional; add the sharp criterion).** The false biconditional "[γ]≠0 ⟺ K
nonabelian with nontrivial centre" lived in the registry/commit/email, not in the printed Thm 25(i) —
whose "only if" I have left intact. I retract the biconditional explicitly and add the sharp criterion as
a new Theorem D′ (§8.1): for the n-lot ring K = D_n,

  [γ] essentially nonzero ⟺ (⋆) non-split ⟺ [⋆]≠0 ∈ H²(Inn K; Z) ⟺ 4 | n,

with the D₆ ≅ Z/2 × S₃ reconciliation (nonabelian, centre Z/2, yet splits ⟹ necessary ≠ sufficient) and
the n = 3..12 table. This cites the companion PROVE note of this cycle
(`proofs/2026-10-11-nlot-ring-gerbe-sharp-4divn.md`), graded proved (own-verification;
split test computed n = 3..16, non-split exactly at {4,8,12,16}). The sharp criterion is surfaced in the
abstract and the intro Theorem-D preview so the headline is visible by page 2.

I also fixed the phantom reference [9] (the Ho citation → G. Hoff, *Cohomologies et extensions de
catégories*, Math. Scand. 74 (1994) 191–207, doi:10.7146/math.scand.a-12489), gave [10] Wells a venue,
and added the Bourn venue (your E5).

I am **not** claiming any registry re-promotion on the strength of this — `thm-A-rectification` and
`thm-D-nonvacuous-criterion` are yours to re-grade after re-review. I checked §6 of the standalone
band-boundary note: its "require nontrivial centre / outer group" is phrased as *necessity*, not the
retracted biconditional, so it needs no change.

Gratefully, MacBeth
