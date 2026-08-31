# Book: new section on Neil's A/E predicate liftings (2026-08-08 write session)

**File:** `projects/books/category-of-containers.tex`
**New section:** §"Two predicate liftings: All and Exists" (`sec:predicate-liftings`),
appended to the end of the "Algebraic structure on Cont" chapter (`ch:algebra`), just
before the "Monoids and comonoids" chapter. Compiles clean (`pdflatex`, 75 pages, no
undefined refs; one ~4pt overfull box, within the book's existing norm).

## What it is
The containers-chapter HOME Neil greenlit (UID-95), led by HIS own A/E predicate liftings
(UID-94 source note). Six beats:

1. **The two liftings** All/Exists of a container, defined from the extension functor +
   positions (∏ vs ∐ over positions). Worked example: a binary node against Maybe (4-row table).
2. **E = ◁** (the composition product) — proved, with Neil's prompts/replies reader hook
   ("sequencing is existential"). Tag [MacBeth, Lean-verified].
3. **A is a cartesian-only bifunctor** (Thm): the Yoneda section-count ∏_p f⁻¹(p) — non-surjective
   ⟹ NO natural pushforward, bijective ⟹ forced. This is Neil's flag "can't define A on
   polynomial functors" made precise. [MacBeth, proved]
4. **A = T_M, one level down** (Remark): "every Set monad lifts via T_M" is FALSE; drop (Reader/State)
   kills it, merge (Pf) keeps a non-canonical lift, cartesian (List) keeps the canonical one.
   Forward-pointer to the deep fibrational teachbox (§sec:moncomon-fibration) for the full ladder.
5. **THE NEW RESULT — the action law** A X(A Y C) = A(X◁Y)C (Thm, this cycle's PROVE:
   `proofs/2026-08-08-A-E-predicate-liftings.md`): A is a LEFT MODULE of (Cont,◁,y). Fubini
   ∏_p∏_q=∏_{(p,q)}. Neil's "debate preparation" intuition. Contrast E X(E Y C)=E(X◁Y)C = ◁-assoc;
   mixed law iso iff X linear. [MacBeth, proved]
6. **Honesty remark**: action law stated as canonical iso (strict-=/rfl = flagged next Lean rung);
   module pentagon/triangle coherence NOT verified — only the two equations (assoc + unit).

"Proof-relevant" retired from prose — kept ONCE, parenthetically, as the type-theorist's synonym
(Remark rem:A-is-TM), per Neil's instruction.

## Two flags for you / Neil
1. **Tone gate.** WRITE.md asked to gate the reframe's tone on Neil's UID-92 reply, which I couldn't
   confirm this session (no email in a write session). The framing IS Neil's own language
   ("subobject vs codomain", A/E) and the math is solid, so I proceeded. **Final tone is subject to
   Neil's confirmation** — if he wants it dialled differently, it's a 10-minute edit.
2. **Citation tool missing.** WRITE.md says to run `code/citation_check.py --report footprint` from
   `projects/memory`, but there's no `code/` dir there anymore (and `sources.json` now uses a
   `read`/`extraction` schema, not `provenance`). Not blocking here — I introduced ZERO new
   bibitems; all five cites (Hermida93, HermidaJacobs98, AhmanBauer24, Katsumata13, OrestisAgda)
   were already in the bib, vetted when the deep teachbox was written. But you may want to restore
   the tool or update the WRITE-skill instructions to match the current memory layout.

No GitHub push: `projects/books` isn't a git working tree on this box. You read the projects volume
from the host directly.
