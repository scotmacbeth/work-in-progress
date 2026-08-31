# State liftings are HOLONOMY-FREE — the grading collapses (2026-08-10 PROVE)

**MacBeth, deep-work.** Closes the structural question the 08-09 open note posed, with a
sign-flipped surprise. Full writeup: `proofs/2026-08-10-state-liftings-holonomy-free.md`.
Engines: `scratch/general-M-liftings/{honest,lean_assoc,copresheaf,product_SxC}.py`.

## The one-paragraph story
We expected State's `S^S`-threading to hand back a *finer* object than Reader's `E`-indexed
categories — an "`S^S`-graded / store-internal category." **It hands back a coarser one.** The
transformation monoid contributes only its *connectivity*. Since `S^S` acts transitively on `S`,
there is one orbit, hence (conjecturally) **one global small category**: **State liftings ≅ Cat**,
via `C ↦ 𝕊×C` (`𝕊` = action category of `S^S↷S`). Reader is the `π_0(𝕊)=|E|` case; State is
`π_0=1`.

## What is solid (proved / machine-verified, |S|=2, polynomial)
- Reduction (Prop A′) + counit-on-`A_id` + threading `σ(s)=t_s(T(s))` = `𝕊`-composition.
- **Purity forced**: inner (naturality) + full (left-unit).
- **Soundness `Cat ↪ liftings`**: `𝕊×C` is a lifting for every small `C`. Constructed
  explicitly; all three monad laws checked by a genuine finite-`Cont`-morphism engine
  (`honest.py`) and a cross-validated sampling-associativity checker (`lean_assoc.py`).
  Verified for `C` = `1`(=Σ), `BM` (`Z/2,Z/3,AND`), walking-arrow, discrete; non-monoids fail.
- **Count match**: profile `[(2,0),(0,2)]` ↔ the **4 monoids on 2 elements** — Reader's exact
  `B_0²→4` mechanism.

## What is REFUTED (computed) — kill these guesses
- "liftings = categories over `𝕊` / discrete Conduché fibrations / copresheaves `𝕊→Set`":
  **false.** Every nontrivial `𝕊`-action (representables `𝕊(0,-)`,`𝕊(1,-)`, a twisted constant
  action) **breaks associativity**. Only the *trivial* (constant-fibre = product) action lifts.
  Root cause: the grade `σ=thread(T,(t_s))` is **not** the composite `𝕊`-arrow `t_s∘T` (they
  agree only at the source), so any fibre-transport keyed to `𝕊`-morphisms is inconsistent.
- "localise a category to one state" (vertical-only): fails the everywhere-defined condition.
- "per-state-different fibres": unroutable — `𝕊` is connected, so one global `C` is forced.

## The open problem (for whoever picks this up)
**Completeness**: prove `C↦𝕊×C` is *onto* (⟹ State liftings ≅ Cat). The clean home is the
**substitution / plethystic monoidal structure `⊛`** on `[Set^S,Set]`-families whose comonoids
are the liftings — show its comonoids are **holonomy-free** (transport along the threading is
forced trivial). That single lemma would also give the **general-`M`** statement:
> liftings of `M` ↔ **`π_0`(the position-threading)-indexed families of small categories, with
> trivial transport**.
The general-`M` "position-threading action" still needs a clean definition when `P_M` varies
with the shape (State/Reader both have constant `P_M`, which is why they were tractable).

## For the grant / book
Ch7 payoff, sharpened: predicate liftings weld to `Cat`, and the *store monad's own algebra is
invisible to its liftings* — a crisp "grading-collapses / holonomy-free" theorem. Neil's steer
was fibrational language; this is exactly a statement about the codomain fibration's monad
liftings, and the surprise (coarser, not finer) is quotable.
