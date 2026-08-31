# Write session 2026-07-24 — fold closed-convolutional CLASSIFICATION into book §sec:closed

## Target (WRITE.md)
Add the positive classification of closed convolutional tensors to `books/category-of-containers.tex`
§`sec:closed`, right after the collapse witness (`sec:vacuity`). Ship BOUNDED theorem + honest
FURTHER-WORK caveat (PROVE did NOT crack the infinite-arity gap: registry `gap-infinite-arities` =
speculative, 2026-07-24 file is a further-work note).

## Source
- `proofs/2026-07-23-closed-convolutional-tensors-classification.md` (main theorem, bounded)
- `proofs/2026-07-24-arity-gap-further-work.md` (why infinite gap is open; Lemma A/Prop B/Prop C)
- registry `proofs/registry/closed-tensor-classification.json`

## Structural decisions
1. **Canonical file = `projects/books/category-of-containers.tex`** (NOT papers/ — doesn't exist;
   skill's path ref is stale). Baseline compiles clean: 38 pp.
2. **Replace the Conjecture `conj:closedconv`** (lines ~1021–1032) — it is now a THEOREM in the
   bounded case. Keep the tautness/cartesian-η mechanism paragraph (genuine insight into WHY collapse
   fails) but retarget its closing sentence from "sufficiency open / conjecture" to a hand-off into
   the classification.
3. **New subsection `\subsection{The complete list}` (`sec:classification`)** after `sec:vacuity`,
   before `\subsection{The other three, and a boundary}`. Arc per WRITE.md:
   biconditional (there) → collapse (there: condition is real) → classification (new: exactly which
   survive).
4. **Compute-first**: lead with normal form + the two running examples' affine data, THEN the three
   moves. Book voice ("Why, in two breaths" proofs, teachbox tradition).
5. **The heart** (WRITE.md): the symmetry identity `B+D_B×X ≅ X+D_X×B ⟹ D_X=1+S×X`. Give it its own
   Lemma (`lem:symid`), present cleanly. It is the one genuinely new lemma.
6. **Honest gap**: `\begin{Remark}[The infinite-arity boundary]` — κ²=κ defeats counting; affine =
   connected-COLIMIT preservation, closure gives connected-LIMIT only (independent); R_2=y+y^λ is a
   formal fixed point ⇒ counting is blind; obstruction (if any) = element-level pentagon. Also flag
   non-symmetric (left-closed ⊉ right-closed) as open. NOT dressed as a near-certain conjecture.

## Proof skeleton being written (all bounded-case steps `proved`)
- Lemma (unit small): |I|≤1. R_1(I)=I⋆1=1 + polynomiality ⇒ no unit ≥2.
- Degree multiplicativity d(C⋆B)=d(C)d(B) from R_B∘R_C≅R_{C⋆B} (associativity) → Key Lemma: finite
  κ≥2 ⇒ κ²>κ contradiction ⇒ all R_B affine.
- Reconstruction: I=1 ⇒ ×; I=∅ ⇒ symmetry identity ⇒ D_B=1+S×B ⇒ ∨_S.
- Main Theorem (bounded): × (⊗) or ∨_S (▷_S), ∨_∅=+ ↦ ×_Cont.

## Provenance
- families ×,∨_S / images ⊗,▷_S = prior/own art (Spivak; already cited in section).
- biconditional (closure ⟺ poly) = MacBeth (already `thm:uniformclosed`).
- classification + Lemma 1 + degree-mult + Key Lemma + symmetry-identity reconstruction = [MacBeth,
  bounded arity]. Tag theorem + symmetry lemma + infinite remark.
- Cardinality corroboration = scratch scripts (footnote, computed).

## Grade discipline
bounded theorem = proved; unconditional/infinite = OPEN (stays out of theorem scope, lives in Remark).

## Status — COMPLETE
- [x] edit mechanism paragraph tail (retargeted to hand off to classification, no conjecture)
- [x] delete conjecture, insert classification subsection `sec:classification` ("The complete list")
- [x] compile clean — 40 pp, no undefined refs, conj:closedconv fully removed
- [x] revision pass: fixed "whose does not" ellipsis + clarified I=1 empty-set chase
- [x] citation_check footprint — new subsection has NO \cite (no provenance regression; floor
      agent-summary is pre-existing from 2405.13157 elsewhere in book)
- [x] update PROGRESSIVE_DISCLOSURE.md §Papers (new bullet); collaborator note
      memory/for-collaborator/2026-07-24-classification-in-book.md

## Delivered
- Theorem[the complete list, bounded arity] [MacBeth]; Lemma[unit small], Lemma[bounded degree
  forces affine], Lemma[the symmetry identity] (the heart); Remark[the infinite-arity boundary]
  (honest open gap, Neil's further-work discipline).
- No git push attempted (repo access is policy-limited per memory; Robin reads projects/ volume
  directly from host). If a future session regains access: push books/category-of-containers.tex.
