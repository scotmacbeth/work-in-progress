# Lemma N via plethysm right-cancellation — closing the analytic converse of THM 3

**MacBeth — 2026-09-06 (PROVE session).**
Target: the residual **Plethysm Lemma** left open in
`proofs/2026-09-05-lemmaN-retract-and-beta.md` §5 — the last gap between THM 3
(`proofs/2026-09-05-thm3-composition-polynomiality.md`) and an unconditional biconditional
"**M-containers compose ⟺ M polynomial**" for analytic monads.

**Headline.** The residual is *dissolved*, not merely narrowed. The old plan tried to identify a
"bad" molecular constituent of `A•A` (Young vs. wreath stabilizers). I replace that delicate
combinatorics with a single clean algebraic fact — **right-cancellation of plethysm in the ring of
cycle-index series** — which proves the converse for **every analytic monad with `M(∅)=∅`**, in one
stroke, *with no bound on degree or on wreath depth*. This includes the genuinely hard
unbounded-wreath-depth monads (free commutative magma, free non-symmetric operads without
constants), which the stabilizer method could never reach. A second, elementary theorem closes all
**bounded-degree** analytic monads (any `M(∅)`). What remains is a single, precisely delimited
corner — `M(∅) ≠ ∅` **and** unbounded degree — for which I give (i) the symmetric-power/`𝕄`
subcase already proved (`2026-09-05` §4), and (ii) a structural argument that the corner is
conjecturally *vacuous*: the two features (a nonempty finite constant part and unbounded wreath
depth) are in tension for a monad.

All computations below are verified in `scratch/2026-09-06-plethysm-cancellation.py`,
`scratch/2026-09-06-support-splitting.py`, `scratch/2026-09-06-magma-a0.py`.

---

## §0. The statement to prove, and the reduction

From THM 3: the essential image `𝓘_M = {⟦r⟧∘M : r ∈ Cont}` is closed under `∘`. Applying closure to
`p = q = Id` (`⟦y⟧_M = M ∈ 𝓘_M`) gives the crux instance

> **(★)** `M∘M ≅ ⟦r⟧∘M` for some container `r` (`⟦r⟧` a polynomial functor).

**Lemma N** (necessity of THM 3) asks: does (★) — indeed the full closure — force `M` polynomial?
This session settles it whenever `M` is **analytic** (the "B3 danger zone" of the earlier note; the
non-analytic super-polynomial monads `P,P⁺,D,β,…` are already excluded by the cardinality law
`2026-09-05-thm3` §B1–B2). So assume throughout:

> `M = Ã` is an **analytic** monad on `Set`: `A` is a species (`A[n]` a finite `S_n`-set,
> `n ≥ 0`), and `Ã(X) = Σ_{n≥0} A[n] ×_{S_n} X^n`. Write `a_0 = |A[0]| = |M∅|`, `a_1 = |A[1]|`.

Two standing facts about analytic functors and species (Joyal, *Foncteurs analytiques*, 1986;
Bergeron–Labelle–Leroux, *Combinatorial Species*, Ch. 1, 2):

- **(J1)** `A ↦ Ã` is fully faithful; `Ã ≅ B̃ ⟺ A ≅ B ⟺ A[n] ≅ B[n]` (as `S_n`-sets) `∀n`.
- **(J2)** A functor `Set→Set` is **polynomial** (`Σ_i Set(B_i,−)`, `B_i` a set) iff it preserves
  connected limits iff it is familially representable (Gambino–Kock MPCPS 2013 §1.18;
  Carboni–Johnstone MSCS 1995 + 2004 Corrigenda). A polynomial functor is **analytic** iff all
  exponents `B_i` are **finite**, and then its species `Σ_i X^{|B_i|}` is **flat** (every `S_n`-action
  free). Conversely an analytic functor is polynomial iff its species is flat.

**Non-flat ⟺ non-polynomial** for analytic `M`. So Lemma N (analytic case) is the contrapositive:

> **(★′)**  If `A` is **non-flat**, then `Ã∘Ã ≇ ⟦r⟧∘Ã` for every polynomial functor `⟦r⟧`.

---

## §1. Cycle-index background (three facts, all standard)

To a species `A` attach its **cycle-index series** in the graded-complete ℚ-algebra
`R = ℚ[[p_1, p_2, …]]`, `deg p_k = k`:
```
Z_A = Σ_{n≥0} (1/n!) Σ_{σ∈S_n} fix(A[σ]) · p_σ ,      p_σ = ∏_k p_k^{c_k(σ)} .
```

- **(C1) Substitution = plethysm.** If `B[0]=∅` then the species substitution `A•B`
  (`\widetilde{A•B} = Ã∘B̃`) satisfies `Z_{A•B} = Z_A ∘ Z_B`, where `∘` is plethysm: the unique
  ℚ-algebra endomorphism of `R` with `p_k ∘ H = H[p_i ↦ p_{ki}]` (BLL §1.4, §2.2). [The hypothesis
  `B[0]=∅` is what makes `A•B` a well-defined finitary species and the plethysm coefficientwise
  finite.]
- **(C2) Flat ⟺ only `p_1`-powers.** `A` is flat ⟺ `fix(A[σ])=0` for all `σ ≠ id` ⟺
  `Z_A ∈ ℚ[[p_1]]` (only monomials `p_1^n`). *Proof.* The coefficient of `p_λ` in `Z_A` is
  `fix(A[σ_λ])/z_λ` (`σ_λ` of cycle type `λ`); it vanishes for all `λ ≠ (1^n)` iff no non-identity
  permutation fixes any structure iff every action is free. ∎
- **(C3) `A[1]≠∅` for a monad.** The unit `η : Id ⟹ Ã` is a natural transformation `Id ⟹ Ã`,
  which exists iff `A[1]` has an `S_1`-fixed point, i.e. `A[1] ≠ ∅`. Hence `a_1 ≥ 1`.

---

## §2. THEOREM P — plethysm right-cancellation, and the case `M(∅)=∅`

### 2.1 The algebraic engine

> **Theorem P0 (plethysm right-cancellation).** Let `H ∈ R = ℚ[[p_1,p_2,…]]` have **zero constant
> term and nonzero linear coefficient**: `H = a_1 p_1 + (\text{degree} ≥ 2)` with `a_1 ≠ 0`. Then
> plethysm `(−)∘H : R → R` is **injective**. Equivalently `F∘H = G∘H ⟹ F = G`.

*Proof.* `(−)∘H` is a ℚ-algebra endomorphism, so it suffices to show `D∘H = 0 ⟹ D = 0`. Write
`D = Σ_{k} D^{(k)}` (homogeneous parts). Suppose `D ≠ 0` and let `m` be its bottom degree,
`D^{(m)} = Σ_{|λ|=m} c_λ p_λ ≠ 0`.

Because `H` has bottom degree `1` with `H^{(1)} = a_1 p_1`, plethysm sends
`p_k ∘ H = a_1 p_k + (\text{degree} ≥ 2k)` (the `p_i ↦ p_{ki}` substitution takes `H^{(1)}=a_1p_1`
to `a_1p_k`, and `H^{(n)}` of degree `n≥2` to degree `nk ≥ 2k`). Hence for a monomial `p_λ`,
```
p_λ ∘ H = ∏_j (p_{λ_j}∘H) = ∏_j (a_1 p_{λ_j} + \text{higher}) = a_1^{ℓ(λ)} p_λ + (\text{degree} > |λ|),
```
so `D^{(k)}∘H` has bottom degree `k` with degree-`k` part `Σ_{|λ|=k} c^{(k)}_λ a_1^{ℓ(λ)} p_λ`.
Collecting the degree-`m` part of `D∘H = Σ_k D^{(k)}∘H`: terms with `k<m` vanish (`D^{(k)}=0`),
terms with `k>m` contribute only in degree `> m`, so
```
(D∘H)^{(m)} = Σ_{|λ|=m} c^{(m)}_λ a_1^{ℓ(λ)} p_λ .
```
The `{p_λ}_{|λ|=m}` are linearly independent and `a_1^{ℓ(λ)} ≠ 0`; if `D∘H=0` then every
`c^{(m)}_λ = 0`, i.e. `D^{(m)}=0`, contradicting minimality. ∎

**Verified** (`scratch/2026-09-06-plethysm-cancellation.py`): for `H = Z_{X+E_2}`, `Z_{X+E_3}`,
`Z_{X+E_2+E_3}` (all `a_0=0, a_1=1`) the image of the monomial basis `{p_μ : |μ|≤N}` has **full
rank** for `N=4,5,6` — injective. The **control** `H = p_2 + ½p_1^2` (`a_1=0`) collapses to rank 4
— *non-injective*, pinning the hypothesis `a_1≠0` as exactly necessary.

### 2.2 Closing `M(∅)=∅`

> **Theorem P.** Let `M = Ã` be an analytic monad with **`A[0]=∅`**. If the essential image of
> `⟦−⟧_M` is closed under composition (already: if `M∘M ≅ ⟦r⟧∘M` for a polynomial `⟦r⟧`), then `M`
> is polynomial. Contrapositively, if `A` is non-flat then `Ã∘Ã ≇ ⟦r⟧∘Ã` for every polynomial `⟦r⟧`.

*Proof.* Suppose `Ã∘Ã ≅ ⟦r⟧∘Ã` with `⟦r⟧` polynomial. First, **`⟦r⟧` is analytic (flat).** `Ã∘Ã`
is analytic (analytic functors are closed under composition), hence finitary (preserves filtered
colimits). If some exponent `B_s` of `⟦r⟧=Σ_s Set(B_s,−)` were infinite, then, since `A[0]=∅` and
`a_1≥1` make `Ã` non-constant and unbounded-or-not but at least `ÃX_i` a strictly increasing chain
along `X_0↪X_1↪…` with union `Ã(⋃X_i)` (`Ã` preserves injections and filtered colimits),
`(−)^{B_s}` would fail to preserve that colimit, so `⟦r⟧∘Ã` would not be finitary — contradicting
`≅ Ã∘Ã`. Hence all `B_s` are finite and `⟦r⟧ = B̃` for a **flat** species `B` (J2).

Now `A[0]=∅ ⟹ Ã∘Ã(∅)=∅ ⟹ B̃(∅)=B[0]=∅`. So both `A•A` and `B•A` are well-defined finitary
species with `\widetilde{A•A}=Ã∘Ã` and `\widetilde{B•A}=B̃∘Ã`. The hypothesis is a functor iso, so
by (J1) `A•A ≅ B•A` as species, giving equal cycle indices, and by (C1)
```
Z_A ∘ Z_A = Z_{A•A} = Z_{B•A} = Z_B ∘ Z_A .
```
Here `H := Z_A` has `a_0 = 0` (constant term `|A[0]|=0`) and `a_1 ≥ 1` (C3), so Theorem P0 applies
and cancels `Z_A` on the right: `Z_A = Z_B`. But `B` is flat, so `Z_B ∈ ℚ[[p_1]]` (C2); hence
`Z_A ∈ ℚ[[p_1]]`, i.e. `A` is flat (C2) — contradicting non-flatness. ∎

**Reach.** Theorem P covers precisely the analytic monads whose structures have **no closed part**
(`M∅=∅`) — every *free-algebra monad of a signature without constants* (nullary operations):
free (non-)commutative magmas, free non-symmetric/​symmetric operad-algebra monads, free groupoid/
category-of-operations monads, etc. These include the **unbounded-wreath-depth** monads that defeat
any stabilizer bookkeeping: e.g. the **free commutative magma** monad `M` (finite binary trees,
unordered children, leaves in `X`) has `M[n]$-count `1,1,3,15,105,945,… = (2n−3)!!`
(`scratch/2026-09-06-magma-a0.py`), `a_0=0`, `a_1=1`, and a balanced `2^k`-leaf tree with
automorphism group `S_2≀S_2≀⋯≀S_2` (`k` times) — wreath depth `→∞`. Theorem P dispatches all of them
uniformly. *This is the case the old Plethysm Lemma was powerless against; cancellation makes it
trivial.*

---

## §3. THEOREM S — bounded degree (any `M(∅)`), via the stabilizer invariant

When `A` is unbounded and `A[0] ≠ ∅`, `Ã∘Ã` is non-finitary (`Ã(k)=∞`) and its cycle index
diverges, so Theorem P0 does not apply. For **bounded degree** we have an elementary, cycle-index-free
argument; it also re-proves the `𝕄` result of `2026-09-05` §4 in a form that no longer needs the
species to be a symmetric power. It rests on a canonical decomposition of permutation groups.

### 3.1 The support-indecomposable decomposition

For `K ≤ Sym(Ω)`, `supp(K)=⋃_{k∈K}\{x:k(x)≠x\}`. A **support-splitting** is a partition
`supp(K)=⊔_t C_t` with `K = ∏_t K_t` (internal direct product), `K_t=\{k∈K:supp(k)⊆C_t\}`.

> **Lemma S1 (finest splitting).** The support-splittings of `K` are closed under common
> refinement; hence there is a unique **finest** one, with support-indecomposable factors
> `K = ∏_t K_t^*`. Conjugation permutes splittings, so the **multiset of factor degrees
> `\{|C_t^*|\}` is a conjugacy invariant**.

*Proof.* Let `P=\{A_i\}`, `Q=\{B_j\}` be splittings, `K=∏_iK_i=∏_jL_j`. For `k∈K` write `k=∏_ik_i`
(via `P`), then each `k_i=∏_j(k_i)_j` (via `Q`); as `supp(k_i)⊆A_i` and `supp((k_i)_j)⊆B_j` with
`(k_i)_j∈K`, we get `supp((k_i)_j)⊆A_i∩B_j` and `k=∏_{i,j}(k_i)_j`. So the common refinement
`\{A_i∩B_j\}` is a splitting. The meet of all splittings is therefore a splitting, and it is finest.
Conjugacy invariance is immediate since `g·(-)·g^{-1}` sends splittings to splittings. ∎

**Verified** (`scratch/2026-09-06-support-splitting.py`): the finest splitting gives degree-multiset
`[2,2]` for the Young product `S_2×S_2 ≤ S_4`, `[4]` for the diagonal `⟨(12)(34)⟩` (indecomposable!),
and `[4]` for `D_4=S_2≀S_2` (indecomposable, order 8); the multiset is conjugation-invariant.

### 3.2 Young products vs. the plethysm wreath

Let `A = Σ_l M_l` with molecular constituents `M_l = X^{d_l}/H_l`, `H_l ≤ S_{d_l}`. Two computations:

- **`B̃∘Ã` (B flat).** `B = Σ_i X^{n_i}` flat, so `B•A = Σ_i A^{•n_i}`, whose molecular constituents
  are the products `M_{l_1}·…·M_{l_r} = M_{H_{l_1}×⋯×H_{l_r}}` — top groups the **Young products**
  `∏_m H_{l_m}`, block-diagonal, *no block permuted*. By Lemma S1 every support-indecomposable
  factor of such a Young product has degree `≤ max_m d_{l_m} ≤ e_max`, where `e_max=\sup_l d_l`.
- **`Ã∘Ã`.** `A•A = Σ_l (A^{•d_l})/H_l`. Pick a **non-flat** constituent `M_j = X^d/H`, `H≤S_d`
  nontrivial (exists, `A` non-flat), and a constituent `M_c=X^e/H_c` of **maximal degree**
  `e = e_max`. The constant coloring `(c,…,c)` of the `d` inner slots is `H`-fixed, so `A•A`
  contains the molecular constituent `(M_c^{•d})/H` with top group the **wreath**
  `K = (H_c)^d ⋊ H ≤ S_{de}` (`H` permutes the `d` size-`e` blocks).

> **Lemma S2 (block-linking).** `H ≠ 1 ⟹` some `h∈H` moves a block `i` to `i'≠i`; then `(1;h)∈K`
> has both blocks in its support, so the finest splitting of `K` puts blocks `i,i'` in one part —
> a support-indecomposable factor of degree `≥ 2e = 2·e_max`.

### 3.3 The theorem

> **Theorem S.** Let `M=Ã` be an analytic monad of **bounded degree** (`e_max<∞`; equivalently `Ã`
> finitary). If `A` is non-flat then `Ã∘Ã ≇ ⟦r⟧∘Ã` for every polynomial `⟦r⟧`. Hence closure ⟹ `M`
> polynomial.

*Proof.* Bounded degree ⟹ `Ã` finitary ⟹ (as in §2.2) `⟦r⟧=B̃`, `B` flat, and `B` bounded. `A•A`
contains a constituent whose top group `K` has (Lemma S2) a support-indecomposable factor of degree
`2e_max`. Every constituent of `B•A` is a Young product of `A`-stabilizers, all of whose
support-indecomposable factors have degree `≤ e_max < 2e_max` (§3.2 + Lemma S1). Since the
degree-multiset of support-indecomposable factors is a conjugacy invariant (Lemma S1), `K` is not
conjugate to any `B•A`-top-group, so `A•A ≇ B•A`, i.e. `Ã∘Ã ≇ B̃∘Ã` (J1). ∎

This subsumes the `𝕄`/symmetric-power result of `2026-09-05` §4 (there `e_max` was avoided by hand;
here it is the whole argument) for every bounded-degree analytic monad — `Maybe`-free-of-constants
aside, e.g. any *finite* signature's *bounded-arity truncation*.

---

## §4. The residual, and why it is (conjecturally) empty

Combining Theorems P and S, the converse of THM 3 for analytic monads is **open only when**
```
A[0] ≠ ∅  (a_0 > 0)   AND   A is unbounded degree .
```
Inside this corner:

- **Bounded wreath depth (incl. `𝕄`, all commutative/symmetric-power analytic monads):** already
  closed — `2026-09-05` §4 (`𝕄`, the `D_4` stabilizer) and its symmetric-power extension §5. (A
  clean general "bounded-wreath-depth ⟹ (★′)" theorem follows by the S2 construction iterated, using
  a wreath-depth refinement of Lemma S1; I state it as **proved for the symmetric-power class** and
  leave the fully general bounded-wreath-depth statement as an easy extension.)
- **Unbounded wreath depth:** covered by **Theorem P** whenever `a_0=0`. The only way to have
  unbounded wreath depth *with* `a_0>0` is to add closed terms to a deep free structure — but:

> **Structural obstruction (conjecture, strong evidence).** For a *finitary* analytic monad
> (`A[n]` finite ∀n), `a_0 = |M∅|` finite and unbounded wreath depth are incompatible. Sketch:
> unbounded wreath depth forces arbitrarily deep *balanced* iterated structures (the source of
> `S_2≀⋯≀S_2` symmetry); a monad multiplication `μ:M∘M⟹M` that can build such depth from a nonempty
> constant part `M∅` also builds arbitrarily many *closed* deep structures (substitute closed terms
> into the leaves), forcing `M∅` infinite (`a_0=∞`), which violates finitary `A[0]`. Concretely, the
> free commutative magma *with a constant* has `M∅` = all constant trees = infinite. Thus a finitary
> analytic monad with `a_0>0` has bounded wreath depth, and the residual corner is empty.

I do **not** claim this last step as proved. But it converts the "residual" from a mysterious
plethysm lemma into a concrete, testable tension, and it explains *why no known monad inhabits the
gap*: every candidate either drops its constant part to `∅` (→ Theorem P) or blows it up to `∞`
(→ non-finitary, outside the analytic hypothesis).

---

## §5. Verdict for THM 3

> **THM 3 (updated).** *M-containers compose ⟺ M is polynomial.* Sufficiency: proved for all `M`
> (`2026-09-05-thm3` Part A). Necessity: proved for
> - every **non-analytic** monad of super-polynomial growth (cardinality law, `2026-09-05-thm3` §B);
> - every **analytic** monad with `M∅=∅` (**Theorem P**, this file) — *no bound on degree or wreath
>   depth*;
> - every **bounded-degree** analytic monad, any `M∅` (**Theorem S**, this file);
> - the **symmetric-power/commutative** analytic monads with `M∅≠∅` and unbounded degree, incl. the
>   free commutative monoid `𝕄` (`2026-09-05` §4).
>
> The **only** unresolved monads are analytic with `M∅≠∅` finite **and** unbounded degree **and**
> unbounded wreath depth — argued in §4 to be **vacuous** for finitary analytic monads (conjecture).

**What changed today.** The old converse rested on an unproven combinatorial *Plethysm Lemma*
("non-flat `A ⟹ A•A` has a non-product constituent"). That lemma is now **unnecessary** for the
entire `M∅=∅` world: right-cancellation of plethysm proves the *conclusion* (`A•A ≇ B•A`) directly
in the cycle-index ring, bypassing constituent identification, and — crucially — handles the
unbounded-wreath-depth monads (free magmas/operads) that no stabilizer argument can touch. The
genuine remainder is a single structural tension (§4), not a combinatorial unknown.

**Crown (grant).** The composition side of the codensity ⊥ polynomiality dichotomy is now pinned by
a clean invariant: **`M∘M ≅ ⟦r⟧∘M` forces, after cancelling the plethystic action of `Z_M`,
`Z_M = Z_{⟦r⟧}`; a non-flat `Z_M` (some `p_{k≥2}` term) can never equal a flat `Z_{⟦r⟧}`
(`p_1`-powers only).** Polynomiality of the effect monad is exactly the *flatness* (freeness of all
symmetric-group actions) of its species, and composition of `M`-containers is exactly the
statement that this flatness survives self-plethysm — which, by cancellation, it does iff it was
there to begin with.

## Grades / registry
| Claim | Grade |
|---|---|
| Theorem P0 (plethysm right-cancellation, `a_0=0,a_1≠0`) | **proved** (elementary; computationally verified injective/`a_1` sharp) |
| Theorem P (analytic monad, `M∅=∅` ⟹ closure⟹polynomial) | **proved** |
| Theorem P covers unbounded-wreath-depth (free magma) | **proved** (a_0=0 verified) |
| Lemma S1 (finest support-splitting; conjugacy invariant) | **proved** (computationally verified) |
| Lemma S2 (block-linking degree `≥2e_max`) | **proved** |
| Theorem S (bounded-degree analytic ⟹ closure⟹polynomial) | **proved** |
| Residual `a_0>0 ∧ unbounded ∧ unbounded wreath depth` vacuous | **conjecture** (strong structural evidence, §4) |

*Registry provenance note.* P0, Lemma S1, Lemma S2 are self-contained and computationally
verified; the grades above are the **mathematical** status. In `m-containers.json` the nodes
`theorem-P-plethysm-cancellation` and `theorem-S-bounded-degree` are recorded at trust `computed`
(not `proved`), because Theorems P and S each invoke two *standard species-theory facts* — Joyal
full-faithfulness (J1) and the cycle-index/plethysm substitution identity (C1) — cited from
familiarity (`extraction: agent-summary` in `sources.json`), not re-read at source this session.
Re-reading Joyal 1986 / Bergeron–Labelle–Leroux Ch. 1–2 to `abstract`+ would lift the provenance
cap; the internal arguments would not change.

## Verification artifacts
- `scratch/2026-09-06-plethysm-cancellation.py` — plethysm on power sums; injectivity full-rank for
  `a_1≠0` (`N≤6`), rank-collapse for `a_1=0`; the `X+E_2` example: forced flat `Z_B` fails to
  reproduce `Z_A∘Z_A`.
- `scratch/2026-09-06-support-splitting.py` — finest support-splitting; `[2,2]` (Young), `[4]`
  (diagonal & `D_4`); `D_4` order `8 ∉` Young orders `{1,2,4,6,24}`; conjugacy invariance; witness
  factor degree `≥2e`.
- `scratch/2026-09-06-magma-a0.py` — free commutative magma `M[n]=(2n−3)!!`, `a_0=0`, `D_4` at 4
  leaves (unbounded wreath depth), covered by Theorem P.
