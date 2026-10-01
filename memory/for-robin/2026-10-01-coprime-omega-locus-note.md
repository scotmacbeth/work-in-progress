# For Robin — new positioning note: coprime forces [Ω]=0 ⊥ ν

**2026-10-01 (WRITE session).** Delivered the WRITE.md-seeded expository/positioning note.

## File
`papers/coprime-omega-locus-residue.tex` → `.pdf`, **6 pages**, pdflatex clean (0 overfull,
0 undefined refs/cites).

Title: *Coprimality is the vanishing of $[\Omega]$, but not the vanishing of $\nu$: the
cohomological locus of skew-brace decomposition and its orthogonal residue.*

## What it says (one paragraph)
Using the peer-reviewed premise `[Ω]=0 ⟺ the skew-brace extension splits ⟺ D has a
sub-skew-brace complement`, the note frames the skew-brace Schur–Zassenhaus theorem
(coprime `(|D|,|H|)` ⟹ complement) as the statement that the coprime regime sits inside the
cohomological vanishing locus `{[Ω]=0}`. A finite, axiom-verified census (all skew braces on
additive groups of order ≤ 24) confirms this: coprime **0/111** split-failures, non-coprime
**582/1236**, so `[Ω]≠0` lives only in the non-coprime regime. The note then **corrects** the
09-30 dream hypothesis: coprimality does **not** kill `[Ω]` by trivialising the residue `ν`.
`ν` survives — non-trivial in 70/111 (outer) and 74/111 (H-action) of the coprime splittings,
with `S₃` and `A₄` as clean textbook witnesses. Coprimality forces `[Ω]=0` for an
order-arithmetic reason **orthogonal** to `ν`. Moral (grant-Theory): the invariant both
*recovers* the classical decomposition theorems and *refines* them by isolating a channel the
order-arithmetic toolkit can't see.

## Honesty / what is NOT claimed
- The census and the orthogonality are **computed** (finite sweep), explicitly flagged as
  not-a-proof. Two open problems are handed to a PROVE session: (1) that non-coprimality is
  *necessary* for `[Ω]≠0` in general; (2) that the coprime vanishing of `[Ω]` is genuinely
  `ν`-independent in general (expected: a Schur–Zassenhaus argument on `[Ω]` that never
  touches `λ|_D`).
- `[Ω]=0 ⟺ splits` is cited as peer-reviewed (no external bibitem), per house style.

## Citations — a deliberate restriction you should know about
Only **two** bibitems, both deep-read: Rathee–Yadav 2601.12371 and GLV 2409.18056. The
general finite-skew-brace Schur–Zassenhaus papers that WRITE.md pointed me at —
**Crespo 2609.24655, Damele 2603.22980 & 2606.29295, Ferrara–Trombetti 2606.30453 — are all
only `agent-summary` in sources.json**, below the deep-read citation floor. So I did **not**
give them formal bibitems; I named them in a single prose footnote as recent independent
work, and anchored the cited coprime-complement statement on the deep-read RY paper (whose
complement theorems cover the trivial-kernel case the witnesses exercise). Verified with
`code/citation_check.py --report footprint` → floor = deep-read.

**TODO for a browse session:** deep-read Crespo / Damele / Ferrara–Trombetti so the *general*
coprime-complement theorem can be cited directly instead of via the RY trivial-kernel anchor.

## Plumbing
wip-sync push is still blocked (the `ghp_` PAT was rejected on 09-30 and flagged to you).
The files are safe on the projects volume and readable from the host. Nothing lost.

— MacBeth
