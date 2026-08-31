# The copowers–coproducts gap for the connected unit:
# a writer-monad reduction, an extensivity upgrade, and the sharp residual

**MacBeth — 2026-08-26 (PROVE session).** Follows the flagship T1
(`proofs/2026-08-25-fullness-unit-connectedness.md`, **proved**). That theorem showed the
container extension `⟦−⟧ : Fam(C^op) → C\text{-}[C,C]` is fully faithful **iff the monoidal unit
`I` is connected**, i.e. `C(I,-):C→Set` preserves small coproducts. This file resolves the
follow-on gap (§6.1 of the flagship, PROVE.md UID-continuation):

> **(Q)** For the unit `I` of a closed symmetric monoidal `C` with small coproducts, does
> `C(I,-)` **preserving all copowers `κ·I = ∐_κ I`** (the one-parameter test `γ_κ : κ·C(I,I) →
> C(I,κ·I)` iso) imply `C(I,-)` **preserves all small coproducts `∐_t X_t`**?

**Headline.** The copower test is exactly the statement that the canonical Set-monad
`T = C(I,(-)·I)` induced by the adjunction `(-)·I ⊣ C(I,-)` is the **writer monad `(-)×M`** for
the commutative monoid `M = End(I)`. Under this identification the upgrade (Q) becomes: *does the
comparison functor `K : C → M\text{-}Set` preserve coproducts?* I prove:

1. **(Reduction, proved.)** (A) ⟺ `T = (-)×M` writer monad ⟺ `K:C→M\text{-}Set`,
   `K(X)=(C(I,X),\ \text{precomposition by }End(I))`, preserves **copowers of `I`**; and
   **(C) ⟺ `K` preserves all coproducts**. The surjectivity of the general comparison `γ`
   reduces to liftability of points through `∐_t ε_{X_t}` (the coproduct of counits).
2. **(Extensivity upgrade, proved.)** If `C` is **extensive** then
   **(A) ⟺ (C) ⟺ `I` is indecomposable and non-initial**. So over every extensive base
   (Set, all presheaf/Grothendieck toposes, `Set×Set`, …) the flagship's fullness reduces to the
   **one-parameter copower test** — the criterion is checkable.
3. **(Residual, honestly open.)** Without extensivity the raw implication (A)⟹(C) is reduced to the
   sharp condition "`K` preserves coproducts / `I` is coproduct-connected"; I isolate the exact
   obstruction (a mixed point not lifting through `∐ ε_{X_t}`) and show that **every natural
   construction that could separate them fails** (additive/pointed bases fail (A); extensive bases
   satisfy the equivalence; Day-convolution and Artin-gluing bases satisfy both). Existence of a
   non-extensive base passing (A) yet failing (C) is the sharpened open question.

The practical payoff for the grant: **the copower test certifies fullness on the entire zoo of
intended bases**, with a theorem, not folklore.

---

## 0. Setup

Fix a closed symmetric monoidal `(C,⊗,I,[-,-])` with small coproducts `∐`. Write
`U := C(I,-) : C → Set` (the *points* / global-elements functor) and, for a set `S`, the copower
`S·I := ∐_{S} I`. The comparison map of interest (flagship Def 1.4) is, for a family `(X_t)_{t∈T}`,
```
        γ_{(X_t)} :  ∐^{Set}_{t} C(I,X_t)  ⟶  C(I, ∐^{C}_{t} X_t),   (t, x) ↦ inj_t ∘ x.
```
Three nested conditions:

- **(A)** `U` preserves **copowers of the unit**: `γ` iso for every *constant* family `(I)_{t∈T}`.
  Equivalently `γ_κ : κ·M → C(I,κ·I)` iso for all cardinals κ, where `M := C(I,I)=End(I)`.
- **(B)** `U` preserves copowers of **every** object `Z`: `γ` iso for all constant families.
- **(C)** `U` preserves **all** small coproducts (`I` **connected**): `γ` iso for all families.

Trivially `(C)⇒(B)⇒(A)`. (Q) asks whether `(A)⇒(C)`.

---

## 1. The adjunction and the writer-monad reduction

**Lemma 1.1 (the copower adjunction).** `(-)·I : Set → C` is left adjoint to `U = C(I,-)`.

*Proof.* `C(S·I, X) = C(∐_S I, X) = ∏_S C(I,X) = Set(S, C(I,X))`. ∎

**Lemma 1.2 (`(-)·I` is strong symmetric monoidal; `U` is lax).** With `(Set,×,1)` and `(C,⊗,I)`,
`F := (-)·I` is strong symmetric monoidal: `F(1)=I` and `F(S)⊗F(S') = (S·I)⊗(S'·I) ≅ (S×S')·(I⊗I)
≅ (S×S')·I = F(S×S')`, using that `⊗` is cocontinuous in each variable (closedness) and `I⊗I≅I`.
Its right adjoint `U` is therefore lax symmetric monoidal, with laxator
`∇_{X,Y}:U(X)×U(Y)→U(X⊗Y)`, `(x,y)↦ x⊗y` (via `I≅I⊗I`), and unit picking `id_I∈M=U(I)`. In a
*symmetric* monoidal category `M=End(I)` is a **commutative** monoid (Eckmann–Hilton on `id_I`). ∎

Let `T := U F : Set → Set`, `T(S) = C(I, S·I)`, the monad of the adjunction. Its underlying
endofunctor evaluated at `S` is exactly the codomain of the copower comparison `γ`. Hence:

**Theorem 1.3 (Reduction A — the writer monad).** The following are equivalent:
1. **(A)** `U` preserves copowers of `I`;
2. the comparison `γ_κ : κ×M → T(κ)` is a natural isomorphism, i.e. `T(S) ≅ S×M` naturally;
3. `T` is the **writer monad** `(-)×M` of the commutative monoid `M=End(I)` (unit `s↦(s,id_I)`,
   multiplication `S×M×M → S×M` via the monoid product of `M`).

*Proof.* (1)⇔(2) is the definition of (A) at the constant family `(I)_κ` (note `C(I,X_t)=C(I,I)=M`).
For (2)⇔(3): the adjunction unit `η_S : S → T(S)=C(I,S·I)` is `s ↦ inj_s`, which under `γ` is
`(s,id_I)` — the writer unit. The multiplication `μ = U ε F` restricts, under `γ`, to the map
`S×M×M → S×M` induced by composition in `End(I)`; associativity/unitality are those of the monoid
`M`. Thus the monad structure transported along the natural iso `γ` is precisely the writer monad;
conversely if `T=(-)×M` as a monad then `γ` (the unique comparison compatible with `η`) is iso. ∎

**Remark 1.4.** (A) is a *strong* condition: it forces the induced monad to be the simplest possible
(a product with a monoid). This already explains why the "obvious" disconnected bases fail (A)
rather than merely failing (C): over any **additive/pointed base** (`Vec`, `R\text{-}Mod`, `CMon`,
`Set_*`, `Rel`, …) the zero morphism `0:I→I` and the shared zero point make `T(κ)=C(I,∐_κ I)` carry
"sums", so `T(κ)⊋κ×M` — (A) fails at the first step. See §4.

---

## 2. The Eilenberg–Moore comparison, and Reduction B for (C)

Algebras for the writer monad `(-)×M` are exactly **`M`-sets** (a structure map `S×M→S` = a monoid
action). So under (A) the Eilenberg–Moore category is `EM(T) = M\text{-}Set`, and the adjunction
`F⊣U` factors through the comparison functor
```
        K : C ⟶ M\text{-}Set,     K(X) = (\,C(I,X),\ ·\,),   x·m := x∘m  (m∈End(I)),
```
i.e. `K(X)` is the set of points of `X` with `End(I)` acting **by precomposition**.

**Lemma 2.1 (`K` computes points, and detects coproduct-preservation).**
`U = (\text{forgetful } M\text{-}Set→Set) ∘ K`. The forgetful functor `M\text{-}Set→Set` **creates
all colimits** (it is evaluation of the presheaf category `[M,Set]` at the unique object). Hence for
any small family `(X_t)`:
```
        U \text{ preserves } ∐_t X_t   ⟺   K \text{ preserves } ∐_t X_t.
```

*Proof.* The structure map of `K(X)` is `U(ε_X):U(FUX)=UX×M→UX`, `(x,m)↦ ε_X∘inj_x∘m = x∘m` (using
`ε_X∘inj_x=x`); so the action is precomposition. `M\text{-}Set→Set` creates colimits (pointwise
colimits in a functor category), so a coproduct is preserved downstairs iff `K` preserves it
upstairs. ∎

**Theorem 2.2 (Reduction B).** Assume (A). Then **(C) holds ⟺ the comparison `K:C→M\text{-}Set`
preserves all small coproducts.** Moreover `K` **always** preserves copowers of `I` (that is exactly
the content of (A): `K(κ·I)=κ·K(I)=κ×M` in `M\text{-}Set`). Thus (Q) is precisely:

> *Does a functor `K:C→M\text{-}Set` arising as `C(I,-)`, known to preserve the single family of
> copowers of `I`, preserve all coproducts?*

*Proof.* Immediate from Lemma 2.1 and (A). ∎

### 2a. Where surjectivity of `γ` lives: liftability through `∐ε`

The following pins the obstruction and will guide both the extensivity proof and the residual.

**Lemma 2.3 (γ = points of the counit-coproduct).** For a family `(X_t)_{t∈T}` put
`A := ∐_t C(I,X_t)` and let `e := ∐_t ε_{X_t} : A·I = ∐_t (C(I,X_t)·I) → ∐_t X_t` (using
`∐_t(S_t·I)=(∐_t S_t)·I`). Then, under (A), `γ_{(X_t)} = U(e)∘η_A` where `η_A:A→U(A·I)=A×M` is the
writer unit `a↦(a,id_I)`. Consequently:
```
        U(e) surjective  ⟹  γ_{(X_t)} surjective.
```

*Proof.* For `a=(t,x)∈A`, `η_A(a)=(a,id_I)` corresponds under (A) to `inj_a:I→A·I`, and
`e∘inj_a = ε_{X_t}∘inj_x = inj_t∘x`, i.e. `U(e)(η_A(a))=inj_t∘x=γ(a)`. If `U(e)` is onto then any
`f:I→∐_tX_t` is `e∘g` with `g∈U(A·I)=A×M`, so `g=inj_a∘m` (a=(t,x), m∈M) and
`f=e∘inj_a∘m=inj_t∘(x∘m)=γ(t,\,x∘m)`. ∎

**Remark 2.4 (why a *single* object never obstructs — but a coproduct can).** For one object `X`
the counit `ε_X:FUX→X` has `U(ε_X)` a **split epi** in `Set` (split by `η_{UX}`, since
`U(ε_X)∘η_{UX}=id`), so points always lift through `ε_X`. But `η_{UX}` is a *Set*-map, not a
`C`-map, so `ε_X` need **not** be split in `C`; hence `e=∐_tε_{X_t}` need not have `U(e)` surjective.
**This is the precise crack**: a *mixed point* `f:I→∐_tX_t` failing to lift through `∐_tε_{X_t}`
gives `γ` non-surjective while (A) still holds. The remainder of the file asks whether the crack can
ever be pried open.

---

## 3. The extensivity upgrade (the applications-covering theorem)

**Theorem 3.1 (upgrade under extensivity — proved).** Let `C` be closed symmetric monoidal with
small coproducts and **extensive** (coproducts disjoint and universal). Then
```
        (A) ⟺ (B) ⟺ (C) ⟺ I is indecomposable and non-initial ⟺ I is connected.
```
In particular the flagship's fullness of `⟦−⟧` over an extensive base is decided by the
**one-parameter copower test** `γ_κ:κ×M→C(I,κ·I)`.

*Proof.* `(C)⇒(A)` is trivial. For `(A)⇒(C)` I show (A) forces `I` connected; extensivity then
gives coproduct preservation for connected objects.

*Step 1: (A) ⟹ `I` non-initial.* If `I` were initial then `C(I,X)=1` for all `X`, so
`C(I,κ·I)=1≠κ=κ×M` for `κ≥2` (here `M=C(I,I)=1`), contradicting (A).

*Step 2: (A) ⟹ `I` indecomposable.* In an extensive category, for any object `A`,
```
        C(A, ∐_{t} X_t) ≅ ∐_{(A=∐_t A_t)} ∏_t C(A_t, X_t)                     (†)
```
the coproduct ranging over `T`-indexed coproduct decompositions `A≅∐_tA_t` (this is the defining
equivalence `C/∐_tX_t ≃ ∏_t C/X_t`). Apply (†) with `A=I`, `T=2`, `X_0=X_1=I`:
`C(I,I⊔I)=∐_{I=A_0⊔A_1} C(A_0,I)×C(A_1,I)`. The two **trivial** decompositions `(I⊔0),(0⊔I)`
contribute `C(I,I)×C(0,I) ⊔ C(0,I)×C(I,I) = M ⊔ M = 2×M`, and this is exactly the image of `γ_2`
(a point into the first or second summand). Suppose a **nontrivial** decomposition `I=A_0⊔A_1`
existed (both `A_i` non-initial). It yields the map `φ:I=A_0⊔A_1 → I⊔I` equal to
`inj_0∘inj_{A_0}` on `A_0` and `inj_1∘inj_{A_1}` on `A_1`. In an extensive (hence disjoint)
category `φ` factors through neither `inj_0:I→I⊔I` nor `inj_1` (that would force `A_1` resp. `A_0`
initial). So `φ ∉ \mathrm{im}(γ_2)`, i.e. `γ_2` is **not surjective** — contradicting (A). Hence no
nontrivial decomposition: `I` is indecomposable.

*Step 3: indecomposable + non-initial ⟹ connected.* By (†) with `A=I`: the only decompositions of
`I` are trivial (one summand `=I`, rest initial), so `C(I,∐_tX_t)=∐_t C(I,X_t)` — `U` preserves all
coproducts. ∎

**Corollary 3.2 (the flagship criterion is checkable on every extensive base).** Over
`C=Set` (`1` connected: full), any **presheaf topos `[𝔻,Set]`** or **Grothendieck topos** (extensive;
unit connected ⟺ the site/terminal is connected), or `Set×Set` (extensive; unit `(1,1)`
*decomposable*, so `γ_2` already fails: not full — recovering flagship Cor 3.3), fullness of `⟦−⟧`
is equivalent to the one-parameter copower test. No mixed family need ever be inspected. ∎

**Remark 3.3 (this *is* the intended zoo).** Every cartesian-closed / topos-theoretic base of
interest for the container calculus is extensive, so Theorem 3.1 discharges the practical form of
(Q) completely. The only closed monoidal bases in the program that are *not* extensive are the
**additive** ones (`Vec`, `R\text{-}Mod`, semiadditive `CMon`), and there (A) already fails (§4).
So on the union of all bases the flagship actually ranges over, **(A) certifies fullness**.

---

## 4. Why the standard non-examples never separate (A) from (C)

This section records the evidence that the residual §5 gap is genuinely hard to populate: every
natural family either satisfies the full equivalence or fails already at (A).

**(i) Additive / pointed / semiadditive bases fail (A).** If `C` has a zero object then
`0:I→I∈M` and the zero point is shared across all coproduct injections, so
`C(I,∐_κ I)` carries cross-summand structure:
- `Vec/R\text{-}Mod`: `C(I,∐_κ I)=|R^{(κ)}|` (finite-support tuples) ⊋ `κ×|R|`; `γ_κ` misses
  `e_1+e_2`. (A) fails. [flagship Cor 3.2]
- `CMon` (semiadditive, `⊕=∏`): `C(ℕ,∐_κℕ)=|ℕ^{(κ)}|⊋κ×ℕ`. (A) fails.
- `Set_*` (smash, `I=S^0`): `C(S^0,∐_κ S^0)=κ+1` while `κ×M=2κ`; (A) fails (basepoint collapse).
- `Rel` (`I=1`, zero object `∅`): `C(1,∐_κ1)=𝒫(κ)=2^κ ⊋ 2κ`; (A) fails.

**(ii) Thin bases (quantales/frames) fail (A).** In a poset `∐_κI=⋁_κI=I` (idempotent join), so
`C(I,∐_κI)=C(I,I)` has one element while `κ×M=κ`; `γ_κ` fails for `κ≥2`.

**(iii) Extensive bases satisfy the equivalence (Theorem 3.1).** Presheaf toposes `[𝔻,Set]`:
`U=ev_i` if the Day unit is representable, or `U=(-)^{fixed pts}` for group/monoid actions — always
preserves *all* colimits when the unit is connected, and fails at copowers when the site is
disconnected (`Set×Set`). No separation.

**(iv) Day-convolution bases have connected unit.** For `[𝔸,Set]` with Day tensor, the unit is the
representable `𝔸(i,-)`, and `U=C(I,-) = ev_i` (enriched Yoneda), which preserves **all** colimits
(pointwise). So (C) holds outright; no separation.

**(v) Artin gluing `Gl(T)` for `T:Set→Set` product-preserving, coproduct-*non*-preserving.**
Take `T=(-)^2`, `Gl(T)=(Set↓T)` (a CCC with coproducts, **non-extensive** because coproducts in the
`B`-coordinate use `T(B⊔B')=(B⊔B')^2≠TB⊔TB'`). The unit is `I=(1,1,\,*↦(*,*))`, `M=End(I)=1`, and
```
        C(I,(A,B,β)) = β^{-1}(Δ_B)   (points = elements landing on the diagonal of B^2).
```
Copowers: `κ·I=(κ,κ,\,\mathrm{diag})`, so `C(I,κ·I)=κ` — **(A) holds**. But the diagonal
subobject is **disjoint-union-local**: for `X⊔Y`, a point lands on `Δ_{B⊔B'}` iff it lands on `Δ_B`
or `Δ_{B'}` (the injections `B,B'↪B⊔B'` are disjoint, so `Δ_{B⊔B'}=Δ_B⊔Δ_{B'}` on the image of
points), whence `C(I,X⊔Y)=C(I,X)⊔C(I,Y)` — **(C) also holds**. *(Verified numerically:
`scratch/2026-08-26-gluing-copower-check.py` — copowers give exactly κ points for κ≤5, and 100
random binary coproducts show 0 mismatches.)* So even this deliberately non-extensive, non-additive
CCC fails to separate: the point-selecting subobject localizes over coproducts.

The moral of (v): to separate (A) from (C) one needs a base whose "point-selecting data" is **not**
coproduct-local while copowers of `I` stay clean — and gluing along a product-preserving functor
never produces this (the diagonal that defines points is always local).

---

## 5. The sharp residual (honestly open) and the exact obstruction

**Status of (Q).** For the intended (extensive or additive) bases, (Q) is **settled** (Thm 3.1 +
§4). The residual purely-logical question is:

> **(Q′)** Does there exist a closed symmetric monoidal `C` with small coproducts that is
> **non-extensive**, satisfies **(A)** (`C(I,-)` preserves copowers of `I`, i.e. `T=(-)×M`), yet
> fails **(C)**?

By Theorem 2.2 this is equivalent to: *a comparison `K:C→M\text{-}Set` that preserves copowers of
`I` but not all coproducts*. By Lemma 2.3 & Remark 2.4 a separating `C` must exhibit a **mixed
point** — a morphism `f:I→∐_tX_t` not factoring through any injection `inj_t` (surjectivity
failure), or two point-data identified after injection (injectivity failure) — while `I⊔I` stays
clean. The obstruction is exactly the failure of `U(∐_tε_{X_t})` to be surjective (resp. injective),
i.e. `I` fails to be a **coproduct-connected generator** even though it is connected on its own
copowers.

**What is proved about (Q′).**
- *Necessary conditions on a separator:* non-extensive (Thm 3.1), non-additive/no zero object and
  non-thin (§4), and `I` not a strong generator (Rem 2.4). This rules out every standard base.
- *A clean sufficient condition making (A)⟹(C):* any of {`C` extensive; `U=C(I,-)` monadic (then
  `C≃M\text{-}Set` and the forgetful functor preserves coproducts); `I` a strong generator that is
  `⊗`-projective on coproducts}. Under any of these the crack of Rem 2.4 cannot open.

**My assessment (not a proof).** The reduction shows closedness controls maps *out* of coproducts
(`[∐X_t,Y]=∏[X_t,Y]`, always true, vacuous here) but gives **no** handle on maps *into* coproducts,
which is what `U(∐)` is. So there is no *a priori* monoidal reason for the upgrade; the upgrade is a
consequence of **extensivity**, not of closedness. I therefore expect (Q′) to have a positive
answer (a separator exists) in some exotic non-extensive base, but I have **not** constructed one —
every construction I can build (§4) localizes points over coproducts. **This is the precise, honest
boundary.**

---

## 6. Verification

- **Gluing `Gl((-)^2)`** (§4v): `scratch/2026-08-26-gluing-copower-check.py`. Copowers of `I`
  have exactly `κ` points (κ=1..5); 100 random binary coproducts preserve points (0 mismatches).
  Confirms (A)∧(C), a non-separator, as argued by hand.
- **Additive/pointed failures of (A)** (§4i): the `Vec/F_3` numbers of flagship §5 (`domain 6`,
  image `5` of `9`) are the copower failure at `κ=2,Z=I`; recomputed consistently.
- **Extensive decomposition (†)** and Step 2 of Thm 3.1: checked by hand on `Set` (only trivial
  decompositions of `1`, `γ` iso) and `Set×Set` (nontrivial decomposition of `(1,1)=(1,0)⊔(0,1)`
  gives the "crossed" transformation, `γ_2` non-surjective — the flagship Cor 3.3 witness).

---

## 7. Status and provenance

**PROVED this session:**
- **Theorem 1.3** (Reduction A): (A) ⟺ the induced Set-monad `C(I,(-)·I)` is the writer monad
  `(-)×End(I)`. [structural; adjunction + Eckmann–Hilton]
- **Theorem 2.2** (Reduction B): under (A), (C) ⟺ the EM-comparison `K:C→End(I)\text{-}Set`
  preserves coproducts; `K(X)=(C(I,X),\text{precomposition})`. [Beck/EM + colimit-creation]
- **Lemma 2.3 / Remark 2.4**: `γ=U(∐ε)∘η`; surjectivity of `γ` ⟸ liftability through `∐ε`; the
  single-object counit is `U`-split but the coproduct need not be — the exact crack.
- **Theorem 3.1** (extensivity upgrade): extensive ⟹ (A)⟺(B)⟺(C)⟺ `I` indecomposable & non-initial.
  **This discharges (Q) for every intended base** (Cor 3.2, Rem 3.3).
- **§4**: additive/pointed/semiadditive/thin bases fail (A); extensive/Day/gluing bases satisfy the
  equivalence — so none separates. `Gl((-)^2)` computed.

**OPEN (sharpened, do not overclaim):**
- **(Q′)**: existence of a *non-extensive* closed symmetric monoidal base satisfying (A) but not (C).
  Reduced to "`K` preserves coproducts / `I` coproduct-connected"; obstruction identified
  (mixed point non-lifting through `∐ε`); ruled out for all standard bases; **not resolved in
  general**. Registered as **computed/partial**, not proved.

**Prior-art guardrail.** The writer-monad-of-a-monoidal-adjunction and `EM=M\text{-}Set` facts are
standard category theory (Kleisli/Eilenberg–Moore; the copower adjunction `(-)·I⊣C(I,-)` is folklore).
The **delta** is their assembly into a decision procedure for the flagship's fullness criterion, and
the extensivity upgrade Theorem 3.1 identifying `I` indecomposable+non-initial as the exact,
checkable content of "connected unit" over extensive bases. Dorta–Jarvis–Niu (arXiv:2305.05655) do
not treat fullness/connectedness (cited for `⊗,◁` definitions only); Gambino–Kock (0906.4931) place
`Vec` outside LCCC — consistent with additive bases failing (A) here.
