# Grant-narrative note: the four-level monad-lift stratification

**Date:** 2026-08-05 (write session)
**File:** `projects/for-collaborator/2026-08-05-monad-lift-stratification.md` (~2pp markdown)
**For:** the Kodamai grant Theory pillar + a drop-in paragraph Neil/you can paste into the
"taxonomy of composable effects" section.

## What it is
A short, self-contained grant note framing this week's PROVE result as a *theory contribution*.
It presents the stratification of Set-monads by how much structure survives the lift to the
container fibration `p:Cont→Set`:

```
pure writer A×(−)  ⊊  writer+exception E+A×(−)  ⊊  cartesian  ⊊  polynomial
   Id, Writer            +Maybe, Exc                 +List         +Pf
strict Beck–Chevalley   arrows form a category    no leaf merging  has a support
```

Each rung has a *computable* fibred detector and a *named* everyday monad witnessing that the rung
is strict. The write is aimed at a reader who knows monads but not containers-as-a-fibration — six
lines of setup, then the ladder.

## The honest hook (and why it reads well)
It began as a *refuted* conjecture. We had a tidy slogan — "containers preserve cartesian morphisms
= non-branching = strict Beck–Chevalley" (a proposed TFAE). It is **false**: those are three
different rungs. The failure IS the content, carried by two monads everyone knows: `List` (cartesian
but branching) separates cartesian from non-branching; `Maybe` (exceptions break the empty product)
separates strict-BC from non-branching. The note leans into the "interesting failure" arc because
it's true and it sells: a collapse would have been a slogan; the ladder is a taxonomy.

## Discipline observed
- No book edits (the book aside awaits Neil's answer — flagged at the foot of the note).
- No new mathematics; everything cites the proved artefacts.
- Citation footprint clean: `citation_check --report footprint` floor = **deep-read** (only external
  cite is Ahman–Bauer 2409.17664, the source of `T_M`).
- Open gaps flagged honestly in a dedicated section (arity-≥2 cross-terms argument sketched not
  line-by-line; E2′ not yet Lean'd in general; `List` cartesianness checked on bounded data).

## Provenance chain (all your host copy can read)
`proofs/2026-08-05-cartesian-preservation-nonbranching.md` (refutation + boundary table),
`proofs/2026-08-05-crown-gap-closure.md` (two rungs upgraded to proved),
`proofs/2026-07-29-effect-coeffect-arrows.md` + `proofs/2026-07-30-affine-classification.md`
(the middle biconditional + `E+A×(−)` classification),
`lean/Containers/Containers/FibredTransfer.lean` (`G_M` cartesian ∀M, machine-checked).

No email this session; no GitHub push (no projects remote I can verify — you read the volume from
the host). Happy to send the note by email once email is back in the loop.
