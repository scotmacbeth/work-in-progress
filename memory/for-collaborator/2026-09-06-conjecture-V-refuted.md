# Conjecture V is FALSE — the THM 3 residual corner is inhabited (free comm. unital magma)

**MacBeth, 2026-09-06 (PROVE). For Neil / Robin / (and Rick, if useful).**
Full write-up: `proofs/2026-09-06-conjecture-V-refuted.md`. Registry: `m-containers.json`,
node `conjecture-V-refuted-unital-magma` under `necessity-lemma-gap`.

## The one-line result
I was asked to prove **Conjecture V** — that the last open corner of THM 3's analytic converse is
*vacuous*, which would make "M-containers compose ⟺ M polynomial" **unconditional**. **It is not
vacuous. Conjecture V is false.** I have an explicit, natural, finite-component, computationally
verified witness sitting in the corner.

## The witness
**`U` = the free commutative UNITAL (non-associative) magma monad.** Signature: a unit `c` (arity 0)
and a commutative binary `μ` with `μ(x,c)=x`. Both equations are linear-regular ⟹ the theory is
operadic ⟹ `U` is analytic. Its species:
- `U[0] = {c}`  →  `a_0 = 1` (**nonempty finite** — property (a)).
- `U[n] = ` commutative binary trees on `n` labelled leaves, `|U[n]| = (2n−3)!!` (**all finite**).
- Unbounded degree (property (b)); balanced `2^k`-leaf trees have stabilizer
  `S_2 ≀ ⋯ ≀ S_2` (`k` times), so **unbounded wreath depth** (property (c)).

It is *literally the free commutative magma* (which Theorem P kills, since there `a_0=0`) **with a unit
adjoined**. Adjoining a unit moves `a_0: 0 → 1` while leaving the entire positive-arity structure —
and hence both unbounded degree and unbounded wreath depth — completely intact.

## Why the §4 obstruction sketch was wrong
§4 argued: "a nonempty constant part, substituted into deep structures, builds arbitrarily many
closed deep structures ⟹ `M∅` infinite." The hidden false step is **"substitute ⟹ build."** A **unit**
is precisely the constant that, when substituted, is **absorbed** (`μ(t,c)=t`) — it builds *nothing*.
So `M∅` stays `{c}`, finite, in perfect coexistence with unbounded depth. The sketch was correct for
a *generic* nullary generator (free magma-with-a-constant does have `M∅=∞`); it silently assumed all
constants are generators. The unit is the exception it forgot.

## What this costs us, and what it buys us
**Cost:** the dream of an unconditional THM 3 converse *via corner-vacuity* is dead. `U` defeats all
three closed classes at once — Theorem P (needs `a_0=0`), Theorem S (needs bounded degree), and the
cardinality law (`|U(1)|=Σ WE_n=∞`, saturated instantly). It is the genuine hard corner, not an edge
case.

**Buy:** the corner is now **sharp**, and it revealed the right invariant. Degree was a red herring;
**wreath depth** is the true axis. Sketch (**Theorem S′**, currently conjecture): for *bounded wreath
depth* `W`, any `a_0`, **any degree**, `A•A` contains a constituent of depth `> W` (a plethysm wreath
`H_c ≀ H` adds one nesting layer to a non-flat `H`) while every `B•A` (`B` flat) constituent is a
Young product of depth `≤ W`; depth is a conjugacy invariant, so `A•A ≇ B•A`. This **subsumes Theorem
S** (bounded degree ⟹ bounded depth) and collapses the residual to a single line:

> **THM 3 converse is open EXACTLY for `a_0 > 0` and unbounded wreath depth** — canonical test
> case `U`.

I re-derived the known `𝕄` (free comm. monoid) result as the *depth-1* instance of S′, and checked
the `D_4 = S_2≀S_2` non-Young separation. S′ needs a rigorous general "wreath depth" invariant
(finest support-splitting + finest imprimitivity blocks, with conjugacy-invariance and max/additive
laws) — that is the clean next PROVE target.

## The honest open question (sharpened)
Does `U`-container composition actually fail (i.e. is `U∘U ≅ ⟦r⟧∘U` impossible for polynomial
`⟦r⟧`)? I **expect yes** — `U∘U` has nested cross-level symmetry no flat power `U(X)^{B_s}` can
match — but neither the plethysm engine (`a_0=0`-blocked) nor the depth gap (`W=∞`-blocked) settles
it. A promising handle: the **positive part** `A′` (`A′[0]:=∅`) is a *sub-operad*, so `Ã′` falls to
Theorem P; the crux is whether closure of `Ã`-containers descends to `Ã′` along the cartesian monad
morphism `Ã′ ⟹ Ã`. Not automatic. That's exactly the remaining gap.

## For the grant / §5.7
Replace the false headline with the true, sharper one: *"M-containers compose iff M is polynomial —
proved for every analytic monad except those with a nonempty finite constant part and unbounded
wreath depth; the free commutative unital magma is the simplest such, and there the question is
open."* Honest, quotable, and it names the exact frontier.

*Everything above is verified in `scratch/2026-09-06-vacuity-{witness,wreath,confluence}.py`.*
