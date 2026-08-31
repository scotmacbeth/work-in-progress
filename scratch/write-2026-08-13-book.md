# Book WRITE session 2026-08-13 — welding Ch7 holonomy climax to the ZS chapter

## Target
New section: emergent holonomy of orchestration. Welds `sec:update-liftings-holonomy`
(Ch7 climax: liftings of ONE update monad ≅ Fun(𝔸(↓),Cat), holonomy = isotropy rep)
to `ch:zs` (Zappa–Szép, [ω]∈H² directed obstruction).

## Placement decision
END of `ch:zs`, AFTER `sec:threemodes` (currently ends ~line 4575), BEFORE the Phase-2
stub chapter (line 4577). New label `sec:emergent-holonomy`.

WHY after threemodes, not before / not last-Ch7-section:
- Needs BOTH the Ch7 holonomy machinery AND the ZS-product / [ω] machinery ⟹ must
  come after both. Ch7 is a different chapter; ZS is this one. So it lives in ch:zs.
- The astonishment ("two of the three modes secretly meet on ONE object") is strongest
  as a rug-pull right after the table that carefully separated State and Directed into
  different rows. Let the reader trust the tidy table, then pull it.
- Makes the true climax of the composition chapter + substantive book.

## Honesty reconciliation with threemodes (CRITICAL)
threemodes says: DON'T collapse the three obstructions into one master class — false.
My section does NOT contradict this. It shows two modes (State/isotropy holonomy,
Directed/[ω]) can be carried by ONE composition (the ZS product of two update agents).
Different claim: not "one obstruction", but "one object bearing two". State this
explicitly so there is no apparent contradiction.

## [ω] site honesty (CRITICAL — do not conflate)
- thm:h2 handoff class: [ω] ∈ H²(Sk_C ; D)  (Baues–Wirsching, handoff category)
- my (c') stabiliser class: [ω] ∈ H²(B ; A)  (group cohomology of point-stabiliser)
- SAME ℤ/2 dichotomy, SAME generator, DISTINCT sites, NOT the same class. Flag it.
  (Proof file §3 insists; WRITE.md insists; Ch7 teachbox already calls it a "sibling".)

## Monoid-anchor consistency
Composition = ZS product of two MONOIDS P, P' (prop:monoidanchor), acting on S.
NOT the mis-reading corrected in that footnote (single update monad as ZS product).
Note this to stay consistent.

## Astonishment arc (WRITE.md)
1. One threading agent has holonomy (recall Ch7).
2. Compose two — naive guess: composite holonomy = ZS product of the two stabilisers.
3. REVERSAL: containment always, PROPER generically. S₃ witness worked concretely.
   Composite fixes a state neither leg fixes ⟹ emergent reentrancy.
4. Resolution: h(s) = |(P·s)∩(P'·s)| = |A\U/B| = |Stab_G|/(|Stab_P||Stab_P'|).
   h(s)=1 ⟺ orbits meet only at s ⟺ aligned ⟺ [ω]∈H²(B;A) analysis applies.
   [ω]=0 ⟺ E≅A×B ⟺ unentangled clean product.

## S₃ witness (do the permutation computation in text — finite, vivid)
G=S₃ on {1,2,3}; P=A₃=⟨(123)⟩, P'=⟨(12)⟩ (exact: every g = p·p' uniquely).
At s=1: P·1={1,2,3}, P'·1={1,2}, meeting M={1,2}, h(1)=|M|=2.
Non-identity loop: 1 —(12)→ 2 —(132)→ 1. Fixes 1, but neither (12) nor (132) fixes 1.
Stab_P(1)=Stab_{P'}(1)={e}; composite holonomy = C₂ = ⟨(23)⟩. Emergent generator = the
surplus meeting point 2.

## Citations (ALL already in bib — no new bibitem)
- AhmanUustalu13 (update monads)
- RW (Rosebrugh–Wood: distributive laws ↔ factorisation)
- BW85 (Baues–Wirsching H²)  [only if needed; thm:h2 already carries it]
- internal labels: thm:update-classification, def:action-category, ex:z2-holonomy,
  sec:zscriterion, prop:monoidanchor, thm:h2, sec:threemodes, ch:zs
Skip skew-brace (Rathee–Yadav) — optional per WRITE.md, not a container cite, not in bib.

## Depth (book level)
- (a) classifier composes: statement + one-line mechanism.
- meeting-points theorem: state h(s) = three equal quantities; ratio-is-integer via
  disjointness at teachbox level (P ∩ gP'g⁻¹ = {e}); do NOT reproduce full bijection proof.
- (c'): "there is [ω]∈H²(B;A), =0 iff composite splits"; the ℤ/2 table; NO cocycle derivation.

## Grant close
"Orchestration can synthesise holonomy the parts lack; a degree-2 cohomology class
certifies when the composite is a clean product of the parts." Operational: an auditor
computes h(s) = crossings of the two agents' reachable-state orbits directly — no
cohomology needed to DETECT emergence, only to classify the aligned case.
