# Chapter 0 "The Machinery" — verified & book-ready (2026-07-16 write session)

**Deliverable Neil asked for (email UID 61):** the preliminary chapter on representables, Yoneda,
Day convolution, Kan extensions — the foundation the four-monoidal chapter leans on.

**File:** `~/projects/expository/preliminaries-representables-yoneda-day-kan.tex` (12 pp, compiles
clean, PDF built). Title now "Chapter 0 — The Machinery".

## ✅ SENT 2026-07-17 (wake session) — to neil@kodamai.com, CC langer.robin@gmail.com, PDF attached, folded into the morning daily update. No further action needed.

## STAGED EMAIL (I could NOT send — write-session rule forbids email. Please send from a wake session, or Robin can forward.)

> **To:** neil@kodamai.com **CC:** langer.robin@gmail.com
> **Subject:** Chapter 0 "The Machinery" — verified draft (representables/Yoneda/Day/Kan)
>
> Neil — the preliminary chapter you asked for is drafted, verified, and book-ready (12pp, PDF
> attached). It proves your two observations as the black boxes the monoidal chapter cites:
> **(i)** the container-extension functor IS the left Kan extension of the representable embedding
> along the singleton inclusion (free coproduct completion) — so Day on Cont needs no coend; and
> **(ii)** closed structure on a Day category is *forced on representables and extended by density*.
>
> One honest correction I have to flag on (ii). The first draft over-reached: it claimed any
> cocontinuous strong-monoidal functor *preserves* the internal hom (and that the Dirichlet hom of two
> representables is y^{b^a}). Both are false. Density *determines* the internal hom but does not hand it
> to an arbitrary L for free — the free-vector-space functor k[−] is a one-line counterexample
> (strong monoidal, cocontinuous, NOT strong closed). And the correct hom of two representables is a
> *coproduct* of representables — `[y^a,y^b] = (Cont(y^a,y^b) shapes, b positions each)`, i.e. your
> "shapes are morphisms" internal hom (Niu–Spivak Ex 4.78) — not y^{b^a}. Your actual observation
> (density) is intact and true; only the draft agent's generalisation of it was wrong. The chapter now
> states the true density principle, computes the right formula, and carries the counterexample as a
> cautionary remark. Closure itself is certified where it belongs — directly, in the monoidal chapter.
>
> Question I still have open (from my 07-16 daily): standalone Chapter 0, or fold into the front matter?
> I've written it standalone with forward-refs to Theorem C.
>
> — MacBeth

## What changed vs the draft agent's version
- Verified both theorem proofs personally (Yoneda, density, Lan, Day all correct).
- Fixed variance (Day embedding domain is C^op) and Day base (Cont uses base (Set,⋆), not Set^op).
- Added a size footnote for Lan along the large category Set^op.
- **Removed a false theorem** and replaced with the honest density principle + correct representable
  internal hom + k[−] counterexample. Details in `~/projects/scratch/write-2026-07-16.md`.

## Still TODO (not this session)
- SECONDARY task in WRITE.md: DJN (2305.05655) "closest neighbour" paragraph + M3 attribution fix on
  `four-monoidal-chapter.tex`. (Doing now if context allows; else next write session.)
