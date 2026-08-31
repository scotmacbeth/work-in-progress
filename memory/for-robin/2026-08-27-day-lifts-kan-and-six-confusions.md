# For Robin — Day convolution, Kan extensions, and your six confusions

*(2026-08-27. In answer to your thread UID 127–130. The one-line headline first, then the
computable examples, then the small confusions, then the RH line.)*

## The headline: your six confusions are ONE seam — and it's the seam I prove theorems about

Every one of your questions is circling a single distinction: **cartesian vs. non-cartesian
monoidal structure**. The "easy" side of everything you noticed (adding, splitting `n=i+j`,
`s_λ(X+Y)`, Littlewood–Richardson, EGF multiplication, union of sets) is the side where the
tensor is a **coproduct** — a genuine categorical sum, which forces a positive combinatorial
rule. The "hard" side (multiplying, factoring `n=d·e`, `s_λ(XY)`, Kronecker, Dirichlet,
intersection/tensor) is the side where the tensor is **not** a categorical product — and the
absence of a universal property is *exactly* why there is no rule and no positivity.

That cartesian/non-cartesian line is the axis my whole container programme lives on (I call the
good behaviour **extensivity**: coproducts that behave like disjoint union). So your "Claude
dump" and my Fam(C^op) work are the same mathematics from two directions. Your PDF is correct —
it is a theorem, not a metaphor — and I'll show you why, in your own language.

## 1. Kan extension = induction (you already compute these every day)

You asked for *"one example I can compute rather than a definition I can recite."* Here it is:
**a left Kan extension is an induction, and the Littlewood–Richardson rule IS a Kan-extension
formula you already know.**

- `Res` (restriction of a symmetric function / representation, `S_{m+n} ↓ S_m×S_n`) is the
  easy, "just relabel" operation. Categorically it's **precomposition** with the inclusion.
- `Ind` (induction, `S_m×S_n ↑ S_{m+n}`) is the "freest way to extend back up." Categorically
  it's the **left adjoint to Res** — and *left adjoint to precomposition* is the definition of
  **left Kan extension**.
- Frobenius characteristic turns the induction product into the LR product:
  `s_μ · s_ν = Ind_{S_m×S_n}^{S_{m+n}}(s_μ ⊠ s_ν) = Σ_λ c^λ_{μν} s_λ`.

So: **`s_μ · s_ν = Σ c^λ_{μν} s_λ` is the evaluation of a left Kan extension.** You have been
computing Kan extensions since you learned the LR rule. `Ran` (right Kan extension) is the mirror:
limit-flavoured, "restrict / coinduce / cofree," the right adjoint side.

Your half-memory — *"pushouts and pullbacks are special cases somehow"* — is right, and here's
which way round: **Left Kan = colimit-flavoured (pushout, coproduct, induce, free, extend);
Right Kan = limit-flavoured (pullback, product, restrict, cofree).** A pushout is a particular
colimit, so it's a particular left Kan extension; a pullback is a particular limit, a right Kan
extension. Kan extensions are the general "best approximation when you push a functor along a
map"; specialise the map to "collapse everything to a point" and Lan becomes plain colimit, Ran
plain limit.

## 2. Day convolution = "multiply by inducing"

Day convolution is exactly this recipe, applied to a monoidal structure on the base:

> To multiply two species / Schur functors `F, G`:
> (1) put them side by side — the external product `F ⊠ G`, an object on *pairs*;
> (2) **induce (left-Kan / push forward) along the base tensor** back to single objects.
> `F ⋆ G = Lan_⊗(F ⊠ G)`.

Its universal property is the one line in your PDF:
`Nat(F ⋆ G, H) ≅ Nat(F ⊠ G, H∘⊗)`. Take `H = S_λ`, expand `S_λ` of a base-tensor, read off the
multiplicity — that's Props 3.1/3.2. **Which base tensor you push along is the only choice, and
it gives the four lifts:**

| base tensor ↓ | the "induce along" map | result | degrees |
|---|---|---|---|
| `⊕` direct sum | addition `S_m×S_n → S_{m+n}` | **LR product** `Σ c^λ_{μν} S_λ` | `|λ|=|μ|+|ν|` (add) |
| `⊗` tensor | diagonal `S_n×S_n → S_n` | **Kronecker** `Σ g(λ,μ,ν) S_λ` | `|λ|=|μ|=|ν|` (preserve) |

The degree check in your PDF §4 is now obvious: `⊕` adds sizes because you induce *up* to
`S_{m+n}`; `⊗` preserves size because both factors and the result live at the *same* `n`. And the
Kronecker column is hard for a structural reason, not an accident: its "induce along" map is the
**diagonal**, which is not a coproduct injection — there is no universal property to force a
positive rule. That's Remark 5.1's cartesian/non-cartesian swap.

**The functor category (your Q4 "what is it a category OF?"):** in all four cells it is the same
one — `[𝔹, Vect] ≃ ⊕_{n≥0} Rep(S_n) ≃ {polynomial functors Vect_fd→Vect}`, i.e. **the Schur
functors** / the representation ring of the symmetric groups / linear species. Day convolution
takes a monoidal structure *downstairs* (on Set or Vect) and installs a product *upstairs* on this
one category. Four downstairs tensors → four upstairs products → your 2×2 table.

Your three example bases, same machine:
- **`(Vect_fd, ⊕)` and `(Vect_fd, ⊗)`** → the two Vect rows above (LR and Kronecker); decategorify
  to `Sym` with ordinary multiplication and with the internal/Kronecker product.
- **`(𝒫(A), ∩/∪)`** → the *toy* case with no representation theory: functors out of the powerset
  poset are `A`-graded objects, and Day convolution along `∪` (or `∩`) is graded convolution
  `(F⋆G)(S) = ⊕_{S=S'∪S''} F(S')⊗G(S'')`. Good place to watch the machine run with the reps
  switched off.
- **`(Vect, braiding/Hecke)`** → the **q-deformation** of the same table: the braiding *is* the
  `q`, and the lift produces Hecke-deformed / canonical-basis structure constants. This is exactly
  your F_1 thread (Q3) reappearing — `q→1` collapses the braiding and you fall back to the
  symmetric (S_n) table. I'd flag this as the deep one; the honest statement is "same recipe, base
  now braided," and the computations live in the Hecke / canonical-basis literature.

## 3. Why the two rows match (your Q6 — real or word-matching?)

**Real.** The free-vector-space functor `k[−] : (FinSet, ⊔, ×) → (Vect, ⊕, ⊗)` is **bimonoidal**
(`⊔ ↦ ⊕`, `× ↦ ⊗`), and a strong monoidal functor downstairs carries each Day lift to the
corresponding one upstairs. So `EGF ↔ LR` and `Dirichlet ↔ Kronecker` are literally **one pair of
columns seen through `k[−]`** — a theorem. (In my own notes this `k[−]` is the "change of
enrichment" functor T3; the reason the linear side loses positivity/combinatorics is that `k[−]`
does not preserve the coproduct as an *extensive* coproduct — `⊔` is disjoint union but `⊕` is a
biproduct. Same fact, two vocabularies.)

The shared structure with a name: **the easy column is the extensive/coproduct one; the hard
column is where the tensor stops being a categorical product.** "Adding is easy, multiplying is
hard" is not a slogan — it is the statement that coproducts have universal properties (hence
combinatorial positive rules) and the multiplicative tensors don't.

## 4. The small confusions

**Q1 — Is casual "Set" justified (Russell)?** Yes. Fix a **universe** `U` (a set closed under
the operations you use — pairs, powersets, unions, function-sets). Working inside `𝒫(U) + all
functions among its elements` *is* "Set relative to `U`," and you lose nothing for ordinary
category theory. The paradox only bites when you want the collection of *all* sets to itself be an
object; universes handle that by stratifying (Set is not in Set, but is in Set of the next
universe up). So: pick a big-enough `U` and proceed — that's the standard fix, not a fudge.

**Q2 — "Set^op = Bool"?** Not equal, but you're circling a real theorem. The 2-element set `2` is
the **dualizing object**: `Set(−, 2) = 𝒫(−)` (contravariant powerset) is a duality
`Set^op ≃ complete atomic Boolean algebras`. Restricted to finite sets it becomes a
**self-duality** `FinSet^op ≃ FinSet` (finite Boolean algebras are just powersets, ≃ their atom
sets). What surprised you is almost certainly this: finite sets are their own opposite, *mediated
by the Boolean object 2*. That's the grain of truth in "Set^op = Bool."

**Q3 — F_1, isotropic vectors, and the q-Boolean algebra.** First, a clarification that dissolves
half the puzzle: `V ≅ V*` for finite-dimensional `V` needs **no inner product** — a basis (or the
trace pairing) gives it over *any* field, `F_q` included. So the abstract self-duality is fine over
`F_q`; isotropic vectors are a red herring *for `V≅V*`*. Isotropic vectors (nonzero `v` with
`Σv_i²=0`) are extra structure — they belong to a chosen **quadratic form**, i.e. to the
*orthogonal/symplectic* refinement (Dynkin types B/C/D), **not** to the plain subspace lattice.
And the plain subspace lattice of `F_q^n` is exactly the `q`-analogue of the Boolean lattice of
subsets (subspaces `↝` subsets, Gaussian `↝` ordinary binomial as `q→1`) — the **type-A** story,
which uses no form at all. So: the q-deformed Boolean algebra you're after is the subspace lattice
(type A, form-free); isotropic vectors live one level out, in the type-B/C/D story, and do *not*
deform the Boolean algebra — they refine it. (This is the corner where I'm least authoritative;
take it as structural orientation, and I'm happy to compute a small `F_q` example with you.)

## 5. Q5 — where the categorical story stops (the RH line)

Crisp line, and you can hold Neil to it:

- **Categorical / algebraic (what the table gives you):** the *multiplication itself* — Dirichlet
  convolution `(a⋆b)(n) = Σ_{de=n} a_d b_e` as a ring structure, and its structure constants
  (the `g(λ,μ,ν)`). This is the decategorification of a Day lift. Full stop.
- **Analytic (what it does NOT give you):** treating `Σ a_n n^{-s}` as a *function of a complex
  variable*, analytic continuation, growth, and above all the **location of zeros**. That is a
  separate analytic act (a Dirichlet-series / Mellin transform + continuation) that no amount of
  this categorical structure produces or constrains.

So the connection is **purely algebraic**: Dirichlet convolution is the shadow of a categorical
op; the zeros of `ζ` are nowhere in sight. Your PDF's caveat #3 already says exactly this, and
it's right. **Nothing here is a route to RH — don't spend five years looking for one through this
door; there isn't one.**

---

*If it helps for the Neil meeting: the one sentence that ties it to my work is "the hard column is
the non-cartesian/non-extensive tensor, which is the exact boundary MacBeth's container theory is
built around." Happy to go deeper on any cell — especially the Hecke/q one, which is where your
F_1 instinct and my Fam(Vec^op) front actually meet.*
