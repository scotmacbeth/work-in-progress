# Connection: Front D is a *family of weakenings* of Σ-Π-Δ, and Vec fails them all for ONE reason

**Opened:** 2026-09-02 (dream), consolidating browse `reading/2026-08-27-browse2.md`.
**Front:** D (three-approaches-to-containers-over-a-base survey; Neil UID-125).
**Depth:** Walker AND Weber now **deep-read** (Weber `1106.1983` direct-read 2026-08-28); Street /
comprehension rungs still `agent-summary`/citation-context. A convergence *observation*, not a proof.
**Updated 2026-09-03 (dream):** Weber-rung verdict + the δ↔Φ spinoff added below.

## The shape

I had been framing Front D as **three disjoint approaches** to "a container in a category":
(1) external `Fam(C^op)` (mine), (2) indexed dependent-polynomial Σ-Π-Δ over an LCCC
(Gambino–Hyland/Kock), (3) fibrational/comprehension. The 08-27 browse — pulling Walker's own
30-item bibliography in full for the first time — shows approaches (2) and (3) are not disjoint at
all. They are **points on one axis: successive weakenings of the Σ-Π-Δ dependent-polynomial
semantics, ordered by how much base structure they demand.**

| Weakening | Base hypothesis | Source | Depth |
|-----------|-----------------|--------|-------|
| Full dependent polynomial | **LCCC** (`Σ_f ⊣ Δ_f ⊣ Π_f`) | Gambino–Kock `0906.4931` | tracked |
| Pullbacks + **exponentiable middle leg** | pullbacks *and* distributivity pullbacks (comparison **δ iso**); NOT mere pullbacks | Weber `1106.1983` "Polynomials in categories with pullbacks" | **deep-read** 2026-08-28 |
| Subcartesian | **subpullbacks** (`∇_f ⊣ ⊠_f`, affine base-change; tensor `A+B−X`) | Walker `2607.10242` LSCC | **deep-read** (`reference_walker_lscc_vec_verdict.md`) |
| Spans | polynomials-as-spans in a bicategory | Street `1903.03890`; Walker `1806.10477` | citation-context |
| Comprehension | Grothendieck fibration + comprehension functor (non-full/non-split allowed) | Najmaei–van der Weide–Ahrens–North `2503.10868`; Street–Verity comprehensive factorization (TAC 2010, no arXiv) | `agent-summary` |

All five sit in **one intellectual neighbourhood** (Street protocalibrations / Weber distributivity
pullbacks / comprehension schemes) — largely **independent of Gambino–Kock** yet converging on the
same object. Four independent browse agents (arXiv keyword, web, citation-trail) landed on the same
cluster from three routes.

## The one reason Vec fails all of them

Every weakening asks for *some* form of the dependent product / base-change right adjoint, and Vec's
obstruction — `∐ ⊊ ⊕` (non-extensive) **and no internal `Π`** — hits each at the same seam:

- **LCCC (GK):** no internal `Π` ⟹ can't even form the semantics. [[extensivity-is-the-container-boundary]]
- **Subcartesian (Walker):** DEEP-READ VERDICT — Vec fails even the affine weakening. `⊠_p` must be a
  *genuine* right adjoint (Def 4.0.1/Prop 4.1.2), not unique-if-exists; the nearest cousin (affine
  spaces, Rem 4.0.2/fn 15) is filed as obstructed by **cross-fiber combinations** = Vec's `∐⊊⊕` in
  disguise. → `reference_walker_lscc_vec_verdict.md`, [[../questions/vec-subcartesian-closure]].
- **Pullbacks+exponentiable (Weber): RESOLVED 2026-09-03 (deep-read) — branch (b), Vec fails.** The
  "categories with pullbacks" name is misleading shorthand: Weber requires every polynomial's **middle
  leg to be exponentiable**, run through **distributivity pullbacks** (comparison **δ must become iso**).
  Exponentiability is exactly Vec's missing `Π`, so the abelian-pullbacks observation was a red herring —
  Vec meets "has pullbacks" but not "exponentiable middle leg." Weber's rung sits *with* GK/Walker, not
  below. What it bought: Weber **localises** the failure (each specific middle leg fails the δ-iso, not a
  global "no `Π`") and is the master reference for the tower. → [[../questions/vec-subcartesian-closure]] Q3.

So the honest shape of Front D is NOT "three disjoint approaches, pick one" but:

> **A totally-ordered family of weakenings of Σ-Π-Δ semantics — and `Fam(Vec^op)` fails essentially
> all of them, always for the same underlying reason (`∐⊊⊕`, no internal `Π`). Only the external
> `Fam(C^op)` construction (approach 1), which uses *external* Set-`∐` and never asks the base for an
> internal `Π` or an extensive coproduct, reaches the linear base.** That is the honest reason Neil
> says `Fam(Vec^op)` "needs the first approach."

This *strengthens* the discriminator thesis (`scratch/2026-08-27-three-approaches-containers-in-category.md`):
the separating axis is not the binary "LCCC vs not" but the graded "how much base-change survives" —
and Vec sits below the bottom of the whole tower.

## Independent community confirmation

**MO 205902** ("What is the monoidal equivalent of a locally cartesian closed category?", 2015) got a
**fresh 2026-07-28 answer (score 5)** naming Walker's LSCC as *the* converged answer. This is
non-MacBeth-sourced evidence that "weakenings of LCCC" is exactly where the field's attention points
right now — Front D is on live territory, not a private preoccupation. Cite this thread alongside
Walker in any survey. (Cross-link into `reference_walker_lscc_vec_verdict.md`.)

## The delta (crown meta-pattern)

Each source smooths over a different seam: GK over *the base must be LCCC*; Weber over *which
pullbacks*; Walker over *which additive base* (quantales/nominal sets, never Vec); comprehension over
*full/split vs not*. **None assembles the family into a single ordered tower and asks where Vec sits.**
That assembly — "here is the weakening lattice, and the linear base the container/attention program
needs falls off the bottom" — is the Front D survey's genuine contribution, consistent with
[[contribution-is-the-delta-prior-work-fused-away]]. Honestly flagged: the *ordering* claim rests on
`agent-summary` reads of Weber/Street; the Walker rung is the only deep-read one so far.

## The δ↔Φ spinoff (NEW 2026-09-03 — the live increment)

Weber's δ-iso condition (distributivity-pullback comparison becomes iso) is the **same logical shape**
as my proved **T2** closedness obstruction Φ (`⊗` on `Fam(C^op)` closed ⟺ `Φ(Z)=∏_t∐_r C(M_r,Z⊗Q_t)`
familially representable). Both say "the tensor/composite has an internal hom / dependent product ⟺ a
canonical comparison is invertible." They even fail over Vec at the same seam (T2: dualizable-and-summable
only on `Fam_fin(Vec_fd^op)`; Weber: exponentiable middle leg). **Open conjecture δ≟Φ** — if the two
comparison maps literally coincide on `Fam(C^op)`, then **T2 closedness IS Weber-distributivity in
disguise**, folding a proved result into the weakening tower. Caveats (different monoidal structure `⊗`
vs `◁`; external vs internal `∐`) and the decision procedure are in the dedicated question
[[../questions/weber-delta-vs-t2-phi]]. This is now the highest-value Front-D thread.

## Next actions (for wake, in priority order)

1. **[[../questions/weber-delta-vs-t2-phi]]** — write both comparison maps explicitly for a 2-shape
   family; decide δ≟Φ (or corner-only via `Fam_fin(Vec_fd^op)`). Highest-value Front-D move.
2. Direct-read Street–Verity comprehensive factorization (TAC 2010) — anchor for the approach-(3)
   fibrational leg (ahead of / alongside Jacobs' comprehension-category textbook).
3. Fold this ordered-family framing into the Front-D `/expository` survey as its spine (replacing the
   "three disjoint approaches" outline). The Front-D survey paper `containers-over-a-base.tex` is now
   14pp with §5 = the proved logic of containers (`Cont(cod)` fibration).

## Links

[[../questions/vec-subcartesian-closure]] · [[../topics/containers-over-vec]] ·
[[extensivity-is-the-container-boundary]] · [[contribution-is-the-delta-prior-work-fused-away]] ·
`reference_walker_lscc_vec_verdict.md` (auto-memory) · SUMMARY Front D.
</content>
</invoke>
