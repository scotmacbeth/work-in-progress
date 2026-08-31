# Write session 2026-08-21 — either-prompt = biproduct, + Vec-structure recap

**File:** `projects/expository/containers-over-vec.tex` (now 27pp, compiles clean, 0 warnings).
**Driver:** `state/WRITE.md` — Neil's 2026-08-21 Vec email. Applied-half deliverable.

## What I added (two pieces, both requested by Neil)

### 1. New §2 "The structure of Vec, for the container-minded"
A short orienting recap for a category theorist who hasn't used the Vec instance
(Neil's self-description). Side-by-side Set/Vec. No proofs — every fact forward-points
to the section that uses it.
- **Vec HAS:** zero object (terminal=initial=0); finite biproducts; kernels/cokernels
  (abelian, idempotents split → Krull–Schmidt); self-enrichment (powers linear co-Yoneda).
- **Vec LACKS vs Set:** extensivity (∐⊊⊕, CLW 1993); disjoint/complemented injections;
  subobject classifier; a shape-detecting terminal (F(1)=S dies, F(0)=0).
- **Punchline:** the single failure of extensivity is the whole note.

### 2. New §9 "Application: handling either prompt is the biproduct"
The ML-facing hook Neil asked for. Prompt with reply-space A = one-shape linear
container ({*},A), extension h_A = Vec(A,−).
- **Prop 9.2 (either-prompt = biproduct):** coproduct of prompt containers
  ({*},A) ⊔ ({*},B) = ({*_A,*_B},(A,B)); its extension is
  `h_A ⊕ h_B ≅ h_{A⊕B} = ⟦({*}, A⊕B)⟧`. Proof is *only* existing lemmas
  (coproduct-in-Fam = disjoint union of shapes + Lemma h additivity). No new proofs.
- **The reading:** A⊕B is the biproduct = coproduct (*either*) = product (*both*).
  So "answer either" and "ready for both" are the SAME object. Over Set they split
  (A⊔B ≠ A×B). Neil's intuition ("coproducts survive but carry the product UP, no
  loss") IS the biproduct — I frame the collapse (Thm 5.x) not as degeneracy but as
  the precise content of either=both self-duality. Same additivity of h that erased
  shapes (a liability for a rep theorem) is here the asset. Global collapse Id^N vs
  local either=both are one equation `h_A⊕h_B≅h_{A⊕B}` with opposite valuations.
- **Tie forward to the algebroid (§8):** responses compose two ways —
  *within* a prompt via the k-algebra on P (single-shape ◁-comonoid, Prop comonoid);
  *across* prompts via the matrix product ⊕_b P_ab⊗Q_bc. The ⊕_b is available for
  exactly the reason of §9: Vec has biproducts. So the biproduct does double duty —
  either=both AND the composable-responses sum. Kept "responses = uncertainty = basis
  of learning" (attributed to Neil).

Also: added a carry-over-table row, a clause to the abstract, roadmap updates, and a
sentence to the grant conclusion so the applied face is visible there.

## Honesty ledger
- Novelty = the container-theoretic framing + either=both reading ONLY. Biproduct =
  standard; extensivity = CLW 1993; algebroid = Bénabou/Mitchell. New §9 provenance
  box states this; prompt/response motivation attributed to Neil (2026-08-21 corr.).
- **No new external citations / arXiv IDs** introduced — footprint unchanged.

## TODO / not-this-session
- Sharable into the separate applied section Neil flagged (Workers/Vec) — the §9 prose
  is written to lift out cleanly.
- Nothing proof/Lean broke; no gaps discovered while writing.

Scratch: `projects/scratch/write-2026-08-21-vec-either-prompt.md`.
