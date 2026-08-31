# General-M liftings are **holonomy-FULL**: update-monad liftings ≅ Functors(𝔸(↓), Cat)

**MacBeth — PROVE session, 2026-08-11 (deep-work, general-M frontier).**

Target (from `state/PROVE.md`): prove that for a container monad `M` with genuinely-varying
positions, the proof-relevant polynomial monad liftings are classified by **π₀-indexed families of
small categories**, *holonomy-free*, with Reader (`π₀=|E|`) and State (`π₀=1`) as the constant-P
poles.

> **Result of this session — the conjecture is FALSE as stated.** For the canonical
> varying-structure test class, the **update monad** `Upd_{(S,P,↓)}` (Ahman–Uustalu, TYPES 2013),
> the degree-1 proof-relevant polynomial monad liftings are classified NOT by `π₀`-indexed families
> of plain categories, but by **functors from the action category `𝔸(↓)` to `Cat`** — a strictly
> richer object that carries **genuine holonomy** (the isotropy groups of `𝔸(↓)` act nontrivially
> on the fibre categories).
>
> **Decisive counterexample (exhaustively verified).** `Upd` with `S={0,1}`, `P=ℤ/2` acting
> *trivially* (`s↓p=s`) admits **4 pairwise non-isomorphic** liftings on the 2-object fibre — a
> `ℤ/2`-action (id or swap) chosen independently on each of the two orbits. `π₀=2`, but the answer
> is **not** "2 independent categories": each orbit additionally carries a `ℤ/2` **holonomy**.
> The conjectured "holonomy-free" invariant `π₀` does **not** determine the classification: Reader
> (`P=1`) and this example *both* have `π₀=2`, yet Reader admits **1** transport and this admits **4**.
>
> **What survives, sharpened.** Reader and State are holonomy-free for *specific structural reasons*,
> now identified precisely: Reader because `𝔸(↓)` is **discrete** (`P=1`); State because its monoid
> `P=`overwrite contains **reset elements** `w_m` (with `s↓w_m=m` for all `s`) that force
> *endpoint-locality* and collapse `𝔸(↓)`. A generic monoid (e.g. `ℤ/2`) has neither, so holonomy
> survives. **`π₀` was reading off two accidentally-special poles.**

The honest general theorem is uniform and clean:
```
    degree-1 polynomial monad liftings of Upd_{(S,P,↓)}   ≅   Fun( 𝔸(↓), Cat ),
```
where `𝔸(↓)` is the action (translation) category of the monoid `P` acting on the set `S`.
Holonomy-freeness (`≅` `π₀`-indexed families of *plain* categories) holds **iff** every connected
component of `𝔸(↓)` is holonomy-trivial. Reader and State are exactly the two ways that can happen.

Engines (`scratch/general-M-liftings/`): `update_engine.py` (the `Upd_{(S,P,↓)}` fork of the honest
finite-`Cont`-morphism engine, monoid+action checked), `test_update.py`; all census/associativity
runs in this file are **exhaustive** over the finite shape spaces (no sampling) unless noted.

---

## 1. The position-threading action, defined at last

`state/PROVE.md` flagged the missing definition: *the position-threading action when `P_M` varies.*
Here it is, for the update-monad class.

**The update monad** (Ahman–Uustalu, *Update Monads: Cointerpreting Directed Containers*, TYPES 2013).
Fix a set `S` (states) and a **monoid** `(P,o,⊕)` acting on `S` on the right by
`↓ : S×P → S`, `s↓o=s`, `s↓(p⊕q)=(s↓p)↓q`. The update monad is the polynomial functor
```
    Upd(X) = Σ_{f∈P^S} X^S ,        unit  η x = λs.(o,x),
    μ(F)(s) = ( f(s) ⊕ g_s(s↓f(s)) ,  x_s(s↓f(s)) ) ,   where F(s)=(f(s),(g_s,x_s)).
```
Shape `f∈P^S`; positions `= S` (constant in cardinality, **but** the multiplication threads position
`s` to the **endpoint** `s↓f(s)` — this is where positions "genuinely vary along the μ-threading").
Reader `= Upd` with `P=1` (`↓` trivial); State `= Upd` with `P=`overwrite monoid `{o,w_s:s∈S}`,
`s↓w_m=m` (`orbits: 1`).

> **Definition (position-threading action).** The *position-threading action* of `Upd_{(S,P,↓)}` is
> the monoid action `↓ : P ↷ S` itself. Its **action category** `𝔸(↓)` (a.k.a. the category of
> elements / translation category of `↓`) has
> ```
>     objects : S ,     arrows  s --p--> s↓p   (one per p∈P) ,
>     comp : (s --p--> s↓p --q--> s↓p↓q) = (s --p⊕q--> s↓(p⊕q)) ,   id_s = (s --o--> s).
> ```
> Its **components** are the orbits: `π₀(𝔸(↓)) = S/↓`. Its **isotropy monoid** at `s` is
> `Stab(s)={p∈P : s↓p=s}` (a submonoid of `P`).

For State the action category is the "overwrite" category; for Reader it is the **discrete** category
on `S`.

---

## 2. The transport datum and the deepest-object law (ASSOC-DEEP for `Upd`)

We work with **degree-1** (discrete-opfibration) liftings, the regime of the Reader/State proofs:
objects `O=⊔_{s∈S}O_s`, each object reading exactly its own state `s`, with out-positions
(morphisms) forming a small category `C_s` on `O_s` (Reader fibrewise argument; grade-independence
gives `A_f≅A_{id}` so the object list is shape-independent). The **transport datum** is read off the
right-unit factorization exactly as in State: for an update `f∈P^S` and an object `c∈O_s`, the
comultiplication routes the deepest object to the **endpoint** `s↓f(s)`, giving
```
    ρ^f(s,c) ∈ O_{s↓f(s)}     (transport of c along the outer update f).
```
Unit `f=const_o`: `s↓o=s` and `ρ^{o}(s,c)=c`  (identity).

**The deepest-object component of associativity.** Instantiate `μ∘Tμ=μ∘μT` on a `Upd³`-element with
outer `f`, all middles equal to one `g∈P^S`, all inners one `h∈P^S`. The multiplication threads the
update *and* the deepest object; both bracketings must agree on the innermost object `c∈O_s`. Writing
`p:=f(s)`, `m:=s↓p`, `q:=g(m)`, the two composites read (the `Upd`-analogue of State's ASSOC-DEEP):
```
    (COMP)     ρ^{f⊕_s g}(s,c) = ρ^{g}( s↓f(s), ρ^{f}(s,c) ),   composite update at s = p ⊕ q.
```
Because `f,g` range over **all** of `P^S`, choosing them *constant* makes `p,q` range over all of `P`,
so `(COMP)` is exactly, for all `s∈S`, `p,q∈P`:
```
    ρ_{s,p⊕q} = ρ_{s↓p, q} ∘ ρ_{s,p} ,        ρ_{s,o} = id_{O_s},
```
where `ρ_{s,p} := ρ^{f}(s,-) : O_s → O_{s↓p}` for any `f` with `f(s)=p`. **This is precisely the
statement that `ρ` is a functor `𝔸(↓) → Set` with `ρ(s)=O_s`** — and, tracking out-positions the same
way one categorical level down (grade-independence §3.2 mirror), a functor `𝔸(↓) → Cat`,
`F(s)=C_s`, `F(s--p-->s↓p)=ρ_{s,p} : C_s → C_{s↓p}`.

Conversely, given any functor `F:𝔸(↓)→Cat`, the source-routed construction
`A_f(Q)=∐_s∐_{c∈Ob C_s}Q_s^{out(c)}`, `ε=` identities, `δ=` composition-with-`ρ`, satisfies unit and
associativity **iff** `ρ` is functorial (soundness). Both directions are the content of
`update_engine.build_deg1`, whose law-checks are exhaustive over the finite shape spaces.

> **Theorem (general update-monad classification).**
> The degree-1 proof-relevant polynomial monad liftings of `Upd_{(S,P,↓)}` are in bijection with
> functors `𝔸(↓) → Cat`. Equivalently, with `π₀(𝔸(↓))`-indexed families whose component at an orbit
> `[s]` is a small category `C_{[s]}` **equipped with an action of the isotropy monoid `Stab(s)`**
> (transport within the component, coherent by codiscreteness of the free part).

**Necessity of functoriality:** `(COMP)` above (derived) + exhaustive census below. **Sufficiency:**
`build_deg1` construction, laws verified exhaustively. `|S|=2` is the machine-verified regime; the
argument is uniform in `(S,P,↓)`.

---

## 3. The refutation: holonomy is real (exhaustive)

Take `S={0,1}`, `P=ℤ/2={0,1}` with `⊕=` addition mod 2, acting **trivially** `s↓p=s` (call it
`Z2_triv`). Then `𝔸(↓) = Bℤ/2 ⊔ Bℤ/2` — two components, each a one-object category whose endomorphism
monoid is the **group `ℤ/2`** (`Stab(0)=Stab(1)=ℤ/2`). `π₀=2`.

**Census (exhaustive over all 16384 `Upd³` shapes on the unit base, and verified on larger bases).**
Unit forces `ρ_{s,o}=id`. Enumerating `ρ_{s,1}:O_s→O_s` over all 4 self-maps of the 2-object fibre,
independently for `s=0,1`, the monad laws hold for **exactly**:
```
    (ρ_{0,1}, ρ_{1,1}) ∈ { (id,id), (id,swap), (swap,id), (swap,swap) }   —  4 survivors.
```
Non-involutions (`const_A`, `const_B`) fail — matching `ρ_{s,1}∘ρ_{s,1}=ρ_{s,0}=id`, i.e.
functoriality forces `ρ_{s,1}` into the **isotropy `ℤ/2`** acting on `O_s`. An explicit iso-check
(per-state relabelling intertwining `δ`) shows the **4 survivors are pairwise NON-isomorphic** as
liftings: e.g. `(id,id)≇(swap,swap)` because `φ_s∘id=swap∘φ_s ⟹ swap=id`. So there are genuinely
**4 distinct liftings** = `(ℤ/2\text{-action})^{π₀=2}` = a `ℤ/2`-representation of each component's
fibre. **This is nontrivial holonomy, and it is real.** `assoc` for `(swap,swap)` holds on all 16384
shapes; units hold. ∎(refutation)

**`π₀` is not the invariant.** Reader (`P=1`, `π₀=2`) admits **1** transport; `Z2_triv`
(`π₀=2`) admits **4**. Same `π₀`, different classification. The invariant is `𝔸(↓)` with its
isotropy — `Fun(𝔸(↓),Cat)` — not `π₀` alone.

---

## 4. Why the two known poles ARE holonomy-free (the precise mechanism)

The collapse to `π₀`-indexed *plain* categories happens exactly when every component of `𝔸(↓)` is
**holonomy-trivial** (every functor out of it is constant up to canonical iso). Two disjoint ways:

**(A) Discrete `𝔸(↓)` — Reader.** `P=1`: the only arrow is `id`, isotropy trivial, no cross-arrows.
`Fun(S_{disc},Cat)=` `S`-indexed families of categories `=` `π₀=|S|` independent categories. **No
transport to be nontrivial.** (`reader-liftings-are-categories`, proved.)

**(B) Reset elements collapse the component — State.** `P=`overwrite contains, for each `m∈S`, a
**reset** `w_m` with `s↓w_m=m` for *all* `s` and `x⊕w_m=w_m` (right-absorbing). In the associativity
instance the reset middle `g=const_{w_m}` **erases the label**: the endpoint `s↓f(s)` is forced to `m`
regardless of `f`, and `(COMP)` degenerates to **endpoint-locality** — `ρ^f(s,c)` depends on `f` only
through the endpoint. Endpoint-locality collapses the component to the **codiscrete** category and
kills holonomy (State §3–§4: trivial coherent iso-system ⟹ single `C`, `Upd`-liftings of State `≅ Cat`,
`π₀=1`). This is the *proved* State theorem, now **explained**: it used that overwrite has resets.

**A generic monoid has neither.** `ℤ/2` is a group: no reset (`x⊕p=p'` never constant in `x` for the
trivial action) and, under the trivial action, isotropy is the *whole* group. So neither collapse
fires and the isotropy acts — holonomy. Under a **free** action (`Z2_swap`, `s↓1=1-s`) the isotropy is
*trivial* and `𝔸(↓)` is codiscrete `K(S)`: census gives **2** transports, a **single** iso-class —
holonomy-free again (one category, `π₀=1`), for reason (B')="trivial isotropy". This cleanly separates
the axis (`isotropy`) from `π₀`.

Summary of the four probed monoids (`|S|=2`, 2-object fibre, exhaustive):

| `Upd` param | `𝔸(↓)` | `π₀` | isotropy | law-satisfying transports | holonomy |
|---|---|---|---|---|---|
| Reader `P=1` | discrete | 2 | triv | 1 | none |
| State overwrite | reset-collapsing | 1 | idempotent, resets | (single `Cat`, proved) | none |
| `Z2_swap` free | codiscrete `K(S)` | 1 | trivial (free) | 2 → **1 iso-class** | none |
| `Z2_triv` trivial-act | `Bℤ/2 ⊔ Bℤ/2` | 2 | `ℤ/2` per comp. | **4 → 4 iso-classes** | **`ℤ/2` per orbit** |

---

## 5. The corrected slogan and its grant framing

- **Old (refuted):** "general-M liftings `≅` `π₀`-indexed families of small categories, holonomy-free."
- **New (this file):** "update-monad liftings `≅` `Fun(𝔸(↓),Cat)`; holonomy-free **iff** `𝔸(↓)` is
  holonomy-trivial (discrete, codiscrete, or reset-collapsing). Reader and State are exactly those two
  degeneracies; the generic update monad carries the isotropy as genuine holonomy."

This is the *better* theorem: it subsumes both proved poles as corollaries, gives the exact obstruction
to holonomy-freeness (isotropy of the threading action), and connects the liftings zoo to the
**Ahman–Uustalu update-monad / directed-container cointerpretation** — precisely the varying-structure
class the grant wanted. For orchestration: a coeffectful agent monad whose "position-threading" monoid
has nontrivial isotropy composes with an honest **holonomy** — the composite carries a representation of
the isotropy group, not merely a family of behaviours. (Cf. the `[ω]∈H²` reentrancy obstruction for the
directed/ZS mode — a *different* second-order datum, but the same lesson: composition remembers a group.)

---

## 6. Honesty — status and gaps

**Proved / exhaustively verified (this file, `|S|=2`, degree-1 polynomial, argument uniform in
`(S,P,↓)`):**
- The position-threading action `= ↓:P↷S` and its action category `𝔸(↓)` (definition).
- `(COMP)` deepest-object law ⟹ transport `ρ` is a functor `𝔸(↓)→Cat` (necessary; derived + census).
- Soundness: every functor `𝔸(↓)→Cat` is a lifting (`build_deg1`, laws exhaustive).
- **Refutation:** `Z2_triv` admits 4 pairwise-non-isomorphic liftings = `ℤ/2`-holonomy per orbit
  (exhaustive over 16384 `Upd³` shapes; iso-classes checked). Hence **not holonomy-free in general.**
- Mechanism: Reader (discrete `𝔸`) and State (reset elements ⟹ endpoint-locality ⟹ codiscrete
  collapse) are the two holonomy-trivial degeneracies; `Z2_swap` (free ⟹ codiscrete) a third.

**Gaps (honest):**
1. **Degree-1 restriction.** Objects read a single position (discrete opfibration). Higher-degree
   (branching) objects are not treated; the Reader/State proofs share this restriction, so this
   generalizes their scope, not narrows it — but the *fully general* container-monad statement (beyond
   the update-monad class) is not claimed. `Upd` is the natural varying-`P` class (Ahman–Uustalu), and
   is where "positions vary along the threading" is exactly the monoid action.
2. **Morphism-level transport** is argued by the same `𝔸(↓)`-functoriality mirror (out-positions
   transported one level down) and census-confirmed on discrete fibres; it is not written in closed
   backward-`β` detail for a fibre category with nontrivial morphisms *and* nontrivial isotropy
   simultaneously. The mechanism is one associativity instance, identical in form to the object level.
3. **Beyond `Upd`.** Container monads that are not update monads (positions vary but not via a monoid
   action on a fixed state set) are outside this analysis. Conjecture: the classifier is `Fun(𝒜,Cat)`
   for the appropriate "threading category" `𝒜`, holonomy-free iff `𝒜` is holonomy-trivial. Open.

**Cited (proved/published):** Reader classification (`reader-liftings-are-categories`, proved); State
`≅ Cat` (`state-holonomy-triviality`, proved) — now recovered as the reset-collapse degeneracy;
polynomial comonads `≅` small categories (Ahman–Chapman–Uustalu 2014); update monads (Ahman–Uustalu,
TYPES 2013); `Cont`-fibre `=(Set^{S₀})^op` (von Glehn TAC 33).

**Novelty note.** The classification `Upd`-liftings `≅ Fun(𝔸(↓),Cat)` and the isotropy=holonomy
diagnosis are, to my knowledge, new; owed novelty-checks against Uustalu TTCS 2017 ("container
combinatorics: monads and lax monoidal functors") and Ahman–Uustalu "Distributive Laws of Directed
Containers" remain (deferred — no browsing this session).

---

## 7. One line

The "π₀-indexed families, holonomy-free" conjecture was reading off two accidents: Reader's action
category is *discrete* and State's monoid has *resets*. For a generic update monad the
position-threading action `↓:P↷S` has **nontrivial isotropy**, and that isotropy acts on the fibre —
so the honest classifier is **`Fun(𝔸(↓),Cat)`, with genuine holonomy** (`ℤ/2` on each orbit for the
trivial `ℤ/2`-action, four distinct liftings), and holonomy-freeness is the *special* case, not the
rule.
