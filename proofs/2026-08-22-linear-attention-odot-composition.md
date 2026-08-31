# Linear attention is a ⊙-composition in Mat(Vec) — exactly at fixed context

**MacBeth — 2026-08-22 — PROVE session**

## Problem statement

Model a linear-attention head over a field (take ℝ). Given queries, keys, values and a feature
map φ, one head computes
$$\mathrm{out}_i \;=\; \sum_j \langle \varphi(q_i),\varphi(k_j)\rangle\, v_j
\;=\; \varphi(q_i)^{\!\top}\!\Big(\sum_j \varphi(k_j)\otimes v_j\Big).$$
The right factor $S=\sum_j\varphi(k_j)\otimes v_j$ is a matrix over ℝ. In the Vec-matrix
bicategory $\mathsf{Mat}(\mathsf{Vec})$, composition contracts an intermediate index
$$(P\odot Q)(a,c)=\bigoplus_b P(a,b)\otimes Q(b,c)\qquad(\text{= profunctor composition; discrete coend}).$$
This is the operation the plain note (`vcont-plain-note.tex` §3–4) proposes as the *pipeline* wiring
for prompt/response workflows, flagged there as **proposal, not theorem**.

**Original claim to test.** (i) One head $=$ one $\odot$; (ii) *stacking $L$ heads $=$ iterated
$\odot$, so a depth-$L$ stack is a single Vec-matrix (algebroid morphism)*; (iii) softmax is the
boundary. The honest test built into the task: this must exhibit **functoriality/compositionality**,
not merely re-notate the algebra.

## Verdict (honest, up front)

- The **strong form (ii) is FALSE** for real (data-dependent) linear attention: a live depth-$L$
  stack with identity feature map is a homogeneous polynomial map of **degree exactly $3^L$** in its
  input tokens, whereas every Vec-matrix $\odot$-composite acts *linearly* (degree 1) on its
  argument. So a live stack is a single Vec-matrix only for $L=0$.
- The claim becomes a **theorem in the fixed-context regime** (KV-state frozen, $\varphi=\mathrm{id}$),
  which is exactly the in-context/KV-cache regime. There the picture is genuinely functorial, with
  **two** functors: contexts compose by $\oplus$ (the §4 *menu* wiring), depths compose by $\odot$
  (the §4 *pipeline* wiring).
- This is **not** restatement: the content is the boundary. The degree-$3^L$ invariant separates
  "trained deep network" from "single Vec-matrix," and it *explains* why O'Neill (2501.02931) is
  forced to model stacking by a **free monad** (a non-collapsing tower) rather than one morphism.

## Setup and notation

A **linear-attention head** is $H=(\varphi,W_Q,W_K,W_V)$ with feature map
$\varphi:\mathbb{R}^{d_k}\to\mathbb{R}^{d_\varphi}$ and learned linear maps $W_Q,W_K,W_V$. On a
context (token sequence) $x_1,\dots,x_n$ put $k_j=W_Kx_j,\ v_j=W_Vx_j$ and form the **KV-state**
$$S \;=\; \sum_{j=1}^n \varphi(k_j)\otimes v_j \;\in\; \mathsf{Mat}(\mathsf{Vec})(d_\varphi,d_v),$$
a single Vec-matrix (one shape on each side; a morphism $d_\varphi\to d_v$). The head reads out a
query $q$ as $\mathrm{out}(q)=\varphi(W_Qq)^{\!\top}S$.

Throughout, "$\odot$" is the Mat(Vec) product above; for one-dimensional entries ($P(a,b)=\mathbb{R}$
carrying a scalar) $\otimes$ is scalar multiplication and $\bigoplus_b$ is summation, so $\odot$ on
scalar-valued matrices *is* ordinary matrix multiplication, and $\oplus$ on hom-objects is matrix
addition.

---

## (A) One head's readout is one ⊙-composition

**Proposition A.** With $u:=\varphi(W_Qq)$ the query feature, $\mathrm{out}(q)=u^{\!\top}S=(y_{d_\varphi}\odot S)$,
the single $\odot$-composition of the query (a $1\times d_\varphi$ row) with the KV-state, contracting
over the **feature index** $b\in\{1,\dots,d_\varphi\}$.

*Proof.* $\mathrm{out}(q)_c=\sum_j\langle\varphi(q),\varphi(k_j)\rangle\,v_{jc}
=\sum_j\big(\sum_b u_b\varphi(k_j)_b\big)v_{jc}=\sum_b u_b\big(\sum_j\varphi(k_j)_b v_{jc}\big)=\sum_b u_b S_{bc}$
by finiteness of the sums and bilinearity of $\langle-,-\rangle$. Reading $u_b=P(\ast,b)$,
$S_{bc}=Q(b,c)$ this is $(P\odot Q)(\ast,c)=\bigoplus_b P(\ast,b)\otimes Q(b,c)$. ∎

**Altitude: translation.** This is the associativity reassociation written in $\odot$-notation. Its
one genuinely new payload is *which* index the abstract §3 contraction variable $b$ is: the **feature
dimension** $d_\varphi$. Verified exactly (numerics: $|{\rm direct}-\odot|=1.6\times10^{-15}$;
readout linear in $u$ to machine eps). This overlaps Vertechi (parametric span) and O'Neill
(parametric 1-morphism in Para(Vect)) and is *not* novel as mathematics.

---

## (B) Context composes by ⊕ — a monoid homomorphism (the linear-RNN functor)

**Proposition B.** Fix $H$. The assignment $C\mapsto S(C)$ from the free monoid of contexts
(token sequences under concatenation $\cdot$, unit the empty context $\varnothing$) to
$(\mathsf{Mat}(\mathsf{Vec})(d_\varphi,d_v),\ \oplus,\ 0)$ is a monoid homomorphism:
$$S(C\cdot C')=S(C)\oplus S(C'),\qquad S(\varnothing)=0.$$

*Proof.* $S(C\cdot C')=\sum_{j\in C\cdot C'}\varphi(k_j)\otimes v_j
=\sum_{j\in C}\varphi(k_j)\otimes v_j+\sum_{j\in C'}\varphi(k_j)\otimes v_j=S(C)+S(C')$, and matrix
addition is the biproduct $\oplus$ on the hom-object; the empty sum is $0$. ∎

This is exactly linear attention in its **recurrent (linear-RNN) form**, $S_t=S_{t-1}+\varphi(k_t)\otimes v_t$
(Katharopoulos et al. 2020, arXiv:2006.16236). The container-theoretic content is the reading of that
recurrence as the §4 *menu/both* wiring $\oplus$ acting on **contexts**: appending context is adding
KV-states. Verified exactly (error $0.0$).

---

## (C) At fixed context, depth composes by ⊙

Call a head **frozen** if its KV-state $S$ is held constant (independent of the argument). With
$\varphi=\mathrm{id}$ a frozen head is the linear map $u\mapsto u^{\!\top}S$ — i.e. *literally the
Vec-matrix $S$*.

**Proposition C.** Let $H_1,\dots,H_L$ be frozen heads with $\varphi=\mathrm{id}$ and with the
value-space of $H_\ell$ equal to the feature-space of $H_{\ell+1}$ (so the axes chain). The
depth-composite readout is the single Vec-matrix
$$S^1\odot S^2\odot\cdots\odot S^L,$$
the $\odot$-product contracting over each shared intermediate axis. Hence the frozen $\varphi=\mathrm{id}$
heads form a full sub-bicategory of $\mathsf{Mat}(\mathsf{Vec})$, and depth-composition **is** $\odot$.

*Proof.* By Proposition A each frozen head acts as $u\mapsto u^{\!\top}S^\ell$. Composing,
$u\mapsto (u^{\!\top}S^1)^{\!\top\top}\!S^2\cdots = u^{\!\top}(S^1S^2\cdots S^L)$, and matrix product
is $\odot$ (discrete coend, §3). A frozen head is a Vec-matrix and its composite is a Vec-matrix, so
the collection is closed under $\odot$ — a full sub-bicategory. ∎

Verified exactly (error $9\times10^{-16}$). A **non-degenerate** instance (contraction index size
$|b|=4>1$) is realised when the value-output of one head feeds the next head's key-feature linearly;
then $b$ is the genuine intermediate feature/value axis of §3, not a formality.

**Altitude: proved, low novelty.** Once framed, (C) is "frozen linear heads are Vec-matrices and
Vec-matrices compose by $\odot$." The content is the *identification of the regime* — fixed context is
exactly where $\odot$ is exact — and it sets up the boundary.

---

## (D) The boundary: live stacks have degree $3^L$ (main result)

Now let each head form its KV-state from the **running representation** (genuine self-attention): the
output of head $\ell$ is the token-input to head $\ell+1$, and $S^{\ell}$ is built from that same
running representation. Write one $\varphi=\mathrm{id}$ layer as a map of the token matrix
$X\in\mathbb{R}^{n\times d}$.

**Lemma D0 (one live layer is degree-3 homogeneous).** With $\varphi=\mathrm{id}$,
$$\mathrm{out}_i = \big(W_V\,X^{\!\top}X\,W_K^{\!\top}\,W_Q\big)\,x_i,$$
so each output-token entry is a homogeneous polynomial of degree $3$ in the entries of $X$.

*Proof.* $S=\sum_j k_jv_j^{\!\top}=\sum_j (W_Kx_j)(W_Vx_j)^{\!\top}=W_K\big(\sum_j x_jx_j^{\!\top}\big)W_V^{\!\top}=W_K X^{\!\top}X\,W_V^{\!\top}$,
which is homogeneous of degree $2$ in $X$. Then $\mathrm{out}_i=S^{\!\top}(W_Qx_i)=W_VX^{\!\top}XW_K^{\!\top}W_Qx_i$;
multiplying the degree-$2$ factor by the degree-$1$ factor $x_i$ gives degree $3$, and every monomial
contains exactly three $X$-factors, so it is homogeneous. ∎

**Theorem D (degree of a live stack).** A live depth-$L$ linear-attention stack with $\varphi=\mathrm{id}$
is a homogeneous polynomial map of degree exactly $3^L$ in its input tokens.

*Proof.* Induction on $L$. $L=1$ is Lemma D0 (degree $3=3^1$). Suppose the depth-$(L-1)$ output $Y$
is homogeneous of degree $d=3^{L-1}$ in $X$ (entrywise). Layer $L$ produces
$W_VY^{\!\top}Y\,W_K^{\!\top}W_QY$-columns (Lemma D0 with input $Y$): $Y^{\!\top}Y$ has degree $2d$, the
trailing $Y$-column degree $d$, total $3d=3^L$, and homogeneity is preserved by products of
homogeneous polynomials. ∎

**Corollary D (strong form refuted).** A live depth-$L$ stack ($L\ge1$) is **not** a single Vec-matrix
$\odot$-composite. Indeed a $\odot$-composite acts on its argument as the linear map
$u\mapsto u^{\!\top}(S^1\odot\cdots)$ — homogeneous of degree $1$ — while the live stack has degree
$3^L\ge3$. Degree is invariant, so they cannot agree. ∎

Verified exactly: measured homogeneity degrees $3,9,27$ for $L=1,2,3$, matching $3^L$ to machine eps.

### (D1) Softmax is not a ⊙-composition at all

**Proposition D1.** The softmax readout $\mathrm{out}(q)=\sum_j\mathrm{softmax}_j(\langle q,k_j\rangle)v_j$
is not equal to $u^{\!\top}S$ for any fixed matrix $S$.

*Proof.* Two independent obstructions. (a) *Non-homogeneity:* softmax$(a\cdot s)\ne a\cdot$softmax$(s)$
in general (the partition-of-unity normaliser $Z(q)=\sum_j e^{\langle q,k_j\rangle}$ depends
nonlinearly on $q$), so $q\mapsto\mathrm{out}(q)$ is not homogeneous of degree $1$, but $u^{\!\top}S$ is.
(b) *Boundedness:* $\mathrm{out}(q)$ is a convex combination of the $v_j$, hence
$\|\mathrm{out}(q)\|\le\max_j\|v_j\|$ for all $q$, while $q\mapsto u^{\!\top}S$ is unbounded whenever
$S\ne0$. ∎

Numerics: homogeneity residual $\approx1.2$ (nonzero); $\|\mathrm{out}\|$ stays in $[0.30,1.39]$ over
queries scaled up to $10\times$. This is corroborated at a stronger, categorical level by Sargsyan
(arXiv:2603.16123, deep-read), which proves softmax attention cannot be functorial for non-trivial
groups; the elementary proof above does not rest on it.

### (D2) A nonlinear feature map keeps ⊙ only in feature space

**Proposition D2.** For any $\varphi$, the readout is $\odot$-linear in the **feature** $u=\varphi(W_Qq)$
(Proposition A). But if $\varphi$ is nonlinear, the map $q\mapsto\varphi(W_Qq)$ is nonlinear, so the
depth-composition expressed in the raw query space is not $\odot$; only the feature-space picture is.

*Proof.* Proposition A used only bilinearity of $\langle-,-\rangle$, giving $u\mapsto u^{\!\top}S$ linear
in $u$; verified to eps for $\varphi=\text{elu}{+}1$. Nonlinearity of $q\mapsto\varphi(W_Qq)$ is immediate. ∎

---

## Synthesis: two functors, one boundary, and why stacking needs a free monad

Assemble (A)–(D) as functoriality:

1. **Context functor ($\oplus$).** $S(-):(\mathrm{Contexts},\cdot,\varnothing)\to(\mathsf{Mat}(\mathsf{Vec}),\oplus,0)$
   is a monoid homomorphism (Prop. B) — the §4 *menu/both* wiring, acting on contexts.
2. **Depth functor ($\odot$).** On the fixed-context ($\varphi=\mathrm{id}$) sub-bicategory of frozen
   heads, depth-composition is $\odot$ in $\mathsf{Mat}(\mathsf{Vec})$ (Prop. C) — the §4 *pipeline*
   wiring, exact.
3. **The boundary.** Off that sub-bicategory — i.e. for genuine data-dependent self-attention — the
   depth-$L$ map has degree $3^L$ (Thm. D), so it is *not* a single Vec-matrix; softmax is not even a
   $\odot$ (D1); a nonlinear $\varphi$ keeps $\odot$ only in feature space (D2).

**The §4 proposal is therefore a theorem for a real ML primitive precisely in the in-context /
KV-cache regime** — the regime where the KV-state is fixed and only the query varies, which is exactly
the operational picture of in-context learning. That is the honest scope of "pipeline $=\odot$."

**Reconciliation with O'Neill (flagged speculative).** O'Neill (arXiv:2501.02931; *agent-summary*
access only) models a linear-attention layer as a parametric 1-morphism in $\mathsf{Para}(\mathsf{Vect})$
and models **stacking as the free monad on the induced endofunctor** — a non-collapsing tower
$F,F^2,F^3,\dots$, not a single morphism. Theorem D supplies the quantitative reason this is *forced*:
the depth-$L$ composite has genuinely different degree $3^L$ at each $L$, so no single morphism can
represent the tower; the free monad is exactly the bookkeeping that keeps all depths distinct. Under
this reading, Para(Vect)'s fixed-parameter map is my fixed-context regime and $\odot$ in
$\mathsf{Mat}(\mathsf{Vec})$ is its concrete feature-axis shadow, while the degree explosion is what
happens when the "parameters" (the KV-state) are themselves functions of the input. Confirming
O'Neill's exact free-monad statement needs a deep-read; I flag this reconciliation as a conjecture, not
a proved equivalence.

---

## Verification summary (all exact to machine precision)

| Claim | Test | Result |
|---|---|---|
| (A) readout $=\odot$ | direct vs $u^\top S$; linearity in $u$ | $1.6\times10^{-15}$; $0.0$ |
| (B) context $=\oplus$-hom | $S(C\!\cdot\!C')-(S{\oplus}S')$ | $0.0$ |
| (C) frozen depth $=\odot$ | stack vs $S^1\odot S^2$; non-degen $|b|{=}4$ | $9\times10^{-16}$ |
| (D) live degree $=3^L$ | homogeneity degree, $L{=}1,2,3$ | $3,9,27$ |
| (D1) softmax $\ne\odot$ | homogeneity; boundedness | resid $1.2$; $\|\!\cdot\!\|\in[0.30,1.39]$ |
| (D2) nonlinear $\varphi$ | linearity in feature $u$ | $1\times10^{-16}$ |

Scripts: `.claude/scratch/attn_toy{,2,3}.py`.

## Gaps / honest altitude

- (A),(B),(C) are elementary; (A) is translation, (B) is the known linear-RNN fact repackaged, (C) is
  "linear maps compose by matrix product." The genuine, novel content is **Theorem D (degree $3^L$)**
  and the **identification of fixed-context as the exact $\odot$-regime with the $\oplus$/$\odot$ functor
  pair**.
- The **O'Neill free-monad reconciliation** is the crown-jewel connection but rests on an
  agent-summary of 2501.02931; it is a conjecture until a deep-read confirms O'Neill's exact
  construction. Do not build on it at `proved`.
- Single-layer-as-parametric-map is prior work (Vertechi, O'Neill); no novelty claimed there.
- The result is stated over ℝ; nothing uses more than a field with the standard bilinear pairing.

## One-line grant statement

*The compositional (⊙/⊕) picture of §4 is exact for linear attention in the in-context regime — two
functors, contexts by ⊕ and depths by ⊙ — and the obstruction to compositional collapse of a trained
network is a single clean invariant: a live depth-L stack has polynomial degree 3^L, which is precisely
why deep attention must be modelled by a non-collapsing tower (free monad), not a single weight-matrix.*
