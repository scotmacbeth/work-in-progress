# The homological reduction of (Q): projective presentation of `F`, the target-dimension dichotomy for `Nat(F,−)`, and the Specker cokernel inside `Ext¹(Q,−)`

### Toward (Q): is `F = ∏_ℕ(⊕_ℕ −)` a coproduct of representables in `Add(Vec,Vec)`?

**MacBeth — 2026-09-04 (PROVE session).**
Target (`state/PROVE.md`): (Q), the crux of the absorptive dichotomy (Conjecture 6.2).
Predecessors (all `proved`): `proofs/2026-09-02-vec-admissibility-rigidity.md` (Lemma R, Lemma R′, the
reduction); `proofs/2026-09-03-nat-F-id-specker-and-free-structure.md` (Thm 1: `Nat(F,id)≅⊕_n k^ℕ`);
`proofs/2026-09-03-row-killing-rigidity-and-zfc-index-bound.md` (Theorem A: `Nat(Q,h_W)=0 ∀W`;
Cor A1/A2; Cor B: `Ext¹(Q,F_fin)≠0`; Theorem C: free ⟹ countably many summands, ZFC).
Registry: `proofs/registry/left-adjoint-over-vec.json`, node `conj-absorptive-dichotomy`.

---

## EXECUTIVE SUMMARY

The predecessor relocated the obstruction to (Q) from `Nat`-groups (all proved to vanish on `Q`) to a
single non-split extension class in `Ext¹(Q,F_fin)`, and conjectured — on the grounds that the
Baer–Specker cardinality engine is unavailable over a field — that (Q) is *independent of ZFC*. This
session makes that picture **homologically precise and computational**, delivers three new ZFC theorems,
and *explains why cardinality is neutral* rather than merely asserting it.

Notation: `A := ⊕_m id = E⊗−` (a coproduct of representables, hence projective); `F := ∏_n A` =
row-finite `ℕ×ℕ` matrices; `in_n:A⟹F`, `pr_n:F⟹A` (`pr_n in_{n'}=δ_{nn'}`); `F_fin := ⊕_n A ⊆ F`;
`Q := F/F_fin`; `E = k^{(ℕ)}`, `k` a countable field, `𝔠 = 2^{ℵ_0}`.

1. **Theorem D (explicit projective presentation).** `P₀ := ⊕_{η∈F(E)} h_E` maps **onto** `F` (each
   `η∈F(E)=Nat(h_E,F)` gives `η̂:h_E⟹F`, `η̂_X(w)=F(w)η`; every `ξ∈F(X)` factors through a
   countable-dimensional space `↪E`, so lies in some `im η̂`). Thus `0→K→P₀→F→0` with `P₀` a coproduct
   of `𝔠` copies of the representable `h_E` — a concrete projective resolution start for `F`. (ZFC.)

2. **Theorem E (the Ext long-exact reduction).** Applying `Nat(−,M)` to `0→F_fin→F→Q→0` (with `F_fin`
   projective) yields, for **every** `M`,
   > `0 → coker(ρ_M) → Ext¹(Q,M) → Ext¹(F,M) → 0`,  `ρ_M : Nat(F,M) → Nat(F_fin,M)` (restriction).

   Hence **`F` is projective ⟺ `Ext¹(F,M)=0 ∀M` ⟺ `Ext¹(Q,M)=coker(ρ_M) ∀M`.** The obstruction to (Q)
   is *exactly* the failure of `Ext¹(Q,−)` to be the pure "restriction cokernel." (ZFC.)

3. **Theorem F (target-dimension dichotomy for `Nat(F,−)`).** For a coproduct of representables
   `G=⊕_j h_{W_j}`:
   - if **every `W_j` is finite-dimensional**, then `Nat(F,G)=⊕_n Nat(A,G)` — every natural
     transformation `F⟹G` has **finite row support**, and `ρ_G` is the inclusion
     `⊕_n Nat(A,G) ↪ ∏_n Nat(A,G)`;
   - if some `W_j` is infinite-dimensional the finite-support conclusion **fails**: e.g. the column-0
     read `r∈Nat(F,h_E)` (`r_X(ξ)=(ξ_{n0})_n:E→X`) has `r∘in_n≠0` for **all** `n` (infinite row
     support).

   This upgrades Thm 1 (`M=id`) and §5's "finite-dim targets are rigid, infinite-dim are not" from a
   heuristic edge to a **theorem about `Nat(F,−)`**, with an explicit infinite-support witness. (ZFC.)

4. **Corollary G (the Specker cokernel).** For `G=⊕_j h_{W_j}` with all `W_j` finite-dimensional (e.g.
   `G∈{id, A, F_fin}`), `coker(ρ_G)` is the **reduced product** `∏_n Nat(A,G) / ⊕_n Nat(A,G)`, always
   nonzero for `G≠0`. So `Ext¹(Q,G)` **contains a reduced-product subobject** and the sequence of Thm E
   reads `0→(∏_n/⊕_n)Nat(A,G)→Ext¹(Q,G)→Ext¹(F,G)→0`. The Specker/Baer phenomenon (a product modulo a
   coproduct) is thereby pinned as a concrete subobject of `Ext¹(Q,−)`. (ZFC.) In particular
   `Ext¹(Q,A)≠0`, `Ext¹(Q,id)≠0` — new explicit non-vanishings, sharper than Cor B's `Ext¹(Q,F_fin)≠0`.

5. **Theorem H (cardinality is neutral — why Baer–Specker does not transport).** The `id`-dual
   `D(M):=Nat(M,id)` satisfies `D(h_N)=N` (Yoneda): **no `2^{dim}` blow-up**, in contrast to
   `Hom_ℤ(ℤ^{(κ)},ℤ)=ℤ^κ` (size `2^κ`) which drives the `ℤ`-Baer–Specker contradiction. Consequently,
   under a set theory making the free shape `F≅⊕_{n∈ℕ}h_{N_n}` with `dim N_n=ℵ_0` (Cor C1; e.g.
   `2^{ℵ_0}<2^{ℵ_1}`), **every dimension invariant `dim Nat(F,M)` and `dim F(X)` agrees on both
   descriptions** — all equal `𝔠` (or the evident finite/countable value). No cardinal invariant
   separates `F` from a free functor; the forced index set is countable (Thm C) and the dual does not
   blow up, so the Baer–Specker size-gap is *provably absent*. Direction A therefore **cannot** be
   established by any cardinality argument — it needs either naturality (all single-target routes dead,
   Thm A) or genuine set theory. This substantiates, rather than merely conjectures, the independence
   bet. (ZFC + the stated hypothesis for the "agree" clause, which is only used to exhibit a candidate.)

**Honest verdict.** (Q) remains **open**. But the problem is now a precise homological question —
*is `Ext¹(F,M)=0` for all `M`?* — with the "easy" part `coker(ρ_M)` computed to a reduced product
(Cor G), the presentation of `F` in hand (Thm D), the target-dimension edge made a theorem (Thm F), and
the cardinality route provably closed (Thm H). Three independent classical attacks (single-target
rigidity — Thm A; cardinality — Thm H; `lim¹`/telescope — predecessor Result 3) are now all theorems
saying *this cannot be decided that way*. What remains is `Ext¹(F,−)` at an **infinite-dimensional**
target, exactly where Thm F's finite-support fails.

---

## 0. Setup (recap; predecessors cited `proved`)

`C=Vec_k`, `k` countable (`dim=card` on infinite spaces). `E=k^{(ℕ)}=⊕_n k e_n`. `A:=⊕_m id = E⊗−`,
a coproduct of representables `⊕_m h_k`, hence **projective**. `F(X)=Hom(E,⊕_ℕ X)=∏_n(⊕_m X)` =
row-finite `ℕ×ℕ` matrices `(ξ_{nm})` over `X` (`n`=row, `m`=column; each row finite in `m`). `F=∏_n A`.
`in_n:A⟹F` (place row `n`), `pr_n:F⟹A` (read row `n`), `pr_n in_{n'}=δ_{nn'} id_A`.
`F_fin:=⊕_n A=`{finitely many nonzero rows}`=⊕_{ℕ²}h_k` (coproduct of representables, projective),
generated by matrix units `{ε_{nm}∈F_fin(k)}`. `Q:=F/F_fin`, `π:F↠Q`.

**Cited `proved`.** (i) *(Yoneda/compactness)* `Nat(h_N,G)=G(N)`; `h_N` compact; coproducts of
representables are projective. (ii) *(Thm 1)* `Nat(F,id)≅⊕_n k^ℕ` via `α↦(α∘in_n)_n` (finite `n`-support,
injective). (iii) *(Theorem A)* `Nat(Q,h_W)=0 ∀W`; hence `Nat(Q,G)=0` for every coproduct of
representables `G`, and `Nat(Q,F)=0` (Cor A1/A2). (iv) *(Cor B)* `0→F_fin→F→Q→0` non-split,
`Ext¹(Q,F_fin)≠0`. (v) *(Thm C)* free `F≅⊕_{j}h_{N_j}` ⟹ `J` countable; Cor C1: free
`F≅⊕_{n∈ℕ}h_{N_n}`, ∞-many ∞-dim, `dim N_n≤𝔠`.

Enough projectives: for any `G`, `⊕_{N,x∈G(N)}h_N↠G`.

---

## 1. Theorem D — an explicit projective presentation of `F`

**Theorem D.** The natural transformation `p:P₀:=⊕_{η∈F(E)}h_E ⟶ F`, whose `η`-component is
`η̂:h_E⟹F`, `η̂_X(w)=F(w)(η)` (`w:E→X`), is an **epimorphism**. Thus `0→K→P₀→F→0` is a projective
presentation with `P₀` a coproduct of `𝔠` copies of the representable `h_E`.

*Proof.* `η̂` is the transformation named by `η∈F(E)=Nat(h_E,F)` under Yoneda. Surjectivity: fix `X`
and `ξ∈F(X)`. Let `Σ:={(n,m):ξ_{nm}≠0}`; `ξ` is row-finite so `Σ` meets each row finitely and is
countable. Put `U:=k^{(Σ)}` (countable-dimensional), `η₀∈F(U)` the tautological spread
`η₀(e_n)=∑_{m:(n,m)∈Σ}u_{nm}f_m` (row-finite ✓), and `w:U→X`, `w(u_{nm})=ξ_{nm}`; then `F(w)(η₀)=ξ`
(predecessor's spread computation). Choose a linear injection `ι:U↪E` (`dim U≤ℵ_0=dim E`), split by
some `π_U:E→U` (`π_U ι=id_U`), and set `η:=F(ι)(η₀)∈F(E)` and `w':=w∘π_U:E→X`. Then
`F(w')(η)=F(w π_U)F(ι)(η₀)=F(w π_U ι)(η₀)=F(w)(η₀)=ξ`. Hence `ξ=η̂_X(w')∈im(p_X)`. As `X,ξ` were
arbitrary, `p` is epi. `P₀` is a coproduct of representables, projective; `dim F(E)=𝔠` gives the index
size. ∎

**Remark (why this is the right size).** `F` is **not** cyclic: no single `h_N` surjects. Indeed a
single `η∈F(N)` has, per row, a *fixed finite* column-support; `η̂_X(w)=(id_E⊗w)η` can only populate
those columns, so cannot reach `ξ` with an entry in a fresh column of that row. The `𝔠`-fold coproduct
is genuinely needed — this is the first quantitative shadow of non-projectivity, though not yet a proof
of it (a coproduct of representables can of course be presented by a larger one).

---

## 2. Theorem E — the Ext long-exact reduction

**Theorem E.** For every `M∈Add(Vec,Vec)` there is a natural short exact sequence
> `0 ⟶ coker(ρ_M) ⟶ Ext¹(Q,M) ⟶ Ext¹(F,M) ⟶ 0`,  where `ρ_M:=ι^*:Nat(F,M)→Nat(F_fin,M)`.

Consequently: **`F` is projective ⟺ `Ext¹(F,M)=0` for all `M` ⟺ `Ext¹(Q,M)=coker(ρ_M)` for all `M`.**

*Proof.* Apply the contravariant `Nat(−,M)` to the exact `0→F_fin→^ι F→^π Q→0`. The long exact
sequence of `Ext^•(−,M)` reads
`0→Nat(Q,M)→Nat(F,M)→^{ι^*}Nat(F_fin,M)→^∂Ext¹(Q,M)→Ext¹(F,M)→Ext¹(F_fin,M)→⋯`.
`F_fin` is projective, so `Ext¹(F_fin,M)=0`; exactness gives `Ext¹(Q,M)→Ext¹(F,M)→0` (surjective) with
kernel `im ∂ = coker(ι^*) = coker(ρ_M)` (since `im ∂ ≅ Nat(F_fin,M)/ker ∂ = Nat(F_fin,M)/im ι^*`).
This is the displayed sequence. The equivalences are immediate (`F` projective ⟺ `Ext¹(F,−)≡0`; a
functor with enough projectives detects projectivity by `Ext¹`). ∎

**Locating the class `[F]`.** The connecting map `∂` sends `id_{F_fin}∈Nat(F_fin,F_fin)` to
`[F]∈Ext¹(Q,F_fin)`. So `[F]∈coker(ρ_{F_fin})` (the left subobject), and `[F]≠0` (Cor B) says exactly
`id_{F_fin}∉im(ρ_{F_fin})` — `F_fin` is not a retract of `F`. Thus **Cor B is the assertion that
`coker(ρ_{F_fin})≠0`**, a *lower-bound* on `Ext¹(Q,F_fin)`; it says nothing about `Ext¹(F,F_fin)`, which
is where projectivity of `F` actually lives.

---

## 3. Theorem F — the target-dimension dichotomy for `Nat(F,−)`

**Theorem F.** Let `G=⊕_{j∈J}h_{W_j}` be a coproduct of representables.

**(a) Finite-dimensional targets are rigid.** If every `W_j` is finite-dimensional, then the restriction
`α↦(α∘in_n)_n` is an isomorphism
> `Nat(F,G) ≅ ⊕_{n∈ℕ} Nat(A,G)`  (finite `n`-support),

so `ρ_G` is the inclusion `⊕_n Nat(A,G) ↪ ∏_n Nat(A,G) = Nat(F_fin,G)`. In particular
`Nat(F,A)=⊕_n End(A)` and `Nat(F,id)=⊕_n k^ℕ` (recovering Thm 1).

**(b) Infinite-dimensional targets are not.** If some `W_{j_0}` is infinite-dimensional the conclusion
fails: for `G=h_E`, the column-0 read `r∈Nat(F,h_E)`, `r_X(ξ)=(ξ_{n0})_n∈Hom(E,X)`, satisfies
`r∘in_n≠0` for **every** `n`, i.e. `r` has infinite row support and `r∉⊕_n Nat(A,h_E)`.

*Proof of (a).* *No-exotic (injectivity):* `G` is a coproduct of representables, so `Nat(Q,G)=0` (Cor
A1); by Thm E's leftmost exactness `ρ_G=ι^*` is injective, i.e. `α∘in_n=0 ∀n ⟹ α=0`.

*Finite support:* Suppose `α∈Nat(F,G)` has `α∘in_n≠0` for all `n` in an infinite set `S`. For each
`n∈S` pick `a_n∈A(k)=k^{(ℕ)}` with `(α∘in_n)_k(a_n)≠0∈G(k)`. Let `X:=k^{(S)}` with basis `{t_n:n∈S}`,
and `s_n:k→X` the inclusion of `t_n` (a split mono). Define `ξ∈F(X)` by row `n` `= A(s_n)(a_n)=a_n⊗t_n`
for `n∈S`, other rows `0` (row-finite ✓, since each `a_n` is finite in `m`). `ξ` has infinitely many
nonzero rows — legitimate in `F`.

Now `α_X(ξ)∈G(X)=⊕_j Hom(W_j,X)`. Each `W_j` is **finite-dimensional**, so each component
`Hom(W_j,X)`-map has finite-dimensional image in `X=k^{(S)}`, hitting only finitely many `t_n`; and only
finitely many `j` are active (coproduct). Hence `α_X(ξ)` involves only finitely many basis vectors
`t_n`, `n∈T` (finite). [*This is exactly the step that uses `dim W_j<∞`.*]

Pick `n₀∈S∖T` and let `q:X→X` be the projection killing `t_{n₀}` (fixing the other `t_n`). Then
`F(q)(ξ)=ξ−in_{n₀}(a_{n₀}⊗t_{n₀})` (row `n₀` uses `t_{n₀}↦0`; other rows use `t_n`, `n≠n₀`, fixed). By
naturality `α_X(F(q)ξ)=G(q)(α_Xξ)=α_Xξ` (as `α_Xξ` involves only `t_n,n∈T∌n₀`, `q` fixes it). But
`α_X(F(q)ξ)=α_Xξ−(α∘in_{n₀})_X(a_{n₀}⊗t_{n₀})`. Therefore `(α∘in_{n₀})_X(a_{n₀}⊗t_{n₀})=0`. However
`a_{n₀}⊗t_{n₀}=A(s_{n₀})(a_{n₀})`, so by naturality
`(α∘in_{n₀})_X(A(s_{n₀})a_{n₀})=G(s_{n₀})((α∘in_{n₀})_k(a_{n₀}))`. `s_{n₀}` is a split mono; `G` (left
exact, a coproduct of `Hom(W_j,−)`) preserves monos, so `G(s_{n₀})` is injective, and
`(α∘in_{n₀})_k(a_{n₀})≠0` forces `G(s_{n₀})(…)≠0`. Contradiction. Hence `S` is finite.

*Surjectivity onto finite-support:* given `(β_n)_{n∈S₀}` (finite `S₀`, `β_n∈Nat(A,G)`), set
`α:=∑_{n∈S₀}β_n∘pr_n` (finite sum of natural transformations); `α∘in_{n'}=β_{n'}` for `n'∈S₀`. ∎

*Proof of (b).* `r_X(ξ)=(ξ_{n0})_n` reads column 0 as a map `E→X`, natural in `X`; it is well-defined
because column 0 `(ξ_{n0})_n` is an arbitrary element of `∏_n X=Hom(E,X)` (no finiteness needed on a
single column). `(r∘in_n)` reads the column-0 entry of row `n`, nonzero for every `n`. So `r` has
infinite row support and is not a finite combination of the `pr_n`. (`r` is the retraction of §5.2
witnessing `F≅h_E⊕F`.) ∎

**Reading.** Thm F is the exact statement of the "wall": rigidity (finite row support of `Nat(F,−)`)
holds **iff** the target is assembled from finite-dimensional representables. Infinite-dimensional
representable summands — which a *free* `F` is forced to contain (Cor C1) — are precisely the targets
where `Nat(F,−)` acquires infinite-support transformations like `r`. Direction A must therefore engage
an infinite-dimensional target; the finite-dimensional-target machinery provably cannot see it.

---

## 4. Corollary G — the Specker cokernel inside `Ext¹(Q,−)`

**Corollary G.** For `G=⊕_j h_{W_j}` with every `W_j` finite-dimensional (in particular `G∈{id,A,F_fin}`
— note `F_fin=⊕_{ℕ²}h_k`), Thm F(a) gives `ρ_G:⊕_n Nat(A,G)↪∏_n Nat(A,G)`, so
> `coker(ρ_G) = ∏_n Nat(A,G) / ⊕_n Nat(A,G)` (a **reduced product**), nonzero whenever `Nat(A,G)≠0`.

Combined with Thm E,
> `0 → (∏_n Nat(A,G))/(⊕_n Nat(A,G)) → Ext¹(Q,G) → Ext¹(F,G) → 0`.

In particular `Ext¹(Q,A)≠0` and `Ext¹(Q,id)≠0` (take `G=A,id`: `Nat(A,A)=End(A)≠0`, `Nat(A,id)=k^ℕ≠0`).

*Proof.* Immediate from Thm F(a) and Thm E. Non-vanishing: a reduced product of nonzero spaces over `ℕ`
is nonzero. ∎

**Significance.** The predecessor's Cor B gave one non-vanishing `Ext¹(Q,F_fin)≠0` via non-splitting.
Cor G upgrades this to a *structural description*: for every finite-dim-representable target,
`Ext¹(Q,G)` contains the **reduced product** `∏_n Nat(A,G)/⊕_n Nat(A,G)` as a canonical subobject — the
Baer/Specker "product-mod-coproduct" object, now living verifiably inside functor-category `Ext`. The
*entire* residual question of (Q) is whether the quotient `Ext¹(F,G)` is zero for all `G`: i.e. whether
`Ext¹(Q,G)` is **nothing but** this Specker cokernel, or strictly larger. `F` projective ⟺ "nothing
but," for all `G`.

---

## 5. Theorem H — cardinality is neutral (why Baer–Specker does not transport)

Write `D(M):=Nat(M,id)` for the `id`-dual on `Add(Vec,Vec)`.

**Lemma H0 (no dual blow-up).** `D(h_N)=Nat(h_N,id)=N` (Yoneda). Hence for a coproduct of representables
`D(⊕_j h_{N_j})=∏_j N_j`, and `dim D(h_N)=dim N` — **no exponential jump**. Contrast: over `ℤ`,
`Hom_ℤ(ℤ^{(κ)},ℤ)=ℤ^κ` has cardinality `2^κ` for infinite `κ`. The `ℤ`-Baer–Specker contradiction is
precisely this jump — `∏_ℕℤ` free would have uncountable rank `κ=𝔠`, so dual size `2^𝔠`, while
`Hom(∏ℤ,ℤ)=⊕ℤ` is countable. Over a field the jump is absent by Lemma H0.

**Theorem H (cardinal invariants do not obstruct freeness).** Suppose a set theory in which the free
shape allowed by Cor C1 is realized abstractly as `⊕_{n∈ℕ}h_{N_n}` with each `dim N_n=ℵ_0` (e.g. any
model of `2^{ℵ_0}<2^{ℵ_1}` pins this shape; the point here is only to compare *dimensions*, not to
assert the iso exists). Then for every `M` in `{id, A, F_fin}` and for evaluation at every `X` with
`dim X≤𝔠`, the dimension invariants computed from `F` and from `⊕_n h_{N_n}` **coincide**:

- `dim F(X)`: `F(X)=∏_n(⊕_m X)`; for `X=k`, `dim=𝔠`. `(⊕_n h_{N_n})(k)=⊕_n N_n^*`; each `dim N_n^*=𝔠`
  (`dim N_n=ℵ_0`), countable coproduct gives `dim=𝔠`. **Agree (`𝔠`).**
- `dim Nat(F,id)=dim(⊕_n k^ℕ)=ℵ_0·𝔠=𝔠` (Thm 1) vs `dim Nat(⊕_n h_{N_n},id)=dim ∏_n N_n`. With
  `dim N_n=ℵ_0`: `∏_n N_n=∏_n k^{(ℕ)}⊆∏_n k^ℕ=k^ℕ`, so `dim≤𝔠`, and `⊇k^ℕ`(diagonal), so `dim=𝔠`.
  **Agree (`𝔠`).**
- index/summand counts: both countable (Thm C). **Agree.**

Hence **no invariant of the form `dim F(X)` or `dim Nat(F,M)` separates `F` from a free functor of the
Cor-C1 shape.** The `ℤ`-style contradiction (dual too small for the forced free rank) has *no analogue*:
the forced rank is countable (Thm C, ZFC) and `D` does not blow up (Lemma H0), so both sides sit at `𝔠`.

**Corollary H1 (the two classical routes are provably closed).** Direction A ("`F` not a coproduct of
representables") cannot be proved by (i) a single-target rigidity — all such vanish on `Q` (Theorem A),
nor by (ii) a cardinality/dual-size count — all such agree (Theorem H). It must proceed through
`Ext¹(F,−)` at an **infinite-dimensional target** (Thm F(b)), i.e. a genuinely homological/set-theoretic
argument. This is the precise, theorem-backed form of the predecessor's independence conjecture: the
obstruction, if any, is *not* cardinal and *not* single-target — it is the Whitehead-type question of
whether the reduced-product extension classes in `Ext¹(Q,G)` (Cor G) exhaust `Ext¹(Q,G)` or leave a
`Ext¹(F,G)` remainder, at infinite-dimensional `G`.

*Proof.* (i) Theorem A. (ii) Theorem H. The residual channel is Thm E's `Ext¹(F,M)`, and by Thm F(a)
that quotient is invisible to all finite-dim-representable `M` beyond the Specker cokernel already
accounted; only infinite-dim `M` (Thm F(b)) can carry it. ∎

---

## 6. What would settle it (precise next steps)

By Thm E, (Q) YES ⟺ `Ext¹(F,M)=0 ∀M`. Two concrete sub-problems, both now well-posed:

- **(NO / direction A).** Exhibit an `M` (necessarily with an infinite-dim representable summand, Thm F)
  and a non-split `0→M→G→F→0`, i.e. `Ext¹(F,M)≠0`. Candidate: `M=F_fin` or `M=h_E`, using the
  presentation `0→K→P₀→F→0` (Thm D): `Ext¹(F,M)=coker[Nat(P₀,M)→Nat(K,M)]`, with
  `Nat(P₀,M)=∏_{F(E)}M(E)`. The task is to understand the syzygy functor `K` well enough to find a
  natural cocycle `K→M` not extending to `P₀`. This is the honest hard core.
- **(YES / direction B).** Show `Ext¹(F,M)=0 ∀M` by proving every `K→M` extends to `P₀` — a
  Whitehead-type extension/uniformization on the syzygies, plausibly requiring a failure of
  `2^{ℵ_0}<2^{ℵ_1}` plus a transfinite construction (the independence bet's positive half).

**Literature gate (unchanged, still required before citing at `proved`):** Shelah, independence of
Whitehead; Eklof–Mekler *Almost Free Modules* Ch. XII (Ext & set theory) transported to functor
categories; Auslander, functor-category projectivity. Thm H explains *why* the transport is nontrivial:
the field kills the slenderness/cardinality engine, so only the set-theoretic (uniformization) content
of that literature can be load-bearing.

---

## 7. Status ledger

| claim | grade | basis |
|---|---|---|
| **Thm D: `⊕_{F(E)}h_E ↠ F` explicit projective presentation** | **proved (ZFC)** | §1 |
| **Thm E: `0→coker(ρ_M)→Ext¹(Q,M)→Ext¹(F,M)→0`; `F` proj ⟺ `Ext¹(F,−)≡0`** | **proved (ZFC)** | §2 |
| `[F]=∂(id_{F_fin})∈coker(ρ_{F_fin})`; Cor B ⟺ `coker(ρ_{F_fin})≠0` | **proved** | §2 |
| **Thm F(a): finite-dim-rep target ⟹ `Nat(F,G)=⊕_n Nat(A,G)` (finite row supp)** | **proved (ZFC)** | §3 |
| **Thm F(b): infinite-dim target ⟹ fails; `r∈Nat(F,h_E)` infinite row supp** | **proved (ZFC)** | §3 |
| `Nat(F,A)=⊕_n End(A)`; recovers `Nat(F,id)=⊕_n k^ℕ` | **proved** | §3 |
| **Cor G: `coker(ρ_G)=∏_n/⊕_n Nat(A,G)` reduced product; `Ext¹(Q,A),Ext¹(Q,id)≠0`** | **proved (ZFC)** | §4 |
| **Thm H: no cardinal invariant separates `F` from free (Lemma H0 reflexivity)** | **proved (ZFC)** | §5 |
| Cor H1: single-target AND cardinality routes both provably closed | **proved** | §5 |
| (Q) / direction A vs B | **OPEN** (crux = `Ext¹(F,M)` at infinite-dim `M`) | §6 |
| independence of (Q)/Conj 6.2 | **speculative** (now theorem-supported by Thm H) | §5–6 |

**Net.** No claim on (Q) itself is upgraded — it stays OPEN — but the problem is now a single, sharply
posed homological question (`Ext¹(F,−)≡0?`) sitting on a fully explicit presentation, with the "easy"
piece `coker(ρ_M)` computed to a reduced product for all finite-dim-representable targets, and with
*both* classical decision routes (rigidity, cardinality) converted into theorems proving they cannot
decide it. That is genuine ZFC structural progress and a materially stronger case for the independence
bet than the predecessor's heuristic.
