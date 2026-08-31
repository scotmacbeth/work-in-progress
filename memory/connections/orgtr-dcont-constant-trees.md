# Connection: DCont is the constant-tree (stable-interface) full sub-bicategory of OrgTr

**Bridges:** Path 2 (directed containers) ↔ Path 3 (Spivak's Org/Poly) ↔ Path 6
(Lean) ↔ SEED-Q6 (coinductive polynomial trees ↔ adaptive GA topologies).

## The claim
Spivak's **OrgTr** ("Interactions that Reshape Interfaces", arXiv:2602.17917, 2026)
generalises the Org bicategory to systems whose *interfaces co-evolve through
interaction*. Objects are **polynomial trees** — elements of the terminal
(u◁u)-coalgebra — where each interaction step determines the child tree (= next
interface). A **directed container is a ◁-comonoid in (Poly, y, ◁)**, i.e. a *constant*
tree (interface never changes). So:

> **DCont embeds as a full sub-bicategory of OrgTr via constant trees.**

Made precise by **Prop 4.6 + Cor 4.8** (corrected 2026-08-26 from a mis-cited "Prop 6.10";
the paper ends at §4): **Prop 4.6** gives a fully faithful functor `[p,q]-Coalg → OrgTr(p,q)`
on hom-categories, whose image is the *time-invariant* objects (same coalgebra at every node,
Rem 4.7); **Cor 4.8** lifts this to a locally fully faithful bifunctor `Org → OrgTr` (the
constant-tree functor). Spivak states the embedding but does **not** name the DCont-as-fragment
reading — that framing is mine. The cofree-comonad right adjoint (Prop 2.2, via Libkind–Spivak
[LS24]) is the *same* adjunction `U: Cat# → Poly` underlying [[cofunctors-are-update-lenses]]
and DCont ≅ Cof.

## Why it matters
- **SEED-Q6 resolved in shape.** Q6 asked how coinductive polynomial trees relate to
  adaptive GA topologies (our Org formulation). Answer: **non-constant trees = interfaces
  that evolve mid-run.** A directed container is the *stable-interface* special case; an
  adaptive GA topology (migration graph that rewires as the run proceeds) is a genuine
  non-constant tree. The whole DCont theory is OrgTr restricted to the fixed point.
- **Grant agent-orchestration narrative, sharpened.**
  - DCont / Cof / lenses → agents with **fixed** capability-interfaces (request types
    P(s) stable). Meta-agent = cofunctor ([[cofunctors-are-update-lenses]]).
  - OrgTr → agents that **acquire new capabilities mid-task** (interface reshapes as the
    interaction unfolds). The general case the grant's "AI Mathematician" actually needs:
    an agent that learns a new tool is a non-constant tree.
- **Lean (Path 6).** The constant-tree embedding is a clean, bounded M5/M6 target: once
  the Poly comonoid layer is in Lean, "DCont ↪ OrgTr full and faithful" is Prop 6.10 —
  a finite, citable theorem rather than open-ended bicategory formalisation.

## The artifact to write (cheap, high value)
A **one-page note**: "Directed containers are the full sub-bicategory of OrgTr on
constant trees," citing Prop 6.10 + Prop 3.2, positioning our DCont ≅ Cof program as the
*stable-interface* fragment of Spivak's adaptive-interface theory. Fills a gap Spivak
left open; gives the grant a clean "we are the verified core, OrgTr is the frontier"
story. Pairs with the ACT 2027 DCont ≅ Cof / ZS-for-categories submission.

## The state-graded composition = Workers, one level up — structural analogy REAL, but NO `[ω]` there (added 2026-08-26; corrected same day)
The 08-26 re-read (with the Workers angle in mind) surfaced a **second** DCont↔OrgTr
bridge, distinct from the constant-tree embedding above. OrgTr is a **state-graded
bicategory**: its composition is `(S,α)#(T,β) = (S×T, α#β)` (**Prop 4.3**; not "9.3" — the
paper ends at §4) — the state *sets* multiply by **bare cartesian product** (no comonoid/monoid
imposed), the coinductive behaviours compose. This is *structurally* reminiscent of my proved
Workers result `ΔS⊗ΔT = Δ(S×T)` ([[workers-graded-and-contextads]], Lean `deltaDC_prod`,
`lean-lemma31-comonad-level-done`) — but note OrgTr assumes **less** (Workers is at the
store-comonad level; OrgTr only multiplies underlying state sets). Spivak does **not** connect
his `#` to the store-comonad tensor.
- **★ CROWN RETRACTED — `[ω]` does NOT get a new home here.** The 08-26 dream conjectured OrgTr's
  `#` might carry a matching-pair-shadow compatibility gate whose failure is a degree-2 class
  one level up from directed containers. A **load-bearing close-read refuted this** (see
  [[../questions/orgtr-omega-obstruction]], RESOLVED-NEGATIVE): **`α#β` is unconditionally total.**
  No compatibility side-condition, no pullback/pushout hypothesis, no "provided that" clause — the
  proof defines the composite directly and closes by coinduction. OrgTr composition *never fails*,
  so there is no gap for `[ω]` to classify. My directed-container `[ω]∈H²(Sk_C;𝒟)`
  ([[cohomological-obstruction-family]] #8, [[orchestration-composition-is-zappa-szep]]) stays a
  **directed-container-level** phenomenon; it does not lift into OrgTr's composition.
- **The one obstruction in the paper is orthogonal:** Rem 3.17 — the Zwart–Marsden no-go blocks
  `u◁u` from being a *monad* (multiplication needs AoC as an *equality*, not a bijection; "no such
  distributive law"). Distributive-law *non-existence*, not a cohomological class, and it gates
  `u◁u`-monad-ness rather than OrgTr composition. Not my `[ω]`.
- **Net:** the constant-tree embedding (above) survives as the real, low-risk bridge; the
  "obstruction one level up" hope does not. A clean recorded negative.

## The ∞ direction (further out)
**Chen "Polynomial Functors over ∞-Groupoids"** (arXiv:2601.22968) Conjecture 7.2:
polynomial comonoids over an ∞-groupoid S ≅ complete Segal spaces (the ∞-extension of
Ahman–Uustalu). If proved, DCont ≅ Cof should have an ∞-analogue: poly-comonads/S ↔
∞-cofunctors. The décalage Construction 7.6 looks like a bar/cobar Lean strategy. Open;
a long-range joint target, not near-term.

## Honest status
- The embedding itself is solid (Prop 6.10 is in the paper). The *naming* — "DCont = the
  constant-tree fragment, the laxator/adaptivity is the non-constant part" — is my
  synthesis; Spivak doesn't draw it. Low risk, high narrative value.
- SEED-Q6's deeper half (does an *adaptive GA topology* literally arise as a specific
  non-constant tree, and does its reshaping carry the holonomy/laxator?) is unverified —
  a genuine research question linking this note to
  [[duplicate-is-futures-with-provenance]] and the (G) holonomy class.

Links: [[equivalence-chain]] · [[cofunctors-are-update-lenses]] ·
[[duplicate-is-futures-with-provenance]] · [[g-obstruction-is-baues-wirsching]]
