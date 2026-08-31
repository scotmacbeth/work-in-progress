# For Neil / Robin — the logic of containers is a *co-hyperdoctrine* (and a correction to yesterday's §6.2)

**MacBeth, 2026-08-28 (deep-work PROVE, fallback target).**
Proof: `proofs/2026-08-28-joint-bc-cont-cod.md`. Verification: `scratch/verify_joint_bc.py`
(exhaustive finite `Set`, all claims). Registry: `joint-bc-cont-cod` (`proved`, validator-clean).

## What I set out to do
The main target (T2 closedness = parametric-right-adjoint, matching **Weber TAC 18 (2007)**) has a
reading gate I could not open this session — Weber isn't in the seed or in `sources.json` (I know it only
from summary), and browsing was off. So I took the self-contained **fallback** the PROVE file names: close
the shape-level / joint gap in yesterday's `Cont(cod)` fibration proof.

## Headline
> **`Cont(cod) = Fam(cod^op)` is a *co-hyperdoctrine*.** The shape quantifiers exist
> (`∃_j = Lan_u ⊣ j^* ⊣ Ran_u = ∀_j`, unconditional). But the combined (shape × position) Beck–Chevalley
> and Frobenius are **one-sided**: they hold for the **right-adjoint (∀) quantifiers**, with conjunction
> `∧` replaced by disjunction `∨` (co-Frobenius), and **fail for the left-adjoint (∃) quantifiers**. The
> naive hope — a two-sided Lawvere hyperdoctrine — is false.

This is exactly the fibrewise-op philosophy pushed to its honest conclusion: opping a topos fibre swaps
limits and colimits, so the quantifier that carries the Frobenius/BC laws moves from `∃` (in `Set`) to `∀`
(in the container logic). `Cont(cod)` satisfies the **fibrewise opposite** of the classical laws.

## The obstruction (uniform, one line)
Every ∃-failure is the same: the left-adjoint quantifier is a `Set`-**product** across the fibre,
substitution is a `Set`-**sum**, and `sum-of-products ≠ product-of-sums` (`ac+bd ≠ (a+b)(c+d)`).
Equivalently the co-topos fibre `(Set/P)^op` is **not distributive** in the direction the ∃-laws need — the
fibrewise op of the fact that the topos `Set/P` *is* distributive. It is precisely `Set`'s
distributivity/extensivity that powers the classical ∃-BC+Frobenius; the op removes it. (Kindred to, but a
*distinct locus* from, the container program's `∐⊊⊕` boundary: there the base changes to Vec; here the base
stays extensive `Set` and the obstruction is manufactured by the fibre op.)

## The correction (please note — it touches yesterday's proof)
Yesterday's `cont-cod-fibration.md` **Prop 6.2** claimed co-Frobenius for the container **existential**
`A = (Π_!)^op`. **That attribution is wrong.** The fibrewise op of `Set`'s `Σ_!`-Frobenius yields the
co-Frobenius for `E = (Σ_!)^op` (the **right** adjoint), and `Π_!` has no Frobenius in `Set` to dualise —
`A` satisfies Frobenius for *no* connective. I've corrected §6.2 in place and flagged it. Root cause: §6.2
was asserted "by duality" and never checked at container level — the exact failure mode I keep a memory
about ("the summary is what gets audited"). Everything else in yesterday's proof (Thms 3.1, 5.1, 5.2,
Prop 6.1) stands.

## Why this is good news for the survey
It gives approach-(3) of the "containers over a base" survey a **crisp, defensible** place in the
landscape: not "a hyperdoctrine" (vague) but *"a co-hyperdoctrine — the fibrewise opposite of a Lawvere
hyperdoctrine, with co-Frobenius/BC on the ∀ side and an identified co-topos-non-distributivity obstruction
on the ∃ side."* That is a sharper claim than a full-Lawvere one would have been, and it's honestly the
truth. It also threads the program's distributivity/extensivity spine through the fibrational leg.

## Open (unchanged / new)
- **Weber p.r.a.** (the deferred main target) — still needs the reading gate. If someone can drop
  Weber TAC 18 (2007) into the seed / `sources.json`, I can do the definition-match properly.
- Intrinsic characterisation of the general `Poly`-pullback squares over which ∀-BC holds (I verified two
  families: shape-pullback and the shape/position exchange square).
- Propositional (`Sub(Set^→)`) truncation and its co-Frobenius — stated, not developed.

— MacBeth
