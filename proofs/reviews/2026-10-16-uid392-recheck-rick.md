# Referee recheck — UID 392 (δ-quadratic, capstone couples-on-torus, two-ends)

- **Reviewer:** Rick (grandparick20@gmail.com)
- **Received:** 2026-10-16 00:27 (inbox UID 230)
- **Subject:** Re: UID 392 remaining 3 MUSTs landed — recheck: all landed, zero MUSTs open
- **Attachment:** `2026-10-16-recheck-macbeth-uid399.pdf` → saved here as
  `reviews/2026-10-16-uid392-recheck-rick.pdf`
- **Registry:** `supply-chain-inventory-gerbe-h2.json`
- **Nodes endorsed:** `delta-is-quadratic-map-polarization-chi` (A),
  `coupled-T2-general-delta-lemma` / `coupled-T2-d2-witness` (B, capstone),
  `gerbe-two-ends-correlation` + `gerbe-two-ends-nilpotent-extension-rick` (C)

## Bottom-line verdict (quoted)

- "All three MUSTs have LANDED. Remaining MUSTs: 0."
- "The 'no theorem statements changed' claim holds. No Theorem, Lemma or Corollary
  statement differs, including in the `.tex` diff."
- "Registry: the δ-quadratic node can move to checked-sober. The capstone and
  two-ends notes are ready."
- Caveat: "no statement's truth value changed except Cor. 5, which went from false
  to true via the intended hypothesis. I accept 'wording only' with that one caveat."

This is a **clean endorsement with zero open MUSTs** — a peer-review promotion event
(Rick's "checked-sober" = my `peer-reviewed`). The MUSTs A/B/C correspond to the
prior-round items M3, M1, N1.

## Verification of record

- MacBeth artifacts verified byte-identical: WIP content commit `16b051d`, stamp
  `05f773d` (both ancestors of HEAD; three PDFs byte-identical to `papers/*.pdf` at HEAD).
- Rick WIP base: `d809aa2`. Prior-check content reference: `3954636` (his 2026-10-15 check).

## One new SHOULD (not a MUST) — two-ends §8, l.299–300

Current prose overstates to an iff that MacBeth's own S₃ / A₄ controls refute
(S₃, A₄ have no central commutator yet show no δ-coupling):
- Current: "…the central end can be switched off while the strictification end couples
  **precisely when** no nontrivial commutator is central".
- Suggested: "So the central end is switched off exactly when no nontrivial commutator
  is central, and in that regime the strictification end can still couple (Dih(C₃²),
  though not S₃ or A₄)."

## Tone note (SHOULD, fold in) — two-ends title/abstract

- Suggested title: "The two T² gerbe ends are not independent: δ-coupling forces
  [𝔤]-coupling".
- Abstract: replace "a forced one-way correlation" with "a one-way implication"; after
  the display add: "For nilpotent K the central class couples exactly when K is
  nonabelian, so the implication amounts to 'δ couples ⇒ K nonabelian'; the converse
  fails (K = D₄). The substantive question is which nonabelian K δ-couple."

## Three nits (capstone)

1. l.135–136: "A nontrivial central datum k_{g,f} ∈ Z(K) … would shift the sharp line
   of §5" — a central k does not change α (conj(k)=id); it only twists the lifting
   equation. Fix: "would twist the lifting problem by [k] ∈ H²(N(C); Z(K)); excluded here".
2. l.171/178/189: retained-datum terminology inconsistent ("central lifting datum" vs
   gloss "the section-lift defect g" — but g is the obstruction, not the datum). Fix:
   use "the lift T through the central extension (II)" in all three places.
3. Def. 4, l.167: "lifting the inner transport" presupposes β=0; the display lifts
   μαμ⁻¹. Fix: "lifting the gauged transport μ·α·μ⁻¹".

## Action taken (MacBeth, 2026-10-16 WAKE)

- SHOULD + tone note + three nits applied to `papers/2026-10-13-two-gerbe-ends-...tex`
  and `papers/inventory-gerbe-couples-on-torus.tex`; recompiled; pushed to WIP
  (see covering email). No theorem statements touched.
- Registry upgrades to `peer-reviewed` recorded against this artifact.
