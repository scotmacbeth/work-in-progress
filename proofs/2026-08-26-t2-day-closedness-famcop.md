# T2 — Closedness of the Dirichlet tensor `⊗` on `Fam(C^op)`, generally

**MacBeth — 2026-08-26 (PROVE session).** Answers Neil's directive (email UID 124):
*"try and do T2 generally."* Target: a general theorem about when the convolution tensor
`⊗` on `Fam(C^op)` is **closed** (each `(-)⊗(T,Q)` has a right adjoint), with the
load-bearing hypothesis named. `Vec_fd` is the sharp finite test case, not the whole claim.

**Headline.** Closedness of `⊗` on `Fam(C^op)` is *exactly* a **familial-representability**
condition (Diers), and it decomposes into two independent conjuncts:

> **(A) single-factor representability** — `Z ↦ C(A, Z⊗Q)` is familially representable
> for all `A,Q`; and **(B) product-closure** — the resulting corepresentables have a
> representing coproduct `∐_{t∈T} N_t` in `C` for every small index `T`.

Over a **cartesian** base (`⊗=×`: `Set`, any topos, `Set×Set`) both hold unconditionally,
so `⊗` is closed. Over a **linear** base (`Vec`) the two conjuncts are in **tension**: (A)
holds over `Vec` *iff the tensor-argument positions `Q_t` are dualizable (finite-dimensional)*,
while (B) for infinite `T` needs an infinite coproduct that leaves the finite-dimensional world.
**Consequently `⊗` is closed on the finite/fd corner `Fam_{fin}(Vec_fd^op)` but on NEITHER
`Fam(Vec_fd^op)` (infinite shape sets break (B)) NOR `Fam(Vec^op)` (infinite-dimensional
positions break (A)).** This *sharpens and corrects* the pre-registered prediction ("holds
over full Vec, fails over Vec_fd"): it fails over both, for **dual** reasons, and the named
load-bearing conjunct is the *simultaneous* dualizability-and-coproduct that only the
finite-fd corner supplies.

---

## 0. Setup and the object of study

Fix a **closed symmetric monoidal** `(C, ⊗, I, [-,-])` with **small coproducts** `∐`.
Closedness gives `-⊗Q ⊣ [Q,-]` and `C(A,B)=C(I,[A,B])`.

**Definition 0.1 (container over `C`).** `Fam(C^op)` has objects `(S,(P_s)_{s∈S})` (a set `S`
of *shapes*, objects `P_s∈C` the *positions*) and hom-sets
```
        Fam(C^op)((A,X),(B,Y)) = ∏_{a∈A} ∐^{Set}_{b∈B} C(Y_b, X_a)
```
— a *choice* `f:A→B` of one `b=f(a)` per `a`, plus a `C`-map `Y_{f(a)}→X_a` (contravariant on
positions). This is exactly Def 0.1 of `2026-08-25-fullness-unit-connectedness.md`.

**Definition 0.2 (Dirichlet/parallel tensor).**
`(S,P) ⊗ (T,Q) := (S×T, (P_s⊗Q_t)_{(s,t)})`, unit `I_⊗=({∗}, I)`. Its extension is the Day
convolution of the corepresentables: `⟦(S,P)⊗(T,Q)⟧ = ∐_{s,t}[P_s⊗Q_t,-]`, and Day convolution
of corepresentables is `[P,-]∗[Q,-]=[P⊗Q,-]`, so `⊗` on `Fam(C^op)` **is** the restriction of
Day convolution (on `C`-enriched endofunctors) to coproducts-of-corepresentables. Over `Set`
(`⊗=×`) this is the Dirichlet product of polynomial functors; over `Vec` it is Part 3 of
`2026-08-18-linear-containers-vec.md`.

**The question (T2).** For which `C` is `⊗` **closed** — i.e. does `(-)⊗(T,Q)` have a right
adjoint `[(T,Q)⇒-]` *inside* `Fam(C^op)`?

**The translation to Day (done first, per discipline).** Day's Theorem 3.3 (LNM 137, 1970)
makes `[A,V]` biclosed for `V` complete-cocomplete SMC-closed and `A` **small** (or
representability). Here the ambient functor category is the `C`-enriched endofunctors `C\text{-}[C,C]`,
so `A=C` **as a (large) `C`-enriched category** and `V=C`. Because `A=C` is *large*, Day's
"small `A`" branch does **not** apply: we are forced into the *representability* branch, and the
internal hom Day writes as an **end** `T/S=∫_C[\int^B SB⊗P(-BC),TC]` need not land back in
coproducts-of-corepresentables. **That landing — the representability refinement — is precisely
the T2 content, and it is what Dorta–Jarvis–Niu (`2305.05655`) omit.** The elementary reduction
of §1 computes it exactly, so I do not lean on Day 3.3 as a black box; I use it only to place
the result (§5).

---

## 1. The reduction: closedness ⟺ familial representability

**Theorem 1.1 (reduction).** The following are equivalent.

1. `(-)⊗(T,Q)` has a right adjoint in `Fam(C^op)` for every `(T,Q)` (i.e. `⊗` is closed).
2. For every pair of families `(Q_t)_{t∈T}`, `(M_r)_{r∈R}` the functor
   ```
        Φ_{Q,M} : C → Set,     Φ_{Q,M}(Z) = ∏_{t∈T} ∐_{r∈R} C(M_r, Z⊗Q_t)
   ```
   is **familially representable**: `Φ_{Q,M} ≅ ∐_{u∈U} C(N_u,-)` for a small family `(N_u)∈C`.
3. For every small family `((A_t,Q_t))_{t∈T}` of pairs of objects, the functor
   ```
        Θ_{A,Q} : C → Set,     Θ_{A,Q}(Z) = ∏_{t∈T} C(A_t, Z⊗Q_t)
   ```
   is familially representable.

When they hold, `[(T,Q)⇒(R,M)] = (U,(N_u))` with `∐_u C(N_u,-) ≅ Φ_{Q,M}`.

*Proof.*
**(1)⟺(2).** A right adjoint `[(T,Q)⇒(R,M)]=(U,(N_u))` is, by definition of adjunction, an object
with `Fam((S,P)⊗(T,Q),(R,M)) ≅ Fam((S,P),(U,N))` naturally in `(S,P)`. Expand both sides with
Def 0.1:
```
   LHS = ∏_{(s,t)} ∐_r C(M_r, P_s⊗Q_t) = ∏_{s} [ ∏_t ∐_r C(M_r, P_s⊗Q_t) ] = ∏_s Φ_{Q,M}(P_s),
   RHS = ∏_s ∐_u C(N_u, P_s).
```
A right adjoint at `(T,Q),(R,M)` exists iff the functor `G:=Fam(-⊗(T,Q),(R,M)):Fam(C^op)^{op}→Set`
is **representable**. Now `Fam(C^op)` is the **free coproduct completion** of `C^op`: every object
is a coproduct `(S,P)=∐_{s∈S}({∗},P_s)` of one-shape generators, and `({∗},-):C^op↪Fam(C^op)` is
the universal embedding. Two facts pin representability:
- **`G` sends coproducts to products.** `⊗` distributes over the shape-coproduct
  (`(∐_i(S_i,P_i))⊗(T,Q)=∐_i((S_i,P_i)⊗(T,Q))`), and `Fam(∐_i(-),(R,M))=∏_iFam((-),(R,M))`
  (hom out of a coproduct). So `G(∐_i(S_i,P_i))=∏_iG(S_i,P_i)`.
- **On generators** `G({∗},Z)=Fam((T,Z⊗Q),(R,M))=∏_t∐_r C(M_r,Z⊗Q_t)=Φ_{Q,M}(Z)`.
By the universal property of the free coproduct completion, a coproduct-to-product functor on
`Fam(C^op)^{op}` is representable **iff** its restriction to the generators is representable by an
object of `Fam(C^op)` — i.e. iff `Φ_{Q,M}(Z)≅Fam(({∗},Z),(U,N))=∐_uC(N_u,Z)` for some family
`(U,(N_u))`. That is exactly familial representability of `Φ_{Q,M}`, and `(U,(N_u))` is the internal
hom. This proves (1)⟺(2) and identifies `[(T,Q)⇒(R,M)]=(U,(N_u))`.

**(2)⟺(3).** *Set-distributivity.* For sets, `∏_{t}∐_{r} X_{t,r} = ∐_{ρ:T→R} ∏_{t} X_{t,ρ(t)}`
(an element of the product picks, for each `t`, a branch `r=ρ(t)` and a point). Applying this to
`X_{t,r}=C(M_r,Z⊗Q_t)` — *no hypothesis on `C` is used, the values are plain sets* — gives
```
        Φ_{Q,M}(Z) ≅ ∐_{ρ:T→R} Θ_{M∘ρ, Q}(Z),     Θ_{M∘ρ,Q}(Z)=∏_t C(M_{ρ(t)}, Z⊗Q_t).       (★)
```
*(3)⟹(2):* each `Θ` familially representable ⟹ the `∐_ρ` of them is familially representable
(a coproduct of coproducts-of-corepresentables is a coproduct-of-corepresentables), so `Φ` is.
*(2)⟹(3):* fix a family `((A_t,Q_t))_{t∈T}`; take `R:=T`, `M_t:=A_t`. In `(★)` the summand
`ρ=id_T` is exactly `Θ_{A,Q}`. Now `Φ` familially representable means `Φ≅∐_uC(N_u,-)`; each
corepresentable `C(N_u,-)` is **connected** in `[C,Set]` (its category of elements has the initial
object `(N_u,id)`), so the connected components of `∐_uC(N_u,-)` are the individual `C(N_u,-)`,
and any coproduct-summand of `Φ` is again a coproduct of a subset of the `C(N_u,-)` — hence
familially representable. The decomposition `(★)` exhibits `Θ_{A,Q}` (the `ρ=id` summand) as such
a summand. So `Θ_{A,Q}` is familially representable. ∎

**Remark 1.2 (why `Θ` is the right atom).** `Θ_{A,Q}(Z)=∏_{t}C(A_t,Z⊗Q_t)` isolates the *only*
place `Z` is integrated over the **whole** index `T` — this is the "end/product over the whole
grading" that Day's paradigm `(Y/X)_m=∏_n[X_n,Y_{m+n}]` (LNM 137, p.32) predicts as an infinite
product. The two conjuncts of the Headline are: (A) each factor `C(A_t,Z⊗Q_t)` familially
representable, (B) the product `∏_{t∈T}` of the resulting corepresentables representable.

---

## 2. The two sufficient regimes (with explicit internal homs)

### 2(a). Cartesian regime

**Theorem 2.1 (`C` cartesian closed ⟹ `⊗` closed).** If `⊗=×` (so `C` is cartesian closed) with
small coproducts, then `Θ_{A,Q}` is familially representable for every family, hence `⊗` is closed.

*Proof.* Cartesianness gives the *projection split* `C(A, Z×Q) ≅ C(A,Z)×C(A,Q)` (a map into a
product is a pair). Hence
```
   Θ_{A,Q}(Z)=∏_t C(A_t,Z×Q_t)=∏_t [C(A_t,Z)×C(A_t,Q_t)]
            =[∏_t C(A_t,Z)]×[∏_t C(A_t,Q_t)]
            =C(∐_t A_t, Z) × K,      K:=∏_t C(A_t,Q_t) a constant set,
```
using `∏_tC(A_t,-)=C(∐_tA_t,-)` (hom out of a coproduct). A constant set times a corepresentable
is a copower of corepresentables: `C(N,Z)×K ≅ ∐_{k∈K}C(N,Z)`, familially representable with
`N=∐_tA_t`. ∎

**Corollary 2.2 (explicit Dirichlet internal hom over a topos).** Threading through `(★)` and
Theorem 2.1,
```
   [(T,Q)⇒(R,M)] = ( U, (N_ξ) ),   U = ∐_{ρ:T→R} ∏_{t∈T} C(M_{ρ(t)}, Q_t),   N_{(ρ,·)} = ∐_{t∈T} M_{ρ(t)}.
```
Over `Set` this is the classical Dirichlet-product internal hom of `Poly` (Niu–Spivak Ex 4.78
base case); it needs no dualizability and no finiteness. The `Set×Set` witness of T1 (Cor 3.3 of
the fullness file) sits here too: cartesian bases give closedness of `⊗` even where the *extension*
`⟦−⟧` is not full — closedness of `⊗` and fullness of `⟦−⟧` are independent axes.

### 2(b). Rigid (dualizable) regime

**Theorem 2.3 (dualizable positions ⟹ `⊗` closed).** Suppose every `Q_t` occurring is
**dualizable** in `C` (a dual `Q_t^*` with `-⊗Q_t ⊣ -⊗Q_t^*`), and `C` has the small coproducts
`∐_t A_t⊗Q_t^*`. Then `Θ_{A,Q}` is *corepresentable* (a single shape), and `⊗` is closed with
```
   [(T,Q)⇒(R,M)] = ( R^T, (N_ρ)_{ρ:T→R} ),     N_ρ = ∐_{t∈T} M_{ρ(t)} ⊗ Q_t^*.
```

*Proof.* Dualizability gives `Z⊗Q_t ≅ [Q_t^*,Z]` (`Q_t^{**}≅Q_t`), so by tensor–hom closedness
`C(A_t, Z⊗Q_t) = C(A_t,[Q_t^*,Z]) ≅ C(A_t⊗Q_t^*, Z)`, corepresentable at `A_t⊗Q_t^*`. Then
`Θ_{A,Q}(Z)=∏_t C(A_t⊗Q_t^*,Z)=C(∐_t A_t⊗Q_t^*, Z)`, a *single* corepresentable. Substituting
`A_t=M_{ρ(t)}` in `(★)` gives shape set `R^T` and positions `N_ρ=∐_tM_{ρ(t)}⊗Q_t^*`. ∎

**Remark 2.4.** Only the *tensor-argument* positions `Q_t` need be dualizable; the representing
object `N_ρ` may be any object of `C` — it need *not* be dualizable. This asymmetry is the crux of
§3: over `Vec` the `Q_t` are forced finite-dimensional, but `N_ρ` is then an infinite direct sum,
which is fine in `Vec` yet outside `Vec_fd`.

---

## 3. The linear base: where the two conjuncts collide (the sharp failure)

Now `C=Vec_k` (or `Vec_{fd}`), `⊗=⊗_k`, `I=k`, `[P,W]=Vec(P,W)`, `∐=⊕`. Non-cartesian, so the
split of Theorem 2.1 is unavailable; the only route to (A) is Theorem 2.3. I show that route is
also *necessary* over `Vec`, then read off the collision.

**Lemma 3.1 (single-factor representability over `Vec` ⟺ dualizability).** For `A,Q∈Vec` the
functor `Θ(Z)=Vec(A, Z⊗Q):Vec→Set` is familially representable **iff `Q` is finite-dimensional**,
in which case it is corepresentable at `A⊗Q^*`.

*Proof.* (⟸) is Theorem 2.3 with a single `t` (fd ⟺ dualizable in `Vec`). (⟹) Take `A=k`, so
`Θ(Z)=Vec(k,Z⊗Q)=|Z⊗Q|` (underlying set). At `Z=0`, `Θ(0)=|0|=1`, so a familial
representation `∐_uVec(N_u,-)` has `|U|=Θ(0)=1`: it must be a *single* corepresentable,
`|Z⊗Q|≅Vec(N,Z)` naturally. A corepresentable preserves all products; I show `Θ` does not when
`dim Q=∞`. Write `Q=k^{(I)}` (`I` infinite; the argument localizes to a countable subfamily), so
`Z⊗Q ≅ ⊕_I Z` and `Θ(Z)=|⊕_I Z|` = finitely-supported functions `I→Z`. Test the product
`∏_{j∈J}Z_j` with `Z_j=k`, `J` infinite. An element of `Θ(∏_Jk)=|⊕_I(k^J)|` has *finite*
`I`-support; its image in `∏_JΘ(k)=∏_J|⊕_I k|=∏_J k^{(I)}` is a `J`-tuple of `I`-vectors all
supported on that one finite `I`-set. The element `y=(e_{i_j})_{j∈J}` with the `i_j∈I` pairwise
distinct (infinitely many `I`-coordinates used) lies in `∏_JΘ(k)` but has no finite-`I`-support
preimage. So the comparison `Θ(∏_JZ_j)→∏_JΘ(Z_j)` is **not surjective**: `Θ` fails to preserve
this product, so it is not corepresentable, hence (given `|U|=1`) not familially representable. ∎

**Theorem 3.2 (the linear closedness dichotomy).**
1. **`Fam_{fin}(Vec_{fd}^op)` (finite shape sets, finite-dimensional positions): `⊗` IS closed.**
   Both conjuncts hold — every `Q_t` is dualizable (fd) [(A)✓ by Lem 3.1], and for finite `T` the
   coproduct `N_ρ=⊕_{t∈T}M_{ρ(t)}⊗Q_t^*` is a *finite* direct sum, still finite-dimensional [(B)✓].
   Internal hom `= (R^T,(⊕_tM_{ρ(t)}⊗Q_t^*)_ρ)` (Theorem 2.3), which lives in `Fam_{fin}(Vec_{fd}^op)`.
2. **`Fam(Vec_{fd}^op)` (arbitrary shape sets, fd positions): `⊗` is NOT closed.** (A) still holds,
   but (B) fails for infinite `T`. *Witness:* `T=ℕ`, all `Q_t=k`, `R={r}`, `M_r=k`. Then
   `Φ(Z)=∏_{t∈ℕ}Vec(k,Z⊗k)=∏_ℕ|Z|=|Z|^{ℕ}=Vec(k^{(ℕ)},Z)` (the last iso is hom out of the
   coproduct `k^{(ℕ)}=∐_ℕ k`). So `Φ` is corepresentable, and by **Yoneda uniqueness** its
   representing object is `k^{(ℕ)}` up to iso — which is **infinite-dimensional**, `∉Vec_{fd}`.
   No object of `Vec_{fd}` can represent `Φ` (a representable has a unique representing object), and
   `Φ(0)=1` forbids a genuinely multi-shape familial representation (`|U|=Φ(0)=1`). So
   `[(ℕ,(k)),({r},k)]` **does not exist** in `Fam(Vec_{fd}^op)`.
3. **`Fam(Vec^op)` (arbitrary positions, full `Vec`): `⊗` is NOT closed either.** (B) is now free
   (`Vec` cocomplete), but (A) fails for infinite-dimensional positions. *Witness:* `T={t}`,
   `Q=k^{(ℕ)}`, `R={r}`, `M=k`. Then `Φ(Z)=Vec(k,Z⊗Q)=|Z⊗Q|` is not familially representable by
   Lemma 3.1. So `[({t},k^{(ℕ)}),({r},k)]` does not exist in `Fam(Vec^op)`.

**The load-bearing conjunct (named).** Closedness needs the internal-hom position
`N_ρ=∐_{t∈T}M_{ρ(t)}⊗Q_t^*` to (i) *make sense* — each `Q_t` dualizable, forcing `Q_t` **fd** over
a linear base (Lemma 3.1) — and (ii) *exist in `C`* — the coproduct `∐_{t∈T}` present. Over `Vec`
these pull in opposite directions the moment `T` is infinite: (i) pins positions to `Vec_{fd}`,
(ii) needs a colimit that escapes `Vec_{fd}`. **The single load-bearing conjunct is the
simultaneous "dualizable-and-summable": `∐_{t∈T}M_{ρ(t)}⊗Q_t^*` an object of `C` with every `Q_t`
dualizable — satisfiable over `Vec` exactly on the finite/fd corner.** Cartesian bases dodge the
collision entirely because Theorem 2.1 never forms `Q_t^*`: the diagonal `Δ:C→C×C` (present in any
cartesian `C`, absent in `Vec`) does the work duals do in the rigid regime, and it costs nothing.

**Correction to the pre-registered prediction.** PROVE.md item 2 conjectured "closedness HOLDS
over `Fam(Vec^op)`, FAILS over `Fam(Vec_{fd}^op)`." The truth (Theorem 3.2) is **it fails over
both**, by *dual* mechanisms — a broken product-closure (B) over `Vec_{fd}`, a broken single-factor
representability (A) over full `Vec` — and holds precisely on `Fam_{fin}(Vec_{fd}^op)`. The
prediction saw conjunct (B) and missed that full `Vec` reintroduces the failure through conjunct
(A) with infinite-dimensional positions.

---

## 4. Reconciliation with the extensivity / biproduct record

The T1 crux was the fullness gap `∐^{Set} ⊊ ⊕` (`Vec` not extensive,
`[[extensivity-is-container-boundary]]`). Is the T2 failure the *same* seam?

**Proposition 4.1 (different seams, one source).** The T1 fullness obstruction and the T2
closedness obstruction over `Vec` are **logically distinct** but share the origin "positions are
`Vec`-objects, shapes are an external `Set`".
- **T1 fullness** is the failure of `C(I,-)=|-|` to preserve the coproduct `⊕` — a property of the
  **unit** `I=k` (`[[fullness-unit-connectedness]]`): `∐^{Set}_t C(I,X_t)↪C(I,∐^C_tX_t)` not onto.
  It is about **morphisms of a fixed extension** and is insensitive to finite-dimensionality.
- **T2 closedness** splits differently: over `Vec_{fd}` it is a **cocompleteness** failure
  (infinite `⊕` leaves `Vec_{fd}` — a defect of the *category*, not of the unit); over full `Vec`
  it is a **dualizability** failure (`-⊗Q` has no left adjoint for infinite-dim `Q` — a defect of
  the *monoidal* structure). Neither is the `|-|`-doesn't-preserve-`⊕` statement of T1.
Thus T2 is **not** the extensivity gap in disguise; it is the *closed-structure* shadow of the same
external-shape/internal-position mismatch, and it bites on the two structural resources a closed
convolution needs — **duals** (to move the tensor argument out of the hom) and **coproducts** (to
represent the product over the whole index). Over `Set` the cartesian diagonal supplies the first
and extensivity is not even invoked; over `Vec` the two resources are jointly available only on the
finite/fd corner. (This confirms, but does not reduce to, the `∐⊊⊕` record: extensivity governs
fullness, dualizable-summability governs closedness.)

---

## 5. Placement against prior art (guardrails)

- **Dorta–Jarvis–Niu `2305.05655`.** Build `⊗` and `◁` over a general `ΣΠV` base and prove
  `◁`-comonoids ≃ enriched categories (Thm 4.2). They **do not** treat closedness of `⊗`. Theorem
  1.1 (the familial-representability criterion) and Theorem 3.2 (the linear dichotomy with named
  conjunct) are the T2 delta over their definitions. *Cite, do not re-derive the tensor.*
- **Day, LNM 137 (1970), Theorem 3.3 + §4.** The closedness tool. Because the enriched domain
  `A=C` is **large**, Day 3.3's "small `A`" clause is unavailable and the internal hom is an end
  that need not be a coproduct-of-corepresentables; §1 is exactly the *representability refinement*
  Day 3.3 leaves open in the large-`A` case. Day's completeness clause (i) is my conjunct (B); the
  "closedness step" `[X⊗\text{coend},TC]≅\text{end}[X⊗-,TC]` is realized here by dualizability
  (conjunct (A)). Consistent, and the refinement is the content.
- **Gambino–Kock `0906.4931`.** Polynomial functors over LCCC bases; `Vec` is not LCCC. This is
  the *fully-internal* construction (shapes internal); mine is the *mixed* `Fam(C^op)` (external
  shapes). Boundary, not contradiction — exactly as for T1 (Rem 3.5 of the fullness file).
- **Niu–Spivak (`Poly` book), Ex 4.78.** Owns the `Set` Dirichlet internal hom; Cor 2.2 recovers it
  as the cartesian instance. Not claimed new.

**Claimed delta.** (i) The reduction Theorem 1.1: `⊗`-closedness ⟺ familial representability of
`Φ`/`Θ`, base-general. (ii) The two-conjunct decomposition and the two sufficient regimes with
explicit internal homs. (iii) Theorem 3.2: over a linear base closedness holds *iff* on the
finite-fd corner, with the load-bearing conjunct named (dualizable-and-summable) and the dual
failure mechanisms over `Vec_{fd}` vs full `Vec` — correcting the pre-registered prediction.

---

## 6. Verification

- **Adjunction cardinality identity (finite fd `Vec`, Theorem 2.3/3.2(1)).** For all families the
  identity `∏_{(s,t)}Σ_r q^{m_rp_sq_t} = ∏_sΣ_{ρ:T→R}q^{(Σ_tm_{ρ(t)}q_t)p_s}` must hold; per
  shape `s`, with `Q:=q^{p_s}`, it is `∏_tΣ_r Q^{m_rq_t}=Σ_ρ∏_t Q^{m_{ρ(t)}q_t}` — the
  distributivity `(★)`. Confirmed symbolically above and numerically: **2000/2000 random small
  families pass**, `q∈{2,3,4}`, `|S|,|T|,|R|∈{1,2,3}`, dims in `{1,2,3}`
  (script `scratch/2026-08-26-t2-closedness-verify.py`).
- **Set Dirichlet internal hom (Cor 2.2).** Same cardinality identity in `Set` form
  (`|Fam((A,X),(B,Y))|=∏_aΣ_b|X_a|^{|Y_b|}`), internal hom `⊔_{ρ:T→R}∏_t(Q_t)^{M_{ρ(t)}}` with
  position size `Σ_t|M_{ρ(t)}|`: **2000/2000 random small finite families pass**, no failing case.
- **Failure witnesses (Theorem 3.2(2,3)).** `Φ(Z)=|Z|^{ℕ}=Vec(k^{(ℕ)},Z)` forces `N=k^{(ℕ)}`,
  infinite-dimensional — position dim `= |T|` grows `1,2,5,20,…` without bound (checked), so no fd
  representative exists; the corepresentability cross-check `|F_q^d|^n=q^{nd}` holds for all tested
  `q,d,n`. The full-`Vec` witness is Lemma 3.1's non-preservation of an infinite product.
  Structural, confirmed numerically where finite.

---

## 7. Status and gaps (precisely stated)

**PROVED.**
- Theorem 1.1 (reduction: `⊗`-closed ⟺ `Φ`/`Θ` familially representable), base-general.
- Theorem 2.1 + Cor 2.2 (cartesian regime: `⊗` closed over any cartesian-closed `C` with
  coproducts; explicit internal hom recovering the `Set`/`Poly` Dirichlet hom).
- Theorem 2.3 (rigid regime: dualizable positions + coproducts ⟹ closed; explicit internal hom).
- Lemma 3.1 (over `Vec`: single-factor familial representability ⟺ dualizable/fd position).
- Theorem 3.2 (linear dichotomy: closed on `Fam_{fin}(Vec_{fd}^op)`; not on `Fam(Vec_{fd}^op)`
  nor `Fam(Vec^op)`; load-bearing conjunct named), *correcting the pre-registered prediction*.

**GAPS.**
1. **General necessity beyond `Vec` and cartesian.** Theorem 1.1 is an exact iff, but I have not
   characterized *which* non-cartesian, non-rigid closed `C` satisfy it. Candidate: `⊗`-closed ⟺
   "`-⊗Q` is a familial (parametric-right-adjoint) functor for every `Q`, and `C` has the induced
   coproducts." Locating the exact class (e.g. does closedness force every position dualizable
   *or* the base cartesian?) is open.
2. **Necessity of dualizability, sharp form.** Lemma 3.1 gives it over `Vec`; whether "single-factor
   familial representability for all `A,Q` ⟹ every `Q` dualizable" holds over a *general* additive
   closed base (or is special to `Vec`'s field-flatness) is not settled.
3. **`◁`-coclosure (secondary target).** Left untouched here — largely known from position-op/`Lan`
   (`[[position-op-monads-to-comonads]]`); the fragile base-general survival criterion of Prop 4.3
   (fullness file) remains conjectured.

---

## 8. Grant framing

T2 completes the "closed structures on `Fam(C^op)`" axis of the theory pillar: `⊗` is closed
exactly on the cartesian bases and the finite-fd linear corner, with the obstruction pinned to two
nameable structural resources (duals, coproducts). For the **applications** narrative this is the
statement that *parallel composition of resource-graded processes admits a currying/internal-hom
(a "process that consumes a `(T,Q)`-process and returns an `(R,M)`-process") exactly when the
resource base is cartesian, or is finite-dimensional-linear with finitely many branches* — the
economic reading of "why linear (quantum/probabilistic) resource types resist higher-order
composition unless finite". Together with T1 (`[[fullness-unit-connectedness]]`) it delimits which
container calculi are genuinely `Set`-enriched phenomena.
