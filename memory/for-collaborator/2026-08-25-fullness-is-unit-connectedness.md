# For Neil/Robin: the fullness of the container extension is UNIT-CONNECTEDNESS, not extensivity

**MacBeth, 2026-08-25 (PROVE).** Neil's #1 (do the four monoidal structures generalize to
`Fam(C^op)`; is `⟦−⟧` full/faithful; is the hypothesis extensivity?). Flagship T1 is done — and
it corrects the conjecture. Full write-up: `proofs/2026-08-25-fullness-unit-connectedness.md`.

## The one-line answer

`⟦−⟧ : Fam(C^op) → C\text{-}[C,C]`, `⟦S,P⟧=∐_s[P_s,-]`, is **fully faithful iff the monoidal
unit `I` is connected** — `C(I,-):C→Set` preserves small coproducts. That's the whole
criterion. The proof is short: enriched co-Yoneda turns the hom into `∏_s C(I,∐_t[Q_t,P_s])`,
and the comparison against the container-hom `∏_s ∐_t C(Q_t,P_s)` is exactly the canonical map
asking whether `C(I,-)` preserves the coproduct.

## The correction you'll want to see (this is the interesting part)

**It is NOT extensivity.** `Set×Set` is (l)extensive but `⟦−⟧` is *not* full there, because its
unit `(1,1)` is disconnected: `C((1,1),(X,Y)+(X',Y')) = (X+X')×(Y+Y')` picks up cross terms
`(x,y')` that no single summand supplies. Cleanest witness: source `({s},(1,1))`, target
`({t₁,t₂},((1,1),(1,1)))` — **2 container morphisms, 4 natural transformations.** The two
"crossed" transformations are real and unrepresentable.

So:
- **Set** works because `1` is *connected* (I re-derive AAG and name its hidden hypothesis).
- **Vec** fails because `k` is connected as an object but `C(k,-)`=forgetful doesn't preserve
  `⊕` — the `∐⊊⊕` crux, now one instance of the general criterion.
- **Set×Set** fails despite extensivity. Extensivity is *neither necessary nor sufficient.*

Bonus honesty: `⟦−⟧` is **not faithful over Vec** either (the two container morphisms `(f,0)`,
`(f',0)` both give the zero natural transformation). "Faithful always" in the brief is false;
faithfulness = `I`-disjointness of coproduct injections.

## Why the field always said "extensivity" (I think this is the real reconciliation)

Two different theorems get fused at `C=Set`: (a) full-faithfulness of the *fixed* extension
`⟦−⟧` — governed by connectedness of the *enrichment base's unit*; and (b) Diers' *reconstruction*
`S=π₀(el F)` from an abstract familially-representable `F:C→Set` — governed by extensivity of the
*codomain* `Set`. At `C=Set` base = codomain, so "extensivity" reads off both and the
distinction is invisible. Off `Set` they split, and it's (a) that controls our `⟦−⟧`.

And it does **not** contradict Gambino–Kock: their polynomials are the *fully internal*
construction (shapes internal, slices), whose representation theorem does hold over LCCC bases
like `Set×Set`. Ours is the *mixed* `Fam(C^op)` (external shape-set `∐`, internal positions) —
Dorta–Jarvis–Niu's setting. External `∐` of internal homs is exactly what a disconnected unit
drops. The two constructions agree only over `Set`.

## What this gives the grant

- **T3 (change of base = change of enrichment)** falls out: `F:Set→C` lax monoidal moves the
  extension into `C`-enriched functors; full-faithful iff the new unit is connected. Free-vec
  `F1=k` isn't connected → linearizing a container *loses exactly* `∐⊊⊕`. This is the precise
  sense in which **Vec-enrichment is the invariant view** — your leaning, now a theorem.
- **T2 (closedness)** I have only as conjecture (adjunction shapes located; the Day-right-adjoint
  bookkeeping and the `◁`-coclosure-via-Lan criterion are honest gaps — see §6 of the writeup).
  These are the natural next PROVE targets if you want them pushed.

## Question for Neil

Is the unit-connectedness criterion the framing you want front-and-centre for the grant's
"theory" pillar (it's cleaner and more general than "extensivity", and the Set×Set
counterexample is memorable), or would you rather I fold it into the existing Vec-attention
unification note as the general theorem the worked instance rides on? I can WRITE either.
