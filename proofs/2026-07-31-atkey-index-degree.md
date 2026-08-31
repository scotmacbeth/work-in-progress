# The branching dichotomy is Boolean, not graded: `Arr_M` admits no Atkey-index degree

**MacBeth — PROVE session, 2026-07-31.** Target: PROVE.md's conjecture that the non-branching
dichotomy for effect–coeffect arrows is secretly a **graded** Freyd statement — that "arity ≤ 1"
is the bottom of a tower "arity ≤ n" measured by Atkey's index of `Arr_M`. Sequel to
`2026-07-29-effect-coeffect-arrows.md` (Thm A: `Arr_M` is a category ⟺ M non-branching),
`...-arrows-first.md` (Thm B: Hughes arrow / Freyd category ⟺ M non-branching), and
`2026-07-30-affine-classification.md` (the non-branching class = `E + A×X`).

---

## Answer in one line

> **The branching dichotomy does NOT refine to a graded Freyd tower.** The conjecture conflates
> two *distinct, nested* boundaries: the collapse of Atkey's index to a **plain** (non-indexed)
> Freyd category happens at **`M = Id`** (the coeffect comonad `W = G_M` becomes trivial), which
> is *strictly stronger* than non-branching (`M = E + A×X`, which contains `Maybe`, `Writer`).
> Along the arity axis there are **no intermediate rungs** (a cartesian monad has max arity ∈
> {≤1, ∞}), and the associativity obstruction `E2′` is **Boolean, not a matter of degree** (the
> merging `μ^T` that branching forces destroys any leaf-count grade). Atkey's index measures the
> **coeffect** `W = G_M` (nontrivial for every `M ≠ Id`), an axis *orthogonal to and coarser
> than* branching. The Boolean dichotomy is Boolean because its underlying invariant is
> two-valued on the monads where the arrow story is even defined.

This is a **negative** resolution of the conjecture, with three precise obstructions (§2–§4) and
one corrected identification (§2). Per Neil's close-out posture it is forward research, not a
ship-blocker; the sharpened Atkey framing (§2) is a citable contribution for the paper's Atkey
remark regardless.

---

## 0. Setup (recap)

Containers `p = (S,P)`; the two `Cont`-liftings of a ∏-cointerpretation Set-monad `M`
(Ahman–Bauer, arXiv:2409.17664 §6):

* **coeffect comonad** `G_M(S,P) = (S, M∘P)`, counit `ε` (backward `η^M`), comult `δ` (backward `μ^M`);
* **effect monad** `T_M(S,P) = (M S, P^⋆)`, `P^⋆(m) = ∏_{b∈lv(m)} P(x_b)`.

An **effect–coeffect arrow** `p ⇝ q` is `f : G_M p → T_M q`; the biKleisli composite has compositor
`κ : G_M T_M ⇒ T_M G_M` (the lax product-comparison on positions). This is **verbatim** Atkey's
BiKleisli Arrow `Ar(x,y) = [W x → T y]` (Atkey, *What is a Categorical Model of Arrows?*, ENTCS 229
(2011), §2; Uustalu–Vene, ENTCS 203 (2008)) with `W = G_M`, `T = T_M`, `λ = κ`. Atkey's thesis:
"Arrows = Freyd categories" is imprecise — a Hughes arrow with a nontrivial comonadic input `W` is
strictly more than a plain Freyd category; the correct object is a **closed *indexed* Freyd
category**, the extra generality controlled by an **index** capturing `W`.

The conjecture reads that index as *graded by M's branching profile*, so non-branching = index
collapse. §2 shows this reading is wrong; §3–§4 show the arity axis carries no grade anyway.

---

## 1. The conjecture, precisely, and what would confirm/refute it

**Conjecture (PROVE.md).** For branching `M` with maximal position-arity `n`, the Atkey index
`J_M` of `Arr_M` is graded by (a function of) `M`'s arities, so that "arity ≤ 1" (trivial index /
plain Freyd) is the bottom of a genuine tower "arity ≤ n" of *indexed* Freyd categories.

**A confirmation** would exhibit, for each `n`, a distinct nontrivial "index level" of `Arr_M`
tied to arity `n`, with the levels assembling into a monoid/PCM grade and composition respecting
it (à la Earnshaw–Nester–Román, cartesian PCM-graded ≅ Freyd, arXiv:2603.16375 Thm 4.23).

**A refutation** (what we find) is any of: (a) the "index collapse" boundary is not the
non-branching boundary; (b) the arity levels `n` do not exist as monads (no rungs); (c) the
composition cannot be made associative by tracking a leaf grade (the obstruction is ON/OFF).

We establish all three.

---

## 2. The two boundaries are distinct and nested (the corrected identification)

**Proposition 2.1.** As a comonad on `Cont`, `G_M = Id` **iff** `M = Id`.

*Proof.* `G_M(S,P) = (S, M∘P)`. If `G_M ≅ Id` then `M∘P ≅ P` naturally in the position set `P`.
Evaluating the natural iso `M(P) ≅ P` at each set `P` (e.g. `P = 0,1,2,…`) and using naturality
gives `M ≅ Id` as an endofunctor of `Set`, and the counit `ε` (backward `η^M`) being iso forces
the monad unit to be that iso. Conversely `M = Id` gives `G_M(S,P) = (S,P) = Id`. ∎

**Proposition 2.2 (nested boundaries).** Write the conditions on a ∏-cointerpretation `M`:

| condition | on `M` | what `Arr_M` is |
|---|---|---|
| index collapse (`W = G_M = Id`) | `M = Id` | a **plain** Freyd category `Kl(T_M) = Cont` |
| non-branching (arity ≤ 1) | `M = E + A×(−)` | a **Hughes arrow = indexed Freyd category** (Thm B), `W = G_M ≠ Id` unless `M=Id` |
| branching | some shape arity ≥ 2 | **not even a category** (Thm A) |

These are **strictly nested**: `{M = Id} ⊊ {M non-branching} ⊊ {all M}`. The first inclusion is
strict because `Maybe` (`E = A = 1`) and `Writer` are non-branching with `M ≠ Id`, hence — by
Prop 2.1 — with `W = G_M ≠ Id`.

**Corollary 2.3 (the conjecture's identification is false).** "Non-branching = collapse of
Atkey's index to a plain Freyd category" is **false**. Index collapse is `M = Id`, a *proper
sub-condition* of non-branching. By Theorem B, every non-branching `M ≠ Id` (`Maybe`, `Writer`,
every `E + A×(−)`) gives a genuine Hughes arrow whose coeffect input `W = G_M` is **nontrivial** — *presented* as an
*indexed* Freyd category (`W ≠ Id`), not manifestly a plain one (whether it is *secretly* plain is
Atkey's closedness question, orthogonal to branching). Atkey's index therefore does **not** collapse at the
non-branching boundary; it measures the coeffect (`M ≠ Id`), an axis **orthogonal to and coarser
than** branching. The two boundaries the conjecture equated are different (nested) boundaries. ∎

This already refutes the conjecture as stated. §3–§4 show that even after discarding the
mis-identification, there is no arity grade to be had.

---

## 3. The arity gap: the arity axis has no intermediate rungs

**Theorem 3.1 (arity gap).** A cartesian Set-monad `M` has maximal leaf-arity in `{≤ 1, ∞}`.
There is **no** cartesian monad of finite maximal arity `n ≥ 2`.

*Proof.* Suppose `M` is cartesian with a shape `s` of arity `n = |ar(s)| ≥ 2` and finite maximal
arity. Cartesian means `μ^M : M M ⇒ M` is a cartesian natural transformation: on leaves it is
substitution, and the leaf-set of `μ^M(t)` is the **disjoint sum** of the leaf-sets plugged in
(no merging, no dropping). Form `s(s,…,s) ∈ M(M X)` — the outer shape `s` with the shape `s`
plugged into each of its `n` leaves. Then `μ^M(s(s,…,s))` is a shape of `M` of arity
`Σ_{n leaves} n = n·n = n² > n`, contradicting maximality of `n`. Hence no finite maximal arity
`≥ 2` exists; the only possibilities are `n ≤ 1` (non-branching) and `n = ∞`. ∎

**Computational sanity (free magma, cartesian).** Binary-tree arities: `node = 2`, `node(s,leaf)
= 3`, `node(s,s) = 4`, `node(node(s,s),node(s,s)) = 8` — the self-plug `n ↦ n²` blows up, arities
`2,3,4,8,…` unbounded (`graded.py` sanity block).

**Corollary 3.2.** The conjectured tower "arity ≤ n" for `2 ≤ n < ∞` is **empty of monads**. The
non-branching bottom (`n = 1`) and the branching top (`n = ∞`) are the *only* levels the invariant
"maximal arity" takes among the monads where `T_M` exists. There is nothing in between to grade.
(∏-cointerpretation branching monads such as `Pf` likewise have unbounded arity — finite powers of
sets of every size.) The dichotomy is **Boolean because its underlying invariant is two-valued.** ∎

---

## 4. `E2′` is Boolean: the leaf grade is destroyed by the merging branching forces

Could a *finer* grade — leaf-count on the **arrows** rather than max-arity on `M` — restore an
associative graded composition for branching `M`? Grade `f : G_M p → T_M q` by the number of
leaves of `f₀(s) ∈ M S_q` (constant in `s` = "uniform-k"); a `k`-leaf shape whose leaves each spawn
a `j`-leaf shape has `k·j` leaves, so the intended grade monoid is `(ℕ, ×)`, identity `1` (the
1-leaf `η^M`-shapes of the identity arrow), `0` absorbing (nullary). Non-branching ⟹ every grade
∈ `{0,1}` ⟹ collapse to a plain Freyd category; branching ⟹ grades ≥ 2 appear.

**This grading fails.** (`graded.py`, `M = Pf`, objects `A1 = ({a,b}; a:2, b:1)`.)

* Uniform-`k` arrows are **still non-associative**: 12 violating triples out of 13824 (cap 8 per
  grade). Restricting to a fixed leaf-count does **not** repair `>>>`.
* The grade is **not even multiplicative**: 128 violations of `grade(g∘f) = grade(f)·grade(g)`.
  Explicit: `f = λs.{a,b}` (grade 2), `g = λs.{a}` (grade 1), yet `g∘f = λs.{a}` (grade 1 ≠ 2).

**Mechanism.** `Pf`'s multiplication `μ^T` is **union**, which is idempotent: when two distinct
leaves carry the same label, `μ^T` **merges** them, dropping the leaf-count. The biKleisli
composition *needs* `μ^T` — it is what gives identities their unit laws (via E1′/E3′) and what
performs the interchange — but that same `μ^T` collapses the grade. You cannot both keep `μ^T`
(for a category) and preserve a leaf grade (for the tower).

**Why merging is inseparable from branching here (so Theorem A stands).** One might hope a
*non-merging* branching monad (multiset, list — where distinct leaves never merge) would carry the
grade. But such monads are **outside the ∏-cointerpretation class**: the Ahman–Bauer `μ^T`
(`entwine.py:234`) requires the leaves of `μ^M(mm)` to have **distinct labels**, and
`μ^{multiset}([[a,b],[a]]) = [a,a,b]` repeats `a` — so `T_multiset` is undefined. Within the class
where `T_M` exists, distinct-labels + a branching (arity ≥ 2) shape **forces** label-sharing at a
small enough object `A`, which **forces** the merging `μ^T` to collapse — exactly the `E2′`
failure. Branching and merging are not separable inside the valid class; `Pf` is the paradigmatic
witness and Theorem A's "category ⟺ non-branching" is correct as stated.

**Both obstructions are ON/OFF.** The two independent axioms that branching disables — associativity
`E2′` (this §), and the effect-monad strength for `first` (Thm B, Lemma 3: a merge-*independent*
Yoneda argument, the only natural maps `C^n → C` being the `n` leaf-projections, no canonical
choice for `n ≥ 2`) — are each equivalent to arity ≤ 1. Neither is a graded quantity: they hold or
fail, with no intermediate degree. ∎

---

## 5. Where a genuine grading could live (open)

The one structure that *is* graded, and survives branching, is the **coeffect** side. `G_M` is a
comonad and is **always costrong** (Thm B, Lemma 2, every `M`); its "index" — Atkey's `W` — is
nontrivial for every `M ≠ Id` and is entirely independent of branching. A grading of `Arr_M` along
the coeffect, if one exists, would be a *graded comonad* grade (depth/size of `M∘P`), not an arity
grade. The Vollmer–Paviotti–Orchard machine `Gmd(I,κ) = [BI^op, κ]_lax` (CT2026; connection note
[[branching-obstruction-is-atkeys-index]]) organizes graded-monad/comonad distributive laws and is
the natural place to test this. It was **not accessible this session** (not yet on arXiv; no-browse
deep-work). Flagged as the open continuation. This is a *different* grading question from the
(refuted) arity one.

---

## 6. Verification (computational)

`scratch/monad-comonad-transfer/graded.py` (imports the verified `entwine.py`/`bikleisli.py`):

* Known `Pf` non-assoc witness has grade `None` (non-uniform: `a↦{a}` 1 leaf, `b↦{a,b}` 2 leaves).
* Uniform-leaf `Pf` arrows (A1-all, cap 8/grade): **12/13824 associativity violations remain**;
  **128 grade-multiplicativity violations** (`grade(f)=2, grade(g)=1 → grade(g∘f)=1`).
* Multiset `μ([[a,b],[a]]) = [a,a,b]` repeats `a` ⟹ `mu_T` distinctness assertion fails ⟹
  `T_multiset` undefined (multiset/list outside the class).
* Free-magma arities `2,3,4,8,…` (self-plug `n↦n²`), confirming the arity gap.

The Boolean results this builds on are all previously machine-verified: Thm A (`bikleisli.py`,
`Pf` non-assoc), Thm B (`arrows_first.py`, strength iff non-branching), the affine classification
(`affine_classify.py`, `affine_e2prime.py`), and the four Lean instances (`BiKleisli*.lean`).

---

## 7. Novelty / attribution

* **Atkey indexed Freyd categories / BiKleisli arrow**: Atkey ENTCS 229 (2011); Uustalu–Vene
  ENTCS 203 (2008). **PCM-graded ≅ Freyd**: Earnshaw–Nester–Román arXiv:2603.16375 Thm 4.23.
  **Cartesian / polynomial monads**: Gambino–Kock; Kock. All cited as framing; the results below
  stand on my own Thm A/B and elementary computations.
* **Contribution (MacBeth, this session):** (i) **Cor 2.3** — the conjecture's identification is
  false: index-collapse is `M = Id` ⊊ non-branching; Atkey's index measures the coeffect
  (`M ≠ Id`), orthogonal to & coarser than branching (sharpens the paper's Atkey remark). (ii)
  **Thm 3.1 arity gap** — cartesian max-arity ∈ {≤1, ∞}, no finite rung ≥ 2, so the arity axis
  carries no grade. (iii) **§4** — the natural `(ℕ,×)` leaf grade is destroyed by the merging that
  branching forces within the ∏-coint class (uniform arrows still non-assoc; grade non-multiplicative),
  and the confirmation that branching/merging are inseparable in the class (so Thm A needs no
  correction). Net: a **negative** resolution with three obstructions and a corrected boundary.

---

## 8. Gaps (precisely stated)

1. **Universality of "no grading."** §3–§4 refute the two *natural* gradings (max-arity on `M`;
   leaf-count on arrows) and correct the Atkey identification (§2). A theorem "no grading whatsoever
   refines the dichotomy" would quantify over *all* possible grade monoids/PCMs; not attempted. The
   conjecture *as stated* (arity-graded Atkey index) is refuted.
2. **Coeffect grading (§5).** Whether a graded-comonad grade on `G_M` (Vollmer–Paviotti–Orchard
   `Gmd`) organizes `Arr_M` is genuinely open; the paper was inaccessible this session (no-browse).
3. **Atkey's exact "closed indexed Freyd" definition.** §2 uses only "plain Freyd = no coeffect
   (`W = Id`)" + Thm B; it does not depend on Atkey's precise indexed-Freyd axioms. A line-by-line
   match of `Arr_M` to Atkey's Definition (his index category `J`) is deferred to a deep-read of
   ENTCS 229 (the gate flagged in PROVE.md; deferred under the session's no-browse rule).
4. **Scope = ∏-cointerpretation, cartesian.** As throughout the entwining program.
