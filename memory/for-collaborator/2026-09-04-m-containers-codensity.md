# M-containers proved — and the sketch's fullness criterion was wrong (it's codensity)

**MacBeth, 2026-09-04 (PROVE).** For Neil (this answers the two 09-04 emails) and Robin.
Full write-up: `proofs/2026-09-04-m-containers-codensity.md`. Registry `m-containers.json`
(validates, `proved`). Verification: `scratch/m-containers/{mcont,dcod,dnat}.py`.

## What's proved

1. **THM 1 (identification).** `M-Cont = Fam(Kl(M)^op)` on the nose, and the M-extension
   factors as `⟦S,P⟧_M = ⟦S,P⟧ ∘ M` — an M-container's functor is a *polynomial functor
   pre-composed with `M`*. This is the honest, clean answer to Neil: the whole "monad-lifted /
   probabilistic containers" idea IS my `Fam(C^op)` programme with `C = Kl(M)`, plus this one
   identity.

2. **THM 2 (faithfulness + fullness).** `⟦−⟧_M : M-Cont → [Set,Set]` is **always faithful**,
   and is **full ⟺ `M` is codense (`M ⇒ Ran_M M` iso) and every `(M−)^A` is connected**
   (affine `⟹` connected). The engine is one adjunction line:
   `Nat(Set(A,M−), H) = (Ran_M H)(A)`, so **the codensity monad `Ran_M M` is the invariant.**

## The correction (please note this, Neil)

My own scoping sketch said "full-faithful ⟺ `M` preserves coproducts, so `D` and `Maybe` both
fail." **That criterion is wrong for the target `[Set,Set]`.** Two independent reasons:

- "M preserves coproducts" is T1's connected-unit condition for the **coarser Kleisli-enriched
  target** `[Kl(M),Kl(M)]`, not for Set-endofunctors. `⟦−⟧_M = R∘⟦−⟧^{Kl}` where `⟦−⟧^{Kl}`
  (free coproduct completion) is *always* fully faithful and `R = (−∘F)` restricts along the
  free `F:Set→Kl(M)`; all the action is the gap between pure- and Kleisli-naturality = codensity.
- The coproduct-**preserving** writer monad `E×(−)` **fails** fullness for `|E|≥2`
  (`Φ(1)=|E|^{|E|}≠|E|`). Direct refutation of the coproduct criterion.

And the headline flips: **distributions `D` are affine + codense, hence FULL**
(`Nat(D^A,D)=DA` — natural operations are exactly affine combinations), whereas **Maybe,
exception `X+E`, writer, reader all fail** (exact AAG counts). So:

> **Probabilistic positions PRESERVE on-the-nose faithfulness of the container extension;
> error / partiality / read-only-context / nondeterministic positions DESTROY it. The
> dividing invariant is the codensity of the effect monad, computed by `Ran_M M`.**

This is a nicer story than the sketch's: it's not "all effects cost faithfulness," it's a
*sharp dichotomy* keyed to codensity, with probability on the good side.

## Honesty flags

- `D` full is graded `computed`, not `proved`: the reduction (`Nat(D^A,D)=DA`) is proved
  *modulo* the base rigidity lemma `Nat(D,D)={id}` (natural sub-`D`-valued endos are scalars) —
  standard but not re-proved here. If you know the clean citation for "the finite distribution
  monad is codense / its natural n-ary operations are the affine combinations," that closes it.
- THM 3 (composition = distributive law `M∘⟦q⟧⇒⟦q⟧∘M`, the ZS/`H²` obstruction; `D` composes,
  `Maybe` obstructs) is unchanged from the sketch and stays `speculative` — parked.

## Why it matters for the grant

- New bridge: **container-extension fullness ↔ codensity monads** (Leinster's line). Worth a
  short WRITE.
- The Maybe case is still the clean Impact story ("an agent may decline" = Maybe positions,
  fullness lost) — but now with the *correct* reason, and with a positive counterpart
  (probabilistic agents keep fullness).
