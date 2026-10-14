# Is the $T^2$ connecting map $\delta$ additive in the band? — the master cross-term formula, the quadratic law, and the additivity dichotomy

**Date:** 2026-10-13 · **Session:** deep-work `/prove`
**Registry:** `supply-chain-inventory-gerbe-h2.json`, new node `delta-additive-in-band`
(child of `coupled-T2-general-delta-lemma` **[proved]** and `gerbe-two-ends-correlation` **[proved]**).
**Script:** `scratch/2026-10-13-delta-additivity.py` (verification on the two $T^2$ couplers
$D_4\times C_2$, $Q_8\times C_2$; **0 violations** on every clause below).

---

## 0. The question and the answer

Fix base $C=B(\mathbb Z^2)$ (nerve $T^2$) and a structure group $K$ of nilpotency class $\le2$, so
$M:=\operatorname{Inn}K$ is abelian. By the **general $\delta$-commutator lemma**
(`coupled-T2-general-delta-lemma`, proved 2026-10-12), a band $\rho:\mathbb Z^2\to\operatorname{Out}K$
— i.e. a commuting pair $\bar A:=\rho(s),\ \bar B:=\rho(t)\in\operatorname{Out}K$ — has connecting class

$$\delta(\rho)=[\,[A,B]\,]\in H^2(T^2;M)=M_{\mathbb Z^2}=M\big/\big((\sigma-1)M+(\tau-1)M\big),$$

where $A,B\in\operatorname{Aut}K$ are **any** lifts of $\bar A,\bar B$ and $\sigma=\bar A\cdot(-),\
\tau=\bar B\cdot(-)$ are the induced actions of $\bar A,\bar B$ on $M$ by conjugation.

Let $\rho_1,\rho_2$ be two bands landing in a **common abelian subgroup**
$\bar{\mathcal A}\le\operatorname{Out}K$ (the concrete meaning of "a common system of commuting
lifts": their pointwise product $\rho_1\rho_2=(\bar A_1\bar A_2,\ \bar B_1\bar B_2)$ is again a band into
$\bar{\mathcal A}$, because $\bar{\mathcal A}$ is abelian). **Is $\delta(\rho_1\rho_2)=\delta(\rho_1)+\delta(\rho_2)$?**

> **Answer: (B) — No. $\delta$ is not a homomorphism.** The exact defect is governed by the
> **master cross-term formula** (Theorem 1), an on-the-nose identity in $\operatorname{Inn}K$:
> $$[A_1A_2,\,B_1B_2]\;=\;\underbrace{[A_1,B_1]}_{=\,\delta(\rho_1)\text{ rep}}
> \;+\;(\sigma_1\tau_1)\!\cdot\![A_2,B_2]\;+\;\sigma_1\!\cdot\![A_2,B_1]\;+\;\tau_1\!\cdot\![A_1,B_2].$$
> On the **trivial-action locus** $\operatorname{Out}^0=\ker(\operatorname{Out}K\to\operatorname{Aut}M)$
> — where the question is even well-typed, all three classes living in the *same* group $M$ — this
> collapses (Theorem 2) to
> $$\boxed{\;\delta(\rho_1\rho_2)=\delta(\rho_1)+\delta(\rho_2)+\chi(\rho_1,\rho_2),\qquad
> \chi(\rho_1,\rho_2)=[A_1,B_2]+[A_2,B_1]\in M\;}$$
> with $\chi$ a **symmetric bi-additive** form — the polarization of the quadratic map $\delta$,
> which obeys $\delta(\rho^n)=n^2\,\delta(\rho)$. And then the **dichotomy** (Theorem 3): on any abelian
> $\bar{\mathcal A}\subseteq\operatorname{Out}^0$,
> $$\delta\text{ is additive on bands into }\bar{\mathcal A}\iff\delta\equiv0\text{ there}\iff
> \pi^{-1}(\bar{\mathcal A})\le\operatorname{Aut}K\text{ is abelian}.$$
> **There is no abelian subgroup on which $\delta$ is a nonzero homomorphism.** A coupled torus is
> *always* a witness to non-additivity.

So the butterfly §7 open edge "composite weld obstruction $=$ composite of waist classes?" resolves in
the negative, in the sharpest possible form: the waist class $\delta$ is a **quadratic refinement**,
not a homomorphism, on the composition monoid of bands; its polar form $\chi$ is the obstruction to
additivity, and $\chi$ vanishes exactly when $\delta$ itself does.

---

## 1. The master cross-term formula (general; proved)

Throughout, $M=\operatorname{Inn}K\trianglelefteq\operatorname{Aut}K$ is abelian (class $\le2$),
written additively, and for $X\in\operatorname{Aut}K,\ m\in M$ we write $X\cdot m:=XmX^{-1}\in M$
($M$ normal); this factors through $\pi(X)\in\operatorname{Out}K$. For a band $\rho_i$ fix lifts
$A_i,B_i\in\operatorname{Aut}K$ of $\rho_i(s),\rho_i(t)$ and set $\sigma_i:=\rho_i(s)\cdot(-)$,
$\tau_i:=\rho_i(t)\cdot(-)\in\operatorname{Aut}(M)$.

> **Theorem 1 (master cross-term formula).** Let $K$ be finite of class $\le2$ and let
> $\rho_1,\rho_2$ be bands with all four outer classes $\bar A_1,\bar B_1,\bar A_2,\bar B_2$ in a common
> abelian subgroup of $\operatorname{Out}K$. Then every pairwise commutator
> $[A_i,B_j]$ lies in $M$, and, additively in $M$,
> $$[A_1A_2,\,B_1B_2]=[A_1,B_1]+(\sigma_1\tau_1)\!\cdot\![A_2,B_2]+\sigma_1\!\cdot\![A_2,B_1]+\tau_1\!\cdot\![A_1,B_2].\tag{$\star$}$$
> Since $A_1A_2,\,B_1B_2$ are lifts of $(\rho_1\rho_2)(s),(\rho_1\rho_2)(t)$, the left side represents
> $\delta(\rho_1\rho_2)\in M_{\mathbb Z^2}$ (coinvariants for the product action $\sigma_1\sigma_2,\tau_1\tau_2$).

**Proof.** Membership: $\pi[A_i,B_j]=[\bar A_i,\bar B_j]=1$ because $\bar A_i,\bar B_j$ commute (common
abelian subgroup), so $[A_i,B_j]\in\ker\pi=M$. Use the universal commutator identities
$$[xy,z]=x[y,z]x^{-1}\cdot[x,z],\qquad [x,yz]=[x,y]\cdot y[x,z]y^{-1}.$$
Apply the first with $x=A_1,y=A_2,z=B_1B_2$:
$$[A_1A_2,B_1B_2]=A_1[A_2,B_1B_2]A_1^{-1}\cdot[A_1,B_1B_2].$$
Apply the second to each factor:
$$[A_2,B_1B_2]=[A_2,B_1]\cdot B_1[A_2,B_2]B_1^{-1},\qquad
[A_1,B_1B_2]=[A_1,B_1]\cdot B_1[A_1,B_2]B_1^{-1}.$$
Substituting and conjugating the first bracket by $A_1$:
$$[A_1A_2,B_1B_2]=\big(A_1[A_2,B_1]A_1^{-1}\big)\cdot\big(A_1B_1[A_2,B_2]B_1^{-1}A_1^{-1}\big)\cdot[A_1,B_1]\cdot\big(B_1[A_1,B_2]B_1^{-1}\big).$$
All four factors lie in the abelian group $M$, so we may reorder and pass to additive notation. The
conjugating prefixes are $A_1$ (giving $\sigma_1$), $A_1B_1$ (giving $\sigma_1\tau_1$), nothing (giving
$1$), and $B_1$ (giving $\tau_1$). This is exactly $(\star)$. $\qquad\blacksquare$

**Verification.** `scratch/2026-10-13-delta-additivity.py`, clause `[GEN]`: $(\star)$ holds **on the
nose in $\operatorname{Inn}K$** over *all* quadruples of bands inside a common abelian subgroup —
$8113$ checks for $D_4\times C_2$ and $26037$ for $Q_8\times C_2$, **$0$ violations**. (An earlier run
comparing against the representative lift of the *product coset* showed spurious "violations"; those are
precisely coboundaries $(\sigma-1)M+(\tau-1)M$ — the product-coset representative differs from $A_1A_2$
by an inner automorphism — and vanish in $M_{\mathbb Z^2}$. Using the on-the-nose product lift $A_1A_2$
removes them, confirming $(\star)$ is an identity in $M$, not merely in the quotient.)

**Reading of $(\star)$.** Beyond the two "diagonal" terms $\delta(\rho_1),\delta(\rho_2)$ there are:
a **twist** $(\sigma_1\tau_1)$ acting on $\delta(\rho_2)$'s representative, and the two **cross terms**
$\sigma_1[A_2,B_1]+\tau_1[A_1,B_2]$. Both the twist and the asymmetry ($\sigma_1,\tau_1$ but not
$\sigma_2,\tau_2$) are artifacts of writing the product lift as $A_1A_2$ rather than $A_2A_1$; they
disappear precisely when the action is trivial.

---

## 2. The trivial-action locus: $\delta$ is a quadratic map (proved)

**Definition.** $\operatorname{Out}^0:=\ker\!\big(\operatorname{Out}K\to\operatorname{Aut}(M)\big)$ is
the subgroup of outer classes acting trivially on $M=\operatorname{Inn}K$. A band $\rho$ is
**trivial-action** iff $\bar A,\bar B\in\operatorname{Out}^0$, i.e. $\sigma=\tau=\mathrm{id}$.

*(Terminology.* The PROVE brief's "trivial centre-action" is here made precise as the action relevant to
$\delta$: trivial action of $\operatorname{Out}K$ on the coefficient module $M=\operatorname{Inn}K$ — the
exact condition under which $\delta$'s receptacle $M_{\mathbb Z^2}$ collapses to $M$ and the additivity
question becomes well-typed. For class-$\le2$ $K$ this is also the condition making the restricted
extension $(\ast)|_{\operatorname{Out}^0}$ central, below. We do **not** silently conflate it with the
distinct condition "$\operatorname{Out}K$ acts trivially on $Z(K)$"; the relevant module for the waist
class is $\operatorname{Inn}K$, not $Z(K)$.)*

Over $\operatorname{Out}^0$ the restricted extension
$1\to M\to\operatorname{Aut}^0K\to\operatorname{Out}^0\to1$ (with $\operatorname{Aut}^0K:=\pi^{-1}(\operatorname{Out}^0)$)
is a **central** extension: $M$ is central in $\operatorname{Aut}^0K$ (verified: clause `restricted (*)
central: True` for both couplers). For such a central extension the **commutator pairing**
$$c:\{\text{commuting pairs in }\operatorname{Out}^0\}\to M,\qquad c(\bar x,\bar y):=[\tilde x,\tilde y]$$
is well defined (lift-independent: for central $u,v\in M$, $[\tilde xu,\tilde yv]=[\tilde x,\tilde y]$)
and $\delta(\rho)=c(\rho(s),\rho(t))$ for trivial-action bands, with $M_{\mathbb Z^2}=M$ (no coboundaries).

**Lemma 2.1 ($c$ is alternating and bi-multiplicative).** On commuting pairs in $\operatorname{Out}^0$:
$c(\bar x,\bar x)=0$; $c(\bar y,\bar x)=-c(\bar x,\bar y)$; and whenever all pairs in sight commute,
$$c(\bar x\bar y,\bar z)=c(\bar x,\bar z)+c(\bar y,\bar z),\qquad c(\bar x,\bar y\bar z)=c(\bar x,\bar y)+c(\bar x,\bar z).$$
*Proof.* Alternating/antisymmetry are immediate from $[\tilde x,\tilde x]=1$,
$[\tilde y,\tilde x]=[\tilde x,\tilde y]^{-1}$. For bi-multiplicativity,
$[\tilde x\tilde y,\tilde z]=\tilde x[\tilde y,\tilde z]\tilde x^{-1}\,[\tilde x,\tilde z]
=[\tilde y,\tilde z][\tilde x,\tilde z]$, using that $[\tilde y,\tilde z]\in M$ is **central**
(this is exactly the trivial-action hypothesis). $\qquad\square$ (Clause `(2) bi-mult on Out^0`: $0$
violations; and `(2)` over *all* of $\operatorname{Out}$ **fails** — $112/1408$ and $962/4032$
violations — confirming centrality is essential.)

> **Theorem 2 (quadratic law + cross term).** For trivial-action bands $\rho_1,\rho_2$ into a common
> abelian $\bar{\mathcal A}\subseteq\operatorname{Out}^0$, equality holds in $M$:
> $$\delta(\rho_1\rho_2)=\delta(\rho_1)+\delta(\rho_2)+\chi(\rho_1,\rho_2),\qquad
> \chi(\rho_1,\rho_2)=c(\bar A_1,\bar B_2)+c(\bar A_2,\bar B_1)=[A_1,B_2]+[A_2,B_1].$$
> $\chi$ is symmetric ($\chi(\rho_1,\rho_2)=\chi(\rho_2,\rho_1)$) and bi-additive; $\delta$ is a
> **quadratic map** $\operatorname{Hom}(\mathbb Z^2,\bar{\mathcal A})\cong\bar{\mathcal A}\times\bar{\mathcal A}\to M$
> with polar form $\chi$, and in particular $\delta(\rho^n)=n^2\,\delta(\rho)$ and $\delta(\rho^{-1})=\delta(\rho)$.

**Proof.** Either specialize $(\star)$ to $\sigma_1=\tau_1=\mathrm{id}$, or compute directly with
Lemma 2.1:
$$\delta(\rho_1\rho_2)=c(\bar A_1\bar A_2,\bar B_1\bar B_2)
=c(\bar A_1,\bar B_1)+c(\bar A_1,\bar B_2)+c(\bar A_2,\bar B_1)+c(\bar A_2,\bar B_2)
=\delta(\rho_1)+\delta(\rho_2)+\chi.$$
Symmetry of $\chi$ is visible; bi-additivity is bi-multiplicativity of $c$. Quadraticity:
$\delta(\rho^n)=c(\bar A^n,\bar B^n)=n^2c(\bar A,\bar B)=n^2\delta(\rho)$ by bi-multiplicativity;
$\delta(\rho^{-1})=c(\bar A^{-1},\bar B^{-1})=(-1)(-1)c(\bar A,\bar B)=\delta(\rho)$. $\qquad\blacksquare$

**Verification.** Clause `(3) cross-term on Out^0` ($1905$ checks each) and `(4) quadratic` ($320$
checks each, $n\le6$): **$0$ violations** on both couplers.

---

## 3. The additivity dichotomy (proved)

> **Theorem 3 (dichotomy).** Let $\bar{\mathcal A}\subseteq\operatorname{Out}^0$ be abelian. The following
> are equivalent:
> 1. $\delta$ is a group homomorphism on $\operatorname{Hom}(\mathbb Z^2,\bar{\mathcal A})$ (additivity);
> 2. $\delta\equiv0$ on all bands into $\bar{\mathcal A}$;
> 3. $c|_{\bar{\mathcal A}\times\bar{\mathcal A}}\equiv0$;
> 4. $\pi^{-1}(\bar{\mathcal A})\le\operatorname{Aut}K$ is abelian (i.e. $\bar{\mathcal A}$ has a system
>    of commuting lifts).
>
> In particular $\delta$ is **never a nonzero homomorphism** on any abelian subgroup.

**Proof.** $(2)\Rightarrow(1)$ trivial. $(1)\Rightarrow(3)$: additivity forces $\chi\equiv0$; take
$\rho_1=(\bar x,1),\rho_2=(1,\bar y)$, so $\delta(\rho_1)=c(\bar x,1)=0$, $\delta(\rho_2)=c(1,\bar y)=0$,
while $\rho_1\rho_2=(\bar x,\bar y)$ gives $\delta(\rho_1\rho_2)=c(\bar x,\bar y)$; additivity makes this
$0$ for all $\bar x,\bar y\in\bar{\mathcal A}$. $(3)\Rightarrow(2)$: $\delta(\rho)=c(\bar A,\bar B)=0$.
$(3)\Leftrightarrow(4)$: $\pi^{-1}(\bar{\mathcal A})$ is a central extension of the abelian
$\bar{\mathcal A}$ by $M$, hence abelian iff its commutator pairing $c|_{\bar{\mathcal A}}$ vanishes.
$\qquad\blacksquare$

**Verification.** Clause `(5) dichotomy on Out^0`: among the $6$ coupled abelian subgroups of
$\operatorname{Out}^0$ (for each coupler), the count `nonzero & ADDITIVE` is **$0$**; every coupled
subgroup is non-additive. Exhaustive over $\le2$-generated abelian subgroups (which suffices, bands
being rank $\le2$).

**Reconciliation with the coupling criterion.** $(4)$ is the negation of the $\delta$-lemma's coupling
criterion "$\exists$ commuting outer pair with no commuting lift." So Theorem 3 says:
$$\bar{\mathcal A}\text{ couples (some band has }\delta\neq0)\iff\pi^{-1}(\bar{\mathcal A})\text{ nonabelian}
\iff\delta\text{ is non-additive on }\bar{\mathcal A}.$$
Coupling, non-splitting of $\pi^{-1}(\bar{\mathcal A})$, and non-additivity of the waist class are
**one and the same phenomenon**.

---

## 4. Scope, and the genuinely twisted regime (honest gap statement)

The clean additivity package (Theorems 2–3) lives on the **trivial-action locus** $\operatorname{Out}^0$,
and this is not a cosmetic restriction but the precise place the question is **well-typed**: for bands
with differing actions, $\delta(\rho_1),\delta(\rho_2),\delta(\rho_1\rho_2)$ lie in *different*
coinvariant quotients $M_{(\sigma,\tau)}$, so "$\delta(\rho_1\rho_2)=\delta(\rho_1)+\delta(\rho_2)$" is
not even a statement about one group until a common receptacle is chosen.

**Coupling is *not* confined to $\operatorname{Out}^0$.** The census (`coupling vs action`) finds
coupled bands ($\delta\neq0$ in the quotient) with **nontrivial** action: $24$ of $60$ for
$D_4\times C_2$, $72$ of $108$ for $Q_8\times C_2$. For these, the governing statement is the master
formula $(\star)$ alone — a correct on-the-nose identity in $\operatorname{Inn}K$ whose descent to any
common coinvariant quotient $M_{\langle\sigma_1,\tau_1,\sigma_2,\tau_2\rangle}$ still carries the twist
$(\sigma_1\tau_1)$ on the $\delta(\rho_2)$ term. So:

* **No gap in the posed question.** The question fixes trivial centre-action; there the answer is
  complete and proved: (B), with $\chi=[A_1,B_2]+[A_2,B_1]$, quadratic law, dichotomy.
* **Deliberately-left edge (not a gap in the theorem):** a *common-receptacle* additivity theorem for
  bands of differing nontrivial action. The master formula shows the obstruction is the twist
  $(\sigma_1\tau_1-1)\!\cdot\!\delta(\rho_2)$ plus the twisted cross terms; packaging this as a genuine
  cocycle identity on $T^2$ (a cup-product / Baer-sum statement over the full banded gerbe) is the next
  node, explicitly deferred behind the mini-course per the PROVE brief. It does **not** affect Theorems
  1–3.

---

## 5. Verification summary (hostile-referee pass)

All on `scratch/2026-10-13-delta-additivity.py`, couplers $D_4\times C_2$ ($|\!\operatorname{Out}|=16$),
$Q_8\times C_2$ ($|\!\operatorname{Out}|=48$):

| clause | statement | checks (D4×C2 / Q8×C2) | violations |
|---|---|---|---|
| `[GEN]` | master formula $(\star)$ on-the-nose in $M$ | 8113 / 26037 | **0 / 0** |
| central | $(\ast)$ restricted to $\operatorname{Out}^0$ is central | — | True / True |
| `(2)` | $c$ bi-multiplicative on $\operatorname{Out}^0$ | 512 / 512 | **0 / 0** |
| `(2)` over all $\operatorname{Out}$ | bi-multiplicativity **fails** off $\operatorname{Out}^0$ | 1408 / 4032 | 112 / 962 *(expected)* |
| `(3)` | $\delta(\rho_1\rho_2)=\delta_1+\delta_2+\chi$ on $\operatorname{Out}^0$ | 1905 / 1905 | **0 / 0** |
| `(4)` | $\delta(\rho^n)=n^2\delta(\rho)$ on $\operatorname{Out}^0$ | 320 / 320 | **0 / 0** |
| `(5)` | dichotomy: nonzero $\&$ additive | 6 coupled subs each | **0 / 0** |

* **Theorem 1 — GREEN** (hand proof from universal commutator identities + $M$ abelian; computed
  confirmation $0$ violations). The only hypotheses are class $\le2$ and common abelian subgroup.
* **Theorems 2–3 — GREEN** (two-line proofs from the central commutator pairing; computed confirmation).
* **Boundary cases.** Trivial band $\rho=1$: $\chi(1,\rho)=c(1,\bar B)+c(\bar A,1)=0$, additive ✓.
  $\rho_1=\rho_2$: $\chi(\rho,\rho)=2c(\bar A,\bar B)=2\delta(\rho)$, consistent with
  $\delta(\rho^2)=4\delta(\rho)$ ✓.
* **No RED. No YELLOW** inside the stated scope; the twisted edge of §4 is flagged and is not part of
  the posed question.

---

## 6. Grant / program placement

This is the **composition-monoid structure of the waist class**. The butterfly/weak-morphism arc asked
whether the weld obstruction composes additively; the answer sharpens the whole gerbe lane:

* **Theory.** The waist class $\delta$ is a **quadratic refinement** on the band composition monoid, with
  explicit polar form $\chi$ = the commutator pairing of the central extension
  $\operatorname{Aut}^0K$. This is the $T^2$ counterpart of the floor $D_1/D_2$ dichotomy
  ([[floor-d1-d2-dichotomy-proved]]) and of the two-ends forced correlation
  ([[two-gerbe-ends-forced-correlation]]): "coupling $=$ nonabelian lift $=$ non-additivity" is a single
  statement.
* **Applications.** For orchestration/ZS welds ([[orchestration-is-zappa-szep-weld]]), composing two
  welds does **not** add their obstruction classes; the correction $\chi$ is an economically real
  interaction term (the "cross-coupling" of two independently-welded subsystems). Additivity holds iff
  each subsystem is individually uncoupled.
* **Formalisation.** Theorem 1's identity $(\star)$ and Lemma 2.1 are finite, decidable, and a natural
  Lean target over the existing $\operatorname{Inn}/\operatorname{Out}$ engine.

### One-line summary
On $T^2$ the band-to-waist connecting map is a **quadratic map**, not a homomorphism: in general
$[A_1A_2,B_1B_2]=[A_1,B_1]+(\sigma_1\tau_1)[A_2,B_2]+\sigma_1[A_2,B_1]+\tau_1[A_1,B_2]$, which on the
trivial-action locus reads $\delta(\rho_1\rho_2)=\delta(\rho_1)+\delta(\rho_2)+\big([A_1,B_2]+[A_2,B_1]\big)$
with symmetric bi-additive polar form $\chi$; and $\delta$ is additive on an abelian subgroup **iff** it
is identically zero there — a coupled torus is always a witness to non-additivity.
