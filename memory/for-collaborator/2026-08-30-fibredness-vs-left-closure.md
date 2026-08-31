# For Neil / Robin — "▷ is not fibred in its left variable" is NOT my ◁-closure obstruction

**MacBeth, 2026-08-30 PROVE.** Full proof: `proofs/2026-08-30-fibredness-vs-left-closure.md`.
Registry `fibredness-vs-left-closure` (proved, validator green). Code
`scratch/fibredness-vs-closure/verify.py` — six checks, all green.

> **Corrected 2026-08-31.** An earlier version of this note claimed the right-variable fibredness
> of `◁` (base functor `⟦q⟧`) and the unconditional preservation of cartesian morphisms in both
> variables as mine, under a heading offering them as a bonus. They are **not mine**: the first is
> **Pradic–Price, `2601.15420`, Lemma 15** (p. 14, proof p. 31) — *with the same base functor* — and
> the second is **Niu–Spivak `2312.00990`, Proposition 6.88** (p. 213), which Pradic–Price
> themselves cite. I fetched and read their paper on 2026-08-30 to close an attribution debt and it
> closed against me. What survives after the subtraction is stated in **"The part I think you'll
> like"** below and accounted for in full in §8 of the proof file. Nothing mathematical changed —
> only who is credited and what the results are claims about.

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

After subtracting prior art (see the correction note above and §8 of the proof file), what survives
is **1–3** below — the third is the one I would put in a grant paragraph — together with the
two-probe diagnosis in **4**, which is also mine.

**1. Theorem A supplies a *proof* of a remark Pradic–Price state without one.** Their Remark 16
(`2601.15420`, p. 14) reads, in its entirety: *"On the other hand, `X ↦ P ⋆ X` is not fibred."*
Their `Q ⋆ P` is my `P ◁ Q`, so their `X ↦ P ⋆ X` is exactly my `L_q = (−)◁q`. There is **no proof
and no justification anywhere in the paper or its 25 pages of appendices** — the only occurrences of
"Remark 16" are the statement and a back-reference in §4.2; Appendix B.1 proves Lemmas 14, 15 and 49
only. Their Definition 13.1 is *strict* (`shape ∘ F = F_0 ∘ shape^k` on the nose) where my (F) asks
only for a natural iso, so PP-fibred ⟹ (F) and Theorem A (ii⟹iv) refutes theirs *a fortiori* —
using only the **object part** of fibredness. And it says more than the remark does: it gives the
exact boundary `|T|=1` and welds it to `(V)` and to `(C)`. Recorded as **Corollary A′**.
*(Conservatively: I prove `C = Set`, which is the instance BHM's clause is about; PP assert Remark
16 for a general lextensive `C` and I do not prove that generality.)*

**2. Theorem B and the strict separation `(V) ⊊ (C) ⊊ (F)` are outside their framework entirely.**
`Fam(Vec_fd^op)` is not `Cont(Vec_fd)` — their `Cont(C)` is *internal*, objects are morphisms
`P : A → I` of `C` with base `C`, mine keeps an external shape *set* with base `Set`; the two agree
exactly at `C = Set`. And their standing hypothesis (§2.1, p. 7) is *"Henceforth, all categories in
sight shall be lextensive"*, which `Vec_fd` is not (`∐ ⊊ ⊕`). So PP-fibredness is simply undefined
there: **no conflict with them, and no support from them.** Theorem B is unambiguously mine.

**3. ★ And that hypothesis is itself the point.** Their *"all categories in sight shall be
lextensive"* is direct corroboration of the extensivity thesis. Theorem A says that over `Set` —
the extensive base par excellence — fibredness, verticality and left-closure are **the same
condition**, and the probe analysis below says why: extensivity leaves exactly one collapse
mechanism (`|T|=1`), which trivialises summability along with it. A framework in which every
category is lextensive therefore **cannot exhibit** `(V) ⊊ (C) ⊊ (F)` — the witnesses `q_2` and
`q_ω` live over a base the hypothesis excludes. Prior work assumes the very condition under which
the seams fuse, and so is structurally unable to watch them come apart. It also explains, with
nobody being wrong, why Remark 16 could sit unproved: inside a lextensive world the left-variable
failure and the closure failure are one phenomenon, and neither needs separating from the other.

**Cited background, not findings.** Two facts the argument leans on are prior art and are used here
as citations. `◁` **is** fibred in its *right* variable for every `q`, with base functor literally
`⟦q⟧`: `π(q◁p) = Σ_{t∈T}(π p)^{Q_t} = ⟦q⟧(π p)` — **Pradic–Price Lemma 15**, same base functor. And
**both** variables of `◁` preserve cartesian morphisms *unconditionally* — **Niu–Spivak Prop. 6.88**
over `Set`, which PP invoke by name in the Lemma 15 proof; the `Fam(C^op)` half with `◁ = ⊗` is
mine. Put together they *isolate* the failure: BHM's non-fibredness is purely a failure of
**base-functoriality**, never of cartesianness — there is no comparison map to be non-invertible,
there is simply no functor on the base at all, which is what makes it unrepairable. That isolation
is an observation about known facts, not a new theorem, and I now describe it that way. (Aside, on
the same footing: their three listed fixpoints `μX.1+A⊗X`, `1+A×X`, `1+A▷X` are all
**right**-variable, hence all fibred, so a fibrational construction would compute their shape level
as the W-type `μS.1+⟦q⟧S` — what such a construction *would* yield; I do not construct the
fixpoints. So BHM's stated reason does not, under my Definition 1.3, block the fixpoints they list;
what it blocks is their own graded monad `T_P`. Worth telling them, gently — a two-page abstract.)

**4. One test, two probes.** Both conditions are the single question "is
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
- **The attribution point is CLOSED, and it closed against me.** Pradic–Price `2601.15420` **is**
  on disk (`papers/pradic-price_2601.15420_fixpoints-poly-of-poly.pdf` + `.txt`), fetched and read
  2026-08-30; extraction in `scratch/2026-08-30-pradic-price-fibred-def.md`. Outcome, in full:
  their `shape` fibration **is** my `π` over `Set` (§2.2, pp. 8–9: *"exactly the fibrewise opposite
  of the codomain fibration"*), confirming the `sources.json` reading; their fibredness is the
  `(F,F_0)` form and **strict** (Def 13.1, p. 14), so PP-fibred ⟹ (F) and every negative result
  here holds *a fortiori*; **my Prop 2.2 is their Lemma 15**, re-attributed; **the `Set` half of my
  Lemma 2.1 is Niu–Spivak Prop. 6.88**, re-attributed; and in the other direction **Theorem A
  supplies a proof of their unproved Remark 16** (Corollary A′). Theorem B is outside their scope.
  I proved both the `(F,F_0)` and the vertical readings precisely so the conclusion does not depend
  on which they meant, and that hedge turned out to be the right one. Full accounting: §8 of the
  proof file.
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
