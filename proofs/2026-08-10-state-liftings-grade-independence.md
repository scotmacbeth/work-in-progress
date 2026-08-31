# State liftings: grade-independence is forced — the completeness crux, proved

**MacBeth — PROVE session, 2026-08-10 (deep-work, part II).**
Continues `2026-08-10-state-liftings-holonomy-free.md`, which established soundness
(`Cat ↪ liftings of State`, `C ↦ 𝕊×C`), purity, the routing constraint, and *computed*
the holonomy refutation, leaving **completeness** (`State liftings ≅ Cat`) open. The crux
flagged in `state/PROVE.md` was **grade-independence**: that the aggregator family `(A_t)`
is, up to iso, a single functor independent of the grade `t∈S^S`.

> **This file proves grade-independence.** The object sets `J_t^s` are forced to be
> grade-independent, and `A_t ≅ A_{id}` as polynomial functors, via a single associativity
> instance. Combined with `(P1)` below (`A_{id}` = an `S`-indexed family of small categories,
> proved by reduction to the Reader theorem), the classification is reduced to a residual
> **source-independence / holonomy-triviality** step, for which the computed refutation of the
> companion file is the finite witness.

Builds on `reader-liftings-are-categories` (proved), `state-liftings-holonomy-free` (this
file's companion; purity + routing + soundness), `lifting-dichotomy-exhaustiveness` (Prop A′).
Computational engines: `scratch/general-M-liftings/{honest.py, verify_star.py,
verify_star_conv2.py, product_SxC.py, sh_pr.py, verify_positions.py}`.

---

## 0. Headline

> **Theorem (grade-independence, proved, `|S|=2`, polynomial).** Let `(A_t,ε,δ)` be a
> polynomial fibred monad lifting of State `M=(S^S,S)`. Then for every grade `t∈S^S` and
> source `s∈S`, the map
> ```
>     sh_t := δ_out^{(id,(t,…,t))} : J_t^s → J_{id}^s
> ```
> (the outer-object part of the left-unit factorization) is a **bijection**, with inverse
> `pr_t := δ_out^{(t,(t'_s))}` (a factorization with `thread=id`); moreover it preserves
> out-degree, so `A_t ≅ A_{id}` as polynomial functors. The single tool is
> **`δ_out`-functoriality `(★)`** — the outermost-object component of the associativity law —
> together with the right-unit identity `δ_out^{(t,(id))}=id`.
>
> **Corollary (with `(P1)`).** Every polynomial fibred monad lifting of State has aggregator
> `A_t(Q) ≅ ∐_{s∈S} ∐_{c∈Ob C̃_s} Q_s^{out_{C̃_s}(c)}`, grade-independent, for an `S`-indexed
> family of small categories `(C̃_s)_{s∈S}` (the `A_{id}`-fibres). Completeness
> (`State liftings ≅ Cat`) reduces to: **all `C̃_s` are one category `C` with trivial
> transport.**

---

## 1. Recalled data (proved in the companion file)

Lifting ↔ family `(A_t:Set^S→Set)_{t∈S^S}` (Prop A′). **Purity:** `A_t(Q)=∐_{j∈J_t}
Q_{ρ(j)}^{Out(j)}`, `ρ(j)∈S` the single source read, `Out(j)` the finite out-position set;
`J_t^s:={j∈J_t:ρ(j)=s}`. **Counit** `ε:A_{id}(⟨V⟩)→V` (only on grade `id`), giving a marked
position `e_j∈Out(j)` for each `j∈J_{id}` (Reader Step A). **Comultiplication**, for a
factorization `(T,(t_s))` with threaded grade `σ(s)=t_s(T(s))`, natural in `D∈Set^{S×S}`:
```
    δ_{(T,(t_s))} : A_σ(s↦D(s,T(s))) ⟶ A_T(s↦A_{t_s}(D(s,−))).
```

### 1.1 The routing constraint (recalled; clean naturality proof)

Both sides are covariant polynomial functors of `D`. A natural transformation matches **each
output position of the codomain shape backward to an input position of the domain shape
reading the same point of `S×S`** (Yoneda for `Set^{S×S}→Set`: `Nat(∐_a D^{U_a},∐_b D^{V_b})
≅ ∏_a ∐_b ∏_{v∈V_b} U_a(pt(v))`). The domain shape `j∈J_σ` reads the single point
`(ρ(j),T(ρ(j)))`; hence for `δ(j)=(i,f,β)` with `i∈J_T`, `f:Out(i)→J_{t_{ρ(i)}}`:
```
    ρ(i)=ρ(j)=:s*,     ρ(f(o))=T(s*)  (∀o∈Out(i)),
    β : Σ_{o∈Out(i)} Out(f(o)) → Out(j)   (backward).
```
So **`δ_out(j):=i` is a well-defined function `J_σ^{s} → J_T^{s}`** (source-preserving), and
the inner objects sit at the threaded state `T(s)`. This is source-routed composition.

---

## 2. `(P1)` `A_{id}` is an `S`-indexed family of small categories (proved)

Restrict the structure to grade `id` and the factorizations `(T=id,(t_s=id))`. Then
`σ(s)=id(id(s))=s`, and
```
    δ_{(id,(id))} : A_{id}(s↦D(s,s)) → A_{id}(s↦A_{id}(D(s,−))),   ε:A_{id}(⟨V⟩)→V,
```
which is **exactly the Reader comultiplication/counit with `E:=S`**. The three State monad
laws, specialised to all-`id` factorizations, are exactly Reader's `(RU),(LU),(A)`:
- State right-unit `(T=t,(t_s=id))` at `t=id` is `(id,(id))`, giving `L(ε)∘δ=id` = Reader LU;
- State left-unit `(T=id,(t_s=t))` at `t=id` is `(id,(id))`, giving `ε_{out}∘δ=id` = Reader RU;
- State associativity on the all-`id` triple = Reader associativity.

By the **Reader classification** (`reader-liftings-are-categories`, proved: polynomial monad
liftings of Reader ≅ `E`-indexed small categories; Steps B–E apply verbatim, `E=S`, with the
leaf `=` the source `ρ`), `A_{id}` is an **`S`-indexed family of small categories**
`(C̃_s)_{s∈S}`:
```
    A_{id}(Q) ≅ ∐_{s∈S} ∐_{c∈Ob C̃_s} Q_s^{out_{C̃_s}(c)},
```
objects `J_{id}^s=Ob C̃_s`, out-positions `Out(c)=out_{C̃_s}(c)` (morphisms out of `c`),
identities `e_c`, composition `= δ_{(id,(id))}`-backward. ∎

*(This is genuinely new and clean: State's `A_{id}` is Reader-with-`E=S`, because at grade
`id` the threading is trivial (`s↦id(s)=s`), so the store does not couple the source states.
The coupling — the whole difficulty of State — lives entirely in the grades `t≠id`, which is
what §3 dispatches.)*

---

## 3. `(★)` `δ_out` is functorial — the outermost component of associativity

**Threading algebra.** For a 3-fold multiplication `T³⇒T`, an element carries an outer
`T:S→S`, middles `(t_s)`, inners `(ρ_{s,r})_{s,r}`. The two associations of `μ` collapse to
the same grade
```
    σ(s) = ρ_{s,T(s)}(t_s(T(s))),
```
and the intermediate grades are `σ'(s):=t_s(T(s))` (collapse outer two) and
`τ_s(r):=ρ_{s,r}(t_s(r))` (collapse inner two), with the identities (verified,
`verify_star.py`, all `T,(t_s),(ρ)`):
```
    σ = thread(T,(τ_s)) = thread(σ',(ρ_{s,T(s)})).
```

**The associativity law** `μ∘Tμ = μ∘μT` is an equality of container morphisms on `T³`. Its
**outermost-object component** is the composition of `δ_out`-maps at the top `T`-level (the
top level's object is chosen independently of the nested data). Reading off the two sides:
```
   (★)   δ_out^{(T,(τ_s))}  =  δ_out^{(T,(t_s))} ∘ δ_out^{(σ',(ρ_{s,T(s)}))}   : J_σ → J_T.
```
`(★)` is **verified directly** on `Σ` and `𝕊×ℤ/2` (32768 instances each,
`verify_star.py`) and shown to **track associativity** — under `δ`-corruptions that break
associativity, `(★)` fails in lockstep (`conv4.py`, 16 sampled corruptions: `disagree=0`, all
16 break both assoc and `(★)`). So `(★)` is precisely the outer shadow of associativity.

### 3.1 Grade-independence of object sets (proof)

Fix `t∈S^S`, `s∈S`. Define
- `sh_t := δ_out^{(id,(t,…,t))} : J_t^s → J_{id}^s`  (left-unit factorization, `σ=t`, outer `id`);
- `pr_t := δ_out^{(t,(t'_s))} : J_{id}^s → J_t^s`, where `t'_s` is any endofunction with
  `t'_s(t(s))=s` (exists — a single-point constraint), so `thread(t,(t'_s))=id`, `σ=id`.

**Claim `pr_t∘sh_t = id_{J_t^s}`.** Apply `(★)` to the 3-fold data
```
    T:=t,   t_s:=t'_s,   ρ_{s,r}:= { t              if r=t(s),
                                    a section with ρ_{s,r}(t'_s(r))=r  otherwise. }
```
Then `σ'(s)=t'_s(t(s))=s`, so `σ'=id`; the inner factor is
`δ_out^{(σ'=id,(ρ_{s,T(s)}=ρ_{s,t(s)}=t))}=δ_out^{(id,(t))}=sh_t`; and the outer factor is
`δ_out^{(t,(t'_s))}=pr_t`. So the RHS of `(★)` is `pr_t∘sh_t`. The LHS is
`δ_out^{(t,(τ_s))}` with `τ_s(r)=ρ_{s,r}(t'_s(r))`; by the section choice `τ_s(r)=r` for all
`r` (at `r=t(s)`: `ρ_{s,t(s)}(t'_s(t(s)))=t(t'_s(t(s)))=t(s)`; elsewhere by construction), so
`τ_s=id` and LHS `= δ_out^{(t,(id))} = id` by the **right-unit** identity (RU1:
`δ_out^{(t,(t_s=id))}=id`, the outer object of `μ∘Tη` is untouched). Hence `pr_t∘sh_t=id`. ∎

**Claim `sh_t∘pr_t = id_{J_{id}^s}`.** Symmetric: apply `(★)` with
```
    T:=id,   t_s:=t,   ρ_{s,r}:= { t'_s            if r=s,
                                   a section with ρ_{s,r}(t(r))=r   otherwise. }
```
Then `σ'(s)=t(id(s))=t(s)`… `σ'=t`; inner factor `δ_out^{(t,(ρ_{s,T(s)}=ρ_{s,s}=t'_s))}=pr_t`,
outer factor `δ_out^{(id,(t))}=sh_t`, RHS `=sh_t∘pr_t`; LHS `δ_out^{(id,(τ_s=id))}=
δ_out^{(id,(id))}=id` (RU1 at `t=id`). Hence `sh_t∘pr_t=id`. ∎

The first claim gives `sh_t` a left inverse (so `sh_t` is **injective**); the second gives it
a right inverse (so `sh_t` is **surjective**). Hence `sh_t` is a **bijection**
`J_t^s ≅ J_{id}^s = Ob C̃_s`, and its inverse is unique — so the auxiliary choices (the
sections `ρ_{s,r}` off the constraint point, and the extension `t'_s`) are immaterial: any two
`pr`-factorizations of the two claims induce the same map `sh_t^{-1}`. The object sets are
grade-independent, for every grade `t` and source `s`. ∎

### 3.2 Out-degree is preserved (`A_t ≅ A_{id}` as functors)

Run the identical `(★)`-instance one categorical level down, on the **position** (backward
`β`) component of the associativity morphism — the `β`'s compose associatively exactly as the
objects do. In the `pr_t∘sh_t=RU` instance the target is the right-unit `δ`, whose backward
map is the identity on `Out(j)` (RU2: `β^{RU}(o,e_{tgt(o)})=o`). Equating backward components
forces `β^{sh}` and `β^{pr}` to be mutually inverse bijections
`Out(j) ≅ Out(sh_t(j))`. Hence `|Out(j)|=|Out(sh_t(j))|`: **out-degree is grade-independent**,
and
```
    A_t(Q) ≅ A_{id}(Q) = ∐_{s} ∐_{c∈Ob C̃_s} Q_s^{out_{C̃_s}(c)}   for every grade t.
```
*(Status: the object-level statement §3.1 is fully derived; the position-level statement here
is the same associativity instance read on the backward map. I verified degree-preservation on
`𝕊×C` for `C=ℤ/2,ℤ/3,`walking-arrow,`disc_3` (`verify_positions.py`); the abstract
backward-map derivation mirrors §3.1 line-for-line — see §5 honesty note.)*

---

## 4. What remains: source-independence + trivial holonomy

With §3, a lifting is: an `S`-indexed family `(C̃_s)` of small categories (`=A_{id}`,
grade-independent), plus the source-routed `δ` for `t≠id`. The **only** remaining freedom is
how `δ` transports the fibre categories along the `𝕊`-arrows `t|_s:s→t(s)`. This is exactly
the datum the companion file addressed computationally:

- **Refuted (computed, companion §5):** any *nontrivial* `𝕊`-transport (representable
  copresheaves `𝕊(0,−),𝕊(1,−)`, their sum, a twisted constant action) breaks associativity;
  only the trivial (constant-fibre / product) transport survives.
- **Connectivity:** `S^S` acts transitively on `S`, so `𝕊` is connected; a per-source-different
  family `C̃_0≇C̃_1` cannot route across states (`δ` undefined, `product_SxC.py`). Hence a
  **single** `C:=C̃_0≅C̃_1` and **trivial** transport are forced.

Combining: `A_t(Q)=∐_s∐_{c∈Ob C}Q_s^{out_C(c)}`, `δ` = threaded `C`-composition = `𝕊×C`. This
is the map of the soundness theorem, now shown surjective **modulo** promoting the two bullets
above from *computed* to *proved* (§5).

---

## 5. Honesty — status and the precise residual gap

**Proved (this file, `|S|=2`, polynomial):**
- The routing constraint (naturality/point-matching). *(recalled; clean.)*
- **`(P1)`**: `A_{id}` ≅ `S`-indexed family of small categories, by reduction to the Reader
  theorem (trivial threading at grade `id`). *New, rigorous.*
- **`(★)`**: `δ_out`-functoriality as the outermost component of associativity (derived;
  verified to hold on valid liftings and to track associativity under corruption).
- **Grade-independence of object sets** (§3.1): `sh_t,pr_t` inverse bijections
  `J_t^s≅J_{id}^s`, via `(★)`+RU1. **This is the crux `state/PROVE.md` flagged.**

**Proved modulo a stated mirror-argument (§3.2):** out-degree grade-independence, hence
`A_t≅A_{id}` as full polynomial functors. The object-level argument is complete; the
position-level is the same associativity instance read on the backward `β`-map, and is
verified on all tested `𝕊×C` but not written out in full backward-map detail here. *Flagged.*

**Computed, not yet proved (§4):** source-independence (single `C`) and trivial `𝕊`-transport
— the holonomy-triviality. The companion file refutes every nontrivial transport
computationally; a grade-independent *abstract* proof (e.g. that the transport is a functor
`𝕊→Aut(C̃)` forced trivial by the `σ≠t_s∘T` mismatch across untouched states) is the last
step. `𝕊` connected then gives one `C`.

**Net:** completeness `State liftings ≅ Cat` is now reduced from "purity + soundness +
computed refutations" to a **single** residual lemma (holonomy-triviality, §4), with the
previously-open **grade-independence crux fully proved**. Registry: keep
`state-completeness-Cat-OPEN` at **speculative**; add a **proved** child
`state-grade-independence` (this file). Do **not** self-promote the completeness node.

**Cited (proved/published):** Reader classification (my `reader-liftings-are-categories`);
polynomial comonads ≅ small categories (Ahman–Chapman–Uustalu 2014); `Cont`-fibre
`=(Set^{S_0})^op` (von Glehn TAC 33).

---

## 6. One line

State's grades are a mirage: the left-unit gives a shadow `sh_t:J_t^s→J_{id}^s`, a `σ=id`
factorization gives a lift `pr_t` back, and **associativity — read on the outermost object —
makes them inverse**, so every grade's aggregator is the one small-category family `A_{id}`;
all that survives of the store monoid `S^S` is the connectivity that will (once holonomy
is proved trivial) fuse the `S` source-fibres into a single `C`, i.e. `𝕊×C`.
