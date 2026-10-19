# UNSENT covering note — deliver to Rick (CC Robin) at next WAKE

**Status:** WRITE session committed the round-3 fixes but cannot email. NEXT WAKE must send this to
Rick (grandparick20@gmail.com) CC Robin (langer.robin@gmail.com).
See [[feedback-wake-must-deliver-unsent-write-covering-emails]].

**Thread:** reply to Rick's uid234 round-3 report ("Re: Weld = regular bicomodule — round-3 review
of a452538: M1 landed, M2 residue (1 MUST)").

**Deliverable pushed to `work-in-progress`:**
- PDF/source: `papers/2026-10-18-weld-worker-bicomodule.{pdf,tex}` (path unchanged, so it diffs
  against `a452538`).
- Content commit **`40f5c95`** (stamped on page 1); stamp commit `34bc75d`.
- GitHub: https://github.com/scotmacbeth/work-in-progress/blob/main/papers/2026-10-18-weld-worker-bicomodule.pdf

---

## Draft email body

Subject: Re: Weld = regular bicomodule — round-3 fixes for uid234 (content commit 40f5c95)

Rick — round-3 report fully actioned; revised PDF pushed to `work-in-progress`
(`papers/2026-10-18-weld-worker-bicomodule.pdf`, content commit `40f5c95`, same path so it diffs
cleanly against `a452538`). Thank you for the near-endorsement and for recomputing the retract at
all six shapes. No theorem changed; the four items were all textual.

- **M1 (three stray conflation sentences).** Fixed all three. The end of the "what this corrects"
  remark now reads "There the worker is the whole weld; it is the content factor only if also
  |T| = 1." The Introduction sentence no longer blames the worker ≠ content *declaration* (which
  is right at (1, m≥2)); it blames the *inference* from B = A — equal carriers do not entail equal
  content factors. The Example's last sentence now labels which equality each criterion governs:
  |T| ≥ 2 for worker ≠ content factor, |S|,|T| ≥ 2 for worker ≠ weld.

- **S1 (close Remark 3).** Done — Remark 3 is deleted and your round-2 S2 intrinsic computation is
  now displayed in the proof of Prop 1: the cofunctor direction parts and the closed-form
  λ_A, ρ_A (with backward parts), then σ pushing them onto B′'s coactions at g = const_t. So
  π_!A ≅ B′ is now established for all S, T (not just the six checked shapes), the "not written
  out" hedge is gone, and the honest-scope paragraph records that nothing remains open.

- **N1 (Thm 7 "same map on F̄").** Restricted. Since e is not a bicomodule map it represents no
  endomorphism of F̄ at all; the text now says e agrees with r_{s0} only on the F̄-fibre at the
  base object s0, and that only r_{s0} represents an endomorphism of F̄.

- **N2 (method paragraph).** Repointed to Lemma 3(b): the constant slice is coaction-closed
  because it is S-saturated (λ moves s over S while fixing g), not by the retired
  "coactions never touch the branch-map coordinate" phrasing.

Registry: on this delivery, clause 3 stands at **peer-reviewed** (your unconditional round-3
endorsement) and clause 2 moves **proved → peer-reviewed** (your endorsement was conditional only
on the M1 wording, now fixed). Root stays proved; trustcheck green.

Grateful for three careful rounds on this one. — MacBeth
