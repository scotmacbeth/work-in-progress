# Independent sketch (MacBeth, main context, BEFORE seeing the agent's answer)

Written deliberately in advance so the agent's report can be AUDITED rather than
believed. If the agent's computation disagrees with this, one of us is wrong and the
disagreement must be resolved explicitly, not averaged.

## Step A — terminal (VERIFIED BY HAND, confident)
Terminal in `Cont(Set)` is `y^0 = (1, ∅)`: unique forward `S → 1`, unique backward
`∅ → P_s`. And `1 ◁ q = (Σ_{s∈1}(∅ → T), Σ_{a∈∅} Q) = (1, ∅) = 1`.
**So `T1 = 1`, the Weber slice is trivial, and p.r.a. ⟺ genuine LEFT adjoint.**

## Step B — products (VERIFIED BY HAND, confident)
`p × p' = Σ_{(s,s')} y^{P_s ⊔ P'_{s'}}` (product of shapes, COPRODUCT of positions —
this is the `Set^op` fibre). Hence
`(p×p')◁q = Σ_{s,s'} ∏_{P_s ⊔ P'_{s'}} q = (p◁q) × (p'◁q)`. Preserved.

## Step C — equalizers (SKETCH ONLY, the crux, NOT verified)
Morphism `f = (u, φ)` where `u : S → S'` and `φ_s : P'_{u s} → P_s` **backward**.
Equalizer of `f=(u,φ), g=(v,ψ)` in `Fam(Set^op)` should be:
- shapes `E = {s ∈ S : u s = v s}` — an equalizer (SUBSET) of shapes;
- positions `P_E(s) = P_s / ~`, the **coequalizer in Set** of `φ_s, ψ_s : P'_{us} ⇉ P_s`
  — a QUOTIENT, because equalizer in `Set^op` = coequalizer in `Set`.

**So a limit in `Cont` is: subset on shapes, quotient on positions.** That mix is the
whole difficulty and is where a careless argument dies.

Now push through `(−)◁q`, whose shapes at `s` are `(P_s → T)`:
- On the equalizer: shapes `Σ_{s∈E} (P_s/~ → T)`.
- Functions out of a quotient = exactly the functions out of `P_s` that are **constant
  on ~-classes**, i.e. a SUBSET of `(P_s → T)`.
So `(−)◁q` turns the position-quotient into a shape-subset — and a subset of shapes is
what an equalizer of shapes looks like. **This is suspiciously well-matched**, which
makes me expect preservation, i.e. outcome (α): p.r.a. for every `q`, crown re-filing
REFUTED.

## My prior, stated in advance
I expect **(α)**. Reasons: (i) the matching above; (ii) `◁` distributes over `+` on the
left and preserves `×` and `1`, which is left-adjoint-shaped behaviour, not
right-adjoint-shaped; (iii) my track record on "are these two conditions the same?" is
three refutations in a row, and this would be the fourth.

## The trap to watch for
p.r.a. asks for a **LEFT** adjoint to `(−)◁q`. My T4-left theorem is about the **RIGHT**
adjoint (the closure), which over `Set` exists iff `|T|=1`. **These are different sides.**
If the agent reports "`(−)◁q` is p.r.a. iff `|T|=1`" I should suspect it has silently
answered the right-adjoint question — the one I already know the answer to — and I must
make it show which adjunction it actually verified, in which order.

## Size caveat
"Preserves all small limits" ⟹ "has a left adjoint" needs a solution-set / co-well-
poweredness condition. `Poly`/`Cont` is not locally presentable. If the agent asserts the
implication without addressing this, the result is `computed`, not `proved`.
