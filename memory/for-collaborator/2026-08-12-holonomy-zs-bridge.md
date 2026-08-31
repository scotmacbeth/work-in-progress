# The state/directed cross-mode bridge — PROVED (with an honest refutation inside)

**For:** Neil, Robin. **Session:** 2026-08-12 PROVE deep-work.
**Artifact:** `projects/proofs/2026-08-12-holonomy-composition-zs-bridge.md`.
**Engine:** `projects/scratch/general-M-liftings/zs_holonomy.py`.
**Registry:** `proofs/registry/holonomy-composition-zs-bridge.json` (status `proved`, validates).

## The headline
Two of the three proved composition modes — **state/isotropy holonomy** (update-monad liftings ≅
`Fun(𝔸(↓),Cat)`, 08-11) and **directed/Zappa–Szép reentrancy** (`[ω]∈H²`, 07-20/Lean) — now genuinely
**weld**, on the *same* ZS product. Composing two update monads that share a state set `S` (a
distributive law) is, by Ahman–Uustalu 2013, a **Zappa–Szép product `P⋈P'`** of the position-threading
monoids acting on `S`. Three claims were on the table; the honest verdict is **(a) proved, (b) refuted,
(c) reshaped and proved**.

## (a) The classifier composes — clean
The composite monad is again an update monad, for the ZS product monoid `P⋈P'` acting on `S`. By the
08-11 classification, its liftings are `Fun(𝔸(↓_⋈),Cat)`, and `𝔸(↓_⋈) = 𝔸(↓)⋈𝔸(↓')` — the ZS product
of the two action categories (same objects `S`, arrows `(p,p')`, composition = ZS multiplication). So
the *classifier composes by the ZS product of the factor classifiers*. Rigorous.

## (b) Isotropy does NOT compose — the refutation is the discovery
The conjecture was `Stab_{P⋈P'}(s) ≅ Stab_P(s)⋈Stab_{P'}(s)`. **False.** Compute-first (the guardrail
worked exactly as designed) killed it before I wrote a line of proof. Fold onto an internal exact
factorisation `G=P·P'` acting on `S`: then `Stab_{P⋈P'}(s) ≅ Stab_G(s)`, and *the factorisation of `G`
need not restrict to the point stabiliser*. Cleanest witness: `S₃ = A₃·⟨(12)⟩` on `{1,2,3}`; at `s=1`,
`Stab_G(1) = ⟨(23)⟩ ≅ C₂`, yet `Stab_P(1) = Stab_{P'}(1) = {e}`. Exhaustive sweep over
`S₃,S₄,A₄,D₄,ℤ/2×ℤ/2` (448 point-checks): the **containment** `Stab_P(s)⋈Stab_{P'}(s) ⊆ Stab_{P⋈P'}(s)`
holds *always*, and is *proper* in 268 of them (including the abelian `ℤ/2×ℤ/2`).

**Why this is better than the conjecture.** The generator `(23) = (132)·(12)` is a P-move then a P'-move
that returns to `1` although *neither leg fixes `1`*. Under (a) this is a nontrivial fibre automorphism
in the composite whose two factor holonomies are both trivial. **Orchestration synthesises holonomy that
neither agent has** — reentrancy created by composition, invisible to the parts. That is precisely the
grant's "composition remembers more than the parts," now with a theorem and a three-line witness.

## (c) Where `[ω]∈H²` honestly lives — the degree gap resolved
Guardrail 1 was right that "the two invariants are the same" is false: the holonomy is degree-1 (a
representation), `[ω]` is degree-2. The clean statement: in the **aligned** case (containment is
equality) with abelian normal `A=Stab_P(s)`, `B=Stab_{P'}(s)`, the composite isotropy is an extension
`1→A→E→B→1` with class `[ω]∈H²(B;A)`. For trivial action, `[ω]=0 ⟺ E≅A×B ⟺` every composite holonomy is
**unentangled** (the two agents' holonomies act on commuting registers of the fibre); `[ω]≠0 ⟺` entangled.
So **`[ω]` is the obstruction to the two H¹ holonomies assembling into an unentangled product** — an H²
class deciding whether an H¹ datum factors, never an equality of the two. The `ℤ/2` witness
(`ε=0→ℤ/2×ℤ/2`, `ε=1→ℤ/4`) is the *stabiliser-level shadow* of the orchestration reentrancy `[ω]=ε`.
I keep the two `[ω]`'s at **distinct sites** (handoff category vs point-stabiliser) and flag rather than
identify them — no repeat of the fusion-category conflation.

## Honesty ledger
- Scope: degree-1 proof-relevant polynomial liftings (inherited from the whole arc); (c) scoped to
  aligned + abelian + normal `A`; nonabelian ZS obstruction deliberately out of scope
  (`g-obstruction-is-h2-class`).
- I direct-read the Ahman–Uustalu DL PDF this session for the ZS-composition claims (clears a deep-read
  TODO).
- Open, conjectural: is the stabiliser `[ω]` the restriction of the handoff `[ω]` along `B·Stab→Sk_C`?

## Suggested next
Natural `/lean` feeder: formalise (b') containment + the `S₃` emergent-holonomy witness (finite,
group-theoretic — tractable), and/or the `ℤ/2` `[ω]` dichotomy at stabiliser level. And a `/write`
paragraph for the grant Impact section: "unprotected orchestration synthesises holonomy; a degree-2
class certifies when the composite is a clean product of the parts."
