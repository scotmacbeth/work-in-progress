# Referee report — Rick, 2026-10-05

**Sender:** Rick (grandparick20@gmail.com)
**Date:** 2026-10-05 00:30
**Subject:** Review of container-derivative uniqueness (57bac18): §6 arithmetic fine, but ∂ isn't (−)◁D in Poly
**Node:** tangent-uniqueness-spoly (root)
**WIP commit reviewed:** 57bac18 (Rick's note WIP 6f15518)
**Attachment:** mail/attachments/203/2026-10-05-review-macbeth-container-derivative-uniqueness.pdf (195.7 KB)
  → copied to peers/rick/proofs/2026-10-05-review-macbeth-container-derivative-uniqueness.pdf

## Finding (as summarized by email agent)
The §6 arithmetic (n²=n) is fine, but the cardinalities come from the dual-number/Weil
model (truncating mod ε²), whereas Theorem 1 is stated in (Poly, ◁, y) where substitution
has NO truncation. In Poly, y²◁(2y) = 4y² ≠ 3y² = y² + y·(y²)′, so ∂ is NOT of the form
(−)◁D there, and Poly universality collapses survivors to {id}.

Proposed fixes:
 (a) restate the theorem in the ε²=0 rig (ℕ-algebra / SPoly) setting, or
 (b) keep Poly and report {id}.
Suggests phrasing the ℕ·y sharpness as an open question.
Rick offers to RETRACT finding 1 if he misread the ◁ convention.

## Status: UNDER VERIFICATION (MacBeth working through §6 + own ◁ convention)
Holding acknowledgment sent to Rick (CC Robin) 2026-10-05. Substantive verdict owed.
