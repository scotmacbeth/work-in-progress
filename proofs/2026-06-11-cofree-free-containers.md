# The cofree comonad and free monad of a container, as containers

**MacBeth — 2026-06-11 deep-work (prove) session.**
Feeds book `papers/category-of-containers.tex` (free/cofree, currently deferred to the
Phase-2 chapter).

Throughout we work in a setting with W-types and M-types (e.g. `Set`, or any locally
cartesian closed category with the relevant initial algebras and terminal coalgebras); this
guarantees the carriers below exist and are again containers (Abbott–Altenkirch–Ghani 2005).

---

## 0. Conventions

A **container** `C = S ◁ P` is a set of shapes `S` with a family of position sets
`P : S → Set`. Its **extension** is the polynomial endofunctor
`⟦C⟧ X = Σ_{s:S} (P(s) → X)`.

The **composition (substitution) product** `◁` satisfies `⟦C ◁ D⟧ = ⟦C⟧ ∘ ⟦D⟧` and is given
on data by
- shapes: `Σ_{s:S} (P(s) → T)` (a `C`-shape `s` and a `D`-shape `f(p)` for each `p:P(s)`);
- positions at `(s,f)`: `Σ_{p:P(s)} Q(f(p))`.

Its unit is the **identity container** `I = 1 ◁ 1` with `⟦I⟧ = Id`.

A **container morphism** `(u,f) : (S◁P) → (T◁Q)` is `u : S → T` (covariant on shapes) and
`f : Π_{s:S} (Q(u s) → P(s))` (contravariant on positions); its extension is the natural
transformation `(s,x) ↦ (u s, x ∘ f_s)`. The extension functor `⟦-⟧ : Cont → [Set,Set]` is
fully faithful and strong monoidal `(Cont,◁,I) → ([Set,Set],∘,Id)` (representation theorem,
AAG 2005). Hence a (co)monad structure on `⟦C⟧` whose maps are polynomial is the same as a
(co)monoid structure on `C` in `(Cont,◁)`.

We use the book's **directed container** vocabulary: a directed container is `S◁P` with a
root `o(s)∈P(s)`, a sub-shape `s↓p∈S`, and a shift `p⊕q∈P(s)` (`q∈P(s↓p)`), satisfying
D1 `s↓o=s`, D2 `o⊕q=q`, D3 `p⊕o=p`, D4 `s↓(p⊕q)=(s↓p)↓q`, D5 `(p⊕q)⊕q'=p⊕(q⊕q')`.
**Theorem (ACU; in the book).** Directed containers are exactly the comonoids in `(Cont,◁)`,
equivalently small categories, equivalently polynomial comonads.

---

## 1. The free monad `C*` (initial / W-type / well-founded)

**Definition.** Let `C = S◁P`. Define the container `C* = S* ◁ P*` by
- `S* = μY. ( 1 + Σ_{s:S} (P(s) → Y) )` — the set of well-founded `C`-trees with a
  distinguished **variable-leaf** constructor (the `1` summand). A shape is either a *variable
  leaf* `•`, or an internal node `node(s, c)` with `s:S` and `c : P(s) → S*`.
- `P*(w)` = the set of **variable leaves** of `w`, defined by recursion:
  `P*(•) = 1`, and `P*(node(s,c)) = Σ_{p:P(s)} P*(c(p))`.

**Proposition 1 (extension).** `⟦C*⟧ A ≅ μX. ( A + ⟦C⟧ X )`, i.e. `⟦C*⟧` is the carrier of
the **free monad** on `⟦C⟧`.

*Proof.* `μX.(A+⟦C⟧X)` has constructors `inl : A → ·` and
`inr : Σ_{s}(P(s)→·) → ·`. Map an element to `Σ_{w:S*}(P*(w)→A)` by induction:
`inl(a) ↦ (•, λ(∗).a)`; `inr(s,k)` with `k:P(s)→μX.(A+⟦C⟧X)` maps each `k(p)` to
`(w_p, ℓ_p)` and yields `(node(s, λp.w_p), [ℓ_p]_p)` where `[ℓ_p]` is the copairing on
`P*(node(s,·)) = Σ_p P*(w_p)`. Both directions are inverse by the universal property of `μ`
(initial algebra), since `S* ≅ 1 + Σ_s(P(s)→S*)` and `Σ_{w}(P*(w)→A)` carries the same
`A + ⟦C⟧(-)`-algebra structure. ∎

**Monad structure (as container morphisms).**
- **Unit** `η : I → C*`: `u_η(∗) = •`, `f_η` trivial (`P*(•)=1 → 1`). Extension:
  `a ↦ (•, a)` = the variable leaf labelled `a`.
- **Multiplication** `μ : C* ◁ C* → C*`. A `C*◁C*`-shape is `(w, g)` with `g : P*(w) → S*`
  (a tree grafted at each variable leaf of `w`). Define
  `u_μ(w,g) = graft(w,g)` (replace each variable leaf `p` of `w` by `g(p)`), and
  `f_μ(w,g)` = the canonical isomorphism `P*(graft(w,g)) ≅ Σ_{p:P*(w)} P*(g(p))` (= the
  `C*◁C*`-position set), which is the **identity** on positions. Extension: substitution.

**Theorem 1 (monad laws).** `(C*, η, μ)` is a monoid in `(Cont,◁)`; equivalently `⟦C*⟧` is
the free monad on `⟦C⟧`. The laws reduce to the monoid laws of **grafting**:
- left/right unit `μ∘(η◁id)=μ∘(id◁η)=id` ⟺ grafting the single variable leaf is neutral;
- associativity `μ∘(μ◁id)=μ∘(id◁μ)` ⟺ grafting is associative (substitution is associative).

On positions every map is a canonical (de)composition isomorphism of `Σ`-types, so the laws
are exactly the coherence of those isomorphisms. *(Cited: AAG W-types; Spivak Poly 2021,
free monad = tree polynomial. The container-language statement and the law reduction to
grafting are re-derived here.)*

---

## 2. The cofree comonad `C^∞` (terminal / M-type / non-well-founded)

**Definition.** Define `C^∞ = S^∞ ◁ P^∞` by
- `S^∞ = νY. Σ_{s:S} (P(s) → Y)` — the **M-type** `M_C` of (possibly infinite) `C`-trees: a
  shape is `⟨s, c⟩` with `s:S` and `c : P(s) → S^∞`, generated coinductively (no variable
  leaves; the tree branches forever unless a shape has empty positions).
- `P^∞(w)` = the set of **nodes** of `w`, i.e. **finite paths from the root**:
  `P^∞(⟨s,c⟩) = 1 + Σ_{p:P(s)} P^∞(c(p))` — the empty path `•` (root) plus, for each
  `p:P(s)`, the paths into the `p`-th child. Each path is finite even when `w` is infinite.

**Proposition 2 (extension).** `⟦C^∞⟧ A ≅ νX. ( A × ⟦C⟧ X )`, i.e. `⟦C^∞⟧` is the carrier of
the **cofree comonad** on `⟦C⟧`: the type of (possibly infinite) `C`-trees with **every node
labelled** by an element of `A`.

*Proof.* Dual to Prop. 1, using the terminal coalgebra. `νX.(A×⟦C⟧X)` has destructor
`⟨head, tail⟩` with `head : · → A`, `tail : · → Σ_s(P(s)→·)`. The position recursion
`P^∞(⟨s,c⟩)=1+Σ_p P^∞(c(p))` gives
`(P^∞(w)→A) ≅ A × Π_{p:P(s)} (P^∞(c(p))→A)`, so
`Σ_{w:S^∞}(P^∞(w)→A) ≅ A × Σ_s (P(s) → Σ_{w'}(P^∞(w')→A))`, the `A×⟦C⟧(-)`-coalgebra whose
anamorphism is the iso. ∎

**Comonad structure (as container morphisms).**
- **Counit** `ε : C^∞ → I`: `u_ε` trivial; `f_ε(w)(∗) = •` (the **root**). Extension:
  `(w,ℓ) ↦ ℓ(•)` extracts the **root label**.
- **Comultiplication** `δ : C^∞ → C^∞ ◁ C^∞`. A `C^∞◁C^∞`-shape is `(w, h)` with
  `h : P^∞(w) → S^∞`. Define `u_δ(w) = (w, λn. w/n)`, where `w/n` is the **subtree of `w`
  rooted at node `n`** (label each node by the subtree hanging from it), and
  `f_δ(w)(n,m) = n·m` (**path concatenation**: `m` is a node of `w/n`, so `n` followed by `m`
  is a node of `w`). Extension: the "all-subtrees" map relabelling each node by its subtree.

**Theorem 2 (comonad laws).** `(C^∞, ε, δ)` is a comonoid in `(Cont,◁)`; equivalently `⟦C^∞⟧`
is the cofree comonad on `⟦C⟧`. The laws reduce to the monoid laws of **path concatenation**:
- left/right counit ⟺ `•·m = m` and `n·• = n` (the root is the empty path);
- coassociativity ⟺ `(n·m)·k = n·(m·k)`.

---

## 3. `C^∞` is a directed container (the clean statement)

**Theorem 3.** `C^∞ = S^∞ ◁ P^∞` is a **directed container** with
> `o(w) = •` (root / empty path), `w ↓ n = w/n` (subtree at node `n`),
> `n ⊕ m = n·m` (path concatenation).

The five laws hold tautologically once `w/(n·m) = (w/n)/m` is observed:
- **D1** `w ↓ o(w) = w/• = w`;
- **D2** `o(w) ⊕ m = •·m = m`;
- **D3** `n ⊕ o(w↓n) = n·• = n`;
- **D4** `w ↓ (n⊕m) = w/(n·m) = (w/n)/m = (w↓n)↓m`;
- **D5** `(n⊕m)⊕k = (n·m)·k = n·(m·k) = n⊕(m⊕k)`.

By the ACU theorem this directed container **is** the comonad of Theorem 2 (the comonad it
induces has counit `f_ε(w)(∗)=o(w)` and comultiplication `u_δ(w)=(w,λn.w↓n)`,
`f_δ(w)(n,m)=n⊕m`, which are exactly `ε, δ`). Thus Theorem 2 and Theorem 3 are the same fact
told twice — the cofree comonad of a container is the **cofree directed container** on it.

**Corollary (the small category).** Under directed-container ≅ small-category, `C^∞`
corresponds to the **subtree category** `𝒯_C`:
- objects = trees `w ∈ S^∞ = M_C`;
- a morphism `w → w'` = a node `n ∈ P^∞(w)` with `w/n = w'` (target = subtree at `n`);
- identity at `w` = the root `•`; composition = path concatenation.

`ε` reads off the identity-component (root), `δ` is "factor every node-path through its
intermediate subtree".

> **⛔ NOVELTY WITHDRAWN 2026-07-14 (cite-check resolved, and it went badly).** The old note here
> claimed "MacBeth contribution: the explicit `o/↓/⊕` data in the book's D1–D5 form". **It is
> Niu–Spivak arXiv:2312.00990 Prop. 8.33 (p. 306), verbatim**: objects = `p`-trees; a morphism out
> of `T` is a **rooted path**; **codomain = the subtree at the path's end**; **identity = the empty
> path**; **composition = concatenation**. Carrier: **Prop. 8.18 (p. 297)**,
> `𝔱_p ≔ Σ_{T∈tree_p} y^{vtx(T)}`. Adjunction: **Thm. 8.45 (p. 314)**. **The whole of §2–§3 is prior
> art.** ⚠️ Note their directions are **`vtx(T)` — ALL vertices ≅ all finite rooted paths**, which is
> exactly `P^∞` above (§2): the mathematics here is *right*; only the novelty claim was wrong.

---

## 4. Worked small cases

### 4a. `C = 1 + X` (Maybe). `S = {nil (P=∅), cons (P=1)}`.
- **Free** `C*`: `S* = μY. 1 + (1 + Y)`. A shape is a finite chain of `cons` ending in
  either the variable leaf `•` or `nil`. `⟦C*⟧A ≅ μX.(A+1+X) = ` lists "of length `n`
  terminated by a variable `a:A` or by `nil`". This is the **free monad on `Maybe`**.
- **Cofree** `C^∞`: `S^∞ = νY. 1 + Y = ℕ̄` (conaturals: a length, possibly `∞`).
  `⟦C^∞⟧A ≅ νX.(A×(1+X)) = ` **nonempty colists of `A`** (a head and maybe a tail). The
  induced comonad is the classic **nonempty-list / "tails" comonad**; `δ` is `tails`,
  `ε` is `head`. The subtree category `𝒯_C` is the poset `(ℕ̄, ≥)` of "drop a prefix".

### 4b. Binary. `S = {leaf (P=∅), node (P={L,R})}`.
- **Free** `C*`: finite binary trees with variable leaves — the **free monad on `X↦1+X²`**;
  `μ` is grafting binary trees at variables.
- **Cofree** `C^∞`: possibly-infinite `A`-labelled binary(-or-leaf) trees; `δ` relabels each
  node by the whole subtree there; `ε` reads the root label.

---

## 5. Verification (computational)

Scripts: `projects/scratch/cofree_free_laws.py`, `projects/scratch/cofree_dircont.py`.
Maps implemented **via the container formulas** (root/subtree/concat; leaf/graft), then laws
checked by exhaustive enumeration of small labelled trees.

| check | container | range | result |
|---|---|---|---|
| comonad: counitL, counitR, coassoc | Maybe | depth ≤ 4 (8 trees) | PASS |
| comonad | Bin | depth ≤ 3 (38 trees) | PASS |
| monad: unitL, unitR, assoc | Maybe | size ≤ 3 (15 trees) | PASS |
| monad | Bin | size ≤ 3 (2707 trees) | PASS |
| directed container D1–D5 | Maybe | depth ≤ 4 | PASS |
| directed container D1–D5 | Bin | depth ≤ 3 | PASS |

The directed-container check confirms concatenation is closed in the node-set (`n⊕m ∈ P^∞(w)`)
and associative, and that `w/(n·m)=(w/n)/m` — the only non-tautological identity behind D4.

---

## 6. Cited vs MacBeth (honesty ledger)

- **[Cited]** carriers `S* = μ`-tree, `S^∞ = ν`-tree (M-type) and that the free monad /
  cofree comonad of a polynomial are again polynomial: AAG (W/M-types) 2005; Spivak,
  *Polynomial Functors* 2021 (cofree comonad = tree polynomial). Free monad = tree-with-leaves
  polynomial.
- **[Cited]** cofree comonoid = tree comonoid with subtree/path category: **Niu–Spivak,
  arXiv:2312.00990 — Prop. 8.18 (p. 297), Prop. 8.33 (p. 306), Thm. 8.45 (p. 314)**
  (cite-check RESOLVED 2026-07-14); polynomial comonad = small category = directed container:
  Ahman–Chapman–Uustalu.

**⛔ LEDGER CORRECTED 2026-07-14 — the old `[MacBeth]` line was an over-claim and is withdrawn.**
- **[Cited — the COFREE half, IN FULL]** the container-language derivation, the structure maps, the
  reduction of the comonad laws to path-concatenation, **and the `o/↓/⊕` D1–D5 packaging** are **all**
  Niu–Spivak **Prop. 8.33** (see §3 banner). **There is no MacBeth delta on the cofree side.** The
  exhaustive small-case checks stand as *verification*, not as *contribution*.
  ⚠️ Directions are **ALL vertices ≅ all finite rooted paths** (`vtx(T)`), **not leaves, not
  root-to-leaf paths**. §2's `P^∞(⟨s,c⟩) = 1 + Σ_p P^∞(c(p))` is correct; the *summaries* of it
  ("nodes-as-paths", "M-tree ◁ paths") were the ambiguous part and were being misread. Also: the book
  **never displays a fixed-point equation** for `tree_p` — **Ex. 8.16** only asserts it is the
  **terminal `p`-coalgebra**, uncredited (classically **Adámek/Barr**). So `S^∞ = νY.…` above is
  legitimate but must be attributed there, **not** to Niu–Spivak.
- **[★ LIVE — the FREE half]** **Niu–Spivak never construct the free monad**, and **characterising
  monads in Poly is their Chapter 9, Question 11 — an explicit OPEN QUESTION.** So §1 (`C*`, grafting)
  is **not** scooped by that book, and a co-directed D1–D5-style packaging of `C*` is a **real target**
  (= Neil's Phase 2). **Clear Gambino–Kock arXiv:0906.4931 first** (free monad on a polynomial is
  polynomial; positions = P-trees, directions = **leaves** — for the *free* monad it genuinely is
  leaves). ⚠️ Ch. 9 cites no one and hedges "may or may not be known": authors' ignorance, not the
  literature's. Independent audit still owed.

## 7. Gaps / open

- **No new gap in the mathematics.** Every step is by definition, the AAG representation
  theorem, the ACU directed-container theorem, or finite computation.
- **[cite-check]** exact theorem numbers in Spivak (2021) and Spivak–Niu for the cofree
  comonoid / tree-polynomial statements — to be filled on the next browse cycle (browsing
  disallowed this session). Flagged, not hidden.
- **Scope note:** the constructions assume W/M-types exist; in general LCCCs this is a
  hypothesis, not automatic. Stated in §0.
