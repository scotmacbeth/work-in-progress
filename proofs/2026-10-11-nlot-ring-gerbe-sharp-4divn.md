# The sharp criterion for strict global inventory on the $n$-lot ring: the gerbe fails **exactly** when $4 \mid n$

**Date:** 2026-10-11 (deep-work prove session)
**Status:** proved (own-verification; computation corroborated, see §5)
**Registry:** `supply-chain-inventory-gerbe-h2.json`, node `thm-D-nonvacuous-criterion`
**Lane brief:** `state/PROVE.md` — independent upgrade of Rick's round-2 sharp replacement for the (refuted) general "Thm D".

---

## 0. Statement

Fix the **$n$-lot ring** fibre $F = F(n)$: $n$ fungible stock lots arranged in a ring,
i.e. the vertex set of the $n$-cycle graph $C_n$ with its cyclic adjacency ("ring") structure
($n \ge 3$). Its relabelling group — the structure group of the inventory gerbe — is

$$K(n) \;:=\; \operatorname{Aut}(F(n)) \;=\; \operatorname{Aut}(C_n) \;=\; D_n,$$

the **dihedral group of order $2n$** (geometer's convention: $D_n = $ symmetries of the regular
$n$-gon), with presentation
$$D_n = \langle r, s \mid r^n = s^2 = 1,\; s r s^{-1} = r^{-1}\rangle.$$
(Source: gerbe note §B line 590 — "four lots arranged in a ring (the $4$-cycle); its relabelling
group is the dihedral group $K=\operatorname{Aut}F = D_4$ of order $8$"; Rick r2 review — "the six-lot
ring has $\operatorname{Aut}F = D_6 \cong \mathbb Z/2 \times S_3$", "the $n$-lot ring ($K = D_n$, $n$
even) carries a class iff $4 \mid n$ (D4, D8 yes; D6 no)".)

The **inventory gerbe class** is $[\gamma] = \rho^*[\star] \in H^2(N(\mathcal C); Z(K))$, the
pullback along an inner-transport functor $\rho : \mathcal C \to B(\operatorname{Inn}K)$ of the class
$[\star] \in H^2(\operatorname{Inn}K; Z(K))$ of the central extension

$$(\star)\qquad 1 \longrightarrow Z(K) \longrightarrow K \xrightarrow{\ \pi\ } \operatorname{Inn}K \longrightarrow 1.$$

Call the inventory gerbe **essentially nonzero** if there exists a base category $\mathcal C$ and an
inner transport $\rho : \mathcal C \to B(\operatorname{Inn}K)$ with $[\gamma] \ne 0$ — equivalently,
if strict global inventory with inner comparison maps is obstructed for some supply chain.

> **Theorem (sharp $n$-lot criterion).** For $K = K(n) = D_n$:
> $$\text{the inventory gerbe is essentially nonzero} \iff (\star)\text{ is non-split} \iff 4 \mid n.$$
> Equivalently, strict global inventory is **always** rectifiable on the $n$-lot ring unless $4 \mid n$.

The three deliverables of the brief:
1. **(§1–2)** $K(n) = D_n$; compute $Z(D_n)$, $\operatorname{Inn}D_n$, and split/non-split of
   $(\star)$ as a function of $n$: split $\iff 4 \nmid n$.
2. **(§3)** The classical identification: $[\gamma]$ essentially nonzero $\iff [\star] \ne 0 \iff (\star)$ non-split.
3. **(§4)** The $D_6 = \mathbb Z/2 \times S_3$ reconciliation: nonabelian with nontrivial centre, yet
   splits, so "$[\gamma] \ne 0$"; it is the honest witness that N2 forces.

---

## 1. The structure group is dihedral, and its centre / inner group

**Lemma 1 (structure group).** $\operatorname{Aut}(C_n) = D_n$ of order $2n$, for $n \ge 3$.

*Proof.* Standard. An automorphism of the $n$-cycle is determined by the image of one vertex and an
orientation; there are $n$ choices of image and $2$ of orientation, giving $2n$ symmetries, and all
$2n$ dihedral symmetries are realised. $\square$

(For $n = 3$ this is $D_3 = S_3$; every permutation of the triangle's vertices preserves adjacency.)

**Lemma 2 (centre of $D_n$).**
$$Z(D_n) = \begin{cases} 1 & n \text{ odd},\\[2pt] \{1, r^{n/2}\} \cong \mathbb Z/2 & n \text{ even}.\end{cases}$$

*Proof.* Write a general element as $r^k$ or $r^k s$. Conjugation gives $s r^k s^{-1} = r^{-k}$ and
$r\,(r^k s)\,r^{-1} = r^{k+2}s$. A rotation $r^k$ is central iff $r^k = s r^k s^{-1} = r^{-k}$, i.e.
$r^{2k} = 1$, i.e. $n \mid 2k$: the only solutions in $0 \le k < n$ are $k = 0$ always, and $k = n/2$
when $n$ is even. A reflection $r^k s$ is central only if $r (r^k s) r^{-1} = r^{k+2}s = r^k s$, i.e.
$r^2 = 1$, i.e. $n \mid 2$, impossible for $n \ge 3$. Hence $Z(D_n) = \{1\}$ for $n$ odd and
$\{1, r^{n/2}\}$ for $n$ even. $\square$

**Lemma 3 (inner group of $D_n$).**
$$\operatorname{Inn}D_n = D_n / Z(D_n) \cong \begin{cases} D_n & n \text{ odd},\\ D_{n/2} & n \text{ even}.\end{cases}$$

*Proof.* $\operatorname{Inn}G \cong G/Z(G)$ for every group $G$. For $n$ odd, $Z = 1$ so
$\operatorname{Inn}D_n = D_n$ (order $2n$). For $n$ even, quotient $D_n$ by $Z = \langle r^{n/2}\rangle$:
the image $\bar r$ of $r$ has order $n/2$, $\bar s$ has order $2$, and $\bar s \bar r \bar s^{-1} =
\bar r^{-1}$, so $D_n/\langle r^{n/2}\rangle = \langle \bar r, \bar s\rangle \cong D_{n/2}$ (order $n$). $\square$

So for $n = 4$: $Z = \{1, r^2\} \cong \mathbb Z/2$, $\operatorname{Inn}D_4 = D_2 = (\mathbb Z/2)^2$
(matches the note). For $n = 6$: $Z \cong \mathbb Z/2$, $\operatorname{Inn}D_6 = D_3 = S_3$ (matches Rick).

**Consequence for the odd case.** When $n$ is odd, $Z(D_n) = 1$, so the central extension $(\star)$
is $1 \to 1 \to D_n \to D_n \to 1$ (trivially split) and the coefficient group of the gerbe is
$H^2(N(\mathcal C); 1) = 0$. The gerbe is **vacuously zero** for all odd $n$. The entire question
lives in the even case, to which we now restrict.

---

## 2. The arithmetic: $(\star)$ splits $\iff 4 \nmid n$

Fix $n$ even, $n \ge 4$, and write $n = 2m$ with $m \ge 2$. By Lemmas 2–3 the central extension is

$$(\star)\qquad 1 \longrightarrow \mathbb Z/2 \cong \langle r^m\rangle \longrightarrow D_{2m}
\xrightarrow{\ \pi\ } D_m \cong \operatorname{Inn}D_{2m} \longrightarrow 1.$$

A **splitting** of $(\star)$ is a subgroup $H \le D_{2m}$ complementary to the centre $Z = \langle r^m\rangle$:
$H \cap Z = 1$ and $HZ = D_{2m}$. Because $Z$ is central (hence normal) and any such $H$ has index
$|Z| = 2$ (hence is normal), a complement makes $D_{2m}$ the **internal direct product** $Z \times H$,
and necessarily $H \cong D_{2m}/Z = D_m$. Thus

$$(\star)\text{ splits} \iff D_{2m} \cong \mathbb Z/2 \times D_m. \tag{2.1}$$

**Theorem 4 (the splitting jump).** For $m \ge 2$, $\;D_{2m} \cong \mathbb Z/2 \times D_m \iff m$ is odd.

*Proof.* The proof is a **centre count** — the order of the centre is a perfect isomorphism invariant
that already separates the two cases.

Left-hand side: $2m$ is even, so by Lemma 2, $|Z(D_{2m})| = 2$.

Right-hand side: the centre of a direct product is the product of centres, so
$$Z(\mathbb Z/2 \times D_m) = \mathbb Z/2 \times Z(D_m), \qquad |Z(\mathbb Z/2 \times D_m)| = 2\cdot |Z(D_m)|.$$
By Lemma 2, $|Z(D_m)| = 1$ if $m$ is odd and $|Z(D_m)| = 2$ if $m$ is even. (For the degenerate
$m = 2$, $D_2 = (\mathbb Z/2)^2$ is abelian with $|Z(D_2)| = 4$; this only *widens* the gap, see below.)
Hence
$$|Z(\mathbb Z/2 \times D_m)| = \begin{cases} 2 & m \text{ odd},\\ \ge 4 & m \text{ even}.\end{cases}$$

If $m$ is **even**, $|Z(\mathbb Z/2 \times D_m)| \ge 4 \ne 2 = |Z(D_{2m})|$, so the two groups are
**not isomorphic** and $(\star)$ does **not** split.

If $m$ is **odd** ($m \ge 3$), we exhibit the complement explicitly. Set $H := \langle r^2, s\rangle$.
Since $m$ is odd, $\gcd(2, 2m) = 2$ and $r^2$ has order $2m/2 = m$; so $\langle r^2\rangle$ has order
$m$ and $H = \langle r^2, s\rangle \cong D_m$ (order $2m = n$). The centre is $Z = \langle r^m\rangle$,
and $r^m \in \langle r^2\rangle \iff m$ is even; since $m$ is odd, $r^m \notin \langle r^2\rangle$, and
$r^m$ is a rotation so it is not one of the reflections $r^{2k}s$ in $H$ either — hence
$H \cap Z = 1$. Then $|HZ| = |H|\,|Z|/|H\cap Z| = 2m \cdot 2 = 4m = |D_{2m}|$, so $HZ = D_{2m}$, and
$Z$ central gives $D_{2m} = Z \times H \cong \mathbb Z/2 \times D_m$. $\square$

**Corollary 5 (the $4 \mid n$ line).** For $K(n) = D_n$:
$$(\star)\text{ is non-split} \iff n \text{ even and } n/2 \text{ even} \iff 4 \mid n.$$

*Proof.* $n$ odd: $Z = 1$, $(\star)$ trivially split (Lemma 2). $n$ even, $n = 2m$: by Theorem 4 and
(2.1), split $\iff m = n/2$ odd $\iff n \equiv 2 \pmod 4 \iff 4 \nmid n$. Taking contrapositives,
non-split $\iff 4 \mid n$. $\square$

**The table** (verified computationally, §5):

| $n$ | $K=D_n$, $\lvert K\rvert$ | $Z(K)$ | $\operatorname{Inn}K$ | $(\star)$ | $4\mid n$? |
|----|----|----|----|----|----|
| 3 | $D_3=S_3$, 6 | $1$ | $S_3$ | split (vacuous) | no |
| 4 | $D_4$, 8 | $\mathbb Z/2$ | $(\mathbb Z/2)^2$ | **non-split** | **yes** |
| 5 | $D_5$, 10 | $1$ | $D_5$ | split (vacuous) | no |
| 6 | $D_6$, 12 | $\mathbb Z/2$ | $S_3$ | split | no |
| 7 | $D_7$, 14 | $1$ | $D_7$ | split (vacuous) | no |
| 8 | $D_8$, 16 | $\mathbb Z/2$ | $D_4$ | **non-split** | **yes** |
| 10 | $D_{10}$, 20 | $\mathbb Z/2$ | $D_5$ | split | no |
| 12 | $D_{12}$, 24 | $\mathbb Z/2$ | $D_6$ | **non-split** | **yes** |

The non-split column is exactly the $4\mid n$ column. This is the "2-divisibility jumps at $4$"
pattern predicted in the brief.

---

## 3. From splitting to the gerbe: $[\gamma]$ essentially nonzero $\iff (\star)$ non-split

This step is classical; we record it to close the logical chain (cf. gerbe note Def. of $[\gamma]$,
eq. $(\dagger)$, Lemma "$\gamma$ is a cocycle", Thm A, Rem. "classical lifting criterion").

**The coefficients are untwisted.** Inner automorphisms of $K$ fix $Z(K)$ pointwise (conjugation by
any element of $K$ acts trivially on central elements). Hence the action of $\operatorname{Inn}K$ on
$Z(K)$ induced by $(\star)$ is **trivial**, and $Z(K)$ is an untwisted $\operatorname{Inn}K$-module.

**Lemma 6 (extension class $\leftrightarrow$ splitting).** $[\star] = 0$ in
$H^2(\operatorname{Inn}K; Z(K)) \iff (\star)$ splits.

*Proof.* The classical bijection (central extensions of $G$ by an abelian group $A$ with trivial
$G$-action, up to equivalence) $\leftrightarrow H^2(G; A)$ sends the split extension to $0$: choose a
set-section $t : \operatorname{Inn}K \to K$ of $\pi$ with $t(1) = 1$; the factor set
$f(a,b) = t(a)t(b)t(ab)^{-1} \in Z(K)$ is a normalised $2$-cocycle representing $[\star]$, and
$[\star] = 0$ iff $f = \delta c$ for some $1$-cochain $c : \operatorname{Inn}K \to Z(K)$, iff the
corrected section $t'(a) = c(a)^{-1}t(a)$ is a group homomorphism, iff $(\star)$ splits
(Eilenberg–Mac Lane; Brown, *Cohomology of Groups*, IV.3). $\square$

**Lemma 7 (essentially nonzero $\iff [\star] \ne 0$).** With $[\gamma] := \rho^*[\star]$ for inner
transports $\rho : \mathcal C \to B(\operatorname{Inn}K)$:
$$\big(\exists\,(\mathcal C, \rho):\ [\gamma] \ne 0\big) \iff [\star] \ne 0.$$

*Proof.* ($\Leftarrow$) Take $\mathcal C = B(\operatorname{Inn}K)$ and $\rho = \operatorname{id}$. The
nerve $N(B(\operatorname{Inn}K)) = B(\operatorname{Inn}K)$ computes group cohomology, and
$\rho^* = \operatorname{id}^* = \operatorname{id}$ on $H^2(\operatorname{Inn}K; Z(K))$, so
$[\gamma] = [\star] \ne 0$. ($\Rightarrow$) If $[\star] = 0$ then $\rho^*[\star] = 0$ for **every**
functor $\rho$ (pullback is a homomorphism $H^2(\operatorname{Inn}K; Z(K)) \to H^2(N(\mathcal C); Z(K))$),
so $[\gamma] = 0$ for all $(\mathcal C, \rho)$; contrapositive gives the claim. $\square$

Chaining Lemmas 6–7 with Corollary 5:

$$\boxed{\ [\gamma]\text{ essentially nonzero} \iff [\star]\ne 0 \iff (\star)\text{ non-split} \iff 4 \mid n.\ }$$

By Theorem A of the note, $[\gamma] = 0$ is exactly rectifiability of strict global inventory (band
trivial). So on the $n$-lot ring, strict global inventory is **always achievable except when
$4 \mid n$**, where it is genuinely obstructed by a nonzero class in
$H^2(\operatorname{Inn}D_n; \mathbb Z/2)$.

*Minimal realisation when $4\mid n$.* Taking $\mathcal C = B(\operatorname{Inn}D_n)$, $\rho = \mathrm{id}$,
the obstruction is the full extension class $[\star]\ne 0$. For $n = 4$ this is the $D_4$ class over
$B((\mathbb Z/2)^2)$ of the note's Rem. "$D_4$ and $Q_8$" and the Lean witness
`d4_central_extension_nonsplit` — consistent and now placed in the sharp $n$-family.

---

## 4. The $D_6$ reconciliation: why "nonabelian + nontrivial centre" is **not** sufficient (N2)

The refuted general "Thm D" claimed $[\gamma] \ne 0 \iff K$ nonabelian with nontrivial centre. The
$6$-lot ring is the explicit witness that the $\Leftarrow$ direction fails.

- $K(6) = D_6$, order $12$. By Lemma 2, $Z(D_6) = \{1, r^3\} \cong \mathbb Z/2 \ne 1$. $D_6$ is
  **nonabelian** (e.g. $sr \ne rs$). So $D_6$ satisfies the old hypothesis "nonabelian with nontrivial centre."
- But $6 = 2\cdot 3$ with $m = 3$ **odd**, so by Theorem 4, $D_6 \cong \mathbb Z/2 \times D_3 =
  \mathbb Z/2 \times S_3$ — precisely Rick's identification. The explicit complement is
  $H = \langle r^2, s\rangle \cong D_3 = S_3$ (order $6$), with $H \cap \langle r^3\rangle = 1$
  (since $3$ is odd, $r^3 \notin \langle r^2\rangle$). Verified in §5.
- Hence $(\star)$ **splits**, $[\star] = 0$ (Lemma 6), and $[\gamma] = \rho^*[\star] = 0$ for **every**
  base $\mathcal C$ and every inner transport $\rho$ (Lemma 7). The $6$-lot inventory is **always
  rectifiable**: no tier-two obstruction, ever.

This is exactly the content N2 forces: nonabelian-with-nontrivial-centre is **necessary** (the
printed Thm 25(i)/Thm 5 "only if" survives — $\operatorname{Inn}K = 1$ kills $\rho$, $Z(K) = 1$ kills
the coefficients) but **not sufficient**. The sharp replacement is *non-splitting of $(\star)$*, and on
the $n$-lot ring that is the arithmetic condition $4 \mid n$. The old biconditional and the $4\nmid 6$
witness are now reconciled: $D_6$ is nonabelian with centre $\mathbb Z/2$ **and** split, so it sits in
the gap between the (necessary) centre condition and the (sharp) non-splitting condition.

---

## 5. Verification (computational)

Sub-agent computation, `scratch/dihedral_split_verify.py` (concrete $D_n$ as pairs $(a,k) \in
\mathbb Z/2 \times \mathbb Z/n$, multiplication $(a,k)(b,l) = (a+b, k + (-1)^a l)$; brute-force search
for a central complement $H$ with $H \cap Z = 1$, $|H| = |\operatorname{Inn}|$):

- Centre: $|Z(D_n)| = 1$ ($n$ odd), $2$ ($n$ even), with $Z = \{(0,0),(0,n/2)\}$ for $n$ even — matches Lemma 2.
- Split test, $n = 3..16$: **NON-SPLIT exactly for $n \in \{4, 8, 12, 16\}$** = $\{4\mid n\}$; SPLIT for all
  others (odd $n$ vacuously; $n \in \{6, 10, 14\}$ with $m$ odd via an explicit $D_m$ complement). Matches Corollary 5.
- $n=4$: NON-SPLIT; $D_4 \not\cong (\mathbb Z/2)^3$ (nonabelian). $n=8,12,16$: NON-SPLIT.
- $n=6$: SPLIT; complement $H = \langle r^2, s\rangle = \{(0,0),(0,2),(0,4),(1,0),(1,2),(1,4)\} \cong S_3$,
  $H \cap Z = \{e\}$, $Z = \{(0,0),(0,3)\}$. $n=10,14$: SPLIT.
- Second, independent confirmation via the centre count: $|Z(\mathbb Z/2 \times D_{n/2})| = 2\,|Z(D_{n/2})|$
  equals $|Z(D_n)| = 2$ iff $n/2$ odd — the jump at $4 \mid n$ reproduced without any subgroup search.

Verbatim split-test output ($n = 3..16$; associativity spot-checked, 200 random triples per $n$):

```
  n |  |Z| |  |Inn| |    split? |  4|n?
  3 |    1 |      6 |     SPLIT | False
  4 |    2 |      4 | NON-SPLIT |  True
  5 |    1 |     10 |     SPLIT | False
  6 |    2 |      6 |     SPLIT | False
  7 |    1 |     14 |     SPLIT | False
  8 |    2 |      8 | NON-SPLIT |  True
  9 |    1 |     18 |     SPLIT | False
 10 |    2 |     10 |     SPLIT | False
 11 |    1 |     22 |     SPLIT | False
 12 |    2 |     12 | NON-SPLIT |  True
 13 |    1 |     26 |     SPLIT | False
 14 |    2 |     14 |     SPLIT | False
 15 |    1 |     30 |     SPLIT | False
 16 |    2 |     16 | NON-SPLIT |  True
```

NON-SPLIT occurs **exactly** at $n \in \{4,8,12,16\}$ = $\{4\mid n\}$ (program returned
`non-split ⟺ 4|n : True` for all $n$ in range). $D_6$ complement found:
$H = \langle(0,2),(1,0)\rangle = \{(0,0),(0,2),(0,4),(1,0),(1,2),(1,4)\} \cong S_3$, with
$H \cap Z = \{(0,0)\}$, $Z = \{(0,0),(0,3)\}$. Centre-count table ($n/2$ odd $\iff$ match $\iff$ split):
$n=4{:}\,8{\ne}2$, $6{:}\,2{=}2$, $8{:}\,4{\ne}2$, $10{:}\,2{=}2$, $12{:}\,4{\ne}2$, $14{:}\,2{=}2$,
$16{:}\,4{\ne}2$ — the split jump reproduced with no subgroup search. The structural proof of §1–4 does
not depend on this run; it is independent corroboration.

---

## 6. Scope and gaps

- **No gaps in the arithmetic (§1–2) or the reconciliation (§4).** These are self-contained, elementary,
  and computation-confirmed; graded **proved**.
- **§3 is classical, cited not re-derived.** Lemma 6 (extension class $\leftrightarrow$ splitting) and
  Lemma 7 (pullback) are textbook (Eilenberg–Mac Lane / Brown IV.3) and already carried by the note's Thm
  A + "$\gamma$ is a cocycle" lemma. The novelty is *placement*: identifying the note's $[\gamma]$ with
  the extension class of the dihedral $(\star)$ and reading non-splitting as the $4\mid n$ inventory line.
- **Band stratum.** Everything here is the band-trivial (stratum-3) obstruction. For $K = D_n$ the band is
  automatically trivial: $\operatorname{Out}(D_n)$ enters stratum 2, but the inventory transport we use is
  inner-valued ($\rho$ lands in $\operatorname{Inn}K$ by construction), so $\beta = 0$. No stratum-2
  interference; cf. band-boundary node.
- **"Essentially nonzero" quantifier.** We prove existence of an obstructing $(\mathcal C, \rho)$ for
  $4\mid n$ and non-existence for $4\nmid n$. The canonical realiser is $\mathcal C = B(\operatorname{Inn}D_n)$,
  $\rho = \mathrm{id}$. This matches the note's "$\exists(\mathcal C,\rho): [\gamma]\ne 0$" reading of N2.

---

## 7. Registry action

Promote `thm-D-nonvacuous-criterion` from **computed** to **proved** (own-verification), recording:
(i) $K(n) = D_n$ with the centre/inner arithmetic of Lemmas 2–3; (ii) Corollary 5 split $\iff 4\nmid n$
via the centre-count Theorem 4; (iii) Lemmas 6–7 identification (classical, cited); (iv) the
$D_6 = \mathbb Z/2\times S_3$ split witness for N2. Record the $4\mid n$ table and
`scratch/dihedral_split_verify.py`. Keep the general biconditional RETRACTED; the proved statement is the
sharp one (non-split $\iff 4\mid n$), with "nonabelian + nontrivial centre" demoted to *necessary only*.
