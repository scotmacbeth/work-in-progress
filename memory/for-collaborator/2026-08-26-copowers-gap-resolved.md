# For Neil/Robin — the copowers gap on the connected-unit criterion is (largely) closed

**MacBeth, 2026-08-26.** Follow-on to flagship T1 (`proofs/2026-08-25-fullness-unit-connectedness.md`).
Full write-up: `proofs/2026-08-26-copowers-gap-writer-monad.md`. Registry:
`registry/copowers-gap-writer-monad.json` (**proved**).

## The question
T1 said: `⟦−⟧ : Fam(C^op) → C-[C,C]` is fully faithful **iff the unit `I` is connected**
(`C(I,-)` preserves small coproducts). But the *necessity* half was only proved on **copowers**
`κ·I`, the *sufficiency* half needs **all** coproducts. Gap: does the one-parameter copower test
certify fullness?

## What I proved
Let `M = End(I)` (commutative, symmetric base). The copower functor `(-)·I` is left adjoint to
`C(I,-)`, and it's a **monoidal** adjunction (`(-)·I` strong monoidal from `(Set,×)`).

1. **Writer-monad reduction.** `C(I,-)` preserves copowers of `I` **⟺** the induced Set-monad
   `C(I, (-)·I)` is the **writer monad `(-)×M`**. (So the copower test = "the monad is as simple as
   possible".)
2. **Comparison reduction.** Then `Eilenberg–Moore = M-Set`, with comparison `K:C→M-Set`,
   `K(X) = (C(I,X),\ \text{precomposition})`. Since `M-Set→Set` creates colimits,
   **full coproduct preservation ⟺ `K` preserves coproducts.**
3. **Extensivity upgrade (the deliverable).** If `C` is **extensive** then
   **copower test ⟺ all-coproduct preservation ⟺ `I` indecomposable & non-initial.**
   Proof: the extensive decomposition formula forces `I` to have no nontrivial coproduct
   decomposition (else there's a map `I→I⊔I` outside the image of `γ₂`, breaking the copower test).

## Why this is the answer you want
**Every intended base is extensive** — `Set`, all presheaf/Grothendieck toposes, `Set×Set`. So the
copower test *decides fullness* there, and it's a genuinely checkable one-parameter condition
(`I` indecomposable + non-initial). The only closed-monoidal bases in the program that are *not*
extensive are the **additive** ones (`Vec`, `R-Mod`, `CMon`), and those **fail the copower test
already** (the zero point makes copowers carry sums). So across the whole zoo, the copower test is
sound and complete for fullness.

## The honest caveat
The *raw* implication "copower test ⟹ all coproducts" **without** extensivity I did **not** settle.
I reduced it to "`K` preserves coproducts" and isolated the exact obstruction (a *mixed point*
`I→∐X_t` not lifting through `∐εₓ`), and I checked that **no standard construction separates them**
(additive/thin fail the test; Day-convolution and Artin-gluing `Gl((-)²)` satisfy both — the last
verified numerically). My read: closedness controls maps *out* of coproducts (vacuous here), not
*into* them, so there's no monoidal reason for the upgrade — I'd expect an exotic non-extensive
separator to exist, but I have none. That's the sharpened open question `(Q′)`.

## Question for you
Is this the right altitude to stop? For the grant's *applications* (all topos/Set-based) the criterion
is now a clean, checkable theorem. Chasing `(Q′)` means hunting an exotic non-extensive closed
monoidal category — interesting, but possibly a drawer item. I'll hold off on the T2 closedness
moonshot per your steer unless you want the residual pushed.
