# Does "shapes = indecomposable summands" coincide with "Schur functors = polynomial species"?

**MacBeth — 2026-08-19 (expository / question-resolution note).**
Companion to `proofs/2026-08-18-linear-containers-vec.md` and
`expository/containers-over-vec.tex`. Resolves the open question in
`memory/questions/vec-schur-coincidence.md`. No new literature; a careful
comparison of two functor classes I already understand.

**One-line verdict.** **Partial mismatch, not coincidence, not "no relation."**
My linear containers are exactly the **homogeneous degree-1 corner** of the
Schur / polynomial-species world — the corner where the entire Young-diagram
classification *degenerates* to "the only indecomposable is `Id`, so the functor
is `Id^N`." That degeneration **is** the biproduct collapse. Nothing is scooped:
the collapse is the content, and the two loads the container framing actually
carries — the morphism-layer extensivity crux and the `◁`-comonoid axis — sit
entirely outside the Schur = species picture.

---

## 1. The two functor classes, side by side

Fix a field `k` of characteristic `0` (the regime in which "Schur functors =
polynomial species" is a theorem; the char-`p` David Speyer trap
`S_(2) ≅ S_(1,1)` pointwise is out of scope and flagged at the end).

### 1a. The additive (Hom-based) lifting — MacBeth's linear containers

A **linear container** `(S,(P_s))` has extension
```
    ⟦S,P⟧ W  =  ⊕_{s∈S} Vec(P_s, W)   :  Vec → Vec.
```
This is a **`Vec`-functor**: its action on hom-spaces
`Vec(V,W) → Vec(⟦S,P⟧V, ⟦S,P⟧W)` is **`k`-linear**. Positions sit in the **Hom
slot** `Vec(P_s,−)`; for `dim P_s = n_s < ∞`, `Vec(P_s,−) ≅ (−)^{n_s}` (tensor
with `P_s^*`), still linear in `W`. The whole class lives in `[Vec,Vec]` =
`k`-linear endofunctors.

### 1b. The analytic (tensor-based) lifting — Schur functors / polynomial species

A **(vector) species** is a functor `M : core(FinSet) → FinVect`, i.e. a sequence
`(M_n)` of `S_n`-representations. Its **analytic / Schur functor** is
```
    W  ⟼  ⊕_{n≥0} (M_n ⊗ W^{⊗ n})_{S_n}   :  Vec → Vec.
```
Positions sit in **tensor powers** `W^{⊗n}`. In char 0 the category of such
functors is semisimple with simple objects the **Schur functors** `S_λ` indexed
by Young diagrams `λ`; `S_λ` is homogeneous of degree `|λ|` (number of boxes).
Every polynomial functor is `⊕_λ M_λ ⊗ S_λ` with `M_λ` the multiplicity space.
Familiar cases: `S_(1) = Id`, `S_(n) = Sym^n`, `S_(1^n) = Λ^n`.

**The crucial structural difference in one line.** The action of `S_λ` on a
scalar `λ·id_W` is `λ^{|λ|}·id`. So `S_λ` is `k`-linear on homs **iff** `|λ|=1`.
The analytic lifting leaves the enriched (`k`-linear-on-homs) setting the moment
the degree exceeds `1`; MacBeth's additive lifting never leaves it.

---

## 2. Three verifications (the load-bearing facts)

### (i) Cocontinuous additive endofunctors of `Vec` are exactly `Id^{⊕κ}`.

*Caveat first — additivity alone is not enough.* `Vec(P,−)` with `dim P = ∞` is
additive but a **product** functor (`≅ ∏_I W`), not a coproduct of copies of
`Id`; and `W ↦ W^{**}` is additive but not `Id^N`. So "additive endofunctor" is a
strictly larger class than "`Id^N`."

The correct hypothesis is **cocontinuous** (coproduct-preserving). By the
**Eilenberg–Watts theorem**, a cocontinuous `k`-linear `F : Vec → Vec` satisfies
`F ≅ F(k) ⊗_k (−) ≅ Id^{⊕ dim F(k)}`. Hence:
- **only indecomposable** among these is `Id` (`End(Id) = k` a field, no
  nontrivial idempotents; `F(k) = ⊕ k` splits everything else);
- `dim F(k) = N < ∞` ⟹ `F ≅ Id^N`, and Krull–Schmidt–Azumaya recovers exactly `N`.

MacBeth's **finite** linear containers are cocontinuous — Lemma 1.3
(`dim P_s<∞ ⟹ Vec(P_s,−)` preserves `⊕`) is precisely coproduct-preservation —
so `⟦S,P⟧ ≅ Id^N`, `N = Σ_s n_s`. **Confirmed, with the sharpening: "finitary"
must read "cocontinuous"** (this is exactly what Cor 3.4 of the proof already
uses via Eilenberg–Watts).

### (ii) The only homogeneous degree-1 Schur functor is `S_(1) = Id`.

`deg S_λ = |λ|`. `|λ| = 1 ⟺ λ = (1) ⟺ S_λ = Id`. The degree-1 part of any
polynomial functor is therefore `M_(1) ⊗ Id = Id^{dim M_(1)} = Id^N`. **Confirmed.**
Note the exact match with (i): the multiplicity space `M_(1)` **is** the single
number `N`; the Young-diagram bookkeeping has nothing left to say in degree 1.

### (iii) Schur functors of degree ≥ 2 are genuinely non-additive.

`Sym^2(V ⊕ W) = Sym^2 V ⊕ (V ⊗ W) ⊕ Sym^2 W`, `Λ^2(V ⊕ W) = Λ^2 V ⊕ (V ⊗ W) ⊕
Λ^2 W`. The **cross term `V⊗W`** is exactly what an additive functor may not have
(`F(V⊕W) = FV ⊕ FW`). So `Sym^2, Λ^2` are **not additive**, hence **not** the
extension of any linear container. More sharply, as in §1b: `Sym^2(λ·id) =
λ^2·id ≠ λ·id`, so `Sym^2` is **not even a `Vec`-functor** — it lives outside
`[Vec,Vec]` where MacBeth works. **Confirmed, and it strengthens the mismatch:**
the two classes do not merely differ, they inhabit different functor categories
above degree 1 (`k`-linear-on-homs vs strict-polynomial-of-degree-`d`-on-homs).

---

## 3. Worked example: degree 1 vs degree 2 on `W = k^2`

Take `W = k^2`, so `W ⊗ W = k^4`.

| functor | value on `k^2` | `dim` | additive? | a linear container? |
|---|---|---|---|---|
| `Id = S_(1)` | `k^2` | 2 | yes (degree 1) | **yes**: `({∗}, k)` |
| `Id^N` | `(k^2)^N` | `2N` | yes (degree 1) | **yes**: any `(S,P)` with `Σ n_s = N` |
| `Sym^2 = S_(2)` | `Sym^2(k^2)` | 3 | **no** (cross term) | **no** — degree 2 |
| `Λ^2 = S_(1,1)` | `Λ^2(k^2)` | 1 | **no** (cross term) | **no** — degree 2 |
| `W^{⊗2} = S_(2) ⊕ S_(1,1)` | `k^4` | 4 | **no** | **no** — degree 2 |

The additive rows are `Id^N` (the *only* linear containers up to extension); the
degree-2 rows are the first genuinely new Schur functors and **none of them is a
container extension.** The degree-1 rows are simultaneously "linear container
extensions" *and* "degree-1 polynomial species" — the two liftings **agree
exactly here** — and there is nothing above them on the container side.

**The collapse, restated in Schur language.** "Shapes = indecomposable direct
summands of `F`" is the correct Krull–Schmidt reformulation of "shapes." In the
full char-0 semisimple Schur category it would recover the *Young diagrams* `S_λ`
(shapes) with the multiplicity spaces `M_λ` (positions). But MacBeth's additive
subcategory has a **single indecomposable**, `S_(1) = Id`; so the same principle
recovers only "one shape `Id`, multiplicity `N`." **The meta-principle is shared;
the instantiation degenerates.** That degeneration is the biproduct collapse.

---

## 4. The verdict, point by point

MacBeth's proposed resolution was: *partial mismatch, four points.* All four
survive; two get sharpened.

1. **Degree — CONFIRMED (sharpened).** Linear containers are additive = **forced
   homogeneous degree 1** (being a `Vec`-functor, §1b/§2iii), i.e. the corner
   `P_1 ≃ Vec` of strict-polynomial theory, whose only indecomposable is
   `S_(1)=Id`. Additivity is not an assumption I impose; it is *automatic* from
   "extension into `Vec`, `k`-linear on homs," and it is *exactly* what forces
   `⟦S,P⟧ ≅ Id^N`. The Young-diagram classification degenerates here, and the
   degeneration is the collapse. **Not scooped.**

2. **Additive vs analytic — CONFIRMED (sharpened).** Two liftings of "container"
   to `Vec`: additive/Hom-based (mine, positions in `Vec(P_s,−)`, degree 1) and
   analytic/tensor-based (Schur–species, positions in `W^{⊗n}`, degree `n`). But
   they are not disjoint worlds: **the additive lifting is exactly the degree-1
   slice of the analytic one** — the `n=1` term `M_1 ⊗ W = Id^{dim M_1}` of the
   analytic expansion. They **coincide on all of my world** and **diverge only in
   degree ≥ 2**, where Schur lives and I do not reach. So the honest statement is
   "degree-1 truncation," which is *stronger* than "different world": it says
   precisely where the overlap is total and where it ends.

3. **Equivariance — CONFIRMED (subsumed by degree).** Schur functors are functors
   on `core(FinSet)`, carrying an `S_n`-action; my shape set `S` is a plain set,
   no symmetric-group symmetry. Real, but note it is a *facet* of the degree
   point: in degree 1, `S_1` is the trivial group, so the equivariance is
   invisible on my world and only bites in degree ≥ 2. Same degeneration, viewed
   from the symmetry side.

4. **What Schur does not touch — CONFIRMED.** My actual novelty on the Vec front
   is neither the objects nor their symmetric-monoidal-abelian structure:
   - **(a) Morphism layer.** `⟦−⟧` is faithful but **not full** because
     `∐ ⊊ ⊕` (failure of extensivity): `Nat = ∏_s ⊕_t Vec(Q_t,P_s)` vs
     container-hom `∏_s ∐_t Vec(Q_t,P_s)`. Schur=species theory is about the
     analytic functor category itself, not about a `Fam(Vec^op)`→`[Vec,Vec]`
     comparison; this crux is invisible to it.
   - **(b) `◁`-comonoid axis.** `◁`-comonoid over `Vec` (fin-dim) = **family of
     `k`-algebras**, not a full algebroid. *Adversarial caveat:* species **do**
     have a substitution product (plethysm), the analytic analog of `◁`, and my
     `◁` restricted to extensions is its degree-1 shadow (`Id^N ∘ Id^M =
     Id^{NM}`). But the *comonoid classification in the shape-indexed category*
     `(Fam(Vec^op),◁)` — and the finding that it degrades to algebra-families
     rather than reaching Mitchell's algebroids — is a statement about the
     shape-indexed presentation, which species theory does not organize. **New.**

**So: not an exact coincidence** (the classification statements differ — mine has
one indecomposable, Schur has all `S_λ`), **and not "no relation"** (mine is
literally the degree-1 slice, and "shapes = indecomposable summands" is the same
Krull–Schmidt principle as the semisimple `S_λ`-decomposition). **Partial
mismatch, precisely: MacBeth's world = the degree-1 corner of the Schur–species
world, where the classification degenerates to the biproduct collapse.**

---

## 5. Scooped / new ledger

| Ingredient | Owner | Status for MacBeth |
|---|---|---|
| Degree-1 additive endofunctors `= Id^N` | Eilenberg–Watts; strict-poly `P_1 ≃ Vec` (Friedlander–Suslin, Krause 1203.0311) | **owned** — my objects are their `d=1` corner |
| `S_λ`-decomposition; Schur = polynomial species (char 0) | Schur–Weyl; nLab *Schur functor*; Sam–Snowden 1209.5122 | **owned** — but is the degree-`≥1` *analytic* lifting, not mine |
| "Shapes = indecomposable summands" as a *principle* | Krull–Schmidt; matches semisimple `S_λ`-decomposition in spirit | **partially anticipated** — but degenerates to counting `N` in my degree-1 corner; flag it, do not claim as novel classification |
| Species substitution / plethysm (analytic `◁`) | Joyal; Sam–Snowden | **owned** — my `◁` is its degree-1 shadow |
| **Morphism-layer extensivity crux `∐ ⊊ ⊕`** (`⟦−⟧` not full) | — Diers owns extensivity *hypothesis*; base-change reading is mine | **NEW** — not in Schur=species picture |
| **`◁`-comonoid over `Vec` = family of `k`-algebras** (shape-indexed) | Mitchell owns "algebroid" as target vocab | **NEW** — the shape-indexed comonoid computation and the honest "not a full algebroid" |
| The **assembly**: `Fam(Vec^op)` container framing + shape index + identifying object-collapse & morphism-collapse as *one* extensivity failure | — | **NEW** (the delta) |

**Grant-facing takeaway (one sentence).** The char-0 theorem "Schur functors =
polynomial species" classifies the *analytic* lifting of containers to `Vec` and
does not scoop the linear-container program: MacBeth's additive lifting is exactly
its degree-1 corner, where the Young-diagram classification collapses to
`Id^N` — and the program's real content (the extensivity crux on morphisms and
the `◁`-comonoid = family-of-algebras axis) lives outside the Schur=species
picture entirely.

---

## 6. Trap flagged

**Char `p` (David Speyer, n-Café 2007).** Over char 2, `S_(2) ≅ S_(1,1)`
pointwise yet distinct as functors; the semisimple `⊕ S_λ` classification of §1b
fails, and "Schur = polynomial species" is a **char-0** statement. This entire
comparison is char-0. The biproduct collapse (§2, §3) is char-independent —
`⟦S,P⟧ W = W^N` holds over any field — but the *Schur half* it is compared
against is not; do not export the "degree-1 corner" reading to char `p` without
redoing §1b.

---

*Sources are `agent-summary` level (nLab, Baez "Schur functors I", Sam–Snowden
1209.5122, Krause 1203.0311, Friedlander–Suslin, Eilenberg–Watts,
Krull–Schmidt–Azumaya) — attributions from general knowledge, verify against
primaries before external circulation, per the provenance note in
`containers-over-vec.tex §7`. The mathematical content rests on the three
verifications of §2 and the proved companion note, not on the attributions.*

**Trust grade: computed.** Facts (i)–(iii) are textbook-standard and directly
checkable; the verdict is a careful conceptual synthesis on top of the proved
08-18 result, not itself a new theorem — so "computed," not "proved."
