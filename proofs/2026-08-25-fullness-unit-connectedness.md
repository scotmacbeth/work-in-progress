# The fullness criterion for the container extension over a closed base:
# connectedness of the monoidal unit — and why it is *not* extensivity

**MacBeth — 2026-08-25 (PROVE session).** Answers Neil's #1 request (email UID 120):
*do the four monoidal structures on containers generalize to `Fam(C^op)`, and is the
extension full/faithful — is the controlling hypothesis extensivity?* This file settles the
**flagship T1** (full/faithful) and states T2/T3 as corollaries + honest gaps.

**Headline.** The extension `⟦−⟧ : Fam(C^op) → C\text{-}[C,C]` is fully faithful **iff the
monoidal unit `I` is a connected object**, i.e. `C(I,-) : C → Set` preserves small
coproducts. This is the precise general form of the Abbott–Altenkirch–Ghani representation
theorem. **It is NOT extensivity of `C`:** `C = Set×Set` is (l)extensive yet `⟦−⟧` is not full
(its unit `(1,1)` is disconnected), and `C = Vec` fails for the dual reason (the unit `k` is
connected as an *object* but `C(k,-)` = the forgetful functor does not preserve `⊕`). The
correct invariant sits one notch away from Neil's conjecture, and the gap is a theorem, not a
hand-wave.

---

## 0. Setup and standing hypotheses

Fix a **closed symmetric monoidal category** `(C, ⊗, I, [-,-])` with **small coproducts**
`∐`. Closedness makes `C` enriched over itself: the hom-object is the internal hom `[-,-]`,
and `C(A,B) = C(I, [A,B])` (points of the internal hom), naturally. Write `V := C` for the
base of enrichment when we want to emphasize the enriched viewpoint.

**Definition 0.1 (container over `C`).** `Fam(C^op)` has objects `(S,(P_s)_{s∈S})` — `S` a
set of *shapes*, `P_s ∈ C` a *position object* — and morphisms `(S,P)→(T,Q)` the pairs
`(f,(φ_s))` with `f:S→T` and `φ_s : Q_{f(s)} → P_s` in `C`. Explicitly
`Fam(C^op)((S,P),(T,Q)) = ∏_{s∈S} ∐^{Set}_{t∈T} C(Q_t, P_s)` (Set-coproduct = a *choice* of
one `t=f(s)` plus a morphism), exactly as for Set-containers.

**Definition 0.2 (extension).** `⟦S,P⟧ := ∐_{s∈S} [P_s, -] : C → C`, a coproduct of the
corepresentable `C`-functors `[P_s,-]`. This is a `C`-enriched endofunctor. Write
`h_P := [P,-]` for the corepresentable at `P`; note `h_I = [I,-] ≅ Id`. The extension is a
functor `⟦−⟧ : Fam(C^op) → C\text{-}[C,C]` into the category of `C`-enriched endofunctors and
`C`-natural (=enriched) transformations.

- `C = Set` (cartesian closed, `I=1`, `[P,X]=X^P`, `∐`=disjoint union): recovers the classical
  container extension `⟦S,P⟧X = ∐_s X^{P_s}` into `[Set,Set]`.
- `C = Vec` (closed, `I=k`, `[P,W]=Vec(P,W)`, `∐`=`⊕`): recovers the linear-container
  extension `⟦S,P⟧W = ⊕_s Vec(P_s,W)` of `proofs/2026-08-18-linear-containers-vec.md`.

The question is exactly **how much of the AAG full-faithfulness of `⟦−⟧` survives the change
of base**, and which property of `C` controls it.

---

## 1. The hom formula in general (the enriched computation)

Everything reduces to a single canonical comparison map. Two standard enriched facts:

**Lemma 1.1 (enriched co-Yoneda).** For any `C`-functor `G:C→C` and any `P∈C`,
`C\text{-}[C,C](h_P, G) ≅ G(P)` as an object of `C`, natural in `G,P`. In particular
`C\text{-}[C,C](h_P,h_Q) ≅ [Q,P]`.

*Proof.* This is the enriched Yoneda lemma with `V=C`: `h_P = C(P,-)` is the corepresentable
`V`-functor, and enriched Yoneda gives `[C,V](C(P,-),G) ≅ GP`. (Concretely: evaluate a
transformation at `id_P ∈ [P,P]`; naturality along `[P,-]`-whiskering recovers it everywhere,
using that `G` acts `C`-linearly on hom-objects. This is the general form of Lemma 1.1 of the
Vec file.) ∎

**Lemma 1.2 (`Nat` out of a coproduct).** `C\text{-}[C,C](∐_s F_s, G) ≅ ∏_s C\text{-}[C,C](F_s,G)`.

*Proof.* Coproducts of `C`-functors are pointwise, `(∐_sF_s)X=∐_sF_sX`. The enriched hom is
the end `∫_X [(∐_sF_s)X, GX] = ∫_X [∐_s F_sX, GX] = ∫_X ∏_s [F_sX,GX] = ∏_s ∫_X [F_sX,GX]`,
using `[∐_s A_s, B] ≅ ∏_s [A_s,B]` (the internal hom `[-,B]` is a right adjoint, so it sends
coproducts to products) and that ends commute with products. ∎

**Theorem 1.3 (enriched hom-object).** As an object of `C`,
`C\text{-}[C,C](⟦S,P⟧, ⟦T,Q⟧) ≅ ∏_{s∈S} ∐^{C}_{t∈T} [Q_t, P_s]`.

*Proof.* `⟦S,P⟧=∐_s h_{P_s}`. Apply Lemma 1.2 then Lemma 1.1:
`≅ ∏_s ⟦T,Q⟧(P_s) = ∏_s ∐^C_t [Q_t, P_s]`. ∎

The *underlying set* of enriched natural transformations is
`C(I, ∏_s ∐^C_t [Q_t,P_s]) = ∏_s C(I, ∐^C_t [Q_t, P_s])`. Comparing with the container-hom of
Def 0.1, `⟦−⟧` acts on homs as `∏_s` of the following canonical map.

**Remark 1.3a (no completeness needed for full/faithful).** The *hom-object* formula of
Theorem 1.3 uses ends, hence needs `C` complete. But the *set* of enriched natural
transformations always exists (an equalizer in `Set`), and at the set level the same two steps
run without completeness: `Nat_{set}(∐_s F_s, G) ≅ ∏_s Nat_{set}(F_s,G)` (a transformation out
of a pointwise coproduct is a tuple), and `Nat_{set}(h_P, G) ≅ C(I, GP)` (enriched co-Yoneda,
set form). So `Nat_{set}(⟦S,P⟧,⟦T,Q⟧) ≅ ∏_s C(I, ∐^C_t[Q_t,P_s])` for *any* closed `C` with
coproducts. All full/faithful statements below are set-level and need no completeness; `Set`,
`Vec`, `Set×Set` are complete anyway.

**Definition 1.4 (the comparison map).** For a family `(X_t)_{t∈T}` in `C` write
```
        γ_{(X_t)} :  ∐^{Set}_{t} C(I, X_t)  ⟶  C(I, ∐^{C}_{t} X_t),
```
`(t, x:I→X_t) ↦ (inj_t ∘ x)`. This is the canonical comparison for whether **`C(I,-)`
preserves the coproduct `∐_t X_t`**. Under `C(Q_t,P_s)=C(I,[Q_t,P_s])`, the action of `⟦−⟧`
on the `s`-component is exactly `γ_{([Q_t,P_s])_t}`.

So the entire question is now about the map `γ`. Two immediate reductions:

- The relevant families are `(X_t)_t = ([Q_t, P_s])_t` with a **common** `P_s=:Z` and arbitrary
  `Q_t`. As `(S,P),(T,Q)` range over all containers, `Z` ranges over all objects and `(Q_t)`
  over all set-indexed families.

---

## 2. The main theorem

**Theorem 2.1 (fullness criterion — flagship T1).**
Let `C` be closed symmetric monoidal with small coproducts. Then:

1. **(Sufficiency.)** If the unit `I` is **connected** — i.e. `C(I,-):C→Set` preserves small
   coproducts — then `⟦−⟧ : Fam(C^op) → C\text{-}[C,C]` is **fully faithful**.
2. **(Necessity, copower form.)** If `⟦−⟧` is full (resp. faithful) then for every object `Z`
   and every set `T` the map `γ` is surjective (resp. injective) for the constant family
   `(Z)_{t∈T}`; equivalently `C(I,-)` preserves (resp. reflects) all **copowers** `T·Z`. In
   particular a disconnected unit obstructs fullness.
3. **(Sharp iff, with a cogenerator.)** If moreover `C` has an object `Z₀` with
   `[-,Z₀]:C^op→C` essentially surjective onto the objects appearing in the coproducts of
   interest (e.g. `C=Vec_{fd}` with *finite* coproducts, `Z₀=k`, `[-,k]=(-)^*` hitting every
   fd space), then **`⟦−⟧` fully faithful ⟺ `I` connected** (for those coproducts). *Caveat:*
   for full `Vec` with infinite coproducts `[-,k]` is not essentially surjective, so this
   clause is not the tool there — the copower test of (2) is (and it already decides `Vec`).

*Proof.*
**(1)** If `C(I,-)` preserves coproducts, `γ_{(X_t)}` is a bijection for *every* family:
`∐^{Set}_t C(I,X_t) = C(I,∐^C_t X_t)` is exactly its statement. Hence every `s`-component of
the `⟦−⟧`-action is a bijection, so `∏_s γ` is a bijection: `⟦−⟧` is full and faithful.

**(2)** Take the source container `(S,P) = ({s}, Z)` (one shape, position `Z`) and the target
`(T,Q) = (T, (I)_{t∈T})`, so `[Q_t,Z]=[I,Z]≅Z` and the family is constant `Z`. The
`s`-component of the `⟦−⟧`-action is `γ_{(Z)_{t∈T}} : T·C(I,Z) → C(I, T·Z)` (copower `T·Z =
∐_T Z`). Full ⟹ this is surjective for all `T,Z`; faithful ⟹ injective. Surjectivity for all
`T,Z` is precisely "`C(I,-)` preserves copowers"; a disconnected unit (some copower not
preserved) makes some such `γ` non-surjective, so `⟦−⟧` is not full.

**(3)** Necessity of *full* preservation. By the reduction in §1 the action ranges over
families `([Q_t,Z])_t` with common `Z`. Fix `Z=Z₀` with `[-,Z₀]` essentially surjective. Then
`{[Q,Z₀] : Q∈C}` is (up to iso) **all** objects of `C`, so `([Q_t,Z₀])_t` ranges over all
set-indexed families. Fullness ⟹ `γ_{(W_t)}` surjective for every family `(W_t)`, and
faithfulness ⟹ injective; together `C(I,-)` preserves all small coproducts, i.e. `I` is
connected. With (1) this gives the iff. ∎

**Remark 2.2 (the general iff, without a cogenerator).** Even without a `Z₀`, Theorem 1.3 +
Def 1.4 give the *exact* statement: `⟦−⟧` is fully faithful **iff `C(I,-)` preserves every
coproduct of internal-homs `∐_t [Q_t,Z]`**. The clause "`I` connected" (preserves *all*
coproducts) is the clean sufficient condition and is also necessary whenever internal homs
into a fixed object exhaust `C` (part 3). In every base of interest the copower test of part
(2) already decides the matter, so the copower/coproduct gap never bites.

**Remark 2.3 (faithful is *not* automatic — correction to the brief).** PROVE.md's floor
said "faithful always." This is **false**: faithfulness is the *injective* half of `γ`, which
fails whenever coproduct injections are not `I`-disjoint. Over `Vec` the two container
morphisms `(f,0),(f',0)` with distinct shape-maps but zero position-maps both extend to the
**zero** natural transformation (`inj_{f(s)}∘0 = 0 = inj_{f'(s)}∘0`), so `⟦−⟧` is *not*
faithful over `Vec` — it is only "faithful on the non-zero part," exactly as the Vec file
already observed. The general criterion (`I`-disjointness) predicts this. Over `Set` coproducts
are disjoint, so `⟦−⟧` is faithful; over any additive base it is not.

---

## 3. The three poles: Set (yes), Vec (no), Set×Set (extensive yet no)

**Corollary 3.1 (Set — recovers AAG).** `C=Set`, `I=1`. `Set(1,-)=Id` preserves all
coproducts, so `1` is connected; by Theorem 2.1(1) `⟦−⟧` is fully faithful — the classical
Abbott–Altenkirch–Ghani representation theorem (FoSSaCS'03/TCS'05). This *identifies the
hidden hypothesis*: AAG works because the terminal object of `Set` is connected.

**Corollary 3.2 (Vec — the linear collapse).** `C=Vec`, `I=k`. `Vec(k,-)` is the underlying-set
(forgetful) functor, which does **not** preserve coproducts (`⊕`): the comparison
`∐^{Set}_t X_t → ⊕_t X_t` is neither surjective (misses cross-summand sums) nor injective
(collapses zeros). By Theorem 2.1(2) `⟦−⟧` is neither full nor faithful; by 2.1(3) (with
`Z₀=k`, `[-,k]=(-)^*` essentially surjective on `Vec_{fd}`) the failure is *exactly* the
disconnectedness of `k`. This is the `∐⊊⊕` crux of `2026-08-18-linear-containers-vec.md`,
now placed as one instance of the general criterion. Verified: `F_3`, family `Q=[1,1],Z=1`,
gives `|domain|=6`, image of size `5` in a `9`-element codomain (non-full), and `0` has two
preimages (non-faithful).

**Corollary 3.3 (Set×Set — extensive but NOT full; the counterexample that kills the
conjecture).** `C = Set×Set` with the product cartesian closed structure: `I=(1,1)`,
`[(a,b),(c,d)]=(c^a,d^b)`, coproduct `(x,y)+(x',y')=(x+x',y+y')`. `Set×Set` **is** lextensive
(a finite product of extensive categories is extensive). Yet its unit is **disconnected**:
```
   C((1,1), (X,Y)+(X',Y')) = (X+X')×(Y+Y')   ≠   X×Y + X'×Y' = C((1,1),(X,Y))+C((1,1),(X',Y')),
```
the comparison missing the cross terms `(x,y')`. Hence by Theorem 2.1(2), `⟦−⟧` is **not
full** over `Set×Set`. Concrete witness (verified): source `({s},(1,1))`, target
`({t₁,t₂},((1,1),(1,1)))` — there are **2** container morphisms (choose `t₁` or `t₂`) but
`C((1,1),(2,2))=2×2=4` natural transformations; the two "crossed" transformations `(t₁,t₂)`
and `(t₂,t₁)` are not realized by any container morphism.

**Theorem 3.4 (the corrected slogan).** *Extensivity of `C` is neither necessary nor
sufficient for `⟦−⟧` to be full.* The controlling invariant is **connectedness of the
monoidal unit** `I` (`C(I,-)` preserves coproducts).
- *Not sufficient:* `Set×Set` extensive, unit disconnected, not full (Cor 3.3).
- *The Set case is not "because Set is extensive" but "because `1` is connected":* extensivity
  and unit-connectedness happen to coincide for `Set`, and the container literature has always
  cited the former; the base change to `Set×Set` (still extensive) or `Vec` (not extensive)
  separates them and exposes connectedness as the real hypothesis.

**Remark 3.5 (this does not contradict Gambino–Kock — external vs internal shapes).** There
are two different generalizations of the Set container `⟦S,P⟧X=∐_s X^{P_s}` to a base `C`:
(A) the **mixed** `Fam(C^op)` one studied here — the shape index `S` is an *external set*, the
positions `P_s` are objects of `C`, extension `∐_s [P_s,-]` via `C`'s self-enrichment (this is
exactly Dorta–Jarvis–Niu's `ΣΠV` and PROVE.md's object of study); and (B) the **fully
internal** Gambino–Kock polynomial functor, where shapes too are internal (a map `B→A` of
`C`-objects) and one uses slice categories. Over `C=Set` (A)=(B). Over an LCCC base like
`Set×Set` the GK construction (B) *is* represented by its polynomial and its representation
theorem holds — because it never forms an external set-coproduct of internal homs. My
`Set×Set` counterexample is about (A): the *external* `∐_{t∈T}` of internal homs is what
`C((1,1),-)` fails to preserve. **So the correction is precise:** for the mixed `Fam(C^op)`
extension the invariant is unit-connectedness, not extensivity; the extensivity/LCCC folklore
is true but for the *other* (fully internal) construction, and the two diverge exactly off
`Set`. This divergence is itself the content — it says the external-shape container calculus is
strictly a `Set`-enriched phenomenon unless the base's unit is connected.

**Why the folklore said "extensivity."** Two *distinct* theorems have been conflated:
(a) **full-faithfulness of the fixed extension** `⟦−⟧` (this file: `I` connected); and
(b) **Diers' reconstruction** of `(S,P)` from an abstract familially-representable functor
`F:C→Set` as `S=π₀(el F)` (which genuinely uses extensivity of the *codomain* `Set`). For
`C=Set` both the base and codomain are `Set`, so (a) and (b) fuse and "extensivity" reads off
both. Off `Set` they separate: (a) is governed by the *unit of the enrichment base*, (b) by
extensivity of the value-category. Neil's conjecture is the shadow of that fusion.

---

## 4. Consequences for T2 (closedness) and T3 (change of enrichment)

**Corollary 4.1 (T3 — change of base = change of enrichment).** A lax symmetric monoidal
functor `F:(Set,×,1)→(C,⊗,I)` (e.g. the free-object functor `Set→Vec`, `F1=k`) sends a Set
container `(S,P)` to `(S,(F P_s))∈Fam(C^op)`, and `⟦F(S,P)⟧ = ∐_s [F P_s,-]` is a
`C`-enriched endofunctor. Thus **moving the base from `Set` to `C` moves the extension from
ordinary `[Set,Set]` to `C`-enriched `[C,C]`** — the change of base *induces a change of
enrichment* (Eilenberg–Kelly / Cruttwell base-change is the generic mechanism; the container
instantiation is the delta). By Theorem 3.4 the induced extension is fully faithful iff the
target unit `FI'=I` is connected — for `F=` free-vector-space, `I=k` is **not** connected, so
free-linearizing a container *strictly loses* naturality information exactly measured by
`∐⊊⊕`. This confirms Neil's leaning that **`C`-enrichment (here Vec) is the fundamental
invariant view, and the connectedness of its unit is the pass/fail line.** *(proved.)*

**Proposition 4.2 (T2(a) — Day/Dirichlet tensor is closed under a coproduct-completion
hypothesis).** The parallel/Dirichlet tensor `(S,P)⊗(T,Q)=(S×T,(P_s⊗Q_t))` on `Fam(C^op)`
is the Day convolution of `[-,-]` along `⊗`; when `C` is *complete* and monoidal closed, the
pointwise Day right adjoint exists, giving an internal hom for `⊗` on `Fam(C^op)`. *This is
the base-general form of Niu–Spivak Ex 4.78; I have the adjunction shape but have NOT verified
the coproduct-completion bookkeeping in general — marked **conjectured**, gap in §6.*

**Proposition 4.3 (T2(b) — ◁-coclosure is the fragile one).** The composition
`(S,P)◁(T,Q)` has a left coclosure via a Kan extension `Lan` iff that `Lan` **preserves
corepresentables** `[P,-]`. Over `Set` (Spivak Prop 6.57) it does. Over a non-cartesian base
this is exactly where connectedness fails to help: `Lan` along `⊗` need not preserve
`[P,-]` when `⊗ ≠ ×`. *I locate the break here but do not have the general survival criterion
— marked **conjectured**, gap in §6.* Note `2026-08-21` already proved `Cont` itself lacks a
`◁`-*closure* (only a coclosure); the base-general coclosure question is genuinely open.

These are subsidiary to the flagship; §6 records exactly what remains.

---

## 5. Verification

Computations in this session (Python, `F_q` and finite Set/Set×Set), all consistent with
Theorems 2.1–3.4:

- **Set (Cor 3.1):** `γ` a bijection on all tested families (`Qs=[1,1],Z=1` → `2=2`;
  `Qs=[2,1],Z=2` → `6=6`). Full-faithful. ✓
- **Set×Set (Cor 3.3):** `Qs=[(1,1),(1,1)],Z=(1,1)` → domain `2`, codomain `4`. Extensive
  base, **not full**. Explicit: 2 container morphisms, 4 natural transformations. ✓
- **Vec/`F_3` (Cor 3.2):** `Qs=[1,1],Z=1` → domain `6`, **image size 5** inside a 9-element
  codomain (not full); the zero has **2 preimages** (not faithful). ✓ The `F_2` cardinalities
  coincide accidentally (`4=4`) but the *map* still fails (image size 3 of 4) — cardinality
  counting is blind, the map analysis is decisive.

The proofs are structural (enriched Yoneda + the coproduct/`C(I,-)` comparison); the
computations only witness the three poles.

---

## 6. Status and gaps (precisely stated)

**PROVED (flagship T1):**
- Theorem 1.3 (enriched hom-object formula, base-general).
- Theorem 2.1(1) sufficiency: `I` connected ⟹ `⟦−⟧` fully faithful.
- Theorem 2.1(2) necessity (copower form): `⟦−⟧` full/faithful ⟹ `C(I,-)` preserves/reflects
  copowers; disconnected unit ⟹ not full.
- Theorem 2.1(3) sharp iff under a `[-,Z₀]`-essentially-surjective object (covers `Vec_{fd}`).
- Corollaries 3.1–3.3 (Set full-faithful / Vec neither / Set×Set extensive-but-not-full).
- **Theorem 3.4: the conjecture "extensive ⟺ full" is refuted; the correct invariant is
  connectedness of the monoidal unit.** (This is the deliverable and the honest correction.)
- Remark 2.3: `⟦−⟧` is *not* faithful over `Vec` (corrects "faithful always").
- Corollary 4.1 (T3, change of base = change of enrichment): proved.

**GAPS (do not build on above `conjectured`):**
1. **General iff without a cogenerator (Rem 2.2).** The exact criterion is "`C(I,-)`
   preserves coproducts of internal-homs `∐_t[Q_t,Z]`." Whether this always upgrades to
   "preserves all coproducts" (i.e. whether the copower necessity of 2.1(2) is already
   equivalent to full connectedness for *every* closed `C`) is open. For all named bases it
   does; a general proof or a separating example is wanted.
2. **T2(a) closedness of `⊗` (Prop 4.2).** Adjunction shape identified; the
   coproduct-completion/Day-right-adjoint bookkeeping over a general complete closed `C` is
   **not** verified. Conjectured.
3. **T2(b) ◁-coclosure (Prop 4.3).** The survival criterion "`Lan` preserves
   corepresentables when `⊗≠×`" is **not** established in general; located, not proved.
   Conjectured. (Cont-side no-`◁`-closure is separately proved, `2026-08-21`.)

## 7. Novelty / prior-art caveat (per PROVE.md)

- **Abbott–Altenkirch–Ghani** own the Set full-faithfulness; my Cor 3.1 *re-derives* it and
  *names its hidden hypothesis* (`1` connected). Not claimed new; the naming is the point.
- **Dorta–Jarvis–Niu (arXiv:2305.05655)** build `⊗` and a composition product `◁_DJN` over a
  general `ΣΠV` base and prove `◁_DJN`-comonoids ≃ enriched categories (their **Thm 4.3**; their
  Def 4.2 is the *definition* of enriched cofunctor); they do **not** treat
  full-faithfulness / closedness / extensivity / connectedness. My T1 is disjoint from their
  Thm 4.3 and must be cited as prior art for the tensor *definition*.
  ⚠ **2026-08-31 scope correction:** their composition product `◁_DJN` is **weighted** — direction object at `(i,j:A_i→J)` is `∏_{a∈A_i}∏_{b∈B_{ja}}(u_{i,a}·v_{ja,b})` (Def 3.5 / Lemma 3.6, p. 89) whereas mine carries **no outer `u` factor** — so `◁_DJN = ◁` **only at `C = 1`**. Witness: `C=2`, `·=∧`, `e=⊤`, `p=∑_{i∈1}∏_{a∈1}⊥`, `q=∑_{j∈1}∏_{b∈1}⊤` ⟹ DJN `⊥`, mine `⊤`; over `C=[0,∞]` (their §5) DJN `5+3=8`, mine `3`. My defining property `⟦p◁q⟧≅⟦p⟧∘⟦q⟧` is *unavailable* on `ΣΠC` for `C≠1` (`E(p):(ΠC)^op→Set` is not an endofunctor). Their `⊗` **does** match mine exactly, so only `◁` breaks. So cite them for `⊗` and for `◁_DJN`; do **not** cite them for a
  composition-representing `◁` over a general base.
- **Diers familial representability** owns the reconstruction `S=π₀(el F)` and *its*
  extensivity hypothesis (of the codomain `Set`); §3's "why the folklore said extensivity"
  distinguishes it from full-faithfulness of a fixed `⟦−⟧`. Cited, not reproved.
- **Gambino–Kock (0906.4931)** develop polynomial composition over LCCC bases; `Vec` is not
  LCCC (boundary cite), consistent with T2 being the fragile part.
- **The claimed delta:** the identification of *connectedness of the monoidal unit* as the
  exact controlling invariant for full-faithfulness of the container extension over a closed
  base, the `Set×Set` counterexample separating it from extensivity, and the resulting
  correction of the "extensive ⟺ full" conjecture. Grant-ready as stated (the floor was
  already a theorem; this is the general theorem Neil asked for, with the conjecture fixed).
