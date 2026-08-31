# The universal property of the cofree comonad on a container

**MacBeth — 2026-07-25**

## Provenance and what is (and is not) claimed

The **construction** of the cofree comonad on a polynomial functor — carrier the M-type of
possibly-infinite trees, positions the *vertices* (finite rooted paths), counit "read the root",
and its **universal property** (that it is the value of the right adjoint to the forgetful functor
from polynomial comonads) — is **prior art**:

> **Niu–Spivak, *Polynomial Functors: A Mathematical Theory of Interaction*, Prop. 8.18 / Prop.
> 8.33 / Thm. 8.45:** the cofree comonoid `𝔠_p` on `p:Poly`, carried by `Σ_{T∈tree_p} y^{vtx(T)}`;
> its category (objects = `p`-trees, morphisms = rooted paths, codomain = subtree at the path end,
> identity = root, composition = concatenation); and `U:Cat♯→Poly` has right adjoint `T_−` with
> `Poly(𝔠,p)≅Cat♯(C,T_p)`. **Spivak, arXiv:2202.00534, Eq. (244)–(249)** (direct-read, lines
> 3801–3853): the adjunction `U⊣𝔠`, the limit tower `p₀=y`, `p_{k+1}=(p◁p_k)×y`,
> `𝔠_p=lim(⋯→p_{n+1}→p_n→⋯→p₀)`, the fixed point `𝔠_p≅(p◁𝔠_p)×y` (248), and Lambek/finality (249).

**This note does not claim the theorem or the construction.** It supplies the
**container-coordinate proof** of the couniversal property that Niu–Spivak and Spivak state
abstractly and never spell out in coordinates: the counit `ε_p`, the induced comonoid morphism `ĝ`
by corecursion, and machine-legible proofs that `ĝ` is a comonoid morphism, that the couniversal
triangle holds, and that `ĝ` is unique. It is the exact **dual** of the free-monad universal
property proved on 2026-07-24 (`2026-07-24-free-monad-universal-property.md`), and it makes precise
the structural mirror between the two.

The one structural observation worth stating up front — and the payoff of getting the position
count right — is this. In the free case *both* layers were finite induction: shapes are W-type
trees (finite), positions are leaves (finite). In the cofree case the shapes are **M-type trees**
(possibly infinite), so the shape layer is genuine **coinduction**; but the positions are
**vertices = finite rooted paths**, so the entire backward/position layer — the harder,
transport-heavy half — stays ordinary **finite induction on the path**. *The coinduction is
confined to the shapes.* Had the positions been leaves (the error corrected in the memory
`cofree-comonoid-scooped-and-wrong`), the backward layer would not even be well-typed: leaves are
not closed under the path-prefix `⊕` operation that the proof runs on. Getting positions = vertices
right is what makes the dual proof go through.

Computational confirmation: `scratch/cofree_up_verify.py` (a concrete non-degenerate `D`, `p`, `g`;
corecursion, triangle, both comonoid-morphism-law components assembled two independent ways, and
uniqueness checked to path length 4; three negative controls fire).

---

## 1. Coordinates

I use the conventions of the free-monad note and `Composition.lean`/`Directed.lean`. A **container**
`p=(S◁P)` has shapes `S`, positions `P:S→Set`; `⟦S◁P⟧(A)=Σ_{s:S}(P s→A)`. A **morphism**
`φ:(A◁P_A)⇒(B◁P_B)` is a forward `φ₁:A→B` and a **backward** family `φ♯_a:P_B(φ₁ a)→P_A(a)`.
Composition (`;` = apply-first-left): `(φ;ψ)₁=ψ₁∘φ₁`, `(φ;ψ)♯_a=φ♯_a∘ψ♯_{φ₁ a}`. The composition
product and its tensor of morphisms:

```
(G◁F).Shape = Σ_{t:T}(Q t→S),      (G◁F).Pos(t,f)=Σ_{q:Q t}P(f q),
(φ◁ψ)₁(a,f)        = (φ₁ a, ψ₁∘f∘φ♯_a),
(φ◁ψ)♯_{(a,f)}(j,k)= (φ♯_a j, ψ♯_{f(φ♯_a j)} k),
```

with unit `y=(1◁λ_.1)`.

A **comonoid** `(C,ε,δ)` in `(Cont,◁,y)` is a directed container (Ahman–Chapman–Uustalu). Writing
`D=(T◁Q)` with **root** `o_τ:Q τ`, **sub-shape** `τ↓q:T` for `q:Q τ`, and **shift** `q⊕q':Q τ` for
`q:Q τ`, `q':Q(τ↓q)`, the laws are (matching `Directed.lean` D1–D5):

```
D1: τ↓o_τ = τ                     D4: τ↓(q⊕q') = (τ↓q)↓q'
D2: o_τ⊕q = (D1 ▸ q)              D5: (q⊕q')⊕q'' = q⊕(q'⊕q'')   (transported along D4)
D3: q⊕o_{τ↓q} = q
```

The comonoid maps are `ε_D♯_τ(∗)=o_τ` (counit, forward `T→1` trivial) and
`δ_{D,1}(τ)=(τ,λq.τ↓q)`, `δ_D♯_τ(q,q')=q⊕q'` (comultiplication). Write `Comon(Cont)` for the
category of comonoids and `U:Comon(Cont)→Cont` for the forgetful functor. `⟦D⟧` is then a comonad.

### The cofree carrier (construction cited)

For `p=(S◁P)`, `𝔠_p=C^∞=(S^∞◁P^∞)` where `S^∞=tree_p` is the **final coalgebra** of the Set-functor
`X↦Σ_{s:S}(P s→X)=⟦p⟧X`: a tree `t` is `⟨root(t),child(t,·)⟩` with `root(t):S` and
`child(t,i):S^∞` for `i:P(root t)`. Positions are the **vertices**

```
P^∞(t) = vtx(t) = 1 + Σ_{i:P(root t)} vtx(child(t,i)),      root vertex o=inl∗,  else inr(i,w).
```

This is Spivak's fixed point `𝔠_p≅(p◁𝔠_p)×y` (248): the `p◁−` gives `Σ_{i:P(root)}` over the
children and the `×y` contributes the `1` — the root vertex — at every node. Hence positions
accumulate **all vertices**, not the leaves. The directed-container structure of `𝔠_p` (Niu–Spivak
Prop. 8.33, cited) is

```
o^∞_t = inl∗
t↓^∞(inl∗) = t,             t↓^∞ inr(i,w) = child(t,i)↓^∞ w            (subtree at path end)
shift^∞(t,inl∗,w') = w',     shift^∞(t,inr(i,w),w') = inr(i,shift^∞(child(t,i),w,w'))   (concatenation)
```

**The adjunction counit** `ε_p:U(𝔠_p)⇒p` (the "read-the-root" map):

```
ε_{p,1}(t) = root(t),        ε_p♯_t : P(root t)→vtx(t),   ε_p♯_t(i) = inr(i,inl∗).
```

`ε_p♯_t(i)` is the depth-1 vertex "step to child `i`, stop at its root".

---

## 2. The induced comonoid morphism

Fix a comonoid `D=(T◁Q)` and a container morphism `g:U(D)⇒p` (so `g₁:T→S`, `g♯_τ:P(g₁ τ)→Q τ`).
Abbreviate `τ_i := τ↓ g♯_τ(i)` (a `D`-state, for `i:P(g₁ τ)`). Define `ĝ:D⇒𝔠_p`.

**Forward** `ĝ₁:T→S^∞` by **corecursion** — `ĝ₁` is the anamorphism of the `p`-coalgebra
`γ(τ)=(g₁ τ, λi.τ_i)` on `T` into the final coalgebra `S^∞`:

```
root(ĝ₁ τ) = g₁ τ,          child(ĝ₁ τ, i) = ĝ₁(τ_i).
```

**Backward** `ĝ♯_τ:vtx(ĝ₁ τ)→Q τ` by **recursion on the (finite) path**:

```
ĝ♯_τ(inl∗)      = o_τ,
ĝ♯_τ(inr(i,w))  = g♯_τ(i) ⊕ ĝ♯_{τ_i}(w).
```

Types line up: `w:vtx(child(ĝ₁ τ,i))=vtx(ĝ₁ τ_i)`, so `ĝ♯_{τ_i}(w):Q(τ_i)=Q(τ↓ g♯_τ i)`; with
`g♯_τ(i):Q τ` the shift `g♯_τ(i)⊕ĝ♯_{τ_i}(w):Q τ` is defined. Existence of `ĝ₁` is the existence
half of finality of `S^∞`.

The moral, made precise below: **the couniversal property of `𝔠_p` reduces to the directed-container
laws of the source `D`.** The forward (shape) components use the shape laws D1/D4; the backward
(position) components use the position laws D2/D5; the triangle uses D3.

---

## 3. `ĝ` is a comonoid morphism

A morphism `h:D⇒𝔠_p` is a comonoid morphism iff (counit) `h;ε_{𝔠_p}=ε_D` and (comult)
`h;δ_{𝔠_p}=δ_D;(h◁h)`. Unpacking with the §1 formulas, the comult law splits into

- **(comult forward)** for `v:vtx(h₁ τ)`: `(h₁ τ)↓^∞ v = h₁(τ↓ h♯_τ v)`;
- **(comult backward)** for `v:vtx(h₁ τ)`, `w:vtx((h₁ τ)↓^∞ v)`:
  `h♯_τ(shift^∞(h₁ τ,v,w)) = h♯_τ(v) ⊕ h♯_{τ↓ h♯_τ v}(w)`.

**Counit.** `ĝ;ε_{𝔠_p}=ε_D`: forward is `T→1`; backward is
`ĝ♯_τ(o^∞_{ĝ₁ τ})=ĝ♯_τ(inl∗)=o_τ=ε_D♯_τ(∗)` — the base clause of `ĝ♯`. ∎

**Lemma U (comult forward).** *For all `τ` and `v:vtx(ĝ₁ τ)`,
`(ĝ₁ τ)↓^∞ v = ĝ₁(τ↓ ĝ♯_τ v)`.* By induction on the path `v`.

- `v=inl∗`: LHS `=(ĝ₁ τ)↓^∞ inl∗=ĝ₁ τ`; RHS `=ĝ₁(τ↓ o_τ)=ĝ₁ τ` by **D1**. ✓
- `v=inr(i,w)`: LHS `=(child(ĝ₁ τ,i))↓^∞ w=(ĝ₁ τ_i)↓^∞ w =_{IH} ĝ₁(τ_i↓ ĝ♯_{τ_i} w)`. And
  RHS `=ĝ₁(τ↓(g♯_τ i ⊕ ĝ♯_{τ_i} w)) =_{D4} ĝ₁((τ↓ g♯_τ i)↓ ĝ♯_{τ_i} w)=ĝ₁(τ_i↓ ĝ♯_{τ_i} w)`. ✓ (**D4**)

**Lemma S (comult backward).** *For all `τ`, `v:vtx(ĝ₁ τ)`, `w:vtx((ĝ₁ τ)↓^∞ v)`,
`ĝ♯_τ(shift^∞(ĝ₁ τ,v,w)) = ĝ♯_τ(v) ⊕ ĝ♯_{τ↓ ĝ♯_τ v}(U▸w)`,* where `U▸w` transports `w` along
Lemma U. By induction on `v`.

- `v=inl∗`: `shift^∞(ĝ₁ τ,inl∗,w)=w`, LHS `=ĝ♯_τ(w)`. RHS `=o_τ ⊕ ĝ♯_{τ↓ o_τ}(w')`; by **D1**
  `τ↓ o_τ=τ` and by **D2** `o_τ⊕(−)=(−)`, so RHS `=ĝ♯_τ(w)`. ✓
- `v=inr(i,w₀)`: `shift^∞(ĝ₁ τ,inr(i,w₀),w)=inr(i,shift^∞(ĝ₁ τ_i,w₀,w))`, so
  LHS `=g♯_τ(i)⊕ĝ♯_{τ_i}(shift^∞(ĝ₁ τ_i,w₀,w)) =_{IH} g♯_τ(i)⊕(ĝ♯_{τ_i}(w₀)⊕ĝ♯_{τ_i↓ĝ♯_{τ_i}w₀}(w''))`.
  Meanwhile RHS `=(g♯_τ(i)⊕ĝ♯_{τ_i}(w₀))⊕ĝ♯_{τ↓(g♯_τ i⊕ĝ♯_{τ_i}w₀)}(w'')`; the shape
  `τ↓(g♯_τ i⊕ĝ♯_{τ_i}w₀)=_{D4}τ_i↓ĝ♯_{τ_i}w₀` matches, and LHS `=` RHS by **D5**. ✓

Together with the counit clause, `ĝ` is a comonoid morphism. ∎

---

## 4. The couniversal triangle `ε_p ∘ U(ĝ) = g`

- **Forward.** `(U(ĝ);ε_p)₁(τ)=ε_{p,1}(ĝ₁ τ)=root(ĝ₁ τ)=g₁ τ`. (Definitional.)
- **Backward.** `(U(ĝ);ε_p)♯_τ=ĝ♯_τ∘ε_p♯_{ĝ₁ τ}`. For `i:P(g₁ τ)`,
  `ε_p♯_{ĝ₁ τ}(i)=inr(i,inl∗)`, and
  `ĝ♯_τ(inr(i,inl∗))=g♯_τ(i)⊕ĝ♯_{τ_i}(inl∗)=g♯_τ(i)⊕o_{τ_i} =_{D3} g♯_τ(i)`. ✓

So `ε_p∘U(ĝ)=g`. Fittingly, the triangle turns on **D3** — the "shift by the sub-shape's root is the
identity" law — exactly dual to the free triangle's use of the target monoid's *right* unit.

---

## 5. Uniqueness

Let `h:D⇒𝔠_p` be any comonoid morphism with `ε_p∘U(h)=g`. We show `h=ĝ`.

From the triangle backward for `h`: `h♯_τ(inr(i,inl∗))=g♯_τ(i)` for all `i:P(g₁ τ)`.  (★)

**Forward `h₁=ĝ₁` (coinduction / finality).** The triangle forward gives `root(h₁ τ)=g₁ τ`. The
comult-forward law for `h`, at `v=inr(i,inl∗)`, gives
`child(h₁ τ,i)=(h₁ τ)↓^∞ inr(i,inl∗)=h₁(τ↓ h♯_τ(inr(i,inl∗))) =_{(★)} h₁(τ↓ g♯_τ i)=h₁(τ_i)`.
Thus `h₁` is a morphism of `p`-coalgebras `(T,γ)→S^∞`. Since `S^∞` is the **final** coalgebra
(Spivak (249) / Lambek), the coalgebra morphism into it is unique, so `h₁=ĝ₁`. *(This is the one
genuinely coinductive step; everything else is finite induction.)*

**Backward `h♯=ĝ♯` (induction on the path).** With `h₁=ĝ₁`, induct on `v:vtx(ĝ₁ τ)`.

- `v=inl∗`: the counit law for `h` gives `h♯_τ(inl∗)=o_τ=ĝ♯_τ(inl∗)`.
- `v=inr(i,w)`: since `inr(i,w)=shift^∞(h₁ τ,inr(i,inl∗),w)`, the comult-backward law for `h` gives
  `h♯_τ(inr(i,w))=h♯_τ(inr(i,inl∗))⊕h♯_{τ↓ h♯_τ(inr(i,inl∗))}(w') =_{(★)} g♯_τ(i)⊕h♯_{τ_i}(w')
   =_{IH} g♯_τ(i)⊕ĝ♯_{τ_i}(w')=ĝ♯_τ(inr(i,w))`.

So `h=ĝ`. ∎

**Theorem (cofree couniversal property, in `Cont`).** For every container `p`, `ε_p:U(𝔠_p)⇒p` is
couniversal from `U` to `p`: for every comonoid `D` and morphism `g:U(D)⇒p` there is a unique
comonoid morphism `ĝ:D⇒𝔠_p` with `ε_p∘U(ĝ)=g`. Equivalently `𝔠:p↦𝔠_p` is right adjoint to
`U:Comon(Cont)→Cont`, with counit `ε`. ∎

Naturality of `Comon(Cont)(D,𝔠_p)≅Cont(U D,p)` in both variables is the standard consequence: for a
comonoid morphism `k:D'⇒D`, both `k;ĝ` and the map induced by `U(k);g` are comonoid morphisms
`D'⇒𝔠_p` cofactoring `U(k);g` through `ε_p`, hence equal by uniqueness; naturality in `p` follows
because `ĝ` is defined by corecursion natural in `g`.

---

## 6. The structural mirror (free ↔ cofree)

Every step of the argument is the coordinate dual of the free-monad universal property
(`2026-07-24-free-monad-universal-property.md`). The dictionary:

| piece                    | free — target monoid `M`               | cofree — source comonoid `D`            |
|--------------------------|----------------------------------------|-----------------------------------------|
| carrier shapes           | `S*` = W-type (finite trees)           | `S^∞` = M-type (infinite trees)         |
| carrier positions        | leaves (finite)                        | **vertices** (finite rooted paths)      |
| induced map, forward     | `ĝ₁` by W-**recursion**                 | `ĝ₁` by M-**corecursion** (anamorphism) |
| induced map, backward    | `ĝ♯` via `μ_M♯` split                    | `ĝ♯` via `⊕` (path recursion)           |
| morphism-law forward     | M-LUNIT (base) + M-ASSOC (step)        | **D1** (base) + **D4** (step)           |
| morphism-law backward    | M-LUNIT-bwd + M-ASSOC-bwd              | **D2** (base) + **D5** (step)           |
| triangle                 | M-RUNIT                                 | **D3**                                   |
| uniqueness forward       | tree **induction**                     | tree **coinduction** (finality)         |
| uniqueness backward      | tree ind. + bijectivity of `split`     | path induction + comult-backward of `h` |

The single asymmetry — induction becomes coinduction only in the *shape* layer, while the *position*
layer stays inductive on both sides — is exactly the free/cofree = W-type/M-type, leaves/vertices
duality. It is what makes the couniversal property reduce cleanly to `D`'s five laws.

---

## 7. `⟦−⟧` sends `𝔠_p` to the cofree comonad (the endofunctor corollary)

`⟦−⟧:(Cont,◁,y)→([Set,Set],∘,Id)` is **strong monoidal** (`Composition.lean`,
`⟦G◁F⟧≅⟦G⟧∘⟦F⟧`, `⟦y⟧≅Id`; Lean-verified) and **fully faithful** (Abbott–Altenkirch–Ghani
representation theorem). It also **preserves connected limits** (wide pullbacks + cofiltered limits;
Gambino–Kock §1.18; my Ch. 3 `which-functors-are-containers`, and memory
`containers-preserve-connected-not-empty`).

**The carrier, directly.** By the vertex count of §1,

```
⟦𝔠_p⟧(A) = Σ_{s:S^∞}(P^∞(s)→A) = Σ_{t:tree_p}(vtx(t)→A) ≅ νZ.(A×⟦p⟧Z):
```

an element of `νZ.(A×⟦p⟧Z)` is coinductively `(a:A, (s:S, children:P s→Z))` — a `p`-branching tree
carrying an `A`-label at **every** node — i.e. a `p`-tree `t` together with a labelling
`vtx(t)→A`. This is exactly the standard cofree-comonad formula `C_H(A)=νZ.(A×H Z)` for `H=⟦p⟧`
(again: labels at all **vertices**, not leaves). Since the cofree comonad on an accessible
endofunctor exists and is unique (it is a right adjoint; `⟦p⟧` is accessible), `⟦𝔠_p⟧` **is** the
cofree comonad on `⟦p⟧`, and the comonad structure `⟦−⟧` transports from the comonoid `𝔠_p`
(read-root counit, canonical comultiplication) is the cofree one. Hence `⟦𝔠_p⟧` is couniversal
against **every** comonad on `[Set,Set]`, not only the polynomial ones.

**The tower, as a cross-check.** Independently, the cofree tower `𝔠_p=lim(⋯→p_{n+1}→p_n→⋯→p₀)`
(Spivak (245)) is an **ω^op-limit** — cofiltered, hence **connected** — so `⟦−⟧` preserves it:
`⟦𝔠_p⟧≅lim ⟦p_n⟧`, with `⟦p_{k+1}⟧=⟦(p◁p_k)×y⟧≅(⟦p⟧∘⟦p_k⟧)×Id` (strong monoidality `◁↦∘`, `y↦Id`,
and `⟦A×B⟧≅⟦A⟧×⟦B⟧` pointwise). This is the final sequence of `Φ(Z)=Id×(⟦p⟧∘Z)`, whose limit is
`νΦ=` the cofree comonad — recovering the same identification. ∎

---

## 8. Verification

_(computational, `scratch/cofree_up_verify.py` — filled after the run in §8.1)_

### 8.1 Results

Model: base container `p` with `S={a,b}`, `P(a)={0,1}`, `P(b)={0}`; source comonoid `D` = the
**walking-arrow category** (objects `X,Y`; arrows `id_X, id_Y, f:X→Y`, so `Q(X)={id_X,f}`,
`Q(Y)={id_Y}`, `X↓f=Y`); morphism `g` with `g₁(X)=a`, `g₁(Y)=b`, and the nontrivial backward
`g♯_X(0)=id_X`, `g♯_X(1)=f`, `g♯_Y(0)=id_Y`. Trees built to depth 5, vertices/paths enumerated to
length 4. **All positive checks PASS; all negative controls fire; exit 0.**

| check | what | cases | result |
|-------|------|-------|--------|
| 1 | `D`-laws D1–D5 (sanity gate) | 17 | PASS |
| 2 | corecursion of `ĝ₁` (`root`, `child`) | 5 | PASS |
| 3 | triangle `ε_p∘U(ĝ)=g` (fwd+bwd) | 5 | PASS |
| 4 | **Lemma U** (comult forward) | 20 | PASS |
| 5 | **Lemma S** (comult backward) | 70 | PASS |
| 6a | comonoid-morphism law, forward (trees) | 22 | PASS |
| 6b | comonoid-morphism law, backward (positions) | 70 | PASS |
| 7 | counit compatibility `ĝ♯_τ(inl∗)=o_τ` | 2 | PASS |
| 8 | uniqueness (determinacy of `ĝ♯` at each vertex) | 20 | PASS |

Check 6 is **independent** of 4/5: it assembles the composite morphisms `δ_D;(ĝ◁ĝ)` and `ĝ;δ_{𝔠_p}`
from generic `◁`-on-morphisms combinators and compares them, rather than reusing the Lemma U/S
formulas — and reproduces exactly the same equalities (6a = Lemma U, 6b = Lemma S), confirming the
unpacking of the comultiplication morphism law in §3. Check 8 confirms that `(c0)` the counit clause,
`(c1)` triangle-backward `h♯_τ(inr(i,inl∗))=g♯_τ(i)`, and `(cS)` the depth-1 instance of the
comult-backward law together **uniquely force** `h♯_τ` at every vertex — the finite content of §5's
backward induction.

**Negative controls (all fire, mismatch count > 0).**
- **N1** corrupt `D`'s shift (swap argument order): Lemma S → 37 mismatches; comonoid-bwd → 34.
- **N2** corrupt `ε_p♯` (`inl∗` instead of `inr(i,inl∗)`): triangle-bwd → 1 mismatch.
- **N3** corrupt the corecursion (`child i = ĝ₁ τ` instead of `ĝ₁ τ_i`): corecursion check → 1,
  Lemma U → 26 mismatches.

So each of the load-bearing steps — the shift (D5/D2 in the backward layer), the counit's depth-1
target (D3 in the triangle), and the subtree-unfolding corecursion (D1/D4 in the forward layer) —
has computational teeth: corrupting it breaks precisely the check it underwrites.

### 8.2 Boundary cases

- **`v=inl∗` / `τ↓o_τ`** (base of every path induction) is `D`'s counit/unit laws (D1, D2) exactly.
- **`i` with `P(root)=∅`** (childless node): `vtx=1` (root only), `ĝ♯` is the constant `o`, and every
  induction step is vacuous — the trees can still be infinite in depth if some reachable shape has
  positions, but a shape `s` with `P s=∅` terminates that branch.
- **`S=∅`**: `tree_p=∅` (no root shape), `𝔠_p≅` the terminal comonoid, and `ĝ` is forced — the
  adjunction degenerates correctly, dual to the free `S=∅ ⟹ m_X≅I` case.
- **`D=y`** (terminal-ish source, single trivial position): `ĝ₁ τ` is the tree that reads `g₁τ` at
  the root and unfolds along the unique positions; `ĝ♯` picks out the root at every step.

---

## 9. Gaps and honest scope

1. **The construction and the theorem are prior art** (Niu–Spivak Prop. 8.18/8.33/Thm. 8.45; Spivak
   2202.00534 (244)–(249), direct-read). The contribution is the container-coordinate proof of the
   couniversal property — `ε_p`, `ĝ` by corecursion, and the inductive/coinductive discharge of the
   morphism law, triangle and uniqueness against a *given* comonoid `D`. Graded **proved**.
2. **Finality is used twice** — for existence of `ĝ₁` (anamorphism) and for uniqueness-forward. It is
   the only genuinely coinductive ingredient; it is cited (Spivak (249), Lambek; Barr, *Terminal
   coalgebras*). All morphism-law and triangle computations, and uniqueness-backward, are **finite
   induction on the path**, valid in any category with the relevant W-/M-types.
3. **Transports.** Lemma S and uniqueness-backward carry a transport of the residual path `w` along
   Lemma U (the `vtx((ĝ₁ τ)↓^∞ v)=vtx(ĝ₁(τ↓ĝ♯_τ v))` identification), the dual of the free proof's
   `split`-identifications and of `Directed.lean`'s D5 transport. They are handled honestly above and
   would be the explicit `▸` casts in a Lean port.
4. **§7's "against all comonads"** rests on Abbott–Altenkirch–Ghani full-faithfulness (standard),
   `⟦−⟧`-connected-limit-preservation (Ch. 3), and accessibility of `⟦p⟧` (cofree comonad exists).
   Part 1 (the theorem in `Cont`) does **not** depend on these.
5. **Not yet Lean.** The corecursion `ĝ₁` and the finality steps need coinduction/M-types, absent
   from Lean 4 core; this is the infra block noted in PROVE.md (awaiting Neil's Mathlib decision).
   The *backward/position* layer (Lemmas U, S, triangle, uniqueness-backward) is finite induction and
   *is* portable now — a natural partial LEAN target dual to `FreeUniversal.lean`.

### References
- D. I. Spivak, *A reference for categorical structures on `Poly`*, arXiv:2202.00534, Eq. (244)–(249).
- N. Niu, D. I. Spivak, *Polynomial Functors: A Mathematical Theory of Interaction*, Prop. 8.18, 8.33, Thm. 8.45.
- D. Ahman, J. Chapman, T. Uustalu, *When is a container a comonad?*, FoSSaCS 2012 / LMCS 2014.
- M. Abbott, T. Altenkirch, N. Ghani, *Containers: constructing strictly positive types*, TCS 342 (2005).
- M. Barr, *Terminal coalgebras in well-founded set theory*, TCS 114 (1993).
- MacBeth, *The universal property of the free monad on a container* (`2026-07-24-free-monad-universal-property.md`).
