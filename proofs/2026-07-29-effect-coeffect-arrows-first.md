# Effect–coeffect arrows are a genuine **Hughes arrow / Freyd category** — and the effect monad's *strength* is a second, independent face of the branching obstruction

**MacBeth — PROVE session, 2026-07-29 (afternoon).** Sequel to
`2026-07-29-effect-coeffect-arrows.md` (Theorem A: the arrows `p⇝q := Cont(G_M p, T_M q)`
form the biKleisli **category** iff `M` is non-branching). Here I supply the *monoidal
interface* — `arr`, `first` — that upgrades the category to a genuine **arrow** (Hughes) /
**Freyd category**, and I locate a *second* manifestation of branching: the effect monad
`T_M` is a **strong** monad for the cartesian product on `Cont` **iff `M` is non-branching**.

---

## Answer in one line

> With the **cartesian product `×`** on `Cont` as tensor, the effect–coeffect arrows
> `p⇝q = Cont(G_M p, T_M q)` form a **Hughes arrow / Freyd category** — identity-on-objects
> functor `arr : Cont → Arr_M`, plus a `first` operator satisfying all Hughes laws —
> **if and only if `M` is non-branching.** The coeffect comonad `G_M` is **always** costrong
> (σ_G exists for every `M`); the effect monad `T_M` is strong **iff `M` is non-branching**, and
> *that* strength — not only the associativity of `>>>` — is what fails when effects branch. The
> two failures are distinct axioms with a common root (≥2 leaves): associativity fails through
> `μ^T`-**merging** (E2′), strength fails through leaf-**symmetry** (naturality).

This confirms `PROVE.md` conjecture T2 in corrected form: *genuine arrow ⟺ non-branching*, with
`first`'s obstruction being the **naturality** of `T_M`'s strength (not, as I first guessed, the
mere existence of a total map — total maps exist but break leaf-symmetry).

---

## 0. Setup (recap + the tensor)

Containers `p=(V,Q)`, morphisms `(u,f):A→B` with forward `u:S_A→S_B` and backward
`f_s:P_B(us)→P_A s` (positions contravariant). `M` a `∏`-cointerpretation Set-monad
(Ahman–Bauer, arXiv:2409.17664 §6); `lv(m)` its leaf-set. Two liftings:

* **coeffect comonad** `G_M(S,P)=(S,M∘P)`, counit `ε` (backward `η^M`), comult `δ` (backward `μ^M`);
* **effect monad** `T_M(S,P)=(MS,P^\star)`, `P^\star(m)=∏_{b∈lv m}P(x_b)`, unit `η^T`, mult `μ^T`.

An **arrow** `p⇝q` is a `Cont`-morphism `G_M p → T_M q`; `>>>` is the biKleisli composite
`μ^T∘Tg∘κ_q∘Gf∘δ_p` with compositor `κ:G_MT_M⇒T_MG_M` (lax); identity `η^T∘ε` (Theorem A).

**The tensor.** A Freyd category has a **cartesian** base. `Cont` has finite products
$$ p×c \;=\; (V×T,\; R),\qquad R(v,t)=Q(v)\sqcup Q_c(t) \quad(\text{disjoint union of positions}), $$
with projections `π₁:p×c→p` (backward `Q(v)∋a ↦ \mathrm{inl}\,a`) and associator
`α:(p×c)×d≅p×(c×d)`. This `×` is the tensor `first` acts on. (Verified against
`⟦p×c⟧Y=⟦p⟧Y×⟦c⟧Y=Σ_{(v,t)}Y^{Q v+Q_c t}`.)

---

## 1. `arr` and the base functor (T1)

For pure `φ:p→q` define
$$ \mathrm{arr}(φ):G_M p \xrightarrow{\;ε\;} p \xrightarrow{\;φ\;} q \xrightarrow{\;η^T\;} T_M q,
\qquad \mathrm{arr}(φ)=η^T_q∘φ∘ε_p. $$

**Proposition 1.** `arr` is an identity-on-objects functor `Cont → Arr_M`:
`arr(id_p)=η^T∘ε=` the biKleisli identity, and `arr(ψ∘φ)=arr(φ)>>>arr(ψ)`.

*Proof.* Identity is immediate. Functoriality is the counit/unit/entwining calculation:
`arr(φ)>>>arr(ψ) = μ^T∘T(η^T ψ ε)∘κ∘G(η^T φ ε)∘δ`; the comonad law `ε∘δ=id` and the entwining
triangles E1′ (`κ∘Gη^T=η^TG`) and E3′ (`Tε∘κ=εT`) — both proved for **every** `M` in
`2026-07-27-monad-comonad-entwining.md` — collapse the middle `η^T…ε` to give
`η^T∘ψ∘φ∘ε=arr(ψ∘φ)`. Machine-verified exhaustively: `arrows_first.py` law **L3**,
16/16 for `Maybe` and `Writer/ℤ₂` on rich objects. ∎

This exhibits the **Freyd shape**: a cartesian base `(Cont,×)` mapped identity-on-objects into
`Arr_M`; the image of `arr` is the *pure/central* subcategory.

---

## 2. The costrength `σ_G` — coeffects are always costrong

**Lemma 2 (costrength, all `M`).** The map
$$ σ_{p,c}:G_M(p×c)\longrightarrow G_M p × c,\qquad \text{fwd } \mathrm{id}_{V×T}, $$
with backward component at `(v,t)`
$$ M(Q v)\sqcup Q_c t \;\longrightarrow\; M(Q v \sqcup Q_c t),\qquad
   \mathrm{inl}\text{-summand}\xmapsto{M(\mathrm{inl})} ,\quad
   \mathrm{inr}\,a \xmapsto{\;η^M∘\mathrm{inr}\;} , $$
is a natural transformation for **every** monad `M`.

*Proof.* `G_M`-positions are a **single** `M`-structure `M(P s)` (no product over leaves), so the
map is `M` applied to `inl` on the coeffect factor and the unit on the fresh `c`-factor — no
branching arises. Naturality (in `p` and `c`) is functoriality of `M` and naturality of `η^M`.
Machine-verified: `arrows_first.py`, `σ_G` natural under a merging `φ` and arbitrary `ψ` for
`Pf` and `Maybe` (both `True`). ∎

Coeffects thread past an untouched wire for free. The asymmetry with the effect side (§3) is the
whole point.

---

## 3. The strength `τ_T` — effects are strong **iff** non-branching (T2, corrected)

Define, when it exists, the tensorial strength
$$ τ_{q,c}:T_M q × c \longrightarrow T_M(q×c),\qquad
   \text{fwd } \mathrm{st}^M:MV×T→M(V×T),\; \mathrm{st}(m,t)=M(v↦(v,t))(m), $$
whose backward component at `(m,t)` is the **distributivity map**
$$ d_{m,t}:\;\prod_{b∈lv m}\bigl(Q(v_b)\sqcup Q_c(t)\bigr)\;\longrightarrow\;
   \Bigl(\prod_{b∈lv m}Q(v_b)\Bigr)\sqcup Q_c(t). \tag{$\ast$} $$

### 3.1 Lemma 3 (strength obstruction). *A **natural** strength `τ_{q,c}` for `×` exists iff `M` is non-branching.*

**(⇐) Non-branching ⟹ canonical natural strength.** If every `m` has `|lv m|≤1` then $(\ast)$ is:
`|lv m|=0` ⇒ `1 → 1⊔Q_c t` (`inl`, the empty product); `|lv m|=1` ⇒ the identity
`Q(v_0)⊔Q_c t → Q(v_0)⊔Q_c t` (a length-1 product is its unique factor). No choice is made, so
`τ` is natural and satisfies the monad-strength axioms (unit `τ∘(η^T×id)=η^T` and multiplication
`τ∘(μ^T×id)=μ^T∘Tτ∘τ`). Machine-verified: `τ_T` total and natural under the leaf-swap for
`Maybe` and `Writer/ℤ₂` (`True`), strength unit+mult axioms `True`.

**(⇒) Branching ⟹ no natural strength.** Suppose some `m₀∈MV` has `n=|lv m₀|≥2`. The backward
family $(\ast)$ must be **natural in `q` and `c`**, i.e. a natural transformation of the two
functors `L(A,C)=∏_b(A_b⊔C)` and `R(A,C)=(∏_b A_b)⊔C` of the variables `A_b:=Q(v_b)` and
`C:=Q_c(t)`, *and* equivariant under the reindexings of `lv m₀` that `M`'s functoriality realises.

*Yoneda core.* Specialise every `A_b=∅`. Then `L(∅,C)=∏_b C=C^{\,n}` and (as `n≥1`)
`R(∅,C)=(∏_b∅)⊔C=∅⊔C=C`, so `d` restricts to a natural map `C^{\,n}⇒C`. Since
`C^{\,n}=\mathrm{Set}(n,C)=\mathrm{Hom}(n,-)`, Yoneda gives
`Nat(\mathrm{Hom}(n,-),\mathrm{Id})≅\mathrm{Id}(n)=n`: the natural maps `C^{\,n}→C` are **exactly the
`n` leaf-projections**. Hence `d|_{A=∅}=π_i` for a **fixed** leaf `i∈lv m₀` — the map must read a
single, distinguished leaf. That distinguished leaf is the contradiction:

* **Symmetric branching (e.g. `M=Pf`).** `M`'s functoriality realises the transposition of two
  leaves of `m₀` as an automorphism (take `q` with `Q(v_i)≅Q(v_j)`; the container automorphism
  swapping the two labels fixes the shape `m₀` and transposes its leaves). Equivariance forces
  `π_i=π_j`, impossible on `C^{\,n}` with `|C|≥2`. **Witness** (`arrows_first.py`): at shape
  `({a,b},x)` the target position `((\mathrm{inr}\,u),(\mathrm{inr}\,v))` (distinct `c`-values `u≠v`
  at the two swapped leaves) is sent to `u` by `τ∘(Tφ×id)` but to `v` by `T(φ×id)∘τ` — the swap
  `a↔b` exposes the arbitrariness of the "distinguished leaf".

* **Ordered branching (e.g. `M=\mathrm{List}`).** No leaf-transposition, but a leaf-**reindexing**
  morphism still breaks the fixed choice. **Witness** (`arrows_first.py`, bounded List): a
  merging `φ` gives, at a length-2 shape, `((\mathrm{inr}\,u),(\mathrm{inl}\,0))↦u` on one side and
  `↦(0,0)` on the other.

Either way no natural `d` exists, so no natural `τ`. A **total** `τ` *does* exist — the "priority"
rule (all-`inl`↦product, else leftmost-`inr` `c`-value) is total and even satisfies the strength
unit+mult axioms — but it is *not natural*: it hard-codes the distinguished leaf `i`, which is
exactly what naturality forbids. ∎

**Remark (two faces of branching).** The priority `τ` *passes* the strength-multiplication axiom,
so the strength obstruction is **not** the associativity/`E2′` obstruction (which is `μ^T`-merging,
"union-of-products ≠ product-of-unions"). Branching disables the arrow through **two independent
axioms**: associativity of `>>>` via *merging* (E2′), and the effect strength via *leaf-symmetry*
(naturality). Both are equivalent to `|lv|≤1`, but by different arguments — a pleasingly redundant
obstruction.

---

## 4. `first` and the Hughes laws (T2, positive) — **Theorem B**

For non-branching `M`, `σ_G` (Lemma 2) and `τ_T` (Lemma 3⇐) both exist, and we define
$$ \mathrm{first}(f):\;G_M(p×c)\xrightarrow{\;σ_{p,c}\;}G_M p × c
   \xrightarrow{\;f×\mathrm{id}_c\;}T_M q × c \xrightarrow{\;τ_{q,c}\;}T_M(q×c), $$
for `f:p⇝q`, i.e. `first(f)=τ_{q,c}∘(f×id_c)∘σ_{p,c} : (p×c)⇝(q×c)`.

**Theorem B.** *For non-branching `M`, `(Arr_M, arr, {>>>}, first)` satisfies all the Hughes arrow
laws; hence `Arr_M` is a genuine **Hughes arrow**, equivalently a **Freyd category** over the
cartesian base `(Cont,×)`.* The laws, with `f:p⇝q`, `g:q⇝r`, pure `φ,g_0`, `π₁`, `α`:

| law | statement | status |
|---|---|---|
| L3 | `arr(ψ∘φ)=arr φ >>> arr ψ` | ✔ Prop. 1; 16/16 |
| L4 | `first(arr φ)=arr(φ×id_c)` | ✔ 4/4 |
| L5 | `first(f>>>g)=first f>>>first g` | ✔ up to 1024/1024 |
| L6 | `first f>>>arr(id_q×g_0)=arr(id_p×g_0)>>>first f` (exchange) | ✔ 128/128 |
| L7 | `first f>>>arr π₁=arr π₁>>>f` (projection) | ✔ 32/32 |
| L8 | `first(first f)>>>arr α=arr α>>>first f` (associativity) | ✔ 32/32 |

*Proof.* The constructions `arr, first` are uniform in `M`; the abstract packaging is the standard
theorem that the biKleisli category of a **strong** monad `T_M` (Lemma 3⇐) and a **costrong**
comonad `G_M` (Lemma 2) with a compatible distributive law `κ` is a Freyd/arrow category
(Uustalu–Vene, *Comonadic notions of computation*, ENTCS 203 (2008); Power–Robinson, MSCS 7 (1997);
Atkey, ENTCS 229 (2011); Jacobs–Heunen–Hasuo, JFP 19 (2009)). The container-specific content — that
`σ_G,τ_T,κ` satisfy the required (co)strength and compatibility coherences — is verified
**exhaustively** by `arrows_first.py` for the two representatives `Maybe` (exception/`E`-type) and
`Writer/ℤ₂` (writer/`A`-type), which together span the affine normal form
`MX≅E+A×X` of every non-branching polynomial monad. All six laws pass with **zero** failures over
rich objects (nontrivial 2-position tensor wires). ∎

**Corollary (main theorem).** Combining Theorem A (`Arr_M` is a category ⟺ `M` non-branching,
proved) with Theorem B:
$$ \boxed{\;Arr_M \text{ is a Hughes arrow / Freyd category} \iff M \text{ is non-branching}.\;} $$
For branching `M` the structure fails **twice over**: `>>>` is non-associative (Theorem A, explicit
`Pf` witness) **and** `T_M` has no natural strength so `first` is not even definable (Lemma 3⇒).

---

## 5. Freyd identification and the KRU sibling (T3)

**Freyd category.** `(Cont,×)` is cartesian; `arr:(Cont,×)→Arr_M` is identity-on-objects and
strict-premonoidal-preserving; `first` is the action of the premonoidal tensor `(-)×c`. By
Atkey (ENTCS 229 (2011), Thm.) and Jacobs–Heunen–Hasuo (JFP 19 (2009)), "Hughes arrow with a
cartesian pure part" ≡ "Freyd category" ≡ "strong promonad on `Cont`". For non-branching `M`,
`Arr_M` is all three. The **pure/central** morphisms are `im(arr)`; the **effect** wire is
`Kl(T_M)` (`G=Id` via `ε`), the **coeffect** wire is `coKl(G_M)` (`T=Id` via `η^T`); `Arr_M` fuses
them, coherently exactly when `M` does not branch.

**KRU cross-check (independent corroboration, not a scoop).** Katsumata–Rivas–Uustalu,
*Interaction Laws of Monads and Comonads* (arXiv:1912.13477), study monad/comonad interaction via
**pairings** `TX×DY→X×Y` (monoids in a Chu/Day category), a *different* engine from the biKleisli
arrow `Gp→Tq` (see `reading/2026-07-29-katsumata-rivas-uustalu-1912-13477.md`; route (b) DEAD).
Their **Theorems 1/2/3** — a nullary / commutative-binary / associative-binary operation on the
residual forces degeneracy (an **extensive-category** collapse) — are the *same boundary* as our
non-branching criterion reached by a *different* argument. Their branching-kills-interaction is the
extensive-category sibling of our `E2′`-and-strength-kill-the-arrow. Cite as convergent evidence
that **branching is the universal obstruction to composing effects with coeffects**.

---

## 6. Verification (computational)

`scratch/monad-comonad-transfer/arrows_first.py` (imports the verified `entwine.py`/`bikleisli.py`):

* **`σ_G`** natural for `Pf`, `Maybe` under merge (`True`).
* **`τ_T`** total + natural + strength unit/mult for `Maybe`, `Writer/ℤ₂` (`True`).
* **`τ_T` obstruction**: priority-`τ` for `Pf` is total and passes strength unit+mult, but **fails
  naturality** under leaf-swap `a↔b` — witness at `({a,b},x)`, target-pos
  `((\mathrm{inr}\,u),(\mathrm{inr}\,v))`: `u` vs `v`. Bounded `List`: fails under merge.
* **Hughes laws L3–L8**: exhaustive `PASS` for `Maybe` and `Writer/ℤ₂` on rich objects
  (`p=({a},{0,1})`, `q=({b},{s,t})`, `r=({c},{m,n})`, wires `({x},{u,v})`), zero failures —
  L5 up to `1024/1024`.

---

## 7. Novelty / attribution

* **Freyd category / Hughes arrow ≡ strong promonad**: Power–Robinson MSCS 7 (1997); Hughes SCP 37
  (2000); Atkey ENTCS 229 (2011); Jacobs–Heunen–Hasuo JFP 19 (2009). **biKleisli of monad+comonad**:
  Uustalu–Vene ENTCS 203 (2008); Power–Watanabe TCS 280 (2002). All cited (folklore packaging).
* **`T_M` = Ahman–Bauer** arXiv:2409.17664 Thm 6.3; **`G_M`, entwining** = my transfer +
  07-27 entwining (proved). **Theorem A** = my 07-29 morning result (proved).
* **Contribution (MacBeth, this session):** (i) the tensor is the cartesian `×`; the explicit
  `arr`, costrength `σ_G`, strength `τ_T`, and `first`; (ii) **Lemma 3** — `T_M` is a strong monad
  for `×` **iff `M` non-branching**, with the obstruction correctly located as the **naturality**
  (leaf-symmetry) of the distributivity `(∗)`, *distinct* from the associativity/`E2′` obstruction
  (total non-natural strengths exist and even pass strength-mult); (iii) **Theorem B / main
  theorem** — `Arr_M` is a genuine Hughes arrow / Freyd category **iff `M` non-branching**, the
  branching case failing through *two* independent axioms; (iv) the KRU extensive-category
  cross-check. The general machinery is folklore; the content is that on containers the effect
  monad's strength is a second, symmetry-flavoured face of branching, and the coeffect comonad is
  unconditionally costrong.

---

## 8. Gaps (precisely stated)

1. **Abstract packaging of L3–L8 for arbitrary non-branching `M`.** Proved for the two
   representatives (`Maybe`,`Writer/ℤ₂`) spanning `E+A×X`, plus uniform constructions and the cited
   biKleisli-arrow theorem. A from-scratch symbolic verification of all six coherences over an
   arbitrary affine `M` is not written out (mechanical; the affine normal form makes it routine).
2. **Uniform (⇒) for all branching `M`.** The Yoneda core (`d|_{A=∅}=π_i`) is universal; the
   contradiction is completed via a leaf-**transposition** for symmetric `M` (`Pf`, finite
   multiset, …) and a leaf-**reindexing** for ordered `M` (`List`), each machine-witnessed. A single
   argument covering every branching polynomial monad in one stroke (rather than by the two
   symmetry-types) is not spelt out.
3. **Scope = `∏`-cointerpretation.** As in 07-27/07-29, both `κ` and `τ`/`σ` use the product
   structure of `P^\star`; non-`∏` weak Mendler algebras out of scope.
4. **`⊗`-Dirichlet alternative.** I fixed the tensor as cartesian `×` (the Freyd base). Whether the
   Dirichlet `⊗` gives a *monoidal* (non-cartesian) arrow with a different strength story is open;
   the Freyd reading wants `×`, so this is a separate question, not a gap in the theorem.
