# Stress-test: is full `Vec_k` `◁`-inadmissible? (the `F = ∏_ℕ(⊕_ℕ −)` obstruction)

**2026-09-03. Pressure-test of the "Vec inadmissibility" sketch.** Verdict up front:
**(B) THERE IS A HOLE.** The sketch's proposed separators are *all non-obstructions* — each
one I can concretely check *fails to distinguish* `F` from a coproduct of representables. The
claim is **not refuted either**: `F` may genuinely fail to be an extension, but establishing
that needs functor-category homological algebra (projectivity in `Add(Vec,Vec)`), which is
**MacBeth's own open problem** (`memory/vec-admissibility-yoneda-rigidity.md`, question (Q);
`proofs/2026-09-02-vec-admissibility-rigidity.md`). Grade: **computed** for every
*non*-obstruction below; **the positive obstruction the sketch asserts does not exist among the
tests proposed**, and no rigorous replacement is offered by the sketch.

---

## 0. Setup, confirmed (Task 1)

`E = k^{(ℕ)} = ⊕_ℕ k`. `q = (ℕ, (k)_{t∈ℕ})`, so `⟦q⟧X = ⊕_ℕ X`. `P = E`.
```
F(X) = [E, ⟦q⟧X] = Hom(k^{(ℕ)}, ⊕_ℕ X).
```
Map out of a coproduct = tuple of maps: `Hom(⊕_ℕ k, Y) = ∏_ℕ Hom(k,Y) = ∏_ℕ Y`. Hence
```
F(X) = ∏_ℕ (⊕_ℕ X)   = (∏_ℕ) ∘ (⊕_ℕ)   [Task 1 CONFIRMED].
```
`F` is an *additive* endofunctor of `Vec` (preserves finite biproducts — verified numerically,
`scratch/vec_stress_check.py`). So we live in `Add(Vec,Vec)`, and the target objects are
`G(X) = ∐_j Hom(N_j, X) = ⊕_j Hom(N_j, X)` for a family `(N_j)`.

**Key given fact.** `Hom(N,−)` preserves coproducts `⟺ N` finite-dimensional. Coproducts commute
with coproducts, so `G = ⊕_j Hom(N_j,−)` preserves coproducts `⟺ every N_j` is finite-dim. Call
this **Case A** (all `N_j` fd) vs **Case B** (some `N_j` infinite-dim).

---

## 1. fd `P` sanity — the framework comes out RIGHT (Task 4)

If `P` is finite-dimensional then `Hom(P,−)` preserves `⊕_ℕ`, so
```
F(X) = Hom(P, ⊕_ℕ X) = ⊕_ℕ Hom(P,X) = ⊕_ℕ (P^* ⊗ X),
```
a **coproduct of copies of the single representable `Hom(P,−)`**. So every fd `P` is absorptive.
This is the load-bearing consistency check and it passes. The *entire* difficulty is that for
infinite-dim `P`, `Hom(P,−)` does **not** commute with `⊕_ℕ`; the product `∏_ℕ` survives and we get
the shape `∏_ℕ(⊕_ℕ −)` whose extensionality is unresolved. This localises the phenomenon precisely:
**fd ⟹ collapse ⟹ obviously an extension; infinite-dim ⟹ product-of-coproduct ⟹ open.**

---

## 2. Every separator the sketch proposes is a NON-obstruction

### 2(a) Preservation of infinite coproducts — FAILS to separate
- `F` does **not** preserve infinite coproducts. **Witness (support argument, exact):** an element
  of `F(⊕_{i∈I} X_i) = ∏_ℕ(⊕_ℕ ⊕_i X_i)` is a sequence `(w_n)_n`, each `w_n` finitely supported.
  Take `I = ℕ`, `X_i = k`, and `w_n =` the basis vector at `(row 0, i=n)`. Each `w_n` is finitely
  supported (valid), but the **total** `i`-support `⋃_n supp_i(w_n) = ℕ` is infinite. The image of
  the canonical map `⊕_i F(X_i) → F(⊕_i X_i)` consists exactly of elements with **finite** total
  `i`-support. So `w ∉ image`; the map is not surjective. (Simulated for `K=3,5,10` slots in
  `vec_stress_check.py`: total support grows without bound.)
- **But** a Case-B `G` *also* fails to preserve infinite coproducts. So "F doesn't preserve
  coproducts" only rules out **Case A**. It does **nothing** against Case B. NOT an obstruction.

### 2(b) Dimension counting at `k`, `k^{(I)}` — FAILS to separate
`dim F(k) = dim ∏_ℕ(⊕_ℕ k) = dim ∏_ℕ k^{(ℕ)} = 2^{ℵ_0}` (continuum, `k` countable). A coproduct of
representables `⊕_j Hom(N_j,k) = ⊕_j N_j^*` can be made continuum-dimensional (e.g. continuum-many
`N_j = k`). Matched. At `k^{(I)}` the same freedom persists. Dimension/cardinality **cannot**
separate. (This is why the naive "count" attempts die — noted, consistent with predecessor memory.)

### 2(c) Preservation of products — FAILS to separate
Representables `Hom(N,−)` preserve *all* limits, but an **infinite coproduct** of them need not
preserve infinite products (⊕ commutes with ∏ only finitely). And `F = ∏_ℕ ∘ ⊕_ℕ` does not preserve
infinite products either (the `⊕_ℕ` inside kills it). Both sides fail product-preservation, so the
sketch's hoped-for "F fails to preserve products but coproducts-of-representables do" is **false on
both clauses**: coproducts of representables do *not* preserve infinite products, so there is no
clean product-preservation property that all `G` share and `F` lacks. NOT an obstruction.

### Summary of §2
| proposed separator | does `F` have it? | do ALL `G=⊕_j h_{N_j}` have it? | separates? |
|---|---|---|---|
| preserves ∞-coproducts | no | no (Case B) | **no** |
| dimension at `k` = specific value | continuum | can match | **no** |
| preserves ∞-products | no | no | **no** |
| preserves finite biproducts (additive) | yes | yes | **no** |
| left-exact / exact | yes (∏,⊕ exact in Vec) | yes | **no** |

Every "local" (preservation/dimension) invariant is blind. This is the precise content of the
sketch's hole: **it asserts a separating property that does not exist among the properties it tests.**

---

## 3. The one solid rigidity result is insufficient (Task 3, adversarial)

- `F` is **not representable**: a single `Hom(N,−)` preserves all products, `F` does not. So `F` is
  not `Hom(N,−)` for any `N`. ✓ (rules out the trivial guess).
- **Lemma R (Yoneda finite-row-support rigidity, PROVED in the predecessor):** using
  `∏_ℕ = Hom(E,−) = h_E` and Yoneda `Nat(h_E, id) = E = k^{(ℕ)}` (finite support), every
  `α ∈ Nat(F, id)` kills the row-inclusions `in_n` for almost all `n`. Slenderness is *false* for
  the base `Vec` (every space is free) but *true in the functor category via Yoneda*. This is real
  and iso-invariant.
- **Why R does not close it (honest):** R (and its companion R′: `⊕_n A` is not a natural retract of
  `F`) only kills the **specific** summand `⊕_n(⊕_ℕ id)`. A general extension
  `G(X)=⊕_j Hom(N_j,X)` has `G(N_j)`-elements of **infinite row-support**, so its summands can spread
  across infinitely many rows and **evade** the finite-support forcing. Refuting *all* `G` is a
  **global** statement = "F is not projective in `Add(Vec,Vec)`", not reachable from R alone.

**Trying to build the `N_j` (adversarial, positive direction).** Nothing I compute forbids it. The
`ℤ`-analogue in `Add(Ab,Ab)` (Baer–Specker + slenderness of `ℤ`) gives inadmissibility cleanly — but
that argument **uses slender objects, which do not exist in Vec** (every vector space is free/`k^{(κ)}`;
even `k^ℕ ≅ k^{(𝔠)}` is free). So the Ab proof does **not** transport. The question genuinely sits at
the point where `Vec` differs from `Ab`.

---

## 4. `k^{(ℕ)}` vs `k^ℕ` (Task 4, second half)

Because every vector space is free, `k^ℕ ≅ k^{(𝔠)}` as an object, so
`Hom(k^ℕ, ⊕_ℕ X) = ∏_𝔠(⊕_ℕ X)` — the *same* shape `∏_κ ∘ ⊕_ℕ` with a bigger index `κ=𝔠`. The
countable choice `P = k^{(ℕ)}` (index `κ=ℵ_0`) is the **cleanest** witness; enlarging `κ` changes
nothing essential. Crucially, there is **no genuine "product object" in Vec that is not also a
coproduct** — this is the structural reason the slenderness route (which distinguishes `∏` from `⊕`
in `Ab`) is unavailable, and hence why the problem is hard rather than a one-line refutation.

---

## 5. Verdict

**(B) HOLE — the sketch is NOT rigorous.** Specifically:

1. The sketch's Step-2 tests (coproduct-preservation, product-preservation, dimension) are each,
   on concrete inspection, **unable to separate** `F` from a coproduct of representables. In
   particular the pivotal 2(c) hope is wrong: infinite coproducts of representables do **not**
   preserve products, so failure of product-preservation is not a distinguishing property.
2. The only surviving rigidity (Lemma R) is iso-invariant but kills merely one summand type;
   extensions with infinite-row-support summands are not excluded.
3. Consequently the assertion "`F` is not naturally isomorphic to any `∐_j Hom(N_j,−)`" is
   **unproven**. The true status is the crux (Q): *is `F` projective (a coproduct of representables)
   in `Add(Vec,Vec)`?* — **OPEN**.

**Consequences.**
- The sketch does **not** establish `Vec` inadmissible; Conj 6.2 does **not** follow from it.
- It also does **not** refute inadmissibility — this is *not* a proof that `Vec` is admissible.
  (If someone *did* exhibit the `N_j`, that would be the bigger result: `Vec` = irreducible Gap-1
  inhabitant.)
- The honest bet remains **direction A (inadmissible)** by analogy with `Add(Ab,Ab)`, but the
  slenderness engine does not transport to a field, so the analogy is **heuristic, not a proof**.

**What a rigorous proof of inadmissibility would need** (open sub-problem): show
`F = ∏_ℕ(⊕_ℕ −)` is not projective in the functor category `Add(Vec,Vec)`, e.g. via
`Ext^1(F, −) ≠ 0` on a suitable short exact sequence, or a functor-category cotorsion/slenderness
statement adapted to Vec. Suggested literature: Auslander functor categories, Eklof–Mekler
(almost-free/cotorsion) reworked over a field. This is exactly the "ask for collaborator" in the
predecessor memory.

**Grade.** Every *non*-obstruction claim in §§1–2 is **computed / concretely checked**
(`vec_stress_check.py`: finite biproduct collapse, the unbounded-support witness, the fd-P
coproduct-of-representables identity). The overall dichotomy verdict ("open, not closed by the
sketch") is **proved at the meta-level** (the sketch's tests demonstrably don't separate) and
**speculative** only as to which way (Q) resolves.
