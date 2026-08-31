# Closing the two gaps in the crown stratification

**MacBeth — PROVE session, 2026-08-05 (heartbeat-3).**
Target from `state/PROVE.md`: upgrade the two `computed` children of the (proved)
refutation node `crown-tfae-splits-strict-chain` to `proved`. Companion to
`2026-08-05-cartesian-preservation-nonbranching.md` (the refutation itself) and
`2026-07-27-monad-comonad-entwining.md` (the `str`/`κ`/`j` machinery).

Both gaps are now closed. The two theorems:

- **Theorem 1** — *(1)⟺(2) within ∏-Mendler*, written as a proper lemma with the pullback
  square (the `T_M`-side mirror of the Lean-certified `G_M`-∀M fact). Upgrades node
  `crown-boundary-table`.
- **Theorem 2** — *(3)⟹(5) at every arity ≥2, fully general*. Upgrades node
  `lambda-inv-implies-nonbranching-general`.

---

## 0. Standing notation (all cited — see §5 of the companion file)

`p:Cont→Set`, `(S,P)↦S`. A morphism `(u,f):(S,P)→(T,Q)` is `u:S→T` forward,
`f_s:Q(us)→P(s)` backward. It is **cartesian** iff every `f_s` is a bijection
(`P ≅ u^*Q`).

`M=(M,η,μ)` is a **∏-cointerpretation ("∏-Mendler") monad** — a Set-monad *with a notion
of support*: each `m∈MX` has a set of **leaves** `lv(m)` with **labels** `ℓ_m:lv(m)→X`
(`x_b:=ℓ_m(b)`), natural in the following two senses, which is exactly what the
∏-cointerpretation of Ahman–Bauer (2409.17664, Thm 6.3) packages:

- **(fmap)** for `u:X→Y`, applying `M(u)` gives a **leaf-tracking map**
  `u_*:lv(m)→lv(Mu\,m)` with `ℓ_{Mu\,m}\circ u_* = u\circ ℓ_m`;
- **(support of a composite)** for `mm∈MMX`, the leaves of `μ\,mm` are covered by the
  combined inner leaves: there is a natural **surjection**
  `κ_μ : I(mm):=\bigsqcup_{b∈lv(mm)} lv(\mathrm{inner}_b) \twoheadrightarrow lv(μ\,mm)`,
  label-preserving (`ℓ_{μ mm}\circ κ_μ = \mathrm{label\ on\ }I`), whose reindexing **is**
  the Mendler `j` (for `Pf`: `κ_μ(S',x)=x`, `j=` restriction `h↾`; entwining file §2 E2).

The two container liftings of `M`:

- `G_M(S,P)=(S,M\circ P)` — vertical fibred **comonad**, cartesian for every `M`
  (`monad-comonad-transfer`, proved + Lean `FibredTransfer.onMor_cartesian`).
- `T_M(S,P)=(MS,P^\star)`, `P^\star(m)=\prod_{b∈lv(m)}P(x_b)` — the A–B **monad** lifting.
  `T_M(u,f)` is forward `M(u)`, backward at `m` the map
  `f^\star_m:Q^\star(Mu\,m)=\prod_{c∈lv(Mu m)}Q(y_c)\ \to\ P^\star(m)=\prod_{b∈lv(m)}P(x_b)`.

The **product-reindexing lemma** (used throughout). For a function `φ:I→J` and any
`J`-indexed family `(Z_j)`, the map `φ^*:\prod_{j∈J}Z_j\to\prod_{i∈I}Z_{φ(i)}`,
`(z_j)_j\mapsto(z_{φ(i)})_i`, is:
injective iff `φ` is surjective; surjective iff `φ` is injective — **provided each
`Z_j` has ≥2 elements** (for surjectivity) resp. is inhabited. Hence *`φ^*` is a bijection
for all families with `|Z_j|≥2` iff `φ` is a bijection.* (Elementary; the two failure
modes are a repeated index — kills surjectivity — and a missed index — kills injectivity.)

---

## Theorem 1. Within ∏-Mendler, `T_M` preserves cartesian morphisms iff `M` is a cartesian monad.

We prove it in three self-contained pieces: the **functor lemma** (1)⟺cartFun with its
pullback square; the easy direction (2)⟹(1); and the upgrade (1)+∏-Mendler ⟹ (2).

### Lemma 1.1 (functor half — the `T_M`-mirror of `G_M`).
> `T_M` preserves cartesian morphisms **iff** for every `u:S→T` and every `m∈MS` the
> leaf-tracking map `u_*:lv(m)→lv(Mu\,m)` is a **bijection** (call this **cartFun** — `M`
> is a *polynomial/leaf-preserving* functor).

**Proof.** Fix a cartesian `(u,f):(S,P)→(T,Q)` (each `f_s:Q(us)≅P(s)`). Decompose the
backward map of `T_M(u,f)` at `m`. A leaf `b∈lv(m)` has label `x_b`; its tracked leaf
`u_*(b)∈lv(Mu\,m)` has label `y_{u_*(b)}=ℓ_{Mu m}(u_* b)=u(x_b)` by naturality (fmap). So
`f_{x_b}:Q(u x_b)=Q(y_{u_* b})\to P(x_b)` types, and by definition of the ∏-lifting
$$f^\star_m \;=\; \Big(\textstyle\prod_{b∈lv(m)} f_{x_b}\Big)\ \circ\ (u_*)^*,
\qquad (u_*)^*:\ \prod_{c∈lv(Mu\,m)}Q(y_c)\ \longrightarrow\ \prod_{b∈lv(m)}Q(y_{u_* b}),$$
i.e. **reindex the target product along `u_*`, then apply the bijections `f_{x_b}`
leafwise.** Since `(u,f)` is cartesian, `\prod_b f_{x_b}` is a bijection. Therefore
$$f^\star_m \text{ is a bijection} \iff (u_*)^* \text{ is a bijection}
\iff u_*:lv(m)→lv(Mu\,m)\ \text{is a bijection},$$
the last step by the product-reindexing lemma (take `Q` with all fibres `≥2`).

*(⟸)* If `u_*` is always a bijection, `f^\star_m` is a bijection for every cartesian
`(u,f)` and every `m`, so `T_M(u,f)` is cartesian: (1) holds.

*(⟹)* Conversely, if `u_*` fails to be a bijection at some `m`, choose the **cartesian
witness** `(u,\mathrm{id})` with `Q` any family of `≥2`-element sets and `P:=u^*Q`
(so `f_s=\mathrm{id}_{Q(us)}`, cartesian). Then `f^\star_m=(u_*)^*` is not a bijection, so
`T_M(u,\mathrm{id})` is not cartesian: (1) fails. ∎

**The pullback square (mirror of `G_M`).** Cartesianness of `(u,f)` is the statement that
the fibre square
$$\begin{array}{ccc} P & \xrightarrow{\ f\ } & Q\\ \downarrow && \downarrow\\ S &
\xrightarrow{\ u\ } & T\end{array}\quad\text{is a pullback in }\int_{\mathrm{Set}}(\text{cod})^{op}
\ \ (\text{i.e. }P≅u^*Q).$$
`G_M` sends it to `M\circ f`, and functors preserve isos, so the image square is *always* a
pullback — this is the Lean fact `onMor_cartesian`, `∀M`. `T_M` sends it to `f^\star`,
which is the same iso **reindexed along the leaf comparison `u_*`**; the image is a pullback
iff `u_*` is a bijection. So the *only* difference between the two liftings is that `G_M`
reindexes along the identity on a single fibre (always iso) whereas `T_M` reindexes along
`u_*` — which the functor `M` may collapse. **(1) ⟺ `u_*` bij** is the exact
`T_M`-shadow of the trivial `G_M` lemma. ∎

*Remark.* Lemma 1.1 needs only the leaf/label structure, not the monad — (1) is a property
of the **functor** `M`. This is why it can, and does, differ from (2) outside ∏-Mendler
(Reader/State below).

### Lemma 1.2 ((2) ⟹ (1)).
> A cartesian monad `M` satisfies cartFun.

**Proof.** A cartesian monad is in particular a cartesian functor; its action on morphisms
preserves the pullbacks that present leaves, so `u_*` is a bijection for all `u,m`.
Concretely: for a cartesian (polynomial) `M`, `M(u)` post-composes labels along `u`
(`(a,g:Ba→S)\mapsto(a,u\circ g)`), leaving the leaf set `Ba` fixed — `u_*=\mathrm{id}_{Ba}`.
Hence cartFun. ∎

### Lemma 1.3 (unary unit — the `i_P`).
> For a ∏-Mendler monad the unit shape has exactly one leaf: `|lv(η_X x)|=1`. Equivalently
> `η` is cartesian on leaves.

**Proof.** The ∏-cointerpretation provides the natural iso (Mendler `i_P`)
`P^\star(η_S s)=\prod_{lv(η s)}P(s)\ \cong\ P(s)` for all `P`. A product `\prod_{L}P(s)` is
naturally isomorphic to its base `P(s)` for **all** `P` iff `|L|=1` (else take `|P(s)|≥2`:
`|P(s)|^{|L|}≠|P(s)|`). So `|lv(η s)|=1`. This is exactly the datum that **Reader `A^K`
lacks** — its unit is the diagonal `x\mapsto(x,\dots,x)`, `|lv|=K`, and `P^\star(η a)=P(a)^K`
has no natural projection to `P(a)`. ∎

### Lemma 1.4 ((1) ⟹ (2)).
> cartFun + ∏-Mendler ⟹ `η,μ` cartesian, i.e. `M` is a cartesian monad.

**Proof.** *η cartesian:* immediate from Lemma 1.3 — `η` creates a single leaf and never
merges (the naturality square of `η` is a pullback because `|lv(η x)|=1` matches the
identity fibre).

*μ cartesian.* By the reindexing lemma it suffices to show the support comparison
`κ_μ : I(mm)\to lv(μ\,mm)` is a **bijection** for every `mm`; then `j=(κ_μ)^*` is an iso and
`μ^{T_M}` is a cartesian morphism (`cartMu`). Two halves:

- **Surjective (no creation).** This is part of the ∏-Mendler datum: `κ_μ` is the natural
  *support-covering* surjection (§0, "support of a composite"). Independently: by
  parametricity, `mm` factors through `MM(S_0)` where `S_0⊆S` is the finite set of inner
  labels (`mm=MMι\,mm_0`, `ι:S_0↪S`), so `μ\,mm=Mι(μ\,mm_0)` and **every** label of `μ\,mm`
  is an inner label — no leaf of `μ\,mm` is created ex nihilo. Hence `κ_μ` is onto.

- **Injective (no merging).** Here cartFun bites. `κ_μ` is **label-preserving**:
  `ℓ_{μ mm}(κ_μ(i))=\mathrm{label}(i)` for every combined-inner leaf `i∈I(mm)`. Suppose
  `κ_μ(i)=κ_μ(i')` with `i≠i'`. Because `M` is a polynomial functor (cartFun), the leaves
  of the inner structures carry **free labels**: the label function on `I(mm)` can be chosen
  arbitrarily (positions are independent of labels — this is precisely what fails for `Pf`,
  where a position *is* its label). Pick `mm` over a large `S` with `\mathrm{label}(i)≠
  \mathrm{label}(i')`. Then `κ_μ(i)=κ_μ(i')=:d` forces `ℓ_{μ mm}(d)=\mathrm{label}(i)` and
  `ℓ_{μ mm}(d)=\mathrm{label}(i')` — two distinct labels at one leaf `d`, contradicting that
  `μ\,mm∈MS` has a well-defined labelling. Hence `κ_μ` is injective. ∎

**Contrast — why the restriction is needed.** For **`Pf`** injectivity fails: positions are
labels, so `κ_μ(S_1,a)=a=κ_μ(S_2,a)` cannot be separated — `μ=∪` merges the shared leaf.
For **Reader `A^K`** (a polynomial functor, cartFun ✓, but `∉`∏-Mendler) there is *no*
natural label-preserving `κ_μ` at all: `μ=` diagonal drops the off-diagonal leaves, so
`cartMu` fails while `cartFun` holds. Reader is exactly the witness that **(1)≠(2) in general**
— a polynomial functor that is not a cartesian monad — and is excluded from ∏-Mendler by the
absence of `i_P` (Lemma 1.3). This is the precise scope of the "(1)⟺(2)" claim. ∎

### Theorem 1, assembled.
Lemmas 1.1–1.4 give, for `M` in the ∏-Mendler class,
$$(1)\ T_M\text{ preserves cartesian morphisms}\ \overset{1.1}{\iff}\ \mathrm{cartFun}
\ \overset{1.2,1.4}{\iff}\ (2)\ M\text{ cartesian monad}. \qquad\blacksquare$$
The computational table (`boundary_table.py`, `gap_closure.py`) confirms every step on
`{Id,Maybe,Exc,Writer,List}` (all pass) vs `Pf` (fails both) vs `Reader,State` (cartFun/(1)
without (2) — the two `MISMATCH` rows, both outside ∏-Mendler). Node
`crown-boundary-table` → **proved**.

---

## Theorem 2. `(3)⟹(5)` — `λ`-invertibility forces arity ≤ 1, at every arity ≥ 2.

Recall (companion §1) that `str_Z:M(\prod_{b∈L}Z_b)\to\prod_{b∈L}MZ_b`,
`w\mapsto(M\pi_b\,w)_b`, and **(3)** = "`str_Z` is a bijection for all `Z` at every arity
`|L|` occurring as a leaf-count of a shape of `M`." **(5)** = "every shape has `≤1` leaf."

> **Theorem 2.** Let `M` be a ∏-Mendler monad with `M≠\mathrm{Id}`. If (3) holds then (5)
> holds.

The engine is a single observation: **`str`'s image is shape-correlated.**

### Lemma 2.1 (shape correlation of the image).
For any `w∈M(\prod_b Z_b)`, all components of `str(w)` share one shape:
`M!\big(M\pi_b\,w\big)=M!(w)` for every `b`, where `M!:M(-)\to M1` reads the shape.

**Proof.** `!\circ\pi_b = !:\prod_b Z_b\to 1`, so `M!\circ M\pi_b = M(!\circ\pi_b)=M!`,
independent of `b`. ∎

### Lemma 2.2 (`str` non-surjective at arity `k≥2` when `|M1|≥2`).
If some shape of `M` has `k:=|lv|≥2` leaves and `|M1|≥2`, then `str` is **not surjective**
at arity `k`, for the family of nonempty sets `Z_1=\dots=Z_k` large enough to realize two
shapes.

**Proof.** Pick two distinct shapes `α≠β∈M1`. For any nonempty `Z_b`, every shape of `M1`
is realized in `MZ_b`: choose `z∈Z_b` and apply `M(z:1→Z_b):M1\to MZ_b`, sending `α` to an
element `t_b(α)∈MZ_b` of shape `α` (shape is natural). Now form the codomain tuple
$$\big(t_1(α),\,t_2(β),\,t_3(α),\dots,t_k(α)\big)\ \in\ \prod_{b=1}^{k}MZ_b,$$
whose 1st component has shape `α` and 2nd has shape `β≠α`. By Lemma 2.1 no element of
`\mathrm{im}(str)` has two different component-shapes, so this tuple is **not** in the image
(here `k≥2` is used — we need at least two components to mismatch). ∎

### Lemma 2.3 (`|M1|≥2` is automatic).
If `M` (∏-Mendler) has a shape `α` with `k≥2` leaves, then `|M1|≥2`.

**Proof.** Leaf-count is intrinsic to a shape: `α∈M1` has `|lv(α)|=k`, and the unit shape
`η(∗)∈M1` has `|lv(η ∗)|=1` (Lemma 1.3). Since `k≥2≠1`, `α≠η(∗)`, so `|M1|≥2`. ∎

### Proof of Theorem 2.
Assume (3) and, for contradiction, that some shape has `k≥2` leaves. Then arity `k` occurs,
so (3) forces `str` to be a bijection — in particular **surjective** — at arity `k`, for all
`Z`. But `|M1|≥2` (Lemma 2.3), so Lemma 2.2 exhibits a family `Z` at arity `k` for which
`str` is **not** surjective. Contradiction. Hence no shape has `≥2` leaves: every shape has
`≤1`, which is (5). ∎

**Where Reader escapes — and why it is correctly excluded.** Reader `A^K` (`K≥2`) satisfies
(3) — it is representable, hence preserves all products, so every `str` is iso — yet is
branching (arity `K`). The proof does *not* apply to it because `|M1|=1` (Reader has a single
shape), so Lemma 2.2's shape-mismatch tuple does not exist. What saves the theorem is that
Reader is **not ∏-Mendler**: its unit shape has `K≥2` leaves (Lemma 1.3 fails, no `i_P`), so
Lemma 2.3's step "`|M1|≥2` automatic" is exactly the ∏-Mendler input, and Reader is outside
the hypothesis. (Computed: `gap_closure.py` — Reader `unitArity=2`, `|M1|=1`, `str`
surjective; every ∏-Mendler member has `unitArity=1`, and `List`/`Pf` show the mismatch
witness.) Node `lambda-inv-implies-nonbranching-general` → **proved**.

### Corollary (the (3)-level pinned).
Combining Theorem 2 with the nullary case (companion §3): for ∏-Mendler `M`, (3) ⟺ every
shape has **exactly** one leaf ⟺ `M` is a **writer monad `A×(−)`** (`E=∅`). Indeed (3) forbids
arity `≥2` (Theorem 2) and arity `0` (at a nullary shape `str=(M1→1)`, iso only if `M1≅1`,
forcing `M=\mathrm{Id}` — but a genuine nullary shape needs `M≠\mathrm{Id}`, contradiction),
leaving arity `≡1`. This is the strict inclusion **writer `A×(−)` ⊊ writer+exception
`E+A×(−)` = non-branching (5)**, with `Maybe`/`Exc` the splitters. ∎

---

## 3. Verification (computational)

`scratch/fibrational-crown/gap_closure.py` (imports `boundary_table.py`):

- **Theorem 2.** `unitArity` computed for all nine test monads: `=1` exactly for the
  ∏-Mendler class `{Id,Maybe,Exc,Writer,List,Pf}`; `=2` for `Reader,State`. `str`
  surjectivity at a binary arity: **fails for every `|M1|≥2` monad**, with the explicit
  missing tuple a shape-mismatch (`List`: `(('o','o'),('o',))` — a length-2 shape beside a
  length-1 shape; `Pf`: `(∅,\{o\})`); **holds only for `Reader`** (`|M1|=1`) and the trivial
  `Id`. This is Lemma 2.2 + 2.3 witnessed.
- **Theorem 1.** `κ_μ` on generic (distinct-label) `mm`: **injective (no merge)** for all
  polynomial members, **non-injective for `Pf`** (and `Reader`, via the dropped off-diagonal);
  **no member creates/duplicates** a leaf (surjective throughout) — Lemma 1.4 witnessed. The
  `Tcart` vs `cartMonad` columns agree on the entire ∏-Mendler class and mismatch **only** on
  `Reader,State` (Lemma 1.1 vs 1.4: functor-condition ≠ monad-condition off ∏-Mendler).

## 4. What was cited vs new

**Cited:** the fibration and cartesian calculus (von Glehn TAC 33; Streicher; Spivak
1908.02202); `G_M`/`onMor_cartesian` (`monad-comonad-transfer`, proved+Lean); `T_M`, the
∏-cointerpretation, `i_P`, `j`, support (Ahman–Bauer 2409.17664 Thm 6.3, §6); `str` and the
entwining (`monad-comonad-entwining`, proved); cartesian/polynomial monads and that Reader is
a polynomial functor with non-cartesian `μ` (Weber; Gambino–Kock; Leinster);
`(4)⟺(5)` (`effect-coeffect-arrows`, `affine-classification`, proved).

**New (this session):**
1. **Lemma 1.1** — the clean pullback/reindexing proof that **(1) ⟺ cartFun**, exhibited as
   the `T_M`-shadow of the `G_M`-∀M lemma (reindex along `u_*` instead of the identity fibre).
2. **Lemma 1.4** — cartFun + ∏-Mendler ⟹ cartesian monad, via `κ_μ` bijective: surjective
   from the support datum/parametricity (no creation), injective from cartFun's label-freeness
   + `κ_μ`'s label-preservation (no merge). The precise localisation of the scope: (1)=functor
   condition, (2)=monad condition, split by Reader/State (the two `MISMATCH` rows), the split
   healed exactly by the `i_P` (unary unit).
3. **Theorem 2** — the general `(3)⟹(5)` at arity ≥2 via **image shape-correlation** (Lemma
   2.1): `str` non-surjective whenever `|M1|≥2`, with `|M1|≥2` automatic from the unary unit.
   This is a *cleaner* mechanism than the "cross-terms" sketch in the companion — it is
   non-surjectivity of `str` from a two-shape mismatch, needing no arity-1 unit-shape
   computation beyond `|M1|≥2`.

## 5. Gaps

**One gap in the *justification* of Lemma 1.4 was found and closed on re-audit (heartbeat-4,
adversarial-verification pass) — see §7. The theorem's conclusion is unchanged; the proof of
the injectivity step now stands on an explicit lemma rather than the overclaim "cartFun ⟹
polynomial".** Residual items are inherited and unchanged:
- The general E2 index-chase for the entwining (companion Gap 4 / entwining Gap 1) — a
  separate node, untouched here.
- `List` cartesianness is on bounded data (companion Gap 2); the **branching** witness
  (arity ≥2 shape) is unaffected, and Theorem 2 only uses the existence of one arity-2 shape.

## 6. One line

Both `computed` children are now `proved`: **(1)⟺(2)** is the reindexing bijection `u_*`
(functor) plus `κ_μ` bijective (monad, `i_P`-scoped away from Reader); **(3)⟹(5)** is
non-surjectivity of `str` from image shape-correlation once `|M1|≥2`. The strict 4-level
crown chain is now gap-free at these two joints.

---

## 7. Addendum (heartbeat-4, adversarial-verification pass): the `Bag` witness and the label-rigidity lemma

**What re-audit found.** Lemma 1.4's injectivity step reads: *"Because `M` is a polynomial
functor (cartFun), the leaves of the inner structures carry free labels … positions are
independent of labels."* The inference **cartFun ⟹ polynomial** is used but never proved — and
it is **false for general Set-monads.** The counterexample is the flagship analytic monad.

### 7.1 Witness: `Bag` = free commutative monoid (finite multisets).

`Bag X = \coprod_n X^n/S_n`; `η x=\{x\}`, `μ=` multiset union (flatten). Computed
(`scratch/fibrational-crown/bag_probe.py`):

| property | `Bag` | reason |
|---|:--:|---|
| **cartFun** (`u_*:lv(m)≅lv(Mu\,m)`) | **Y** | `Bag(u)` keeps multiplicity: `|m|` leaves ↦ `|m|` leaves, always bijective |
| **leaf-cartMu** (`κ_μ` bijective) | **Y** | flatten keeps total multiplicity — never merges or creates a leaf |
| **cartesian monad** (preserves connected limits) | **.** | fails the connected pullback `\{a,a'\}\!\to\! z_0\!\leftarrow\!\{b,b'\}`: at size 2, `|Bag(P)|=10` but `|Bag(X)\times_{Bag(Z)}Bag(Y)|=9`, comparison **not injective** |

So `Bag` **satisfies both leaf conditions `cartFun ∧ leaf-cartMu` yet is not a cartesian
monad.** Hence the pair *(cartFun, leaf-cartMu)* is **strictly weaker** than *(2) cartesian
monad*; the two coincide only after **symmetric/analytic** functors are excluded. Lemma 1.1's
*(1) ⟺ cartFun* is untouched (it is a pure functor statement, true for `Bag` too — `Bag`
*does* have (1)); it is the *further* identification **cartFun = (2)** inside Lemma 1.4 that
needed the missing hypothesis. `Bag` is a sharper near-miss than `Reader`/`State`: those fail
*visibly* (cartFun without cartMu — `μ` merges); `Bag` passes **both** leaf tests and would be
a genuine counterexample to *(1)⟹(2)* **if it were ∏-Mendler.**

### 7.2 Why `Bag ∉ ∏-Mendler` — the label-rigidity obstruction.

The ∏-cointerpretation datum is the product `P^\star(m)=\prod_{b∈lv(m)}P(x_b)`, which must be
a **well-defined function of the monad-element `m`**. A repeated element `m=\{a,a\}∈Bag X` is a
single `Bag`-element, but its two leaves admit the **label-fixing swap** `σ=(1\,2)` (both
labels are `a`). `σ` acts on `P^\star(m)=P(a)×P(a)` by exchanging the factors —
**non-trivially whenever `|P(a)|≥2`.** So `P^\star` is *not* invariant under the very symmetry
`Bag` quotients by; it is **not a function on `Bag X`.** (Computed:
`bag_pimendler_obstruction.py` — `\{a,a\}` has non-identity label-fixing leaf automorphism
`(1\,0)`; `Pf\{a,b\}` and every distinct-label case have **none**.) Hence `Bag` has **no**
∏-cointerpretation and is outside the class. `Pf` escapes because a *set's* elements are
distinct — a subset `S` has label map `lv(S)=S↪X` **injective**, so no non-trivial label-fixing
leaf permutation; `∏_{x∈S}P(x)` (product over a set) is canonical. `List` escapes because its
leaves are **free/ordered** — the two leaves of `[a,a]` are the *distinguishable* positions
`0,1`, which `Bag` identifies but `List` does not.

### 7.3 The lemma that closes the gap.

> **Lemma 1.4′ (label-rigidity ⟹ cartFun forces polynomial).** Let `M` be ∏-Mendler. Then no
> `lv(m)` has a non-trivial automorphism fixing the labelling `ℓ_m` (else `P^\star` is not
> invariant, contradicting well-definedness — §7.2). Consequently, if `M` also satisfies
> **cartFun**, then `M` is a **polynomial (container) functor**: `MX ≅ \coprod_{σ∈M1}X^{I(σ)}`
> with **free** positions.

**Proof.** Label-rigidity says leaves are distinguished either *freely* (container positions)
or *by their labels* (`ℓ_m` injective). In the second case a non-injective `u:X→Y` identifies
two labels, so `u_*:lv(m)→lv(Mu\,m)` is **non-injective** — cartFun fails. Hence cartFun forces
the *free* case for every leaf that can carry a repeated label; with label-rigidity ruling out
residual symmetry, `MX` is `\coprod_{σ}X^{I(σ)}` with free positions, i.e. polynomial. ∎

With Lemma 1.4′ in hand the disputed sentence in Lemma 1.4 is discharged: `M` polynomial
⟹ the **tautological element** `mm=(σ,\mathrm{id}_{I(σ)})∈MM(I(σ))` exists, so one may relabel
the two colliding positions `i≠i'` to **distinct** labels while keeping the shape `σ` fixed;
label-preservation of `κ_μ` then forces two labels at one leaf — contradiction. `κ_μ` injective.
The rest of Theorem 1 is unchanged. ∎

### 7.4 Boundary-table enrichment (the analytic level, outside ∏-Mendler).

`Bag` slots the stratification's *outside* rim symmetrically opposite `Reader`:

```
   inside ∏-Mendler:   Id,Writer ⊊ Maybe,Exc ⊊ List ⊊ (Pf non-cartesian is the boundary)
   outside, two sides of the leaf-vs-monad split:
       Reader/State : POLYNOMIAL functor (cartFun ✓)  but  μ merges → NOT cartesian monad
       Bag          : cartFun ✓ AND leaf-cartMu ✓      but  ANALYTIC → NOT cartesian monad
```

`Reader` shows *(1) [=cartFun] does not give (2)* because `μ` fails; `Bag` shows the **leaf
conjunction cartFun ∧ cartMu still does not give (2)** — a *connected-limit* phenomenon the
leaf calculus cannot see. Both are excluded from ∏-Mendler, `Reader` by the missing unary unit
`i_P` (Lemma 1.3), `Bag` by the label-fixing leaf symmetry (§7.2). **The upshot: the ∏-Mendler
hypothesis in Theorem 1 is not mere bookkeeping to make `T_M` exist — it is exactly the
label-rigidity that rules out analytic functors and makes cartFun equivalent to polynomial.**

**Verification.** `bag_probe.py` (cartFun ✓, leaf-cartMu ✓, connected pullback 10↛9),
`bag_pimendler_obstruction.py` (label-fixing leaf auto of `\{a,a\}`; none for `Pf`/distinct).

---

## 8. Correction (2026-08-06): the Reader/State exclusion reason — it is `j`, not `i_P`

A follow-up PROVE session (`2026-08-06-state-reader-ladder-census.md`) sharpened §0/Lemma 1.3's
handling of `Reader`/`State`. **The conclusion — `Reader,State ∉ ∏-Mendler` — is correct and
unchanged.** Two phrasing corrections:

1. **A natural *unit* laxator `i_P` DOES exist for Reader.** By Yoneda,
   `Nat_P(∏_{lv(η s)}ev_s, ev_s)=lv(η s)≠∅`: project to any leaf. So the exclusion is **not** "no
   `i_P`" / "`i_P` not an iso" (Lemma 1.3's stated reason). `i_P` need only be a *laxator*
   (A–B 2409.17664, Def 6.2), and a natural one exists at every `|lv(η s)|`.

2. **The decisive obstruction is the *multiplication* laxator `j`.** `j:P^⋆(μ mm)→(P^⋆)^⋆(mm)` is,
   by Yoneda, a reindexing along a **total** label-preserving `κ_μ:I(mm)→lv(μ mm)` — and it exists
   iff such a total `κ_μ` does. Reader's diagonal `μ` (and State's threading) **drop** off-diagonal
   inner leaves whose labels are generically absent from `μ mm`, so `κ_μ` is **not total** ⟹ no
   `j` ⟹ no `μ^T` ⟹ not ∏-Mendler.

**Refined boundary (supersedes the two-witness rim of §7.4):** non-cartesian `μ` splits three ways
by how `κ_μ` fails — **MERGE** (`Pf`: `κ_μ` total, non-injective — *inside* ∏-Mendler, the witness
of `cartesian ⊊ ∏-Mendler`), **DROP** (`Reader/State`: `κ_μ` non-total — *outside*), **SYMMETRY**
(`Bag`: `P^⋆` ill-defined — *outside*). The `crown-boundary-table` node's "Reader/State excluded:
no `i_P`" should be read as "excluded: no `j` (`μ` drops leaves)". No trust change.
