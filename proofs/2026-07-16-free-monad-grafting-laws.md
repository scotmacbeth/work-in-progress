# The free monad on a container as a `◁`-monoid: the grafting-monoid laws in container coordinates

**MacBeth — 2026-07-16**

## Provenance and what is (and is not) claimed

The *construction* of the free monad on a polynomial endofunctor — positions = trees,
directions = **leaves**, multiplication = grafting — is **prior art**:

> **Gambino–Kock, "Polynomial functors and polynomial monads", arXiv:0906.4931, Theorem 4.5
> (2009):** the free monad on a polynomial endofunctor is a polynomial monad, in any locally
> cartesian closed category with W-types.

Gambino–Kock construct the carrier and the unit/multiplication and then state that the monad
laws are *"lengthy but routine"* and **omit the verification** (pp. 30–31). The single-variable
case is **Gambino–Hyland, TYPES 2003**; the finitary/Set case is **Kock, arXiv:0807.2874**; the
container-side W-type technology is **Abbott–Altenkirch–Ghani, ICALP 2004**.

**This note does not claim the construction and does not claim a new theorem.** Its entire content
is *spelling out the omitted calculation*: I write the three monoid laws of the free monad as
explicit **container-coordinate** equations — a forward map on shapes and a backward map on
positions for each — and prove them by structural induction. This is the monoid mirror of my
comonoid work M2b/M3b (directed container ⇔ `◁`-comonoid), and it is the paper-level companion to
the intended Lean formalisation, where these coordinate laws become the proof obligations.

Everything below is checked computationally in `scratch/free_monad_*.py` (6 containers, trees up
to 3 internal nodes, **all** labellings; leaf-bijection verified; two negative controls fire).

**Neighbours (checked, none a scoop of this note's stated scope).** That a *monoid* in the
substitution-monoidal category `(Cont, ◁, I)` is exactly a monad on `⟦m⟧` is standard (it is the
definition of the substitution product); for the indexed generalisation, **De Pascalis–Uustalu–
Veltri, arXiv:2509.25879** prove "a monoid in `(I-Cont, ◁, y)` = a monad on `Set^I`" — but as a
*characterisation*, not an explicit grafting-law derivation. **Aberle, arXiv:2604.01303** *uses*
the free monad on `Poly` (an ordinary `return`/`bind` AST) as an ingredient for program
verification in Agda, but does **not** formalise G-K's "positions = trees, directions = leaves,
`μ` = grafting" isomorphism or its monoid laws — so the intended **Lean** formalisation of this
note remains genuinely un-done in the literature.

---

## 1. Coordinates

A **container** `p = (S ◁ P)` is a set `S` of shapes together with a family `P : S → Set` of
positions; its extension is the polynomial endofunctor `⟦S◁P⟧(X) = Σ_{s:S} (P(s) → X)`.

**Composition product.** For `G = (T ◁ Q)` and `F = (S ◁ P)`, the composite `G ◁ F`
("`G` outside, `F` inside") is
```
(G ◁ F).Shape   = Σ_{t:T} (Q(t) → S)
(G ◁ F).Pos(t,f)= Σ_{q:Q(t)} P(f q)                      ⟦G ◁ F⟧ = ⟦G⟧ ∘ ⟦F⟧.
```
Its unit is the identity container `I = (1 ◁ λ_.1)`, `⟦I⟧ = Id`.

**Morphisms.** A container morphism `φ : (S◁P) ⇒ (S'◁P')` is a forward shape map
`φ₁ : S → S'` and a **backward** position map `φ♯_s : P'(φ₁ s) → P(s)`; it represents a natural
transformation `⟦S◁P⟧ ⇒ ⟦S'◁P'⟧`. Identities are `(id, id)`; composition of `φ : C⇒D` then
`ψ : D⇒E` is `(ψ₁∘φ₁, s ↦ φ♯_s ∘ ψ♯_{φ₁ s})` (forward composes forward, backward composes
backward). The horizontal (tensor) composite `φ ◁ ψ : a◁c ⇒ b◁d` of `φ:(A◁P_A)⇒(B◁P_B)` and
`ψ:(C◁P_C)⇒(D◁P_D)` is
```
(φ ◁ ψ)₁ (a, g)      = (φ₁ a,  ψ₁ ∘ g ∘ φ♯_a),          g : P_A(a) → C
(φ ◁ ψ)♯_{(a,g)}(j,k)= (φ♯_a j,  ψ♯_{g(φ♯_a j)} k),      j : P_B(φ₁ a), k : P_D(ψ₁(g(φ♯_a j))).
```
The unitors and associator of `(Cont, ◁, I)` are (matching `Composition.lean`):
```
λ_F : I◁F ≅ F        hom₁(*,g) = g(*),        hom♯(p) = (*, p)
ρ_F : F◁I ≅ F        hom₁(s,g) = s,           hom♯(p) = (p, *)
a    : (H◁G)◁F ≅ H◁(G◁F)   hom₁((a,g),k) = (a, u↦(g u, v↦k(u,v))),  hom♯(u,v,p) = ((u,v),p).
```
A **monoid** in `(Cont, ◁, I)` is `(m, μ, η)` with `μ : m◁m ⇒ m`, `η : I ⇒ m`, satisfying (in
diagrammatic order, `;` = "then")
```
(FM-unitL)  (η ◁ m) ; μ  = λ_m       : I◁m ⇒ m
(FM-unitR)  (m ◁ η) ; μ  = ρ_m       : m◁I ⇒ m
(FM-assoc)  (μ ◁ m) ; μ  = a ; (m ◁ μ) ; μ    : (m◁m)◁m ⇒ m.
```
Equivalently, `⟦m⟧` is a monad (unit `⟦η⟧`, multiplication `⟦μ⟧`). This is the **mirror** of a
directed container = `◁`-comonoid, `δ : m ⇒ m◁m` running the opposite way (§M3).

## 2. The carrier (Gambino–Kock 4.5 in coordinates)

Fix `(S ◁ P)`. Let `Tr(X)` be the initial algebra of `Y ↦ X + Σ_{s:S}(P(s) → Y)` — the
well-founded `P`-trees with leaves labelled in `X` — with constructors
```
lf : X → Tr(X)                              (a leaf carrying a label)
nd : (Σ_{s:S}(P(s) → Tr(X))) → Tr(X)        (a node of shape s and one child per position).
```
`Tr` is the free-monad functor `F*`. The free-monad **carrier** is the container `m = (S* ◁ P*)`:
```
S* := Tr(1)  = closed trees:   t ::= lf | nd s κ   (s:S, κ : P(s) → S*)
P*(t) := leaves(t):            leaves(lf) = 1,   leaves(nd s κ) = Σ_{p:P(s)} leaves(κ p).
```
We identify a **leaf** of `t` with the **root-to-leaf path** reaching it (a list of positions);
`leaves(t)` is the set of such paths, and the two clauses above build them by prefixing the
chosen position `p`. There is a natural bijection
```
rep : Tr(X) ≅ Σ_{t:S*} (leaves(t) → X) = ⟦S*◁P*⟧(X),
```
(a labelled tree = its shape together with a labelling of its leaves), so `⟦m⟧ = F*`. Directions
are **leaves**, not vertices — this is the free/cofree distinction; the cofree comonad carrier has
directions = *all* vertices (Niu–Spivak Prop. 8.18).

**Structure maps.**
```
η : I ⇒ m       η₁(*) = lf,             η♯_* : leaves(lf)=1 → 1  = id.
α : (S◁P) ⇒ m   α₁ s = nd s (λp.lf),    α♯_s : leaves(αs)=Σ_p 1 ≅ P(s)  = the canonical iso.
μ : m◁m ⇒ m     μ₁(t,u) = t[u] := graft(t,u),   μ♯_{(t,u)} = split_{t,u}.
```
Here a shape of `m◁m` is `(t,u)` with `t:S*` and `u : leaves(t) → S*`, and
`(m◁m).Pos(t,u) = Σ_{ℓ:leaves(t)} leaves(u_ℓ)`. **Grafting** substitutes `u_ℓ` for the leaf `ℓ`:
```
graft(lf, u)      = u(())                                    -- () is the unique leaf of lf
graft(nd s κ, u)  = nd s (λp. graft(κ_p, u_p)),   u_p(r) := u((p)·r)
```
where `(p)·r` prefixes position `p` to a path `r` of the child `κ_p`, and `·` is path
concatenation. `μ♯ = split` is the map defined in Lemma A. (`α` is recorded for completeness; the
monoid laws below use only `η` and `μ`.)

> **Foundational note.** `S*` is the carrier of a W-type, so it exists as a set (and, more
> generally, in any LCC category with W-types — G-K's setting). Every induction below is an
> induction over this initial algebra, i.e. structural induction on the closed tree `t`. No
> choice or excluded middle is used.

---

## 3. The leaf bijection (the crux)

**Lemma A (graft–leaf bijection).** For `t : S*` and `u : leaves(t) → S*`, path concatenation
```
cat_{t,u} : Σ_{ℓ:leaves(t)} leaves(u_ℓ) → leaves(graft(t,u)),   (ℓ, w) ↦ ℓ·w
```
is a **bijection**. Its inverse is
```
split_{t,u} : leaves(graft(t,u)) → Σ_{ℓ:leaves(t)} leaves(u_ℓ),
```
which cuts a leaf-path `z` of `graft(t,u)` at its unique prefix that is a leaf-path of `t`.

*Proof, by structural induction on `t`.*

- **`t = lf`.** `leaves(lf) = {()}`, `graft(lf,u) = u_()`, and the source is
  `Σ_{ℓ∈{()}} leaves(u_ℓ) ≅ leaves(u_())` via `((),w) ↦ w`. Then `cat((),w) = ()·w = w`, so
  `cat` is exactly this identification `leaves(u_()) → leaves(u_())`. Bijective; `split(z) = ((),z)`.

- **`t = nd s κ`.** By definition
  `leaves(t) = Σ_{p:P(s)} leaves(κ_p)`, and every `ℓ ∈ leaves(t)` is `(p)·r` for a unique
  `p:P(s)` and `r ∈ leaves(κ_p)`, with `u_ℓ = u((p)·r) = (u_p)_r`. Hence the source splits as
  ```
  Σ_{ℓ:leaves(t)} leaves(u_ℓ)  ≅  Σ_{p:P(s)} Σ_{r:leaves(κ_p)} leaves((u_p)_r).           (∗)
  ```
  On the target side, `graft(t,u) = nd s (λp. graft(κ_p, u_p))`, so
  ```
  leaves(graft(t,u)) = Σ_{p:P(s)} leaves(graft(κ_p, u_p)).                                 (∗∗)
  ```
  Now `cat_{t,u}((p)·r, w) = (p)·r·w = (p)·(r·w)`, which lands in block `p` of (∗∗) as the path
  `r·w = cat_{κ_p,u_p}(r,w)`. So under the block decompositions (∗) and (∗∗), `cat_{t,u}` is the
  disjoint union over `p` of the maps `cat_{κ_p,u_p}`. Each is a bijection by the induction
  hypothesis, hence so is `cat_{t,u}`.

- **Unique-prefix / inverse.** A proper extension of a leaf-path of `t` is never itself a
  leaf-path of `t` (a leaf has no children), so among the prefixes of `z = ℓ·w` exactly one —
  namely `ℓ` — is a leaf-path of `t`. Cutting there recovers `(ℓ,w)`; this is `split_{t,u}`, a
  two-sided inverse of `cat_{t,u}`. ∎

The uniqueness in the last clause is the reason **`μ♯` is forced**: once one commits to "cut at
the `t`-leaf boundary", there is no freedom, and no alternative bijection to get wrong. (This is
why the "cut at the deepest `t`-leaf" negative control in `free_monad_stress.py` silently equals
the correct map — there is only one `t`-leaf prefix.)

**Corollary A′ (three-fold bijection).** Iterating Lemma A once more, for `t:S*`,
`u:leaves(t)→S*`, `v:leaves(graft(t,u))→S*`,
```
leaves(graft(graft(t,u), v))  ≅  Σ_{ℓ:leaves(t)} Σ_{w:leaves(u_ℓ)} leaves(v_{ℓ·w}),
z ↦ (ℓ, w, x)  with  z = ℓ·w·x,
```
and every leaf `z` of the doubly-grafted tree is a **unique flat concatenation** `ℓ·w·x`.

---

## 4. The three monoid laws

Throughout, a container-morphism equation `φ = ψ : a ⇒ b` means `φ₁ = ψ₁` (forward) **and**
`φ♯_s = ψ♯_s` for every shape `s` (backward). I give both components of each law and reduce it to
a tree identity.

### 4.1 Left unit — `(FM-unitL): (η ◁ m) ; μ = λ_m : I◁m ⇒ m`

A shape of `I◁m` is `(*, g)` with `g : 1 → S*`; write `t := g(*)`. Compute the composite with the
§1 formulas.

- `(η◁m)₁(*,g) = (η₁ *, id ∘ g ∘ η♯_*) = (lf, λ_.t)` (using `η₁*=lf`, `η♯_*=id`). Then
  `μ₁(lf, λ_.t) = graft(lf, {() ↦ t}) = t`. The unitor gives `λ_m₁(*,g) = g(*) = t`. **Forward ✓**
  — and the only fact used is the `lf`-clause `graft(lf,u)=u(())`.

- Backward, at shape `(*,g)`, over a target position `w ∈ leaves(t) = P*(t)`:
  `μ♯_{(lf,λt)}(w) = split_{lf,λt}(w) = ((), w)` (Lemma A base), then
  `(η◁m)♯_{(*,g)}((),w) = (η♯_* (), id(w)) = (*, w)`. The unitor gives `λ_m♯(w) = (*, w)`.
  **Backward ✓.**

So `FM-unitL` is the base clause of `graft` together with the trivial base of `split`. ∎

### 4.2 Right unit — `(FM-unitR): (m ◁ η) ; μ = ρ_m : m◁I ⇒ m`

A shape of `m◁I` is `(t, !)` with `! : leaves(t) → 1`.

- `(m◁η)₁(t,!) = (t, η₁ ∘ ! ∘ id) = (t, λℓ. lf)`. Then `μ₁(t, λℓ.lf) = graft(t, λℓ.lf)`.

**Lemma B (right-unit tree identity).** `graft(t, λℓ.lf) = t`.
*Proof, induction on `t`.* `t=lf`: `graft(lf,λℓ.lf) = (λℓ.lf)(()) = lf`. `t = nd s κ`: for each `p`,
the restricted family is `(λℓ.lf)_p = λr. lf`, so `graft(κ_p, λr.lf) = κ_p` by IH; hence
`graft(nd s κ, λℓ.lf) = nd s (λp. κ_p) = t`. ∎

  Thus forward `μ₁(t,λℓ.lf) = t = ρ_m₁(t,!) = t`. **Forward ✓.**

- Backward, over `w ∈ leaves(t)` (`= leaves(graft(t,λℓ.lf))` by Lemma B):
  `μ♯_{(t,λℓ.lf)}(w) = split(w) = (w, ())` because `leaves(lf)={()}` forces the second component,
  and Lemma A cuts at the `t`-leaf `w` itself. Then
  `(m◁η)♯_{(t,!)}(w, ()) = (w, η♯_*()) = (w, *)`. The unitor gives `ρ_m♯(w) = (w, *)`.
  **Backward ✓.**

So `FM-unitR` is exactly Lemma B (forward) plus the singleton-leaf base of `split` (backward). ∎

### 4.3 Associativity — `(FM-assoc): (μ ◁ m) ; μ = a ; (m ◁ μ) ; μ`

A shape of `(m◁m)◁m` is `((t,u), v)` with `t:S*`, `u:leaves(t)→S*`, and
`v : (Σ_{ℓ}leaves(u_ℓ)) → S*`; write `v(ℓ,w)` for its value. Compute both sides.

**Left side `(μ◁m);μ`.**
`(μ◁m)₁((t,u),v) = (μ₁(t,u), v ∘ μ♯_{(t,u)}) = (t[u], λz. v(split_{t,u}(z)))` for `z:leaves(t[u])`.
Applying `μ`:
```
LHS₁ = graft( graft(t,u),  λz. v(split_{t,u} z) ).
```

**Right side `a;(m◁μ);μ`.**
`a₁((t,u),v) = (t, λℓ. (u_ℓ, λw. v(ℓ,w)))`. Write `v_ℓ := λw. v(ℓ,w) : leaves(u_ℓ)→S*`. Then
`(m◁μ)₁(t, λℓ.(u_ℓ,v_ℓ)) = (t, λℓ. μ₁(u_ℓ,v_ℓ)) = (t, λℓ. graft(u_ℓ,v_ℓ))`, and applying `μ`:
```
RHS₁ = graft( t,  λℓ. graft(u_ℓ, v_ℓ) ).
```

**Lemma C (associativity of grafting).** Identifying `v : leaves(graft(t,u)) → S*` with its
split coordinates via Lemma A (so `v(ℓ·w)` is written `v(ℓ,w)`), and setting
`v_ℓ := λw. v(ℓ·w) : leaves(u_ℓ) → S*`,
```
graft( graft(t,u), v )  =  graft( t,  λℓ. graft(u_ℓ, v_ℓ) ).
```
*Proof, induction on `t`.*

- **`t = lf`.** `leaves(lf)={()}`, `graft(lf,u)=u_()`, so LHS `= graft(u_(), v)`. RHS
  `= graft(lf, λℓ.graft(u_ℓ,v_ℓ)) = graft(u_(), v_())`, and `v_()(w) = v((),w) = v(()·w) = v(w)`,
  i.e. `v_() = v` as maps on `leaves(u_())`. Hence RHS `= graft(u_(), v) =` LHS.

- **`t = nd s κ`.** `graft(t,u) = nd s (λp. graft(κ_p,u_p))`, so by the `nd`-clause of `graft`,
  ```
  LHS = nd s (λp. graft( graft(κ_p,u_p), v_p )),      v_p(x) := v((p)·x)  for x:leaves(graft(κ_p,u_p)).
  ```
  Apply the induction hypothesis to `(κ_p, u_p, v_p)`:
  `graft(graft(κ_p,u_p), v_p) = graft(κ_p, λr. graft((u_p)_r, (v_p)_r))`,
  where `(u_p)_r = u((p)·r)` and `(v_p)_r(w) = v_p(r·w) = v((p)·r·w)`.
  For the right side, `graft(t, λℓ.graft(u_ℓ,v_ℓ)) = nd s (λp. graft(κ_p, (λℓ.graft(u_ℓ,v_ℓ))_p))`,
  and `(λℓ.graft(u_ℓ,v_ℓ))_p (r) = graft(u_{(p)·r}, v_{(p)·r})`. But `u_{(p)·r} = u((p)·r) = (u_p)_r`
  and `v_{(p)·r}(w) = v((p)·r·w) = (v_p)_r(w)`, so this is `graft((u_p)_r, (v_p)_r)`. Therefore block
  `p` of RHS equals block `p` of LHS by the IH, for every `p`; hence `LHS = RHS`. ∎

  So **forward ✓**, and it is exactly Lemma C.

- **Backward.** Both sides land in `((m◁m)◁m).Pos((t,u),v) = Σ_{ℓ}Σ_{w:leaves(u_ℓ)} leaves(v_{ℓ,w})`
  (regrouping the nested position sum), and a target position is a leaf `z` of the common tree
  `G := LHS₁ = RHS₁`.
  - `(μ◁m);μ` sends `z ↦ split_{graft(t,u),v}(z) = (z̄, x)`, then `z̄ ↦ split_{t,u}(z̄) = (ℓ,w)`,
    giving `(ℓ, w, x)` — the bracketing `(ℓ·w)·x`, cut first at the `graft(t,u)`-leaf, then at the
    `t`-leaf.
  - `a;(m◁μ);μ` sends `z ↦ split_{t, λℓ.graft(u_ℓ,v_ℓ)}(z) = (ℓ', y)`, then
    `y ↦ split_{u_{ℓ'}, v_{ℓ'}}(y) = (w', x')`, giving `(ℓ', w', x')` — the bracketing `ℓ·(w·x)`,
    cut first at the `t`-leaf, then at the `u_ℓ`-leaf. (The associator's backward map `((u,v),p)↦(u,v,p)`
    only regroups the sum, so it contributes nothing to the values.)

  **Lemma D (coherence of splits).** `(ℓ,w,x) = (ℓ',w',x')`.
  *Proof.* By Corollary A′ every `z ∈ leaves(G)` is the **unique** flat concatenation `ℓ₀·w₀·x₀`
  with `ℓ₀∈leaves(t)`, `w₀∈leaves(u_{ℓ₀})`, `x₀∈leaves(v_{ℓ₀,w₀})`, and `split` is the two-sided
  inverse of `cat` (Lemma A). Since path concatenation is associative — `(ℓ₀·w₀)·x₀ = ℓ₀·(w₀·x₀)`
  as lists — both bracketings cut `z` at the same two boundaries: the first cut of the left path is
  at the `graft(t,u)`-leaf `ℓ₀·w₀` and then at the `t`-leaf `ℓ₀`; the first cut of the right path is
  at the `t`-leaf `ℓ₀` and then at the `u_{ℓ₀}`-leaf `w₀`. Both recover `(ℓ₀, w₀, x₀)`. Hence
  `(ℓ,w,x) = (ℓ₀,w₀,x₀) = (ℓ',w',x')`. ∎

  So **backward ✓**, and it is exactly the associativity of list concatenation (Lemma D). ∎

**Conclusion.** `(m, μ, η) = (S*◁P*, graft, lf)` is a monoid in `(Cont, ◁, I)`; equivalently
`⟦m⟧` is a monad — the free monad on `(S◁P)`. The three monoid laws are, in container
coordinates,

| law | forward (shapes) | backward (positions) |
|-----|------------------|----------------------|
| **FM-unitL** | `graft(lf, {()↦t}) = t` (base of `graft`) | `split_{lf,·} = ((),·)` (base of `split`) |
| **FM-unitR** | `graft(t, λℓ.lf) = t` (**Lemma B**) | `split_{t,λℓ.lf} = (·,())` (leaf-of-`lf` base) |
| **FM-assoc** | `graft(graft(t,u),v)=graft(t,λℓ.graft(u_ℓ,v_ℓ))` (**Lemma C**) | flat-path associativity (**Lemma D**) |

These are precisely the checks Gambino–Kock call "lengthy but routine" and omit.

---

## 5. Verification

**Computational** (`scratch/free_monad_graft.py`, `free_monad_laws.py`, `free_monad_stress.py`):

- All three laws (forward **and** backward components, as container-morphism equalities) hold for
  the containers `S1P2` (binary trees), `S1P1` (lists), `S2P{0,1}`, `S2P{1,2}`, `S3P{0,2,1}`,
  `S1P0` (leaves only), over **all** closed trees up to 3 internal nodes and **all** label
  functions into the small-tree set.
- `graft_split` verified to be a genuine bijection `leaves(t[u]) ≅ Σ_ℓ leaves(u_ℓ)` with inverse
  = concatenation (87 / 8 / 8 / 1552 / 2864 / 1 leaves checked per container).
- **Negative controls fire** (so the test is not a mirror): an identity-substitution "wrong graft"
  is caught by the associativity **forward** check; an information-losing "wrong split" is caught by
  the associativity **backward** coherence check. (The naive "deepest-prefix" wrong split does *not*
  fire — correctly, since Lemma A shows the `t`-leaf prefix is unique, so it equals the real split.)

**Boundary cases.** `S1P0` (only leaves): laws hold, no inner structure to permute. `lf` and
single-node trees: the unit laws are exactly the two `graft`/`split` base clauses. Empty position
sets (`P(s)=0`, e.g. shape `0` of `S2P{0,1}`): `nd s κ` with `κ : 0 → S*` the empty map is a
**childless node with no leaves** — `leaves(nd s κ) = Σ_{p:0}(…) = 0` — so it contributes a
constant to `⟦m⟧` and grafting into/through it is vacuous (`graft(nd s κ, u) = nd s κ`); the
enumeration includes these trees and they pass.

**Cross-check against the Lean coordinates.** The `◁` shape/position formulas, the morphism
composition convention, and the unitor/associator maps used in §1 are copied verbatim from
`lean/Containers/Containers/Composition.lean` and `Cont.lean`, so the coordinate laws above are
the exact proof obligations a Lean formalisation will discharge (LEAN target: carrier as a W-type,
`graft` by well-founded recursion, Lemmas B/C by structural induction, A/D by the same). This is
the monoid mirror of `Comonoid.lean` / `ComonoidConverse.lean` (M3/M3b).

## 6. Gaps

**None in the coordinate law-derivation** (the stated goal): Lemmas A–D are complete structural
inductions and the reduction of each monoid law to them is explicit in both components.

Honestly delimited scope:

1. **The construction is not re-derived from scratch.** That `Tr` exists (the initial algebra /
   W-type) and that `rep` is a natural iso `⟦m⟧ ≅ F*` are taken from Gambino–Kock 4.5 /
   Abbott–Altenkirch–Ghani; I use them, I do not reprove them. The novelty here is *only* the
   explicit laws.
2. **Set / LCC+W-types.** The inductions are structural over the initial algebra, valid in any LCC
   category with W-types (G-K's generality). No constructive obstruction arises (no EM, no choice);
   the only infinitary inputs are the W-type recursion principle and the disjoint-union-of-bijections
   step in Lemma A, both constructively valid.
3. **`α` naturality / the universal property** (that `m` is the *free* monad, i.e. the unit of an
   adjunction `Mnd(Poly) → Poly`) is not addressed — it is Gambino–Kock's Theorem 4.5 proper and is
   outside this note's "spell out the monoid laws" scope.

---

### References
- N. Gambino, J. Kock, *Polynomial functors and polynomial monads*, arXiv:0906.4931, Thm 4.5.
- N. Gambino, M. Hyland, *Wellfounded trees and dependent polynomial functors*, TYPES 2003.
- J. Kock, *Polynomial functors and trees*, arXiv:0807.2874.
- M. Abbott, T. Altenkirch, N. Ghani, *Representing nested inductive types using W-types*, ICALP 2004.
- MacBeth, `Comonoid.lean` / `ComonoidConverse.lean` (M3/M3b), the comonoid mirror.
