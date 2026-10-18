# UNSENT covering note — deliver to Rick (CC Robin) at next WAKE

**Status:** WRITE session committed the rework but cannot email. NEXT WAKE must send this to
Rick (grandparick20@gmail.com) CC Robin (langer.robin@gmail.com).
See [[feedback-wake-must-deliver-unsent-write-covering-emails]].

**Thread:** reply to Rick's uid233 round-2 report ("Re: Weld = regular bicomodule -- review of
UID 412 (585de70): B' is closed, 2 MUST").

**Deliverable pushed to `work-in-progress`:**
- PDF/source: `papers/2026-10-18-weld-worker-bicomodule.{pdf,tex}`
- Content commit **`a452538`** (stamped on page 1); stamp commit `fcfd038`.
- GitHub: https://github.com/scotmacbeth/work-in-progress/blob/main/papers/2026-10-18-weld-worker-bicomodule.pdf
- Supporting: `scratch/write-2026-10-18-M1-selfcheck.py` (M1 re-derivation),
  `lean/2026-10-18-retract-bicomodule-map.lean` ([propext]).

---

## Draft email body

Subject: Re: Weld = regular bicomodule — rework for uid233 (content commit a452538)

Rick — round-2 report fully actioned; revised PDF pushed to `work-in-progress`
(`papers/2026-10-18-weld-worker-bicomodule.pdf`, content commit `a452538`). Thank you for the
B′-closure endorsement and the two sharp MUSTs — both landed, and the retract one changed the
paper for the better.

- **M1 (retract is not a bicomodule map).** Confirmed, and I re-derived your (2,2) witness
  myself (`scratch/write-2026-10-18-M1-selfcheck.py`; also Lean-certified, `[propext]`). `e`
  fails λ-equivariance at every non-constant `g` because it reads the branch at the *current*
  input while λ moves the input over all of S — on your witness the moved copy broadcasts
  g(1)=1 against g(0)=0. The paper now uses your fix `r_{s0}(s,g)=(s,const_{g(s0)})` as the
  genuine bicomodule retraction B ↠ B′ (both squares, idempotent, image = σ(A), restricts to
  id on B′), honestly flagged non-canonical, keeping every count (fibre m^{n-1}) and the same
  F̄. `e` is demoted to the set-level idempotent (its keep/discard combinatorics stand).

- **M2 (clause-2 verdict conflation).** Fixed. The verdict now states two labelled readings and
  never conflates them: *worker = content factor (−)^S* iff |T|=1; *worker = whole weld* (A=B,
  equiv. F̄_A=F̄_B) iff |S|=1 ∨ |T|=1. The (1,2) case is spelled out — A=B on the nose yet
  F̄_A=2V≠V=content — so the worker is the whole weld there but not the content factor.

- **S1.** Lemma now gives B = ∐_{g∈T^S} B_g (all B_g mutually isomorphic), identifies the
  coaction-closed subobjects as the S-saturated unions, and singles out B′ by the diagonal
  Δ:T→T^S (Yoneda), *not* by closure — correcting my earlier "closed because g fixed pointwise".
- **S2.** σ is now a genuine iso via cobase change π_!A of the regular (A,A)-bicomodule along
  π_S, π_T (built without reference to B, so non-circular). Remark states honestly the one
  residual item (general coaction-by-coaction identity, checked at five shapes).
- **S3.** Lemma proof text corrected: λ moves s, ρ fixes the whole position; no spurious ψ in δ_T.
- **N1/N2.** Fibre called *non-trivial* (size m^{n-1}>1); the redundant third refutation dropped.

Registry: clause2 & clause3 re-promoted computed→proved on this rework; root stays proved; the
Lean leaf stands. Trustcheck GREEN. — MacBeth

---

## After sending
Mark this file delivered (rename `*-SENT.md` or note the send date) and record the send in the
registry disposition for node `weld-is-regular-bicomodule`.
