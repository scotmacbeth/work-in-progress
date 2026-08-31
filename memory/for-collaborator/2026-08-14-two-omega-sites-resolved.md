# Gap #3 closed: the two [ω] sites are irreducibly distinct — with a scope-correction to the bridge

**MacBeth, 2026-08-14 PROVE session.** Full proof: `proofs/2026-08-14-two-omega-sites-isotropy-restriction.md`.
Registry: `proofs/registry/two-omega-sites.json` (validates, status `proved`). Engines:
`scratch/two-omega-sites/{comp1_bw_isotropy.py, comp2_geometric_splitting.py}`.

## What was asked (PROVE.md 2026-08-14)
Refute the naive "stabiliser class = isotropy-restriction of handoff class" (Part 1), then try to
build a common-refinement functor recovering both (Part 2). Both are 𝔽₂ with generator ε; do they
coincide?

## What I proved
1. **Part 1 (primary, clean negative).** `Sk_C` (the handoff orbit category) is **automorphism-rigid**
   — every object has only its identity endomorphism (the token τ was pushed into the coefficient
   `𝒟(Sup)=ℤ/2`, not into an arrow). So the standard isotropy-restriction map
   `i_x*: H²_BW(Sk_C;𝒟) → H²(Aut(x);𝒟(x))` has target `H^{≥1}(1;·)=0` for every `x`: it is the **zero
   map**. Hence `i_x*[ω_h]=0`, and it cannot equal the nonzero stabiliser class. Naive identification
   FALSE. (At cochain level: `ω_T=(0,ε)` is supported on non-loops, so its restriction to loops is 0.)

2. **Part 1.5 (the real discovery — a scope-correction of my own bridge §3).** In the ZS geometry
   (`G=P·P'`, `E=Stab_G(s)`, `A=E∩P`, `B=E∩P'`): `A∩B ⊆ P∩P'={e}` always. If `s` is **aligned**
   (`E=A·B`) and `A◁E`, then `B` is a subgroup complement, so `E=A⋊B` **splits** and `[ω_st]=0` — for
   any action. The nonsplit `ℤ/4` witness is **geometrically impossible**: `|A|=|B|=2, A∩B=1` gives two
   distinct involutions, but `ℤ/4` has a unique involution ⟹ `E≅V₄` not `ℤ/4`. And non-aligned ⟹
   `|E/A|>|B|` so `E/A≇B` and the extension `1→A→E→B→1` with `B=Stab_{P'}(s)` doesn't even typecheck.
   **So the geometric stabiliser class is defined only when aligned, and is then 0.** The bridge §3
   table's `[ω]=ε ⟺ E=ℤ/4` row is abstract extension theory, *not* the aligned ZS point-stabiliser
   geometry it is stated under. Confirmed by exhaustive sweep (S₃,S₄,A₄,D₄,V₄,D₁₂,A₅): `(C₂,C₂,C₄)`
   never occurs; no aligned+normal case is ever nonsplit.

3. **Part 2 (obstruction, for ALL functors).** Key lemma: isotropy restriction is natural in functors,
   `i_a*∘F* = F_a*∘i_{Fa}*`. Rigid target ⟹ `i_a*F*Ω=0` for every `Ω`. So for **every** functor
   `F:𝔸(↓_⋈)→Sk_C` and every state `s`, `i_s*F*[ω_h]=0`: no comparison functor can relocate the handoff
   class into an isotropy group. The reverse `BG`-cospan also collapses (right-cancellation forces
   `g_s=g_{s₂}`, so any pullback lands in `B²`). The two sites are irreducibly distinct.

## Why they rhyme without being equal
`H²_BW` has two structure maps: **isotropy restriction** (loop/automorphism part) and the complementary
**off-diagonal/nerve** part (chains through distinct objects). The handoff class is off-diagonal
(invisible to isotropy); the stabiliser class is pure isotropy. The single ZS bit `ε` surfaces in
*both* — once as "does a serialising distributive law exist?" (handoff), once as "does the isotropy
group split?" (stabiliser). Two images of one datum under two **incomparable** maps, not two
restrictions of one class.

## The one honest gap
The reverse **general many-object cospan** `Sk_C→𝒞←𝔸(↓_⋈)` with a single `Ω` restricting to both is
obstructed only when the image of `[p]` is right-cancellable; I proved the `BG` case and the specific
forward direction (all `F`), but not the fully general cospan. I believe the off-diagonal-vs-isotropy
invariant obstructs it; flagged as `general-cospan-open` (speculative) in the registry.

## Ask for Neil/Rick
- **Rick (H²/cohomological-obstruction peer):** the Part 1.5 collapse (aligned ⟹ `[ω_st]=0`) means my
  earlier bridge §3 "aligned abelian `[ω]∈H²(B;A)`" witness is only ever the *zero* class in the aligned
  scope. Do you agree the nonzero representative is non-geometric (abstract extension theory grafted
  onto the aligned hypothesis)? This is exactly the fusion-conflation trap turned on my own file.
- **Neil:** grant-wise this *strengthens* the orchestration story (two provably-distinct obstructions,
  one ZS bit, two incomparable homes) and inoculates the book's emergent-holonomy section against the
  conflation error it was flagged for. Worth a sentence in the Impact section?
