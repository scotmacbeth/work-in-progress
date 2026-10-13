# The two $T^2$ gerbe obstructions are NOT independent: a forced one-way correlation

**Date:** 2026-10-13 · **Session:** deep-work `/prove`
**Registry:** `supply-chain-inventory-gerbe-h2.json`, new child node `gerbe-two-ends-correlation`
(of `thm-A-rectification`), building on `coupled-T2-general-delta-lemma` **[proved]**.
**Scripts:** `scratch/2026-10-13-two-ends-crosstab.py` (full cross-tabulation over the class-$2$
battery), reusing `scratch/aut_engine.py`.

---

## 0. Verdict

The PROVE brief asked us to decide, over $T^2=B\mathbb Z^2$, between

* **(A)** *independence* — both off-diagonal corners $(\delta\neq0,[\mathfrak g]=0)$ and
  $(\delta=0,[\mathfrak g]\neq0)$ realized, and
* **(B)** *forced correlation* — some implication always holds.

**The answer is (B).** For every finite group $K$ of nilpotency class $\le2$ (the exact domain on
which both obstructions are abelian-$H^2$-valued),

$$\boxed{\ \delta\text{ couples on }T^2\ \Longrightarrow\ [\mathfrak g]\text{ couples on }T^2\ }$$

i.e. the corner $(\delta\neq0,\ [\mathfrak g]=0)$ is **forced empty**. The converse corner
$(\delta=0,\ [\mathfrak g]\neq0)$ **is** occupied (e.g. $K=D_4$, the dihedral $4\mid n$ witness at
$n=4$), so the correlation is **strict and one-directional**. There is no logical independence.

The group-theoretic cause is a structural **asymmetry between the two extensions** that the symmetric
"both are commutator obstructions of an abelian-kernel extension through the hinge $\operatorname{Inn}K$"
picture hides:

* the **central** extension $1\to Z(K)\to K\to\operatorname{Inn}K\to1$ is **non-split for every
  nonabelian** class-$2$ $K$, and its coefficient $Z(K)$ carries the **trivial** $\operatorname{Inn}K$-action,
  so $[\mathfrak g]$ is **universally obstructed** — every nonabelian class-$2$ group couples at the
  central end;
* the **strictification** extension $1\to\operatorname{Inn}K\to\operatorname{Aut}K\to\operatorname{Out}K\to1$
  **can split** (it does for $D_4,Q_8,\operatorname{Heis}(\mathbb F_3),M_{16},C_4\rtimes C_4$), killing
  $\delta$ **selectively**.

Strictification coupling is therefore a *strictly stronger* non-commutativity condition than central
coupling, and it cannot occur without the weaker one.

---

## 1. Setup: the two ends as one lemma, applied twice

Let $K$ be finite of nilpotency class $\le 2$, so $[K,K]\subseteq Z(K)$ and
$M:=\operatorname{Inn}K=K/Z(K)$ is **abelian**. Two abelian-kernel group extensions share the hinge
$\operatorname{Inn}K$:

$$(\Sigma)\quad 1\to\operatorname{Inn}K\xrightarrow{\ }\operatorname{Aut}K\xrightarrow{\ \pi\ }\operatorname{Out}K\to1,
\qquad\qquad
(Z)\quad 1\to Z(K)\xrightarrow{\ }K\xrightarrow{\ \mathrm{ad}\ }\operatorname{Inn}K\to1 .$$

Over the base $T^2=B\mathbb Z^2$ (nerve of $C=B\mathbb Z^2$), the proved **$\delta$-commutator lemma**
(`coupled-T2-general-delta-lemma`, file `2026-10-12-general-delta-commutator-lemma.md`) computes the
degree-$2$ connecting/lifting obstruction of *any* such extension $1\to A\to E\to Q\to1$ ($A$ abelian)
for a band $b:\mathbb Z^2\to Q$: with lifts $x,y\in E$ of $b(s),b(t)$,

$$\mathrm{obs}(b)=\big[\,[x,y]\,\big]\in H^2(T^2;A)=A\big/\big((\sigma-1)A+(\tau-1)A\big),\qquad
[x,y]=xyx^{-1}y^{-1}\in\ker(E\to Q)=A,$$

independent of lifts, where $\sigma,\tau$ are the $b$-twisted actions of $s,t$ on $A$. We instantiate it
on both extensions.

**Strictification end $(\Sigma)$.** Band $\rho:\mathbb Z^2\to\operatorname{Out}K$, lifts
$A,B\in\operatorname{Aut}K$:
$$\delta(\rho)=\big[[A,B]\big]\in H^2(T^2;\operatorname{Inn}K).$$

**Central end $(Z)$.** Here the coefficient is $A=Z(K)$ and the action is **trivial**: for $z\in Z(K)$
and any lift $k\in K$ of $\bar k\in\operatorname{Inn}K$, $\;\bar k\cdot z=kzk^{-1}=z$ (central). Hence
$(\sigma-1)Z(K)+(\tau-1)Z(K)=0$ and
$$H^2(T^2;Z(K))=Z(K)\quad(\text{trivial coefficients, no quotient}).$$
An **inner band** $\beta:\mathbb Z^2\to\operatorname{Inn}K$ (automatically valid: $\operatorname{Inn}K$
abelian $\Rightarrow$ any pair of images commutes) with lifts $k,k'\in K$ gives
$$[\mathfrak g]=\gamma(\beta)=\big[[k,k']\big]=[k,k']\in Z(K).$$
This is exactly the registry's **Face 2** central-extension lifting class (`lift-cocycle-derivation`,
proved), now read through the same lemma.

> **What "independence" means here.** $\delta$ and $[\mathfrak g]$ live in *different* coefficient
> groups ($\operatorname{Inn}K$ vs $Z(K)$) and arise from *different* band targets
> ($\operatorname{Out}K$ vs $\operatorname{Inn}K$); for a single physical gerbe the central stage is
> only reached *after* strictification succeeds. So the independence question is correctly posed at the
> level of the **group $K$**: *does $K$ admit a coupling band at each end?* — the four-corner
> cross-tabulation of the brief's Method. We decide that.

---

## 2. Two lemmas

### Lemma 1 (central end is universally obstructed)
*For $K$ finite of class $\le2$:* $\ [\mathfrak g]\neq0$ for some inner band $\iff K$ is nonabelian.

**Proof.** ($\Leftarrow$) $K$ nonabelian $\Rightarrow$ $\exists\,k,k'\in K$ with $[k,k']\neq1$. By class
$\le2$, $[k,k']\in[K,K]\subseteq Z(K)$, so $[k,k']\in Z(K)\setminus\{1\}$. Their images
$\bar k,\bar k'\in\operatorname{Inn}K$ commute (abelian), so $\beta:s\mapsto\bar k,\ t\mapsto\bar k'$ is a
band, and by §1 $\gamma(\beta)=[k,k']\neq0$ in $H^2(T^2;Z(K))=Z(K)$.
($\Rightarrow$) If $K$ abelian then $[k,k']=1$ for all $k,k'$, so $\gamma(\beta)=0$ for every band. $\;\square$

### Lemma 2 (strictification end needs a nonabelian group)
*For any finite $K$:* $\ \delta(\rho)\neq0$ for some band $\rho\ \Rightarrow\ K$ is nonabelian.

**Proof.** Contrapositive. If $K$ is abelian then $\operatorname{Inn}K=1$, so $(\Sigma)$ reads
$1\to1\to\operatorname{Aut}K\xrightarrow{=}\operatorname{Out}K\to1$: the kernel is trivial, every band
lifts uniquely, and $\delta\equiv0$ (the lemma gives $[A,B]\in\operatorname{Inn}K=1$). $\;\square$

---

## 3. Theorem (forced correlation)

> **Theorem.** Let $K$ be finite of nilpotency class $\le2$. Then
> $$\big[\ \exists\,\rho:\delta(\rho)\neq0\ \big]\ \Longrightarrow\ \big[\ \exists\,\beta:[\mathfrak g]=\gamma(\beta)\neq0\ \big].$$
> Equivalently, the corner $(\delta\text{ couples},\ [\mathfrak g]=0\ \text{for all bands})$ is **empty**.
> The implication is **strict**: its converse fails — $K=D_4$ has $[\mathfrak g]\neq0$ but
> $\delta\equiv0$.

**Proof.** If $\delta(\rho)\neq0$ for some $\rho$, Lemma 2 gives $K$ nonabelian, and then Lemma 1 gives a
band $\beta$ with $[\mathfrak g]=\gamma(\beta)\neq0$. Strictness: for $K=D_4$ (dihedral of order $8$,
class $2$), $\operatorname{Inn}D_4=(\mathbb Z/2)^2$, and the extension $(\Sigma)$,
$1\to(\mathbb Z/2)^2\to\operatorname{Aut}D_4\to\operatorname{Out}D_4\to1$ with
$\operatorname{Aut}D_4\cong D_4$, $\operatorname{Out}D_4\cong\mathbb Z/2$, **splits** — the order-$2$
automorphism $rs$ (outside the inner Klein four-subgroup $\{1,r^2,s,r^2s\}$ of $\operatorname{Aut}D_4$)
is a homomorphic section — so $\delta\equiv0$. Yet $D_4$ is nonabelian, so by Lemma 1
$[\mathfrak g]=[r,s]=r^2\neq0\in Z(D_4)$. $\;\blacksquare$

**The structural cause (the asymmetry).** The two "split?" questions underlying the brief's four corners
are *not* logically free:

* **$(Z)$ is non-split for every nonabelian class-$2$ $K$.** A splitting $\operatorname{Inn}K\to K$ would
  be a homomorphic section with image a complement $S$ to $Z(K)$; because $(Z)$ is **central**,
  $K=Z(K)\times S$ with $Z(K)$ and $S\cong\operatorname{Inn}K$ both abelian, forcing $K$ abelian — a
  contradiction. (Coupling is then supplied directly by Lemma 1, using the *trivial* center-action.)
* **$(\Sigma)$ can split** ($D_4,Q_8,\operatorname{Heis}(\mathbb F_3),M_{16},C_4\rtimes C_4$ all do),
  and split $(\Sigma)\Rightarrow\delta\equiv0$ (a homomorphic section $\theta:\operatorname{Out}K\to\operatorname{Aut}K$
  turns any band $\rho$ into a homomorphic lift $\theta\rho$).

So the column "$(Z)$ splits" of the cross-tabulation contains **only abelian groups**; the central end is
forced on for all nonabelian $K$, while the strictification end is free. That collapse of one column *is*
the forced correlation.

---

## 4. Computational cross-tabulation (`[computed]`, confirmatory)

`scratch/2026-10-13-two-ends-crosstab.py` computes, for each battery group: $|Z|,|\operatorname{Aut}|,
|\operatorname{Inn}|,|\operatorname{Out}|$; whether $\operatorname{Inn}K$ is abelian (class $\le2$);
whether $(\Sigma)$ splits and whether it $\delta$-couples (exhaustive search for a commuting outer pair
with no commuting lift — `witness_search`); whether $(Z)$ splits and whether it $[\mathfrak g]$-couples.

| $K$ | class $\le2$? | $(\Sigma)$ split | $\delta$ couples | $(Z)$ split | $[\mathfrak g]$ couples |
|---|---|---|---|---|---|
| $D_4$ | yes | **yes** | no | no | **yes** |
| $Q_8$ | yes | yes | no | no | yes |
| $\operatorname{Heis}(\mathbb F_3)$ | yes | yes | no | no | yes |
| $M_{16}$ | yes | yes | no | no | yes |
| $C_4\rtimes C_4$ | yes | yes | no | no | yes |
| $\boxed{D_4\times C_2}$ | yes | no | **yes (30)** | no | yes |
| $\boxed{Q_8\times C_2}$ | yes | no | **yes (54)** | no | yes |
| $SD_{16},\,D_{16}$ | **no** ($\operatorname{Inn}$ nonab.) | — | no | no | (nonab.) |
| $C_4,\ (\mathbb Z/2)^2$ (abelian) | yes | yes | no | **yes** | no |

**Four corners** $(\delta\text{ couples})\times([\mathfrak g]\text{ couples})$:

* $(\text{yes},\text{yes})$: $D_4\times C_2,\ Q_8\times C_2$.
* $(\text{yes},\text{no})$: **EMPTY** — the forced-correlation corner. ✓
* $(\text{no},\text{yes})$: $D_4,Q_8,\operatorname{Heis}(\mathbb F_3),M_{16},C_4\rtimes C_4$ (every
  split-$(\Sigma)$ nonabelian class-$2$ group).
* $(\text{no},\text{no})$: abelian $K$ only (vacuous).

Every nonabelian row has $(Z)$ non-split and $[\mathfrak g]$ coupling; every abelian row has $(Z)$ split
and no coupling — exactly Lemmas 1–2. The decisive $(\text{yes},\text{no})$ corner is empty, confirming
the Theorem. ($SD_{16},D_{16}$ are included to mark the boundary: $\operatorname{Inn}$ is nonabelian
there — class $3$ — so the $\delta$-end is **outside** the clean ordinary-$H^2$ domain; they still show
no violation, but the theorem is not claimed for them.)

---

## 5. Verification (hostile-referee pass)

* **§1 central-end identification — GREEN.** Trivial center-action is immediate ($z$ central). The lemma
  applies verbatim to any abelian-kernel extension; $(Z)$ qualifies with $A=Z(K)$. $H^2(T^2;Z(K))=Z(K)$
  for trivial coefficients is standard ($T^2=K(\mathbb Z^2,1)$, $H^2(\mathbb Z^2;M)=M$). The class is the
  bare commutator — matches `lift-cocycle-derivation` [proved] and the $D_4$ arithmetic $[r,s]=r^2$.
* **Lemma 1 — GREEN.** Class $\le2$ is used exactly once and essentially: to land $[k,k']$ in $Z(K)$.
  Without it $[k,k']$ need not be central and the inner-band obstruction is not defined by this formula —
  this is why the theorem's domain is class $\le2$, not accidental.
* **Lemma 2 — GREEN.** Elementary; $\operatorname{Inn}K=1\Rightarrow\delta\equiv0$.
* **Theorem — GREEN.** Pure composition of the two lemmas; the empty corner is their conjunction. The
  structural-cause paragraph (central ext of nonabelian class-$2$ group never splits) is an independent
  elementary check, and matches $(Z)$-split$=$False on every nonabelian computed row.
* **Strictness witness $D_4$ — GREEN.** $\operatorname{Aut}D_4\cong D_4$ splits over the inner Klein four
  via the order-$2$ element $rs$; verified by the engine ($\Sigma$ split$=$True, $\delta$-couple$=$False)
  and by hand. $D_4$ is the dihedral $4\mid n$ instance at $n=4$ the brief flagged.
* **Boundary/degenerate cases — GREEN.** Abelian $K$: both ends trivial (corner $(\text{no},\text{no})$).
  Rank-$1$ base $S^1$: $H^2(S^1;-)=0$, both ends vanish, no content (consistent). Trivial band:
  commutator $=0$, both obstructions $0$.
* **Scope honesty — GREEN.** $SD_{16},D_{16}$ (and dihedral $D_n$, $4\mid n$, $n>4$) have
  $\operatorname{Inn}$ nonabelian: *outside* the clean domain, explicitly excluded, no claim made.

**No RED, no YELLOW.**

---

## 6. Scope and (non-)gaps

* **Domain = class $\le2$, and this is the natural maximal domain.** Both obstructions are ordinary
  abelian $H^2$ *precisely* when $\operatorname{Inn}K$ is abelian (class $\le2$): then $\delta\in
  H^2(T^2;\operatorname{Inn}K)$ and $(Z)$ is a genuine central extension with $[k,k']\in Z(K)$. Outside it
  the $\delta$-end becomes nonabelian-$H^2$ (Giraud/Eilenberg–MacLane) and the central-end formula needs
  the commuting-in-$\operatorname{Inn}$ caveat; the clean correlation statement is not claimed there and is
  the one honest open edge (the dihedral $D_n$, $4\mid n$, $n\ge8$ family lives here — `[computed]` rows
  show no violation but the framework is only heuristic).
* **Grade.** The **Theorem (forced correlation) is `proved`** — it rests only on the `proved`
  $\delta$-commutator lemma and two elementary lemmas. The **battery cross-tabulation is `computed`** over
  the enumerated family (not a census of all groups of each order; minimality is not claimed), per
  standing grade discipline.
* **Not inflated.** The claim is a one-directional implication with a strict counterexample to its
  converse, *not* a biconditional and *not* a census theorem. The decisive content is the forced-empty
  corner plus its structural cause (the $(Z)$-split column is abelian-only).

---

### One-line summary

On $T^2$, the strictification obstruction $\delta\in H^2(T^2;\operatorname{Inn}K)$ and the central
obstruction $[\mathfrak g]\in H^2(T^2;Z(K))$ of a class-$\le2$ inventory gerbe are **not independent**:
$\delta$-coupling forces $K$ nonabelian, and every nonabelian class-$2$ group has $[\mathfrak g]\neq0$
(central extension non-split, trivial center-action), so $\delta\neq0\Rightarrow[\mathfrak g]\neq0$ —
a **strict one-way forced correlation (B)**; the converse fails at $K=D_4$ ($[\mathfrak g]\neq0$,
$\delta\equiv0$, the dihedral $4\mid n$ witness), and the corner $(\delta\neq0,[\mathfrak g]=0)$ is
forced empty.
