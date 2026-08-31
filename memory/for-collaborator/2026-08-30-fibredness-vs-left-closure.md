# For Neil / Robin — "▷ is not fibred in its left variable" is NOT my ◁-closure obstruction

**MacBeth, 2026-08-30 PROVE.** Full proof: `proofs/2026-08-30-fibredness-vs-left-closure.md`.
Registry `fibredness-vs-left-closure` (proved, validator green). Code
`scratch/fibredness-vs-closure/verify.py` — six checks, all green.

## The question

Braithwaite–Hedges–Mihejevs' *Polylang* (ACT 2026 extended abstract) says, in one parenthetical
clause of §3, that they cannot use Pradic–Price's fibred-endofunctor fixpoints "because the
composition product `▷` is not fibred in its left variable." Their varied variable is
`T_P(X)=X▷P` — **exactly** the functor `(−)◁q` whose right adjoint I proved does not exist over
`Set` (Workers Thm 2) and does exist over `Vec_fd` only after the tininess collapse (T4-left).
Same functor, same escape hatch (`|T|=1`), same `Σ_s T^{P_s}` formula. It really looks like one
obstruction in two vocabularies.

**It isn't.**

## What I proved

Shape fibration `π : Fam(C^op) → Set`, `π(S,P)=S` — the family fibration of `C^op`; a morphism is
cartesian iff every position component is an iso. For `q=(T,Q)`, three conditions on `L_q=(−)◁q`:
**(V)** vertical (`πL_q≅π`), **(F)** fibred (`πL_q≅F_0π`), **(C)** `L_q` has a right adjoint.

> **Theorem A (over `Set`).** `(V) ⟺ (F) ⟺ (C) ⟺ |T|=1`.
>
> **Theorem B (over `Vec_fd`, where tininess makes `◁=⊗`).** `(F)` holds **always**;
> `(V) ⟺ |T|=1`; `(C) ⟺ #\{t : Q_t≠0\}` is **finite**. Hence
> **`(V) ⊊ (C) ⊊ (F)`**, strictly — `q=(2,k)` is closed but not vertical, `q=(ℕ,k)` is
> **fibred but not closed**.

The separation is two-sided, so the answer is "no" whichever notion of fibred Pradic–Price meant.

## The part I think you'll like

Two things fell out that are better than the question asked for.

**1. `◁` *is* fibred in its right variable, and the base functor is `⟦q⟧` itself.**
`π(q◁p) = Σ_{t∈T}(π p)^{Q_t} = ⟦q⟧(π p)`. Moreover **both** variables of `◁` preserve cartesian
morphisms *unconditionally* — the position map is always a reindexing along the iso `φ^♯_s`. So
BHM's failure is purely a failure of **base-functoriality**, never of cartesianness: there is no
comparison map to be non-invertible, there is simply no functor on the base at all. (Corollary:
`μX.1+q◁X` *is* fibrationally constructible, its shape level being the W-type `μS.1+⟦q⟧S`. Their
three listed fixpoints are all right-variable, so their stated reason doesn't actually block them;
what it blocks is their own graded monad `T_P`. Worth telling them, gently — a two-page abstract.)

**2. One test, two probes.** Both conditions are the single question "is
`G_r(Z)=Fam(⟨Z⟩◁q,\,r)` familially representable?", evaluated at different `r`:

| probe | `r` | what it sees |
|---|---|---|
| **shape probe** | `(R,\,0)` (all positions initial, `C(0,X)=1`) | `G_r(Z)=R^{π(⟨Z⟩◁q)}` — the shape object only |
| **position probe** | `⟨I⟩` | whether the forced position object exists in the base |

Over `Set` the shape probe is the binding one and it forces `|T|=1` — so *closed ⟹ fibred*
conceptually, not by classification. Over `Vec_fd` the shape probe is **vacuous** (tininess has
already collapsed the shape object to `S×T`; constant functors are familially representable), and
the obstruction migrates to the position probe.

> **Fibredness = the shape object collapses. Left-closure = collapse *and* the collapsed
> coproduct is summable inside the base.** Over `Set` the only collapse mechanism is `|T|=1`,
> which trivialises summability too. Over a linear base collapse is generic, and the two decouple.

## Two of my own theorems got stronger on the way

- **Workers Thm 2 superseded.** Its counting argument (`|H([n])| ≥ 2^{2^n}`) only covers finite
  `T`. Replacing counting by a two-line **least-support lemma** (`x=(u,g)` lies in `\mathrm{im}\,F(A)`
  iff `\mathrm{im}(g)⊆A`, so supports are closed under intersection — the elementary form of
  Carboni–Johnstone) covers **all** `|T|≥2`, finite or infinite, *and* the degenerate `|T|=0` case
  the counting argument never addressed. The witness is `Z=ℕ` with `A_n=ℕ∖\{n\}`: the
  "eventually-`t_0`" set of sequences is invariant under every single-coordinate change but is
  neither `∅` nor everything.
- **T4-left Thm 3.1(2) sharpened.** The `Vec_fd` boundary is not "`T` infinite" but
  "**infinitely many non-zero positions**" — a `q` with infinitely many shapes all carrying the
  zero position object *is* left-closed, because zero positions contribute no summand. The `Set`
  analogue is false (`q=(2,∅)` is not closed), which is itself the two-probe diagnosis in action.

## Honesty

- BHM assert non-fibredness in one clause, with no definition and no proof. Cited as
  corroboration; the definition and both proofs are mine.
- `◁ := ⊗` on the tiny locus is a **definition**, not a deduction — `⟦−⟧` is not full over `Vec`
  (my T1), so the collapse pins the extension, not the object. Theorem B is literally about
  `(−)⊗q`.
- **The one open attribution point, and it is cheap.** Pradic–Price `2601.15420` is not on disk.
  My `sources.json` entry (graded `deep-read`) records their framing as *"fibred endofunctors over
  the fibrewise-opposite-of-the-codomain-fibration"* — which is verbatim my
  `Cont = ∫_{Set}(\mathrm{cod})^{op}`, whose projection is the shape map. But that read was
  grep-targeted at a different question, and my own 07-29 log still lists "is their fibrewise-op
  the same operation as mine?" as **open**. Their definition of *fibred endofunctor* was never
  extracted. **One fetch of `arXiv:2601.15420` closes this.** I proved both the `(F,F_0)` and the
  vertical readings precisely so the conclusion does not depend on the answer.
- Genuinely open: is "closed ⟹ fibred" true over an arbitrary base? Prop 5.2 gives only the
  shape-probe necessary condition; the `Set` upgrade uses a `Set`-specific lemma. No
  counterexample known.

## Why it matters for the grant

This is the **third** time two conditions that look like the same "canonical map is an
isomorphism" have turned out to constrain **different legs of one formula** (after Weber-`Φ` vs
T2-`δ`, and T2's conjuncts A/B). The resolution move was identical all three times: *write down
the single formula both conditions are about, and identify which factor each one constrains.*
Three occurrences is a **method**, not a coincidence — and a method is a better grant paragraph
than a theorem.
