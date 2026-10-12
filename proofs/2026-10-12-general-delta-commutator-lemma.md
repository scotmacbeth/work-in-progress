# The general δ-commutator lemma and the $T^2$ coupling criterion (route B: discrete Schreier)

**Date:** 2026-10-12 · **Session:** deep-work `/prove`
**Registry:** `supply-chain-inventory-gerbe-h2.json`, new node `coupled-T2-general-delta-lemma`
(child of `coupled-T2-d2-witness`; promotes the asserted `lifting-delta-commutator-lemma`).
**Scripts:** `scratch/verify_twisted_liftindep.py` (element-wise twisted-case verification across the
class-2 battery), `scratch/aut_engine.py` (coupling battery).

---

## 0. What this note proves (and what was already there)

The witness note `2026-10-11-coupled-T2-gerbe-stratum.md` stated a "Lemma (commutator formula for
$\delta$)" and dispatched its proof in one paragraph: *"The single relator $sts^{-1}t^{-1}$ of
$\mathbb Z^2$ evaluates the obstruction $2$-cocycle on the fundamental $2$-cell; its value is exactly
the defect $[A,B]$."* That is a correct slogan but not a proof — it asserts a cup/$d_2$ bookkeeping
fact without doing it. This note **does** the bookkeeping, in the discrete Schreier / extension-class
register (route B), for **general** finite $G$ of nilpotency class $\le 2$ and **general** (twisted)
coefficient action — not merely the trivial-action $D_4\times C_2$ witness. The finite $D_4\times C_2$
arithmetic is **not** re-derived; it is the instance, machine-checked separately
(`coupled-T2-finite-core-lean`, `[propext]`).

The two non-classical deliverables:
1. an **explicit bar$\leftrightarrow$Koszul comparison chain map** for $\mathbb Z^2$,
   $\varphi_2(e_{st})=[s\,|\,t]-[t\,|\,s]$, which turns the slogan into the identity
   $\langle[f],e_{st}\rangle=f(s,t)-f(t,s)$ and pins the class to the commutator;
2. the **coupling criterion** and its reading against the finite battery.

Everything resting on a classical black box (obstruction $=\rho^*[\ast]$; split $\leftrightarrow$ $0$;
extensions-with-abelian-kernel $\leftrightarrow H^2$) is flagged and cited (Brown, *Cohomology of
Groups*, GTM 87, Ch. IV; Eilenberg–MacLane 1947). The register is Borovoi `1608.07366` /
Pirashvili `2010.06493` (Schreier-style nonabelian $H^2$); the bare Schreier argument **suffices** —
Breen bitorseurs are not needed.

---

## 1. Standing hypotheses and the module $M$

Let $G$ be a finite group of **nilpotency class $\le 2$**, i.e. $[G,G]\subseteq Z(G)$, equivalently
$\operatorname{Inn}G\cong G/Z(G)$ is **abelian**. Write $M:=\operatorname{Inn}G$, additively. Consider
the extension of groups

$$1\longrightarrow M\xrightarrow{\ \iota\ }\operatorname{Aut}G\xrightarrow{\ \pi\ }\operatorname{Out}G\longrightarrow 1.\tag{$\ast$}$$

**$M$ is an $\operatorname{Out}G$-module.** $\operatorname{Aut}G$ acts on the normal subgroup
$\operatorname{Inn}G$ by conjugation; concretely $A\,c_g\,A^{-1}=c_{A(g)}$ for $A\in\operatorname{Aut}G$,
$g\in G$ ($c_g$ = conjugation by $g$). Inner automorphisms act **trivially** on $M$ (the conjugation
action of $M$ on the abelian group $M$ is trivial), so the action factors through
$\operatorname{Out}G=\operatorname{Aut}G/M$. We write $\bar A\cdot m$ for the action of
$\bar A\in\operatorname{Out}G$ on $m\in M$.

A **band** on $T^2$ is a homomorphism $\rho:\mathbb Z^2=\langle s,t\mid [s,t]\rangle\to\operatorname{Out}G$;
since $\mathbb Z^2$ is abelian, this is exactly a pair of **commuting** classes
$\bar A:=\rho(s),\ \bar B:=\rho(t)\in\operatorname{Out}G$. Via $\rho$, $M$ becomes a
$\mathbb Z^2$-module; set $\sigma:=\bar A\cdot(-)$, $\tau:=\bar B\cdot(-)\in\operatorname{Aut}(M)$ (they
commute, as $\mathbb Z^2$ is abelian and the action is a homomorphism). Because $T^2=B\mathbb Z^2$ is a
$K(\mathbb Z^2,1)$ and $M$ is abelian, $H^\bullet(T^2;M)=H^\bullet(\mathbb Z^2;M)$ is ordinary group
cohomology.

---

## 2. The connecting/obstruction map, as an extension class (route B)

For a band $\rho$ form the **pullback extension**

$$E_\rho:=\operatorname{Aut}G\times_{\operatorname{Out}G}\mathbb Z^2
=\{(a,\gamma)\in\operatorname{Aut}G\times\mathbb Z^2:\pi(a)=\rho(\gamma)\},\qquad
1\to M\xrightarrow{m\mapsto(\iota m,1)}E_\rho\xrightarrow{\ p\ }\mathbb Z^2\to1,$$

with $p(a,\gamma)=\gamma$ and $\ker p=\{(\iota m,1)\}\cong M$. Conjugation in $E_\rho$ gives $M$ exactly
the $\rho$-twisted module structure of §1: $(a,\gamma)(\iota m,1)(a,\gamma)^{-1}=(\iota(\pi(a)\cdot m),1)
=(\iota(\rho(\gamma)\cdot m),1)$, so $\gamma=s^it^j$ acts by $\sigma^i\tau^j$. 

**Definition.** $\delta(\rho):=[E_\rho]\in H^2(\mathbb Z^2;M)$, the class of this extension.

Three classical facts (Brown IV.3 Thm 3.12 for the $H^2\leftrightarrow$extensions dictionary, IV.4 for
lifting; Eilenberg–MacLane 1947):

* **(C1)** Extensions of $\mathbb Z^2$ by the abelian $\mathbb Z^2$-module $M$ inducing the fixed action
  are classified up to equivalence by $H^2(\mathbb Z^2;M)$, with the **split** extension
  $\leftrightarrow 0$.
* **(C2)** A homomorphic lift $\tilde\rho:\mathbb Z^2\to\operatorname{Aut}G$ of $\rho$ (i.e.
  $\pi\tilde\rho=\rho$) is the **same datum** as a group-theoretic splitting of $p:E_\rho\to\mathbb Z^2$:
  a lift $\tilde\rho$ gives the section $\gamma\mapsto(\tilde\rho(\gamma),\gamma)$, and a section
  $\gamma\mapsto(a(\gamma),\gamma)$ gives the lift $a=\tilde\rho$. Hence
  $$\delta(\rho)=0\iff \rho\text{ lifts to a homomorphism }\mathbb Z^2\to\operatorname{Aut}G.$$
* **(C3)** $[E_\rho]=\rho^*[\ast]$, where $[\ast]\in H^2(\operatorname{Out}G;M)$ is the class of the
  extension $(\ast)$ (pullback of extensions $=$ restriction of cohomology classes).

So $\delta$ is the connecting map of the pointed nonabelian sequence
$H^1(\operatorname{Aut}G)\xrightarrow{\pi_*}H^1(\operatorname{Out}G)\xrightarrow{\delta}H^2(M)$
on $T^2$, packaged concretely as an extension class. **The content left to prove is the value of this
class.**

---

## 3. $H^2(\mathbb Z^2;M)$ and the comparison chain map (the crux)

### 3.1 The two resolutions

Let $R=\mathbb Z[\mathbb Z^2]=\mathbb Z[s^{\pm1},t^{\pm1}]$. Two free resolutions of the trivial module
$\mathbb Z$:

**Koszul** $K_\bullet$: $\;0\to K_2\xrightarrow{\partial_2^K}K_1\xrightarrow{\partial_1^K}K_0\to\mathbb Z\to0$,
with $K_0=R\langle1\rangle$, $K_1=R\langle e_s,e_t\rangle$, $K_2=R\langle e_{st}\rangle$, and

$$\partial_1^K e_s=s-1,\quad\partial_1^K e_t=t-1,\qquad
\partial_2^K e_{st}=(s-1)\,e_t-(t-1)\,e_s.$$

(Check $\partial_1^K\partial_2^K e_{st}=(s-1)(t-1)-(t-1)(s-1)=0$ in the commutative ring $R$.)

Applying $\operatorname{Hom}_R(-,M)$ and identifying $\operatorname{Hom}_R(K_i,M)=M,M^2,M$:

$$M\xrightarrow{\ d^1\ }M^2\xrightarrow{\ d^2\ }M,\qquad
d^1(m)=\big((\sigma-1)m,(\tau-1)m\big),\quad
d^2(m_1,m_2)=(\sigma-1)m_2-(\tau-1)m_1,$$

(where $d^2=(\partial_2^K)^*$ reads off the two coefficients of $\partial_2^K e_{st}$). Hence

$$\boxed{\,H^2(\mathbb Z^2;M)=\operatorname{coker}d^2=M\big/\big((\sigma-1)M+(\tau-1)M\big)=M_{\mathbb Z^2}\,}$$

the **coinvariants**. (Exactly the formula used in the witness note.)

**Bar** $B_\bullet$: $B_n=R[\,\mathbb Z^2{}^n]$ free on normalized tuples $[g_1|\dots|g_n]$, with
$\partial_1[g]=(g-1)\cdot[\,]$ and $\partial_2[g|h]=g[h]-[gh]+[g]$. A bar $2$-cochain is a function
$f:(\mathbb Z^2)^2\to M$; it is a cocycle iff
$g\cdot f(h,k)-f(gh,k)+f(g,hk)-f(g,h)=0$ for all $g,h,k$.

### 3.2 The comparison map $\varphi:K_\bullet\to B_\bullet$

Define $R$-linear $\varphi_i$ lifting $\mathrm{id}_{\mathbb Z}$:
$\varphi_0(1)=[\,]$, $\varphi_1(e_s)=[s]$, $\varphi_1(e_t)=[t]$, and we **claim**

$$\boxed{\ \varphi_2(e_{st})=[s\,|\,t]-[t\,|\,s].\ }$$

*Verification that $\varphi$ is a chain map in the top degree.* We must check
$\partial_2^B\varphi_2=\varphi_1\partial_2^K$ on $e_{st}$.

$$\varphi_1\partial_2^K e_{st}=\varphi_1\big((s-1)e_t-(t-1)e_s\big)=(s-1)[t]-(t-1)[s].$$

On the other side, using $\partial_2^B[g|h]=g[h]-[gh]+[g]$,

$$\partial_2^B\big([s|t]-[t|s]\big)=\big(s[t]-[st]+[s]\big)-\big(t[s]-[ts]+[t]\big).$$

Since $st=ts$ in $\mathbb Z^2$, the terms $-[st]+[ts]$ cancel, leaving

$$s[t]+[s]-t[s]-[t]=(s-1)[t]-(t-1)[s].$$

The two sides agree. $\checkmark$ (The lower-degree conditions
$\partial_1^B\varphi_1=\varphi_0\partial_1^K$ are immediate: $\partial_1^B[s]=(s-1)[\,]$, etc.)

Because $\varphi$ is a chain map between **free** resolutions of $\mathbb Z$ lifting $\mathrm{id}$, the
induced $\varphi^*:H^2_{\mathrm{bar}}(\mathbb Z^2;M)\to H^2_{\mathrm{Koszul}}(\mathbb Z^2;M)=M_{\mathbb Z^2}$
is **the** canonical isomorphism (uniqueness of comparison maps up to homotopy). For a bar cocycle $f$,

$$\varphi^*[f]=\big[f\circ\varphi_2\big]=\big[f([s|t]-[t|s])\big]=\big[f(s,t)-f(t,s)\big]\in M_{\mathbb Z^2}.\tag{3.1}$$

This is the promised precise form of "evaluate the cocycle on the fundamental $2$-cell": the $2$-cell
$e_{st}$ maps to the antisymmetric bar expression $[s|t]-[t|s]$, the algebraic shadow of the torus
relator $sts^{-1}t^{-1}$.

---

## 4. The δ-commutator lemma

> **Lemma (general δ-commutator).** Let $G$ be finite of class $\le2$, $M=\operatorname{Inn}G$,
> $\rho:\mathbb Z^2\to\operatorname{Out}G$ a band, $A,B\in\operatorname{Aut}G$ **any** lifts of
> $\rho(s),\rho(t)$. Then
> $$w:=[A,B]=ABA^{-1}B^{-1}\in\ker\pi=M,$$
> and, under the identification $H^2(T^2;M)=M_{\mathbb Z^2}$ of §3.1,
> $$\delta(\rho)=[\,w\,]\in M_{\mathbb Z^2}.$$
> The class $[w]$ is independent of the choice of lifts, and
> $$\delta(\rho)=0\iff\exists\text{ lifts }A,B\text{ that commute in }\operatorname{Aut}G
> \iff\rho\text{ lifts to a homomorphism }\mathbb Z^2\to\operatorname{Aut}G.$$

**Proof.**

*(i) $w\in M$.* $\pi(w)=[\pi A,\pi B]=[\rho(s),\rho(t)]=1$ in $\operatorname{Out}G$, because
$\rho(s),\rho(t)$ are images under a homomorphism of the commuting generators $s,t$. Hence
$w\in\ker\pi=\operatorname{Inn}G=M$.

*(ii) The class is $[w]$.* Work in the pullback extension $1\to M\to E_\rho\xrightarrow{p}\mathbb Z^2\to1$
of §2. Choose lifts $\hat s:=(A,s),\ \hat t:=(B,t)\in E_\rho$ (legitimate: $\pi A=\rho(s),\pi B=\rho(t)$).
Then $[\hat s,\hat t]=([A,B],[s,t])=(w,1)$, i.e. $w\in\ker p$ is the commutator of the two lifts.

Define a **set-section** $u:\mathbb Z^2\to E_\rho$ by $u(s^it^j):=\hat s^{\,i}\hat t^{\,j}$ (every element
of $\mathbb Z^2$ is uniquely $s^it^j$; $u(1)=1$, $p\circ u=\mathrm{id}$). Its factor set
$f(g,h):=u(g)\,u(h)\,u(gh)^{-1}\in\ker p=M$ is a normalized bar $2$-cocycle representing $[E_\rho]$ with
the module action $g\cdot m=u(g)\,m\,u(g)^{-1}$ (Brown IV.3; the cocycle identity is the associativity of
$u(g)u(h)u(k)$). Evaluate on the two orderings of $(s,t)$, writing $M$ multiplicatively inside $E_\rho$:

$$f(s,t)=u(s)u(t)\,u(st)^{-1}=\hat s\hat t\,(\hat s\hat t)^{-1}=1,$$
$$f(t,s)=u(t)u(s)\,u(ts)^{-1}=\hat t\hat s\,(\hat s\hat t)^{-1}=\hat t\hat s\hat t^{-1}\hat s^{-1}
=[\hat s,\hat t]^{-1}=w^{-1},$$

using $ts=st$ so $u(ts)=u(st)=\hat s\hat t$. In additive $M$: $f(s,t)=0,\ f(t,s)=-w$. By (3.1),

$$\delta(\rho)=[E_\rho]=\varphi^*[f]=[\,f(s,t)-f(t,s)\,]=[\,0-(-w)\,]=[\,w\,]\in M_{\mathbb Z^2}.$$

*(iii) Lift-independence (direct form).* Any other lifts are $A'=A\,c_u,\ B'=B\,c_v$ with
$c_u,c_v\in M$ (two lifts of the same outer class differ by an inner, i.e. by an element of
$\ker\pi=M$); equivalently in $E_\rho$ replace $\hat s\mapsto\hat s\,u,\ \hat t\mapsto\hat t\,v$,
$u,v\in M$. Compute $w'=[\hat su,\hat tv]$ by moving every $M$-letter to the far left, each letter
picking up the action of the $\hat s/\hat t$-prefix to its left (recall $\hat s m\hat s^{-1}=\sigma(m)$,
$\hat t m\hat t^{-1}=\tau(m)$, depending only on the image in $\mathbb Z^2$):

$$\hat s\,u\,\hat t\,v\,u^{-1}\hat s^{-1}v^{-1}\hat t^{-1}
=\underbrace{\big[\sigma(u)+\sigma\tau(v)-\sigma\tau(u)-\tau(v)\big]}_{\in M}
\cdot\underbrace{\hat s\hat t\hat s^{-1}\hat t^{-1}}_{=w},$$

where the prefix of $u$ is $\sigma$ (letters to its left: $\hat s$), of the first $v$ is $\sigma\tau$
($\hat s\hat t$), of $u^{-1}$ is $\sigma\tau$, of $v^{-1}$ is $sts^{-1}=t\rightsquigarrow\tau$
($\hat s\hat t\hat s^{-1}$). Hence, additively,

$$w'-w=\sigma(u)-\sigma\tau(u)+\sigma\tau(v)-\tau(v)
=\tau(\sigma-1)v-\sigma(\tau-1)u.\tag{4.1}$$

Since $\sigma,\tau$ commute with $\sigma-1$ and $\tau-1$, we have
$\tau(\sigma-1)v=(\sigma-1)\tau(v)\in(\sigma-1)M$ and $\sigma(\tau-1)u=(\tau-1)\sigma(u)\in(\tau-1)M$.
Thus $w'-w\in(\sigma-1)M+(\tau-1)M$, so $[w']=[w]$ in $M_{\mathbb Z^2}$: the class is lift-independent.
(This also re-derives lift-independence without §2's intrinsic argument, and matches the formula asserted
in the witness note.)

*(iv) The vanishing criterion.* By (C1)+(C2), $\delta(\rho)=0\iff E_\rho$ splits $\iff\rho$ lifts to a
homomorphism. Concretely via (4.1): commuting lifts exist $\iff$ some $(u,v)$ makes $w'=0$ $\iff
0\in w+\big((\sigma-1)M+(\tau-1)M\big)$ $\iff[w]=0$ in $M_{\mathbb Z^2}$ $\iff\delta(\rho)=0$. $\qquad\blacksquare$

**Remark (sharp vs. slogan).** The vanishing criterion is "**no commuting lifts**", i.e.
$w\notin(\sigma-1)M+(\tau-1)M$ — strictly weaker than $w\neq0$ in $M$ when the action is nontrivial.
When $\sigma=\tau=\mathrm{id}$ (trivial action, as for the $D_4\times C_2$ witness), the coboundaries
vanish, $M_{\mathbb Z^2}=M$, and the criterion reduces to the clean $w=[A,B]\neq0$ in $\operatorname{Inn}G$.

---

## 5. The coupling criterion

Say $G$ **couples on $T^2$** if there is a band $\rho:\mathbb Z^2\to\operatorname{Out}G$ with
$\delta(\rho)\neq0$ (automatically $\beta=[\rho]\neq0$, since $\delta$ kills the trivial band:
$\delta(1)=0$ by the Lemma, $w=[\mathrm{id},\mathrm{id}]=0$).

> **Criterion.** For $G$ finite of class $\le2$:
> $$G\text{ couples on }T^2\iff\exists\text{ commuting }\bar A,\bar B\in\operatorname{Out}G\text{ with
> NO commuting lifts in }\operatorname{Aut}G.$$
> In particular, coupling forces $(\ast)$ to be **non-split**. (Non-split is necessary, not sufficient.)

**Proof.** ($\Leftarrow$) Such a pair defines a band $\rho(s)=\bar A,\rho(t)=\bar B$; by the Lemma
(iv), no commuting lifts $\Rightarrow\delta(\rho)\neq0$. ($\Rightarrow$) $\delta(\rho)\neq0$ for some
$\rho$; by (iv) the pair $(\rho(s),\rho(t))$ (commuting in $\operatorname{Out}G$) has no commuting lifts.

**Split $\Rightarrow$ decouple.** If $(\ast)$ splits there is a homomorphism
$\theta:\operatorname{Out}G\to\operatorname{Aut}G$ with $\pi\theta=\mathrm{id}$. For every band $\rho$,
$\theta\circ\rho:\mathbb Z^2\to\operatorname{Aut}G$ is a homomorphic lift, so $\delta(\rho)=0$ for all
$\rho$ (equivalently, the lifts $A=\theta\rho(s),B=\theta\rho(t)$ commute:
$[A,B]=\theta([\rho(s),\rho(t)])=\theta(1)=1$). By contraposition, coupling $\Rightarrow$ non-split.

**Necessity is not sufficiency.** Coupling needs a band, i.e. a $\rho:\mathbb Z^2\to\operatorname{Out}G$
(a *pair of commuting* outer classes) with $\rho^*[\ast]\neq0$. A rank-$1$ image never suffices
($H^2(\mathbb Z;-)=0$). So $[\ast]\neq0$ (non-split) is necessary, but one further needs $[\ast]$ to
restrict nontrivially to some commuting $\mathbb Z^2\to\operatorname{Out}G$; this can fail even when
$[\ast]\neq0$. The battery (§6) exhibits exactly this gap. $\qquad\blacksquare$

---

## 6. Against the finite battery `[computed]`

Scope guard (per PROVE brief): the criterion is **proved**; the enumeration below is **computed** over
the explicitly listed order-$\le16$ (plus $\mathrm{ES}^+_{32}$, $\mathrm{Heis}(\mathbb F_3)$) class-$2$
family — *not* a census of all groups of a given order.

`scratch/aut_engine.py` builds $\operatorname{Aut},\operatorname{Inn},\operatorname{Out}$ and, for each
group, searches **all** commuting outer pairs for one with no commuting lift (re-run 2026-10-12):

| $G$ | $\lvert\operatorname{Aut}\rvert$ | $\lvert\operatorname{Inn}\rvert$ | $\lvert\operatorname{Out}\rvert$ | $(\ast)$ split? | couples? |
|---|---|---|---|---|---|
| $D_4,\ Q_8$ | $8,24$ | $4$ | $2,6$ | split | no |
| $\mathrm{Heis}(\mathbb F_3)$ | $432$ | $9$ | $48$ | split | no |
| $M_{16},\ C_4\rtimes C_4$ | $16,32$ | $4$ | $4,8$ | — | no |
| $\mathrm{ES}^+_{32}=2^{1+4}_+$ | $1152$ | $16$ | $72$ | split | no |
| $\boxed{D_4\times C_2}$ | $64$ | $4$ | $16$ | **non-split** | **yes (30)** |
| $Q_8\times C_2$ | $192$ | $4$ | $48$ | **non-split** | **yes (54)** |

Only $D_4\times C_2$ and $Q_8\times C_2$ couple; every split row decouples, consistent with
"split $\Rightarrow$ decouple". $M_{16},C_4\rtimes C_4$ are the instructive rows: they need not split but
still carry **no** coupled band — "non-split" is genuinely weaker than "couples", as §5 warned.

**Twisted verification of the Lemma itself.** `scratch/verify_twisted_liftindep.py` checks the Lemma's
algebra **element-wise in $\operatorname{Aut}G$** across the whole class-$2$ battery, over **all**
commuting outer pairs and **all** $u,v\in M$ — crucially including pairs with **nontrivial** action
$\sigma,\tau$ (the $D_4\times C_2$ witness is trivial-action only). For every case:

* identity (4.1): $w'-w=\tau(\sigma-1)v-\sigma(\tau-1)u$ holds on the nose, and
* the equivalence "$\exists$ commuting lift $\iff w\in(\sigma-1)M+(\tau-1)M$" holds.

Totals: $D_4$ (1 nontrivial-action pair), $Q_8$ (6), $M_{16}$ (5), $C_4\rtimes C_4$ (10),
$\mathrm{Heis}(\mathbb F_3)$ (**168** nontrivial-action pairs, **13 608** element-wise checks),
$D_4\times C_2$ (44), $Q_8\times C_2$ (188) — **all pass**. This exercises the *twisted* coinvariant
quotient that the $D_4\times C_2$ witness alone cannot reach.

---

## 7. Verification (hostile-referee pass)

* **§3.2 chain map — GREEN.** $\partial_2^B([s|t]-[t|s])=(s-1)[t]-(t-1)[s]$ verified line-by-line; the
  cancellation $-[st]+[ts]=0$ uses only commutativity of $\mathbb Z^2$. $\varphi^*$ is the canonical iso
  by uniqueness of comparison lifts between free resolutions.
* **§4(ii) factor set — GREEN.** $f(s,t)=0,\ f(t,s)=w^{-1}$ are direct; the identification
  $[E_\rho]=\varphi^*[f]$ with $[f]$ represented by the section cocycle is Brown IV.3. No step uses the
  action being trivial.
* **§4(iii) formula (4.1) — GREEN** (hand-derivation) **and independently computed** on hundreds of
  nontrivial-action pairs (§6). The two agree.
* **§2 (C1)–(C3) — cited, classical** (Brown IV.3–4; Eilenberg–MacLane). Not re-derived; load-bearing but
  standard.
* **Boundary cases.** Trivial band: $w=0$, $\delta=0$ ✓. Rank-1 ($\mathbb Z$): $H^2=0$, never couples ✓
  (matches §5). Trivial action: reduces to the witness-note form ✓.
* **Reconciliation with the witness.** $D_4\times C_2$: $\sigma=\tau=\mathrm{id}$, $M_{\mathbb Z^2}=M=(\mathbb
  Z/2)^2$, $w=[A,B]=[s]\neq0\Rightarrow\delta\neq0$. Matches `coupled-T2-finite-core-lean`. ✓

**No RED. No YELLOW.**

---

## 8. Scope and (non-)gaps

* **Class-$\le2$ is essential**: it makes $M=\operatorname{Inn}G$ abelian, so $\delta$ lands in ordinary
  $H^2$ and $(\ast)$ is classified by $H^2(\operatorname{Out}G;M)$. Dropping it replaces $(\ast)$'s
  abelian-kernel theory by nonabelian $H^2$ (Eilenberg–MacLane obstruction valued in $Z(\operatorname{Inn}
  G)$-torsors) — genuinely harder, left open (and not needed for the inventory lane).
* **Classical backbone cited, not re-proved**: (C1)–(C3). The novelty is the explicit comparison map
  §3.2 $\Rightarrow$ commutator identity, the twisted lift-independence (4.1) with element-wise
  confirmation, and the criterion §5 with its necessary-not-sufficient refinement.
* **Battery is `computed`** over the enumerated family; minimality over *all* order-$\le16$ groups is not
  claimed (only the listed nonabelian class-$2$ ones were tested).
* **Base is $T^2$.** The argument is special to $\mathbb Z^2$ only through §3 (the two-generator one-relator
  Koszul resolution); a $g$-holed surface $\Sigma_g$ would use its genus-$g$ relator and give a sum of
  commutators — a natural next node, not done here.

---

### One-line summary

For $G$ of class $\le2$, the band-to-lifting connecting map on $T^2$ is given exactly by the commutator
of lifts, $\delta(\rho)=[\,[A,B]\,]\in\operatorname{Inn}G\big/\big((\sigma-1)+(\tau-1)\big)$ — proved in
the discrete Schreier register via the explicit comparison map $\varphi_2(e_{st})=[s|t]-[t|s]$ — and $G$
couples on $T^2$ iff some commuting outer pair has no commuting lift, forcing $\operatorname{Aut}G\to
\operatorname{Out}G$ non-split; only $D_4\times C_2,\,Q_8\times C_2$ couple in the enumerated order-$16$
class-$2$ family.
