# The two container-feeds of a monad entwine — one direction only (2026-07-27)

**For Neil / Robin.** PROVE session result. Full proof:
`proofs/2026-07-27-monad-comonad-entwining.md`; harness `scratch/monad-comonad-transfer/entwine.py`;
registry `proofs/registry/monad-comonad-entwining.json` (proved, trustcheck OK).

## The question (Neil's Ch4 territory)
One Set-monad `M` feeds a container two ways, locked to the fibrewise op:
- **shapes → monad** `T_M(S,P)=(MS,P^\star)` — Ahman–Bauer 2409.17664 Thm 6.3 (the `∏`-cointerpretation
  weak Mendler algebra `P^\star(m)=∏_{leaf b}P(x_b)`);
- **positions → comonad** `G_M(S,P)=(S,M∘P)` — our transfer (proved + Lean).

Do they interact via a mixed distributive law? (Distributive laws are the seed's core tool.)

## The answer
**Yes, canonically — and in exactly one orientation.** The map every functor has by the universal
property of a product,
$$\mathrm{str}: M\big(\textstyle\prod_b Z_b\big)\to\prod_b M Z_b,\qquad w\mapsto(M\pi_b\,w)_b,$$
is (because container morphisms run backward on positions) the backward map of a genuine **entwining**
$$\lambda: T_M\,G_M \Longrightarrow G_M\,T_M$$
— the *standard* mixed-distributive-law orientation. All four axioms hold, for **every** such `M`:
E3=naturality of `η`, E1=`i` is identity on singleton products, E4=naturality of `μ`, E2=naturality of
`str` w.r.t. the product-reindexing (= A–B's `j`-naturality, machine-verified incl. branching `Pf`). So
`G_M` lifts to a comonad on `T_M`-algebras and `T_M` to a monad on `G_M`-coalgebras.

**`λ` is just "`M` oplax-preserves products, transported to positions."** Fibrationally it's a
Beck–Chevalley 2-cell: `G_M=(M^{op})_*` is vertical, `T_M` covers the base monad `M`, and `λ` compares
apply-`M`-on-base-then-fatten vs fatten-then-apply.

## The twist you'll want to know
The **opposite** orientation `G_M T_M ⇒ T_M G_M` (which needs the *lax* map `∏M→M∏`) **fails** as soon as
`M` genuinely branches. Concretely for `M=Pf` and `X=(\{a,b\},\,a\mapsto\{0,1\},\,b\mapsto\{0\})` it breaks
the monad-multiplication axiom: one path gives a **correlated** set, the other the **full cartesian
product** — *union-of-products ≠ product-of-unions*.

**The obstruction is branching, not non-commutativity.** `Pf` is commutative and still fails; arity-≤1
monads (`Maybe`, exception, `Writer`, `Id`) satisfy both orientations because `str`=lax=iso there. I had
initially guessed the obstruction would be commutativity — the computation corrected me.

## Grant hook
A new interaction 2-cell in the `Cont` calculus, sitting on top of Neil's Ch4 pair (`T_M` monad / `G_M`
comonad). Candidate for the distributive-law / composition strand — and a clean "one canonical direction,
with a named obstruction" story. Fits after the transfer chapter.

## Open (honest)
1. E2 general index-chase over an arbitrary Mendler `j` (mechanical; done for the `∏` examples).
2. Non-`∏` weak Mendler algebras: is there a canonical `λ` without the product structure? (No evident map.)
3. A crisp match of the descended entwining to a *named* free-monad-over-cofree-comonad law on `Set`.

Questions welcome — especially whether you want this as its own short section or folded into Ch4.
— MacBeth
