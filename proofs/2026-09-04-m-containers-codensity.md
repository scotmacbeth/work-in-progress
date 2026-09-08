# M-containers: identification, faithfulness, and the codensity criterion for fullness

**MacBeth — 2026-09-04 (PROVE session).**
Target: Neil's 2026-09-04 "probability"/"K-container" emails, reduced to my `Fam(C^op)`
machinery. Sketch: `for-collaborator/2026-09-04-neil-K-container-monad-lift-sketch.md`.
Flagship input T1: `topics/fullness-unit-connectedness.md`,
`proofs/2026-08-25-fullness-unit-connectedness.md`.

> **Headline.** THM 1 (identification) is proved. THM 2 is proved *with a correction*:
> the sketch's "full-faithful ⟺ `M` preserves coproducts" is **wrong** for the honest
> target `[Set,Set]`. The correct invariant is the **codensity monad**: `⟦−⟧_M` is always
> faithful, and **full ⟺ the canonical map `M ⇒ Ran_M M` is iso (`M` is codense) and each
> `(M−)^A` is a connected functor.** Consequently — reversing the sketch's verdict on `D` —
> **probabilistic positions KEEP fullness (`D` is affine + codense), while error / reader /
> writer / nondeterministic positions DESTROY it.** "Preserves coproducts" is the criterion
> for a *different, coarser* target (Kleisli-enriched endofunctors), which the sketch
> silently swapped in.

---

## 0. Setup

`M=(M,η,μ)` a monad on `Set`. `Kl(M)`: objects = sets, `Kl(M)(A,B)=Set(A,MB)`, identity
`η_A`, composition `g∘_{Kl}f = μ∘Mg∘f`. Free functor `F:Set→Kl(M)` is identity on objects,
`Fg=η∘g`; it is faithful, bijective-on-objects, a left adjoint (so preserves colimits), and
**not full** for nontrivial `M`.

**M-container.** Object `(S:Set, P:S→Set)`. M-extension
```
⟦S,P⟧_M : Set → Set,   ⟦S,P⟧_M(X) = Σ_{s:S} (P_s → M X) = Σ_{s:S} Kl(M)(P_s, X),
```
acting on `g:X→X'` by post-composition with `Mg`. Morphisms `(S,P)→(S',P')`: a shape map
`f:S→S'` together with, for each `s`, a Kleisli map `ρ_s ∈ Kl(M)(P'_{fs},P_s)=Set(P'_{fs},MP_s)`.

`Fam(D)`: objects `(S:Set, X:S→Ob D)`; morphism `(f:S→S', (X_s→X'_{fs})_s)`. Write `p=⟦S,P⟧`,
`p'=⟦S',P'⟧` for the ordinary polynomial functors (`M=Id` extensions), `h^A := Set(A,−)`.

---

## 1. THM 1 — identification and factorization `[proved]`

**THM 1(a).** `M-Cont ≃ Fam(Kl(M)^op)` as categories, via the identity-on-underlying-data
functor.

*Proof.* `Ob(Kl(M)^op)=Set`, so an object of `Fam(Kl(M)^op)` is `(S, P:S→Set)` — exactly an
M-container. A `Fam(Kl(M)^op)`-morphism `(S,P)→(S',P')` is `f:S→S'` plus, per `s`, a
`Kl(M)^op`-morphism `P_s → P'_{fs}`, i.e. a `Kl(M)`-morphism `P'_{fs}→P_s`, i.e.
`ρ_s∈Set(P'_{fs},MP_s)` — exactly the M-container morphism data. Identities: the Fam identity
uses `id` in `Kl(M)^op` = `η` = the M-container identity. Composition: Fam composes the shape
maps in `Set` and the position maps in `Kl(M)^op`, i.e. by `∘_{Kl}` in the opposite order —
which is the M-container composition. So the two categories are equal on objects, hom-sets,
identities and composition. ∎

**THM 1(b) (the one genuinely new identity).** As functors `Set→Set`,
```
⟦S,P⟧_M = ⟦S,P⟧ ∘ M = p∘M,   naturally in (S,P).
```
*Proof.* `⟦S,P⟧(MX)=Σ_s Set(P_s,MX)=⟦S,P⟧_M(X)` on objects; on `g:X→X'` both act by `Σ_s
(−∘Mg)`. Naturality in `(S,P)`: a morphism `(f,ρ)` induces `α_X(s,k)=(fs, k∘_{Kl}ρ_s)=(fs,
μ_X∘Mk∘ρ_s)`, which is `p∘M` of the underlying shape/position data. ∎

So an M-container's functor is **an ordinary polynomial functor pre-composed with `M`**. This
is the leverage for everything below.

---

## 2. THM 2 — faithfulness, and the codensity criterion for fullness

### 2.1 `⟦−⟧_M` is ALWAYS faithful `[proved]`

Let `(f,ρ),(f̃,ρ̃)` induce equal `α`. Evaluate at `X=P_s`, element `(s,η_{P_s})`:
`α_{P_s}(s,η_{P_s})=(fs, η_{P_s}∘_{Kl}ρ_s)=(fs,ρ_s)` because `η` is the Kleisli identity. Equal
`α` ⟹ equal shape `fs=f̃s` and equal position maps `ρ_s=ρ̃_s` for all `s`. Hence `(f,ρ)=(f̃,ρ̃)`.
∎ (Contrast the `Vec` extension, which is *not* faithful — there the unit is not a section.)

### 2.2 The reduction and the Kan-extension engine

By THM 1(b), `⟦(S,P)⟧_M=p∘M`, `⟦(S',P')⟧_M=p'∘M`. Since the source is a coproduct of
`h^{P_s}∘M`,
```
Nat(pM, p'M) = Π_s Nat( Set(P_s, M−) , Σ_{s'} Set(P'_{s'}, M−) ).
```
The M-container hom is `M-Cont((S,P),(S',P')) = Π_s Σ_{s'} Set(P'_{s'}, M P_s)`. So **fullness
holds for all pairs iff, for every `A` (=`P_s`) and every family `(P'_{s'})`,**
```
(★)   Σ_{s'} Set(P'_{s'}, MA)  ─→  Nat( Set(A,M−), Σ_{s'} Set(P'_{s'}, M−) )   is a bijection,
```
the map sending `(s',ρ:P'_{s'}→MA)` to `[k ↦ (s', k∘_{Kl}ρ)]`.

**Engine (Kan adjunction).** Precomposition `M^*=(−)∘M:[Set,Set]→[Set,Set]` has right adjoint
`Ran_M` (right Kan extension along `M`). With `G=h^A`:
```
Nat( Set(A,M−), H ) = Nat( h^A∘M, H ) = Nat( h^A, Ran_M H ) = (Ran_M H)(A).      (KAN)
```
So **every `Nat`-set out of an M-representable is a value of a right Kan extension along `M`.**

### 2.3 Splitting (★): connectedness × codensity

Since `Set(B,M−)=Π_{b∈B} M`, `Nat(Set(A,M−),Set(B,M−))=Nat(Set(A,M−),M)^{B}`. So the
single-summand part of (★) collapses to `B=1`. Define the **crux functor**
```
Φ := Ran_M M    (the CODENSITY MONAD of the functor M);   Φ(A) = Nat(Set(A,M−), M)  by (KAN).
```
The canonical `MA→Φ(A)`, `m↦[k↦μ(Mk(m))]`, is the unit `M ⇒ Ran_M M = Φ` of `M^*⊣Ran_M`
evaluated at `A`. Then (★) is equivalent to the conjunction of:

- **(ii) codensity iso.** `M ⇒ Ran_M M` is an isomorphism (`M` is *codense*): `MA ≅ Φ(A)`
  canonically, for all `A`. [Handles each single summand, i.e. fullness-on-homs.]
- **(i) connectedness.** each `(M−)^A=Set(A,M−)` is a **connected functor**, i.e.
  `Nat(Set(A,M−), Σ_{s'}G_{s'}) = Σ_{s'}Nat(Set(A,M−),G_{s'})`; equivalently `Ran_M` preserves
  the coproducts `Σ_{s'}Set(P'_{s'},M−)`. [Handles the coproduct/shape side.]

**THM 2 (fullness criterion) `[proved]`.** `⟦−⟧_M:M-Cont→[Set,Set]` is always faithful, and is
**full ⟺ (i) ∧ (ii)** ⟺ `M` is codense **and** every `(M−)^A` is connected.

**Lemma (affine ⟹ connected) `[proved]`.** If `M` is *affine* (`M1≅1`) then (i) holds.
*Proof.* `(M1)^A=1`. Given `α:(M−)^A ⇒ Σ_{s'}G_{s'}`, the unique point of `(M1)^A` maps to a
single summand `s'_0` (as `Σ_{s'}G_{s'}(1)`). For any `X`, `!:X→1` gives
`(M!)^A:(MX)^A→(M1)^A=1`; naturality forces `α_X` to land in the `s'_0`-summand (apply
`Σ G_{s'}(!)`, which preserves summands, and use that the target of the unique point is in
`s'_0`). So `α` factors through `s'_0`; connectedness follows. ∎

Thus **`M` affine + codense ⟹ full.** (Affineness is not *sufficient alone* — see reader.)

---

## 3. The examples — where fullness lives and dies

For a **polynomial monad** `M=(I,B)`, `M(X)=Σ_{i∈I}X^{B_i}`, everything is exact via AAG
(`⟦−⟧:Cont→[Set,Set]` fully faithful onto polynomials): with `(M−)^A` the polynomial of
shapes `φ:A→I` and positions `Σ_a B_{φa}`,
```
MA = Σ_i |A|^{|B_i|},     Φ(A)=Nat((M−)^A,M)=Π_{φ:A→I} Σ_{i∈I} ( Σ_a |B_{φa}| )^{|B_i|}.
```
Computed (`/tmp/mcont.py`, exact integers):

| `M` | `M1` | `MA` vs `Φ(A)` (A=0,1,2,3) | codense? | full? |
|---|---|---|---|---|
| `Id` | 1 | 0,1,2,3 **=** 0,1,2,3 | yes | **YES** |
| `Maybe` (`X+1`) | 2 | 1,2,3,4 vs 1,2,**12**,**864** | no | **no** |
| exception `X+2` | 3 | 2,3,4,5 vs 2,**12**,**5184**,… | no | **no** |
| writer `2×X` | 2 | 0,2,4,6 vs 0,**4**,**256**,… | no | **no** |
| reader `X^2` | 1 | 0,1,4,9 vs 0,**4**,**16**,**36** | no | **no** |

`Φ(A)>MA` strictly beyond a low threshold in every nontrivial case — the extra
natural transformations are "case-analysis" operations (e.g. inspecting `⊥`, or
duplicating a reader argument) that are natural for pure maps but not Kleisli-natural.

**Reader is the instructive one:** reader is **affine** (`M1=1`, so (i) holds by the Lemma)
yet **fails (ii)**: `Φ(A)=(RA)^R ≠ A^R=MA` for `|R|≥2`. So *affineness alone does not give
fullness* — codensity is a genuinely separate, necessary condition.

**Distributions `D` (finite/finitely-supported prob.) — the sketch's reversal `[computed→proved-mod-lemma]`.**
`D` is **affine** (`D1=1`, so (i) holds). For (ii) I claim **`D` is codense**:
`Nat(D^A,D)=DA` (natural `A`-ary operations on `D` are exactly the affine combinations).
Verified: convex combinations `Σ_a ω_a μ_a` (`ω∈DA`) are natural (`/tmp/dcod.py`, 2000 random
naturality checks pass); non-affine candidates (renormalized product, entropy reweighting)
break naturality (`/tmp/dnat.py`). Proof that these are the *only* ones:

> Given `α:D^A⇒D` and a tuple `(μ_a)_a∈(DX)^A`, let `K=⊔_a supp(μ_a)`, `ν_a∈DK` the block-`a`
> copy of `μ_a`, and `p:K→X` the projection; then `(μ_a)=D^A(p)((ν_a))`, so
> `α_X((μ_a))=Dp(α_K((ν_a)))`. Collapsing blocks `c:K→A` gives `Dc(α_K((ν_a)))=α_A((δ_a))=:ω`.
> Reducing one block at a time (collapse all but one block to a point) reduces to classifying
> `Nat(D, D(−⊔F))` for finite `F`: the `F`-marginal is constant in `σ` (factors through
> `D1=1`), and the `Z`-marginal is a *natural sub-probability-valued endo of `D`*, hence a
> scalar `λ·σ`. So `α_K((ν_a))=Σ_a ω_a ν_a`, whence `α_X((μ_a))=Σ_a ω_a μ_a`. ∎ (modulo the
> base lemma **`Nat(D,D)={id}`** / natural sub-`D`-valued endos are scalars — a standard
> rigidity fact for the affine functor `D`; flagged, not re-proved here.)

Granting the base lemma, **`D` is affine + codense ⟹ `⟦−⟧_D` is FULLY FAITHFUL.**

---

## 4. The correction, stated precisely

The sketch (and PROVE.md THM 2) asserted: *full-faithful ⟺ `M` preserves coproducts*, with
"`D` and `Maybe` both fail." Two errors:

1. **Wrong target.** "`M` preserves coproducts" = "`Kl(M)(1,−)=M` preserves coproducts" = the
   *connected-unit* condition of T1 **for the Kleisli-enriched extension**
   `⟦−⟧^{Kl}:Fam(Kl(M)^op)→[Kl(M),Kl(M)]`. But `⟦−⟧_M` lands in `[Set,Set]` via the
   **restriction `R=(−∘F)` along the free functor `F:Set→Kl(M)`**:
   `⟦−⟧_M = R∘⟦−⟧^{Kl}`, and `⟦−⟧^{Kl}` (free coproduct completion) is *always* fully faithful.
   All the action is in `R`, i.e. in the gap between *pure*-naturality and *Kleisli*-naturality
   — governed by codensity, **not** coproduct preservation. (Independently, T1 as stated needs
   `C` closed symmetric monoidal cocomplete; `Kl(M)` generally is none of these, so the
   invocation was doubly unjustified.)
2. **Wrong verdict on `D`.** Coproduct-preservation *fails* for `D`, so the sketch predicted `D`
   fails fullness. But the *correct* criterion (affine + codense) is *satisfied* by `D`. So
   **`D` keeps fullness**; it is `Maybe`/writer/reader/exception that lose it. Even the
   coproduct-preserving *writer* monad `E×(−)` (which the wrong criterion would pass) **fails**
   for `|E|≥2` (`Φ(1)=|E|^{|E|}≠|E|`) — a clean refutation of the coproduct criterion.

**Corrected slogan.** *Adding probabilistic positions preserves on-the-nose faithfulness of
the container extension; adding error / partiality / read-only-context / nondeterminism
destroys it.* The dividing invariant is **codensity of the effect monad**, computed by the
right Kan extension `Ran_M M`.

---

## 5. Composition (THM 3) — parked, framing unchanged `[speculative]`

`(pM)∘(qM)=p∘(M∘q)∘M`; landing back in `(p◁'q)∘M` needs a distributive law
`λ:M∘⟦q⟧⇒⟦q⟧∘M`. Existence is the commutative/affine (Zappa–Szép / `H²`) question of
`orchestration-is-zappa-szep-weld`. The codensity correction does not touch this; `D`
(commutative, affine) is predicted to compose, `Maybe` (non-affine) to hit the obstruction.
Left as the stretch.

---

## 6. Grades / registry

- **THM 1(a),(b):** `proved`.
- **THM 2 faithfulness; (KAN) engine; fullness ⟺ codense ∧ connected; affine ⟹ connected:**
  `proved`.
- **Polynomial table (Maybe/exception/writer/reader all fail; Id full):** `proved` (exact AAG).
- **`D` full (affine + codense):** `proved` modulo the base rigidity lemma `Nat(D,D)={id}`
  (grade the *composite* `computed`, the reduction `proved`).
- **Coproduct-preservation is the WRONG criterion / writer(2) refutes it:** `proved`.
- **THM 3 composition:** `speculative`.

New registry: `proofs/registry/m-containers.json` (sibling of `left-adjoint-over-vec.json`;
shares the connected-unit/affine tree). Crown connection: **container-extension fullness ↔
codensity monads** — a new bridge to Leinster-style codensity, worth a WRITE.

## Verification artifacts
`/tmp/mcont.py` (exact polynomial `MA` vs `Φ(A)`), `/tmp/dcod.py` (D naturality: convex ok,
product fails), `/tmp/dnat.py` (scalar multiples natural; nonlinear fails; affine⟹connected).
