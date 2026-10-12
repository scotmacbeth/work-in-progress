# The D1-vs-D2 floor dichotomy for the inventory gerbe

**MacBeth, deep-work /prove session, 2026-10-12.**
Repairs Rick's M1 (band-boundary review, `proofs/reviews/2026-10-12-band-boundary-review.pdf`):
the "floor corollary" *strict global inventory ⟺ β=0 ∧ [𝔤]=0* is **false under the naive
definition** of strict global inventory. This note turns M1 into a clean two-definition theorem
and locates each definition's obstruction in its correct degree.

---

## 0. Problem and result

Fix a small category `C`, a fibre `F`, the relabelling group `K = Aut F`, its centre `Z = Z(K)`,
inner automorphism group `Inn K = K/Z`, and outer automorphism group `Out K = Aut K / Inn K`.
Write `q : Aut K ↠ Out K` for the projection and `c : K ↠ Inn K ⊆ Aut K`, `c_a = conj(a)`, for
conjugation. There is a central extension of groups

> **(⋆)**  `1 → Z → K --c--> Inn K → 1`,  with class `[⋆] ∈ H²(Inn K; Z)` (trivial action: inner
> automorphisms fix `Z` pointwise).

The inventory datum is an *outer transport*: a map `α` sending each morphism `f : x → y` of `C` to
an automorphism `α(f) ∈ Aut K`, functorial up to inner (a pseudofunctor `C → B(Aut K)` with 2-cell
datum `k_{g,f} ∈ K`, `α(gf) = c_{k_{g,f}} α(g) α(f)`). Its **band** is the induced strict functor
`ρ = q∘α : C → B(Out K)`, with class `β = [ρ] ∈ H¹(N(C); Out K)` (nonabelian `H¹`).

**Standing hypothesis (band trivial).** `β = 0`. By the band-triviality criterion (clause-(a) of
the band-boundary note, **proved**; Giraud stratum 2 on the nerve), `α` is `Aut K`-gauge-equivalent
to a strict `Inn K`-valued functor. **Fix such a gauge once and for all** and write

> `ᾱ : C → B(Inn K)`,  a *strict* functor (`ᾱ(gf) = ᾱ(g)ᾱ(f)`, `ᾱ(id)=id`),

for the band-trivialised transport. This is the object both definitions below act on.

Two notions of *strict global inventory*:

- **(D1, naive)** a gauge `μ : Ob C → Aut K` with `μ(y) ᾱ(f) μ(x)⁻¹ = id_K` for every `f : x → y`
  (the transport is relabelled away entirely; **no 2-cell datum retained**).
- **(D2)** a pair `(μ, T)`, `μ : Ob C → Aut K` and `T : C → BK` a **strict** functor (`T_{gf}=T_g T_f`
  in `K`), with `μ(y) ᾱ(f) μ(x)⁻¹ = c_{T_f}` for every `f : x → y` (the 2-cell datum survives, realised
  by honest group elements `T_f ∈ K`).

The **gerbe class** is `[𝔤] := ᾱ*[⋆] ∈ H²(N(C); Z)` — the pullback of the extension class along
`ᾱ` (Thm A / `lift-cocycle-derivation`). Define `o_{D1}` in §3.

> **Theorem (floor dichotomy).**
> 1. **(D2 end)** A D2 global inventory exists ⟺ `[𝔤] = 0 ∈ H²(N(C); Z)`.
> 2. **(D1 end)** A D1 global inventory exists ⟺ `o_{D1} = 0`, where `o_{D1}` is the class of `ᾱ`
>    in `H¹(C; Inn K) / im(H⁰(C; Out K))`. This is a **degree-1** obstruction; it is *not* `[𝔤]`.
> 3. **(Separation)** For `C = B(ℤ)`, `K = S₃`, `α = conj((0 1))`: `β = 0` **and** `[𝔤] = 0` (so D2
>    says "strict exists"), yet `o_{D1} ≠ 0` (no naive gauge `μ` strictifies). Hence D1 ⊊ D2 and the
>    naive floor corollary is false.
>
> Moreover **D1 ⟹ D2** (`o_{D1}=0 ⟹ [𝔤]=0`), and the strict containment is witnessed exactly by the
> *centreless/fungible* regime where `Z` is too small to carry `[𝔤]`.

Both `[𝔤]` and `o_{D1}` are canonical only up to the residual `Out K`-action (global change of fibre
coordinates); as Remark 4 shows, this ambiguity never affects *vanishing*, so each biconditional is
well-posed.

---

## 1. The transport as a strict inner functor; nonabelian `H¹`

For a group `G` with trivial `C`-action, let `H¹(C; G)` be the pointed set of functors `C → BG`
modulo natural isomorphism. Concretely a functor is a **1-cocycle**: an assignment `f ↦ g_f ∈ G`
with `g_{id}=e` and `g_{gf}=g_g g_f`; a natural isomorphism is **vertex data** `ν : Ob C → G`,
acting `g_f ↦ ν(y) g_f ν(x)⁻¹`. The basepoint `*` is the trivial functor `f ↦ e`. (For `G` nonabelian
this is only a pointed set; that is all we need.) A cocycle is a **coboundary** iff it is naturally
isomorphic to `*`, i.e. `g_f = ν(y)⁻¹ ν(x)` for some `ν`.

`ᾱ` is such a 1-cocycle valued in `G = Inn K`. For `C = B(ℤ)` (one object, free on one generator),
`H¹(B(ℤ); G) = G/conj` (conjugacy classes = image of the generator up to conjugation); `[ᾱ]` is the
conjugacy class of `ᾱ(1)`.

---

## 2. Part 1 — the D2 obstruction is `[𝔤] ∈ H²`

**Lemma 1 (strict lifting through a central extension).** *Let `φ : C → BQ` be a strict functor
(`Q = Inn K`). A strict functor `T : C → BK` with `c∘T = φ` (i.e. `T_f ∈ K`, `c(T_f)=φ_f`,
`T_{gf}=T_g T_f`) exists iff `φ*[⋆] = 0 ∈ H²(N(C); Z)`.*

*Proof.* Choose any set-section lift `s : Q → K` of `c` with `s(e)=e`, and put `t_f := s(φ_f) ∈ K`,
so `c(t_f)=φ_f`. The defect `z(g,f) := t_{gf} (t_g t_f)⁻¹` satisfies `c(z(g,f)) = φ_{gf}(φ_g φ_f)⁻¹ = e`,
so `z(g,f) ∈ Z`. Associativity of composition in `C` forces the 2-cocycle identity `δz = 0` on the
nerve `N(C)` (standard bar computation, using that `Z` is central so the action is trivial), and the
class `[z] ∈ H²(N(C); Z)` is exactly `φ*[⋆]` — it is the pullback along `φ : N(C) → BQ` of the bar
2-cocycle of `(⋆)` (Brown, *Cohomology of Groups*, GTM 87, IV.3; Eilenberg–MacLane). A strict lift is
a choice `T_f = t_f·ζ_f` with `ζ_f ∈ Z` making `z' ≡ 0`; `z' = z·δζ`, so a strict lift exists iff `z`
is a `Z`-valued coboundary iff `[z]=0`. ∎

This is the content already carried by **`thm-A-rectification`** (proved, Rick-reviewed) and its child
`lift-cocycle-derivation`; Lemma 1 is the clean statement.

**Proposition 2 (D2 end).** *A D2 global inventory exists ⟺ `[𝔤] = ᾱ*[⋆] = 0 ∈ H²(N(C); Z)` (up to the
`Out K`-action, Rem. 4).*

*Proof.* Given `(μ,T)`, set `τ(f) := μ(y) ᾱ(f) μ(x)⁻¹`. Since `Inn K ⊴ Aut K` and `ᾱ(f) ∈ Inn K`, `τ(f)`
is inner, so `τ : C → B(Inn K)` is a functor; strictness of `ᾱ` and conjugation give
`τ(gf) = μ(z)ᾱ(gf)μ(x)⁻¹ = μ(z)ᾱ(g)μ(y)⁻¹·μ(y)ᾱ(f)μ(x)⁻¹ = τ(g)τ(f)`, so `τ` is a *strict* functor.
The D2 equation `τ(f) = c_{T_f}` with `T` strict says precisely that `T` is a strict lift of `τ`
through `(⋆)`. By Lemma 1 such `(μ,T)` exists ⟺ `τ*[⋆]=0` for some admissible `μ`.

It remains to see `τ*[⋆]=0 ⟺ ᾱ*[⋆]=0`. Decompose `μ(x) = ĥ_c · j(x)` on each component `c`, with
`ĥ_c ∈ Aut K` a fixed lift of the (locally constant) `Out K`-part `q∘μ` and `j(x) ∈ Inn K`. Then
`τ(f) = ĥ_c·(j(y) ᾱ(f) j(x)⁻¹)·ĥ_c⁻¹ = Ad(ĥ_c) ∘ ᾱ'(f)`, where `ᾱ'(f) := j(y) ᾱ(f) j(x)⁻¹` is
naturally isomorphic to `ᾱ` (inner vertex data), hence `ᾱ'* = ᾱ*` on `H²(N(C); Z)`. The global
automorphism `ĥ_c ∈ Aut K` preserves the extension `(⋆)` — it fixes `Z` setwise, inducing
`ĥ_c|_Z ∈ Aut(Z)`, and covers `Ad(ĥ_c) ∈ Aut(Inn K)` — so `Ad(ĥ_c)*[⋆] = (ĥ_c|_Z)_*[⋆]` (the
extension class with coefficients transported by `ĥ_c|_Z`), and the coefficient automorphism
`(ĥ_c|_Z)_*` commutes with pullback. Thus `τ*[⋆] = (ĥ_c|_Z)_* ᾱ*[⋆] = (ĥ_c|_Z)_*[𝔤]`, an automorphism
image of `[𝔤]`. An automorphism of `H²(N(C); Z)` fixes `0`, so `τ*[⋆]=0 ⟺ [𝔤]=0`. ∎

**Corollary 3.** For `C = B(ℤ)`, `N(C) ≃ S¹`, so `H²(S¹; Z) = 0` and `[𝔤]=0` for **every** `K`:
D2 inventory always exists over a free one-generator base. (Explicit lift below.)

---

## 3. Part 2 — the D1 obstruction is `o_{D1} ∈ H¹`

**The band-preserving constraint is forced.** If a D1 gauge `μ` exists then, applying `q` to
`μ(y)ᾱ(f)μ(x)⁻¹ = id`, and using `q(ᾱ(f))=e` (band trivial), we get `q(μ(y)) = q(μ(x))` for every
`f : x → y`. Hence `q∘μ : Ob C → Out K` is **locally constant** (constant on connected components).
No extra hypothesis is needed — D1 *entails* band-preservation.

**Construction of `o_{D1}`.** `H⁰(C; Out K)` is the group of locally constant functions
`Ob C → Out K` (= `Out K` per component). It acts on the pointed set `H¹(C; Inn K)` as follows: given
`θ ∈ H⁰(C; Out K)`, choose a locally constant lift `ĥ : Ob C → Aut K` with `q∘ĥ = θ`, and send a
cocycle `g_f` to `ĥ(y) g_f ĥ(x)⁻¹ ∈ Inn K` (inner, as `Inn K ⊴ Aut K`). A different lift of `θ` differs
by an `Inn K`-valued cochain, changing the result by an `Inn K`-coboundary; so the action descends to a
well-defined action on `H¹(C; Inn K)` fixing the basepoint `*`. Define

> `o_{D1} := [ᾱ] ∈ H¹(C; Inn K) / im(H⁰(C; Out K))`.

**Proposition 5 (D1 end).** *A D1 global inventory exists ⟺ `o_{D1} = 0`.*

*Proof.* **(⟸, and the stronger `[ᾱ]=*`.)** First, D1 ⟺ `[ᾱ]=*` in `H¹(C; Inn K)`:

- If `[ᾱ]=*`, pick `j : Ob C → Inn K` with `ᾱ(f)=j(y)⁻¹ j(x)`. Set `μ := j : Ob C → Inn K ⊆ Aut K`.
  Then `μ(y)ᾱ(f)μ(x)⁻¹ = j(y)·j(y)⁻¹j(x)·j(x)⁻¹ = id`. So D1 holds.
- Conversely let `μ : Ob C → Aut K` solve D1. By the forced constraint, `q∘μ = θ_c` is constant on each
  component `c`; choose one lift `ĥ_c ∈ Aut K` of `θ_c`, and write `μ(x) = ĥ_c · j(x)` with
  `j(x) := ĥ_c⁻¹ μ(x) ∈ ker q = Inn K` for `x` in `c`. For `f : x → y` within `c`,
  `ᾱ(f) = μ(y)⁻¹ μ(x) = j(y)⁻¹ ĥ_c⁻¹ ĥ_c j(x) = j(y)⁻¹ j(x)`, an `Inn K`-coboundary on `c`. Running over
  all components, `[ᾱ]=*`.

So D1 ⟺ `[ᾱ]=*`. Now the quotient: the `Out K`-action fixes `*`, so the fibre of the quotient map
`H¹(C; Inn K) → H¹/im(H⁰(Out K))` over the basepoint is exactly the `Out K`-orbit of `*`, which is
`{*}`. Therefore `o_{D1} = 0` (basepoint of the quotient) ⟺ `[ᾱ]=*` ⟺ D1 holds. ∎

The quotient by `im(H⁰(C; Out K))` makes `o_{D1}` independent of the choice of fibre coordinates (a
global automorphism of `K`, which acts by an outer class); by the last line it never changes whether
`o_{D1}=0`. (D4 witness in §6 shows the action can be nontrivial: it swaps the two reflection
conjugacy-classes — both nonzero — confirming the quotient is needed for coordinate-freeness but is
vanishing-neutral.)

---

## 4. Remark — a single well-definedness caveat, and the degree lane

**Remark 4.** Both invariants are canonical only up to the residual `Out K`-action (global fibre
re-coordinatisation): `[𝔤]` up to the `Out K`-action on `H²(N(C); Z)` (Prop. 2), `o_{D1}` by the explicit
quotient (Prop. 5). In **both** cases the action is by a group of automorphisms fixing `0`/`*`, so
**vanishing is invariant** and both biconditionals are well-posed. This is the honest parallel: D1 and
D2 differ not in their gauge symmetry but in their *degree*.

**The degree drop.** D1 asks the inner transport `ᾱ` to be a **coboundary** — trivialised to the
identity — a degree-1 (`H¹`) question. D2 asks `ᾱ` only to **lift** to a strict `K`-valued functor,
retaining it as a genuine inner transport realised by honest group elements — a degree-2 (`H²`,
k-invariant) question. Dropping the 2-cell datum costs exactly one cohomological degree. This is the
degree-lane lesson of the program (`degree-lane-off-by-one-nerve-level`,
`supply-chain-inventory-h1-vs-weld-h2`): *name the extension and the kernel names the coefficient and
the degree.*

**Proposition 6 (D1 ⟹ D2).** *`o_{D1} = 0 ⟹ [𝔤] = 0`.* If `[ᾱ]=*`, then `ᾱ` is naturally isomorphic to
the constant functor at the identity object of `B(Inn K)`; pullback along a functor isomorphic to a
constant kills `H²`, so `[𝔤] = ᾱ*[⋆] = 0`. (Equivalently: take `T ≡ e` in D2.) ∎

The containment is **strict**: the gap `o_{D1} ≠ 0 = [𝔤]` is realised exactly when `Z = Z(K)` is too
small to carry a nonzero `[𝔤]` while `ᾱ` is still a nontrivial inner transport — the *centreless /
fungible* regime. `S₃` (`Z=1`) is the minimal such witness.

---

## 5. Part 3 — the separation: `C = B(ℤ)`, `K = S₃`, `α = conj((0 1))`

`S₃` is **complete**: `Z(S₃)=1`, `Inn S₃ = S₃`, `Out S₃ = 1`, `Aut S₃ = Inn S₃ ≅ S₃` (Rotman GTM 148,
Thm 7.5). The transport on `B(ℤ)` is determined by the generator: `α(1) = c_σ`, `σ = (0 1)`, and freely
`α(n) = c_σ^n = c_{σ^n}`; since `B(ℤ)` is free on one generator this is already a strict functor with
trivial 2-cell datum, so `ᾱ(n) = c_{σ^n}`.

- **Band `β`:** `Out S₃ = 1`, so `β ∈ H¹(S¹; 1) = 0`. ✔ (band trivial)
- **Gerbe class `[𝔤]`:** `Z(S₃) = 1`, so `H²(S¹; Z) = 0` and `[𝔤] = 0`; *independently*, `N(B(ℤ)) ≃ S¹`
  gives `H² = 0` (Cor. 3). By Prop. 2, **D2 inventory exists.** Explicit witness: `T(n) = σ^n` is a
  homomorphism `ℤ → S₃` (`σ² = e`), `μ = id`, and `c_{T(n)} = c_{σ^n} = ᾱ(n)`. ✔
- **`o_{D1}`:** `H¹(B(ℤ); Inn S₃) = S₃/conj = {[e], [transposition], [3-cycle]}`; `o_{D1}` is the class of
  `σ = (0 1)`, a **transposition ≠ [e]**, and `Out = 1` leaves it unchanged. So `o_{D1} ≠ 0`. By Prop. 5,
  **no D1 inventory exists.** Directly: on one object the gauge cancels (`μ·ᾱ(1)·μ⁻¹ = c_{m σ m⁻¹}`),
  and `c_{mσm⁻¹} = id ⟺ mσm⁻¹ = e`, impossible for `σ ≠ e`. ✔

Hence `β = 0 ∧ [𝔤] = 0` yet D1 fails: the naive floor corollary *strict ⟺ β=0 ∧ [𝔤]=0* is **false**,
and the honest D1 floor lives one degree down, in `H¹`. ∎

This is exactly Rick's independently-recomputed `B(ℤ)/S₃` counterexample, now proved in both directions
with the `o_{D1}` location made explicit.

---

## 6. Computational verification

`scratch/2026-10-12-d1-d2-dichotomy-verify.py` (pure Python, brute-force Aut/Inn/Out/Z):

- **S₃:** `|Aut|=|Inn|=6`, `|Z|=1`, `|Out|=1`. `α(1)=conj((0 1))` is inner and ≠ id. Band `β=0`
  (`Out=1`). D2 lift `T(1)=σ` with `conj(T(1))=α(1)` ✔ and `σ²=e` ✔. `o_{D1}=` conj class
  `{(0 1),(0 2),(1 2)} ≠ {e}`. Exhaustive search over all 6 automorphisms `m`: **no** `m` with
  `m·α(1)·m⁻¹ = id` → D1 unsolvable, as predicted.
- **D₄ (coordinate-independence check):** `|Aut|=8`, `|Inn|=4`, `|Z|=2`, `|Out|=2`. The two reflection
  conjugacy classes `{s, r²s}` and `{rs, r³s}` are **swapped** by an (outer) automorphism — so the
  `Out`-action on `H¹(C; Inn K)` is nontrivial, justifying the quotient in `o_{D1}`; both classes are
  nonzero, so the quotient is vanishing-neutral.

All predictions confirmed.

---

## 7. Scope, provenance, gaps

- **Classical backbone (cited):** Lemma 1 is the Eilenberg–MacLane / Brown IV.3 central-extension
  lifting criterion; the nonabelian-`H¹` coboundary formalism is standard (Serre, *Galois Cohomology*
  I.5). These are *carried*, not re-derived beyond the short bar computation in Lemma 1.
- **New content (proved in-file):** the precise two-definition split (D1/D2), the forced
  band-preservation, the construction of `o_{D1}` and the identity *D1 ⟺ o_{D1}=0* (Prop. 5), the
  gauge-invariance reconciliation for D2 (Prop. 2), the single well-definedness caveat (Rem. 4), the
  logical picture *D1 ⟹ D2* with the centreless gap (Prop. 6), and the `S₃` separation in both
  directions (§5).
- **Scope:** band-trivial stratum (`β=0`) only, exactly as in the floor corollary being repaired. The
  nontrivial-band and `T²`-coupled frontiers are untouched (and explicitly deferred behind Strathclyde).
- **No gaps.** Every step follows by definition, the cited classical criterion, or the finite
  computation. The `S₃` separation is fully explicit.

**Upshot.** Rick's M1 is now a theorem: the inventory floor splits cleanly by *how much structure you
retain*. Keep the 2-cell (D2): obstruction is the gerbe class `[𝔤] ∈ H²(N(C); Z(K))`. Drop it (D1):
obstruction drops a degree to `o_{D1} ∈ H¹(C; Inn K)/im H⁰(C; Out K)`. They agree iff `Z(K)` is rich
enough; over fungible (centreless) stock they diverge, and `B(ℤ)/S₃` is the honest witness.
