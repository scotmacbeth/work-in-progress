# For Robin — new book chapter: "Which Functors Are Containers?"
*Write session, 2026-07-16. (This session forbids email — please forward the gist to Neil, or I'll send on the next wake.)*

## What
A new standalone chapter for *The Category of Containers* (Neil's uid-63 ask):
the chapter that opens with **Cont ≅ Fam(Set^op)** and delivers the core content
Neil wanted — **which functors are containers**, and how to **recover the positions**.

**File:** `projects/papers/which-functors-are-containers.tex` (+ `.pdf`, 7pp, compiles clean).
Written as a self-contained compilable article, macros matched to Chapter 0, so it
slots into the book or reads alone.

## The chapter's one promise
By the end you can look at any functor `F: Set→Set`, decide whether it's a container,
read its shapes and positions off — and see why the first formula you'd guess for the
positions is wrong.

## The two surprises (the engine)
1. **Covariant powerset is not a container — one-line counting.** `|𝒫(1)|=2` gives
   2 shapes; `|𝒫(0)|=1` forces one shape with 0 positions; `|𝒫(2)|=4` forces `2^p=3`
   on the other shape. Impossible. Elementary, and it teaches the recovery method.
2. **★ The correction for Neil.** Neil guessed `P(s)` = fibre of `F(2)→F(1)` over `s`.
   That fibre is `{φ: P(s)→2} = 2^{P(s)}` — the **powerset** of the positions, not the
   positions. Recovery genuinely needs the generic element (connected-limit universal
   property), not any single evaluation-and-fibre. Boxed honestly as a correction.

## Sections
1. A container is a family of sets: `Cont ≅ Fam(Set^op)`, free coproduct completion of
   `Set^op`; `⟦S,P⟧ = ∐_s y^{P(s)}` (back-ref Ch0 Kan). Terminology box (Spivak's
   "positions/directions" = our "shapes/positions", opposite naming).
2. The test: compute friendly functors, powerset fails, then the characterisation —
   **F is a container ⟺ F preserves connected limits** [Gambino–Kock; orig. Diers /
   Carboni–Johnstone]. Box on why "connected" is the right word (see 07-17 revision).
3. Reading positions back off: `S=F(1)`; correction box; generic-element recovery
   [G–K Prop 1.22]; derivative-at-1 caveat.
4. Limits & colimits: `Cont` complete+cocomplete; products/coproducts explicit
   (**Lean-verified, Cont.lean** — product positions are a *coproduct* `P s + Q t`);
   `⟦–⟧` preserves connected limits + products + coproducts but is **not cocontinuous**.
5. The boundary of the theory: powerset (value side) and coequalisers (colimit side)
   are one failure — you leave Cont the moment you *quotient*. Hands off to the
   comonoid chapter (DCont ≅ Cat).

## Provenance & honesty
- Everything substantive is **classical** (Diers/CJ/Gambino–Kock). Value = arrangement,
  the concrete non-examples, and the correction. No novelty claimed. Reproof pattern
  did **not** fire — I checked my own notes + the GK PDF first.
- Citation floor = **deep-read** (Gambino–Kock 0906.4931). Passed `citation_check.py
  --report footprint`. Diers/Carboni–Johnstone are historical attribution reported
  *through* GK, stated as such — not claimed independently read.
- Fixed a Neil-lens precision bug in §4: powerset is a quotient by rearrangement **and
  repetition** (idempotent), coarser than a group action — so it's *not* analytic; I no
  longer imply it is.

## Two open TODOs left in the text (NOT fixed — not a write-session job)
1. **Abbott-thesis coequaliser reference not pinned.** The "⟦–⟧ does not preserve
   coequalisers" claim is boxed as honest folklore with the exact reference flagged
   unverified — needs a browse session to pin (and ideally a concrete two-container
   coequaliser exhibiting the failure). Do NOT attribute a theorem number yet.
2. The generic-element recovery + connected-limit characterisation could get a `/lean`
   target someday, but it's deep (parametric right adjoints) — parked.

## Delivery
Chapter is in `projects/papers/` (host-readable). No git push: seed is read-only,
projects isn't a repo, and the shared-repo route has a fraught history — book
integration (where it slots in `category-of-containers.tex`) is Neil's call.

---

## REVISION ADDENDUM — 2026-07-17 (write session, referee pass)
Ran the /write revision loop on the finished chapter. Intro↔conclusion consistent;
counting arguments re-verified; no padding to cut. **Found and fixed one genuine
mathematical error** — worth flagging to Neil since it touches the characterisation.

### ★ Corrected error: the "connected, not finite" box
The old box claimed *the empty diagram is a cofiltered limit whose limit is the terminal
object, and containers must preserve it*. **This is false and self-contradictory.** A
container has `⟦S,P⟧(1) = S`, which is `≅ 1` only when `|S|=1`; so a container does
**not** preserve the empty limit (the terminal object) in general. The empty diagram is
**disconnected**, so it is correctly *outside* condition (ii) — you cannot use it as a
limit containers preserve.

**The fix turns the mistake into pedagogy.** The box now explains "connected" as the
line between two errors:
- **not merely wide pullbacks** — cofiltered limits are connected too and must be
  demanded separately (cited to Gambino–Kock §1.18; I did *not* attribute this to the
  CJ 2004 corrigenda — my source note says that corrigenda concerned the Artin-glueing
  side and is unrelated to this equivalence);
- **not all limits** — the very fact `F(1)=S` is *why* the condition is "connected" and
  not "all": preserving the empty limit would collapse `S` to a point.

### Other change
Tightened the "`y^A=(-)^A` preserves all limits" aside: it's the right adjoint to `-×A`,
stated plainly instead of "a right adjoint's cousin".

### State
7pp, still compiles clean (2-pass, no undefined refs, no overfull >30pt). Citation floor
unchanged at **deep-read** (GK 0906.4931), re-passed `citation_check.py --report
footprint`. No new citations. The two open TODOs above (Abbott coequaliser ref; possible
Lean target) are unchanged — still not write-session work.
