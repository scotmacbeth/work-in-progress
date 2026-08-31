# The Σ-lifting is just `M ◁ −`: Σ-monad ⟺ container-monad, and Bag refutes `reverse-total ⟹ Σ-monad`

**MacBeth — PROVE session, 2026-08-08 (deep-work).**
Resolves registry node `reverse-total-implies-coherent-section-OPEN` (speculative) in
`proofs/registry/effect-coeffect-arrows.json`. Companion to and re-framing of
`2026-08-07-sigma-monad-proved.md` (Reader/State Σ-monad) and
`2026-08-07-proof-relevance-boundary.md` (the □/∏/Σ boundary).

---

## 0. Headline

> **The Σ-container lifting is left composition-product by `M`:  `T^Σ_M(C) = M ◁ C`.**
> Consequently `(T^Σ_M, η^Σ, μ^Σ)` is a monad on `Cont` **iff `M` is a ◁-monoid in `Cont`
> (a *container monad*)** — equivalently, iff `M` is a Set-monad whose functor *and* structure
> maps are polynomial (a plain container). The "canonical section" `σ` of the earlier proof is
> nothing but the backward position map of `M`'s own multiplication, and the three coherence
> conditions **(U1),(U2),(A)** are exactly the ◁-monoid laws read on positions.
>
> **Hence `reverse-total ⟹ Σ-monad` is FALSE as a clean implication.** The witness is the
> **finite multiset monad `Bag`**: it is leaf-supported and reverse-total (its `μ` is a
> *bijection* on leaves, so every surviving leaf has a matching origin token), yet `T^Σ_Bag` is
> **not even a functor on `Cont`**, because `Bag` is not a container functor — it fails to
> preserve the connected pullback `A → 1 ← B`. Reader/State satisfy the coherence *not* by a
> miracle but because they **are** container monads; the meta-pattern holds — reverse-total is
> the pointwise/object-level shadow, container-monad structure is the coherence.

This is the resolution PROVE.md conjectured: the surviving-Σ-lifting story is *the ◁-monoid /
directed-container spine* (grant Path 2). Reader = the diagonal comonoid on `E`; State = the
store monad; both are `◁`-monoids, and *that* is why their sections cohere.

---

## 1. Setup (recap, notation of the boundary/census files)

A **container** `C=(S,P)`: shape set `S`, position set `P(s)` for each `s`. `⟦C⟧X = ∐_{s} X^{P(s)}`.
A **morphism** `φ=(f,f♯):(S,P)→(S',P')`: forward `f:S→S'` and, for each `s`, backward
`f♯_s: P'(fs) → P(s)`. `Cont` is this category; it is equivalent (monoidally) to the category
`Poly` of polynomial functors and natural transformations, with the composition product `◁`
corresponding to functor composition and unit `y=(1,1)` to `Id` (Niu–Spivak; my
`lean-monoidal-coherence-done`, `lean-cont-category-done`).

**Leaf-supported Set-monad `M`.** Each `m∈MX` carries a finite leaf set `lv(m)` with labels
`x_b∈X` (`b∈lv(m)`); `Mf` relabels leaves. Reader `MX=X^E` (`lv=E`, label of `e` is `m(e)`) and
State `MX=(St×X)^{St}` (`lv=St`, label of `s` is `π_X m(s)`) are such. **We will see the honest
content of "leaf-supported" is exactly "`M` is a container functor" — a *functorial* leaf
assignment — and that this, not the pointwise condition, is what matters.**

**Σ-lifting** (Ahman–Bauer's `∏`-partner on the surviving side of the ℤ/2 grading):
```
T^Σ_M(S,P) = (MS, P^Σ),   P^Σ(m) = ∐_{b∈lv(m)} P(x_b).
```
Unit `η^Σ_C`: fwd `η_S`, bwd the codiagonal fold `(b,p)↦p`. Mult `μ^Σ_C`: fwd `μ_S`, bwd
`(L,p)↦(σ(mm,L),p)` for a label-preserving section `σ:lv(μ mm)→I(mm)`,
`I(mm)=∐_{b∈lv(mm)}lv(inner_b)`.

**reverse-total(mm):** `∀L∈lv(μ mm). ∃ i∈I(mm). lab(i)=lab(L)` — every surviving leaf's label was
already an inner token's. This is *exactly* "the backward map `σ` exists pointwise, label-
preservingly" (boundary file, node `reader-state-reverse-total-universal`).

---

## 2. The identification `T^Σ_M(C) = M ◁ C`

> **Proposition 2.1.** For a container functor `M=(S_M,P_M)` and any container `C=(S,P)`, there is
> an equality of containers `T^Σ_M(C) = M ◁ C`, natural in `C`; and under it
> `η^Σ = η_M ◁ (−)`, `μ^Σ = μ_M ◁ (−)`.

*Proof (positions).* Write `MX = ∐_{s∈S_M} X^{P_M(s)}`; an element `m∈MX` is `(s, x:P_M(s)→X)`,
so `lv(m)=P_M(s)` and `x_b = x(b)`. The composite container is
```
⟦M ◁ C⟧X = ⟦M⟧(⟦C⟧X) = ∐_{s∈S_M} (⟦C⟧X)^{P_M(s)}
         = ∐_{s∈S_M} (∐_{s'∈S}X^{P(s')})^{P_M(s)}.
```
Its **shapes** are `∐_{s∈S_M}(S)^{P_M(s)} = M(S)` — i.e. an element `m∈M(S)` with `lv(m)=P_M(s)`,
labels `x_b∈S`. Its **positions** at that shape are `∐_{b∈P_M(s)} P(x_b) = ∐_{b∈lv(m)} P(x_b)`.
These are *exactly* the shapes `MS` and positions `P^Σ(m)` of `T^Σ_M(C)`. On morphisms both act by
`M ◁ φ`. Finally `η^Σ_C` (fwd `η_S`, bwd fold) is the whiskering `η_M ◁ C` of the container-unit
`η_M:y→M`, and `μ^Σ_C` (fwd `μ_S`, bwd `σ`) is the whiskering `μ_M ◁ C` of the container-mult
`μ_M:M◁M→M`, whose backward map at `mm` is precisely a label-preserving `σ:lv(μ mm)→I(mm)`. ∎

So `T^Σ_M = M ◁ (−)`: **left ◁-multiplication by the container `M`.** Nothing more.

---

## 3. Σ-monad ⟺ container-monad (the characterization, both directions)

> **Theorem 3.1.** Let `M` be a container functor. The following are equivalent.
> 1. `(T^Σ_M, η^Σ, μ^Σ)` is a monad on `Cont`.
> 2. `(M, η_M, μ_M)` is a ◁-monoid in `(Cont, ◁, y)` — a **container monad**.
> 3. `(⟦M⟧, ⟦η_M⟧, ⟦μ_M⟧)` is a monad on `Set` (with polynomial structure maps).
> Under any of them the coherence conditions **(U1),(U2),(A)** of `2026-08-07-sigma-monad-proved.md`
> hold *automatically*: they are the backward parts of the ◁-monoid unit and associativity laws.

*Proof.* **(2⟺3)** The extension `Cont ≃ Poly ↪ [Set,Set]` is fully faithful and *strong
monoidal* (`◁ ↦ ∘`, `y ↦ Id`); a fully faithful strong monoidal functor reflects and creates
monoids, so `M` is a ◁-monoid in `Cont` iff `⟦M⟧` is a monoid in `([Set,Set],∘,Id)` = a Set-monad.
(Full faithfulness = "every natural transformation between polynomial functors is a polynomial
morphism", Yoneda: `Nat(∐_s y^{P_M s}, Q) ≅ ∏_s Q(P_M s)` = shape map + backward position map,
composition-respecting.)

**(2⟹1)** Any monoid `A` in a monoidal category `(V,⊗,I)` makes `A⊗(−):V→V` a monad, with
multiplication `A⊗A⊗(−) →^{m⊗-} A⊗(−)` and unit `(−)≅I⊗(−)→^{e⊗-}A⊗(−)`. Apply with
`(V,⊗,I)=(Cont,◁,y)`, `A=M`: by Prop 2.1 this monad is exactly `(T^Σ_M, η^Σ, μ^Σ)`.

**(1⟹2)** By Prop 2.1 the structure maps of `T^Σ_M` are `η_M◁(−)` and `μ_M◁(−)`; the monad laws
are equalities of whiskered 2-cells, natural in `C`. Evaluating at `C = y` (using `M◁y ≅ M`,
`M◁M◁y ≅ M◁M`) yields precisely the ◁-monoid unit and associativity laws for `(M,η_M,μ_M)`.
(Conversely those laws, whiskered by `C`, give the monad laws for all `C` — this is the direction
that made "all `C`" force the index identities in the reduction lemma of the 08-07 proof.)

**(U1),(U2),(A) are the ◁-monoid laws.** The backward map of `μ_M` *is* `σ`; the backward map of
`η_M` is the fold. The left/right unit ◁-monoid laws, read on positions, are exactly (U1),(U2); the
◁-associativity of `μ_M`, read on positions, is exactly the section pentagon (A). Hence the 08-07
proof's three conditions are automatic once `M` is a container monad — the "canonical diagonal /
threading section" is just `μ_M`'s backward map, and its coherence is `μ_M`'s associativity. ∎

**Reader/State recovered.** Reader `= (1,E) = y^E` is a container monad: its `◁`-monoid structure
is the *unique comonoid on the set `E`* (diagonal `E→E×E`), so `σ(mm,e)=(e,e)`. State `= (St^St,
const St)` is the store/state container monad, `σ` = threading. Theorem 3.1 subsumes the entire
08-07 computation: those pages verified, in coordinates, that Reader and State are ◁-monoids.

---

## 4. `reverse-total ⟹ Σ-monad` is FALSE: the Bag counterexample

The clean implication would say: *pointwise existence of a label-preserving section (reverse-total)
already yields a Σ-monad.* Theorem 3.1 says the real requirement is that `M` be a **container
monad**. The gap between them is realised by an analytic-but-not-polynomial monad.

**The finite multiset monad `Bag`.** `Bag X` = finite multisets over `X`; `η x = {x}`,
`μ = ⊎` (multiset union). It is leaf-supported pointwise: `m={x_1,…,x_n}` has `n` leaves labelled
`x_1,…,x_n`, and `Bag f` relabels them (leaf-count preserved — multiplicities are kept).

> **Lemma 4.1 (Bag is reverse-total, indeed forward-total).** For every `mm∈Bag Bag S`, the union
> `μ mm` collects exactly the inner tokens: the canonical map `I(mm) → lv(μ mm)` is a *bijection*.
> Hence every surviving leaf has a (unique) origin token of equal label — reverse-total holds.

*Proof.* `μ mm = ⊎_{b∈lv(mm)} inner_b` is the disjoint union of the inner leaf-multisets; its leaf
set is literally `∐_{b} lv(inner_b) = I(mm)`, labels preserved. ∎

So `Bag` clears the hypothesis of the putative implication as strongly as possible: not only does a
section exist, `μ` is a leaf-*bijection*, `σ = id`.

> **Lemma 4.2 (Bag is not a container functor).** `Bag` does not preserve the connected pullback
> `A →^{!} 1 ←^{!} B` (i.e. `Bag(A×B) ≇ Bag A ×_{Bag 1} Bag B`). Container/polynomial functors
> preserve all connected limits (wide pullbacks), so `Bag ∉ Cont`.

*Proof (computed witness).* Take `A=B={0,1}`, so `A×B` has 4 elements. Compare cardinalities graded
by total size `n` (fibre over `n∈ℕ = Bag 1`):
`|Bag(A×B)|_n = C(n+3,3)` vs `|Bag A ×_{Bag1} Bag B|_n = (n+1)^2`.
For `n=2`: `10 ≠ 9`; for `n=3`: `20 ≠ 16` (verified below). The comparison map is not injective: the
two distinct size-2 multisets
```
w₁ = {(0,0),(1,1)},   w₂ = {(0,1),(1,0)}   over A×B
```
have the *same* image `(π_A, π_B) = ({0,1},{0,1})` — the multiset structure has forgotten the
pairing. Preservation fails, so `Bag` is not familially representable, i.e. not a container. ∎
(This is the classical reason `Bag`/multiset is *analytic but not polynomial*: it has nontrivial
`Sₙ` symmetries; the leaf assignment is not natural.)

> **Theorem 4.3 (refutation).** `reverse-total ⟹ Σ-monad` is false. `Bag` is leaf-supported and
> reverse-total (Lemma 4.1) but `T^Σ_Bag` is not a monad on `Cont` — it is not even a functor on
> `Cont`.

*Proof.* Suppose `T^Σ_Bag` were an endofunctor of `Cont`. Restrict it along the full embedding
`Set ↪ Cont`, `S ↦ (S,1)` (positions singleton; morphisms `(S,1)→(S',1)` are just functions
`S→S'`, backward trivial). On objects `T^Σ_Bag(S,1) = (Bag S, lv(−))` — shape set `Bag S`,
positions `lv(m)` at `m`. Functoriality would supply, for each `f:S→S'`, a *container morphism*
`T^Σ_Bag(S,1) → T^Σ_Bag(S',1)`, i.e. forward `Bag f` **plus a natural backward map**
`lv(Bag f · m) → lv(m)`, compatibly with composition. That is precisely a **container structure on
the functor `Bag`** (a functorial, label-preserving leaf assignment). By Lemma 4.2 no such structure
exists (`Bag ∉ Cont`). Hence `T^Σ_Bag` is not a functor on `Cont`, a fortiori not a monad — despite
`Bag` being reverse-total. ∎

Concretely, the obstruction is visible on the witness of Lemma 4.2: a relabeling `f` that identifies
labels forces a choice of "which inner leaf survives where" among symmetric tokens, and no choice is
natural in `f` — exactly the failure the section pentagon (A) would need, now located at the level of
`T^Σ` being well-defined at all.

---

## 5. The sharpened theorem, and what "reverse-total" really is

Putting §§2–4 together:

> **Theorem 5.1 (characterization; resolves the OPEN node).**
> For a leaf-supported Set-monad `M`, `T^Σ_M = M ◁ (−)`, and
> * `T^Σ_M` is an endofunctor of `Cont` ⟺ `M` is a **container functor** (functorial leaves);
> * given that, `T^Σ_M` is a **monad** on `Cont` ⟺ `M` is a **container monad** (◁-monoid).
>
> `reverse-total(mm) ∀mm` is the strictly weaker **pointwise/object-level** condition "each `μ_M`
> has *some* label-preserving backward map"; it does **not** imply either bullet. `Bag` satisfies
> reverse-total but neither bullet. The genuine extra content over reverse-total is: the backward
> maps are *natural in the labels* (container functor) and *coherent* (◁-monoid). Reader and State
> supply both because they are container monads; the diagonal/threading section is `μ_M`'s backward
> map and (U1),(U2),(A) are its unit/associativity laws.

**What forces the coherence (answering PROVE.md's "identify the extra structure").** Not a bespoke
directedness axiom: the extra structure is *precisely* "`M` lives in `Cont` as a ◁-monoid." Directed
containers `= ◁-comonoids` (my `dcont-morphisms-are-cofunctors`), and container **monads** are the
`◁`-monoid partner; Reader (diagonal comonoid `E`) and State (store) are the two motivating monoids.
So the surviving-Σ-lifting is welded to the directed-container / composition-monoid spine, as
conjectured — but the weld is an *identity of endofunctors*, `T^Σ_M = M◁−`, not a coincidence of
sections.

**Reconciliation with the 08-07 proof.** Nothing there is wrong; Theorem 3.1 *explains* it. The
reduction lemma ("every backward map is a pushforward `Σ_α`, and `Σ` is faithful") is the shadow of
full faithfulness `Cont ≃ Poly ↪ [Set,Set]`; verifying (U1),(U2),(A) for Reader/State was verifying,
by hand, that they are ◁-monoids. The only correction is to the *open flag*: the hoped-for clean
`reverse-total ⟹ Σ-monad` fails, and the meta-pattern (structure returns a finer distinction, now 6
for 6) is intact — the finer distinction is exactly *pointwise section vs container-monad structure*,
i.e. *analytic vs polynomial*.

---

## 6. Verification (computational)

`scratch/sigma-monad-coherence/` (this session, `bag_not_container.py`):
- **Lemma 4.2**, cardinality obstruction: `|Bag(2×2)|_2 = 10 ≠ 9 = |Bag2 ×_{Bag1} Bag2|_2`;
  `|·|_3 = 20 ≠ 16`. Collision witness `w₁={(0,0),(1,1)}`, `w₂={(0,1),(1,0)}` distinct with equal
  `(π_A,π_B)`-image. `Bag` fails connected-pullback preservation ⟹ `Bag ∉ Cont`. ✓
- **Prop 2.1** position match `T^Σ_M(C) = M◁C`: shapes `= MS`, positions `= ∐_{lv(m)}P(x_b)`, checked
  against the harness's `T_container` for Reader/State on the base containers. ✓
- Reader/State remain Σ-monads (08-07), now *because* they are container monads (Theorem 3.1); their
  harness sections `(L,L)` / `(L,h(L))` are the ◁-monoid backward maps.

---

## 7. One line

`T^Σ_M = M ◁ −`, so the Σ-lifting is a monad on `Cont` **iff `M` is a container monad**; the
"canonical section" is just `M`'s own backward multiplication and its coherence is `M`'s
associativity — and `Bag`, reverse-total but only *analytic* (not a container), shows that pointwise
sections are not enough: `reverse-total ⟹ Σ-monad` is false, the true condition is the ◁-monoid /
directed-container structure.
