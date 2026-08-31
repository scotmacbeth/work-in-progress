# Five independent lineages generalize attention beyond matrices — none uses container framing, none gives a depth-composition law

**Status:** live connection, crown-jewel for Neil's #1 priority ("find a USE for Vec-containers").
**Consolidated:** dream 2026-08-27; **updated WAKE 2026-08-28** — fifth lineage (Mahadevan KET,
arXiv:2605.27259) read and placed; action item 1 discharged.

## The pattern

There are now **five independent research lineages** that all make the same structural move —
*replace the weight matrix of an attention/MLP layer with a linear-algebra-valued structured functor*
— and **not one of them uses container / Poly / polynomial-functor language**, and **none cites any
other** (zero cross-citation, checked). Sharper still, **not one of the five gives a compositional law
for DEPTH / layer-stacking** — every one models a *single* layer (or a weighted aggregation) and then
treats depth L as an experimental hyperparameter. That missing law is exactly the container delta: my
**free ◁-monoid = tensor algebra `⊕_L AttP^{⊗L}`** ([[oneill-free-monad-tensor-algebra-linear-container]])
IS the stacking law, and **degree-`3^L`** ([[linear-attention-odot-degree-3L]]) is the quantitative form
of the linear/nonlinear boundary all five only gesture at. This is the sharpest framing of the stakes:
the container/Poly framing is a genuine contribution **only if it unifies these five** — and its
distinctive, uncontested contribution is precisely the **compositional/stacking** axis none of them touch.

| # | Lineage | The "vector" is… | Machinery | Citation |
|---|---------|------------------|-----------|----------|
| 1 | **Vertechi** — NN layers as parametric spans | index-set span `s ← P → t` with `w[π(p)]` | span/`Fam`, `y[t(p)]+=x[s(p)]·w[π(p)]` | (agent-summary — *verify before load-bearing*) |
| 2 | **O'Neill** — self-attention as parametric endofunctor | `Para(Vect)` 1-morphism, param obj `AttP=QP⊕KP⊕VP` | free monad on layer endofunctor, `T=colim(id,F,F²,…)` | arXiv:2501.02931, Def 2.3 / Thm 3.1–3.2 (**full-text verified 08-27**) |
| 3 | **Hedges** — generalized transformers from applicative functors | any applicative (lax-monoidal+strength) functor: `CVector`, binary trees, distributions | `pair`/`Counit`/`Ring` typeclass replaces sum-product linear algebra | cybercat.institute 2025-02-12 (blog; not GPU-competitive, author's own caveat) |
| 4 | **Maruyama** — category-equivariant deep learning | `Vect`-valued presheaves `X,Y:C^op→Vect` | continuous nat. transf. as layers; naturality = equivariance; universal-approx density | arXiv:2511.18417, Def 10 / Thm 3.1 (full HTML read; **zero** cite of Ghani/Ahman/Uustalu/Spivak) |
| 5 | **Mahadevan** — Kan Extension Transformers | `Vect`-valued source features `X:𝒩→Vect` over a neighborhood category | layer = weighted (discretized) **left Kan extension** / coend `∫^σ W(t,σ)⊗X(σ)`; attention = singleton nbhd, KET = simplicial nbhd | arXiv:2605.27259 (Adobe/UMass, v2 25 Jul 2026; full 31pp read WAKE 08-28; **zero** cite of O'Neill/Ghani/Ahman/Uustalu/Spivak/Poly) |

*(Separate but adjacent: Hedges "Autodiff through function types" (julesh.com 2026-02-20) — additive
lenses CCC because commutative monoids have biproducts = my [[extensivity-is-the-container-boundary]]
lemma. That is a **structural rhyme**, not a fifth attention-layer lineage.)*

## Why it matters (the actual delta the container framing must deliver)

Each lineage independently rediscovers a *fragment* of the container/Poly structure:
- **O'Neill's free monad** IS the free ◁-monoid on the one-shape linear container `(⋆,AttP)` = the
  **tensor algebra `T(AttP)=⊕_L AttP^{⊗L}`** — *proved* 2026-08-27
  (`proofs/2026-08-23-oneill-free-monad-linear-container.md`, registry
  `oneill-free-monad-linear-container` = **proved**). His "colimit of bare powers" is corrected to the
  Adámek partial-sum chain `⊕_n Fⁿ`; residual/skip connection = the unit η (pointable, not
  well-pointed). This is the **first** of the four placed *inside and corrected by* the container
  framework. → [[lean-free-monad-unit-laws-done]], instantiates the degree-3^L boundary
  ([[linear-attention-odot-degree-3L]]).
- **Vertechi's span** `s←P→t` is literally a container shape/position pair with a Vec-valued action on
  positions — the `Fam(Vec^op)` container object, unglossed.
- **Maruyama's `Vect`-valued presheaves** are exactly the objects of the Vec-container front
  (`Fam(Vect)`-valued), with **naturality standing in for the directed-container law**; his
  universal-approximation density theorem is a property of the whole functor category that the container
  equivalence could re-derive.
- **Hedges' applicative functors** are the lax-monoidal generalization; the container ◁/⊗ tensors are a
  *specific* applicative structure. The question: is "container" a strictly stronger hypothesis than
  "applicative," and does the extra strength buy a composition/orchestration theorem Hedges can't state?

**The unification thesis (to test, not yet claimed):** all four are instances of *linear containers
over `Fam(Vec^op)`* with their layer-stacking = the ◁-monoid free-monad construction. If true, the
container framing is the common generalization that (a) explains *why* stacking is a free monad
(O'Neill) not one morphism — the degree-`3^L` non-collapse; (b) explains *which* algebraic structure is
minimal (Hedges applicative vs container ◁); (c) gives the naturality/equivariance layer (Maruyama) a
compositional-orchestration reading. If false, the honest verdict is "container framing is one more
un-unifying dialect" — and that is worth knowing too.

## Action items

1. ✅ **DONE (WAKE 08-28) — arXiv:2605.27259 "Kan Extension Transformers" read (full 31pp).** Verdict:
   **orthogonal parallel lineage, NOT a scoop, NOT a container lineage.** Mahadevan models a layer as a
   weighted discretized **left Kan extension / coend** over a neighborhood category (attention = singleton
   nbhd; simplicial = KET). Its one theorem-grade statement (§10.6) is a *honesty caveat*: the coend is a
   genuine enriched Kan extension **only in the representable case**; softmax weights are non-representable,
   so generic attention is only "Kan-style," an analogy not an identity. **This independently rediscovers
   my linear/nonlinear boundary** (representability ↔ my degree-1 vs degree-`3^L`) — cite as external
   corroboration. Critically, KET gives **no depth/stacking composition law** (L is a hyperparameter), so
   my free-◁-monoid stacking result and degree-`3^L` bound are entirely **uncontested**. → the fifth row
   above; strengthens the thesis (the missing composition axis is now confirmed across all five).
2. **The five-lineage unification note is now the live WRITE target** (`expository/`, grant-facing). The
   comparison pass is owed; the KET read gives it a clean spine — *five categorical accounts of a single
   attention layer, all hitting the same linear/representable boundary, none supplying a compositional law
   for depth; the container framing supplies exactly that (free ◁-monoid = tensor algebra) and makes the
   boundary quantitative (degree-`3^L`).* Set as WRITE.md this WAKE.
3. Verify Vertechi (#1) at full-text before it becomes load-bearing (currently agent-summary).

## Cross-links
- [[extensivity-is-the-container-boundary]] — the Vec biproduct-collapse lemma (also universal:
  Hedges autodiff).
- [[linear-attention-odot-degree-3L]] — the degree-`3^L` boundary that forces the free-monad tower.
- [[orgtr-dcont-constant-trees]] — the *other* frontier (adaptive interfaces); this is the *linear/ML*
  frontier.
- topic `containers-over-vec.md` — the home front.
