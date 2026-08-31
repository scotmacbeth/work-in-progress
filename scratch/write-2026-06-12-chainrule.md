# Write session 2026-06-12 — §6.2 The derivative and the chain rule

## Task
Promote the derivative from a stub *bullet* in Ch6 (Functors over Cont) to a worked
**section §6.2**, centred on the now-proved container chain rule.
Raw material: proofs/2026-06-12-container-chain-rule.tex (already reader-friendly).
Target: papers/category-of-containers.tex (the living book). Audience: Neil + reviewers.

## Phase 1 — the one sentence
> The container derivative ∂ satisfies a chain rule ∂(G◁F) ≅ (∂G◁F)×∂F — Leibniz for an
> *indexed* product — so the one-hole-context operation is compatible with the very
> composition product ◁ that organises the book.

Why it earns a section: it is the **first genuinely original functor-level theorem** in
the book, and it interacts with ◁ (the central operation). The free/cofree section (§6.1)
is mostly cited-in-substance; this is [MacBeth, Original].

## Skeleton of §6.2 (section inside an existing chapter — NO local abstract)
1. Lead ¶: ∂ : Cont→Cont, one-hole contexts/zippers; the question is its interaction with ◁.
2. Def: derivative (book notation \cont S P). [Cited: AAGM derivatives 2003]
3. Prop (basic calculus): ∂Id≅1, ∂K_A≅0, sum rule, Leibniz. Stated [Cited: AAGM]. Short —
   these are the classical rules; they set up the chain rule and the y² check.
4. Lemma (pointed-domain splitting): the crux. Flag classical logic / decidable point.
5. Theorem (chain rule) [MacBeth]. Proof restructured: KEY IDEA FIRST (indexed Leibniz),
   then explicit shape + position bijection, tightened from the proof file.
6. Payoff ¶ "where the two factors come from" — keep, it is the intuition.
7. Remarks: y² sanity check (1 line), Faà di Bruno (1 line), computational verification
   (23 finite containers), Lean status.

## Provenance decisions (honesty)
- Derivative def + sum + Leibniz: [Cited: AAGM 2003] (Derivatives of Containers).
- Chain rule under ◁: [MacBeth]. NOT machine-checked. PR #13 formalised ◁ (unit/assoc/
  extension law) but NOT the chain rule itself → footnote: "Lean ◁ infrastructure in
  Cont.lean (PR #13); a Lean proof of the chain rule is pending." Matches proof-file status.
- Univalent case: Joram–Veltri arXiv:2512.17484 — cite alongside, classical case consistent
  with our Lemma (set-truncation = our excluded-middle splitting).

## New bibitems needed
- AAGM03 "Derivatives of Containers" (Abbott–Altenkirch–Ghani–McBride, TLCA 2003 / 2005).
- JV24 Joram–Veltri arXiv:2512.17484.

## Notation reconciliation (proof file → book)
- \tri → \triangleleft (book has \cont{S}{P}); \pd → \partial (add nothing, use \partial).
- inl/inr: book preamble has no macro → use \mathsf{inl}/\mathsf{inr}.
- product ×: book Prop prod positions are P1 ⊔ P2 (disjoint union) — matches RHS (positions add). OK.

## Other edits in the file
- Chapter intro (l.623–624): "one exception §6.1" → "two worked sections §6.1, §6.2".
- Candidate-examples derivative bullet (l.636–640): change "targets here" → now a result,
  point to §6.2; keep zipper sentence.
- Reading tracker: add AAGM Derivatives + Joram–Veltri rows.

## Cut discipline
Proof file has: full atoms section, remark on classical logic, status itemize. For the
book: compress atoms to one Prop, fold status into the prov-tag + one footnote + one
verification remark. Target ~ one page of the chain rule, not the 9-page note.
