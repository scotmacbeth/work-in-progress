# The proof-relevant monad liftings of Reader are small categories

**MacBeth — PROVE session, 2026-08-09 (deep-work).**
Answers `state/PROVE.md` ("exhaustiveness of the ∏/Σ parity dichotomy for proof-relevant liftings
of Reader/State"). The clean conjecture ("every proof-relevant monad lifting is ∏, Σ, or a leafwise
mix") is **false** — as the honest meta-pattern predicted (7th instance). The finer structure it
hands back is the crown one: the fibred proof-relevant monad liftings of **Reader** `y^E` are
classified by **`E`-indexed families of small categories** — i.e. by (`E`-indexed) polynomial
comonads, one categorical level down. The clean points ∏/Σ are respectively **excluded** (∏) and
one **extreme** (Σ = discrete categories) of this classification.

Builds on `proof-relevance-boundary` (proved), `sigma-monad-is-triangle-monoid` (proved),
`neil-A-E-predicate-liftings` (proved). Registry node `pi-sigma-dichotomy-exhaustive` in
`proofs/registry/effect-coeffect-arrows.json`.

---

## 0. Headline

> **Theorem (Reader classification).** Let `E` be a set and `R = y^E = (1,E)` the Reader container
> monad. Fibred proof-relevant (`Cont`-valued) monad liftings of `R` along the shape fibration
> `p : Cont → Set`, `(S,P) ↦ S`, whose position-aggregator is **polynomial**, are in bijection with
> **`E`-indexed families of small categories** `(C_v)_{v∈E}`. Under the bijection the lifting has
> aggregator
> ```
>     L(B) = ∐_{v∈E} ∐_{i ∈ Ob C_v}  B_v^{ C_v(i,→) },      C_v(i,→) = {morphisms of C_v out of i},
> ```
> with unit `ε` = identity morphisms and multiplication `δ` = composition.
>
> Equivalently: **monad liftings of Reader = (`E`-indexed) polynomial comonads = small categories.**
> Consequences: (i) the Ahman–Bauer `∏`-lifting `T_R` (full product over leaves) is **not** among
> them — Reader has no proof-relevant `∏`-monad lifting, matching `R` non-cartesian; (ii) `Σ_U`
> (partial sum over `U ⊆ E`) is the family of **discrete** categories on the leaves of `U`; the
> full `Σ` is the discrete category on all of `E`; (iii) genuine **non-discrete** liftings exist —
> e.g. `L(B)=B_0×B_0` with the ℤ/2 comonad structure (a one-object groupoid), which is neither ∏
> nor Σ nor a leafwise mix; (iv) **analytic** (non-polynomial, e.g. symmetric/Bag) aggregators are
> excluded by the counit — polynomial *is* the boundary (the recurring "polynomial vs analytic"
> discriminator, now 7-for-7).

The proof-relevant lifting story thereby **welds to the directed-container / `Cat` spine** (grant
Path 2): predicate liftings of Reader *are* small categories.

---

## 1. Setup

A **container** `X=(S,P)`: shapes `S`, positions `P s` (`s∈S`); extension `⟦X⟧Q = Σ_{s}Q^{P s}`.
Morphism `(u,φ):X→X'`: `u:S→S'` forward, `φ_s:P'(us)→P s` backward; **cartesian** iff each `φ_s`
bijective. `Cont ≃ Poly` monoidally (`◁`=composition, unit `y=(1,1)`); `lean-cont-category-done`.

**Reader** `R=y^E=(1,E)`: one shape, `E` positions; `⟦R⟧Q=Q^E`, so `R(S)=S^E`. As a Set-monad
`R(A)=A^E` with `η_A:A→A^E` constant and `μ_A:A^{E×E}→A^E` the diagonal `mm ↦ (b↦mm(b,b))`. `R` is
a `◁`-monoid — the diagonal comonoid `(E, Δ:E→E×E, !:E→1)` (`sigma-monad-is-triangle-monoid`).

**The shape fibration** `p:Cont→Set`, `(S,P)↦S`, is the families fibration: the fibre over `S` is
`Set^S`, reindexing along `f:S→S'` is `f^*` with adjoints `Σ_f ⊣ f^* ⊣ Π_f`.

**A fibred monad lifting of `R`** is a monad `(T,η^T,μ^T)` on `Cont` such that `p` is a strict monad
morphism onto `(R,η,μ)` and `T` preserves cartesian morphisms (fibred). "Proof-relevant" = `T`
lands in `Cont` (positions are *sets*, not truth values) — as opposed to the `□/◇` liftings on the
subobject fibration (`proof-relevance-boundary` §3).

---

## 2. Reduction: liftings ↔ aggregators `(L,ε,δ)`

> **Proposition 2.1 (reduction).** Fibred endofunctors of `Cont` over `R` correspond bijectively
> (up to natural iso) to functors `L : Set^E → Set`, via `T(S,P) = (S^E, m ↦ L(P∘m))`
> (`m:E→S` a Reader-shape). Monad structures on such a `T` over `(R,η,μ)` correspond to pairs
> ```
>   ε_A : L(⟨A⟩) → A            (⟨A⟩ = constant family at A),      natural in A;
>   δ_D : L(b↦D(b,b)) → L(b↦L(c↦D(b,c))),                          natural in D:E×E→Set,
> ```
> subject to the three monad laws (§2.2). Here `η^T`'s backward part is `ε`, `μ^T`'s is `δ`.

*Proof.* **(functor part)** For `m:E→S` let `α_m:(E,P∘m)→(S,P)` be `(m, id)` — forward `m`,
backward the identities `P(mb)→P(mb)`. It is **cartesian**. Fibredness ⟹ `Tα_m` is cartesian, so
its backward map at the shape `id_E ∈ E^E` (which `R(m)` sends to `m`) is a bijection
`P̃(m) ≅ (P∘m)~(id_E)`. Define `L(B) := B~(id_E)` on the container `(E,B)`; then `P̃(m) ≅ L(P∘m)`,
naturally. Functoriality of `T` on vertical morphisms makes `L:Set^E→Set` a functor. Conversely any
functor `L` yields a fibred `T` by the displayed formula (cartesian in, cartesian out, since `L`
preserves isos). **(monad part)** `η^T_{(S,P)}` lies over `η_S:s↦const_s`; its backward map
`P̃(const_s)=L(⟨P s⟩)→P s` is, by naturality in `(S,P)`, a single natural `ε_A:L(⟨A⟩)→A`
(generic case `(1,A)`). `μ^T:TT→T` lies over `μ_S:S^{E×E}→S^E`; its backward map at `mm` is
`P̃(μ mm)=L(b↦P(mm(b,b)))→(TT)~(mm)=L(b↦L(c↦P(mm(b,c))))`, i.e. a natural `δ_D` with
`D(b,c)=P(mm(b,c))`. The monad laws transport identically (both `T`-laws and `(ε,δ)`-laws are
determined at the generic object). ∎

### 2.1 The two canonical points, in these terms
- **`∏` (Ahman–Bauer `T_R`):** `L(B)=∏_{v∈E}B_v`. Then `T_R(S,P)=(S^E, m↦∏_v P(mv))`.
- **`Σ` (`R◁−`):** `L(B)=∐_{v∈E}B_v`. Then `T^Σ_R = R◁− = (S^E, m↦∐_v P(mv))`.
- **`Σ_U`:** `L(B)=∐_{v∈U}B_v`, `∅≠U⊆E`.

### 2.2 The three laws (backward maps; forward parts are Reader's, a genuine monad)
With `ε` the counit and `δ` the comultiplication of §2:
- **(RU)** `ε_outer ∘ δ = id` : `L(Δ^*D) →^δ L(L̂ D) →^{ε on outer L} L(Δ^*D)`.
- **(LU)** `L(ε)∘ δ = id` : apply `ε` inside each leaf.
- **(A)** `L(δ)∘δ = δ_L ∘ δ` : the two `E^3` composites agree.

---

## 3. The classification (proof)

Assume `L` **polynomial**: `L(B) = ∐_{s∈Σ} ∏_{v∈E} B_v^{P_L(s,v)}`, shape set `Σ`, position sets
`P_L(s,v)` (finite). Write `Q_s = ∐_v P_L(s,v)` (all positions of shape `s`). We show `(L,ε,δ)+laws`
is exactly a small category per leaf.

**Step A (unit ⟹ marked position per shape).** By Yoneda,
`Nat_A(L(⟨A⟩),A)=Nat_A(∐_s A^{Q_s}, A)=∏_s Nat_A(A^{Q_s},A)=∏_s Q_s`. So a natural `ε` exists **iff
every `Q_s≠∅`**, and then `ε` is a choice of a **distinguished position** `e_s∈Q_s` per shape. Let
`λ(s)∈E` be the leaf of `e_s`.

**Step B (δ ⟹ inner shapes are pure).** As functors of `D∈Set^{E×E}`, `Dom(D)=L(Δ^*D)` and
`Cod(D)=L(L̂ D)` are polynomial: a `Dom`-shape is `s∈Σ` with arity `P_L(s,v)` at variable `(v,v)`
and **`∅` at every off-diagonal `(b,c)`, `b≠c`**; a `Cod`-shape is `(s†; (s'_{v,k})_{v,k∈P_L(s†,v)})`
with arity at `(v,c)` equal to `∐_k P_L(s'_{v,k},c)`. A container morphism `Dom⇒Cod` maps each
`Dom`-shape `s` to some `Cod`-shape and, per variable, a **backward** map on positions. At an
off-diagonal `(b,c)` the `Dom`-arity is `∅`, so the backward map `[Cod-arity]→∅` forces the
`Cod`-arity `∅` there: **every inner `s'_{v,k}` is `v`-pure** (`P_L(s'_{v,k},c)=∅` for `c≠v`).
*(Corollary: `∏` — whose only shape reads two leaves and has no pure shape — admits no `δ` at all.)*

**Step C (left unit ⟹ δ preserves the outer shape).** `(LU)`: `L(ε)∘δ=id`. Applying `ε` inside
each inner `L` collapses each inner shape to its marked position but leaves the **outer** shape `s†`
untouched; equality with `id` (which fixes shape `s`) forces `s† = s`. So `δ(s)=(s;(s'_{v,p})_{p∈P_L(s,v)})`.

**Step D (right unit ⟹ every shape is pure).** `(RU)`: `ε_outer∘δ=id`. `ε_outer` selects the
outer marked position `e_s=(λ(s),p_0)`, returning the inner element `s'_{λ(s),p_0}` at that slot;
equality with `id` forces `s'_{λ(s),p_0}=s`. By Step B this inner is `λ(s)`-pure, hence **`s` is
`λ(s)`-pure**: `P_L(s,v)=∅` for `v≠λ(s)`. Therefore
```
   Σ = ∐_{v∈E} Σ_v   (Σ_v = shapes with λ=v),      L(B) = ∐_{v∈E} ∐_{s∈Σ_v} B_v^{P_L(s)},
```
with `P_L(s):=P_L(s,λ(s))`.

**Step E (each leaf = a polynomial comonad = a category).** Fix `v`. Restrict to families
supported on leaf `v` (`B_w=∅`, `w≠v`); write `L_v(A):=L(B)|_{B_v=A}=∐_{s∈Σ_v}A^{P_L(s)}`. The
structure restricts to `ε:L_v⇒Id` and `δ:L_v⇒L_vL_v` (Steps C–D make the `E^2`-data collapse to
the leaf-`v` diagonal), and `(RU),(LU),(A)` become exactly the **comonad** counit and
coassociativity laws. So `(L_v,ε,δ)` is a **polynomial comonad on `Set`**. By the equivalence
**polynomial comonads ≅ small categories** (Ahman–Chapman–Uustalu 2014, "When is a container a
comonad?"; Spivak's `Cat^♯`, `cat-hash-is-dcont-cof`), this is precisely a small category `C_v`:
objects `Σ_v`; morphisms out of `s` the set `P_L(s)`, with **target** `t(p)=s'_{v,p}∈Σ_v`;
identities `e_s` (the marked positions); composition the backward map of `δ`. The monad-lift laws
`(RU),(LU)` are the identity laws and `(A)` is associativity.

Conversely, any family `(C_v)` yields `(L,ε,δ)` by the displayed formulae, and the category axioms
give `(RU),(LU),(A)`. The two constructions are mutually inverse. ∎

> **The `monad↔comonad` twist.** The lifting is a **monad** on `Cont` but its per-leaf aggregator is
> a **comonad** on `Set`: `μ^T:TT→T` is a container morphism, so its backward map runs
> `L_v ⇒ L_vL_v` — a *comultiplication*. This is the "one operation, two faces" phenomenon
> (`position-op-monads-to-comonads`): the fibrewise op turns the lift's multiplication into the
> category's composition.

---

## 4. What the clean points become

| aggregator `L` | category data | is it a monad lifting of Reader? |
|---|---|---|
| `∏_v B_v` (Ahman–Bauer `T_R`) | a single object reading **all** leaves (impure) | **No** — Step B has no pure inner; `δ` does not exist. (Matches `R` non-cartesian: `proof-relevance-boundary`.) |
| `∐_{v∈U} B_v` (`Σ_U`) | **discrete** category on objects `U`, `λ=id` | Yes — unique structure (identities only). |
| `∐_v W_v·B_v` (weighted) | **discrete** category, `λ:∐W_v→E` non-injective | Yes. |
| `B_0×B_0` with swap `δ` | **one-object groupoid ℤ/2** on leaf 0 | Yes — a genuine non-Σ, non-∏ lifting. |
| `B_0×B_1` etc. (any impure shape) | a cross-leaf object | **No** — 0 liftings. |

So the survivors are **categories**; `Σ_U` are exactly the *discrete* ones; the previously-imagined
"leafwise mix of ∏ and Σ" is a red herring at the Reader level — the honest parameter is a *small
category per leaf*, and products appear only **within a single leaf** (a shape may read one leaf
with multiplicity `≥2`, giving the hom-sets of a non-discrete category), never **across** leaves
(which is exactly the ∏-obstruction).

---

## 5. Analytic aggregators are excluded (polynomial is the boundary)

The classification assumed `L` polynomial. The counit rules out the natural non-polynomial rivals.

> **Proposition 5.1.** If `L:Set^E→Set` admits a natural counit `ε:L(⟨-⟩)⇒Id`, then no summand of
> `L` may be a non-trivially *symmetric* functor. In particular the symmetric square `Sym²(B_v)` and
> the size-2 multiset (`Bag`) functor admit **no** natural `ε`, hence are not monad liftings.

*Proof/evidence.* A natural `ε:L(⟨-⟩)⇒Id` assigns to each `x∈L(⟨A⟩)` an element `ε(x)∈A`, natural
in `A`; naturality under every `f:A→A'` forces `ε(x)` to lie in the intersection of all subsets
`A_0⊆A` with `x∈im(L(⟨A_0⟩))` — a *canonical* element. A symmetric summand (e.g. an unordered pair
`{a,b}`, fixed by the swap of `A`) has no swap-invariant canonical element, contradiction. Verified
computationally (`analytic.py`): `Sym²(B_0)` and `Bag_2(B_0)` yield **no** natural `ε`, while the
ordered `B_0×B_0` does. ∎

This is the recurring **polynomial-vs-analytic** discriminator (the boundary file's 6th-instance
prediction), here in its 7th incarnation: the exotic escape is *analytic*, and it is killed by the
unit. (A fully general "every Set-comonad with a counit is polynomial" would upgrade Prop 5.1 to a
theorem removing the polynomiality hypothesis in §3; I do not claim it — see §7.)

---

## 6. Verification (computational)

`scratch/dichotomy-exhaustiveness/` — two *independent* engines agree:
- `monad.py` builds `T,η^T,μ^T` as genuine `Cont`-endofunctor/morphisms and checks the three monad
  laws on small containers; `enum.py` enumerates **all** `(ε,δ)` (complete for polynomial `L`: `ε`=
  marked position, `δ`= pure routing, both forced by §3) and counts monad liftings.
- `catcount.py` counts labeled small categories with prescribed objects/out-degrees from the
  category axioms.

Matches (`#monad-liftings` = `#categories`):

| `L` (leaf-graph) | `enum` monads | `catcount` | note |
|---|---|---|---|
| `B_0²`  = out-deg `[2]` | **4** | **4** | = monoids on 2 elements (incl. ℤ/2) |
| `B_0+B_0` = `[1,1]` | **1** | **1** | discrete on 2 objects |
| `B_0²+B_0` = `[2,1]` | **6** | **6** | |
| `B_0³` = `[3]` | (not run; expensive) | 33 | = monoids on 3 elements |
| `B_0²+B_1` (multi-leaf) | **4** | **4** = 4·1 | leaves independent (coproduct) |
| `Σ_U`, weighted | **1** each | 1 | discrete categories |
| `∏=B_0B_1` | **0** (`δ` ∄) | 0 | ∏ excluded |
| `B_0B_1+B_0+B_1` (∏+pures) | **0** | 0 | any impure shape ⟹ no lifting |

`analytic.py`: `Sym²`, `Bag_2` have **no** natural `ε`; ordered `B_0²` does.

---

## 7. Honesty — status and gaps

- **Proved (this file):** the reduction (Prop 2.1); Steps A–E, giving the bijection **polynomial
  monad liftings of Reader ≅ `E`-indexed small categories**; ∏ excluded; the analytic counit
  obstruction (Prop 5.1). Two independent computations agree on every tested case.
- **Hypothesis in the main theorem:** `L` **polynomial**. Justified as the intended ("`Cont`-valued",
  familially-representable) setting and by Prop 5.1 excluding the natural analytic rivals; a full
  removal of the hypothesis needs the lemma *"every accessible `Set`-comonad with a counit is a
  polynomial comonad."* I neither prove nor assume this beyond Prop 5.1 — **flagged**.
- **`Cat` equivalence cited:** polynomial comonads ≅ small categories (Ahman–Chapman–Uustalu; used
  in Step E). This is `proved`/published elsewhere; cited, not re-proved.
- **State and general container monads:** NOT settled here. State is also a container monad (the
  store `◁`-monoid) that keeps exactly one distinguished token per surviving leaf
  (`proof-relevance-boundary` §4.2), so Steps B–D (pure-shape forcing) should transfer; but its
  shape set `S^S` makes the aggregator vary with shape and couples the leaves through threading.
  **Conjecture (next PROVE target):** monad liftings of a container monad `M` ↔ *categories internal
  to / fibred over `M`* (for Reader, `M=y^E` discrete ⟹ plain `E`-indexed categories). State is the
  first test. Flagged as open.

---

## 8. One line

Reader's proof-relevant monad liftings are **not** ∏/Σ/mix — ∏ is excluded (Reader is not
cartesian) and the survivors are exactly **(`E`-indexed) small categories**: the multiplication of
the lift is category composition read through the fibrewise op, `Σ_U` are the discrete categories,
ℤ/2-type groupoids are genuine non-Σ liftings, and analytic aggregators die on the counit — so the
predicate-lifting story welds, one categorical level down, to the directed-container `Cat` spine.
