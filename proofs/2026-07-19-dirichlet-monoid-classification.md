# Bare ⊗-monoids in Poly are exactly a *monoid on shapes plus an oplax monoidal functor on fibres*

**MacBeth — 2026-07-19 (PROVE deep-work session; promotes `dirichlet-monoid-classification` computed → proved)**

> **Headline.** A monoid `(c, μ:c⊗c→c, η:y→c)` for the **Dirichlet (parallel) tensor**
> `(Cont, ⊗, y)` — with *no* `◁`/directed structure imposed — is **exactly** the data of
> 1. a **monoid** `(·, e)` on the shape set `S = c(1)`, together with
> 2. an **oplax monoidal functor** `P : (S,·,e) → (Set,×,1)` on the fibres, sending
>    `s ↦ P_s := c[s]` — i.e. structure maps `φ_{s,t} : c[s·t] → c[s] × c[t]` and a counit
>    `ε : c[e] → 1` (forced: the unique map), satisfying the oplax associativity coherence and the
>    two oplax unit coherences.
>
> This is the exact **dual** of the (proved) ⊗-**comonoid** classification
> `2026-07-17-bare-dirichlet-comonoid.md` (= *families of monoids*). The comonoid forces the shape
> comultiplication to the **diagonal** (trivial) and puts a **monoid** on each fibre; the monoid lets
> the shapes carry an arbitrary **monoid** and puts an **oplax functor** on the fibres. The asymmetry
> is structural, not accidental — see §5.
>
> Categorically: `Mon(Cont, ⊗, y) ≅ ∫_{(S,·,e) ∈ Mon} OplaxMon((S,·,e), (Set,×))`.
> This answers the **Poly/⊗-monoid slice** of the notion Niu–Spivak flag as *future work* in **Remark
> 3.78** (the dual of their Chapter 9, Question 5): ⊗-monoids in Poly, previously uncharacterised.
>
> **Secondary (proved).** The **`×`-monoid** refinement: a monoid for the *categorical product* tensor
> `(Cont, ×, 1)` is exactly a monoid `(S,·,e)` whose **identity fibre `c[e]` is empty**, together with
> an oplax monoidal functor `P : (S,·,e) → (Set, ⊔, ∅)` on fibres (backward routing
> `ψ_{s,t} : c[s·t] → c[s] ⊔ c[t]`). Same theorem, with the fibre target `(Set,×,1)` replaced by
> `(Set,⊔,∅)` — because the product tensor combines fibres by **disjoint union**, and its unit `1` has
> **empty** fibre. Generic containers admit **no** `×`-monoid (the empty-identity-fibre obstruction);
> when all fibres are empty, `×`-monoids `=` monoids on `S`.

---

## 1. Setup and conventions

A **container / polynomial functor** is `c = Σ_{s ∈ S} y^{c[s]}`: a set of **shapes** `S = c(1)` and
for each `s` a set of **directions/positions** `c[s]`; write `P_s := c[s]`. A **Poly morphism**
`f : p → q` is a *forward* map on shapes `f₁ : S_p → S_q` with, for each `s`, a *backward* map on
directions `f♯_s : q[f₁ s] → p[s]`. Composition of `p --f--> q --g--> r` is `(gf)₁ = g₁∘f₁` and
`(gf)♯_s = f♯_s ∘ g♯_{f₁ s}` (backward maps compose contravariantly). This is `Cont ≅ Fam(Set^op)`
(Spivak–Garner–Fairbanks Prop. 3.6; my `2026-07-14-day-family-classification.md` Lemma 1.2).

**Dirichlet tensor `⊗ = Day(Set, ×, 1)`** (Niu–Spivak arXiv:2312.00990 Prop. 3.79, deep-read):
```
    (p ⊗ q) = Σ_{(s,t) ∈ S_p × S_q} y^{p[s] × q[t]},        unit  y = y^1.
```
For morphisms `f : p→p'`, `g : q→q'`: `(f⊗g)₁(s,t) = (f₁ s, g₁ t)` and
`(f⊗g)♯_{(s,t)} = f♯_s × g♯_t : p'[f₁ s]×q'[g₁ t] → p[s]×q[t]`. The tensor is symmetric; its
associator `α_{p,q,r}` has shape map `((s,t),u)↦(s,(t,u))` and backward map `(x,(y,z))↦((x,y),z)`,
strict on the nose modulo re-bracketing.

**Definition.** A **⊗-monoid** is `(c, μ, η)` with `μ : c⊗c → c`, `η : y → c` Poly morphisms
satisfying unitality `μ∘(η⊗id) = λ`, `μ∘(id⊗η) = ρ` and associativity
`μ∘(μ⊗id) = μ∘(id⊗μ)∘α` (with `λ, ρ` the unitors of `⊗`). **No `◁` structure is assumed.** This is
the exact dual of the ⊗-comonoid of `2026-07-17-bare-dirichlet-comonoid.md`.

---

## 2. Unpacking the data

Write the two morphisms in coordinates.

**Unit `η : y → c`.** The shape map `S_y = {∗} → S` picks a shape `η₁(∗) =: e ∈ S`. The backward map
at `∗` is a map `η♯ : c[e] → y[∗] = 1`, i.e. **the unique map `ε : c[e] → 1`** (forced — `1` is
terminal). So the unit datum is a *choice of shape* `e`; there is no further position content, but the
unit **laws** will constrain the fibres through `ε`.

**Multiplication `μ : c⊗c → c`.** The shape map is a binary operation
```
    μ₁ : S × S → S,    write   s · t := μ₁(s,t).
```
The backward map at `(s,t)` is
```
    φ_{s,t} := μ♯_{(s,t)} : c[s·t] → (c⊗c)[(s,t)] = c[s] × c[t].
```
Write its two components `φ_{s,t}(x) = (φ¹_{s,t}(x), φ²_{s,t}(x))`, with `φ¹_{s,t}(x)∈c[s]`,
`φ²_{s,t}(x)∈c[t]`, for `x ∈ c[s·t]`.

So a ⊗-monoid is exactly the data `(· : S×S→S, e ∈ S, {φ_{s,t}}_{s,t∈S})`. The three monoid laws pin
this down, split into a **shape part** (forward) and a **fibre part** (backward), as follows.

---

## 3. The unit laws: `e` is a two-sided unit on shapes; `φ` is identity-on-the-unit-side on fibres

Compute `μ∘(η⊗id) : y⊗c → c` and demand it equal the left unitor `λ : y⊗c ≅ c`.

*Shapes.* `(∗,s) ↦ (e, s) ↦ e·s`. The unitor `λ` has shape map `(∗,s)↦s`. Equality forces
**`e·s = s`** for all `s`.

*Fibres.* At shape `(∗,s)`, `λ♯` sends `p ∈ c[s] = c[e·s]` to `(0,p) ∈ y[∗]×c[s]` (the canonical
`c[s] ≅ 1×c[s]`). The composite `μ∘(η⊗id)` sends `p` first through `μ♯_{(e,s)} = φ_{e,s}` to
`(a, p') ∈ c[e]×c[s]`, then through `(η⊗id)♯ = ε × id` — which collapses the `c[e]` component to the
point `0` and keeps the second — giving `(0, φ²_{e,s}(p))`. Demanding `= (0,p)`:
```
    φ²_{e,s} = id_{c[s]}          (the c[t]-side of φ_{e,s} is the identity).
```
Symmetrically `μ∘(id⊗η) = ρ` forces **`s·e = s`** and **`φ¹_{s,e} = id_{c[s]}`**.

> These are precisely the two **oplax unit coherences** of an oplax monoidal functor into `(Set,×,1)`:
> since the source `(S,·,e)` is the *discrete* monoidal category of the monoid `S` (only identity
> morphisms, so `F` of every structure isomorphism is an identity), the coherence
> `λ'_{P_s}∘(ε×id)∘φ_{e,s} = P(λ_s) = id` reads exactly `φ²_{e,s}=id`, and dually
> `ρ'_{P_s}∘(id×ε)∘φ_{s,e} = id` reads `φ¹_{s,e}=id`.

---

## 4. Associativity: `·` is associative on shapes; `φ` satisfies the oplax hexagon on fibres

Both sides of `μ∘(μ⊗id) = μ∘(id⊗μ)∘α` are morphisms `(c⊗c)⊗c → c`. Source shape `((s,t),u)`; source
positions at `((s,t),u)` are `(c[s]×c[t])×c[u]`.

*Shapes.* LHS: `((s,t),u) ↦ (s·t, u) ↦ (s·t)·u`. RHS: `((s,t),u) ↦_α (s,(t,u)) ↦ (s, t·u) ↦
s·(t·u)`. Equality forces **`(s·t)·u = s·(t·u)`** — `·` is associative.

*Fibres.* Fix `r ∈ c[(s·t)·u] = c[s·(t·u)]`. Trace both backward maps into `c[s]×c[t]×c[u]`
(backward maps compose contravariantly, so we apply the *outer* `μ♯` first).

- **LHS `μ∘(μ⊗id)`.** Outer `μ♯` is `φ_{s·t, u}`: `r ↦ (w, z)` with `w ∈ c[s·t]`, `z ∈ c[u]`. Then
  `(μ⊗id)♯ = φ_{s,t} × id`: `(w,z) ↦ (φ_{s,t}(w), z)`. Result
  ```
     LHS♯(r) = ( φ¹_{s,t}(w), φ²_{s,t}(w), z ),   (w,z) = φ_{s·t,u}(r).
  ```
  i.e. `LHS♯ = (φ_{s,t} × id_{c[u]}) ∘ φ_{s·t,u}`.

- **RHS `μ∘(id⊗μ)∘α`.** Outer `μ♯` is `φ_{s, t·u}`: `r ↦ (p, w')` with `p∈c[s]`, `w'∈c[t·u]`. Then
  `(id⊗μ)♯ = id × φ_{t,u}`: `(p,w') ↦ (p, φ_{t,u}(w'))`. Then `α♯`: `(p,(q,w)) ↦ ((p,q),w)`,
  re-bracketing only. Result
  ```
     RHS♯(r) = ( p, φ¹_{t,u}(w'), φ²_{t,u}(w') ),   (p,w') = φ_{s,t·u}(r).
  ```
  i.e. `RHS♯ = (id_{c[s]} × φ_{t,u}) ∘ φ_{s,t·u}`.

Equating `LHS♯ = RHS♯` on `c[s·t·u]` for all `s,t,u` is exactly
```
    (φ_{s,t} × id) ∘ φ_{s·t,u}  =  (id × φ_{t,u}) ∘ φ_{s,t·u}
                          : c[s·t·u] ⟶ c[s] × c[t] × c[u],
```
componentwise the three equations
```
   φ¹_{s,t}∘φ¹_{s·t,u} = φ¹_{s,t·u},
   φ²_{s,t}∘φ¹_{s·t,u} = φ¹_{t,u}∘φ²_{s,t·u},
   φ²_{s·t,u}          = φ²_{t,u}∘φ²_{s,t·u}.
```

> This is precisely the **oplax associativity coherence** of `P : (S,·,e)→(Set,×,1)` (with the strict
> associator of `×` in `Set`). There is **no cross-shape condition beyond this** (a Poly morphism is a
> shape map plus an *independent* family of backward maps), and **no cocommutativity/commutativity** is
> forced (symmetry of `⊗` makes ⊗-monoids a symmetric-monoidal notion, but a monoid need not be
> commutative).

---

## 5. Theorem, converse, and the structural duality

**Theorem A (⊗-monoids).** For a container `c = Σ_{s∈S} y^{c[s]}`, the following data are in natural
bijection:

1. ⊗-monoid structures `(μ, η)` on `c` in `(Cont, ⊗, y)`;
2. a monoid `(·, e)` on the shape set `S`, together with an oplax monoidal functor
   `P : (S,·,e) → (Set,×,1)`, `s ↦ c[s]`, with structure maps `φ_{s,t}:c[s·t]→c[s]×c[t]` and counit
   `ε:c[e]→1` (the unique map), satisfying the associativity coherence (§4) and the two unit
   coherences (§3).

The correspondence: `μ₁ = ·`, `μ♯_{(s,t)} = φ_{s,t}`, `η₁(∗) = e`, `η♯ = ε`.

**Proof.** §§3–4 show (1) ⟹ (2): the shape parts of the unit and associativity laws say `(S,·,e)` is a
monoid, and the fibre parts say `{φ_{s,t}, ε}` are exactly an oplax monoidal functor. For the converse
(2) ⟹ (1), read §§3–4 backwards: given a monoid `(S,·,e)` and an oplax functor `P`, *define* `μ` by
`(·, φ)` and `η` by `(e, ε)`; the same coordinate identities — now read as hypotheses — give the three
monoid laws, and `ε` is automatically the unique map to `1` so the unit datum is well-defined. The two
passages are mutually inverse on the nose, so the bijection is natural. ∎

**Converse, spelled out.** The only thing to check in (2)⟹(1) beyond the reversed computation is that
*every* choice of monoid `(S,·,e)` and oplax `P` yields a *well-formed* pair of Poly morphisms — it
does: `μ₁ = ·` is a function `S×S→S`, each `φ_{s,t}` is a function `c[s·t]→c[s]×c[t]`, `η₁(∗)=e`, and
`η♯=ε` is the forced map `c[e]→1`. No positivity/nonemptiness side-condition arises (unlike the `×`
case in §6).

**Categorical form.** A morphism of ⊗-monoids `h : c → d` is a Poly morphism commuting with `μ, η`.
Unwinding (Appendix): a forward shape map `h₁ : S_c → S_d` that is a **monoid homomorphism**
`(S_c,·)→(S_d,·)`, together with, for each `s`, a backward map `h♯_s : d[h₁ s] → c[s]` intertwining the
oplax structure maps `φ^d` and `φ^c` along `h₁` (a monoidal transformation of the fibre functors). So
`Mon(Cont,⊗,y)` is a **Grothendieck-type category** over `Mon`: objects `= (monoid on S) + (oplax
functor on fibres)`, morphisms `= (monoid hom) + (fibrewise intertwiner)`. This is the *lax/oplax dual*
of `Comon(Cont,⊗,y) ≅ Fam(Mon^op)`. (I state this at the level of the object bijection, which §§3–4
prove, plus the explicit morphism conditions of the Appendix; the precise variance decoration of the
`∫` — the fibre functor `Mon^op → Cat`, `(S,·,e) ↦ OplaxMon((S,·,e),(Set,×))`, and on which side the
backward `h♯` lands — I have checked on the morphism level but do not assert as a polished
equivalence-of-categories statement here.)

**Why the asymmetry (comonoid ↔ monoid).** The two live over the *same* tensor `⊗ = Day(×)`. The
difference is the direction of the shape map:
- **Comultiplication** `δ : c → c⊗c` has forward shape map `S → S×S`; the **counit** forces it to the
  **diagonal** — `×` is *cartesian* in `Set`, so its Day image admits only the diagonal comultiplication
  on shapes. The remaining content is a *covariant* fibre operation `c[s]×c[s]→c[s]` = a **monoid**.
- **Multiplication** `μ : c⊗c → c` has forward shape map `S×S → S`; this is **unconstrained beyond
  being a monoid**. The remaining content is the *contravariant* fibre operation `c[s·t]→c[s]×c[t]` =
  an **oplax** structure.

So the very same "shapes carry the unique cartesian (co)monoid" phenomenon that *trivialises* the
comonoid's shape layer (forcing the diagonal) *liberates* the monoid's shape layer (any monoid on `S`)
— because comultiplication maps *into* the cartesian product of shapes, multiplication maps *out* of
it. This is the honest reason the dual is **not** a mirror image: comonoid `=` family-of-monoids
(shape trivial), monoid `=` monoid-on-shapes-plus-oplax (shape non-trivial).

---

## 6. Theorem B — the `×`-monoid refinement (secondary)

The **categorical product** tensor on `Cont` is `(c × d) = Σ_{(s,t)} y^{c[s] ⊔ d[t]}` with unit the
terminal container `1 = y^∅` (one shape, *empty* fibre). Repeating §§2–4 with `×` in place of `⊗`
changes exactly two things: the fibre combiner `× → ⊔` and the unit fibre `1 → ∅`.

- **Unit `η : 1 → c`.** Shape map picks `e ∈ S`; the backward map is `η♯ : c[e] → 1[∗] = ∅`. **Such a
  map exists iff `c[e] = ∅`.** So a `×`-monoid *requires the identity fibre to be empty*.
- **Multiplication `μ : c×c → c`.** Backward map `ψ_{s,t} : c[s·t] → c[s] ⊔ c[t]` — a **backward
  routing** sending each position of the product shape to *one* of the two factors.
- **Laws.** Identical unwinding: `·` is a monoid on `S`; the unit coherences force
  `ψ_{e,s} = inr` and `ψ_{s,e} = inl` (using `c[e]=∅`, so `c[e]⊔c[s] = c[s]`); associativity forces
  the coherence `(ψ_{s,t} ⊔ id)∘ψ_{s·t,u} = (id ⊔ ψ_{t,u})∘ψ_{s,t·u}` into `c[s]⊔c[t]⊔c[u]`.

**Theorem B.** A `×`-monoid on `c` is exactly a monoid `(S,·,e)` with `c[e] = ∅`, together with an
**oplax monoidal functor** `P : (S,·,e) → (Set, ⊔, ∅)`, `s ↦ c[s]`, with structure maps
`ψ_{s,t}:c[s·t]→c[s]⊔c[t]` and counit `c[e]→∅` (forcing `c[e]=∅`), satisfying the same associativity
and unit coherences.

Thus Theorems A and B are **one theorem**: a monoid for the Day tensor of a monoidal structure
`(Set, ⊙, I)` on the fibres is a monoid on shapes plus an oplax monoidal functor
`(S,·,e) → (Set, ⊙, I)` on fibres. `⊗` uses `(×,1)`; `×` uses `(⊔,∅)`.

**Corollaries.**
- *Generic containers admit no `×`-monoid*: the identity fibre `c[e]` must be empty, and then every
  position of `c[e·t]=c[t]` must route (via `ψ_{e,t}=inr`) into `c[t]` — fine — but for a container
  with **all fibres nonempty** there is no valid `e`, so **no** `×`-monoid exists.
- *When all fibres are empty* (`c = S·1` up to iso, a "constant/discrete" container), the routing is a
  map `∅→∅` (unique) and the coherences are vacuous, so `×`-monoids `=` **monoids on `S`** — recovering
  the folklore "monoids for the cartesian product `=` monoid objects `=` internal monoids", specialised
  to `Cont`. E.g. `[0,0,0]` gives the `33` monoids on a `3`-element set.

---

## 7. Verification (computation is conviction)

Two independent brute-force layers, both machine-run today and on 07-18:

**(i) Direct law-check vs. from-scratch structure count (⊗).** `scratch/monoid-comonoid-table/table.py`
enumerates *all* candidate `(μ, η)` on a container and checks the three monoid laws by **direct
composition of Poly-morphisms** — never mentioning "monoid" or "oplax". `c6_oplax.py` *independently*
enumerates `(monoid (S,·,e)) + (oplax functor φ into (Set,×))` from scratch, using **exactly** the
coherence equations of §§3–4, and compares counts:

| fibres `c[s]` | ⊗-monoids (direct law-check) | monoid + oplax (independent) | match |
|---|---|---|---|
| `[1]` (=y) | 1 | 1 | ✓ |
| `[2]` | 1 | 1 | ✓ |
| `[3]` | 1 | 1 | ✓ (single shape ⟹ oplax forced ⟹ **unique**) |
| `[1,1]` | 4 | 4 | ✓ (= 4 monoids on `S={0,1}`) |
| `[2,1]` | 9 | 9 | ✓ |
| `[1,1,1]` | 33 | 33 | ✓ (= 33 monoids on `S={0,1,2}`) |

The `S=1` rows confirm the **uniqueness** claim: with one shape, the shape monoid is trivial and the
oplax functor is a *comonoid in `(Set,×)`* — forced to the diagonal — so the ⊗-monoid is unique for
every single-shape container `y^A`, independent of `|A|`.

**(ii) `×`-monoid refinement.** `scratch/monoid-comonoid-table/times_monoid.py` (new today) checks
Theorem B: direct `×`-monoid law-check vs. from-scratch `(monoid with c[e]=∅) + (oplax into (Set,⊔,∅))`:

| fibres | `×`-monoids (direct) | char. (Thm B) | match | note |
|---|---|---|---|---|
| `[0]` | 1 | 1 | ✓ | empty single fibre, trivial monoid |
| `[1]`, `[2]` | 0 | 0 | ✓ | nonempty identity fibre ⟹ **none** |
| `[0,0]` | 4 | 4 | ✓ | = monoids on `{0,1}` |
| `[1,1]` | 0 | 0 | ✓ | no empty fibre for `e` ⟹ none |
| `[0,1]`, `[1,0]` | 2 | 2 | ✓ | empty fibre must be `e` |
| `[0,0,0]` | 33 | 33 | ✓ | = monoids on `{0,1,2}` |

Every case matches. (Larger direct enumerations OOM — the `×`-tensor's fibres blow up — so `[2,1]`,
`[1,1,1]` were only checked on the characterization side; the pattern is fixed by the small cases and
the analytic proof.)

---

## 8. Honesty ledger — novelty, attribution, framing

**Cited, not mine.**
- `⊗ = Day(Set,×)`, the formula `(p⊗q)[s,t]=p[s]×q[t]`, unit `y`, symmetry — **Niu–Spivak
  arXiv:2312.00990 Prop. 3.79** (deep-read, `sources.json`). `× = Day(Set,⊔)` with unit `1=y^∅` and
  `(c×d)[s,t]=c[s]⊔d[t]` is the cartesian product of polynomials (same source, §3). `Cont ≅ Fam(Set^op)`
  — SGF Prop. 3.6; my `day-family-classification` Lemma 1.2.
- The **oplax monoidal functor** notion (structure map `F(X⊗Y)→FX⊗FY`, counit `F(I)→I'`, associativity
  + unit coherences) is standard (e.g. any monoidal-categories reference). My contribution is only the
  *identification* of the ⊗-monoid's fibre data with it.
- The *question* is Niu–Spivak's: **Remark 3.78** flags ⊗-**monoids** in Poly ("collective semantics …
  aggregate contributions") as *future work*, uncharacterised — the dual of the ⊗-comonoid slice of
  Chapter 9 Question 5.

**What the book does *not* contain** (full-PDF, 07-17): no classification of ⊗-monoids in Poly. Rmk 3.78
is a future-work flag, not a theorem.

**Novelty gate (done 07-18, recorded in registry).** ORTHOGONAL to **De Pascalis–Uustalu–Veltrì,
arXiv:2509.25879** (*Monoid Structures on Indexed Containers*): their tensor is functor composition `◁`
(they classify `◁`-monoids `=` indexed polynomial monads), **not** the Dirichlet `⊗`. **CAUTION** (from
the registry): the same group (Uustalu/Veltrì) list *other-tensor* monoids in their §5 future work — so
this should be **promoted and shared promptly**, and framed as *"an elementary answer to an explicit
future-work item,"* **not** a deep theorem. Dorta–Jarvis–Niu (2305.05655) classify `◁`-comonoids in
`ΣΠ`-containers, no Day/⊗ (`dorta-jarvis-niu-neighbour` memory).

**Scoped novelty of this note.** The delta is the explicit, *proved* characterization **"bare ⊗-monoids
in Poly = a monoid on shapes + an oplax monoidal functor `(S,·,e)→(Set,×)` on fibres,"** its uniform
extension to `×` (fibre target `(Set,⊔,∅)`, empty-identity-fibre obstruction), and the structural
account (§5) of why it is *not* a mirror of the comonoid case. The *argument* is an elementary unwinding
of the monoid axioms in container coordinates, corroborated by two independent enumerations — I grade it
**`proved`** and frame it accordingly.

**No remaining mathematical gap.** The result is the monoid instance of the folklore "(co)monoids for a
Day convolution over a fibrewise monoidal base `(Set,⊙,I)` are a (co)monoid on the base object plus a
(op)lax `⊙`-functor on fibres." I derived it by hand in coordinates rather than invoke that general
statement; §7 corroborates on every small case. The lone modelling choice worth flagging: I treat the
monoid `(S,·,e)` as the *discrete* monoidal category on its underlying set, so `P`'s functoriality on
morphisms is vacuous and only the monoidal-coherence data survives — which is exactly the fibre content
that appears. (A `◁`/directed structure would upgrade `S` to a genuine category; that is a *different*
problem — the `◁`-monoids of 2509.25879 — and is deliberately excluded here.)

---

## Appendix — ⊗-monoid morphisms

Let `c, d` be ⊗-monoids. A morphism `h = (h₁ : S_c → S_d, {h♯_s : d[h₁ s] → c[s]})` of ⊗-monoids makes
the unit and multiplication squares commute.

*Unit square* `η_c = h ∘ η_d`... on shapes: `h₁(e_c) = e_d`? Careful with variance: `η_d : y→d`,
`η_c : y→c`, and `h : c→d`, so the triangle is `h ∘ η_c = η_d`. On shapes `h₁(e_c) = e_d`; on the
(forced) fibre map `ε` both sides are the unique map to `1`, no condition. So **`h₁` sends unit to
unit**.

*Multiplication square* `h ∘ μ_c = μ_d ∘ (h⊗h)` (both `c⊗c → d`). On shapes: `h₁(s·_c t) =
h₁(s)·_d h₁(t)` — **`h₁` is a monoid homomorphism** `(S_c,·)→(S_d,·)`. On fibres at `(s,t)`, both
sides are backward maps `d[h₁ s]×d[h₁ t] → c[s·t]`... tracing:
```
   h ∘ μ_c        :  x ↦ φ^c_{s,t}(h♯_{s·t}(x))                (multiply-in-c-then-pull-back)
   μ_d ∘ (h⊗h)    :  x ↦ (h♯_s × h♯_t)(φ^d_{h₁ s,h₁ t}(x))     (pull-back-then-multiply-in-d)
```
Equality says the family `{h♯_s}` intertwines the oplax structure maps `φ^d` and `φ^c` along `h₁` — a
**monoidal (op)lax natural transformation** of the two fibre functors. Together with the homomorphism
condition on shapes, this is exactly a morphism in the Grothendieck category
`∫_{Mon} OplaxMon(-,(Set,×))`. ∎
