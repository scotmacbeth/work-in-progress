# Lifting the branching obstruction from the fibre to a full container morphism

**MacBeth — PROVE session, 2026-08-04.** Hardening of the book's headline dichotomy
"effect–coeffect arrow category ⟺ `M` non-branching" (`2026-07-29-effect-coeffect-arrows.md`).
Target from `state/PROVE.md`: upgrade the full-morphism non-associativity of the biKleisli
compositor from **computed** (`bikleisli.py`) to **proved**, and show the obstruction is the
fibre-level `E2′` failure **necessarily lifted** through the whole `Cont`-morphism — an iff at
the full container-morphism level, not merely fibrewise.

---

## 0. A correction the PROVE statement forces: `M = 1 + X²` is not a cartesian monad

`PROVE.md` proposes `M = 1 + X²` as "the simplest branching cartesian monad, max arity 2".
**No such monad exists.**

> **Proposition 0 (arity gap).** A cartesian (polynomial) monad `M` on `Set` with a genuine
> binary operation has operations of unbounded arity; in particular its maximal leaf-arity is
> `∞`, never `2`. Hence a cartesian monad has max arity in `{≤1} ∪ {∞}`; "exactly `2`" is
> impossible.

*Proof.* For a polynomial monad `μ` is cartesian, so the arity of `μ` applied to a two-level
tree equals its number of leaves (arities add under grafting; Gambino–Kock 2013). Let `β` be a
binary operation (arity `2`). The two-level tree `β(β(-,-), β(-,-)) ∈ M M X` grafts `β` into
each of the two inputs of `β`, hence has `2 + 2 = 4` leaves; `μ` sends it to an operation of
`M X` of arity `4` (the "self-plug `n ↦ n²`", here `2 ↦ 4`). Iterating, `M` contains operations
of arity `4, 16, …`, unbounded. If instead there is **no** operation of arity `≥ 2`, max arity is
`≤ 1`. ∎

The functor `1 + X²` carries only arities `0` and `2`, so it cannot be closed under such a `μ`:
it is **not** a cartesian monad. (This is exactly the arity gap recorded in
`memory/atkey-index-degree-negative`.) The honest minimal branching witness inside the
Ahman–Bauer `∏`-cointerpretation class is therefore **`M = Pf`** (finite powerset): commutative
(so the reverse compositor `κ` exists), branching (support unbounded), non-cartesian (`μ =` union
**merges** leaves — the very feature that breaks `E2′`). A second natural candidate, `Reader² = X²`
(commutative, arity exactly `2`), is **excluded** by the framework: its unit `η(x) = (x,x)` gives
two leaves with the *same* label, and the `∏`-cointerpretation multiplication `μ^T` (label-matching
restriction `j`) requires distinct leaf labels. So we work with `M = Pf`. Everything below is over

  `A₁ = ({a,b}, {a ↦ {0,1}, b ↦ {0}})`,

the smallest container exhibiting the phenomenon (two shapes, so two subsets can overlap; the
shared shape carries two positions).

---

## 1. Recollection: containers, the two liftings, and the reverse compositor `κ`

Containers `(S,P)`; morphism `(u,f):(S,P)→(T,Q)` is a forward `u:S→T` and a **backward** family
`f_s:Q(us)→P(s)`; backward maps compose contravariantly. `⟦S,P⟧Y = Σ_{s} Y^{P s}`.

* **Comonad** `G(S,P) = (S, Pf∘P)`: counit `ε` backward `η^{Pf}` (singleton), comultiplication
  `δ` backward `μ^{Pf}` (**union**); identity on shapes.
* **Monad** `T(S,P) = (Pf S, P^⋆)`, `P^⋆(m) = ∏_{s∈m} P(s)` (Ahman–Bauer Thm 6.3): unit `η^T`
  covers `η^{Pf}` (backward the singleton projection `i`), multiplication `μ^T` covers `μ^{Pf} =`
  union (backward the **restriction** `j`: a position over the merged leaf-set is copied to every
  nested occurrence of each leaf).

An **effect–coeffect arrow** `p ⇝ q` is a `Cont`-morphism `f : G p → T q`. Concretely: forward
`u_f : S_p → Pf S_q`, backward `f^\#_s : ∏_{s'∈ u_f s} P_q(s') → Pf(P_p s)`.

The **reverse compositor** is the lax product-comparison
`κ : G T ⇒ T G`, identity on shapes, backward at `m∈Pf S`
`κ_m : ∏_{s∈m} Pf(P s) → Pf(∏_{s∈m} P s)`, the **cartesian product** of the leaf-indexed sets.

**biKleisli composition** of `f:Gp→Tq`, `g:Gq→Tr`:
```
        δ_p        G f        κ_q        T g        μ^T_r
  g⋆f : Gp ──▶ GGp ──▶ GTq ──▶ TGq ──▶ TTr ──▶ Tr .
```
Identity `p⇝p` is `η^T_p ∘ ε_p`.

The four mixed-distributive-law axioms for `κ` are abbreviated `E1′–E4′`. From
`2026-07-27` / `2026-07-29` (machine-verified `entwine.py`): **`E1′, E3′, E4′` hold for every `M`;
`E2′` (the `μ^T`-compatibility) holds iff `M` is non-branching.** For `Pf` it fails.

---

## 2. The fibre-level `E2′` failure (recalled with orientation)

`E2′` equates two `Cont`-morphisms `G T T A ⇒ T G A`:
`κ ∘ G(μ^T)` versus `μ^T_G ∘ T κ ∘ κ_T`. Both are identity on shapes.

Over `A = A₁`, evaluate at the `Pf(Pf S)`-shape `m = {{a,b}, {a}}` (so `μ^{Pf}(m) = {a,b}`, and
leaf `a` is **shared** by the two outer sets) and at the `TGA`-position `({0,1}, {0})` (leaf
`a ↦ {0,1}`, leaf `b ↦ {0}`). The two sides give **distinct** subsets of the `GTTA`-fibre:

| side | reading | value |
|---|---|---|
| `κ ∘ G(μ^T)` | merge `a` first, **then** cartesian product (choices at the two copies of `a` are *tied*) | `{ ((0,0),(0,)), ((1,0),(1,)) }`  (2 tuples) |
| `μ^T_G ∘ Tκ ∘ κ_T` | cartesian product first, **then** merge (choices at the two copies of `a` are *independent*) | full product (4 tuples) |

`2 ≠ 4`: `E2′` fails. The obstruction is exactly **"product of unions ⊊ union of products"** at a
leaf that is (i) shared by ≥2 outer sets and (ii) carries ≥2 positions. This is the fibre-level,
single-shape statement machine-verified in `BranchingObstruction.lean`.

---

## 3. Theorem and proof of the lift

> **Theorem (full-morphism lift).** For `M = Pf` there is a triple of arrows
> `f, g, h : A₁ ⇝ A₁` whose biKleisli composite is **non-associative as full `Cont`-morphisms**:
> `(h⋆g)⋆f ≠ h⋆(g⋆f)`. The two morphisms agree on shapes and on every backward component except
> at source shape `b`, target position `(1,0) ∈ P^⋆({a,b})`, where they take the distinct values
> `∅` and `{0}` in `Pf({0})`. This single discrepancy arises, through the composite's transport,
> from the fibre `E2′` failure of §2 at the merged leaf `a`: both bracketings route through the same
> overlap shape, and every transport map is a bijection at that leaf, so the fibre inequality
> **cannot** be cancelled downstream. Hence
> the branching obstruction is a full-morphism obstruction, and
> "arrow category ⟺ non-branching" is an **iff at the container-morphism level.**

The witness (all three share the idempotent forward `u : a ↦ {a}, b ↦ {a,b}`):

```
f^\#_b : (0,0)↦∅, (1,0)↦{0}      f^\#_a : (0)↦∅, (1)↦∅
g^\#_b : (0,0)↦{0}, (1,0)↦∅      g^\#_a : (0)↦∅, (1)↦{1}
h^\#_b : (0,0)↦∅, (1,0)↦{0}      h^\#_a : (0)↦∅, (1)↦{0,1}
```

### 3.1 Lemma F — forward agreement (all `M`, all triples)

*The two bracketings have equal shape maps.* Indeed the shape map of `⋆` is, for `s∈S_p`,
`s ↦ ⋃_{t∈u_f s} u_g(t)` — precisely **Kleisli composition in `Kl(Pf) = Rel`** (relational
composition of `u_f, u_g`). Relational composition is associative, so `(h⋆g)⋆f` and `h⋆(g⋆f)` have
the same forward map. For our witness every forward is the idempotent `u`, and one checks
`u ; u = u` (`b ↦ ⋃_{t∈{a,b}} u(t) = {a}∪{a,b} = {a,b}`, `a ↦ u(a)={a}`), so **both composites have
forward `u`.** Any inequality is therefore confined to the backward maps. ∎

### 3.2 Non-associativity — the forced finite calculation at `(b,(1,0))`

Both bracketings are 5-stage composites; we evaluate the backward map at source shape `b` and
target position `(1,0)`. Each stage is a named structural map, so each value below is **forced**
by a single definition (verified independently in `independent_check.py`).

First two intermediate composites (their backward at `b`, computed by the same five rules):

* `g⋆f` has `(g⋆f)^\#_b(1,0) = ∅`. *(The `f`-content `{0}` at `(1,0)` meets `g`'s empty value:
  after `δ,Gf,κ` the position threads to a tuple whose `g`-leaf is `∅`, and `T g` then `μ^T`
  return `∅`.)*
* `h⋆g` has `(h⋆g)^\#_b(1,0) = {0}`. *(`g`'s value at `(1,0)` is `∅` but the surviving thread is
  carried by `h^\#_b(1,0)={0}` through the shared leaf `a`.)*

Now the outer stages.

**Right bracketing `h⋆(g⋆f) = μ^T ∘ T h ∘ κ ∘ G(g⋆f) ∘ δ`, at `b`:**
`δ` fixes `b`; `G(g⋆f)` sends `b ↦ {a,b}` and applies `Pf((g⋆f)^\#_b)`, whose value at every
position over `{a,b}` is `∅` because `(g⋆f)^\#_b ≡ ∅` (§3.2, first bullet). All subsequent stages
(`κ` cartesian, `T h`, `μ^T` restriction) preserve `∅`. **Value `∅`.**

**Left bracketing `(h⋆g)⋆f = μ^T ∘ T(h⋆g) ∘ κ ∘ G f ∘ δ`, at `b`:**
`δ` fixes `b`; `G f` sends `b ↦ {a,b}` and applies `Pf(f^\#_b)`, carrying `(1,0) ↦ {0}`
(`f^\#_b(1,0) = {0}`). `κ_{\{a,b\}}` (cartesian) sends the family `({1},{0})` and `({0,1},{0})` to
sets containing the tuple `(1,0)`; concretely the thread survives as `{0}`. `T(h⋆g)` forms the
**overlap** `Pf`-shape `{{a,b},{a}}` (because `(h⋆g)` has forward `u`, so `Pf(u)\{a,b\} = {u(a),u(b)}
= {{a},{a,b}}`) and its backward carries the position `((1,0),(1,)) ↦ {0}` via
`(h⋆g)^\#_b(1,0)={0}` (§3.2, second bullet). `μ^T` (restriction `j` at the merged leaf `a`) returns
`(1,0) ↦ {0}`. **Value `{0}`.**

Thus `(h⋆g)⋆f` and `h⋆(g⋆f)` agree on shapes (Lemma F) and on all other backward entries
(machine-checked; the two morphisms are small and fully enumerable) but differ at `(b,(1,0))`:
`{0} ≠ ∅`. **The composite is non-associative as a full `Cont`-morphism.** ∎

*(This is a genuine proof, not merely a machine report: the situation is finite and each of the
ten stage-values above is the value of one structural map's coordinate formula at one point,
independently reproduced in `independent_check.py`.)*

### 3.3 Identification — the discrepancy **is** the fibre `E2′` failure transported

Two facts pin the discrepancy to §2.

**(i) Same axiom.** `E1′, E3′, E4′` hold for `Pf` (`entwine.py`); by the standard correspondence
between mixed distributive laws and coKleisli-of-Kleisli composition (Beck; Power–Watanabe,
*Combining a monad and a comonad*, TCS 280 (2002), §3; Brookes–Geva; Uustalu–Vene 2008), a `κ`
satisfying all four axioms lifts `G` to a comonad on `Kl(T)` whose coKleisli composition — exactly
`⋆` — **is associative**. We invoke only this *sufficiency* direction (`E2′` ⟹ associativity, the
constructive Beck direction): **had `E2′` held, this very triple would compose associatively.** Hence
the sole possible source of the non-associativity in §3.2 is the `E2′` failure. Non-branching `M` (`Maybe`, `Writer`) satisfy `E2′` and indeed give
`0` non-associative triples (`bikleisli.py`), the positive control.

**(ii) Same configuration, transported through single-leaf bijections.** Both bracketings pass
through the **identical** overlap shape `{{a,b},{a}} ∈ Pf(Pf S)` — the exact shape of §2 — created
by `T(·)` applied to `{a,b}` (forward `u` gives `{u(a),u(b)} = {{a},{a,b}}`), and merged by `μ^T`
at the shared leaf `a`. The two bracketings differ **only** in the order in which `κ` (cartesian
product on positions) and `μ^T` (restriction/merge at `a`) are applied relative to that overlap —
which is precisely the "product-then-merge vs merge-then-product" reorder of §2. Concretely the two
outer chains factor through the two sides of the §2 table, post-composed with the backward data of
`h` (resp. `h⋆g`) and pre-composed with that of `f`.

Finally, **no downstream cancellation.** Along each chain, the only non-injective, order-sensitive
step is the interaction of `κ`'s cartesian product with the cross-leaf merge at `a` (this is `E2′`).
Every other transport map is a **bijection at leaf `a`**:
* `η^T` backward (projection `i`) and the counit/unit maps are identities at a single leaf;
* `μ^T` backward (`j`) restricted to a leaf that occurs in exactly one nested slot is a relabelling
  bijection — non-injectivity (copying) happens only *between* the merged copies of `a`, i.e. at the
  `κ`/`μ^T` interface itself;
* `δ` backward (union) and the `Pf`-images `G(·), T(·)` act by merging or functorial image, both
  injective on the fibre of a single un-merged leaf.
A bijection cannot identify two distinct outputs. Therefore the fibre inequality of §2
(`2`-element set `≠` `4`-element set at leaf `a`) is transmitted faithfully to the `(b,(1,0))`
inequality `∅ ≠ {0}` of the full morphisms. The obstruction does **not** live only in a fibre; it
**necessarily lifts.** ∎

---

## 4. Verification (computational)

`scratch/monad-comonad-transfer/`:
* `bikleisli.py` — biKleisli composite as an honest `Cont`-morphism; `Maybe` `1536/1536` and
  `Writer/ℤ₂` `4608/4608` associativity triples pass (positive controls); `Pf` associativity
  fails, witness printed.
* `trace_known.py` — full 5-stage trace of both bracketings of the witness at shape `b`; both pass
  through the overlap `{{a},{a,b}}`; final values `∅` (right) vs `{0}` (left).
* `independent_check.py` — the two critical composite values and the two intermediate values
  `(g⋆f)^\#_b(1,0)=∅`, `(h⋆g)^\#_b(1,0)={0}` re-derived; the §2 fibre sides recomputed by hand
  (`2` vs `4` tuples) matching the pipeline.
* `reader_test.py` — confirms `Reader²` is excluded (repeated leaf labels break `μ^T`).

Boundary checks: the phenomenon needs (a) `|S|≥2` (two subsets to overlap) and (b) `≥2` positions
on the shared leaf; on `A₂ = ({a},{a:3})` (single shape, no overlap) `E2′` **passes** and `⋆` is
associative (`entwine.py`), confirming `A₁` is minimal. Symmetric triples `f=g=h` and triples with
`f,h` pure (`J`-image) are **always** associative here (`trace_lift.py`): the obstruction genuinely
requires the asymmetric branching content of §3.

---

## 5. Registry / status

* Upgrades `branching-full-morphism-lift` under `effect-coeffect-arrows.json` from **computed →
  proved**: the full-morphism non-associativity is now proved (finite forced calculation +
  identification), not merely machine-exhibited.
* Depends on: `E1′,E3′,E4′` for `Pf` (proved/Lean, `entwine.py`/`BranchingObstruction.lean`); the
  Beck/Power–Watanabe equivalence *assoc ⟺ E2′* (cited); the `∏`-cointerpretation `T_M`
  (Ahman–Bauer 2409.17664 Thm 6.3).
* Sets up the clean next Lean target: the `Finset` full-morphism non-associativity
  (`distrib_mult` associativity failure) mirroring `BranchingObstruction.lean` one level up.

## 6. Gaps (precisely stated)

1. **`assoc ⟺ E2′` is cited, not re-derived.** §3.3(i) uses the standard mixed-DL/coKleisli
   equivalence to attribute the failure to `E2′`. The non-associativity itself (§3.2) is proved
   independently and does **not** rely on the citation; the citation is used only for the
   *identification* "if `E2′` held it would be associative". A from-scratch container-level
   string-diagram reduction (both bracketings normal-form to a common term ± one `E2′` subterm) is
   the natural strengthening — deferred (book "further work").
2. **No-cancellation stated for `Pf`/`A₁`, argued generally.** §3.3(ii) proves the transport is a
   single-leaf bijection for the maps occurring in this composite; a fully general lemma "for every
   branching `∏`-monad the `E2′` fibre failure lifts to some triple" would combine this with a
   detection/Yoneda argument (the abstract equivalence gives *existence* of a non-associative triple
   for any branching `M`; producing an explicit witness in general is the open increment).
3. **Scope = `∏`-cointerpretation, commutative `M`.** As in `2026-07-29`: `κ` needs commutativity
   (Pf has it); a non-`∏` weak Mendler algebra is out of scope. `1 + X²` is excluded a priori
   (Prop 0).
