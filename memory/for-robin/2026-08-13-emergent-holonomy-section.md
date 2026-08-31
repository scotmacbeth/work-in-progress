# For Robin — new book section: emergent holonomy (the Ch7↔ZS weld)

**2026-08-13 WRITE session.** Book: `projects/books/category-of-containers.tex`
(compiles clean, `pdflatex`, 91pp, 0 undefined refs, no new bibitems).

## What landed
A new section **"When two of the modes meet: emergent holonomy"**
(`\label{sec:emergent-holonomy}`), placed as the **last section of the Zappa–Szép
chapter** (`ch:zs`), immediately after `sec:threemodes`. It is the long-planned weld
between:
- the Ch7 climax (`sec:update-liftings-holonomy`): liftings of ONE update monad ≅
  `Fun(𝔸(↓),Cat)`, holonomy = isotropy representation; and
- the ZS chapter's directed obstruction `[ω]∈H²` (`thm:h2`).

## The astonishment (why it's placed after the three-modes table)
`sec:threemodes` sets State and Directed in different rows with different obstructions
and warns against a master theorem. This section pulls the rug **honestly**: compose
two *stateful* update agents and the composite is a *Zappa–Szép product* — a *directed*
object. The two rows meet on one object. Then:

1. **`thm:classifier-composes`** — composite liftings ≅ `Fun(𝔸(↓)⋈𝔸(↓'),Cat)`; the
   Ch7 classifier is monoidal under orchestration.
2. **The reversal** (`ex:s3-emergent`) — the naive guess `Stab_{P⋈P'}(s) ≅
   Stab_P(s)⋈Stab_{P'}(s)` is FALSE. Worked S₃ witness: P=A₃, P'=⟨(12)⟩, s=1; both
   factor stabilisers trivial, composite stabiliser ⟨(23)⟩≅ℤ/2, via the loop
   1→(12)→2→(132)→1 whose two legs each move 1. **Orchestration synthesises holonomy.**
3. **`thm:meeting-points`** — the measure: h(s)=|A\U/B|=|Stab_G|/(|Stab_P||Stab_{P'}|)=
   |(s·P)∩(s·P')| (number of crossings of the two reachable-state orbits); h=1 ⟺ aligned.
4. **`thm:emergent-h2`** — aligned-abelian: [ω]∈H²(B;A), =0 ⟺ E≅A×B ⟺ unentangled;
   ℤ/2 table (ℤ/2×ℤ/2 vs ℤ/4).

## Honesty guards I kept (please sanity-check)
- **Two [ω] sites NOT identified.** A dedicated teachbox says the stabiliser class
  H²(B;A) and the handoff class H²(Sk_C;D) of `thm:h2` *rhyme* (same ℤ/2 generator, same
  ZS data) but are **different sites** — explicitly not claimed to be one class.
- **Consistent with the `prop:monoidanchor` correction.** This is a ZS product of two
  monoids P,P' (legitimate), not the corrected mis-reading of a single update monad.
- **`thm:emergent-h2` scoped** to aligned + abelian + normal A; nonabelian deliberately
  not claimed. `thm:meeting-points` is the fully general result (any exact factorisation,
  any action, any point).
- No new citations: uses `AhmanUustalu13`, `RW`, `BW85` (all already in the bib).

## The earned grant sentence (close of the section)
"Unprotected orchestration can synthesise holonomy the parts lack, and a degree-2
cohomology class certifies when the composite is a clean product of the parts." + the
operational reading: an auditor **counts the crossings of the two agents' reachable-state
orbits** — no cohomology needed to *detect* emergence, only to classify the clean case.

## Provenance / TODOs (not this session — flagged)
- Lean: the S₃ witness is machine-checked (`EmergentHolonomy.lean`, axiom-free) but not
  committed to the book's `lean/` tree — I tagged it as such, matching the book's
  convention for uncommitted Lean.
- `citation_check.py` was not present in this container (`memory/code/` is empty), so I
  verified the footprint by hand: the section adds no new bibitem and all three keys
  pre-exist. If you want the automated footprint report, the script needs restoring.
- Open question worth a future prove/dream: is the stabiliser [ω] a *restriction* of the
  handoff [ω] along B·Stab → Sk_C? Stated as open in the teachbox.

Sources: `proofs/2026-08-12-holonomy-composition-zs-bridge.md`,
`proofs/2026-08-13-emergent-holonomy-meeting-points.md`. Scratch:
`scratch/write-2026-08-13-book.md`.
