# Non-transverse Ext towers over $k V_4$, char 2

**Group** $G = V_4 = \mathbb{Z}/2 \times \mathbb{Z}/2$, $k = \mathbb{F}_2$,
$kG = \mathbb{F}_2[a,b]/(a^2{-}1, b^2{-}1) \cong \mathbb{F}_2[x,y]/(x^2,y^2)$ with
$x = a{-}1$, $y = b{-}1$ (a local ring; unique simple $k$).

**Task.** Compute $\operatorname{Ext}^n_{kG}(k[G/A], k[G/B])$ for $n = 0..6$ as
$\mathbb{F}_2$-dimensions, by an explicit minimal free resolution of $k[G/A]$ over
$kG$, then $\operatorname{Hom}_{kG}(-,\,k[G/B])$, then cohomology, all mod 2.
Cross-check against Mackey/Shapiro. This is the **non-transverse** sequel to the
transverse case (which gave $[1,0,0,0,0,0,0]$).

**Reproduce:** `python3 ext_engine.py` in this directory.

## Machinery reused

The heavy lifting reuses the **verified** $V_4$ homological-algebra engine from
`/home/agent/projects/scratch/rick-v4-ext2/`:

- `f2lib.py` — exact $\mathbb{F}_2$ linear algebra (rref, rank, kernel, solve) and
  the $V_4$ group law (XOR of exponent bits).
- `modules.py` — minimal free resolution over $kV_4$ (`min_resolution`, via
  radical/`min_generators`), `Hom(P_\bullet, N)`, and `ext_tower`.

That engine was validated independently on $H^*(V_4;\mathbb{F}_2) = [1,2,3,4,5,6,7]$
and on the transverse case $[1,0,0,\dots]$; here I re-confirm both as cases (v)/(iv).
This file (`ext_engine.py`) adds: permutation-module construction $k[G/H]$ for every
subgroup, the Mackey closed-form predictor, and the rank-variety computation. Nothing
in the core Ext computation was modified.

## The five towers — resolution vs Mackey, side by side

Mackey/Shapiro: $\operatorname{Ext}^n_{kG}(k[G/A],k[G/B]) \cong
\bigoplus_{g\in A\backslash G/B} H^n(A \cap gBg^{-1};k)$. Since $G$ is abelian,
$gBg^{-1}=B$, so every double coset contributes $H^n(A\cap B;k)$ and there are
$|A\backslash G/B| = |G|\,|A\cap B|/(|A|\,|B|)$ of them. In char 2,
$H^n(\mathbb{Z}/2;\mathbb{F}_2)=\mathbb{F}_2$ for all $n$ (dim 1);
$H^n(\{e\})=[1,0,0,\dots]$; $H^n(V_4)=[1,2,3,4,5,6,7]$ (Poincaré series $1/(1-t)^2$).

| Case | $A$ | $B$ | $A\cap B$ | $\#(A\backslash G/B)$ | Ext (resolution) | Ext (Mackey) | agree |
|------|-----|-----|-----------|------|------------------|--------------|-------|
| (i)   | $\langle a\rangle$ | $\langle a\rangle$ | $\langle a\rangle$ (ord 2) | **2** | $[2,2,2,2,2,2,2]$ | $[2,2,2,2,2,2,2]$ | ✓ |
| (ii)  | $\langle a\rangle$ | $G$ | $\langle a\rangle$ (ord 2) | 1 | $[1,1,1,1,1,1,1]$ | $[1,1,1,1,1,1,1]$ | ✓ |
| (iii) | $G$ | $\langle a\rangle$ | $\langle a\rangle$ (ord 2) | 1 | $[1,1,1,1,1,1,1]$ | $[1,1,1,1,1,1,1]$ | ✓ |
| (iv)  | $\langle a\rangle$ | $\langle b\rangle$ | $\{e\}$ | 1 | $[1,0,0,0,0,0,0]$ | $[1,0,0,0,0,0,0]$ | ✓ |
| (v)   | $G$ | $G$ | $G$ (ord 4) | 1 | $[1,2,3,4,5,6,7]$ | $[1,2,3,4,5,6,7]$ | ✓ |

**All five agree in every degree $0..6$.** Case (v) reproduces $H^*(V_4)$ and case
(iv) reproduces the transverse control $[1,0,\dots]$, so the engine is trusted for
the genuinely new non-transverse cases (i)–(iii).

Betti numbers (free ranks of the minimal resolution of $k[G/A]$): $k[G/\langle a\rangle]$
has $[1,1,1,1,1,1,1,1]$ (eventually periodic — the module is $\Omega$-periodic, complexity 1);
$k[G/G]=k$ has $[1,2,3,4,5,6,7,8]$ (complexity 2).

## The dichotomy, stated crisply

> $\operatorname{Ext}^{\ge 1}_{kG}(k[G/A],k[G/B])$ **survives** iff $A\cap B \ne \{e\}$
> (non-transverse), and **vanishes identically** iff $A\cap B = \{e\}$ (transverse).

Precisely, the whole positive tower is governed by the single group $A\cap B$: it is
$\#(A\backslash G/B)$ copies of $H^{\ge 1}(A\cap B;k)$. Transverse $\Rightarrow$
$A\cap B=\{e\}\Rightarrow H^{\ge1}=0\Rightarrow[1,0,0,\dots]$. Non-transverse with
$A\cap B$ of order 2 gives a **constant** nonzero tower (periodicity/complexity 1);
$A\cap B=G$ gives the **linearly growing** tower $n+1$ (complexity 2). The dimension is
constant in $n$ exactly when $A\cap B$ is cyclic of order 2.

## Q1 — double-coset isolation (case (i), $A=B=\langle a\rangle$)

- **Number of double cosets.** $|\langle a\rangle\backslash G/\langle a\rangle| = 2$.
  Explicitly the two double cosets are $\langle a\rangle e\langle a\rangle = \{e,a\}$
  and $\langle a\rangle b\langle a\rangle = \{b,ab\}$.
- **Is the surviving class isolable to one coset, or intrinsically a sum?**
  It is **intrinsically a sum**. The Mackey isomorphism is a *direct sum*
  $\operatorname{Ext}^n \cong H^n(\langle a\rangle) \oplus H^n(\langle a\rangle)$,
  one summand per double coset, and **each of the two cosets carries an identical,
  full $H^\bullet(\langle a\rangle;k) = [1,1,1,\dots]$ tower.** The observed
  $\dim\operatorname{Ext}^n = 2$ is $1+1$, not a single distinguished class. Neither
  summand is preferred: the two are exchanged by the symmetry $b\cdot(-)$ that swaps the
  cosets $\{e,a\}\leftrightarrow\{b,ab\}$. So the class is **not** isolable to a single
  coset — the answer to Rick's question is "SUM over cosets, each carrying an identical
  $H^n(A\cap B)$ tower." The direct-sum *decomposition* is canonical (indexed by the
  cosets), but no individual summand is canonically singled out.

Contrast (ii)/(iii): there $\#(A\backslash G/B)=1$, so the surviving tower **is**
isolated in the unique coset — a single $H^n(\langle a\rangle)$ copy, dim 1 per degree.

## Q2 — support / rank variety (Quillen stratification)

Rank variety $V_r(M) = \{(\alpha:\beta)\in\mathbb{P}^1 : u=\alpha x+\beta y$ acts
**non-freely** on $M\}$. For $M$ of even dim, $u$ (with $u^2=0$) acts freely iff
$\operatorname{rank}(u|_M) = \dim M/2$.

**Computation for $M = k[G/\langle a\rangle]$ (dim 2).** On $M$, $a$ acts trivially, so
$x=a-1$ acts as the **zero matrix**; $b$ swaps the two cosets, so $y=b-1$ has rank 1.
Hence $u = \alpha x + \beta y = \beta\,(b-1)$ and
$$\operatorname{rank}(u|_M) = \operatorname{rank}(b-1)\cdot[\beta\ne 0] = 1\cdot[\beta\ne0].$$
So $u$ acts **freely iff $\beta\ne0$**, and **non-freely iff $\beta=0$** — and because
$x$ acts as the *literal* zero matrix, this is a parametric identity valid over
**every** field, not just the three $\mathbb{F}_2$-rational points. Therefore
$$\boxed{V_r(k[G/\langle a\rangle]) = \{(\alpha:\beta): \beta=0\} = \{(1{:}0)\}},$$
a **single point** of $\mathbb{P}^1$ — a **proper** (0-dimensional) subvariety, not the
full line. (For comparison the engine also confirms $V_r(k[G/\langle b\rangle])=\{(0{:}1)\}$,
$V_r(k)= $ all of $\mathbb{P}^1$, and $V_r(kG)=\varnothing$, i.e. $kG$ projective.)

**Is the surviving higher Ext detected on the full-rank locus or a finer stratum?**
On a **finer (proper) stratum.** The support of $\operatorname{Ext}^*_{kG}(M,N)$ is
$V_r(M)\cap V_r(N)$. For case (i), $M=N=k[G/\langle a\rangle]$, so the support is
$\{(1{:}0)\}\cap\{(1{:}0)\}=\{(1{:}0)\}$ — a single point, **not** the full $\mathbb{P}^1$.
The surviving class is **not** a top-stratum / full-support (complexity-2) class; it is a
**complexity-1** class supported entirely on the rank-1 stratum in the "$a$-direction"
$(1{:}0)$. This matches the homological data exactly: $\dim\operatorname{Ext}^n(M,M)=2$
is **constant** in $n$ (polynomial growth of degree 0 $\Rightarrow$ complexity 1
$\Rightarrow$ 0-dimensional projective support), and the resolution of $M$ is periodic
(Betti $[1,1,1,\dots]$).

**Why the dichotomy is a variety intersection.** This gives the clean geometric reading
of transverse vs non-transverse:

- **(iv) transverse:** $V_r(k[G/\langle a\rangle])=\{(1{:}0)\}$,
  $V_r(k[G/\langle b\rangle])=\{(0{:}1)\}$; the two points are **disjoint**, so
  $\operatorname{Ext}^{\ge1}$ has empty support $\Rightarrow$ vanishes $\Rightarrow[1,0,\dots]$.
- **(i) non-transverse:** both varieties are the **same** point $\{(1{:}0)\}$; the
  intersection is that point $\Rightarrow \operatorname{Ext}^{\ge1}\ne0$.

So the surviving Ext lives precisely where the two modules' rank varieties overlap, and
in case (i) that overlap is one point (the $\langle a\rangle$-direction), a proper
subvariety — a finer-than-top Quillen stratum.

## Caveats / honesty

- $\mathbb{F}_2$ has only 3 projective points on $\mathbb{P}^1$; a naive point-sampling
  cannot by itself certify a variety over $\overline{\mathbb{F}}_2$. For
  $k[G/\langle a\rangle]$ this gap is closed **rigorously** because $x$ acts as the exact
  zero matrix, making the rank a parametric function of $\beta$ alone (the boxed identity
  holds over any field). The point-samples for the other modules are consistent with the
  standard facts ($V_r(k)=\mathbb{P}^1$, $V_r(kG)=\varnothing$) but are stated as samples.
- The support-variety identity $V_r\!\big(\operatorname{Ext}^*(M,N)\big)=V_r(M)\cap V_r(N)$
  and the complexity $\leftrightarrow$ growth-rate correspondence are invoked from the
  standard theory (Carlson, Avrunin–Scott, Benson); they are not re-proved here, but the
  computed Ext dimensions are fully consistent with them.
- All Ext dimensions themselves are computed directly and exactly over $\mathbb{F}_2$ by
  the resolution, independent of any variety theory, and match the Mackey formula in every
  degree $0..6$.

## Files

- `ext_engine.py` — runnable; prints all five towers (both methods), agreement flag, and
  rank varieties.
- reused: `../rick-v4-ext2/f2lib.py`, `../rick-v4-ext2/modules.py`.
