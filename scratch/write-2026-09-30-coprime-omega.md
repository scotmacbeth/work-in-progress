# Write scratch — coprime forces [Ω]=0 orthogonally to ν (positioning note)

Date: 2026-09-30. Target: standalone expository/positioning note, work-in-progress.
Source: proofs/2026-09-30-crespo-coprime-omega-witness.md (grade: computed).

## PHASE 1 — the one sentence

> For finite skew braces, coprimality of the ideal and its quotient forces the bilinear
> extension class [Ω] to vanish — recovering the classical decomposition theorems as the
> [Ω]=0 locus — but it does so for a purely order-arithmetic (Schur–Zassenhaus) reason
> that is orthogonal to the residue channel ν, which survives non-trivially in a majority
> of the decomposable cases.

Two-part sentence because the note has two-part content: (a) framing, (b) the correction.

## CITATION REALITY (hard constraint — checked sources.json 2026-09-30)

Deep-read (CITABLE as bibitems):
- Rathee–Yadav 2601.12371 [RY] — extension H²_Sb, complements, coprime Schur–Zassenhaus-type
  complement theorem (for trivial-brace/socle kernels). THE anchor for "coprime ⟹ complement".
- Gran–Letourmy–Vendramin 2409.18056 [GLV] — homology leg (only a passing mention, if at all).

Agent-summary (CANNOT bibitem — below floor):
- Crespo 2609.24655, Damele 2603.22980 & 2606.29295, Ferrara–Trombetti 2606.30453.
  → The general finite-skew-brace Schur–Zassenhaus (coprime ⟹ complement for ANY ideal) is
    THEIRS. I may NAME them in prose as recent independent structure-theoretic work but must
    NOT give formal bibitems, and must flag "citation pending deep-read". Anchor the cited
    version on RY (deep-read).

My own:
- [Ω]=0 ⟺ SES splits ⟺ D has sub-skew-brace complement — PEER-REVIEWED within group
  (Rick), state as such, no external bibitem (as the two-legs paper did).
- Computed witness table — grade COMPUTED, my own scripts. State finite, not a proof.

## SCOPE-CHECK RESOLUTION (WRITE.md demanded it)
"coprime ⟹ skew brace splits" IS ALREADY A THEOREM (RY coprime complements; general case
Ferrara–Trombetti / Damele 2026). So I do NOT claim it. NOVEL content = (a) the [Ω]-cohomological
FRAMING + (b) the ν-orthogonality observation + (c) the axiom-verified computed confirmation.
Say this explicitly in the intro (gap paragraph) and conclusion.

## PHASE 2 — skeleton

1. Introduction — decomposition of skew braces; the [Ω] obstruction; two ways coprimality
   could kill it (order-arithmetic vs residue-trivialisation); the note's claim: it's the
   former, ν survives. State main "observation" (not theorem) by page 2.
2. Preliminaries — skew brace, ideal, extension SES, split/complement; the class [Ω] and the
   peer-reviewed [Ω]=0⟺split; the residue ν (outer H-action on D, im λ|_D mod inner); coprime.
   Only what's used.
3. The [Ω]=0 locus recovers classical decomposition — restate premise; note the coprime
   Schur–Zassenhaus (cite RY; name FT/Damele as recent, citation-pending). This is the
   "recovers" half.
4. The computed witness — method (GV enumerator, orders ≤24, 16 groups, axiom-verified,
   direct complement search not cohomological proxy); Table 1 (coprime 0/111, non-coprime
   582/1236); the boundary reading (non-coprimality NECESSARY for [Ω]≠0 in the sweep).
5. The residue survives — the crux/correction. Dream hypothesis stated & refuted. 70/111
   non-trivial outer residue, 74/111 non-trivial H-action. Witnesses S₃ (A₃⋊Z₂ invert),
   A₄ (V₄⋊Z₃ 3-cycle). Orthogonality reading.
6. Conclusion — [Ω] recovers AND refines classical decomposition (isolates ν the classical
   toolkit doesn't see); grant framing (H²-cluster explains a classical result + sees one
   more thing); honest scope (finite sweep; general orthogonality = open); open questions.
Refs: RY, GLV.

## NOTATION
- 0→D→G→H→0 skew-brace SES; D ideal, H=G/D quotient. (matches witness file & two-legs.)
- [Ω] bilinear class; ν residue; λ the (multiplicative) action map.
- gcd(|D|,|H|)=1 coprime.
- Reuse two-legs macros: \Sb, \Z, \Aut, \im, \id, \Grp.

## HONESTY FLAGS to embed
- "computed witness, finite sweep, NOT a proof" — say in §4 and conclusion.
- residue-trivial := im λ|_D in Aut(D) mod Inn(D) AND mod D-action — define exactly.
- general "coprime⟹split for skew braces" = cite RY (trivial-kernel), name FT/Damele recent.
- ν-orthogonality proven only as computed observation; general theorem OPEN → prove session.

## TODOs discovered (NOT for this session)
- deep-read Crespo/Damele/Ferrara-Trombetti to lift them above floor → then can bibitem the
  general coprime-complement theorem directly. (browse session)
- general proof "coprime ⟹ [Ω]=0 ⊥ ν" → prove session.
