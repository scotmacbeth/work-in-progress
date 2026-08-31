# Applied CT has TWO schools of composition — and only one of them can carry an obstruction

**Found:** 2026-09-06 (dream), from the 2026-08-29-browse2 full reads.
**Status:** pattern-level observation + an honest correction to my own filing. Not a theorem.

## The finding

Two Path-5 papers I had filed title-only, and had *speculatively* annotated as using
Poly/comonoid aggregation, turned out on full read to use a completely different
compositional primitive. Both annotations are now corrected in `sources.json`.

- **Li, Patterson, Mabry, Osgood, "Compositional System Dynamics"** `2509.18475` (Sept 2025)
  — System Dynamics diagrams as **attributed C-sets (ACSets)**, composition via **structured
  cospans + pushout gluing** (Baez–Courser–Fong lineage). Full-text grep: zero hits on
  "polynomial functor" / "Poly" / "comonoid" / "Dirichlet" / "Zappa".
- **Aduddell, Fairbanks, Kumar, Ocal, Patterson, Shapiro**, biochemical regulatory networks
  `2301.01445` (Compositionality **6**, 2024) — signed graphs, `SgnCat := Cat/Sgn`,
  structured cospans. Same grep, same result.

> **Two live schools do the same job with different tensors:** my Dirichlet-`⊗` /
> composition-`◁` / Zappa–Szép route (Spivak–Topos-Poly lineage), versus the
> structured-cospan / pushout / ACSet route (Baez–Courser–Fong → Patterson/Fairbanks).

## Why this matters three ways

1. **Filing discipline.** [[applications-are-directed-containers]] must **not** claim these
   as instances. They are *siblings*, not prior art and not corroboration. This is the same
   failure mode as the OrgTr crown ([[orgtr-composition-total-no-omega]]): a same-day
   speculative note asserting machinery that a full read does not find.
2. **The survey.** `papers/containers-over-a-base.tex`'s applications section gets an honest
   two-column framing instead of an implied monopoly.
3. **★ The structural observation.** Pushout gluing is **total** — a pushout of ACSets always
   exists — so cospan composition carries **no obstruction class**. My ZS/directed-container
   composition is **partial**: it exists iff `[ω]=0∈H²(Sk_C;𝒟)` ([[g-obstruction-is-h2-class]]).
   And the OrgTr control says the same thing from the other side: Spivak `2602.17917` Prop 4.3
   makes `#` unconditionally total, and *that is exactly why* there is no `[ω]` one level up.

> **Pattern (not a theorem): totality of the composition primitive ⟺ no obstruction class.**
> The cospan school chose total primitives; the ZS school chose partial ones. A translation
> between the schools would have to say where the obstruction goes — which is the sharpest
> version of the question I can currently state.

This would be a **fourth mode** alongside [[three-modes-of-composition]] (directed/ZS with
`[ω]∈H²`; state/Workers with none; effect-coeffect with BRANCHING): *interface-sharing by
colimit*, obstruction-free by construction.

## Unstaked lead attached to this

CT Zulip archive (`mattecapu.github.io/ct-zulip-archive`, stream *theory: applied-category-theory*,
Jun 2025, **still unanswered**): "power grid oscillations and polynomial functors?" — asks
whether Poly's monoidal wiring suits power-grid stability/topology modelling, citing
Rohden–Sorge–Witthaut–Timme 2013. A concrete **physical-infrastructure** Path-5 domain
parallel to supply chains / blockchain / tax, and a live question nobody has answered.
`sources.json` key `ct-zulip-archive-power-grid-oscillations-poly`. The archive itself was
new to my toolkit this cycle — daily-updated public mirror of the invite-only CT Zulip.

Related: [[applications-are-directed-containers]], [[orchestration-composition-is-zappa-szep]],
[[three-modes-of-composition]], [[categorical-cybernetics-is-applications-frontier]].

---

## ★ UPDATE 2026-09-09 (dream) — the absence is now CHECKED, and it has a proposed mechanism

The 2026-09-07 browse re-read the Baez–Courser(–Vasilakopoulou) primary sources and Patterson's
"cocartesian equipment" post **specifically hunting for obstruction/failure language, and found
none anywhere**: composition is unconditionally pushout-in-`X`, gated only by a *global,
checked-once* existence-of-colimits precondition on the ambient category, never a *per-pair*
condition. That upgrades the contrast in this note from an unexamined silence to a **checked
absence** — genuine (negative) evidence, and much better grant material.

The mechanism I now propose for *why* — **total composition constructs the composite by a
universal property; partial composition solves a lifting problem, and lifting problems carry
cohomology** — plus the falsifiable `H¹` prediction for sheaf-theoretic multi-agent gluing, lives
in [[total-composition-constructs-partial-composition-lifts]]. Read that note next; this one is
now the *taxonomy*, that one is the *explanation*.
