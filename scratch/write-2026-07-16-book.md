# Write session 2026-07-16 — book chapter "Which functors are containers?"

## Target
New standalone chapter for `category-of-containers` book (Neil uid 63). Written as a
self-contained compilable article (like Chapter 0), macros matched. Output:
`~/projects/papers/which-functors-are-containers.tex`.

## The ONE promise
By the end you can look at any functor F: Set→Set and say whether it is a container,
read its positions off — and you'll see why the obvious way to read them off is wrong.

## Hook / surprise (the engine)
- Concrete test: is 1+X a container? yes. Powerset P? **NO** — and the reason is a
  one-line counting argument (S=F(1) has 2 elts; F(0)=1 forces one shape with 0
  positions; F(2)=4 forces 2^p=3 on the other shape — impossible). Delightful,
  elementary, teaches the method that leads to the recovery formula.
- The correction box: naive "P(s) = fibre of F(2)→F(1)" gives 2^{P(s)} (POWERSET),
  not P(s). Recovery genuinely needs the generic element / connected-limit UP.
  (This is Neil's own guessed formula — honest flag for him.)

## Structure
0. Hook + promise + landscape (the question; where it sits in book arc).
1. A container is a family of sets: Cont ≅ Fam(Set^op). Free coproduct completion of
   Set^op; ⟦S,P⟧ = ∐_s y^{P(s)} (back-ref Ch0 Lan). Terminology warning box here.
2. Which functors are containers? Compute 1+X ✓, list ✓, powerset ✗ (counting arg).
   Theorem: F container ⟺ preserves connected limits (wide pullbacks + cofiltered).
   Intuition: coproducts commute with connected limits in Set. Finiteness fork footnote.
3. Recovering positions — and the formula everyone gets wrong. S=F(1); generic element
   gives P(s); ★ correction box (fibre of F(2) = powerset). ∂F(1)=Σ_s P(s) caveat.
4. Limits & colimits in Cont. Fam(Set^op) complete+cocomplete. Products/coproducts
   explicit + Lean-verified (Cont.lean): coprod = S+T; prod shapes S×T positions P s + Q t.
   ⟦–⟧ preserves connected limits + coproducts, NOT all colimits. Coequaliser: quotients
   create symmetries → analytic not polynomial → escape Cont. Ties powerset/unordered-pairs
   non-examples to "the boundary of the theory."
5. Connections: the polynomial boundary; forward-ref comonoid + monoidal chapters.

## Provenance discipline (citation floor = deep-read)
- Characterization + recovery: [Cited: Gambino–Kock 2009 (arXiv:0906.4931), §1.18 & Prop 1.22;
  historical: Diers 1977, Carboni–Johnstone 1995 — as reported by GK]. GK is deep-read ✓.
- Cont ≅ Fam(Set^op): [Folklore] / free coproduct completion; back-ref Ch0. Do NOT cite
  von Glehn (not deep-read). Present self-containedly.
- Representation thm: [Cited: AAG05] back-ref to book's Ch "Containers".
- Products/coproducts: [MacBeth, Lean-verified: Cont.lean].
- Powerset non-example: elementary exposition, NOT claimed new (standard: powerset not
  polynomial).

## TODOs / gaps (write-session honest flags — NOT to fix now)
- Abbott-thesis coequaliser reference: NOT pinned (can't browse). State the negative
  fact conservatively via the polynomial-boundary argument; footnote flags the exact
  reference is to be pinned in a prove/browse session. Do NOT assert "Abbott thesis Thm X".
- "F preserves connected limits" — cite GK; do NOT reprove.

## Style reminders (book skill)
- One idea per sentence. Compute before generalise. Diagrams carry argument. Signal
  surprise. Provenance tags on every result. Voice: honest excitement only.

---
## FINAL STATE (end of session)
DONE. `papers/which-functors-are-containers.tex` — 7pp, compiles clean (2-pass, no
undefined refs, no overfull >20pt). ~3050 words. All 5 draft-book passes run:
- P2 (arc): fixed muddled product paragraph (removed false "as it must, connected-limit"
  inference; now tees up the warnbox cleanly).
- P3 (examples): recomputed all counting (powerset 1/2/4, |F(n)|=Σn^|P(s)|, fibre=2^P(s))
  — all correct. Grounded "connected limit" with the •→•←• pullback shape. No diagrams
  added: arguments are arithmetic/Yoneda, prose carries them, container pictures belong
  to the earlier chapter (avoided decoration).
- P4 (reader/Neil): fixed precision bug — powerset quotients by rearrangement AND
  repetition (idempotent), NOT analytic; corrected.
- P5 (cut): trimmed scaffolding lead-ins ("Let us gather...", "The key fact is this",
  derivative-remark hedge).
Citation floor = deep-read (GK 0906.4931), passes citation_check --report footprint.
Delivered: for-robin note + PROGRESSIVE_DISCLOSURE updated. No git push (out of scope).
TODO carried in-text: pin Abbott-thesis coequaliser ref (browse/prove session).
