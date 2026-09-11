# Referee sign-off — m-container paper revision (Rick, 2026-09-11)

**Reviewer:** Rick (grandparick20@gmail.com)
**Received:** 2026-09-11 (email UID 166, subject "M-containers revision — sign-off with one clarification")
**Paper:** `papers/mcontainers-codensity-polynomiality.tex`, revision reviewed at wip commit `3a8bb3c` (29pp; stamped `487982c`).
**Corrected/clarified version after this sign-off:** wip commit `d63c0ce`.
**Prior referee report (ACCEPT w/ minor revisions):** `reviews/2026-09-10-m-containers-thm3-arc.md` (paper 70becd9).

## Outcome
**ACCEPT-with-minor-revisions loop CLOSES.** This is the sign-off on the referee-revision pass. Rick
confirms the revision is CLEAN on every major point:

- The corrected headline **Δ_{C₂} ∉ 𝒮** landed correctly in the abstract, revision-note, and
  dividing-line statement.
- The buggy `O_{2,C₃}` "commutative-μ" result was dropped; the M1 counterexample is now `O_{μν}`.
- **Prop 5.21 (the exhaustive characterization Δ_{C₂}∈𝒮 ⟺ M1∨M2), Lemma 5.19–5.20 (Witness Lemma),
  and Thm 5.22 (the escape criterion (i)+(ii) ⟹ necessity) are "tight."**

## The one clarification (non-blocking)
Rick flagged the parenthetical at the bottom of p.24 (near Corollary 5.23): the claim that a second,
non-absorbed nullary "contributes only a trivial direct factor to every stabilizer" was asserted
without argument. He offered two options — (a) drop the parenthetical, or (b) add a one-line
justification ("the rigid peg is fixed pointwise by every automorphism, so it factors out as ×1").

**Resolution (MacBeth, 2026-09-11):** took **option (b)**. Edited the parenthetical to read that the
second nullary, "as a uniquely labelled rigid leaf … is fixed pointwise by every automorphism of any
tree in which it occurs, so it contributes only a trivial ×1 direct factor to every stabilizer." Applied
in commit `d63c0ce` (recompiled clean, 29pp). Loop closed.

## Registry effect
Rick's endorsement of Prop 5.21 / Lemma 5.19–5.20 / Thm 5.22 is peer review of the corrected
dividing-line result. Node `commutative-mu-corrected-dividing-line` promoted `proved → peer-reviewed`
on this artifact. (The eight §5 THM-3-arc nodes were already promoted to `peer-reviewed` on the
2026-09-10 report; this sign-off additionally covers the corrected §5.9 that replaced the buggy result
he had originally refereed.)

## Also in the email (non-registry)
- UID 156 (separate, 2026-09-11): Rick endorses the biconditional framing and offers to review the
  all-m induction step (μ-commutative propagation, Hopf-composition intuition from his CQF work) if
  MacBeth lands it — that would be substantive and must go as a PDF per PROTOCOL §2.
- P.S. unrelated Hikita/Macdonald weather report.

*Source: faithful paraphrase of UID 166 via the session's email agent; email left unread in the inbox
for the verbatim record.*
