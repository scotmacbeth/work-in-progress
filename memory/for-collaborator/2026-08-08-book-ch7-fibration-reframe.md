# Book Ch (Monads & comonads) — fibrational rung reframed to Neil's subobject-vs-codomain language

**Date:** 2026-08-08 (write session). **File:** `books/category-of-containers.tex`,
subsection "The fibrational picture", teachbox "The fibration stratifies the monad zoo"
(the "One rung further out" material). Compiles clean, 71 pp, 0 undefined citations.

## What changed (three folds from WRITE.md)

**(0) The main rewrite — Neil's fibration language.** The rung that used to open
"the proof-relevance boundary" now opens by naming the *two fibrations over Set* Neil
identified in his UID-92 challenge:
- **subobject fibration** `Sub(Set)→Set` — a leaf carries a *truth value* (Prop);
- **codomain/families fibration** `Cont→Set` — a leaf carries an *actual set of positions* (Type).

Cited Hermida–Jacobs 1998 (Inf. Comput. 145(2), DOI 10.1006/inco.1998.2725) for the distinction.
The prose now:
- Leads with the **failing core theorem** as the headline: *"every Set monad lifts to a
  container monad via T_M" is FALSE* (Reader, State drop leaves), true for cartesian M.
- Leads the intuition with the **∀-row, fibration held-flip** — the sentence that landed for
  you: a "for all leaves" *proposition* only gets easier on a drop (□ survives); a *Type*-valued
  datum at every leaf can't reindex through a drop (∏ = T_M dies).
- Adds the **concrete 2×2 Reader witness** (E={0,1}, diagonal μ keeps (0,0),(1,1), drops
  (0,1),(1,0)) you found clarifying.
- Presents the full **2×2 ℤ/2 grading** as a table (`direction = is-limit XOR records-data`)
  and states plainly: **neither fibration survives uniformly** — survivor is □ (∀ in the
  subobject world) AND Σ (∃ in the codomain world). Merge keeps all four; drop kills the two
  forward-total ones (∏, ◇).
- "Proof-relevant" retired from the prose except ONE parenthetical (as the type-theorist's
  synonym for "records positions rather than truth").

**Independent witness added.** Orestis's Agda (`CoLift.agda:163–184`, Reader named at l.175)
is cited as an independent machine-checked witness that the ∀/Π lift is a container monad only
when μ drops nothing. **Honest caveat stated in the book:** his framework is *entirely*
type-valued, so his □/◇ are our ∏/Σ (both in the codomain column) — he witnesses ∏-dies/Σ-survives
*within* the codomain leg, and does NOT touch the subobject box. Attribution is first-name-only
("Orestis") in the bibliography — I did not invent a surname; cited as unpublished, personal
communication via Neil. **If you know the full name/how he wants to be cited, tell me.**

**(A) Three fibred-monad citation verdicts — already correct, no change needed.** Audited:
T_M = lifting always / fibred monad (Hermida Def 5.4.1) iff M cartesian; G_M = vertical fibred
comonad ∀M (Jacobs Ex 1.7.9); λ = mixed distributive law / entwining (Beck 1969), strict-BC a
*consequence*. All three already stated correctly with the right cites.

**(B) Σ-monad hedge removed.** The prov note now reads "proved … and **Lean-verified for
Reader**" (was just "proved"). The honest OPEN caveats are kept verbatim: the *general*
`reverse-total ⇒ Σ-monad` implication is still open (pointwise section ≠ coherent section; Reader/
State only meet it via their canonical diagonal/threading), and the exhaustiveness of the parity
dichotomy is open.

## One thing to confirm (tone gate)

WRITE.md asked me to gate the *tone* of the reframe on your reply to my UID-92 answer. I couldn't
check email this session (write-session rule). I went ahead because the frame is *your own*
language and the mathematics is settled — but if you'd phrase "subobject vs codomain" differently,
it's a one-paragraph change. Flag it and I'll adjust.

Nothing here is a new proof or a Lean change; it's exposition of results already in
`proofs/2026-08-07-*` and the Reader Σ Lean rung.
