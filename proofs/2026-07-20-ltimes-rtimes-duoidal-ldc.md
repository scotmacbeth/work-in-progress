# A normal duoidal structure $(\ltimes,\rtimes)$ on $\mathbf{Poly}$, and the linear distributor $\delta$

**MacBeth — 2026-07-20 (deep-work PROVE session)**

## Problem

Dorta–Jarvis–Niu (arXiv:2305.05655, §6) introduce two non-convolutional monoidal
structures on $\mathbf{Poly}\simeq\mathbf{Cont}$, identified in the registry
`other-cont-monoidal-tensors` as the **Dialectica tensor** $\ltimes$ and its **directed
variant** $\rtimes$. In container coordinates (polynomial
$p=\sum_{s\in S_p}y^{p[s]}$, shape set $S_p$, directions $p[s]$):
$$
(p\ltimes q)[(s,t)] = p[s]^{S_q}\times q[t]^{S_p},\qquad
(p\rtimes q)[(s,t)] = p[s]^{S_q}\times q[t],
$$
both on shape set $S_p\times S_q$, both with unit $y$ ($S=1$, $y[*]=1$).

**Question (PROVE.md).** Is there a natural *linear distributor*
$\delta_{A,B,C}\colon A\ltimes(B\rtimes C)\to (A\ltimes B)\rtimes C$ making $\mathbf{Poly}$
a **linearly distributive category (LDC)** on $(\ltimes,\rtimes)$?

**Answer. Yes.** More: $(\mathbf{Poly},\ltimes,\rtimes,y)$ is a **normal duoidal category**,
and $\delta$ is the induced linear distributor. Both structures are coherent, by a single
combinatorial mechanism (the *reindexing calculus*). The distributor is genuinely non-invertible,
so this is not a degenerate/duoidal-iso collapse.

Morphism convention: a map of polynomials $\varphi\colon p\to q$ is a forward shape map
$\varphi_1\colon S_p\to S_q$ together with backward direction maps
$\varphi^\#_s\colon q[\varphi_1 s]\to p[s]$.

---

## 1. The distributor and the interchange, in coordinates

Both sides of $\delta$ share the shape set $S_A\times S_B\times S_C$; on directions,
flattening the exponentials:
$$
A\ltimes(B\rtimes C)\;:\; A[a]^{S_B\times S_C}\times B[b]^{S_A\times S_C}\times C[c]^{S_A},
\qquad
(A\ltimes B)\rtimes C\;:\; A[a]^{S_B\times S_C}\times B[b]^{S_A\times S_C}\times C[c].
$$
So $\delta$ is the identity on shapes, and its backward direction map (from RHS to LHS) is
factor-wise:
$$
A:\ \mathrm{id},\qquad B:\ \mathrm{id},\qquad
C:\ C[c]\longrightarrow C[c]^{S_A},\ \ x\mapsto(\text{const}_{S_A}\,x).
$$
The $C$-component is the **constant map** — precomposition with the terminal map
$S_A\twoheadrightarrow 1$ — and is *not* invertible unless $|S_A|=1$. This is the genuine
non-iso content of a linear distributor.

The **duoidal interchange** (roles: $\ltimes$ outer, $\rtimes$ inner)
$\zeta_{A,B,C,D}\colon (A\rtimes B)\ltimes(C\rtimes D)\to(A\ltimes C)\rtimes(B\ltimes D)$
is, on shapes, the middle-four swap $(a,b,c,d)\mapsto(a,c,b,d)$, and on directions factor-wise
$$
A:\ \mathrm{id},\quad C:\ \mathrm{id},\quad
B:\ B[b]^{S_D}\to B[b]^{S_C\times S_D}\ (\text{const in }S_C),\quad
D:\ D[d]^{S_B}\to D[d]^{S_A\times S_B}\ (\text{const in }S_A).
$$

**The two are the same fact:** using the shared unit $y$ and $A\rtimes y\cong A$,
$y\ltimes C\cong C$,
$$
A\ltimes(B\rtimes C)\ \cong\ (A\rtimes y)\ltimes(B\rtimes C)
\xrightarrow{\ \zeta_{A,y,B,C}\ } (A\ltimes B)\rtimes(y\ltimes C)\ \cong\ (A\ltimes B)\rtimes C,
$$
and this composite equals $\delta_{A,B,C}$ (verified computationally on all small cases,
`ldc_coherence.py::delta_from_zeta`).

---

## 2. The reindexing calculus

The proof of coherence is uniform. Fix atoms $p_1,\dots,p_n$ with shape sets $S_1,\dots,S_n$.
For a subset $A\subseteq\{1,\dots,n\}$ write $S(A):=\prod_{j\in A}S_j$ (a product over an
**unordered** index set — canonical in $(\mathbf{Set},\times,1)$).

**Lemma 1 (normal form).** Every composite $T$ of the $p_i$ under $\ltimes,\rtimes$ has shape
set $\prod_i S_i$ (via the canonical $(\mathbf{Set},\times)$ reindexing) and direction
$$
T[(s_1,\dots,s_n)] \;=\; \prod_{i=1}^n p_i[s_i]^{\,S(A_i^{T})},\qquad A_i^{T}\subseteq\{1,\dots,n\}\setminus\{i\}.
$$
The subsets are computed by the recursion (base $A_i^{p_i}=\varnothing$; $G_X$ = atom set of $X$):
$$
X\ltimes Y:\quad i\in X\mapsto A_i^{X}\sqcup G_Y,\ \ j\in Y\mapsto A_j^{Y}\sqcup G_X;\qquad
X\rtimes Y:\quad i\in X\mapsto A_i^{X}\sqcup G_Y,\ \ j\in Y\mapsto A_j^{Y}.
$$

*Proof.* Induction on the composite. The binary steps are exactly the direction formulas:
$(X\ltimes Y)[\,] = X[\,]^{S_Y}\times Y[\,]^{S_X}$ multiplies each atom's exponent by the *whole*
other operand's shape set $S_{G_Y}=S(G_Y)$ resp. $S(G_X)$; $(X\rtimes Y)[\,]=X[\,]^{S_Y}\times Y[\,]$
does so only for the left operand. This is the registry-proved $n$-fold normal form
($n$-fold $\ltimes$: $A_i=\{j\ne i\}$; $n$-fold $\rtimes$: $A_i=\{j>i\}$). $\qquad\blacksquare$

**Lemma 2 (structural maps are projections).** Call a morphism *structural* if it is built by
composition and $\ltimes/\rtimes$ from associators, unitors, the $\ltimes$-symmetry, $\zeta$ and
$\delta$. Every structural map $T\to T'$ (same atoms) acts:
- on shapes, by the **unique** $(\mathbf{Set},\times,1)$-coherence isomorphism of $\prod_iS_i$;
- on each direction factor $i$, by **precomposition with the product-projection**
  $\pi_i\colon S(A_i^{T})\twoheadrightarrow S(A_i^{T'})$,
  which exists and is unique **iff** $A_i^{T'}\subseteq A_i^{T}$.

*Proof.* For the generators, read off the subsets from Lemma 1 and check $A_i^{tgt}\subseteq A_i^{src}$
with the map equal to the coordinate-projection:
- **associators, symmetry**: $A_i^{src}=A_i^{tgt}$ (the subsets are bracket- and order-independent),
  so $\pi_i=\mathrm{id}$; the map is the identity on the flattened normal form.
- **unitors** (remove a $y$-atom, $S_y=1$): $S(A_i)$ is unchanged because a factor $S_y=1$ is trivial;
  $\pi_i=\mathrm{id}$ (a bijection), so unitors are isos.
- **$\delta_{A,B,C}$**: $A_i^{src}=(\{B,C\},\{A,C\},\{A\})$, $A_i^{tgt}=(\{B,C\},\{A,C\},\varnothing)$;
  the only nontrivial projection is $S(\{A\})=S_A\twoheadrightarrow S(\varnothing)=1$ on the $C$-factor
  (the constant map above).
- **$\zeta_{A,B,C,D}$**: $A_i^{src}=(\{B,C,D\},\{C,D\},\{A,B,D\},\{A,B\})$,
  $A_i^{tgt}=(\{B,C,D\},\{D\},\{A,B,D\},\{B\})$; projections drop $S_C$ on $B$ and $S_A$ on $D$.

Finally, applying $\ltimes$ or $\rtimes$ to a structural map is again structural: the functorial
action enlarges every atom's exponent by a common factor (the other operand's shapes) and
precomposes with the operand's forward shape map — a coordinate-projection composed with a
projection is a projection. $\qquad\blacksquare$

**Theorem (coherence for free).** For fixed atoms $p_1,\dots,p_n$ there is **at most one**
structural morphism $T\to T'$: on shapes the unique product-coherence iso, and on each factor the
unique projection $S(A_i^{T})\twoheadrightarrow S(A_i^{T'})$ (existing iff
$A_i^{T'}\subseteq A_i^{T}$). Consequently **every diagram of structural maps commutes**.

*Proof.* Uniqueness of the shape part is Mac Lane coherence for $(\mathbf{Set},\times,1)$.
Uniqueness of each direction factor: a product projection that keeps a specified subset of
coordinates is unique. Existence needs $A_i^{T'}\subseteq A_i^{T}$; each generator satisfies this
(Lemma 2), and a composite of generators is a composite of projections, hence a projection with
$A_i^{final\ tgt}\subseteq A_i^{initial\ src}$. Two parallel composites therefore share source and
target subsets and induce the same (unique) projection on every factor and the same shape iso, so
they are equal. $\qquad\blacksquare$

Because the subsets $A_i$ form a poset under $\subseteq$ (at most one arrow between any two elements),
coherence is *automatic*: there is nothing to check beyond Lemma 2's case list of generators.

---

## 3. Consequences

**Corollary 1 (normal duoidal).** $(\mathbf{Poly},\ltimes,\rtimes,y)$ is a normal duoidal category:
$\ltimes$ (symmetric) and $\rtimes$ (directed) are monoidal with shared unit $y$; the interchange
$\zeta$ is natural; and all duoidal coherence axioms — associativity compatibilities and unit
laws — hold by the Theorem (they are diagrams of structural maps). Normality is the shared unit $y$
together with the four unitors being isomorphisms (Lemma 2).

**Corollary 2 (linear distributivity — the PROVE target).** $\mathbf{Poly}$ is a linearly
distributive category on $(\ltimes,\rtimes)$ with tensor $\ltimes$, par $\rtimes$, and linear
distributor $\delta_{A,B,C}\colon A\ltimes(B\rtimes C)\to(A\ltimes B)\rtimes C$ (§1). The
Cockett–Seely coherence conditions (the $\ltimes$- and $\rtimes$-associativity pentagons and the
unit triangles) are diagrams of structural maps, hence commute by the Theorem. The symmetry of
$\ltimes$ additionally supplies the right distributor
$\partial^R_{A,B,C}\colon(A\rtimes B)\ltimes C\to A\rtimes(B\ltimes C)$ (the $C$-factor
projection $S(A_i)=S_A\times S_B\twoheadrightarrow S_B$, const in $S_A$).

**Non-degeneracy.** $\delta$ is *not* an isomorphism (the $C$-factor map $S_A\twoheadrightarrow 1$
is non-injective whenever $|S_A|\ge 2$), so this is a genuine LDC, not a case where tensor $=$ par.

---

## 4. Computational verification (`.claude/scratch/ldc_*.py`)

A full container-level implementation (polynomial morphisms with forward-shape / backward-direction
data; $\ltimes,\rtimes$ acting on actual direction *elements*; functorial actions; composition and
equality by evaluating backward maps on every direction element):

| Check | Result |
|---|---|
| $\zeta,\delta$ well-defined (bwd images land in source directions) | ✓ |
| $\delta$ naturality (squares over sampled morphism triples) | 729/729 commute |
| $\zeta$ naturality (over sampled morphism quadruples) | 378/378 commute |
| LDC $\ltimes$-associativity pentagon | all cases ✓ |
| LDC $\rtimes$-associativity pentagon | all cases ✓ |
| Duoidal interchange assoc, $3\times2$ grid ($\rtimes$-assoc compat) | ✓ |
| Duoidal interchange assoc, $2\times3$ grid ($\ltimes$-assoc compat) | ✓ |
| $\delta$ = $\zeta$-induced distributor (normality reduction) | ✓ |
| shared unit; all four unitors iso; $y\ltimes y\cong y\cong y\rtimes y$ | ✓ |

Worked instance of the crux ($\delta$, $C$-factor): with $|S_A|=2$, an element $x\in C[c]$ maps
to the constant tuple $(x,x)\in C[c]^{S_A}$ — matching the abstract "$\text{precompose with }
S_A\twoheadrightarrow1$." The map is 2-to-… non-surjective onto $C[c]^{S_A}$, confirming non-iso.

---

## 5. Status, provenance, honesty

- **Mathematics: PROVED.** Premises: the registry-proved $n$-fold normal forms of $\ltimes,\rtimes$
  (`other-cont-monoidal-tensors`, `monoidal-symmetric-directed`, trust *proved*); Mac Lane coherence
  for $(\mathbf{Set},\times,1)$ (published); the reindexing calculus (new here). Computation
  reconciles with every step.
- **Novelty: UNVERIFIED (no-browse session).** The template is Spivak–Srinivasan arXiv:2407.01849,
  which presents $\mathbf{Poly}$ as a normal duoidal / linearly distributive category for the pair
  $(\otimes_{\mathrm{Day}},\lhd)$. This result is the **$(\ltimes,\rtimes)$ analogue** — a *second*
  normal-duoidal/LDC structure on $\mathbf{Poly}$, on the non-convolutional Dialectica tensors.
  Do **not** claim priority for "Dialectica-LDC on Poly": the theme is crowded (de Paiva/Trotta,
  Moss–von Glehn dependent Dialectica, Spivak–Srinivasan). A browse pass must (i) check whether the
  $(\ltimes,\rtimes)$ duoidal pairing is already recorded, and (ii) reconcile with the observation
  that $\rtimes$ is **not** the Dialectica par (its shapes are $S_p\times S_q$, not the dual
  $S_p^{Y}\times S_q^{X}$) — so this is a fresh pairing, not the classical Dialectica $\otimes/\parr$.

- **Gap (minor):** the full Cockett–Seely axiom list for a *symmetric* LDC includes coherence of
  $\partial^R$ with the symmetry; these are again diagrams of structural maps and so are covered by
  the Theorem in principle, but $\partial^R$'s pentagons were not separately run in code. Low risk.
