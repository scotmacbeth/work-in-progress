# ⋉ and ⋊: the two non-convolutional monoidal structures on **Cont** are the Dialectica tensors

**Date:** 2026-07-17
**Author:** MacBeth
**Registry:** `other-cont-monoidal-tensors` (new; sibling of `day-family-classification`); touches
`closed-day-structures` (sub-Q 6.1).
**Source of target:** Dorta–Jarvis–Niu, *Monoidal Structures on Generalized Polynomial Categories*,
arXiv:2305.05655, EPTCS 397 (2023), §6 "Other monoidal structures on polynomials" — an explicit open
problem ("we would like to know if there are interpretations or applications for these").

---

## 0. Problem statement

DJN show that for any monoidal category `(C, e, ·)`, the generalized polynomial category `ΣΠC` carries,
in addition to Day convolution `⊗` and the composition product `◁`, **at least two more** monoidal
structures `⋉`, `⋊` with the same unit `e`. Restricting to `C = 1` gives `ΣΠ1 ≈ Poly ≈ Cont`
(DJN Prop 2.9; `Cont = Fam(Set^op)`). DJN state — and leave open — the question of what `⋉`, `⋊`
*mean*. This note answers that.

**Two independent sub-targets.**

- **(A)** Write `⋉/⋊` in container coordinates; determine their structure (symmetry, associativity),
  place them in the taxonomy relative to the convolutional (Day) family and to `◁`, and **interpret**
  them. *Claim:* `⋉` is de Paiva's **Dialectica tensor** extended from the homogeneous (= dialectica)
  subcategory to all of `Cont`; `⋊` is its **directed / one-sided** variant.
- **(B)** (closure residue, `closed-day-structures` sub-Q 6.1) Does there exist a monoidal `⋆` on `Set`
  with `(−) ⋆ B` non-polynomial for some `B`? Equivalently, is every convolutional tensor on `Cont`
  left-closed?

Convention throughout: a container is `p = (S_p, p[-])` with shape set `S_p` and, at each shape `s`,
a direction (position) set `p[s]`; extension `⟦p⟧X = ∑_{s∈S_p} X^{p[s]}`. I write `y = (1, *↦1)` for
the unit container (`⟦y⟧ = Id`). "Polynomial functor `Set→Set`" and "container" are used
interchangeably (Poly ≃ Cont).

---

## PART A — ⋉ and ⋊

### A.1 Container coordinates (from DJN §6, specialised to C = 1)

DJN §6 give, for general `C`:

```
(∑_i ∏_{a∈A_i} u_{i,a}) ⋉ (∑_j ∏_{b∈B_j} v_{j,b}) := ∑_{i∈I} ∑_{j∈J} ∏_{a:J→A_i} ∏_{b:I→B_j} (u_{i,a_j} · v_{j,b_i})
(∑_i ∏_{a∈A_i} u_{i,a}) ⋊ (∑_j ∏_{b∈B_j} v_{j,b}) := ∑_{i∈I} ∑_{j∈J} ∏_{a:J→A_i} ∏_{b∈B_j}   (u_{i,a_j} · v_{j,b}).
```

Set `C = 1`: every predicate `u_{i,a}, v_{j,b}` is the unique object `y`, the fusion `·` is trivial, and a
homogeneous factor `∏_{a∈A_i} y = y^{A_i}`. A container `p` is `∑_{i∈I} y^{A_i}` with `I = S_p`,
`A_i = p[i]`. The double product `∏_{a:J→A_i}∏_{b:I→B_j} y` is a single representable whose exponent is
the **index set** `A_i^J × B_j^I`. Reading off (with `I = S_p`, `J = S_q`, `A_i = p[s]`, `B_j = q[t]`):

> **Definition A.1 (⋉, ⋊ in container coordinates).**
> `⋉` and `⋊` both have shape set `S_p × S_q`, and
> ```
>   (p ⋉ q)[(s,t)] = p[s]^{S_q} × q[t]^{S_p}          (both factors exponentiated)
>   (p ⋊ q)[(s,t)] = p[s]^{S_q} × q[t]                (only the LEFT factor exponentiated)
> ```
> Unit: `y` (both sides). Contrast the two **convolutional** siblings, whose direction at `(s,t)`
> depends only on the fibres `p[s], q[t]`:
> ```
>   (p ⊗ q)[(s,t)] = p[s] × q[t]        (DJN Day product = Dirichlet tensor; positions, no exponential)
>   (p × q)[(s,t)] = p[s] + q[t]        (categorical product = Day-of-+)
> ```

`X^{S}` denotes the set of functions `S → X`; here `S` ranges over a **global shape set** of the *other*
container. That single feature — an exponential indexed by the opposite shape set — is the whole story:
it is what pushes `⋉/⋊` outside the Day family (§A.3) and it is the Dialectica hallmark (§A.4).

There is an obvious mirror of `⋊`, namely `(p ⋊' q)[(s,t)] = p[s] × q[t]^{S_p}` (right factor
exponentiated); it equals `⋊` with arguments transposed, and since `⋊` is not symmetric (§A.2) it is a
genuinely distinct-looking, isomorphic operation `⋊' ≅ (⋊)^{sw}`.

### A.2 They are monoidal; ⋉ is symmetric, ⋊ is directed

DJN assert `(ΣΠC, e, ⋉)` and `(ΣΠC, e, ⋊)` are monoidal. I re-derive the `C=1` case directly and, in
doing so, expose closed forms that make the symmetry/asymmetry visible.

**Unit laws.** `y` has one shape `∗`, one direction. For `⋉`: `(p ⋉ y)[(s,∗)] = p[s]^{1} × 1^{S_p} = p[s]`,
so `p ⋉ y ≅ p`; and `(y ⋉ q)[(∗,t)] = 1^{S_q} × q[t]^{1} = q[t]`, so `y ⋉ q ≅ q`. Same for `⋊`
(`(p⋊y)[(s,∗)] = p[s]^1 × 1 = p[s]`, `(y⋊q)[(∗,t)] = 1^{S_q} × q[t] = q[t]`). ✓ (verified computationally).

**Associativity, via the n-fold closed form.** Composing `⋉` (`k` times) gives shape set
`S_{p_1} × ⋯ × S_{p_k}` and, at a tuple of shapes `(s_1,…,s_k)`,

> **Lemma A.2 (n-fold ⋉).**
> `(p_1 ⋉ ⋯ ⋉ p_k)[(s_1,…,s_k)] ≅ ∏_{f=1}^{k} p_f[s_f]^{ (∏_{g≠f} S_{p_g}) }.`

Each factor `p_f`'s fibre is exponentiated by the product of **all the other** shape sets. This
expression is manifestly invariant under any reassociation of the `⋉`'s and under any **permutation** of
the factors, so `⋉` is associative *and symmetric*. (Proof: induction using the exponential laws
`(X×Y)^S ≅ X^S × Y^S` and `X^{S×T} ≅ (X^S)^T`; the base case is Def. A.1. The bracketing `(p⋉q)⋉r`
gives `p[s]^{S_q S_r} q[t]^{S_p S_r} r[u]^{S_p S_q}` and so does `p⋉(q⋉r)` — verified below.)

> **Lemma A.3 (n-fold ⋊).**
> `(p_1 ⋊ ⋯ ⋊ p_k)[(s_1,…,s_k)] ≅ ∏_{f=1}^{k} p_f[s_f]^{ (∏_{g>f} S_{p_g}) }.`

Now each factor is exponentiated only by the shape sets of the factors **to its right** — a *triangular*
exponent pattern. This is associative (the product over `g>f` is unambiguous) but **not** symmetric: the
factor order matters. This is the precise sense in which `⋊` is *directed*: reading the factors left to
right, the challenge to factor `f` sees the positions chosen by all *later* factors, but not the earlier
ones — a strict, one-directional dependency. (`⋉` is the symmetric closure: every factor sees every
other.)

Computational verification (`scratch/ltimes_check.py`): unit laws ✓ (both); associativity ✓ (both,
cardinality profiles of `(p⋉q)⋉r` vs `p⋉(q⋉r)` and the `⋊` analogue agree on explicit small
containers); `⋉` symmetric ✓; `⋊` **not** symmetric ✓.

### A.3 Taxonomy: non-convolutional, non-cocontinuous, non-closed

**(i) Not convolutional / not pointwise.** Call a binary functor `⊙: Cont×Cont→Cont` *convolutional*
(pointwise) if there is a functor `F: Set×Set→Set` with `S_{p⊙q} = S_p×S_q` and
`(p⊙q)[(s,t)] = F(p[s], q[t])` — the direction is a function of the two *fibres alone*. Every Day tensor
is of this form (Theorem A, `2026-07-14-day-family-classification.md`), with `F = ⋆`.

`⋉` is **not** convolutional. Take `p = y²` (`S_p = 1`, `p[∗] = 2`) and `q_n` with `S_{q_n} = n`, every
fibre `= 2`. Then `(p ⋉ q_n)[(∗,t)] = 2^{n} × 2^{1} = 2^{n+1}`. The fibre `p[∗]=2` and the fibre `q_n[t]=2`
are fixed, yet the resulting direction grows with `n = |S_{q_n}|`. A convolutional `F(2,2)` would be
constant. Hence no such `F` exists. The same computation kills `⋊`. **This is exactly why Theorem A does
not reach them:** Thm A classifies the convolutional tensors as Day convolutions of monoidal `(Set,⋆)`;
`⋉/⋊` sit outside its domain, so "the Day family does not exhaust the monoidal structures on Cont."

**(ii) Not cocontinuous; no distribution over `+`.** `(−) ⋉ q` does **not** preserve coproducts:
```
((p + p') ⋉ q)[(s,t)]  =  (p+p')[s]^{S_q} × q[t]^{S_p + S_p'}   (shape set of p+p' is S_p + S_p')
((p ⋉ q) + (p' ⋉ q))[(s,t)]  has direction  p[s]^{S_q} × q[t]^{S_p}   at the p-summand.
```
The exponents `q[t]^{S_p+S_p'} = q[t]^{S_p} × q[t]^{S_p'}` and `q[t]^{S_p}` differ. Computationally the
direction profiles are `[8,8,32,32,32,32]` vs `[8,8,16,16,16,16]` — genuinely unequal. So **⋉ does not
distribute over `+`**, whereas the Day `⊗` does (verified). The obstruction is the exponent's dependence
on the *entire* shape set `S_p`, which a coproduct enlarges.

**(iii) Not closed.** Cocontinuity of `(−) ⊙ q` in the left variable is necessary for a right adjoint
(internal hom). Since `(−) ⋉ q` and `(−) ⋊ q` fail to preserve coproducts (ii), **neither `⋉` nor `⋊`
is left-closed** — indeed `(−)⋉q` is not a left adjoint at all. This is a sharp contrast with the other
Cont tensors: `×` is cartesian-closed (Altenkirch–Levy–Staton), `⊗` is closed (Niu–Spivak Ex 4.78), `◁`
has a right coclosure (Meyers / Niu–Spivak Prop 6.57). **`⋉/⋊` are the first non-closed monoidal
structures in the Cont story** — and they are non-convolutional, so they do not bear on the *closure of
convolutional* tensors (Part B).

Summary placement:

| tensor | shapes | direction at `(s,t)` | convolutional? | distributes `/+` | closed | symmetric |
|---|---|---|---|---|---|---|
| `+` | `S_p+S_q` | — | (colimit) | — | — | ✓ |
| `×` | `S_p×S_q` | `p[s]+q[t]` | ✓ (Day of `+`) | ✓ | ✓ (CCC) | ✓ |
| `⊗` | `S_p×S_q` | `p[s]×q[t]` | ✓ (Day of `×`) | ✓ | ✓ | ✓ |
| `◁` | `∑_{S_p} q^{S_q}`… | (composition) | ✗ | left only | coclosed | ✗ |
| **`⋉`** | `S_p×S_q` | `p[s]^{S_q}×q[t]^{S_p}` | **✗** | **✗** | **✗** | **✓** |
| **`⋊`** | `S_p×S_q` | `p[s]^{S_q}×q[t]` | **✗** | **✗** | **✗** | **✗ (directed)** |

### A.4 Interpretation — the Dialectica tensors (the answer to DJN's open question)

**The dialectica subcategory.** DJN Prop 2.13: the *homogeneous* polynomials in `ΣΠ2` (those
`∑_{i∈I}∏_{a∈A} c_{i,a}` with the direction set `A` **independent of `i`**) form a full subcategory
`Hmg(2) ≃ Dial(Set)`, de Paiva's original dialectica category. Under the dictionary an object
`∑_{i∈I}∏_{a∈A} c_{i,a}` is de Paiva's `(U, X, α)` with `U = I` (positions), `X = A` (directions), and
`α = c: I×A → 2` (the relation). A morphism carries a forward `ϕ: I→J` and a backward `ϕ^♯: I×B → A`
(DJN Ex 2.12) — exactly de Paiva's `(f: U→V, F: U×Y→X)`. So **positions = `U`, directions = `X`.**

**de Paiva's tensor.** The symmetric monoidal (linear-logic) tensor on `Dial(Set)` is
```
   (U,X,α) ⊗_Dial (V,Y,β) = ( U×V ,  X^V × Y^U ,  α⊗β ),
```
with `(α⊗β)((u,v),(f,g)) = α(u,f v) ∧ β(v,g u)`, for `f:V→X`, `g:U→Y`. The witness (backward)
object `X^V × Y^U` is the defining feature of the Gödel–de Paiva functional interpretation: to respond
to a challenge against a conjunction `A⊗B` you must supply, for each of the opponent's moves in one
component, a strategy in the *other* — hence the mutual function spaces.

**The identification.** Take homogeneous containers `p` (fibre `A = p[s]` constant, shape set `I = S_p`)
and `q` (fibre `B = q[t]` constant, shape set `J = S_q`). Then Def. A.1 gives
```
   (p ⋉ q)[(s,t)] = p[s]^{S_q} × q[t]^{S_p} = A^{J} × B^{I} = X^{V} × Y^{U}.
```
This is **exactly `⊗_Dial`.** (`⋉` also carries the right forward part: shapes `S_p×S_q = U×V`.
Verified computationally: `X^V·Y^U = 36 = A^{|S_q|}·B^{|S_p|}`.) Meanwhile DJN's Day `⊗` restricts on
`Hmg(2)` to direction `A×B = X×Y` (a *pair* of challenges, one to each factor, presented together) —
this is the naive **Gödel-interpretation conjunction** `A∧B`, whose Dialectica challenge is the product
`X×Y`. It is *neither* de Paiva's linear tensor `⊗` (`X^V×Y^U`) *nor* the categorical product `&`
(challenge `X+Y`, forced by contravariance in the challenge variable). So the two Cont tensors split the
two conjunctions of the Dialectica interpretation cleanly:

> **Theorem A.4 (interpretation of ⋉).** `⋉` restricts on the homogeneous subcategory
> `Hmg(2) ≃ Dial(Set)` to **de Paiva's Dialectica tensor `⊗_Dial`**. Equivalently: `⋉` is the
> polynomial-functor incarnation of the multiplicative conjunction of Gödel's Dialectica interpretation,
> extended from the dialectica subcategory to all of `Poly ≈ Cont`. The linear-logic (multiplicative)
> content of `Dial(Set)` lives in `⋉`; the Day tensor `⊗` restricts to the *Gödel conjunction* `∧`
> (challenge `X×Y`) — the non-linear conjunction.

> **Theorem A.5 (interpretation of ⋊).** `⋊` is the **directed / sequential Dialectica tensor**: by
> Lemma A.3 each factor's challenge (backward part) is functionalised only over the positions of the
> factors *to its right*, so the dependency is strictly one-directional. In the game reading of `Dial`,
> `⋉` is the conjunction where both players respond adaptively to the other's move; `⋊` is the
> conjunction where the dependency flows one way only — one problem is answered adaptively in response to
> the other, which is played blind. (`⋊` mirror `⋊'` reverses the direction.)

This **answers DJN's stated open problem** ("interpretations or applications for these"): `⋉` and `⋊`
are the Dialectica multiplicative conjunction and its directed variant, hiding in plain sight in `Poly`
because de Paiva's dialectica lives on the *homogeneous slice* and `⋉/⋊` are precisely the extensions of
that structure off the slice. Applications inherit from the Dialectica program: models of intuitionistic
linear logic, proof-relevant relational composition, Petri-net / Dialectica dynamics (Di Lavore–Leal–de
Paiva); `⋊`'s directedness is a natural home for *sequential* / *causal* compositional bounds
(cf. DJN's own "compositional bounds on dynamical systems" motivation for `◁`).

### A.5 Novelty audit (mandatory — high scoop risk)

**What is certainly known / not mine:**
- `Dial(Set) ≃ Hmg(2)` and the polynomials↔dialectica relationship: DJN Prop 2.13, and DJN's whole
  framing ("renewed interest… de Paiva's dialectica categories and their relationship to polynomial
  functors"). Also already in my own memory ([[dorta-jarvis-niu-neighbour]], line "ΣΠ2 = Dial(Set)").
- de Paiva's tensor formula `X^V × Y^U`: textbook (de Paiva 1989, *The Dialectica categories*).
- The `⋉/⋊` operations themselves: DJN §6.

**What is the candidate delta (this note):** the specific identification "`⋉ = ⊗_Dial` extended to all
of `Poly`, `⋊ =` its directed variant," the symmetric/triangular closed forms (Lemmas A.2/A.3) exposing
the directedness, and the taxonomy placement (non-convolutional / non-cocontinuous / non-closed;
`⋉/⋊` outside Theorem A).

**Honesty on the identification vs. its novelty.** The *mathematical* identification is essentially a
matching of definitions (DJN Prop 2.13 + Def. A.1 + de Paiva's tensor) — it is **proved**, not
conjectural, at the level of the formulas. The *novelty* I **cannot fully clear offline** (this is a
no-browsing deep-work session): I have not checked 2023–2026 work of de Paiva, Trotta, Spivak, Hedges,
Capucci for a statement of the extension. Two facts bound the risk:
- **DJN themselves did not make it** — they pose `⋉/⋊` as an *open* interpretation question, despite
  knowing `Dial(Set)≃Hmg(2)` intimately. Whoever would most naturally state "these are the Dialectica
  tensors" left it open.
- The extension lives off the homogeneous slice, which is *DJN's* generalisation (`ΣΠ`), not classical
  dialectica territory; de Paiva's own work stays on the dialectica category proper.

**Grade:** identification `proved`; **novelty `speculative` pending a live arXiv check** (owed next
browse: de Paiva / Trotta / Spivak / Hedges 2023–2026 "dialectica polynomial functors"; DJN §5 in full;
Niu–Spivak *Poly* book Ch 3–4 for any function-space tensor). If found → cite; the delta becomes the
Cont-language closed forms + directedness of `⋊` + interaction placement. If clear → a genuine
cross-domain identification. **Do not publish the novelty claim before the check.**

### A.6 Interaction with `◁` and `⊗` (two new rows/columns — partial)

The full `6×6` interaction table (extending Hedges' `4×4`, `hedges-interchange-table` [proved]) needs a
row/column for each of `⋉`, `⋊`. Established here:

- **`⋉/⋊` vs `+`:** no distributive law in the exponentiated variable (§A.3(ii)); a lax comparison
  `(p⋉q)+(p'⋉q) → (p+p')⋉q` exists (there is a natural inclusion `q[t]^{S_p} ↪ q[t]^{S_p+S_p'}` picking
  the `S_p`-restriction — direction *maps go backwards*, so the container morphism goes forwards), giving
  a **lax** (one-directional, non-iso) interchange. Direction of the cell: `+ ⊳ ⋉` lax, never strict.
- **`⋉` vs `⊗`:** both have shapes `S_p×S_q`; a duoidal-type law `(a⊗b)⋉(c⊗d) → (a⋉c)⊗(b⋉d)` would need
  a natural map on directions `(a⋉c)[..]×(b⋉d)[..] → ((a⊗b)⋉(c⊗d))[..]`, i.e.
  `a[·]^{S_c}c[·]^{S_a} × b[·]^{S_d}d[·]^{S_b} → (a[·]b[·])^{S_c×S_d}(c[·]d[·])^{S_a×S_b}` — the target
  exponents `S_c×S_d, S_a×S_b` dominate the source `S_c,S_a,…`, so a canonical map exists only via
  diagonal/restriction and is **not** iso. *Status: candidate lax duoidal law; coherence unchecked —
  GAP.*
- **`⋉` vs `◁`:** DJN's own future-work asks to generalise Spivak's `◁`-over-`⊗` duoidality; the
  `⋉`-analogue is untouched here. *Status: OPEN.*

I record these honestly as partially-computed. The solid new content is the two direction *columns*
(non-distribution, laxness) rather than a completed table.

---

## PART B — closure-vacuity residue (self-contained)

**Sub-Q 6.1.** Does there exist a monoidal `(Set, ⋆, e)` with `(−) ⋆ B` **non-polynomial** for some set
`B`? (Equivalently, by `closed-day-structures` [proved]: is some convolutional tensor on `Cont`
*not* left-closed? YES → a clean non-closed convolutional example; NO → every convolutional tensor is
left-closed.)

Recall `(−)⋆B` polynomial ⟺ it preserves connected limits ⟺ it preserves wide pullbacks
(Gambino–Kock / familial representability on `Set`).

**Reduction (proved).** *Non-polynomial requires non-cocontinuity.* Every **cocontinuous**
(colimit-preserving) endofunctor of `Set` is a monomial: `F(X) = F(∐_X 1) = ∐_X F(1) = X × F(1)`, which
is polynomial (`= F(1)·y`) and preserves connected limits. Hence:
```
   (−)⋆B non-polynomial   ⟹   (−)⋆B not cocontinuous.
```
So any witness `⋆` must fail cocontinuity in the relevant variable.

**Non-cocontinuity is necessary but not sufficient.** The coproduct `+` is a monoidal structure on `Set`
(unit `∅`), and `(−)+B` is **not** cocontinuous — `(X+X')+B ≇ (X+B)+(X'+B)` (verified: `9 ≠ 11`) — yet
`(−)+B = y+B` **is** polynomial (shapes `1+B`: one shape with one direction, `B` shapes with none). So the
gap between "non-cocontinuous" and "non-polynomial" is real; a witness must be *strictly more exotic*
than `+`.

**Standard structures all give polynomial (indeed closed) `(−)⋆B`.**
- `×`: `(−)×B` is a right adjoint, polynomial (`= y^B`… rather `B·y`? — `X×B` is the monomial `B·y`),
  closed. ✓
- `+`: `(−)+B = y+B` polynomial (non-closed, since not cocontinuous — consistent with
  `closed-day-structures`: `+` induces `×` on Cont which *is* CCC, no contradiction: the *induced*
  Cont-tensor of `⋆` is closed iff `(−)⋆B` polynomial, and `y+B` is polynomial). ✓
- `∨_S` (Day-of-…): the members catalogued in Thm A/B⁺/C all have polynomial `(−)⋆B`. ✓

**Resolution status: reduced, conjectured, not settled.** The question is now sharp:

> **Open (sub-Q 6.1, reduced).** Is there a monoidal `(Set,⋆,e)` with some `(−)⋆B` failing to preserve
> wide pullbacks? Such `⋆` must be (a) non-cocontinuous in that variable, and (b) strictly beyond the
> `+`-type "polynomial-but-non-cocontinuous" band — i.e. `(−)⋆B` must be a genuinely non-polynomial
> endofunctor (symmetric-square-like, powerset-like) that nonetheless sits inside an associative, unital
> `⋆`.

**Conjecture (mine, `speculative`): NO** — every monoidal structure on `Set` has `(−)⋆B` polynomial in
each variable, hence **every convolutional tensor on `Cont` is left-closed**, a structural completion of
Theorem A. *Evidence:* the associativity constraint `L_B ∘ L_C ≅ L_{C⋆B}` makes `{L_B := (−)⋆B}` a
composition-closed family of endofunctors of `Set`; polynomials are closed under composition, and no
non-polynomial endofunctor is known to arise as one leg of an associative, unital `⋆` on `Set`; `Set` is
known to carry very few monoidal structures (all the standard ones are polynomial-in-each-variable).
*I could not construct a non-polynomial witness, nor prove the classification offline.* This is a clean,
sharply-stated GAP — and nothing in Part A depends on it.

---

## Verification (computational)

`scratch/ltimes_check.py` (explicit finite containers):
- Unit laws `p⋉y ≅ p ≅ y⋉p`, `p⋊y ≅ p ≅ y⋊p`: ✓.
- Associativity of `⋉` and `⋊` (direction profiles agree): ✓.
- `⋉` symmetric, `⋊` **not** symmetric: ✓ / ✓.
- `⋉` does **not** distribute over `+` (`[8,8,32,32,32,32]` vs `[8,8,16,16,16,16]`); Day `⊗` does: ✓.
- Dialectica witness `X^V×Y^U = 36 = p[s]^{|S_q|}·q[t]^{|S_p|}` on homogeneous inputs: ✓.
- Target B: `(−)+B` non-cocontinuous (`9 ≠ 11`) yet `y+B` polynomial: ✓.

All computations are cardinality/profile checks that confirm the *closed-form direction formulas*; the
isomorphisms themselves are the canonical exponential-law isos used in Lemmas A.2/A.3 (natural, not
merely bijective on cardinalities).

## Gaps (precisely stated)

1. **Novelty of the Dialectica identification** — the identification is proved; whether it is *new*
   is unresolved because this was a no-browse session. Live arXiv check owed (§A.5).
2. **Interaction table** — the `⋉/⋊` rows against `⊗` and `◁` are only partially computed: a candidate
   lax duoidal `⋉`-over-`⊗` law is identified but its coherence is unchecked; `⋉`-vs-`◁` is untouched
   (§A.6).
3. **Target B** — reduced to a sharp question and conjectured NO, but neither a non-polynomial witness
   nor the "no monoidal `⋆` on Set has non-polynomial `(−)⋆B`" classification is established (Part B).

## What this delivers

- `⋉/⋊` in clean container coordinates + elegant `n`-fold closed forms exposing `⋉` symmetric, `⋊`
  directed (Lemmas A.2/A.3) — **the directedness of `⋊` is, I believe, not previously articulated.**
- A crisp taxonomy placement: **the four canonical tensors + the Day family do not exhaust the monoidal
  structures on Cont**; `⋉/⋊` are non-convolutional, non-cocontinuous, non-closed — the first non-closed
  monoidal structures on Cont.
- An **interpretation answering DJN's open problem**: `⋉` = de Paiva's Dialectica tensor extended to
  Poly; `⋊` = its directed variant. A candidate cross-domain isomorphism (Poly ↔ Dialectica), pending
  a novelty check.
- Part B: the closure residue reduced to a sharp, self-contained open question with the standard cases
  disposed of.
