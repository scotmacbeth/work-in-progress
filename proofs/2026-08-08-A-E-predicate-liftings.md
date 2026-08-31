# Neil's two predicate liftings: `A = ∏/All` is a cartesian-only action, `E = Σ/Exists = ◁`

**MacBeth — PROVE session, 2026-08-08 (deep-work).**
Answers Neil's UID-94 note (2026-08-08): his two canonical predicate liftings `All`/`Exists` of a
container are exactly our `∏`/`Σ` liftings, and his two flags —
(1) *"I can't see how to define `A` on polynomial functors"* and
(2) *"`A` acts on `(Cont, E, 1)`: `A X (A Y C) = A (E X Y) C"* — are, respectively, the
object-level restatement of **`T_M`-lifts-⟺-`M`-cartesian** (proved,
`2026-08-07-proof-relevance-boundary.md`) and a clean **dependent-product Fubini** identity making
`A` a right action of the `◁`-monoidal structure `E`. A third, mixed law is computed and shown to
be strict **iff `X` is linear** (a sharper condition than non-branching).

Registry: node `neil-A-E-predicate-liftings` in `proofs/registry/effect-coeffect-arrows.json`,
building on `proof-relevance-boundary` (proved) and `sigma-monad-is-triangle-monoid` (proved).

---

## 0. Headline

> Neil independently wrote down the `∏`/`Σ` predicate liftings (his names `All`/`Exists`) and two
> operations `A X Y = (⟦X⟧S_Y, All X P_Y)` and `E X Y = (⟦X⟧S_Y, Exists X P_Y)` on `Cont`. Then:
>
> **(P1)** `E = ◁` (the composition product) and is a bifunctor on all of `Cont`; **`A` is a
> functor in its *first* argument exactly on cartesian morphisms**, so it does *not* extend to a
> bifunctor on all polynomial functors. The obstruction is a single Yoneda count: a natural
> pushforward `A X Y → A X' Y` along `α=(u,φ)` is a **section of the backward position map `φ`**,
> and the set of such sections is `∏_{p} φ⁻¹(p)` — *empty* if `φ` is not surjective, a *singleton*
> (canonical `= φ⁻¹`) iff `φ` is a bijection. `∏` is contravariant in its index; a container
> morphism reindexes that index the wrong way. This is `T_M`-lifts-⟺-`M`-cartesian, one categorical
> level down (the instance `α = μ_M`).
>
> **(P2)** `A X (A Y C) = A (E X Y) C = A (X ◁ Y) C`, an equality of containers, via
> `∏_p ∏_q = ∏_{(p,q)}` (Fubini) on positions and distributivity + currying on shapes. Hence **`A`
> is a left action / left module of the `◁`-monoidal `(Cont, E, 1)=(Cont,◁,y)` on `Cont`** — object
> law unconditional, unit `A y C = C`; as a *functorial* action it lives on `Cont_cart × Cont` by
> P1. (Dually `E X (E Y C) = E (X◁Y) C` is just `◁`-associativity.)
>
> **(P3)** The mixed interchange `A X (E Y C)` vs `E (A X Y) C` is **not** an equality; the canonical
> comparison is the distributivity (`κ`-entwining) map, an iso **iff every shape of `X` carries
> exactly one position** (`X` *linear*, `⟦X⟧ ≅ S_X × (−)`). This is strictly finer than
> "non-branching (`≤1`)": an empty-position shape breaks it (`Σ_∅ = 0 ≠ 1 = Π_∅`).

---

## 1. Setup — the objects, pinned down

A **container** `X = (S_X, P_X)`: shapes `S_X`, positions `P_X s` for `s∈S_X`; extension
`⟦X⟧Q = Σ_{s:S_X} Q^{P_X s}`. A **morphism** `α=(u,φ):X→X'` is `u:S_X→S_{X'}` (shapes forward)
with `φ_s : P_{X'}(u s) → P_X s` (positions **backward**); `α` is **cartesian** iff every `φ_s` is a
bijection. `Cont ≃ Poly` monoidally, `◁` = functor composition, unit `y=(1,1)`, `⟦y⟧Q=Q`
(`lean-cont-category-done`, `lean-monoidal-coherence-done`).

**Neil's fibration** is `Cont → Set`, `(S,P)↦S`. Its total category *is* `Cont`: an object over `S`
is a family `P:S→Set`, i.e. a container. So a "container-with-predicate" `(Q,T)` is a container
(shapes `Q`, positions `T`), and both liftings are operations `Cont × Cont → Cont`.

**The two predicate liftings of a container `X`** (for a predicate `Y=(S_Y,P_Y)`, evaluated at
`(s,g) ∈ ⟦X⟧S_Y`, i.e. `s:S_X`, `g:P_X s → S_Y`):

```
All    X Y (s,g) = ∏_{p:P_X s} P_Y(g p)      (∏ / "for all positions")
Exists X Y (s,g) = Σ_{p:P_X s} P_Y(g p)      (Σ / "exists position", proof-relevant)
```

**The two bifunctors** (same shapes `Σ_{s} S_Y^{P_X s}`, differing on positions):

```
E X Y = (⟦X⟧S_Y, Exists X P_Y):  positions at (s,g) = Σ_{p:P_X s} P_Y(g p)
A X Y = (⟦X⟧S_Y, All    X P_Y):  positions at (s,g) = ∏_{p:P_X s} P_Y(g p)
```

**`E = ◁`.** For `X◁Y`: shapes `Σ_{s} S_Y^{P_X s}` (an `X`-shape with a `Y`-shape at each
`X`-position), positions at `(s,g)` the sum `Σ_{p:P_X s} P_Y(g p)` (an `X`-position, then a
`Y`-position beneath it). Identical to `E X Y`. ∎ (Sanity-checked, `E=◁`: 1000/1000, §5.)
So `(Cont, E, 1) = (Cont, ◁, y)`, monoidal and Lean-verified.

---

## 2. P1 — `A` is functorial in the first argument iff cartesian

Fix `α=(u,φ):X→X'` and a predicate `Y`. We seek an induced `A X Y → A X' Y` natural in `Y`.

**Shapes (forward).** `(s, g:P_X s→S_Y) ↦ (u s,\; g∘φ_s : P_{X'}(u s)→S_Y)`. Uses `φ_s` backward;
**defined for every `α`.** (Same shape map as for `E=◁`.)

**Positions (backward).** We need
`P_{A X' Y}(u s, g∘φ_s) → P_{A X Y}(s,g)`, i.e.
```
Ψ : ∏_{p':P_{X'}(u s)} P_Y(g φ_s p')  ⟶  ∏_{p:P_X s} P_Y(g p).
```
Abbreviate `P' = P_{X'}(u s)`, `P = P_X s`, `φ = φ_s : P'→P`, and `B := P_Y∘g : P → Set` — an
**arbitrary** family (arbitrary as `Y,g` vary). The left side is `∏_{p'} B(φ p')`. We want a
transformation **natural in `B`** (equivalently in `Y`).

### Lemma 1 (the obstruction is a section set)
`Nat_B( ∏_{p'∈P'} B(φ p'),\; ∏_{p∈P} B(p) ) ≅ ∏_{p∈P} φ⁻¹(p)` = { set-sections `θ:P→P'` of `φ` }.
The transformation attached to a section `θ` is `Ψ_θ(σ)(p) = σ(θ p) ∈ B(φ θ p) = B(p)`.

*Proof.* Work in `Set^P = ∏_{p} Set` (`P` discrete). A natural transformation into a product is a
tuple of natural transformations into the factors:
`Nat(F, ∏_p ev_p) ≅ ∏_p Nat(F, ev_p)`.
The source functor is representable: `∏_{p'} B(φ p') = ∏_{p} B(p)^{|φ⁻¹ p|} = Set^P(D, B)` with
`D(p) = φ⁻¹(p)`. Each `ev_p = Set^P(y^p, -)` with `y^p(x)=[x=p]`. By Yoneda,
`Nat(Set^P(D,-), Set^P(y^p,-)) ≅ Set^P(y^p, D) = D(p) = φ⁻¹(p)`.
Hence `Nat(...) ≅ ∏_p φ⁻¹(p)`. Unwinding the Yoneda iso gives `Ψ_θ(σ)(p)=σ(θ p)`. ∎

### Corollary (P1, the trichotomy)
The natural pushforwards `A X Y → A X' Y` over `α` are indexed by `∏_{s}∏_{p:P_X s} φ_s⁻¹(p)`:
- `φ_s` **not surjective** (some fibre empty) ⟹ the product is **empty**: *no* natural map exists.
  (Witness: `B(p₀)=∅` on the missed `p₀`, `B=1` else; then domain `=1`, codomain `=∅`.)
- `φ_s` **surjective, non-injective** ⟹ product has `≥2` elements: maps exist but **none is
  canonical/unique**.
- `φ_s` **bijective** (all `s`: `α` cartesian) ⟹ product is a **singleton**, the section is forced
  `θ_s = φ_s⁻¹`.

Only in the cartesian case is the lift **canonical** (choice-free, determined by the data), and then
it is functorial: `id ↦ id` (`φ=id ⟹ θ=id`) and composites compose (`(φ_2∘φ_1)⁻¹ = φ_1⁻¹∘φ_2⁻¹`).
Therefore

> **`A` extends canonically to a bifunctor `Cont_cart × Cont → Cont`, and there is no canonical
> (choice-free, determined-by-the-data) extension to any non-cartesian morphism.** In particular `A`
> does *not* extend to a bifunctor on all polynomial functors — and this failure is not mere
> non-canonicity but genuine non-existence: along any morphism with a **non-surjective** `φ_s`
> *no* natural pushforward exists at all (§2 witness). (The precise link to "`μ` drops leaves" for
> a monad multiplication `α=μ_M` is the boundary file's forward-totality analysis, §2.2.)

(Whether some *choice* of sections could make `A` functorial on a wider — necessarily
choice-dependent, non-canonical — subcategory containing surjective-non-injective morphisms I do not
settle; it is irrelevant to Neil's flag, which is about the canonical/polynomial-functor extension.
The decisive obstruction for "all polynomial functors" is the non-surjective case, where existence
itself fails.)

*Verified:* the section count `∏_p|φ⁻¹(p)|` matches "exists ⟺ surjective, unique ⟺ bijective" on
3000 random backward maps, edge cases (`P` or `P'` empty) included (§5).

### 2.1 Why `E` is fine and `A` is not — and the second argument
For `E=◁`, the position map is on **sums**: `Σ_{p'}B(φ p') → Σ_p B(p)`, `(p',b)↦(φ p',b)` — defined
for **every** backward `φ` (`Σ` pushes forward covariantly *along* `φ`). `A` would need `φ⁻¹`, since
`∏` is **contravariant in its index set**. That single variance flip is Neil's flag (1).

In the **second** argument `A` is functorial for *all* morphisms: for `β=(v,ρ):Y→Y'`,
`A X Y → A X Y'` has shapes `(s,g)↦(s,v∘g)` and positions
`τ ↦ (p ↦ ρ_{g p}(τ_p))` — `ρ` acts **inside each factor, pointwise**, always defined. The
asymmetry is the whole point:

> **1st argument `φ` reindexes the `∏`'s index set (⟹ needs `φ⁻¹` ⟹ cartesian); 2nd argument `ρ`
> acts within each factor (pointwise ⟹ always fine).**

### 2.2 This is `T_M`-lifts-⟺-`M`-cartesian, one level down
`A = All = ∏ = T_M` (Ahman–Bauer's proof-relevant `∏`-lifting). Take the first argument to be a
monad-multiplication `α = μ_M : M◁M → M`. P1 says the pushforward exists-and-is-canonical iff `μ_M`
is cartesian — exactly the boundary of `2026-08-07-proof-relevance-boundary.md` (node
`proof-relevance-boundary`, proved) and its Maybe/Pf Lean instance (`lean-tm-cartesian-boundary-done`).
Neil's functoriality flag and our multiplication-drop are **one statement**: `∏` has no canonical
pushforward along a non-cartesian backward map. The Yoneda count `∏_p φ⁻¹(p)` is the fine form of
that boundary's "forward-total" condition read at a single morphism.

---

## 3. P2 — `A X (A Y C) = A (X ◁ Y) C`: the module action

Let `X=(S_X,P_X)`, `Y=(S_Y,P_Y)`, `C=(S_C,P_C)`; write `p:P_X s`, `q:P_Y(–)`.

**LHS `A X (A Y C)`.** Inner `W := A Y C`: `S_W = Σ_{t}S_C^{P_Y t}`, `P_W(t,h)=∏_{q:P_Y t}P_C(h q)`.
Then `A X W`:
- shapes: `(s,k)`, `k:P_X s→S_W`, `k(p)=(t_p,h_p)`, `t_p:S_Y`, `h_p:P_Y t_p→S_C`;
- positions: `∏_{p:P_X s} P_W(k p) = ∏_{p} ∏_{q:P_Y t_p} P_C(h_p q)`.

**RHS `A (X◁Y) C`.** Inner `Z := X◁Y`: `S_Z=Σ_s S_Y^{P_X s}`, `P_Z(s,g)=Σ_{p}P_Y(g p)`. Then `A Z C`:
- shapes: `((s,g),m)`, `g:P_X s→S_Y`, `m:(Σ_{p}P_Y(g p))→S_C`;
- positions: `∏_{r:Σ_p P_Y(g p)} P_C(m r) = ∏_{p}∏_{q:P_Y(g p)} P_C(m(p,q))`.

**Shape iso** (distributivity of `∏` over `Σ` = type-theoretic axiom of choice, then currying):
```
∏_{p}(Σ_{t}S_C^{P_Y t})  ≅  Σ_{g:S_Y^{P_X s}} ∏_{p} S_C^{P_Y(g p)}  ≅  Σ_{g} S_C^{Σ_p P_Y(g p)},
```
sending `(t_p,h_p)_p ↦ (g:=(p↦t_p),\; m:=((p,q)↦h_p q))`, a bijection. Under it the two shape sets
coincide.

**Positions match on the nose.** Along the shape iso `h_p q = m(p,q)`, so
`∏_p ∏_q P_C(h_p q) = ∏_p ∏_{q:P_Y(g p)} P_C(m(p,q)) ≅ ∏_{(p,q):Σ_p P_Y(g p)} P_C(m(p,q))` by Fubini
`∏_p ∏_q = ∏_{(p,q)}`. This is precisely the RHS position set.

Hence **`A X (A Y C) ≅ A (X◁Y) C`**, natural in `C` (and in cartesian `X,Y`). *Verified:* 2000/2000
random small containers, both shape- and position-counts (§5).

### 3.1 What this is: a right action of `(Cont, ◁, y)`
Define `X • C := A X C`. P2 is the associativity axiom `X•(Y•C) = (X◁Y)•C`; the unit is
`A y C = C` (`y=(1,!)`, `P_y(*)=1`: shapes `S_C^1≅S_C`, positions `∏_{p:1}P_C(c)=P_C(c)`). So:

> **`A` is a left action (left module) of the `◁`-monoidal category `(Cont,◁,y)=(Cont,E,1)` on
> `Cont`.** The *object-level* action law is unconditional; as a *functorial* action it is an action
> of `Cont_cart` (P1). Dually `E X (E Y C)=E (X◁Y) C` is just `◁`-associativity
> (`lean-monoidal-coherence-done`) — stated for contrast: `E` acts by its *own* monoidal structure,
> `A` acts *alongside* it but only cartesian-functorially.

### 3.2 Strict, and base-monad-free — contrast with Orestis's oplax `⊆`
P2 is an **equality/iso of container objects**, base-monad-free: pure `∏_p∏_q=∏_{(p,q)}` Fubini.
This is a *different layer* from Orestis's `Λ-join : Λ P ∘ join ⊆ Λ(Λ P)`
(`peers/orestis/Effects/PredicateLiftings.agda:19`), which is the interaction of `All` with a **base
monad's `join`** — an oplax `⊆`, not a strict equation. The meta-pattern's pre-logged finer
distinction: **the pure composition law is strict (P2); once a base monad's multiplication enters,
it degrades to Orestis's oplax `⊆`** (that is the `T_M`-monad boundary of §2.2 again — the base
`μ` must be cartesian for `⊆` to become `=`).

---

## 4. P3 — the mixed law is not strict; iso ⟺ `X` linear

Compute both mixed composites.

`A X (E Y C)`: shapes `≅ Σ_s Σ_{g:S_Y^{P_X s}} S_C^{Σ_p P_Y(g p)}`; positions `∏_{p} Σ_{q} P_C`.
`E (A X Y) C = (A X Y)◁C`: shapes `Σ_s Σ_{g} S_C^{∏_p P_Y(g p)}`; positions `Σ_{r:∏_p P_Y(g p)} P_C(m r)`.

The `S_C`-exponents differ: `Σ_p P_Y(g p)` vs `∏_p P_Y(g p)`. So **no strict interchange**. The
canonical comparison is the distributivity map `∏_p Σ_q ⟶ Σ_{choice} ∏_p` (the `κ:GT⇒TG` entwining,
`two-feeds-entwine-one-direction`, `effect-coeffect-arrows`). It is an **iso iff `Σ_p = ∏_p` over
`P_X s` for every `s`**, i.e.

> **iff `|P_X s| = 1` for every shape `s` — `X` *linear*, `⟦X⟧ ≅ S_X × (−)`.**

This is **strictly finer than non-branching (`|P_X s|≤1`)**: an empty-position shape breaks it,
`Σ_∅=0 ≠ 1=Π_∅` (so `S_C^0=1 ≠ S_C=S_C^1`). *Verified* (§5): `X=[1],[1,1],[1,1,1]` give equality
over 400 trials each; `X=[0],[1,0],[2]` fail. The mixed law is where `∏` and `Σ` genuinely refuse to
commute — the same branching gap that obstructs the arrow-category composition.

---

## 5. Verification (computational)

`scratch/prove-A-E-verify.py` (containers as position-count lists, composites built explicitly):
- `E = ◁` (sanity): **1000/1000**.
- units `A y C = C`, `E y C = C`: **500/500** each.
- **P2** `A X(A Y C) = A(X◁Y)C` (shape- & position-multiset): **2000/2000**.
- **P1** section count `∏_p|φ⁻¹(p)|` vs "exists⟺surjective, unique⟺bijective": **3000/3000**,
  empty-`P`/`P'` edges included.
- **P3**: iso exactly for linear `X` (`[1],[1,1],[1,1,1]` pass; `[0],[1,0],[2]` fail).

The symbolic proofs (§2 Yoneda, §3 Fubini) make the finite checks conclusive: P1's count is the
representable Yoneda formula for all finite `φ`; P2's iso is `∏_p∏_q=∏_{(p,q)}` for all containers.

---

## 6. One line

`E = Σ = ◁` is a bifunctor by covariant push-forward on sums; `A = ∏ = All` is a **cartesian-only**
action of `◁` on `Cont`, because `∏` is contravariant in its index and so has a canonical
push-forward `∏_p φ⁻¹(p)` only when `φ` is a bijection — that is `T_M`-lifts-⟺-`M`-cartesian one
level down; the action law `A X(A Y C)=A(X◁Y)C` is dependent-product Fubini, strict and
base-monad-free, while `A/E` interchange is strict only for linear `X`.

---

## 7. Honesty — status and gaps

- **Proved (this file):** P1 (Lemma 1 + trichotomy, Yoneda, computationally corroborated); P2 (Fubini
  + AC/currying iso, corroborated); P3's exact iso condition (`X` linear).
- **Cited (proved elsewhere):** `E=◁` monoidal & Lean'd; `A=T_M` boundary `T_M`-lifts-⟺-cartesian
  (`proof-relevance-boundary`); `E=Σ=M◁−` (`sigma-monad-is-triangle-monoid`).
- **Strictness caveat:** P2 is stated as a canonical iso; whether it is a *definitional* equality
  (`=`, as Neil wrote) or a coherent iso depends on the encoding. In the Lean encoding where `◁`'s
  pentagon/triangle are `rfl` (`lean-monoidal-coherence-done`), the same currying/Fubini normal forms
  should make the `A`-associator `rfl` too — a natural next LEAN rung (not yet done; flagged, not
  claimed).
- **Coherence of the action not fully checked:** I proved the associativity (P2) and unit
  (`A y C=C`) equations at the object level, but did **not** verify the module *pentagon* and
  *triangle* coherence 2-cells (associator/unitor compatibility). For a strict/`rfl` encoding these
  are automatic; for a bicategorical statement they remain to check. Flagged as `computed`→`proved`
  for the two equations, coherence `speculative`.
