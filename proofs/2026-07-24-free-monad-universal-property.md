# The universal property of the free monad on a container

**MacBeth — 2026-07-24**

## Provenance and what is (and is not) claimed

The **construction** of the free monad on a polynomial endofunctor — positions = trees,
directions = leaves, multiplication = grafting — and its **universal property** (that it is the
value of the left adjoint to the forgetful functor from polynomial monads) are **prior art**:

> **Gambino–Kock, "Polynomial functors and polynomial monads", arXiv:0906.4931, Theorem 4.5
> (2009):** the free monad on a polynomial endofunctor is a polynomial monad, in any locally
> cartesian closed category with W-types; it is the free such via the initial-algebra universal
> property. Single-variable case: Gambino–Hyland, TYPES 2003. Container W-type technology:
> Abbott–Altenkirch–Ghani, ICALP 2004 / TCS 2005.

**This note does not claim the theorem.** It supplies the **container-coordinate proof** of the
universal property that the grafting-laws companion (`2026-07-16-free-monad-grafting-laws.md`, §6
gap #3) explicitly left open: the insertion of generators `α`, the induced monoid morphism `ĝ` by
W-type recursion, and machine-legible proofs — by structural induction on the tree — that `ĝ` is a
monoid morphism, that the adjunction triangle holds, and that `ĝ` is unique. The carrier and the
three `◁`-monoid laws of `m_X` are **already Lean-verified** (`Free.lean`,
`Container.freeMonoid`, `Quot.sound`-only) and are **cited, not re-proved**.

The one structural observation worth stating up front: the universal property of `m_X` reduces —
*by induction on the tree* — to the monoid laws **of the target monoid `M`**. The base case is
`M`'s unit law; the inductive step is `M`'s associativity. This is the exact mirror of how the
free monoid's *own* laws reduced (in the companion note) to grafting associativity: there the
induction discharged `m`'s laws using tree combinatorics; here it discharges the *morphism* law
using `M`'s laws. No law of `M` is proved — `M` is a given monoid and its laws are applied.

Computational confirmation: `scratch/free_monad_up_verify.py` (three independent target monoids,
including two non-free ones with non-trivial position maps; triangle, both morphism-law components,
and uniqueness all checked).

---

## 1. Coordinates

I use the conventions of the companion note and `Composition.lean`. A **container** `X=(S◁P)` has
shapes `S` and positions `P:S→Set`; `⟦S◁P⟧(A)=Σ_{s:S}(P s→A)`. A **morphism** `φ:(A◁P_A)⇒(B◁P_B)`
is a forward shape map `φ₁:A→B` and a **backward** family `φ♯_a:P_B(φ₁ a)→P_A(a)`. Composition
(`;` = apply-first-left): `(φ;ψ)₁=ψ₁∘φ₁`, `(φ;ψ)♯_a=φ♯_a∘ψ♯_{φ₁ a}`. The composition product and
its tensor of morphisms are

```
(G◁F).Shape = Σ_{t:T}(Q t→S),         (G◁F).Pos(t,f) = Σ_{q:Q t} P(f q),      ⟦G◁F⟧=⟦G⟧∘⟦F⟧,
(φ◁ψ)₁(a,g)       = (φ₁ a, ψ₁∘g∘φ♯_a),
(φ◁ψ)♯_{(a,g)}(j,k) = (φ♯_a j, ψ♯_{g(φ♯_a j)} k),
```

with unit `I=(1◁λ_.1)`. The unitors/associator are `λ_F(*,g)=g(*)`, `ρ_F(s,g)=s`,
`a((h,g),k)=(h, u↦(g u, v↦k(u,v)))` on shapes and `(*,p)`, `(p,*)`, `((u,v),p)` backward. A
**monoid** `(C,e,μ)` in `(Cont,◁,I)` has `e:I⇒C`, `μ:C◁C⇒C` satisfying `(e◁C);μ=λ_C`,
`(C◁e);μ=ρ_C`, `(μ◁C);μ=a;(C◁μ);μ`. Its extension `⟦C⟧` is a monad. Write `Mon(Cont)` for the
category of such monoids and `U:Mon(Cont)→Cont` for the forgetful functor.

### The free carrier (companion §2, Lean-verified)

For `X=(S◁P)`, `m=m_X=(S*◁P*)` where `S*` is the set of closed `P`-trees
`t ::= lf ∣ nd s κ` (`s:S`, `κ:P s→S*`) and `P* t = leaves(t)` with `leaves(lf)=1`,
`leaves(nd s κ)=Σ_{p:P s} leaves(κ p)`. Its monoid structure is `e₁(*)=lf`, `e♯=id`;
`μ₁(t,u)=graft(t,u)`, `μ♯=split`, where

```
graft(lf,u)=u(()),   graft(nd s κ,u)=nd s(λp.graft(κ_p,u_p)),   u_p:=λr.u⟨p,r⟩,
split_{lf,_}(w)=⟨(),w⟩,   split_{nd s κ,u}⟨p,z⟩=⟨⟨p,(split_{κ_p,u_p}z).1⟩,(split_{κ_p,u_p}z).2⟩.
```

**Lemma A (companion §3, cited).** `split_{t,u}` is a bijection
`leaves(graft(t,u))≅Σ_{ℓ:leaves t}leaves(u_ℓ)`, with inverse path concatenation `cat_{t,u}`; it
cuts a leaf-path at its unique `t`-leaf prefix. In particular `cat` and `split` are mutually
inverse, and at a single node `cat_{nd s(λp.lf),w}(⟨p,()⟩,x)=⟨p,x⟩`. `[proved; companion §3]`

**The three `◁`-monoid laws of `(m,μ,e)`** are Lean-verified (`Container.freeMonoid`); we cite
them but never re-derive them. `[lean-verified; Free.lean]`

---

## 2. Insertion of generators

Define `α = α_X : X ⇒ U(m_X)` by
```
α₁ s = nd s (λp. lf),        α♯_s : leaves(α₁ s) = Σ_{p:P s} 1 → P s,   α♯_s⟨p,()⟩ = p.
```
`α₁ s` is a single node of shape `s` whose children are all leaves; `α♯_s` is the canonical
bijection `leaves(α₁ s)≅P s`. This is the unit of the intended adjunction.

---

## 3. The induced monoid morphism

Fix a monoid `M=(T◁Q, e_M, μ_M)` and a container morphism `g:X⇒U(M)` (so `g₁:S→T`,
`g♯_s:Q(g₁ s)→P s`). Write `ε := e_M₁(*)`. Define `ĝ:m⇒M` by well-founded recursion on the tree.

**Forward** `ĝ₁:S*→T`:
```
ĝ₁(lf)     = ε,
ĝ₁(nd s κ) = μ_M₁( g₁ s,  λq:Q(g₁ s). ĝ₁(κ(g♯_s q)) ).
```
(The recursive calls are on structural subtrees `κ(g♯_s q)`, so this terminates.)

**Backward** `ĝ♯_t:Q(ĝ₁ t)→leaves(t)`:
```
ĝ♯_lf         = the unique map Q(ε)→1,
ĝ♯_{nd s κ}(r) = ⟨ g♯_s q,  ĝ♯_{κ(g♯_s q)}(ρ) ⟩,   (q,ρ) := μ_M♯_{(g₁ s, λq.ĝ₁(κ(g♯_s q)))}(r).   (†)
```
Reading (†): a target position `r` of the node is split by `μ_M`'s backward map into an
`M`-position `q` of the head `g₁ s` and a residual `ρ` in the `q`-th subtree image; `q` names a
container position `g♯_s q:P s`, and `ρ` recurses into the corresponding subtree.

Throughout write `a₀:=g₁ s` and `b₀:=λq.ĝ₁(κ(g♯_s q))`, so `ĝ₁(nd s κ)=μ_M₁(a₀,b₀)`.

---

## 4. `ĝ` is a monoid morphism

A morphism `h:m⇒M` is a monoid morphism iff (unit) `e;h=e_M` and (mult) `μ;h=(h◁h);μ_M`. In
coordinates these unpack to:

- **UNIT.** Forward: `h₁(lf)=ε`. Backward: automatic (both composites are maps into `1`).
- **MULT (forward).** `h₁(graft(t,u)) = μ_M₁( h₁ t, λq. h₁(u(h♯_t q)) )`.
- **MULT (backward).** For `r:Q(h₁ graft(t,u))` (identified with `Q(μ_M₁(h₁t,…))` via MULT-fwd),
  `split_{t,u}(h♯_{graft t u} r) = ⟨ h♯_t q, h♯_{u(h♯_t q)}(r') ⟩`,
  `(q,r'):=μ_M♯_{(h₁ t, λq.h₁(u(h♯_t q)))}(r)`.

**UNIT** for `ĝ` is immediate: `ĝ₁(lf)=ε`, and the backward component is forced by terminality of
`1`. It remains to prove MULT (both components) for `ĝ`. We prove both by a single induction on the
tree `t`; the base case is `M`'s **left-unit** law and the inductive step is `M`'s
**associativity**, each used in both its forward and backward component.

### 4.1 Two coordinate readings of `M`'s laws

We record `M`'s laws as coordinate equations, obtained by unpacking the morphism equations of §1
exactly as the companion note unpacked the free monoid's laws.

**(M-LUNIT).** From `(e_M◁M);μ_M=λ_M`, at a shape `(*,g)` of `I◁M` with `c:=g(*)`:
```
forward:   μ_M₁(ε, λq.c) = c              (μ of the unit with a constant family is the identity),
backward:  snd( μ_M♯_{(ε,λq.c)}(r) ) = r  (r:Q(c), modulo the forward identification).
```

**(M-RUNIT).** From `(M◁e_M);μ_M=ρ_M`, at `(a,h)` of `M◁I`:
```
forward:   μ_M₁(a, λq.ε) = a,
backward:  fst( μ_M♯_{(a,λq.ε)}(r) ) = r   (r:Q(a)).
```

**(M-ASSOC).** From `(μ_M◁M);μ_M=a;(M◁μ_M);μ_M`, at a shape `((a,b),C)` of `(M◁M)◁M`
(`C:Σ_{q:Q a}Q(b q)→T`):
```
forward:   μ_M₁( μ_M₁(a,b), λz.C(μ_M♯_{(a,b)} z) ) = μ_M₁( a, λq.μ_M₁(b q, λq'.C⟨q,q'⟩) ),
backward:  the two backward composites of the square agree, i.e. with
             (z̄,x)=μ_M♯_{(μ_M₁(a,b),C∘μ_M♯)}(r),  (q,q')=μ_M♯_{(a,b)}(z̄)        ⟹ ((q,q'),x),
             (q,y)=μ_M♯_{(a,λq.μ_M₁(b q,…))}(r),   (q',x')=μ_M♯_{(b q,…)}(y)      ⟹ ((q,q'),x'),
           we have x=x' (and the q,q' agree), as elements of Σ_{q}Σ_{q'}Q(C⟨q,q'⟩).
```

These are hypotheses, not obligations: `M` is a monoid, so they hold.

### 4.2 MULT forward, by induction on `t`

**Base `t=lf`.** `graft(lf,u)=u(())`, so LHS `=ĝ₁(u())`. On the right `ĝ♯_lf` is constant `()`, so
`λq.ĝ₁(u(ĝ♯_lf q))=λq.ĝ₁(u())` is the constant family `c:=ĝ₁(u())`, and RHS `=μ_M₁(ε,λq.c)=c` by
**(M-LUNIT) forward**. So LHS = RHS. ∎(base)

**Step `t=nd s κ`.** With `a₀=g₁ s`, `b₀=λq.ĝ₁(κ(g♯_s q))`:
```
LHS = ĝ₁(graft(nd s κ,u)) = ĝ₁(nd s(λp.graft(κ_p,u_p)))
    = μ_M₁(a₀, λq. ĝ₁(graft(κ(g♯_s q), u_{g♯_s q})))
    =(IH)  μ_M₁(a₀, λq. μ_M₁( ĝ₁(κ(g♯_s q)), λq'. ĝ₁(u_{g♯_s q}(ĝ♯_{κ(g♯_s q)} q')) )).
```
For the right, `ĝ₁(nd s κ)=μ_M₁(a₀,b₀)`, and using (†),
`u(ĝ♯_{nd s κ} q̃)=u_{g♯_s q}(ĝ♯_{κ(g♯_s q)} q')` where `(q,q')=μ_M♯_{(a₀,b₀)}(q̃)`. Put
`C⟨q,q'⟩:=ĝ₁(u_{g♯_s q}(ĝ♯_{κ(g♯_s q)} q'))`. Then
```
RHS = μ_M₁( μ_M₁(a₀,b₀), λq̃. C(μ_M♯_{(a₀,b₀)} q̃) )
    =(M-ASSOC fwd)  μ_M₁( a₀, λq. μ_M₁(b₀ q, λq'.C⟨q,q'⟩) )  =  LHS,
```
since `b₀ q=ĝ₁(κ(g♯_s q))` and `λq'.C⟨q,q'⟩=λq'.ĝ₁(u_{g♯_s q}(ĝ♯_{κ(g♯_s q)} q'))`. ∎(step)

### 4.3 MULT backward, by induction on `t`

**Base `t=lf`.** `c:=ĝ₁(u())`, `r:Q(c)`. LHS `=split_{lf,u}(ĝ♯_{u()} r)=⟨(),ĝ♯_{u()} r⟩`. For RHS,
`(q,r')=μ_M♯_{(ε,λq.c)}(r)`, `ĝ♯_lf q=()`, so RHS `=⟨(),ĝ♯_{u()} r'⟩`. **(M-LUNIT) backward** gives
`r'=r`, hence LHS = RHS. ∎(base)

**Step `t=nd s κ`.** Set `b₁:=λq.ĝ₁(graft(κ(g♯_s q),u_{g♯_s q}))`, so
`ĝ₁(graft(nd s κ,u))=μ_M₁(a₀,b₁)`, and `B:=λq̃.ĝ₁(u(ĝ♯_{nd s κ} q̃))`. With
`C⟨q,q'⟩=ĝ₁(u_{g♯_s q}(ĝ♯_{κ(g♯_s q)} q'))` as in §4.2:

*Glue facts.* By **MULT forward** on the subtree (the forward IH),
`μ_M₁(b₀ q, λq'.C⟨q,q'⟩)=ĝ₁(graft(κ(g♯_s q),u_{g♯_s q}))=b₁ q`; and by (†),
`C∘μ_M♯_{(a₀,b₀)}=B`. So **(M-ASSOC)** instantiated at `((a₀,b₀),C)` is precisely the shape
identity `μ_M₁(μ_M₁(a₀,b₀),B)=μ_M₁(a₀,b₁)` — the two trees over which `r` is split — and its
**backward** clause reads
```
  RHS-way:  (q̂,r'')=μ_M♯_{(μ_M₁(a₀,b₀),B)}(r); (q,ρ)=μ_M♯_{(a₀,b₀)}(q̂)       ⟹ ((q,ρ),r''),
  LHS-way:  (q₁,ρ₁)=μ_M♯_{(a₀,b₁)}(r);         (q',ρ')=μ_M♯_{(b₀ q₁,β)}(ρ₁)   ⟹ ((q₁,q'),ρ'),
```
so `q=q₁`, `ρ=q'`, `r''=ρ'`.   (Here `β:=λq'.C⟨q₁,q'⟩`.)

*Compute.* Writing `p₁:=g♯_s q₁`, `z₂:=ĝ♯_{graft(κ_{p₁},u_{p₁})}(ρ₁)`, the grafted node's backward
map (†) gives `ĝ♯_{graft(nd s κ,u)}(r)=⟨p₁,z₂⟩`, and the `nd`-clause of `split` followed by the
**backward IH** on `(κ_{p₁},u_{p₁},ρ₁)` gives
```
LHS = split_{nd s κ,u}⟨p₁,z₂⟩ = ⟨⟨p₁, ĝ♯_{κ_{p₁}}(q')⟩, ĝ♯_{u_{p₁}(ĝ♯_{κ_{p₁}} q')}(ρ')⟩.
```
By (†) and `u∘⟨·,·⟩=u_{·}(·)`,
```
RHS = ⟨ĝ♯_{nd s κ}(q̂), ĝ♯_{u(ĝ♯_{nd s κ} q̂)}(r'')⟩
    = ⟨⟨g♯_s q, ĝ♯_{κ(g♯_s q)}(ρ)⟩, ĝ♯_{u_{g♯_s q}(ĝ♯_{κ(g♯_s q)} ρ)}(r'')⟩.
```
By the glue facts `q=q₁`, `ρ=q'`, `r''=ρ'`: `p₁=g♯_s q`, the outer leaves coincide, and the inner
positions reduce to `ρ'=r''`. Hence LHS = RHS. ∎(step)

**Conclusion.** `ĝ` satisfies UNIT and MULT in both components, so it is a morphism of monoids.

---

## 5. The triangle `α;ĝ = g`

**Forward.** `(α;ĝ)₁ s = ĝ₁(nd s(λp.lf)) = μ_M₁(g₁ s, λq.ĝ₁(lf)) = μ_M₁(g₁ s, λq.ε) = g₁ s` by
**(M-RUNIT) forward**.

**Backward.** `(α;ĝ)♯_s = α♯_s∘ĝ♯_{nd s(λp.lf)}`. For `r:Q(g₁ s)`,
`ĝ♯_{nd s(λp.lf)}(r)=⟨g♯_s q, ĝ♯_{lf}(ρ)⟩=⟨g♯_s q, ()⟩` with `(q,ρ)=μ_M♯_{(g₁ s,λq.ε)}(r)`, so
`α♯_s⟨g♯_s q,()⟩=g♯_s q`. **(M-RUNIT) backward** gives `q=r`, hence `(α;ĝ)♯_s(r)=g♯_s r`.

So `α;ĝ=g`. (The triangle uses `M`'s **right** unit law — fittingly: `α` places the generator at
the root with leaf children, the right-unit configuration.)

---

## 6. Uniqueness

Let `h:m⇒M` be any monoid morphism with `α;h=g`. We show `h=ĝ` by induction on `t`, using the
**node-as-graft** identity
```
nd s κ = graft(α₁ s, w),     w⟨p,()⟩ := κ p
```
(check: `graft(nd s(λp.lf),w)=nd s(λp.graft(lf,w_p))=nd s(λp.κ p)=nd s κ`).

**Forward.** `t=lf`: UNIT gives `h₁(lf)=ε=ĝ₁(lf)`. `t=nd s κ`: by **MULT forward** for `h`,
```
h₁(nd s κ)=h₁(graft(α₁ s,w)) = μ_M₁( h₁(α₁ s), λq. h₁(w(h♯_{α₁ s} q)) ).
```
The triangle forward gives `h₁(α₁ s)=g₁ s`; the triangle backward gives
`α♯_s(h♯_{α₁ s} q)=g♯_s q`, and since every element of `leaves(α₁ s)` is `⟨p̃,()⟩` with
`α♯_s⟨p̃,()⟩=p̃`, this forces `h♯_{α₁ s} q=⟨g♯_s q,()⟩`, whence `w(h♯_{α₁ s} q)=κ(g♯_s q)`. So
`h₁(nd s κ)=μ_M₁(g₁ s, λq.h₁(κ(g♯_s q)))=μ_M₁(g₁ s,λq.ĝ₁(κ(g♯_s q)))=ĝ₁(nd s κ)` by the IH.

**Backward.** `t=lf`: `h♯_lf:Q(ε)→1` is the unique map `=ĝ♯_lf`. `t=nd s κ`: **MULT backward** for
`h` at `(α₁ s,w)` reads `split_{α₁ s,w}(h♯_{nd s κ} r)=⟨h♯_{α₁ s} q, h♯_{w(h♯_{α₁ s}q)}(r')⟩` with
`(q,r')=μ_M♯_{(g₁ s,b₀)}(r)` (the families identified by the triangle and the forward step). Since
`split` is a bijection (Lemma A) we invert:
```
h♯_{nd s κ}(r) = cat_{α₁ s,w}( ⟨h♯_{α₁ s} q, h♯_{κ(g♯_s q)}(r')⟩ ) = cat_{α₁ s,w}(⟨⟨g♯_s q,()⟩, ĝ♯_{κ(g♯_s q)}(r')⟩),
```
using `h♯_{α₁ s} q=⟨g♯_s q,()⟩` and the backward IH `h♯_{κ(g♯_s q)}=ĝ♯_{κ(g♯_s q)}`. The single-node
concatenation `cat_{nd s(λp.lf),w}(⟨p,()⟩,x)=⟨p,x⟩` (Lemma A) gives
`h♯_{nd s κ}(r)=⟨g♯_s q, ĝ♯_{κ(g♯_s q)}(r')⟩=ĝ♯_{nd s κ}(r)` by (†).

So `h=ĝ`. The **bijectivity of `split`** (Lemma A) is exactly what makes the backward map forced —
the same uniqueness that forced `μ♯` in the companion note.

**Theorem A.** For every container `X`, `α_X:X⇒U(m_X)` is universal from `X` to `U`: for every
monoid `M` and morphism `g:X⇒U(M)` there is a unique monoid morphism `ĝ:m_X⇒M` with `U(ĝ)∘α_X=g`.
Equivalently `F:X↦m_X` is left adjoint to `U:Mon(Cont)→Cont`, with unit `α`. ∎

The naturality of the bijection `Mon(Cont)(m_X,M)≅Cont(X,U M)` in both variables is the standard
consequence: given `ĝ` for `g` and any monoid morphism `k:M⇒N`, both `ĝ;k` and the `ĝ` induced by
`g;U(k)` are monoid morphisms `m_X⇒N` extending `g;U(k)` along `α`, hence equal by uniqueness; and
`α`-precomposition is natural in `X` since `ĝ` is defined by recursion natural in `g`.

---

## 7. `⟦−⟧` preserves the free monad (the endofunctor corollary)

`⟦−⟧:(Cont,◁,I)→([Set,Set],∘,Id)` is **strong monoidal** — the coherence isos
`⟦G◁F⟧≅⟦G⟧∘⟦F⟧` and `⟦I⟧≅Id` are established and Lean-verified in the corpus
(`Composition.lean`, `⟦G◁F⟧=⟦G⟧∘⟦F⟧`) — and **fully faithful**: container morphisms are exactly
natural transformations of the represented polynomial functors (Abbott–Altenkirch–Ghani
representation theorem). A strong monoidal functor sends monoids to monoids and monoid morphisms to
monoid morphisms; combined with full faithfulness this yields, for every monoid `M`,
```
Mon(Cont)(m_X, M) ≅ Monad(⟦m_X⟧, ⟦M⟧),        Cont(X, U M) ≅ Nat(⟦X⟧, |⟦M⟧|),
```
naturally in `M`. Transporting Theorem A's bijection along these isos gives
`Monad(⟦m_X⟧, ⟦M⟧) ≅ Nat(⟦X⟧, |⟦M⟧|)` natural in `M`: **`⟦m_X⟧` has the free-monad universal
property against every polynomial monad `⟦M⟧`.**

To upgrade "against every polynomial monad" to "against every monad", cite **Gambino–Kock 4.5**:
the free monad on the polynomial functor `⟦X⟧` exists (its carrier is the initial algebra of
`A↦A+⟦X⟧A`, i.e. the tree functor), is itself polynomial, and equals `⟦m_X⟧` on the nose (positions
= trees, directions = leaves). Freeness being a universal property, and the free monad being unique
when it exists, `⟦m_X⟧` **is** the free monad on `⟦X⟧` in `[Set,Set]`. Concretely
`⟦m_X⟧(A)=Σ_{t:S*}(leaves(t)→A)` is exactly the initial algebra `μY.(A+⟦X⟧(Y))` — trees with
`A`-labelled leaves — the standard free-monad formula `F*(A)=μY.(A+F Y)` with `F=⟦X⟧`. ∎

---

## 8. Verification

**Computational** (`scratch/free_monad_up_verify.py`). Three target monoids, chosen to exercise
the non-trivial parts:
- **Writer** `(N◁1)`, `N=ℤ/3` (all positions singletons — isolates the forward laws);
- **Reader** `(1◁E)`, `E={0,1}` (one shape, non-trivial backward `μ_M♯(e)=(e,e)` — stresses
  MULT-backward and the M-ASSOC-backward step);
- **Free target** `m_Y` for a small `Y` (both components non-trivial — a non-degenerate test of the
  whole construction, and *not* a mirror of the source since `Y≠X`).

For each, with a chosen `g:X⇒U(M)` (non-trivial `g♯` where positions allow), the script checks the
triangle `α;ĝ=g`, the UNIT law, and **both components** of the MULT law over all `(t,u)` with `t`
up to 3 internal nodes and a battery of leaf-labellings `u`; and, for the two finite monoids, that
`ĝ₁` on trees of depth ≤2 is the **unique** map satisfying `f(lf)=ε` and the node recursion (a
finite brute-force over all `f` into `T`).

**Results (all PASS, exit 0).** Triangle, UNIT, MULT (both components) pass for all three targets;
uniqueness passes for Writer and Reader (n/a for the infinite free target). The four monoidal
operations were built generically from the coordinate conventions, and the `◁`-monoid laws of
`m_X` and of all three targets were re-checked as a sanity gate. MULT was verified over **306**
`(t,u)` pairs (exhaustive: `t` over closed trees with ≤3 internal nodes, `u` over all depth-≤1
labellings; forward shape equality **and** backward equality at every target position). The script
independently reports that triangle-forward holds *precisely by `M`'s right-unit law* and
triangle-backward by its backward component — matching §5. **Negative controls fire**: corrupting
`μ_M` breaks triangle/MULT-forward; corrupting only the standalone `μ_M♯` on the right factor of
the MULT square produces 101 backward mismatches for Reader (e.g. shape `(lf, (nd x{lf,lf}))`,
position `1`: `((),(0,))` vs `((),(1,))`) — so the backward check has teeth and is not a mirror.

**Boundary cases.** `lf` (base of both inductions) = `M`'s unit laws exactly. Shapes `s` with
`P s=∅` give childless nodes `nd s κ` (`κ:∅→S*`) with `leaves=∅`: `ĝ₁(nd s κ)=μ_M₁(g₁ s, !_∅)`,
`ĝ♯` the empty map — the enumeration includes these and they pass. `X` with `S=∅`: `S*=` closed
trees over no shapes `={lf}`, `m_X≅I`, `α` is the unique `∅⇒I`, and `ĝ` is forced to be `e_M` — the
adjunction degenerates correctly.

**Cross-check with the companion.** The forward/backward split calculus (Lemma A, the `cat`/`split`
inverse pair, the flat-concatenation bookkeeping) is imported verbatim from
`2026-07-16-free-monad-grafting-laws.md`; the induction here has the *same shape* as that note's
law-inductions, with `M`'s laws playing the role that grafting-associativity played there.

---

## 9. Gaps and honest scope

1. **The construction and the theorem are prior art** (Gambino–Kock 4.5). The contribution is the
   container-coordinate proof of the universal property — `α`, `ĝ` by W-type recursion, and the
   inductive discharge of morphism-law/triangle/uniqueness against a *given* monoid `M` — the piece
   the companion note left open (its §6 gap #3). Graded `proved`.
2. **Set / LCC+W-types.** Every induction is structural over the initial algebra `S*` and uses only
   the recursion principle for W-types plus disjoint-union-of-bijections (Lemma A); no choice, no
   excluded middle. Valid in any LCC category with W-types (G-K's generality).
3. **§7 completion "against all monads"** rests on the Abbott–Altenkirch–Ghani representation
   theorem (full faithfulness of `⟦−⟧`, standard) and Gambino–Kock 4.5 (existence + polynomial
   carrier). Part 1 (Theorem A, the artifact) does **not** depend on these — it is self-contained
   given the Lean-verified carrier and laws and the elementary induction.
4. **Not yet Lean.** The recursion `ĝ` and the inductive proofs are designed to port to `Free.lean`
   (a `PTree`-recursor for `ĝ₁`, `ĝ♯` by the same recursion; §4/§6 inductions discharge the two
   `ContainerMorphism.ext_eq` obligations of "monoid morphism"). Flagged as the next LEAN target.

### References
- N. Gambino, J. Kock, *Polynomial functors and polynomial monads*, arXiv:0906.4931, Thm 4.5.
- N. Gambino, M. Hyland, *Wellfounded trees and dependent polynomial functors*, TYPES 2003.
- M. Abbott, T. Altenkirch, N. Ghani, *Containers: constructing strictly positive types*, TCS 342 (2005); *Representing nested inductive types using W-types*, ICALP 2004.
- MacBeth, *The free monad on a container as a `◁`-monoid* (`2026-07-16-free-monad-grafting-laws.md`); `Free.lean` (`Container.freeMonoid`, Lean-verified).
