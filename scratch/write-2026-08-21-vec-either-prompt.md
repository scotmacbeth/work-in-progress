# Write scratch — two additions to `containers-over-vec.tex`

Date: 2026-08-21 (write session). Source spec: `state/WRITE.md` (Neil's 08-21 Vec email).
Target file: `projects/expository/containers-over-vec.tex` (~22pp, compiles clean).
**This is an extension of a polished note, not a new paper.** Honesty guardrails stay:
extensivity = CLW 1993; biproduct = standard; algebroid = Bénabou/Mitchell.

## The one sentence (piece 2, the load-bearing new idea)

> In `Vec`, "handle either prompt A or prompt B" is the **coproduct** of the two
> linear containers, and its extension is the corepresentable at the **biproduct**
> `A⊕B` — so being able to answer *either* is literally the same functor as being
> ready for *both*. That self-duality IS the biproduct collapse, read as a feature.

## Piece 1 — "The structure of Vec" recap (orienting, short)

Placement: NEW section right after §1 (The question, one-line answer), BEFORE Definitions.
Audience: fluent category theorist who simply hasn't used the `Vec` instance (Neil).

Content (side-by-side Set vs Vec):
- **What Vec HAS:** zero object (terminal = initial = 0); finite biproducts
  (finite coproduct = product = ⊕); all kernels & cokernels (abelian); enrichment
  over itself (hom is a vector space) — this last is what powers linear co-Yoneda.
- **What Vec LACKS vs Set:** NOT extensive (`∐ ⊊ ⊕`, CLW 1993); coproduct
  injections not disjoint / not complemented; no subobject classifier; terminal ≠ 1
  (so "shapes = F(1)" dies).
- **Punchline:** the SINGLE failure of extensivity is the whole story of the front.
  Cite the note's own collapse thm (\ref{thm:collapse}) and crux (\ref{thm:crux}).
  Keep it a recap — no proofs, forward-point to the sections that prove each item.

Do NOT re-derive; this section only *names* the structural facts and points forward.

## Piece 2 — Application: either-prompt = biproduct

Placement: NEW section AFTER §7 (Part 4, the matrix/algebroid section), BEFORE the
carry-over table. Rationale: it ties BACK to the collapse (§4) and FORWARD to the
matrix product `⊕_b P_ab⊗Q_bc` (§7); best placed while §7 is fresh, before the
scorecard table closes the arc. Keep prose sharable into a future applied section.

### The ML framing (attribute to Neil, keep visible throughout)
A response to a prompt is not one token but a distribution / superposition; the reply
space is a vector space whose basis the model learns. "Responses = uncertainty =
basis of learning." So: prompt with reply-space `A` ⇒ one-shape linear container
`𝖠 = ({*}, A)`, extension `h_A = Vec(A,−)`.

### The computation (uses ONLY existing lemmas — no new proofs)
- Coproduct in `LinCont = Fam(Vec^op)` = disjoint union of shape sets:
  `𝖠 ⊔ 𝖡 = ({*_A,*_B}, (A,B))`.
- Extension preserves coproducts: `⟦𝖠⊔𝖡⟧ = h_A ⊕ h_B`.
- **Lemma h (h additive / biproduct):** `h_A ⊕ h_B ≅ h_{A⊕B} = ⟦({*}, A⊕B)⟧`.
- `A⊕B` = biproduct = coproduct (either) = product (both) in Vec.
- ⇒ "either A or B" (coproduct of containers) = corepresentable at `A⊕B` =
  "one prompt with reply-space `A⊕B`" = "ready for both." **either = both.**

Proposition (either-prompt = biproduct). Proof = coproduct-in-Fam is disjoint union +
extension preserves coproducts + Lemma h. □  (all existing — cite \ref{lem:h}.)

### The reading (novelty = the framing)
- Neil's intuition: "coproducts survive but ALSO carry the universal property of
  products, so no loss of coproducts" — that IS the biproduct.
- Reframe the collapse (Thm \ref{thm:collapse}) NOT as degeneracy but as the *precise
  content* of either = both self-duality. The same additivity of `h` that ERASED
  shapes (a liability for a representation theorem) is here an ASSET: it is exactly
  what makes "either" carry the universal property of "both."
- Global vs local: the collapse `Id^N` is the global biproduct fact; either=both is
  its local face on a single coproduct. Same fact (additivity of h / ⊕ in Vec).

### Tie forward to the algebroid (§7)
- Responses compose two ways:
  - WITHIN one prompt: the `k`-algebra structure on `P` (single-shape ◁-comonoid =
    `k`-algebra, Prop \ref{prop:comonoid}). Composing a response with a response of
    the same prompt.
  - ACROSS prompts (a→b→c): the matrix product `(P⊙Q)_{ac} = ⊕_b P_{ab}⊗Q_{bc}`
    (algebroid, §\ref{sec:algebroid}). The `⊕_b` — sum over the intermediate prompt —
    is available precisely because Vec has biproducts.
- So biproducts do DOUBLE DUTY: they collapse shapes (either=both) AND power
  cross-prompt composition (the algebroid). The single ⊕ that gives "no loss of
  coproducts" is the same ⊕ that gives the composable-arrows sum.

## Housekeeping
- Update roadmap paragraph in §1 to mention the new recap + application sections.
- Add one compact clause to the abstract for the either=both ML hook (Neil wants it
  prominent).
- Update date line: "18 August 2026 (rev. 21 August 2026)".
- Recompile with pdflatex; check no new errors; run citation footprint check.
- No new citations needed beyond CLW (already in note) — biproduct is standard.

## Referee (hostile) checks to do at the end
- Does the recap only *name* facts it forward-references? (no orphan definitions)
- Is the either=both Proposition proof genuinely just existing lemmas? (yes: Lemma h)
- Is "biproduct = standard" attributed and not over-claimed as novel?
- Does the ML prose stay honest (motivation attributed to Neil, math self-contained)?

## DONE (2026-08-21)
Both pieces landed. `containers-over-vec.tex` → 27pp, `pdflatex` exit 0, no undefined
refs, no citation warnings, no serious overfull boxes (fixed the one pre-existing
companion-footer path overflow with `\sloppy`). Visual spot-check of pages 4 (recap)
and 18 (Prop 9.2 + either/both underbrace display) confirms clean rendering.
Referee checks all pass:
- Recap only *names* forward-referenced facts (no orphan defs). ✓
- Prop 9.2 proof = coproduct-in-Fam + Lemma h only; no new proof. ✓
- Biproduct attributed as standard; novelty scoped to framing + either=both. ✓
- ML motivation attributed to Neil; math self-contained. ✓
No new external citations / arXiv IDs; footprint unchanged.
Note for Robin: `memory/for-robin/2026-08-21-vec-either-prompt-writeup.md`.
Disclosure map updated. Email is off this session (write-session rule) — Robin reads
projects volume from host.
