# Referee Report — Floor Theorem + Capstone M1–M3

**From:** Rick (grandparick20@gmail.com)
**Date:** 2026-10-13 00:37:02
**Subject:** Re: floor theorem + capstone M1–M3 — review
**Email UID:** 223
**Attachment PDF:** `/home/agent/projects/proofs/reviews/2026-10-13-floor-theorem-review.pdf` (4 pp)
**Reviews commits:** UID 382 (e306ae5 capstone) and UID 383 (f19cfcb D1-vs-D2 note)
**Checks:** github.com/grandpa-rick/work-in-progress scripts/day238, WIP 2910aff

**Verdict summary:** Floor "proved" is FAIR once Thm 1.3 is corrected and "α strict" is adopted as the standing hypothesis. M2/M3 fixed. M1 only half-fixed. Band-boundary: NO re-promotion yet.

---

## Full content (near-verbatim)

Review of UID 382 (e306ae5) and 383 (f19cfcb) attached (4 pp; checks at github.com/grandpa-rick/work-in-progress scripts/day238, WIP 2910aff).

- M2/M3 are **fixed** and the §3.2(ii) sign is right (also eq. (5) for nontrivial actions).
- **M1 is only half-fixed:** Def 4 as printed takes T strict with no k in the equation, so it fails on non-strict alpha (B(Z/3), D4) even though beta=0 and [g]=0.
- The floor dichotomy 1.1 / 1.2 / Prop 7 / 1.4 **checks out for strict alpha** (0 failures over 248 cases, controls fail as they must).
- BUT the "gap exactly when the centre is too small" characterisation in **Thm 1.3 / abstract / Upshot is FALSE** (D4 on B(Z) with c_s already separates).
- The **abstract states D2 => D1** (incorrect).
- **§2 cites clause (a) where it is false** for non-strict alpha.
- Answers to MacBeth's three questions and the grade call are in §3–4 of the PDF.
- Grade call: **no re-promotion of band-boundary yet**; floor "proved" is fair once 1.3 is corrected and "alpha strict" is the standing hypothesis.

---

## Registry impact

- **Floor D1/D2 dichotomy:** re-grade to **"proved" CONDITIONAL** — holds under standing hypothesis "α strict" AND after Thm 1.3 / abstract / Upshot are corrected (remove the false "centre too small" characterisation and the false D2⟹D1 claim; fix §2 clause (a) citation; repair Def 4 / M1 to handle non-strict α or scope it out).
- **Band-boundary:** HOLD — no re-promotion.
- The strict-α dichotomy itself is machine-corroborated (0/248 failures, controls fail correctly).
