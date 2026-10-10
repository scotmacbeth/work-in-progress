# Crown Stage 2 — REPAIR: contravariant encoding, the branch-functor no-go, and the false ceiling

**MacBeth — PROVE session, 2026-10-10 (deep work).**
Repairs the three defects Rick's referee report (`proofs/reviews/2026-10-10-crown-stage2-rick.md`,
reviews commit 4136ecf) found in the shipped note `proofs/2026-10-09-crown-stage2-multishape-branch-extension.md`.
The positive core survives; this note makes it correct. Supersedes §2, §2A, §3 (object-vs-morphism claims)
and §4 (ceiling) of the 10-09 note. Grade the registry node `crown-stage2-multishape-branch-extension`
by THIS note, not the shipped prose.

Builds on: Stage 1 (`proofs/2026-10-02-crown-stage1-orientation.md`, **computed**); `Cont(cod)=Fam(cod^op)`
bifibration (`proofs/2026-08-28-cont-cod-fibration.md`, **proved**); Lemma 4.1 coalgebras = copresheaves
(`proofs/2026-10-01-game-comonads-poly.md`, **proved**).
Verification: `scratch/crown_stage2_repair_verify.py` (ALL PASS — reproduces Rick's exact witnesses).

**No external citation needed.** The step (∗) is proved in six lines inside our own category 𝒜 (§1);
Jakl–Reggio arXiv:2603.21841 is *not* used and its citation is dropped (see §5 hygiene).

---

## 0. What was wrong, and the one-line fix

Three defects, all traceable to a single mistake: the shipped note made the encoding functor **covariant**
and then had to patch the variance by hand with a nearest-ancestor retraction `ρ_f`, which does not do
what preimage does.

| Defect | Shipped (10-09) | Status | Repair |
|---|---|---|---|
| **M1** Clause 1 backward map | `Ψ'(f)=(id₁,ρ_f)`, `ρ_f` nearest-ancestor retraction | **false** (neither leg of `ρ_f` is `j⁻¹`) | make `Ψ'` **contravariant**: `Ψ'(f)=(id₁,j)`, `j` the backward position map; reindexing = opcartesian leg = `j⁻¹` (§2). Clause 1 **proved, unconditional**. |
| **M3** `Ψ` on morphisms | `Ψ` defined on objects only | **gap** | **no-go theorem**: `Ψ` admits no functorial action (either variance) encoding the embedding (§3). |
| **M4** `k≥2` "ceiling" | "k-ary power lies beyond `Cont(cod)`" | **false** | `Ψ'_k(T)=(1,{nodes(T)^k})` with backward map `j^k` reproduces the k-ary fibre exactly (§4). Only the narrow "unary `Ψ'` is blind to k-ary" survives, and it is trivial. |

The single fix — **encode contravariantly, carry `j` backward** — is the *same* orientation Stage 1 already
used in its positive match (Lemma 3/§4 of the Stage-1 note carried `j` as the backward map of a reversed
container arrow; the collapse `ρ` appeared there only as the leg that *fails*). So Stage 1 is **not infected**
(§2, cross-check); the shipped Stage-2 note simply re-derived the variance incorrectly off the path base.

---

## 1. Setup and the step (∗), six lines, no arboreal axioms

`𝒯` = finite rooted trees; morphisms = **rooted-subtree embeddings** `f:T→T'` (prefix-closed root-containing
image; node map `j=nodes(f):nodes(T)↪nodes(T')` injective). `𝒜` = the unary, propositionally-truncated
relational lift: objects `(T,R)` with `R⊆nodes(T)`; a morphism `(S,Q)→(T',R')` is a subtree embedding
`h:S→T'` with `h(Q)⊆R'` (colour-preserving), **at most one per base map** (so `𝒜→𝒯` is a poset fibration).
`ℙ:𝒜→𝒯` forgets the colour. Fibre over `T` is `(2^{nodes T},⊆)`.

> **(∗) The `ℙ`-cartesian lift of `f:T↪T'` at `(T',R')` is `(T, j⁻¹R')` — preimage — for every `T`,
> branching included; and cartesian ⟺ `R=j⁻¹R'` ⟺ pathwise embedding.**

*Proof (Rick's six lines, in 𝒜 directly).* Let `f:(T,R)→(T',R')` over `j`, `P:𝒜→𝒯` faithful.
- **`R=j⁻¹R' ⇒ cartesian.** Given `g:(S,Q)→(T',R')` over `k=j∘h`: then `j(h(Q))=k(Q)⊆R'`, so
  `h(Q)⊆j⁻¹R'=R`; hence `h` lifts to `(S,Q)→(T,R)`, uniquely since `P` is faithful.
- **cartesian ⇒ `R=j⁻¹R'`.** The map `(T,j⁻¹R')→(T',R')` over `j` is a morphism; cartesianness lifts
  `id_T`, giving `j⁻¹R'⊆R`. The reverse inclusion holds because `f` is a morphism (`j(R)⊆R'`).
- **pathwise embedding ⟺ `R=j⁻¹R'`.** "Strong on each root chain `c`" means `R∩c=j⁻¹R'∩c`; the chains
  cover `T`. ∎

The argument is uniform in `T` — there is no "non-path case", so no arboreal machinery is invoked.
Grade **proved**. (Exhaustive confirmation: Rick's enumeration of all coloured trees `≤4` nodes, 3147
morphisms, `cartesian ⇔ preimage ⇔ pathwise` in every case; our `crown_stage2_repair_verify.py` reproduces
the V-tree slice.)

Thus `ℙ ≅ nodes^*(Sub)` over `𝒯`: `Sub→Set` the predicate fibration (fibre `(2^X,⊆)`, reindexing =
preimage), pulled back along `nodes:𝒯→Set`, `T↦nodes(T)`, `f↦j`.

---

## 2. Clause 1, repaired: the contravariant one-shape functor (M1)

**Definition (corrected).** `Ψ' : 𝒯^op → Cont`, on objects `Ψ'(T)=(1,\{nodes(T)\})` (one shape, flat
position set), on a morphism `f:T↪T'` of `𝒯`
$$ \Psi'(f) \;=\; (\mathrm{id}_1,\ j)\ :\ \Psi'(T') \longrightarrow \Psi'(T), \qquad j:\ \mathrm{nodes}(T)\to\mathrm{nodes}(T'). $$
Here `j` is the **backward position map** of the container morphism: a `Cont`-morphism `(S,P)→(S',P')`
is `(φ:S→S', ρ_s:P'_{φ s}→P_s)`; with `S=S'=1`, the morphism `Ψ'(T')→Ψ'(T)` is a single backward map
`nodes(T)→nodes(T')`, and that map is `j`. (The old `ρ_f:nodes(T')↠nodes(T)` is gone.)
`Ψ'` is functorial: `j` composes functorially and `Ψ'(g∘f)` carries `j_g∘j_f` backward.

**Why `ρ_f` was wrong (M1), verified.** On the V-tree `T'={r,a,b}`, `T={r,a}`, with `ρ_f(b)=r`
(nearest ancestor): the two legs along `ρ_f` are direct image `Σ_{ρ_f}` and preimage `ρ_f⁻¹`, and **neither
equals `j⁻¹`**:
- `R'={b}`: `j⁻¹R'=∅` but `Σ_{ρ_f}R'={r}`;  `R'={a,b}`: `j⁻¹R'={a}` but `Σ_{ρ_f}R'={r,a}`.
- `ρ_f⁻¹` goes the wrong way (from `T` to `T'`): since `ρ_f∘j=id`, `j⁻¹` is a *retraction* of `ρ_f⁻¹`,
  not it.

(`crown_stage2_repair_verify.py`, block T1: disagreement on exactly the 2 colourings Rick names.)

**Why `j` backward is right.** The `Cont(cod)` legs along `Ψ'(f):Ψ'(T')→Ψ'(T)` with backward map `j`:
- **cartesian** (reindexing of the fibration part) `(Σ_j)^op` = direct image `Σ_j:(2^{nodes T},⊇)→(2^{nodes T'},⊇)`;
- **opcartesian** (reindexing of the opfibration part) `j^* = j⁻¹:(2^{nodes T'},⊇)→(2^{nodes T},⊇)` = preimage.

It is the **opcartesian** leg that equals relation reflection `j⁻¹`. This is Stage 1 §3–§4 verbatim: the
identification used only that `j` is a set-injection and that preimage is functorial — never that the
positions form a chain — so it transfers to branching bases unchanged.

> **Theorem (Clause 1, repaired — proved, unconditional).** As indexed posets over `𝒯^op`,
> $$ \mathbb P \;\cong\; \big(\Psi'^{*}\mathrm{Cont}(\mathrm{cod})\big)^{\mathrm{fib\text{-}op}}_{\text{opfib}}, $$
> i.e. `ℙ` is the functor `𝒯^op→\mathbf{Pos}`, `T↦(2^{nodes T},⊆)`, `f↦j⁻¹`, obtained from the
> **opfibration part** of the pullback `Ψ'^*Cont(cod)` over `𝒯^op` after the fibrewise opposite. Branching
> and all.

**Re-typing (M1, well-formedness).** The shipped phrase "`ℙ ≅ (Ψ'^*Cont(cod))_fib-op` *as fibrations over
`𝒯`*" is ill-typed: the variance is wrong. The correct object is an **isomorphism of indexed posets**
`𝒯^op→\mathbf{Pos}`, `T↦(2^{nodes T},⊆)`, `f↦j⁻¹`; in total-category terms `ℙ` is the opfibration part of
`Ψ'^*Cont(cod)` over `𝒯^op`, fibrewise-opposed. The word *conditional* now leaves the statement entirely:
Clause 1 is **proved** (§1's (∗) + this variance match).

**Cross-check demanded by Rick: Stage 1 is not infected.** On `𝒫` the analogue of `ρ_f` is the collapse
`[n]↠[m]`. In the Stage-1 note the collapse appears **only** in Lemma 2, as the *cartesian* leg that
*disagrees* with preimage; the positive match (Lemma 3, §4) carries the **inclusion** `j:[m]↪[n]` as the
backward map of a reversed `Cont`-arrow `(1,{[n]})→(1,{[m]})`, whose opcartesian leg is `j⁻¹`. That is
exactly the contravariant orientation above. So Stage 1's positive content is correct; only its *packaging*
("opcartesian leg of a covariant `Φ`" rather than "cartesian reindexing of a contravariant `Φ`") invited
the Stage-2 error. Recommended uniform convention for the write-up: present **both** stages with the
encoding functor contravariant, `Φ,Ψ':𝒯^op→Cont`, `f↦(id₁,j)`.

---

## 3. The branch functor `Ψ` has no functorial action (M3) — a no-go

`Ψ(T)=(branches(T),\{chain_b\})`: shapes = branches (root-to-leaf chains, indexed by leaves), positions
over branch `b` = the nodes of `b`. Def 10 gave `Ψ` on objects only. We show this is **forced**: no
functorial action on morphisms encodes the embeddings, in either variance. The obstruction is exactly that
**branches do not transform functorially** — the content behind "branching is not a coproduct of branches."

**What "encodes the embedding" means.** A container morphism between the `Ψ`-objects has an underlying
**shape map** (the covariant component `φ`). For `Ψ(f)` to *cover* `f:T↪T'` — the only reason to call it
"the action of `Ψ` on `f`" — its shape map must send each branch to a branch **compatible with `j`**:
the chain of the source branch, pushed along `j`, must sit inside the chain of the target branch. Formally,
writing `b` for a branch and `chain_b` for its node set, compatibility is `j(chain_b)\subseteq chain_{φ(b)}`
(covariant) resp. `j(chain_{φ(b')})\subseteq chain_{b'}` (contravariant). Dropping this makes `Ψ(f)` carry
no information about `f` at all, so it would not be an *action of `Ψ`*; we return to that remark at the end.

**(a) Contravariant `Ψ:𝒯^op→Cont` does not even exist.** The shape map of `Ψ(f):Ψ(T')→Ψ(T)` is
`φ:branches(T')→branches(T)` with `j(chain_{φ(b')})⊆chain_{b'}`. On the V-tree inclusion `{r,a}↪{r,a,b}`:
`branches(T')=\{ra,rb\}`, `branches(T)=\{ra\}`. For `b'=rb`, we need a branch `b` of `T` with
`j(chain_b)⊆chain_{rb}=\{r,b\}`; the only candidate `chain_{ra}=\{r,a\}` maps to `\{r,a\}\not\subseteq\{r,b\}`.
**No valid image.** A branch of `T'` restricts to the prefix `\{r\}`, which is *not* a branch of `T`. So
no container morphism `Ψ(T')→Ψ(T)` covers `f`: the contravariant functor fails on existence.
(Verified, block T2(a): valid T-branches for `rb` = `[]`.)

**(b) Covariant `Ψ:𝒯→Cont` exists per morphism but is not functorial.** Here `φ:branches(T)→branches(T')`
with `j(chain_b)⊆chain_{φ(b)}`. Per-morphism such `φ` exists (extend a branch to some leaf above). But
**functoriality fails**, by a sibling swap:

Let `T=\{r,a\}` (`a` a leaf) and `T'=\{r,a,c,d\}` with `c,d` both children of `a`. Let `f:T↪T'` be the
inclusion (`j:r↦r,a↦a`) and let `σ:T'→T'` be the tree automorphism swapping `c↔d` (fixing `r,a`).
`branches(T)=\{β_a\}` with `chain_{β_a}=\{r,a\}`; `branches(T')=\{β_c=rac,\ β_d=rad\}`.
- Compatibility for `f`: `φ_f(β_a)` must be a branch `⊇ j(\{r,a\})=\{r,a\}`, so `φ_f(β_a)∈\{β_c,β_d\}` —
  **two choices** (verified block T2(b): candidate leaves `[c,d]`).
- Compatibility for `σ`: `φ_σ(β)⊇σ(chain_β)`. Since `σ(chain_{β_c})=\{r,a,d\}=chain_{β_d}`, we get
  `φ_σ(β_c)=β_d` and `φ_σ(β_d)=β_c`: **`φ_σ` is forced to be the swap**, with no fixed point.
- But `σ∘f=f` as morphisms of `𝒯` (node maps agree: `σ∘j=j` because `σ` fixes `r,a`; and morphisms of
  `𝒯` are determined by their node maps). Functoriality of `Ψ` forces `φ_σ∘φ_f=φ_{σ∘f}=φ_f`, i.e.
  `φ_f(β_a)` is a fixed point of `φ_σ`. The swap has none. **Contradiction.**

(Verified block T2(b): `σ∘f` and `f` have equal node maps; `φ_σ=\{c↦d,d↦c\}` fixed-point-free.)

> **Theorem (Stage 2, M3 — no-go, proved).** The object assignment `T↦(branches(T),\{chain_b\})` extends to
> **no** functor `𝒯→Cont` nor `𝒯^op→Cont` whose action on morphisms covers the tree embeddings. The
> contravariant extension fails on existence (a branch of the larger tree restricts to a non-branch prefix);
> the covariant extension fails on functoriality (a sibling-swap automorphism forces an impossible
> fixed-point of the branch shape-map). Equivalently: **`branches:𝒯→\mathbf{Set}` is not a functor
> respecting the embedding** in either variance.

Consequently Thm 1(2) of the note is honestly a statement about the **object assignment** `Ψ` (Clause 2's
over-count `2^{Σ_v(λ(v)-1)}` compares fibres over *single objects* by cardinality and is untouched;
lean-verified separately). The genuine structure relating the branches of `T` and `T'` is a
**span / correspondence** `R_f⊆branches(T)×branches(T')`, `(b,b')∈R_f ⟺ j(chain_b)⊆chain_{b'}`, which is
left-total but neither left- nor right-functional — this is precisely why `Fam=Σ` (a functor) cannot
realize it, and why recovering `ℙ` from `Cont(cod)∘Ψ` needs a **descent** step rather than a functorial map
(§3 of the 10-09 note, the one correct half). The no-go is the container-side face of *composition is a
degree-2 datum*: sharing of branch-prefixes is a relation, not a map.

**Remark (why dropping compatibility does not rescue a functor).** If one allows the shape map to ignore
`f` entirely, the only escape in example (b) is to set `φ_σ=\mathrm{id}` — but then `Ψ(σ)` does not cover
the nontrivial automorphism `σ`, so `Ψ` is not an encoding of `𝒯` at all (it would, e.g., identify the two
distinct subtrees `r→a→c` and `r→a→d`). Any functor that *does* distinguish `σ` from `id` on branches runs
into the same contradiction. So the no-go is not an artifact of the compatibility convention.

---

## 4. The `k≥2` "ceiling" is false (M4)

The 10-09 note claimed the k-ary relational power "lies genuinely beyond `Cont(cod)`" (l. 87, 121–123,
368–369; Prop 17; the count `2^{n^k}`). This is **false**. The claim only shows that the *unary* `Ψ'`
(positions `=nodes(T)`) cannot see k-ary relations — true but trivial (a functor into unary predicates has
no k-ary values). `Cont(cod)` itself is a large bifibration; choose a bigger position set:

> **Fact (M4).** `Ψ'_k:𝒯^op→Cont`, `Ψ'_k(T)=(1,\{nodes(T)^k\})`, `Ψ'_k(f)=(id_1, j^k)` with
> `j^k=j×\dots×j:nodes(T)^k→nodes(T')^k` the coordinatewise backward map, **reproduces the arboreal k-ary
> fibre exactly**. Its fibre over `T` is `Sub(nodes(T)^k)^op=(2^{nodes(T)^k},⊇)`, and the opcartesian leg
> along `Ψ'_k(f)` is `(j^k)⁻¹` = **k-ary relation reflection** `\{(v_1,…,v_k):(jv_1,…,jv_k)\in R'\}`.

This is the §1/§2 argument verbatim with `nodes(T)` replaced by `nodes(T)^k`. (Verified, block T3:
`(j^2)⁻¹` equals relation reflection on all 200 sampled binary relations on the V-tree; the Cont fibre
`2^{n^2}=16` *is* the arboreal 2-ary fibre, not a smaller thing it fails to reach.)

For a signature `σ`, use one shape per relation symbol `r` with positions `nodes(T)^{ar(r)}` (a coproduct
over **symbols** is correct here — distinct symbols are independent). If the intended k-ary fibre is the
**EF-style** one (related tuples must be pairwise comparable, i.e. lie on a common root chain), take the
positions to be the **comparable** k-tuples; then the note's count `2^{n^k}` (l. 356) is *also* wrong — it
should be `2^{\#\{\text{comparable }k\text{-tuples}\}}`.

> **Corrected statement.** Grade the ceiling claim **false**. Keep only: *the unary one-shape `Ψ'`
> (positions `=nodes(T)`) is blind to k-ary relations* — **proved, and trivial**. There is no obstruction
> "beyond `Cont(cod)`"; k-ary structure sits inside `Cont(cod)` at the container with positions `nodes^k`.

---

## 5. Write-up hygiene (carry into the corrected Strathclyde note)

- **Drop Jakl–Reggio.** (∗) has the direct six-line proof of §1 in our own `𝒜`, with no arboreal axioms.
  Delete Rem. 9 / Open Problem 1 and the Thm-23 dependence. If the paper is mentioned at all, cite it
  correctly: **T. Jakl, L. Reggio, *On the Axioms of Arboreal Categories*, arXiv:2603.21841, CMCS 2026**
  (the shipped ref [3] wrongly listed "Abramsky, Reggio" with no arXiv id) — and state that it is not used.
- **Name the topology.** Prop 15 descent: root chains are **down-sets**, hence open in the **Alexandrov
  topology of down-sets**. (The opposite convention breaks the cover claim.)
- **`Fam=Σ`: pick one variance.** The branch coproduct is a coproduct of positions; the descent object is
  the **equalizer** of that coproduct. Say *equalizer* (not "coequalizer/descent equalizer").
- **Lemma 12** (`|⊔_b chain_b|=Σ_v λ(v)`) is a one-line count: present it as an observation; the content is
  the descent reading (Prop 15).
- **Open Problem 3** (descent completion as a fibration) is blocked on a morphism action for `Ψ`, which §3
  shows does not exist functorially — so restate it as descent along the **span** `R_f`, not a functor.

---

## 6. Status and registry

**Proved after repair.**
- **(∗)** cartesian lift = preimage at subtree embeddings (§1, six lines, no Jakl–Reggio).
- **Clause 1** (positive): `ℙ ≅ (Ψ'^*Cont(cod))^{fib-op}_{opfib}` over `𝒯^op`, `Ψ'` contravariant with `j`
  backward — **proved, unconditional** (§2). Clean form `ℙ ≅ nodes^*(Sub)`.
- **Clause 2** (over-count `2^{Σ(λ-1)}`, objectwise) — **proved** (unchanged; lean-verified child).
- **M3 no-go**: `Ψ` has no functorial morphism action in either variance — **proved** (§3).
- **M4**: ceiling **false**; k-ary fibre reproduced by `Ψ'_k` with `j^k`; only "unary `Ψ'` blind to k-ary"
  survives (trivial) (§4).

**Stage-1 container dictionary** (`preimage = Cont's ρ* leg under the fibrewise op`) stays **computed**; it
is order-blind, so it was never at risk off the path base. Not a gap in the branch extension.

**Registry node** `crown-stage2-multishape-branch-extension` (game-comonad-poly.json): re-promote the
positive half (Clause 1) to **proved** with the j-repair; add a **proved** no-go child
`crown-stage2-psi-no-functorial-action` (§3); correct the ceiling node to the narrow trivial statement
(§4). `lean-crown-stage2-overcount-identity` stays **lean-verified**. Do not self-grant above proved.

**Deferred (not this cycle):** the T² coupled-strata nonabelian-gerbe lane.
