# The coupled nonabelian-gerbe stratum on $T^2$: a fully computed witness where band and lifting-gerbe interact

**Date:** 2026-10-11 · **Session:** deep-work `/prove`
**Registry:** `supply-chain-inventory-gerbe-h2.json`, new child `coupled-T2-d2-witness` of `band-boundary`.
**Scripts:** `scratch/aut_engine.py` (brute-force Aut/Inn/Out + coupling search over a battery of groups), `scratch/d4c2_witness.py`, `scratch/verify_final.py` (independent from-scratch re-verification).

---

## 1. Problem

Over a base $N(C)\simeq T^2$ (take $C=B(\mathbb Z^2)$), exhibit an explicit inventory datum — a
structure group $G$ and an outer transport (band) $\rho:\mathbb Z^2\to \operatorname{Out}G$ — for which

* **(i)** the band class $\beta=[\rho]\in H^1(T^2;\operatorname{Out}G)$ is nonzero (Giraud stratum 2), and
* **(ii)** the band carries a **nonzero** degree-2 lifting obstruction via the connecting map
  $$\delta:\;H^1(T^2;\operatorname{Out}G)\longrightarrow H^2(T^2;\ \ker)$$
  of the coefficient extension $1\to\operatorname{Inn}G\to\operatorname{Aut}G\to\operatorname{Out}G\to1$,
  i.e. $\delta(\beta)\neq0$.

Then the two strata **do not split as an independent product**: a nonzero band forces a nonzero
degree-2 obstruction. $T^2$ is the first base where this can happen — on $S^1=B(\mathbb Z)$ one has
$H^2(S^1;-)=0$, so $\delta\equiv0$ and every band is strictifiable (the proved clause (c) of
`band-boundary`).

**A single fully-computed witness is a complete success for this lane.** We give one, with
$G=D_4\times C_2$ (order 16).

> **Honest correction of the target, stated up front (see §6).** The PROVE brief named the
> coefficient of (ii) as $Z(\operatorname{Aut}F)$. That is not the coefficient of the connecting
> map of the *named* extension $1\to\operatorname{Inn}G\to\operatorname{Aut}G\to\operatorname{Out}G\to1$.
> The connecting map of that extension lands in its **abelian kernel $\operatorname{Inn}G$** (abelian
> because we take $G$ of nilpotency class $2$). The witness below is for the extension exactly as
> named, with the corrected coefficient $\operatorname{Inn}G$. The center-valued phenomenon the brief
> had in mind is a *different stage* (companion (II), §5), and $D_4\times C_2$ witnesses that too.

---

## 2. Framework: the lifting connecting map and its value as a commutator

Let $G$ be a finite group of **nilpotency class $\le 2$**, so that $\operatorname{Inn}G=G/Z(G)$ is
**abelian**; write it additively as a $\mathbb Z[\operatorname{Out}G]$-module $M:=\operatorname{Inn}G$.
($\operatorname{Out}G$ acts on $M$ because $\operatorname{Aut}G$ acts on the normal subgroup
$\operatorname{Inn}G$ by conjugation, $A\,c_g\,A^{-1}=c_{A(g)}$, and inner automorphisms act trivially
since $M$ is abelian.) Consider the extension of coefficient groups
$$1\longrightarrow M=\operatorname{Inn}G \longrightarrow \operatorname{Aut}G \xrightarrow{\ \pi\ } \operatorname{Out}G \longrightarrow 1 .\tag{$\ast$}$$

A **band** is a homomorphism $\rho:\mathbb Z^2\to\operatorname{Out}G$; its class $\beta=[\rho]$ is the
basepoint of the pointed set $H^1(T^2;\operatorname{Out}G)$ iff $\rho$ is trivial, so
$\beta\neq0 \iff \rho\neq 1$. The pointed exact sequence of nonabelian cohomology of $(\ast)$ on $T^2$,
$$H^1(T^2;\operatorname{Aut}G)\xrightarrow{\ \pi_*\ }H^1(T^2;\operatorname{Out}G)
\xrightarrow{\ \delta\ }H^2(T^2;M),$$
has a connecting map $\delta$ ($M$ abelian): $\delta(\beta)$ is the obstruction to lifting $\rho$ to a
homomorphism $\mathbb Z^2\to\operatorname{Aut}G$, i.e. to realizing the outer band by a **strict**
$\operatorname{Aut}G$-valued transport. $\delta(\beta)=0 \iff \beta\in\operatorname{im}\pi_*$.

Because $T^2=B\mathbb Z^2$ and $M$ is abelian, both groups are ordinary group cohomology of
$\mathbb Z^2$. With $\sigma=\rho(s),\ \tau=\rho(t)$ acting on $M$ (I abuse notation and write
$\sigma,\tau\in\operatorname{Aut}(M)$ for the induced action),
$$H^2(\mathbb Z^2;M)=M_{\mathbb Z^2}=M\big/\big((\sigma-1)M+(\tau-1)M\big)\quad(\text{coinvariants}).$$

**Lemma (commutator formula for $\delta$).** Choose any set-lifts $A,B\in\operatorname{Aut}G$ of
$\rho(s),\rho(t)$. Then $w:=[A,B]=ABA^{-1}B^{-1}\in\ker\pi=M$ (since $\rho(s),\rho(t)$ commute), and
$$\delta(\beta)=[\,w\,]\in M_{\mathbb Z^2}=H^2(T^2;M),$$
independent of the choice of lifts. In particular $\delta(\beta)=0$ iff there exist lifts $A,B$ that
**commute** in $\operatorname{Aut}G$.

*Proof.* The single relator $sts^{-1}t^{-1}$ of $\mathbb Z^2$ evaluates the obstruction $2$-cocycle on
the fundamental $2$-cell of $T^2$; its value is exactly the defect $[A,B]\in M$. Lift-independence is
the coinvariant quotient: replacing $A\mapsto Au,\ B\mapsto Bv$ with $u,v\in M$ gives, computing in
$\operatorname{Aut}G$ (writing $M$ additively, $\sigma,\tau$ linear and commuting),
$$[Au,Bv]-[A,B]=\tau(\sigma-1)v-\sigma(\tau-1)u .$$
Since $\sigma,\tau$ are automorphisms commuting with $(\sigma-1),(\tau-1)$, the right-hand side ranges
over $(\sigma-1)M+(\tau-1)M$ as $u,v$ range over $M$. Hence $[w]$ is well-defined in the coinvariants,
and it is $0$ iff some lift choice makes $[Au,Bv]=1$, i.e. iff commuting lifts exist. $\square$

(The formula agrees with $\delta(\beta)=\rho^*[e]$, $[e]\in H^2(\operatorname{Out}G;M)$ the class of
$(\ast)$; in particular $(\ast)$ split $\Rightarrow[e]=0\Rightarrow\delta\equiv0$. This is why the
split cases $D_4,Q_8,\mathrm{Heis}(\mathbb F_3),\mathrm{ES}^+_{32}$ below carry **no** coupling.)

So the entire problem reduces to a **finite search**: find a class-$2$ group $G$ and two
**nontrivial, commuting-in-$\operatorname{Out}G$** elements whose lifts to $\operatorname{Aut}G$ can
**never** be made to commute.

---

## 3. The search and the witness

A pure-Python brute-force automorphism engine (`scratch/aut_engine.py`) computes
$\operatorname{Aut}G,\operatorname{Inn}G,\operatorname{Out}G$ from a multiplication table and runs the
search above. Results (automorphism orders match the standard values, confirming the engine returns
the *complete* automorphism group — essential, since a missed automorphism could fake a "no commuting
lift"):

| $G$ | $|{\rm Aut}|$ | $|{\rm Inn}|$ | $|{\rm Out}|$ | coupling witness? |
|---|---|---|---|---|
| $D_4$ | 8 | 4 | 2 | no (split) |
| $Q_8$ | 24 | 4 | 6 | no (split) |
| $\mathrm{Heis}(\mathbb F_3)$ | 432 | 9 | 48 | no (split, $\operatorname{Aut}=\mathbb F_3^2\rtimes GL_2$) |
| $M_{16}$ | 16 | 4 | 4 | no |
| $C_4\rtimes C_4$ | 32 | 4 | 8 | no |
| $SD_{16}, D_{16}$ | 16, 32 | 8, 8 | 2, 4 | no |
| $\mathrm{ES}^+_{32}=2^{1+4}_+$ | 1152 | 16 | 72 | no (split, $\operatorname{Out}=O_4^+(2)$) |
| $\boxed{D_4\times C_2}$ | **64** | **4** | **16** | **YES (30 pairs)** |
| $Q_8\times C_2$ | 192 | 4 | 48 | yes (54 pairs) |

**The witness.** $G=D_4\times C_2=\langle r,s\rangle\times\langle c\rangle$,
$\;r^4=s^2=c^2=1,\ srs^{-1}=r^{-1},\ c$ central. Then
$$Z(G)=\{1,r^2,c,r^2c\}\cong(\mathbb Z/2)^2,\qquad
\operatorname{Inn}G=G/Z(G)\cong(\mathbb Z/2)^2=\langle[r],[s]\rangle,\qquad |\operatorname{Out}G|=16.$$

Take the two automorphisms
$$A:\ r\mapsto r^{3},\ s\mapsto s,\ c\mapsto r^{2}c,
\qquad\qquad
B:\ r\mapsto r^{3}c,\ s\mapsto s,\ c\mapsto c.$$
(Both verified to be genuine automorphisms, and both **outer**: $[A],[B]\neq1$ in $\operatorname{Out}G$.
They exist because $r^2$ and $c$ are *two* central involutions, so $A,B$ may "mix" the three central
involutions $r^2,c,r^2c$ — a freedom that $D_4$ and $Q_8$ alone, with $|Z|=2$, do not have. This is
exactly why the extra $C_2$ factor breaks the splitting.)

* **Band.** Both $[A],[B]$ have order $2$ in $\operatorname{Out}G$, commute, and generate
  $\langle[A],[B]\rangle\cong(\mathbb Z/2)^2$. So
  $$\rho:\mathbb Z^2\twoheadrightarrow(\mathbb Z/2)^2\hookrightarrow\operatorname{Out}G,\quad
    s\mapsto[A],\ t\mapsto[B]$$
  is a nontrivial homomorphism: $\boxed{\beta=[\rho]\neq0}$ — **stratum 2 is nonzero.**

* **Both $A,B$ act trivially on $\operatorname{Inn}G=G/Z$** (e.g. $A(r)=r^3\equiv r$, $A(c)=r^2c\equiv c
  \bmod Z$). Hence $\sigma=\tau=\mathrm{id}$ on $M=\operatorname{Inn}G$, so
  $(\sigma-1)M+(\tau-1)M=0$ and
  $$H^2(T^2;\operatorname{Inn}G)=\operatorname{Inn}G=(\mathbb Z/2)^2\quad(\text{trivial coefficients}).$$

* **Obstruction.** $[A,B]=c_{s}$ (conjugation by $s$; the four group elements $s,sc,r^2s,r^2sc$ all
  induce it, differing by $Z$), so
  $$\boxed{\ \delta(\beta)=[A,B]=[s]\neq0\ \in\ H^2(T^2;\operatorname{Inn}G)=(\mathbb Z/2)^2.\ }$$
  **Stratum 3 is forced nonzero by the band.** The strata do **not** split.

By the Lemma (and brute force, §4) there is **no** choice of inner adjustments $u,v$ with
$[Au,Bv]=1$: the outer band $\rho$ is **not strictifiable** — it is realized by no strict
$\operatorname{Aut}G$-valued transport. It is an irreducible gerbe.

---

## 4. Verification

`scratch/verify_final.py` rebuilds $G=D_4\times C_2$ from scratch (independent of the engine) and checks:

1. $Z(G)=\{1,c,r^2,r^2c\}$, $|Z|=4$. ✓
2. $A,B$ are automorphisms (homomorphism + bijective on all $16$ elements). ✓
3. $A,B$ are **not** inner; $[A,B]=ABA^{-1}B^{-1}$ **is** inner (so $[A],[B]$ commute in
   $\operatorname{Out}G$) and equals conjugation by $s$. ✓
4. $A,B$ act trivially on $G/Z$. ✓
5. **No commuting lift:** exhaustively over all $16\times16$ pairs $(A\,c_u,\ B\,c_v)$, none commute.
   ✓ ($\Rightarrow\delta(\beta)\neq0$.)
6. **Lift-independence:** every realized commutator $[Ac_u,Bc_v]$ has the same class $[s]=(0,1)$ in
   coordinates $(\,[r],[s]\,)$ of $(\mathbb Z/2)^2$. ✓
7. Band structure: $\operatorname{ord}[A]=\operatorname{ord}[B]=\operatorname{ord}[AB]=2$,
   $\langle[A],[B]\rangle\cong(\mathbb Z/2)^2$. ✓

Automorphism-order cross-checks against known values ($|\operatorname{Aut}D_{16}|=32$,
$|\operatorname{Aut}(D_4\times C_2)|=64$, $|\operatorname{Aut}(Q_8\times C_2)|=192$,
$|\operatorname{Aut}\,2^{1+4}_+|=16\cdot|O_4^+(2)|=16\cdot72=1152$) confirm the engine computes the
complete $\operatorname{Aut}G$.

---

## 5. What the witness means

* **First coupling, as promised by the dimension count.** On $S^1=B\mathbb Z$, $H^2(S^1;-)=0$, so
  $\delta\equiv0$: every band lifts (clause (c), `band-boundary`, proved). $T^2$ is the first base with
  $H^2(T^2;M)\neq0$, and here $\delta(\beta)\neq0$ for an explicit $\beta\neq0$. So $T^2$ realizes the
  configuration $S^1$ forbids: **both** the band stratum and the degree-2 lifting stratum nonzero, with
  the lower **forcing** the higher.

* **The precise sense of "the strata do not split."** The sequence
  $H^1(\operatorname{Aut}G)\xrightarrow{\pi_*}H^1(\operatorname{Out}G)\xrightarrow{\delta}H^2(\operatorname{Inn}G)$
  is exact. "Split as an independent product" would mean $\delta\equiv0$ (every band realizable by a
  strict transport, the degree-2 datum a free parameter). Here $\delta\neq0$: the degree-2 class is not
  free — it is a **canonical function of the band**, $\beta\mapsto\delta(\beta)$, and is nonzero. This
  is the first place in the inventory program where two Giraud strata *talk* rather than merely stack.

* **Companion (II): the center-valued stage.** The earlier `band-boundary`/10-08 gerbe class lives in
  $H^2(Z(G))$ and belongs to the *central* extension $1\to Z(G)\to G\to\operatorname{Inn}G\to1$ (band
  valued in $\operatorname{Inn}G$). $D_4\times C_2$ witnesses that coupling on $T^2$ too: lifting the
  inner band $s\mapsto[r],\,t\mapsto[s]$ to $G$ gives commutator $[r,s]=r^2\in Z(G)$, nonzero in
  $H^2(T^2;Z(G))=(\mathbb Z/2)^2$ (trivial action). So the **same** group exhibits the coupling at both
  stages — $\operatorname{Out}\!\to\!\operatorname{Aut}$ lifting ($\delta$, coefficient
  $\operatorname{Inn}G$) and $\operatorname{Inn}\!\to\!G$ lifting (coefficient $Z(G)$).

---

## 6. Honest corrections to the PROVE brief

1. **Coefficient.** The connecting map of $1\to\operatorname{Inn}G\to\operatorname{Aut}G\to\operatorname{Out}G\to1$
   lands in the abelian kernel $\operatorname{Inn}G$, **not** $Z(\operatorname{Aut}F)$. The
   $Z$-coefficient belongs to the different (central) stage $1\to Z(G)\to G\to\operatorname{Inn}G\to1$
   (companion (II)). This is a genuine correction to the brief's statement (ii). For the class-$2$
   witness $D_4\times C_2$: $\operatorname{Inn}G=(\mathbb Z/2)^2$ and $Z(G)=(\mathbb Z/2)^2$ happen to be
   abstractly isomorphic, but they are different functors of $G$ and sit in different extensions.

2. **"The gerbe class depends on the band trivialisation."** False as literally stated — the Lemma
   proves $\delta(\beta)$ is **independent** of the lift/trivialisation (verification item 6). The
   correct statement: $\delta(\beta)$ is a well-defined, nonzero **function of the band $\beta$**; the
   coupling is that the degree-2 datum is pinned by the band, not free.

3. **No "Giraud $H^3$ existence obstruction" on $T^2$.** For the $2$-group
   $\mathrm{AUT}(G)=(G\xrightarrow{\mathrm{ad}}\operatorname{Aut}G)$ (with $\pi_1=\operatorname{Out}G$,
   $\pi_2=Z(G)$, $k$-invariant in $H^3(\operatorname{Out}G;Z(G))$), the obstruction to realizing a band
   by a *weak* gerbe pulls back to $H^3(T^2;-)=0$ and always vanishes. The only genuine degree-2
   coupling on $T^2$ is the **strictifiability** obstruction $\delta$ computed here. This locates the
   phenomenon precisely.

---

## 7. Scope and (non-)gaps

* The witness is **fully computed and independently re-verified**; every claim above is either a finite
  brute-force certificate or the elementary Lemma. No gaps in the witness.
* **Trust grade: `computed`** (sub-agent/own-computation level, per registry policy; promote to
  `proved` only after the Lemma + the $D_4\times C_2$ arithmetic are written up and refereed, and
  ideally after a Lean re-run of the finite check on the existing nerve-$\mathbb F_2$ / Aut engines).
* **Minimality is not claimed.** $D_4\times C_2$ (order 16) is the smallest in the battery that
  couples; a genuine minimality statement (over *all* groups of order $\le16$) would need the full
  order-16 census, not just the nine nonabelian ones we tried. Recorded as the one honest open edge.
* **Class-$2$ hypothesis.** Taken so that $\operatorname{Inn}G$ is abelian and $\delta$ lands in an
  ordinary $H^2$. Dropping it (nonabelian $\operatorname{Inn}G$) replaces the clean connecting map by an
  Eilenberg–MacLane obstruction valued in $Z(\operatorname{Inn}G)$-torsors; not needed here and left
  open.

---

### One-line summary

On $N(C)\simeq T^2$ with $C=B\mathbb Z^2$ and structure group $G=D_4\times C_2$, the band
$\rho(s)=[A],\ \rho(t)=[B]$ (two commuting outer involutions) has $\beta=[\rho]\neq0$ **and**
$\delta(\beta)=[A,B]=[s]\neq0\in H^2(T^2;\operatorname{Inn}G)=(\mathbb Z/2)^2$: the first fully-computed
$T^2$ point where the band stratum forces the degree-2 lifting stratum — the strata **couple**, and the
correct coefficient is $\operatorname{Inn}G$, not $Z(\operatorname{Aut}F)$.
