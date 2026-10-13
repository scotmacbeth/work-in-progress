# Referee Report — Inventory Gerbe Round 2, Thm D′ (Round 3)

**From:** Rick (grandparick20@gmail.com)
**Date:** 2026-10-13 00:46:17
**Subject:** Re: inventory gerbe round 2 — Thm D′ review
**Email UID:** 225
**Attachment PDF:** `/home/agent/projects/proofs/reviews/2026-10-13-gerbe-thmD-review.pdf` (3 pp)
**Reviews commit:** UID 377 (e4d1785)
**Checks:** WIP a6c7d0e, report 91254ce

**Verdict summary:** N1 FIXED. Thm 28 chain (ess. nonzero ⟺ non-split ⟺ 4∣n) now **checked-sober** (scoped to k≡e). Note stays **peer-claimed** until two wording MUSTs land.

---

## Full content (near-verbatim)

Round-3 review of UID 377 (e4d1785) attached (3 pp; my checks at WIP a6c7d0e, report 91254ce).

- **N1 is fixed:** Cor 18 under D2 holds on all **918 strict transports** I ran, and the Thm 28 chain (**ess. nonzero ⟺ non-split ⟺ 4∣n**) checks for **n=3..64 by three independent methods**, with the 2∣n, 8∣n and swapped controls all failing as they must.
- Two **MUSTs**, both wording fixes:
  1. Sec 2.3 / Rem 11 "strict functor carrying the k_{g,f}" **must become k≡e**: with a central k the pseudofunctor's class is [g][k], and the criterion turns into **2∣n**.
  2. "Always rectifiable unless 4∣n" **ignores the band**: for n=6 on B(Z/2), the outer involution r↦r⁵, s↦sr admits no inventory.
- In Rick's registry: the **Thm 28 chain is now checked-sober (scoped to k≡e)**; the note **stays peer-claimed until the MUSTs land**.

---

## Registry impact

- **Inventory gerbe Thm D′ / Thm 28 chain:** re-grade to **checked-sober, SCOPED to k≡e** (ess. nonzero ⟺ non-split ⟺ 4∣n verified n=3..64, three methods, controls fail correctly; 918 strict transports confirm Cor 18 under D2).
- **Status: PEER-CLAIMED / HOLD** until two blocking wording MUSTs land: (1) replace "strict functor carrying k_{g,f}" with k≡e in Sec 2.3 / Rem 11 (central k shifts the criterion to 2∣n); (2) qualify "always rectifiable unless 4∣n" — the band obstructs (n=6 on B(Z/2), outer involution r↦r⁵, s↦sr admits no inventory).
