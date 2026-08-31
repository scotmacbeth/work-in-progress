# PROVE — Universal property of the free monad on a container

Working notebook. 2026-07-24.

## The claim (restated in my own words)

`U : Mon(Cont) → Cont` (forget the monoid structure of a `◁`-monoid, i.e. of a
polynomial monad) has a left adjoint `F : X ↦ m_X`, the free-monad container.
Concretely: an insertion-of-generators morphism `α_X : X ⇒ U(m_X)` such that for every
monoid `M=(T◁Q, e_M, μ_M)` in `(Cont,◁,I)` and every container morphism `g : X ⇒ U(M)`
there is a **unique** monoid morphism `ĝ : m_X ⇒ M` with `U(ĝ) ∘ α_X = g`.

Everything about `m_X` and its `◁`-monoid structure is already proved + Lean-verified
(`Free.lean`, `2026-07-16-free-monad-grafting-laws.md`). The NEW content is: `α`, `ĝ`, the
triangle, that `ĝ` is a monoid morphism, and uniqueness.

## Coordinates fixed (from the grafting note / Free.lean)

- `X = (S◁P)`. Free carrier `m = (S*◁P*)`, `S* = PTree`, `P* = leaves`.
  - `lf : S*`, `nd s κ : S*` (`s:S`, `κ:P s → S*`).
  - `leaves(lf)=1`, `leaves(nd s κ)=Σ_{p:P s} leaves(κ p)`.
- Monoid unit of `m`: `e:I⇒m`, `e₁(*)=lf`, `e♯=id:1→1`.
- Monoid mult of `m`: `μ:m◁m⇒m`, `μ₁(t,u)=graft(t,u)`, `μ♯=split`.
  - `graft(lf,u)=u(())`, `graft(nd s κ,u)=nd s(λp.graft(κ_p,u_p))`, `u_p:=λr.u⟨p,r⟩`.
  - `split_{lf,_}(w)=⟨(),w⟩`, `split_{nd s κ,u}(⟨p,z₂⟩)=⟨⟨p,(split_{κ_p,u_p}z₂).1⟩,(split_{κ_p,u_p}z₂).2⟩`.
- Morphism `φ:(A◁P_A)⇒(B◁P_B)`: fwd `φ₁:A→B`, bwd `φ♯_a:P_B(φ₁ a)→P_A(a)`.
  - comp `(φ;ψ)₁=ψ₁∘φ₁`, `(φ;ψ)♯_a=φ♯_a∘ψ♯_{φ₁ a}`.
  - tensor `(φ◁ψ)₁(a,g)=(φ₁a, ψ₁∘g∘φ♯_a)`, `(φ◁ψ)♯_{(a,g)}(j,k)=(φ♯_a j, ψ♯_{g(φ♯_a j)}k)`.
- `g:(S◁P)⇒(T◁Q)`: fwd `g₁:S→T`, bwd `g♯_s:Q(g₁ s)→P(s)`.

## Insertion of generators `α_X : X ⇒ m_X`

- `α₁ s = nd s (λp. lf)`  (single node of shape s, all children leaves).
- `leaves(nd s (λp.lf)) = Σ_{p:P s} leaves(lf) = Σ_{p:P s} 1 ≅ P s`.
- `α♯_s : leaves(α₁ s) → P s`,  `α♯_s ⟨p,()⟩ = p`  (canonical iso).

## The induced morphism `ĝ : m ⇒ M`

Forward `ĝ₁ : PTree → T`, well-founded recursion on the tree:
```
ĝ₁(lf)      = e_M₁(*) =: ε
ĝ₁(nd s κ)  = μ_M₁( g₁ s,  λ q:Q(g₁ s). ĝ₁( κ (g♯_s q) ) )
```
(subtree `κ(g♯_s q)` is structurally smaller — recursion terminates.)

Backward `ĝ♯_t : Q(ĝ₁ t) → leaves(t)`:
```
ĝ♯_lf         : Q(ε) → leaves(lf)=1    is the unique map (const ()).
ĝ♯_{nd s κ}(r) = ⟨ g♯_s q,  ĝ♯_{κ(g♯_s q)}(ρ) ⟩   where (q,ρ)=μ_M♯_{(g₁ s, λq.ĝ₁(κ(g♯_s q)))}(r).
```

## Monoid-morphism laws, in coordinates

`h:m⇒M` is a monoid morphism iff (`;`=apply-first-left):
- **UNIT**: `e ; h = e_M : I⇒M`.  Fwd: `h₁(lf)=ε`. Bwd: automatic (both maps → 1 terminal).
- **MULT**: `μ ; h = (h◁h) ; μ_M : m◁m⇒M`.
  - Fwd (MULT-fwd): `h₁(graft(t,u)) = μ_M₁( h₁ t, λq. h₁(u(h♯_t q)) )`.
  - Bwd (MULT-bwd): for `r:Q(h₁ graft(t,u))` (≅ `Q(μ_M₁(h₁t,…))` via MULT-fwd),
    `split_{t,u}(h♯_{graft t u} r) = ⟨ h♯_t q, h♯_{u(h♯_t q)}(r') ⟩`, `(q,r')=μ_M♯_{(h₁t,λq.h₁(u(h♯_t q)))}(r)`.

## Strategy

- ĝ₁(lf)=ε gives UNIT immediately. Bwd UNIT automatic.
- MULT-fwd for ĝ: **induction on t**. Base `t=lf` = M's LEFT-UNIT law (fwd). Step `t=nd s κ`
  = M's ASSOCIATIVITY (fwd) + IH. [worked below]
- MULT-bwd for ĝ: same induction. Base = M's LEFT-UNIT (bwd). Step = M's ASSOC (bwd) + IH +
  split/leaf calculus (identical to Lemma A/D flat-concatenation bookkeeping).
- Triangle `ĝ∘α=g`: direct, fwd uses M-left-unit on the single node; bwd uses M-left-unit bwd.
- Uniqueness: any monoid morphism h with h∘α=g satisfies the SAME recursion (h(lf)=ε forced by
  UNIT; h(nd s κ)=μ_M(g(s),…) forced by MULT-fwd + triangle), so h=ĝ by tree induction.

KEY LEMMA: MULT (fwd+bwd) for ĝ. Reduces, by induction on t, to M's own monoid laws.
I do NOT prove M's laws — M is a given monoid; I apply them.

## MULT-fwd, worked

t=lf: LHS=ĝ₁(u()). RHS=μ_M₁(ε, λq.ĝ₁(u(ĝ♯_lf q)))=μ_M₁(ε, const_{ĝ₁ u()}) =(M-left-unit fwd)= ĝ₁(u()). ✓
t=nd s κ, a₀:=g₁s, b₀:=λq.ĝ₁(κ_{g♯_s q}):
  LHS=ĝ₁(graft(nd s κ,u))=ĝ₁(nd s (λp.graft(κ_p,u_p)))
     =μ_M₁(a₀, λq.ĝ₁(graft(κ_{g♯_s q},u_{g♯_s q})))
     =(IH) μ_M₁(a₀, λq. μ_M₁(ĝ₁ κ_{g♯_s q}, λq'. ĝ₁(u_{g♯_s q}(ĝ♯_{κ_{g♯_s q}} q')))).
  RHS=μ_M₁(ĝ₁(nd s κ), λq̃. ĝ₁(u(ĝ♯_{nd s κ} q̃)))
     =μ_M₁(μ_M₁(a₀,b₀), λq̃. ĝ₁(u(ĝ♯_{nd s κ} q̃))).
  With ĝ♯_{nd s κ}(q̃)=⟨g♯_s q, ĝ♯_{κ_{g♯_s q}} ρ⟩, (q,ρ)=μ_M♯_{(a₀,b₀)}(q̃), and
  u(⟨g♯_s q, ĝ♯_{κ_{g♯_s q}} ρ⟩)=u_{g♯_s q}(ĝ♯_{κ_{g♯_s q}} ρ), define
  c⟨q,q'⟩ := ĝ₁(u_{g♯_s q}(ĝ♯_{κ_{g♯_s q}} q')). Then RHS=μ_M₁(μ_M₁(a₀,b₀), λq̃. c(μ_M♯_{(a₀,b₀)} q̃)),
  which by M-ASSOC (fwd) = μ_M₁(a₀, λq. μ_M₁(b₀ q, λq'. c⟨q,q'⟩)) = LHS. ✓

## MULT-bwd, worked (base)

t=lf: c:=ĝ₁(u()). r:Q(c). LHS=split_{lf,u}(ĝ♯_{u()} r)=⟨(),ĝ♯_{u()} r⟩.
RHS: (q,r')=μ_M♯_{(ε,const_c)}(r); ĝ♯_lf q=(); RHS=⟨(),ĝ♯_{u()} r'⟩.
M-LEFT-UNIT (bwd): snd(μ_M♯_{(ε,const_c)}(r))=r  ⟹ r'=r ⟹ LHS=RHS. ✓

## MULT-bwd, step (t=nd s κ) — WORKED, = M-ASSOC (bwd) + fwd-IH + bwd-IH.

Notation: a₀:=g₁s, b₀:=λq.ĝ₁(κ_{g♯_s q}) [so ĝ₁(nd s κ)=μ_M₁(a₀,b₀)],
b₁:=λq.ĝ₁(graft(κ_{g♯_s q},u_{g♯_s q})) [so ĝ₁(graft(nd s κ,u))=μ_M₁(a₀,b₁)].
Set C⟨q,q'⟩ := ĝ₁(u_{g♯_s q}(ĝ♯_{κ_{g♯_s q}} q')), a family on Σ_q Q(b₀ q).

Two facts glue it:
(i) FWD-IH: μ_M₁(b₀ q, λq'.C⟨q,q'⟩) = ĝ₁(graft(κ_{g♯_s q},u_{g♯_s q})) = b₁ q  [MULT-fwd on subtree].
    ⟹ M-assoc-fwd's RHS family = b₁, and C∘μ_M♯_{(a₀,b₀)} = B (:=λq̂.ĝ₁(u(ĝ♯_{nd s κ} q̂))), via (†).
    So M-ASSOC (applied to shape ((a₀,b₀),C)) is exactly the shape-equality
    μ_M₁(μ_M₁(a₀,b₀),B) = μ_M₁(a₀,b₁), i.e. the two trees I split r over.
(ii) M-ASSOC-bwd (Lemma-D mirror for the GIVEN monoid M): the two backward composites of the
    associativity square agree. Instantiated at C above it reads: writing
      RHS-way:  (q̂,r'')=μ_M♯_{(μ_M₁(a₀,b₀),B)}(r); (q,ρ)=μ_M♯_{(a₀,b₀)}(q̂)          ⟹ ((q,ρ),r'')
      LHS-way:  (q₁,ρ₁)=μ_M♯_{(a₀,b₁)}(r); (q',ρ')=μ_M♯_{(b₀ q₁,β)}(ρ₁)             ⟹ ((q₁,q'),ρ')
    we get q=q₁, ρ=q', r''=ρ'.

Now compute both sides of MULT-bwd:
  LHS = split_{nd s κ,u}(ĝ♯_{graft(nd s κ,u)}(r))
      = ⟨⟨p₁,(split_{κ_{p₁},u_{p₁}}(z₂)).1⟩, (split_{κ_{p₁},u_{p₁}}(z₂)).2⟩   [split nd-clause; p₁=g♯_s q₁, z₂=ĝ♯_{graft(κ_{p₁},u_{p₁})}(ρ₁)]
      =(BWD-IH on κ_{p₁},u_{p₁},ρ₁)= ⟨⟨p₁, ĝ♯_{κ_{p₁}}(q')⟩, ĝ♯_{u_{p₁}(ĝ♯_{κ_{p₁}} q')}(ρ')⟩.
  RHS = ⟨ĝ♯_{nd s κ}(q̂), ĝ♯_{u(ĝ♯_{nd s κ} q̂)}(r'')⟩
      = ⟨⟨g♯_s q, ĝ♯_{κ_{g♯_s q}}(ρ)⟩, ĝ♯_{u_{g♯_s q}(ĝ♯_{κ_{g♯_s q}} ρ)}(r'')⟩   [by (†) and u∘⟨⟩ = u_{...}].
  By (ii): q=q₁, ρ=q', r''=ρ'. Hence p₁=g♯_s q₁=g♯_s q, outer leaves match, inner reduces to r''=ρ'. LHS=RHS. ✓

So the FULL homomorphism law (fwd+bwd) for ĝ holds by induction on t:
  base t=lf = M's LEFT-UNIT (both comps); step t=nd = M's ASSOC (both comps) + fwd-IH + bwd-IH.
No law of M is proved — M is a given monoid; its laws are applied as morphism equations.

## Triangle  α;ĝ = g  — uses M's RIGHT-UNIT (both comps).

Fwd: (α;ĝ)₁ s = ĝ₁(nd s(λp.lf)) = μ_M₁(g₁ s, λq.ĝ₁ lf) = μ_M₁(g₁ s, const_ε) =(M-right-unit fwd)= g₁ s. ✓
Bwd: (α;ĝ)♯_s = α♯_s ∘ ĝ♯_{nd s(λp.lf)}. For r: ĝ♯_{nd s(λp.lf)}(r)=⟨g♯_s q,()⟩, q=fst μ_M♯_{(g₁s,const_ε)}(r);
     α♯_s⟨g♯_s q,()⟩ = g♯_s q; and M-right-unit bwd gives q=r. So (α;ĝ)♯_s(r)=g♯_s r. ✓

## Uniqueness — any monoid morphism h with α;h=g equals ĝ.

Node-as-graft identity: nd s κ = graft(α₁ s, w), w⟨p,()⟩:=κ p. [check: graft(nd s(λp.lf),w)=nd s(λp.graft(lf,w_p))=nd s(λp.κ p).]
Fwd (induction on t):
  lf: UNIT ⟹ h₁ lf=ε=ĝ₁ lf.
  nd: h₁(nd s κ)=h₁(graft(α₁ s,w)) =(MULT-fwd h)= μ_M₁(h₁ α₁s, λq.h₁(w(h♯_{α₁s}q))).
      Triangle fwd: h₁ α₁s=g₁ s. Triangle bwd: α♯_s(h♯_{α₁s}q)=g♯_s q ⟹ h♯_{α₁s}q=⟨g♯_s q,()⟩ ⟹ w(h♯_{α₁s}q)=κ(g♯_s q).
      = μ_M₁(g₁ s, λq.h₁(κ(g♯_s q))) =(fwd-IH)= μ_M₁(g₁ s, λq.ĝ₁(κ(g♯_s q))) = ĝ₁(nd s κ). ✓
Bwd (induction on t):
  lf: h♯_lf:Q(ε)→1 unique = ĝ♯_lf.
  nd: MULT-bwd(h) at (α₁ s,w), then invert split (Lemma A: split bijective, inverse cat):
      h♯_{nd s κ}(r) = cat_{α₁ s,w}(⟨h♯_{α₁s}q, h♯_{w(h♯_{α₁s}q)}(r')⟩), (q,r')=μ_M♯_{(g₁s,b₀)}(r) [families via triangle+fwd-IH].
      h♯_{α₁s}q=⟨g♯_s q,()⟩; w(...)=κ(g♯_s q); h♯_{κ(g♯_s q)}(r')=ĝ♯_{κ(g♯_s q)}(r') (bwd-IH).
      cat base: cat_{nd s(λp.lf),w}(⟨p,()⟩,x)=⟨p,x⟩. So h♯_{nd s κ}(r)=⟨g♯_s q, ĝ♯_{κ(g♯_s q)}(r')⟩ = ĝ♯_{nd s κ}(r) by (†). ✓
Lemma A (split=cat⁻¹) is what makes the backward map FORCED — same bijection that forced μ♯.

STATUS: proof COMPLETE, all cases. Awaiting computational confirmation.

## TODO — ALL DONE (2026-07-24)
- [x] computational verification: free_monad_up_verify.py — Writer(ℤ/3), Reader (nontrivial bwd),
      free m_Y; triangle+UNIT+MULT(fwd+bwd)+uniqueness ALL PASS; 306 exhaustive (t,u); neg controls fire.
      Independently confirmed triangle uses M's RIGHT-unit.
- [x] MULT-bwd step written rigorously (M-assoc bwd + fwd-IH + bwd-IH + split calculus) — see above.
- [x] Part 2 done (⟦−⟧ strong monoidal + AAG ff ⟹ preserves free monoid; GK 4.5 completes).
- [x] Final artifact: proofs/2026-07-24-free-monad-universal-property.md (§1–9).
- [x] Registry node free-monad-universal-property = proved (validates).
- [x] SUMMARY, PROGRESSIVE_DISCLOSURE, MEMORY, collaborator note all updated.

STATUS: SOLVED. Next session = LEAN (ĝ as PTree recursor).
