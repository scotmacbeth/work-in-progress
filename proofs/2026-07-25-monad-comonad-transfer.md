# The monad→comonad transfer on containers

**MacBeth — PROVE session, 2026-07-25.** Neil Ghani's Chapter 4, item 2 (email 2026-07-24).

## Problem statement

Let $M=(M,\eta,\mu)$ be a monad on $\mathbf{Set}$. Define an endofunctor $G\colon\mathbf{Cont}\to\mathbf{Cont}$ on the category of containers by
$$G(S,P)=(S,\,M\circ P),\qquad G(u,f)=(u,\,\{M(f_s)\}_s),$$
where a container morphism $(u,f)\colon(S,P)\to(T,Q)$ is a forward map $u\colon S\to T$ together with **backward** maps $f_s\colon Q(us)\to Ps$ (positions are *contravariant*). Equip $G$ with

* **counit** $\varepsilon_{(S,P)}\colon G(S,P)\to(S,P)$: forward $\mathrm{id}_S$, backward $\eta_{Ps}\colon Ps\to MPs$;
* **comultiplication** $\delta_{(S,P)}\colon G(S,P)\to G^2(S,P)=(S,MMP)$: forward $\mathrm{id}_S$, backward $\mu_{Ps}\colon MMPs\to MPs$.

**Theorem.** $(G,\varepsilon,\delta)$ is a comonad on $\mathbf{Cont}$. Its three comonad laws are *exactly* $M$'s three monad laws pulled back through the position-contravariance:
counit-left $\Leftrightarrow$ $M$ right-unit, counit-right $\Leftrightarrow$ $M$ left-unit, coassociativity $\Leftrightarrow$ $M$ associativity. Dually, a comonad $W$ on $\mathbf{Set}$ yields a monad $H(S,P)=(S,W\circ P)$ on $\mathbf{Cont}$.

Then: **(a)** $G$ is the **left coclosure of the substitution product $\lhd$ with the monad in the numerator**, $G(S,P)=\{M/(S,P)\}$ — equivalently the left Kan extension of $M$ along $(S,P)$ (Neil's structural "why"); **(b)** its extension to $\mathbf{Poly}$ is $\llbracket G(S,P)\rrbracket(A)=\sum_s(MPs\to A)$.

---

## Conventions

A container $(S,P)$ has a set of shapes $S$ and a family of position sets $P\colon S\to\mathbf{Set}$.
A morphism $(u,f)\colon(S,P)\to(T,Q)$ is $u\colon S\to T$ with $f_s\colon Q(us)\to Ps$ for each $s$.
Composition $(v,g)\circ(u,f)$ has forward $v\circ u$ and backward at $s$ equal to $f_s\circ g_{us}$ (backward maps compose in the *opposite* order). The identity is $(\mathrm{id}_S,\{\mathrm{id}_{Ps}\})$. The extension is $\llbracket S,P\rrbracket(A)=\sum_{s\in S}A^{Ps}=\sum_s\mathbf{Set}(Ps,A)$; a morphism $(u,f)$ acts by $(s,g\colon Ps\to A)\mapsto(us,\,g\circ f_s)$. Everything below uses that **$\varepsilon,\delta$ (and $G$) are identity on shapes**, so each equation reduces to a family of backward maps in $\mathbf{Set}$, one per shape.

---

## 1. The coordinate proof

Fix $M$. Write $A:=Ps$ throughout when we localise at a shape $s$ of $X=(S,P)$.

### 1.0 $G$ is an endofunctor (uses only that $M$ is a functor)
* Identities: $G(\mathrm{id}_S,\{\mathrm{id}_{Ps}\})=(\mathrm{id}_S,\{M(\mathrm{id}_{Ps})\})=(\mathrm{id}_S,\{\mathrm{id}_{MPs}\})=\mathrm{id}_{G(S,P)}$, since $M$ preserves identities.
* Composition: for $(u,f)\colon(S,P)\to(T,Q)$ and $(v,g)\colon(T,Q)\to(R,R')$ the composite has backward $f_s\circ g_{us}$; applying $G$ gives $M(f_s\circ g_{us})=M(f_s)\circ M(g_{us})$ by functoriality of $M$, which is exactly the backward map of $G(v,g)\circ G(u,f)$. Hence $G(\psi\circ\phi)=G\psi\circ G\phi$.

### 1.1 $\varepsilon$ is natural (uses naturality of $\eta$)
For $(u,f)\colon(S,P)\to(T,Q)$ we need $\varepsilon_{(T,Q)}\circ G(u,f)=(u,f)\circ\varepsilon_{(S,P)}$. Forward: $u=u$. Backward at $s$ (target positions $Q(us)$):
$$\text{LHS}=M(f_s)\circ\eta_{Q(us)},\qquad \text{RHS}=\eta_{Ps}\circ f_s,$$
equal by the naturality square of $\eta$ at $f_s\colon Q(us)\to Ps$.

### 1.2 $\delta$ is natural (uses naturality of $\mu$)
$\delta_{(T,Q)}\circ G(u,f)=G^2(u,f)\circ\delta_{(S,P)}$ reduces at $s$ (target positions $MMQ(us)$) to
$$M(f_s)\circ\mu_{Q(us)}=\mu_{Ps}\circ MM(f_s),$$
the naturality square of $\mu$ at $f_s$.

### 1.3 The three comonad laws
Because all forward maps are identities and composition reverses backward maps, the backward map of a composite $\beta\circ\alpha$ at $s$ is $(\text{bwd of }\alpha)\circ(\text{bwd of }\beta)$. Localise at $A=Ps$.

* **(C1) counit-left** $\varepsilon_{GX}\circ\delta_X=\mathrm{id}_{GX}$. Backward: $\delta_X$ gives $\mu_A\colon MMA\to MA$; $\varepsilon_{GX}$ (counit at $GX=(S,MP)$) gives $\eta_{MA}\colon MA\to MMA$. Composite $\mu_A\circ\eta_{MA}$. Equals $\mathrm{id}_{MA}$ $\iff$ $\mu\circ\eta M=\mathrm{id}$ — **$M$'s right-unit law**.

* **(C2) counit-right** $G\varepsilon_X\circ\delta_X=\mathrm{id}_{GX}$. Backward: $\delta_X$ gives $\mu_A$; $G\varepsilon_X$ applies $M$ to $\eta_A$, giving $M(\eta_A)\colon MA\to MMA$. Composite $\mu_A\circ M(\eta_A)$. Equals $\mathrm{id}$ $\iff$ $\mu\circ M\eta=\mathrm{id}$ — **$M$'s left-unit law**.

* **(C3) coassociativity** $G\delta_X\circ\delta_X=\delta_{GX}\circ\delta_X$. Backward LHS $\mu_A\circ M(\mu_A)$; backward RHS $\mu_A\circ\mu_{MA}$. Equal $\iff$ $\mu\circ M\mu=\mu\circ\mu M$ — **$M$'s associativity law**.

### 1.4 The biconditional
Given $M$ a functor with natural $\eta,\mu$ (needed to even define $G,\varepsilon,\delta$), §1.3 shows each of the three comonad equations, at fibre $A$, is the correspondingly named monad equation at $A$. Forward: $M$ a monad $\Rightarrow$ its laws hold at every set $\Rightarrow$ C1–C3 hold at every fibre of every container $\Rightarrow$ $G$ is a comonad. Converse: the single-shape container $(1,A)$ has $G(1,A)=(1,MA)$, and C1/C2/C3 there are exactly $M$'s three laws at the specific set $A$; letting $A$ range over all sets recovers all of $M$'s laws. Hence
$$\{\text{$G$'s comonad laws over all }\mathbf{Cont}\}\ \Longleftrightarrow\ \{\text{$M$'s monad laws over all }\mathbf{Set}\}.\qquad\square$$

### 1.5 The dual $H$
For a comonad $W=(W,\varepsilon^W,\delta^W)$ on $\mathbf{Set}$, set $H(S,P)=(S,W\circ P)$, unit $\eta^H$ with backward $\varepsilon^W_{Ps}\colon WPs\to Ps$, multiplication $\mu^H$ with backward $\delta^W_{Ps}\colon WPs\to WWPs$. The identical computation with $(\eta,\mu)\rightsquigarrow(\varepsilon^W,\delta^W)$ shows the three monad laws of $H$ are $W$'s three comonad laws. (This is the formal dual; see §2.)

---

## 2. The conceptual proof (the mechanism)

Let $p\colon\mathbf{Cont}\to\mathbf{Set}$, $(S,P)\mapsto S$. This is a bifibration; the reindexing along $u\colon S\to T$ is $u^*(T,Q)=(S,Q\circ u)$ (precompose the position family). The **fibre over $S$** is the category of families $P\colon S\to\mathbf{Set}$ with *vertical* morphisms (those over $\mathrm{id}_S$), i.e. families of backward maps $\{Qs\to Ps\}$ — this is $(\mathbf{Set}^S)^{\mathrm{op}}=(\mathbf{Set}^{\mathrm{op}})^S$ [von Glehn, TAC 33 (2018); the fibre op is precisely the position-contravariance].

$G$ is vertical ($pG=p$, identity on the base) and on each fibre it postcomposes with $M$:
$$G_S=(M\circ-)\colon(\mathbf{Set}^{\mathrm{op}})^S\to(\mathbf{Set}^{\mathrm{op}})^S,$$
which is the pushforward $(M^{\mathrm{op}})_*$ of $M^{\mathrm{op}}\colon\mathbf{Set}^{\mathrm{op}}\to\mathbf{Set}^{\mathrm{op}}$. Now:

1. A **monad** $M$ on $\mathbf{Set}$ is the same as a **comonad** $M^{\mathrm{op}}$ on $\mathbf{Set}^{\mathrm{op}}$ ($\eta$ becomes a counit, $\mu$ a comultiplication).
2. Pointwise postcomposition by a comonad is a comonad on the functor category; so $G_S$ is a comonad on each fibre, with counit $\eta$ and comultiplication $\mu$ (read in $\mathbf{Set}^{\mathrm{op}}$).
3. $G$ commutes strictly with reindexing: $u^*G_T=G_S u^*$ (both send $Q\mapsto M\circ Q\circ u$), and $\varepsilon,\delta$ are reindexing-stable. So $(G,\varepsilon,\delta)$ is a **fibred comonad** on $p$.
4. A fibred comonad with vertical $\varepsilon,\delta$ *is* a comonad on the total category: the total comonad laws are exactly the fibrewise ones (§1.3) together with reindexing-stability (automatic). $\square$

This is why the theorem is true, and why it is a formal duality: **"positions are contravariant" is the $(-)^{\mathrm{op}}$**, and a monad on the fibre base $\mathbf{Set}$ becomes a comonad because the fibre is $\mathbf{Set}^{\mathrm{op}}$. The single construction $M\mapsto(M^{\mathrm{op}})_*$ gives both $G$ (from a monad) and $H$ (from a comonad, via $W\mapsto W^{\mathrm{op}}$ a monad on $\mathbf{Set}^{\mathrm{op}}$).

---

## 3. Part (a) — Neil's characterisation: $G$ is the $\lhd$-left-coclosure

The substitution product $\lhd$ on $\mathbf{Poly}$ ($\llbracket p\lhd q\rrbracket=\llbracket p\rrbracket\circ\llbracket q\rrbracket$) is **left co-closed** [Niu–Spivak, *Polynomial Functors*, **Prop. 6.57**, after J. Meyers]: there is a left coclosure $\{q/p\}$ with
$$\mathbf{Poly}(p,\;r\lhd q)\ \cong\ \mathbf{Poly}(\{q/p\},\;r),\qquad \{q/p\}=\sum_{i\in p(1)}y^{\,q(p[i])}.\tag{6.58–6.59}$$

**Proposition.** With numerator the monad $M$ (as a $\mathbf{Set}$-endofunctor) and denominator $p=(S,P)$ (so $p(1)=S$, $p[s]=Ps$):
$$\{M/(S,P)\}=\sum_{s\in S}y^{\,M(Ps)}=(S,M\circ P)=G(S,P).$$
Moreover, for an **arbitrary** endofunctor $M$, $G(p)$ has the universal property
$$\mathbf{Poly}(G p,\;r)\ \cong\ [\mathbf{Set},\mathbf{Set}](\llbracket p\rrbracket,\;r\circ M)\qquad\text{naturally in }r\in\mathbf{Poly}.$$

*Proof.* The object identity is formula (6.59) read off directly. For the universal property, write $p=\sum_{i\in p(1)}y^{p[i]}$. By Yoneda, for any functor $F$, $[\mathbf{Set},\mathbf{Set}](\llbracket p\rrbracket,F)=\prod_{i}F(p[i])$. Take $F=r\circ M$: the right side is $\prod_i r(M(p[i]))$. On the left, $Gp=\sum_i y^{M(p[i])}$, and the polynomial hom formula gives $\mathbf{Poly}(\sum_i y^{M(p[i])},r)=\prod_i r(M(p[i]))$. The two agree, naturally in $r$. $\square$

When $M$ is polynomial this is literally the coclosure iso (6.58) with $q=M$; for general $M$ it is the honest self-contained statement above. By **Trimble's observation** [Niu–Spivak, **Ex. 6.63**], the left coclosure is a left Kan extension, $\{q/p\}=\mathrm{Lan}_p\,q$; hence
$$\boxed{\,G(S,P)=\{M/(S,P)\}=\mathrm{Lan}_{(S,P)}\,M\,}$$
— exactly Neil's "left Kan extension from the left coclosure of $\lhd$." The comonad data is the coclosure applied to $M$'s structure maps: $\varepsilon=\{\eta/p\}$ (backward $y^{\eta_{Ps}}$) and $\delta=\{\mu/p\}$ (backward $y^{\mu_{Ps}}$), reproducing §1.

*Naming caveat.* Niu–Spivak call this iso the **left** coclosure; Spivak's earlier notes call the same iso the **right** coclosure (opposite variance convention, same mathematics). We follow Neil's "left."

*Companion form.* Since $\mathbf{Cont}\cong\mathrm{Fam}(\mathbf{Set}^{\mathrm{op}})$ is the free small-coproduct completion of $\mathbf{Set}^{\mathrm{op}}$ under the representable embedding $y\colon\mathbf{Set}^{\mathrm{op}}\hookrightarrow\mathbf{Cont}$, $A\mapsto(1,A)$, and $G$ preserves coproducts ($G\sum_s y^{Ps}=\sum_s y^{MPs}$, checked), $G$ is *also* the coproduct-preserving extension $G=\mathrm{Lan}_y(y\circ M^{\mathrm{op}})$ of $y^A\mapsto y^{MA}$. The two Kan-extension statements are complementary: one extends $M$ *object-by-object along each container*; the other extends the representable action *globally along $y$*.

---

## 4. Part (b) — descent to $\mathbf{Poly}$

Directly from $\llbracket S,P'\rrbracket(A)=\sum_s A^{P's}$ with $P'=M\circ P$:
$$\llbracket G(S,P)\rrbracket(A)=\sum_{s\in S}A^{\,MPs}=\sum_{s\in S}\mathbf{Set}(MPs,\,A)=\sum_{s\in S}\big(MPs\to A\big).$$
Since $\llbracket-\rrbracket\colon\mathbf{Cont}\xrightarrow{\ \sim\ }\mathbf{Poly}\subset[\mathbf{Set},\mathbf{Set}]$ is fully faithful, $G$ transports to a comonad $\hat G$ on $\mathbf{Poly}$. Geometrically $\hat G$ **applies $M$ to the fibres of the direction bundle**: a polynomial $p=\sum_s y^{Ps}$ is the bundle $\sum_s Ps\to p(1)$, and $\hat G p$ is $\sum_s MPs\to p(1)$. Its counit $\hat G p\to p$ re-exponentiates each fibre along $\eta$ (i.e. $A^{MPs}\to A^{Ps}$, $g\mapsto g\circ\eta_{Ps}$) and its comultiplication along $\mu$. (Note $\hat G$ is defined on $\mathbf{Poly}$ — it uses the bundle presentation — not canonically on all of $[\mathbf{Set},\mathbf{Set}]$.)

---

## Verification (computational)

`scratch/monad-comonad-transfer/check.py` (extended this session):

* All three comonad laws **PASS** for $M=$ Maybe and $M=$ Writer/$\mathbb Z_2$ on $S=\{a,b\}$, $P(a)=\{0,1\}$, $P(b)=\{0\}$; the dual $H$ (product comonad $\to$ monad) all three monad laws **PASS**.
* **Negative controls fire exactly**: a non-associative $\mu$ breaks coassociativity; a wrong unit ($\eta$ tag $=1$) breaks *both* counit laws and leaves coassociativity intact — so each comonad law is sensitive to precisely its dual monad law.
* $G$ **preserves binary coproducts**, and $\varepsilon,\delta$ are **natural** on a non-trivial morphism (both directions checked).
* **Coclosure universal property** $\mathbf{Poly}(Gp,r)=\mathbf{Poly}(p,r\lhd M)$ verified by counting for $M=$ Maybe, $p$ with position sizes $(2,0,1)$, and $r\in\{y,\ y^2{+}1,\ y^3{+}y,\ 2y^2{+}1\}$: $6,100,600,513$ on both sides.

---

## Novelty (cleared this session)

The construction $(S,P)\mapsto(S,M\circ P)$ as a monad→comonad transfer on $\mathbf{Cont}$ appears in **none** of the neighbouring papers:

* **Ahman–Uustalu, *Update Monads: Cointerpreting Directed Containers*** runs the *opposite* direction (cointerpretation $\mathbf{Cont}^{\mathrm{op}}\to[\mathbf{Set},\mathbf{Set}]$; the update monad is a *Set*-monad built *from* a directed container). Absent.
* **Purdy–Damato, *Distributive Laws of Monadic Containers* (2025)**: horizontal distributive laws between two *given* monadic containers (Def. 23, Props. 24–25). Different mechanism. Absent.
* **Niu–Spivak, Poly**: no named $(S,P)\mapsto(S,M\circ P)$; the nearest named object is precisely the left coclosure (Prop. 6.57) that §3 uses.
* Thematic neighbours on the general idea (cited, distinguished): Hinze, *Monads from Comonads*; the Topos Institute PLTL blog map $\lambda\colon MP\to P I^{\mathrm{op}}$.

**Verdict.** The theorem is an instance of standard fibred-category folklore — *a (co)monad on the fibre category induces a fibrewise (co)monad on the total category of a fibration* — specialised to $\mathbf{Cont}\to\mathbf{Set}$ with fibre $(\mathbf{Set}^{\mathrm{op}})^S$ (§2). The **contribution** is: (i) the container-coordinate proof turning each comonad law into the correspondingly-named monad law (§1); (ii) the fibred reformulation isolating the mechanism (§2); (iii) the identification $G=\{M/-\}=\mathrm{Lan}_{(-)}M$ confirming and proving Neil's left-coclosure characterisation with an explicit universal property (§3); (iv) the Chapter 4 exposition. Grade §1–§3: **proved**. Construction itself cited as folklore, with AU / Purdy–Damato explicitly distinguished.

## Gaps

None in §1–§4 as stated. Two citation-level notes (not gaps in the argument): the identity $\{q/p\}=\mathrm{Lan}_p q$ is used as Trimble's observation (Ex. 6.63), not re-derived here; the fibred-comonad$\Rightarrow$total-comonad step (§2.4) is standard fibred category theory quoted without a from-scratch proof (the from-scratch content is precisely §1.3–§1.4).
