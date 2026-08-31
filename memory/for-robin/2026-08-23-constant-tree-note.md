# For Robin — new note drafted: "Directed containers are the constant-tree fragment of OrgTr"

**Date:** 2026-08-23 (WRITE session)
**File:** `~/projects/papers/dcont-constant-tree-fragment.tex` (+ `.pdf`, 6pp, compiles clean)
**Status:** Draft complete. Not emailed (write-session rules forbid send — this is the note.)

## What it is
The short positioning note Neil's WRITE.md asked for, sharpened by the 08-27 load-bearing
close-read of Spivak, *Interactions that reshape the interfaces of the interacting parties*
(arXiv:2602.17917). Two clean verified facts + one honest negative:

1. **Embedding (Spivak's, positioned by me).** `Org ↪ OrgTr` is fully faithful onto the
   **constant / time-invariant trees** — Prop 4.6 (ff `[p,q]-Coalg → OrgTr(p,q)`, image =
   time-invariant, Rem 4.7) lifted to a locally ff bifunctor by Cor 4.8. So the
   directed-container / DCont≅Cof world = the **static-interface corner** of the adaptive theory.
2. **Composition is total (Spivak's, Prop 4.3).** `(S,α)#(T,β) = (S×T, α#β)`, bare cartesian
   state pairing, **no matching-pair / distributive-law / "provided that" gate** — closes by
   coinduction.
3. **The obstruction stays downstairs (mine).** Therefore the Zappa–Szép class
   `[ω] ∈ H²(Sk_C;𝒟)` does **not** lift into OrgTr. The subtle point (which I make the crux of
   the note): this is **not** because `[ω]` is trivialised upstairs, but because the operation
   it obstructs — **welding two comonoids/objects `⋈` along a shared resource** — is a different
   operation from OrgTr's `#`, which composes **1-cells** and is total. Two operations, two
   levels; the apparent tension ("downstairs can fail, upstairs never fails") is not a
   contradiction. Rem 3.17's Zwart–Marsden `u◁u`-monad no-go is a third, orthogonal thing.

## Honesty ledger (in the paper's §5.3)
- Spivak's: Prop 4.6, Cor 4.8, Prop 4.3, Rem 3.17.
- Ahman–Uustalu's: DCont≅Cat (1604.01187) and the base ZS product (2013 distributive-laws paper).
- Mine: the *naming* (DCont = constant-tree fragment) and the *positioning of `[ω]` as
  strictly downstairs*. No new machinery claimed — the value is the clean map + the negative.
- All 9 Spivak prop numbers re-verified against the PDF this session (the old notes' "6.10" and
  "9.3" were wrong; correct = 4.6/4.8 and 4.3).

## Provenance
Citation footprint floor = **deep-read** (OrgTr 2602.17917, AU 1604.01187, AU-DL, Niu–Spivak).
Shapiro–Spivak 2205.03906 (Org) and Zwart–Marsden ZM19 appear **only as Spivak's own
attributions**, framed as such in text and bibliography — not trusted from a browse paraphrase.
Libkind–Spivak 2404.16321 (agent-summary) deliberately **not** used as a load-bearing bibitem;
the cofree comonad is cited via Spivak's Prop 2.2 instead.

## Open TODO for a future PROVE session (flagged in §5.2, not attempted here)
Does an **adaptive orchestration topology** (a migration graph that rewires mid-run) arise as a
specific non-constant tree, and does its reshaping carry its own tree-level holonomy — an
adaptive analogue of the `(G)` closing datum? `[ω]` itself does not lift (proved-negative), but
this does **not** rule out a *distinct* tree-level invariant. That's SEED-Q6's deeper half.

## Where it fits the grant
"We are the verified core, OrgTr is the frontier." DCont≅Cof (proved + Lean) = fixed-interface
agents; OrgTr = agents that reshape interfaces mid-task (learn a tool). The re-entrancy `[ω]` is a
checkable property of the *static* composition; the adaptive composition is total — generality
buys freedom, not friction. Pairs with the ACT DCont≅Cof / ZS-for-categories submission.

Read the PDF directly from the projects volume if you want; happy to email Neil the summary in
the next wake session.
