# ◁-comonoids in finite-dimensional linear containers = families of k-algebras

**MacBeth — 2026-08-19 (PROVE session).** Upgrades Proposition 4.2 of
`proofs/2026-08-18-linear-containers-vec.md` from **computed** to **proved**.

> **Headline.** In the monoidal category `(LinCont_fd, ◁, I) = (Fam(Vec_fd^op), ◁, I)`
> with composition `(S,P)◁(T,Q) = (S×T, (P_s⊗Q_t))` and unit `I=({∗},k)`, a ◁-comonoid
> `((S,P), δ, ε)` is **exactly** a family `(A_s)_{s∈S}` of unital associative k-algebras —
> one algebra `A_s = (P_s, μ_s, η_s)` on the position space of each shape, with **no**
> cross-shape composition. The comonoid morphisms are backward algebra homomorphisms, so
>
> **`Comon_◁(Fam(Vec_fd^op)) ≅ Fam(Alg_k^op)`**,
>
> the exact k-algebra upgrade of `Cont ≅ Fam(Set^op)` and the exact ◁/Vec analogue of the
> Set fact `⊗`-comonoid in Poly = family of monoids (`bare-dirichlet-comonoid`). The
> crown guess "◁-comonoid over Vec = algebroid (k-linear category)" is **refuted in finite
> dimension**: the counit forces the comultiplication's shape map to the diagonal, so δ
> never reaches an off-diagonal block `P_s⊗P_{s'}` (`s≠s'`), and multi-object composition
> is structurally impossible. The structure is a disjoint family of *one-object* k-linear
> categories = k-algebras.
>
> **Hypotheses used, sharpened.** Only **finite-dimensional positions** are needed
> (to make the composition `◁` land in `Fam(Vec_fd^op)` via Prop 4.1). The shape set `S`
> may be **arbitrary** — finite S is *not* required. Char k is unrestricted.

---

## 1. Setup

I work entirely inside the monoidal category `(Fam(Vec_fd^op), ◁, I)`; no appeal to the
extension functor `⟦−⟧` is needed for this classification.

**Objects and morphisms** (`Fam(Vec_fd^op)`, Def. 0.1 of the 08-18 file). An object is a
pair `(S,(P_s)_{s∈S})` with `S` a set and each `P_s` a finite-dimensional k-vector space.
A morphism `(S,P) → (T,Q)` is a pair `(f, (φ_s)_{s∈S})` with `f:S→T` a function and, for
each `s∈S`, a **k-linear map `φ_s : Q_{f(s)} → P_s`** — *forward on shapes, backward
(contravariant) on positions*. Composition of `(S,P) --u--> (T,Q) --v--> (U,R)` is

    (v∘u)_shape = v_shape ∘ u_shape,        (v∘u)♯_s = u♯_s ∘ v♯_{u_shape(s)}

(backward maps compose contravariantly). This is `Fam(Vec^op)`; identities are `(id, (id))`.

**Monoidal structure** (`◁`, Prop. 4.1 of the 08-18 file). For finite-dimensional
positions,

    (S,P) ◁ (T,Q) := (S×T, (P_s⊗Q_t)_{(s,t)∈S×T}),        I := ({∗}, k).

On morphisms `u:(S,P)→(S',P')`, `w:(T,Q)→(T',Q')`,

    (u◁w)_shape(s,t) = (u_shape s, w_shape t),
    (u◁w)♯_{(s,t)}   = u♯_s ⊗ w♯_t : P'_{u_shape s}⊗Q'_{w_shape t} → P_s⊗Q_t.

The associator `α` and unitors `λ,ρ` are the images of the canonical Set product
associator/unitor on shapes and the canonical Vec tensor associator/unitor on positions;
concretely, on positions (which is all that will matter below) they are the standard
`(U⊗V)⊗W ≅ U⊗(V⊗W)`, `k⊗V ≅ V`, `V⊗k ≅ V`. This makes `(Fam(Vec_fd^op),◁,I)` a
(non-strict) monoidal category. *(That `◁` is well-defined on `Fam(Vec_fd^op)` — i.e. the
composite of two finite-linear containers is again finite-linear — is exactly where
finite-dimensionality of positions enters, via Lemma 1.3 in the 08-18 file. This is the
only hypothesis the whole classification consumes.)*

**Definition (◁-comonoid).** A ◁-comonoid is `(C, δ, ε)` with `C=(S,P)`, morphisms
`δ : C → C◁C` and `ε : C → I`, satisfying

- **counit:** `λ ∘ (ε◁id) ∘ δ = id_C` and `ρ ∘ (id◁ε) ∘ δ = id_C`;
- **coassoc:** `α ∘ (id◁δ) ∘ δ = (δ◁id) ∘ δ`  (both `C → (C◁C)◁C`).

---

## 2. Unpacking the data

`C◁C = (S×S, (P_a⊗P_b)_{(a,b)})`. So:

- **δ : C → C◁C.** A shape map `δ_shape : S → S×S`, write `δ_shape(s) = (l(s), r(s))`; and
  for each `s`, a backward linear map
  `δ♯_s : (P⊗P)_{δ_shape(s)} = P_{l(s)}⊗P_{r(s)} → P_s`.
- **ε : C → I=({∗},k).** The shape map `S→{∗}` is forced. The backward map is, for each
  `s`, a linear map `ε♯_s : k → P_s`, i.e. **a distinguished element** `η_s := ε♯_s(1) ∈ P_s`
  (equivalently the linear map `η_s : k → P_s`).

The variance is the whole point: because positions are contravariant, `δ♯_s` runs
`P_{l(s)}⊗P_{r(s)} → P_s` (a *multiplication*-shaped map) and `ε♯_s` runs `k → P_s` (a
*unit*-shaped map). A ◁-comonoid over Vec will therefore be an *algebra*, not a coalgebra —
exactly as the ⊗-comonoid over Set was a *monoid* (`bare-dirichlet-comonoid` §2).

---

## 3. The counit forces the diagonal on shapes

This step is purely about the shape (Set) components and needs **no** dimension or
cardinality hypothesis.

Shape maps compose covariantly. Read the first counit law `λ∘(ε◁id)∘δ = id_C` on shapes:

    s  --δ-->  (l s, r s)  --(ε◁id)-->  (∗, r s)  --λ-->  r s.

The composite shape map is `s ↦ r(s)`; it must equal `id_S`, so **`r = id_S`**.
The second counit law `ρ∘(id◁ε)∘δ = id_C` on shapes gives `s ↦ l(s) = s`, so **`l = id_S`**.
Hence

> **`δ_shape(s) = (s,s)` — the diagonal.**

Equivalently: the shape components of `(δ,ε)` are a comonoid structure on `S` in the
cartesian monoidal category `(Set,×,1)`, and every object of a cartesian monoidal category
carries a *unique* such structure — the diagonal `Δ` with counit `!`. (This is the identical
mechanism to `bare-dirichlet-comonoid` §3 and to the shape half of `DCont≅Cat`; it holds
verbatim over Vec because shapes live in Set.)

With `l = r = id`, the comultiplication's position component at `s` is a linear map on the
*diagonal* block only:

    μ_s := δ♯_s : P_s ⊗ P_s → P_s.

**Nothing else on shapes is available.** In particular δ can never reach an off-diagonal
block `P_a⊗P_b` with `a≠b`. Flag this — it is the negative half (§6).

---

## 4. The counit laws on positions = the two-sided unit axiom

Now compute the position (backward) component of the first counit law
`λ∘(ε◁id)∘δ = id_C` at shape `s`. Write the composite as `h₃∘h₂∘h₁` with
`h₁=δ`, `h₂=ε◁id`, `h₃=λ`. Contravariant composition gives

    (h₃h₂h₁)♯_s = h₁♯_s ∘ h₂♯_{(s,s)} ∘ h₃♯_{(∗,s)}.

The three factors:

- `h₃♯_{(∗,s)} = λ♯` is the **inverse unitor** `P_s → k⊗P_s`, `v ↦ 1⊗v`
  (λ is the morphism `I◁C→C`; on positions it runs backward, so it is the inverse of the
  canonical `k⊗P_s → P_s`).
- `h₂♯_{(s,s)} = (ε◁id)♯_{(s,s)} = ε♯_s ⊗ id_{P_s} = η_s ⊗ id_{P_s} : k⊗P_s → P_s⊗P_s`.
- `h₁♯_s = δ♯_s = μ_s : P_s⊗P_s → P_s`.

Chasing `v ∈ P_s` right-to-left:

    v  ↦  1⊗v  ↦  η_s⊗v  ↦  μ_s(η_s⊗v).

The law says this equals `id_{P_s}(v) = v`, i.e.

> **`μ_s(η_s ⊗ v) = v`  for all v — `η_s` is a left unit.**

Symmetrically, the second counit law `ρ∘(id◁ε)∘δ = id_C` at `s` gives
`μ_s(v⊗η_s) = v` — `η_s` is a **right unit**. So `η_s` is a two-sided unit for `μ_s`.

*(No finiteness used here beyond `◁` being defined; the computation is pure linear algebra
on the fixed finite-dimensional space `P_s`.)*

---

## 5. Coassociativity = associativity of μ_s

Both sides of the coassociativity law are morphisms `C → (C◁C)◁C = (S×S×S, (P_a⊗P_b⊗P_c))`.
Because `δ_shape = Δ` (diagonal), both sides have shape map `s ↦ (s,s,s)`, so the two
position components at `s` are linear maps `P_s⊗P_s⊗P_s → P_s`. Compute them.

- **`(δ◁id)∘δ`.** `(δ◁id)♯_{(s,s)}` acts as δ on the first tensor factor and `id` on the
  second: `(δ◁id)♯_{(s,s)} = μ_s ⊗ id_{P_s} : (P_s⊗P_s)⊗P_s → P_s⊗P_s`. Precomposing with
  `δ♯_s = μ_s`,

      ((δ◁id)∘δ)♯_s = μ_s ∘ (μ_s ⊗ id) :  x⊗y⊗z ↦ μ_s(μ_s(x⊗y)⊗z).

- **`α∘(id◁δ)∘δ`.** `(id◁δ)♯_{(s,s)} = id_{P_s} ⊗ μ_s : P_s⊗(P_s⊗P_s) → P_s⊗P_s`, and the
  associator's position component `α♯` is the canonical
  `(P_s⊗P_s)⊗P_s → P_s⊗(P_s⊗P_s)` (backward), which merely re-brackets. Precomposing with
  `δ♯_s = μ_s`,

      (α∘(id◁δ)∘δ)♯_s = μ_s ∘ (id ⊗ μ_s) ∘ (rebracket) :  x⊗y⊗z ↦ μ_s(x⊗μ_s(y⊗z)).

Coassociativity equates the two:

> **`μ_s(μ_s(x⊗y)⊗z) = μ_s(x⊗μ_s(y⊗z))`  for all x,y,z — `μ_s` is associative.**

The associator `α` is exactly the bookkeeping that makes the two bracketings comparable; it
is absorbed by the standard MacLane argument (as in any "comonoid coassociativity ⟺
associativity" unwinding). There is **no cross-shape condition** — a `Fam(Vec^op)`-morphism
is a shape map plus an *independent* family of backward maps — and **no cocommutativity** is
forced (symmetry of `◁` on the two middle factors is not part of the comonoid axioms). Hence
`(P_s, μ_s, η_s)` is an *arbitrary* unital associative k-algebra `A_s`.

**Converse.** Given a family `(A_s = (P_s,μ_s,η_s))_{s∈S}` of unital associative k-algebras,
define `ε` by `ε♯_s = η_s` and `δ` by `δ_shape = Δ`, `δ♯_s = μ_s`. Reading §§3–5 backwards,
the two counit laws hold (two-sided unit) and coassociativity holds (associativity). So
every family of algebras yields a ◁-comonoid, inverse to the above. ∎

---

## 6. The negative half: why NOT an algebroid

The crown target hoped `◁`-comonoid over Vec `≅` k-linear category (algebroid, Mitchell
*Rings with several objects*). An algebroid on object set `S` needs, for objects `a,b,c`,
composition maps `hom(b,c) ⊗ hom(a,b) → hom(a,c)` genuinely mixing **distinct** objects.
Encode it container-style with shapes = objects and positions = (co)arrows; composition
would require the comultiplication to send a shape `s` to a configuration indexing a
composable pair `s → · → ·` whose intermediate object may differ from `s`.

**This is impossible over finite-dimensional Vec, and §3 pinpoints why.** The counit forces
`δ_shape(s) = (s,s)`. Therefore:

- δ's position component at `s` is `μ_s : P_s⊗P_s → P_s`, landing in the **diagonal block**
  `(s,s)` only;
- δ never reaches an off-diagonal block `P_a⊗P_b` with `a≠b`;
- so there is no linear map `P_a⊗P_b → P_?` in the structure — no hom-between-distinct-
  objects composition.

The ◁-comonoid is a **disjoint family of one-object k-linear categories**, i.e. a family of
k-algebras: the "diagonal algebroid" with `hom(s,s)=A_s` and `hom(s,s')=0` for `s≠s'`.

**Where does the Set case get its extra composition?** In `DCont ≅ Cat`, the Set container
composition `c◁c` has shape set the *dependent sum* `Σ_{s∈S} S^{c[s]}` — richer than `S×S`
— and it is precisely this dependency (a shape of `c◁c` is "a shape `s` together with, for
each position of `s`, a next shape") that lets the directed-container comultiplication encode
"an arrow followed by an arrow," with the intermediate object varying. Over Vec, Prop. 4.1
shows the composition's shape set collapses to the **plain product** `S×S`: linearity
flattens the dependent sum `Σ_s S^{c[s]}` into `S×S` (a linear map `P_s → ⊕_t V_t` is a
*sum of components*, not a *choice of branch*; Lemma 1.3 / the "genuine structural
difference" remark of Prop. 4.1). With no dependency in the shapes of `C◁C`, the counit's
forcing of a `(Set,×)`-comonoid on `S` has a *unique* solution — the diagonal — and the
off-diagonal blocks are unreachable. **The same biproduct/linearity collapse that flattened
the composition (Prop. 4.1) now degrades algebroids to algebra-families.** It strikes here
for the third time (objects, morphisms, and now comonoids), and this is its comonoid face.

A genuine k-linear category would require a *different*, dependency-carrying composition on
`Fam(Vec^op)` (a lax / bimodule ◁ that does not collapse `Σ_s` to `×`); pinning that down is
Further Work, flagged as the honest sequel.

---

## 7. Theorem (statement) and the category of comonoids

**Theorem.** Let `C = (S,P) ∈ Fam(Vec_fd^op)` with `S` an arbitrary set and each `P_s`
finite-dimensional. The following data are in natural bijection:

1. ◁-comonoid structures `(δ,ε)` on `C` in `(Fam(Vec_fd^op), ◁, I)`;
2. families `(A_s)_{s∈S}` of unital associative k-algebra structures `A_s=(P_s,μ_s,η_s)`,
   one on each position space `P_s`.

The bijection is `δ_shape = Δ`, `δ♯_s = μ_s`, `ε♯_s = η_s`. In particular a **one-shape**
◁-comonoid `({∗},P)` is *exactly* a k-algebra structure on `P` (Mitchell's one-object case),
and there is no cross-shape composition (§6).

**Morphisms.** A ◁-comonoid morphism `h:C→D` (`C,D` with fibre algebras `A^C_s, A^D_t`) is a
`Fam(Vec^op)`-morphism `h=(h_1:S_C→S_D, (h♯_s:P^D_{h_1 s}→P^C_s))` commuting with `ε,δ`.
Unwinding (Appendix), the counit square says `h♯_s(η^D_{h_1 s}) = η^C_s` (preserves unit)
and the comultiplication square says
`h♯_s ∘ μ^D_{h_1 s} = μ^C_s ∘ (h♯_s ⊗ h♯_s)` (preserves multiplication). So each `h♯_s` is a
**k-algebra homomorphism `A^D_{h_1 s} → A^C_s`, backward along `h_1`**. Therefore

    Comon_◁(Fam(Vec_fd^op))  ≅  Fam(Alg_k^op),

the free-coproduct completion of `Alg_k^op` — the precise k-algebra upgrade of
`Cont ≅ Fam(Set^op)` and the ◁/Vec analogue of `Comon(Cont,⊗,y) ≅ Fam(Mon^op)`
(`bare-dirichlet-comonoid`). The **cocommutative** ◁-comonoids form the full subcategory
`Fam(CAlg_k^op)` (commutative algebras).

Layers side by side, over the *same* linear carrier:

| structure on `(S,P)` | is | reference |
|---|---|---|
| ⊗-comonoid in Poly (Set base) | family of **monoids** | `bare-dirichlet-comonoid` |
| ◁-comonoid in Fam(Set^op) | small **category** | `DCont≅Cat` (Ahman–Uustalu) |
| **◁-comonoid in Fam(Vec_fd^op)** | **family of k-algebras** | **this note** |

The Vec/◁ layer sits at "family of one-object k-linear categories": it has the *algebra*
enrichment of the ⊗/Set layer but, unlike the ◁/Set layer, has **lost the multi-object
composition** — the finite-dimensional biproduct collapse is exactly the difference.

---

## 8. Verification (computation is conviction)

`scratch/vec-comonoids/verify.py` (this session) works over `k = F_2` and, for a container
`(S,P)`, enumerates **all** candidate ◁-comonoid data `(δ_shape:S→S×S, (δ♯_s), (ε♯_s))` and
checks the comonoid laws by **direct composition of `Fam(Vec^op)`-morphisms** using the
Prop. 4.1 composition (with the canonical F_2 unitors/associator) — *with no reference to
the word "algebra"* — then compares the surviving set against an *independent* brute-force
enumeration of families of unital associative F_2-algebras on the fibres.

**Results (run 2026-08-19, all four cases MATCH):**

| case | dims | #◁-comonoids (direct law-check) | `∏_s A(n_s)` (independent) | all δ_shape diagonal? | match |
|---|---|---|---|---|---|
| `S={0}` | `(1)` | 1 | `A(1)=1` | yes | ✓ |
| `S={0}` | `(2)` | 12 | `A(2)=12` | yes | ✓ |
| `S={0,1}` | `(1,1)` | 1 | `1·1=1` | yes | ✓ |
| `S={0,1}` | `(1,2)` | 12 | `1·12=12` | yes | ✓ |

Here `A(n)` = number of unital associative F_2-algebra structures on the *fixed* space
`F_2^n` (structures, not iso classes): `A(1)=1`, `A(2)=12`. What the run confirms
*independently of the hand-proof*:
- **`δ_shape` forced diagonal** in every surviving solution (confirms §3). In case 4,
  `δ_shape` ranged over all 16 functions `S→S×S`; **no off-diagonal survivor** — the two
  shapes decouple, `1·12=12` (confirms §6, the algebroid refutation).
- **count = unfiltered algebra count** — associativity + unit only, never commutativity —
  so **no cocommutativity is forced** (confirms §5), and each surviving `(δ♯_s, ε♯_s)` is a
  unital associative multiplication with unit exactly `ε♯_s` (the per-shape correspondence
  is a bijection).
- the associator `α` was numerically validated to be the identity under left-nested
  `np.kron` ordering (checked on random triples before the main run), matching §5.

---

## 9. Honesty ledger

**Cited, not mine.** `◁ = (S×T, P⊗Q)` and the finite-dim composition formula — Prop. 4.1 of
`2026-08-18-linear-containers-vec.md` (mine, `proved`). The Set precedents: ⊗-comonoid = family
of monoids (`bare-dirichlet-comonoid`, mine, `proved`); ◁-comonoid in Set = small category
(`DCont≅Cat`, Ahman–Uustalu; Niu–Spivak Thm 7.28). "Algebroid" = Mitchell, *Rings with
several objects*, Adv. Math. 8 (1972). Strict polynomial functors (Friedlander–Suslin) own
the additive *objects* (Remark 3.5 of the 08-18 file); they do not index the shape set.

**Novelty (scoped).** The delta is the explicit, proved identification
**◁-comonoid in `Fam(Vec_fd^op)` = family of k-algebras**, `Comon_◁ ≅ Fam(Alg_k^op)`, with
the sharpened hypothesis (finite-dim positions only, **S arbitrary**), and the precise
diagnosis (§6) that the counit-forced shape-diagonal — a consequence of Prop. 4.1's collapse
of the dependent sum to a plain product — is what refutes the algebroid guess in finite
dimension. The argument is elementary (an unwinding of the comonoid axioms in `Fam(Vec^op)`
coordinates), so I grade it **proved** and describe it as *"a clean base-change of the Set
computation, with the variance turning comonoid into algebra and the biproduct collapse
turning algebroid into algebra-family,"* not as a deep theorem.

**Scope guardrails.** Finite-dimensional positions are used exactly once — to keep `◁`
inside `Fam(Vec_fd^op)` (Prop. 4.1). The **infinite-dimensional** case is *not* settled: there
the composition formula weakens (Lemma 1.3 fails, tensor–hom needs f.d.), the dependent-sum
may not fully collapse, and genuine algebroids may reappear — this is exactly the
Diers-extensivity obstruction and is the stated sequel, **not** claimed here. No char-`p`
subtlety arises: `μ_s : P_s⊗P_s → P_s` is an unrestricted bilinear map (no evaluation,
no division by 2).

---

## Appendix — comonoid morphisms are backward algebra homomorphisms

Let `C,D` be ◁-comonoids with fibre algebras `A^C_s=(P^C_s,μ^C_s,η^C_s)`,
`A^D_t=(P^D_t,μ^D_t,η^D_t)`. A morphism of ◁-comonoids is a `Fam(Vec^op)`-morphism
`h=(h_1:S_C→S_D, (h♯_s:P^D_{h_1 s}→P^C_s))` making the counit and comultiplication squares
commute.

*Counit square* `ε_C = ε_D ∘ h`. On positions at `s` (`k → P^D_{h_1 s} → P^C_s`):
`1 ↦ η^D_{h_1 s} ↦ h♯_s(η^D_{h_1 s})`, and this must equal `η^C_s`. So `h♯_s` **preserves the
unit**.

*Comultiplication square* `δ_D ∘ h = (h◁h) ∘ δ_C`. Both sides have shape map
`s ↦ h_1 s ↦ (h_1 s, h_1 s)` (using `δ` diagonal on both). On positions at `s`
(`P^D_{h_1 s}⊗P^D_{h_1 s} → P^C_s`), contravariant composition gives:

    δ_D ∘ h      :  u⊗v ↦ h♯_s( μ^D_{h_1 s}(u⊗v) )         [multiply in D, then pull back]
    (h◁h) ∘ δ_C  :  u⊗v ↦ μ^C_s( h♯_s(u) ⊗ h♯_s(v) )        [pull back, then multiply in C]

Equality for all `u,v` says `h♯_s` **preserves multiplication**. Hence each `h♯_s` is a
k-algebra homomorphism `A^D_{h_1 s} → A^C_s`, *backward* along `h_1` — exactly a morphism in
`Fam(Alg_k^op)`. With §7 this gives the isomorphism of categories
`Comon_◁(Fam(Vec_fd^op)) ≅ Fam(Alg_k^op)` (and `Fam(CAlg_k^op)` on the cocommutative full
subcategory). ∎
