# Corrected inventory-gerbe note, for Rick (CC Neil) — 2026-10-10

**Status:** QUEUED for WAKE delivery (WRITE has no email tool). Email to Rick
(grandparick20@gmail.com), CC Robin (langer.robin@gmail.com). Content commit **4e7264d**, pushed to
`github.com/scotmacbeth/work-in-progress` (`papers/supply-chain-inventory-gerbe.{tex,pdf}`, 13 pp,
recompiles clean). **This corrected note IS the deliverable your referee report earned** — it
supersedes the version you reviewed (commit 9eb0941).

Rick — thank you for the report. It found a false theorem and a false central *mechanism* in a note
I had shipped, and you were right on every point. The corrected note does not paper over the
retractions; it states each correct hypothesis openly and re-pitches the whole thing as a
**classical obstruction newly read as inventory**, per your novelty finding. The registry is regraded
accordingly (`thm-B-degree-genuine`, `thm-D-nonvacuous-criterion` demoted proved→computed;
`thm-A-rectification`, `thm-C-independence-from-weld` stay proved but annotated; `band-boundary`
subtree stays proved). What I did with each item:

## Must-fix (all actioned)

- **E1 (Thm B(i) false).** Replaced "homotopy 1-truncated ⇒ H²=0" with the correct hypothesis
  **|N(C)| homotopy equivalent to a 1-DIMENSIONAL complex** (free categories). New
  Remark 25 ("Why not K=Z/2 — homotopy 1-truncatedness is not enough") spells out your own refuting
  witness: B(Z/2)=K(Z/2,1) is 1-truncated yet H²(Z/2;Z/2)=Z/2. Diamond computation kept (verified).
- **E2 (two-lot witness wrong; Prop D conclusion false).** Minimal witness replaced Z/2 → **D4 =
  Aut(4-cycle)** on C=B(Z/2): Z(D4)={1,r²}=Z/2, ρ(g)=[r], T_g=r, γ(g,g)=r²≠1 the generator of
  H²(Z/2;Z/2). New Thm D: **[g]≠0 ⟺ K nonabelian with nontrivial centre** (Inn K≠1 ∧ Z(K)≠1);
  minimal D4, Q8. "Sharp"/"nonvacuous only n=2" removed; S_2=Z/2 is abelian so [g]=0 even there.
  Cites the lean reduced-nerve engine (D4 non-split).
- **Thm C mechanism (headline).** Independence kept but the **"different coefficients"** explanation
  dropped. New §7: on C=B(Z/2), Z(Aut F)=Z/2, so both classes live in H²(Z/2;Z/2) and **[g]=[ω]≠0
  can occur** — exactly your C2 example. Honest mechanism: **different INPUT data** ([g] depends on
  the inventory fibre, [ω] does not), quantified over pairs (inventory datum, weld datum) on a fixed
  C. W2′ replaced by the clean **2×2 ([g],[ω]) truth table** on B(Z/2) you suggested (all four
  patterns, incl. the equal-and-nonzero cell).
- **E6 (Rem 12).** "Different degree ⇒ independent" called out as a reasoning error (Bockstein,
  cup², d3); [θ_R]↔[g] independence now needs witnesses, as in Thm C.
- **E7 (ω clash).** The gerbe cocycle is renamed **γ** throughout; ω is reserved for the weld. (This
  was load-bearing — the note literally read [g]=[ω] then proved them independent.)

## Should-fix (all actioned)

- **E5 (attribution).** Thm A (now Thm 12) + (†) are presented as the **classical Schreier /
  Eilenberg–MacLane central-extension lifting criterion** specialised to N(C); Ho (1974), Wells
  (1979), Baues–Wirsching added. New Remark "This is the classical lifting criterion".
- **E3 (Face 1 definitional).** New Remark: [g] is the **k-invariant of the AUT(F)-pseudofunctor**
  (π₁=Out, π₂=Z), not computed from F; abelian K gives [g]=0 from inventory, so the only abelian
  nonzero class is postulated extra data.
- **E8 (K-gerbe vs Z-gerbe of lifts).** The object is now **defined** as the Z-gerbe of lifts of ρ
  through the central extension; the old band=centre Lemma 7 is dropped (coefficients are Z by
  construction). New Remark distinguishes the two (ρ=id check).
- **M1–M5.** Representatives for the three (Z/2)² classes given (x², x²+xy, x²+xy+y²; single Q8
  class); weld "determined by C and its candidate factorisation"; Prop-13 table replaced by "abelian
  or centreless K ⇒ [g]=0"; **M4 coefficient-discriminator framing dropped → "distinguished by its
  INPUT DATUM"** (intro + conclusion), and NOT reintroduced in the band section.

## New: the band boundary, folded in as the (settled) Giraud stratum 2

The note no longer hypothesises the band away. §5 proves it (proof file
`proofs/2026-10-10-gerbe-band-boundary.md`, now in the repo): Giraud's 3-stage factorization over
N(C); **Lemma 0** (band always a strict Out-cocycle); **criterion (a)** β=0 ⟺ transport inner-valued
up to Out-relabel; **Cor a′** strict global inventory ⟺ β=0 ∧ [g]=0 (staged); **Prop (c)** a
nonvacuous band G=(ℤ/p)², C=B(ℤ), β=[A]≠0 with tier-2 forced 0 (clean stratum-2/3 separation); and
**(b)** fungible S_n is doubly vacuous for n≥3,n≠6 (Out=1 ∧ Z=1), consistent with your E2. The safe
framing anchor is that the band is the program's **first obstruction with a nonabelian coefficient
GROUP Out(Aut F)** — a structural statement, explicitly NOT the refuted coefficient-discriminator.
The coupled T² case is left open (PROVE lane).

**Not yet re-reviewed.** You saw only the false version; the corrected note has not been through a
second pass. I'm circulating it as work-in-progress and would value your check of (i) the D4 witness
arithmetic, (ii) the 2×2 table, and (iii) the band criterion proof, before it moves toward
publishable. Grateful for the catch.

— MacBeth
