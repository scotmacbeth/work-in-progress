# ⊗-monoid classification — PROVED (was computed) — 2026-07-19

**For Neil / Robin. One-line:** the last open cell of the (co)monoid table is now analytically proved.

## What was closed
`dirichlet-monoid-classification` (registry) moves **computed → proved**. Full proof:
`proofs/2026-07-19-dirichlet-monoid-classification.md`. Trustcheck green.

## The result (Theorem A)
A monoid `(c, μ:c⊗c→c, η:y→c)` for the **Dirichlet tensor** `(Cont,⊗,y)` is **exactly**:
- a **monoid** `(·, e)` on the shape set `S = c(1)`, plus
- an **oplax monoidal functor** `P:(S,·,e)→(Set,×,1)` on fibres — maps `φ_{s,t}:c[s·t]→c[s]×c[t]`
  and a forced counit `ε:c[e]→1`, obeying the oplax associativity + two unit coherences.

The proof is the dual unwinding of `2026-07-17-bare-dirichlet-comonoid.md`: split each monoid law into
its **shape part** (forward map `S×S→S` — becomes the monoid) and **fibre part** (backward map
`c[s·t]→c[s]×c[t]` — becomes the oplax structure). Elementary; ~2 pages.

## The one idea worth remembering (§5) — why the dual is NOT a mirror
Comonoid and monoid live over the *same* tensor, but the shape map points opposite ways:
- **δ:c→c⊗c** — shape map `S→S×S`, **forced to the diagonal** by the counit (× is cartesian). Fibres
  get a *covariant* op `c[s]×c[s]→c[s]` = a **monoid**. ⟹ *family of monoids* (shapes trivial).
- **μ:c⊗c→c** — shape map `S×S→S`, **unconstrained beyond being a monoid**. Fibres get a
  *contravariant* op `c[s·t]→c[s]×c[t]` = **oplax**. ⟹ *monoid on shapes + oplax on fibres*.

Comult maps *into* the cartesian product of shapes (⟹ diagonal forced); mult maps *out of* it (⟹ any
monoid free). Same cartesian fact *trivialises* one layer and *liberates* the other. This is the honest
climax for the (co)monoid table you asked about.

## Bonus (Theorem B) — the whole table is ONE theorem
The `×`-monoid (categorical product) is the **same** statement with the fibre target `(Set,×,1)`
replaced by `(Set,⊔,∅)`:
> `×`-monoid = monoid `(S,·,e)` with **identity fibre `c[e]=∅`** + oplax functor `(S,·,e)→(Set,⊔,∅)`.

`η:1→c` forces `c[e]=∅` (backward `c[e]→∅`); `μ♯:c[s·t]→c[s]⊔c[t]` is a backward routing. Generic
containers admit **none** (empty-identity-fibre obstruction); all-fibres-empty ⟹ `×`-monoids = monoids
on `S` (recovers "cartesian monoids = internal monoids", counts 1,4,33). So both cells of the *monoid*
column are the same theorem, parameterised by the fibre monoidal structure `(Set,⊙,I)` that the tensor
uses (`⊗`→`(×,1)`, `×`→`(⊔,∅)`).

## Verification
Two independent brute-force enumerations agree on every small case: direct monoid-law check on Poly
morphisms vs. from-scratch `(monoid + oplax functor)` count — `scratch/monoid-comonoid-table/c6_oplax.py`
(⊗: 1,1,1,4,9,33 all match) and `times_monoid.py` (× refinement, all match).

## Framing / caution (from novelty gate 07-18)
Frame as **"an elementary answer to an explicit future-work item"** (Niu–Spivak **Remark 3.78** flags
⊗-monoids in Poly as uncharacterised future work), **not** a deep theorem. **Share promptly**: the same
group (De Pascalis–Uustalu–Veltrì, arXiv:2509.25879, who did the `◁`-monoid = indexed-polynomial-monad
side) list *other-tensor* monoids in their §5 future work. This is orthogonal to their `◁` result.

## Next
- `/lean` target: formalise Theorem A forward direction (⊗-monoid ⟹ monoid+oplax) — mirrors the
  already-lean-verified `DirichletComonoid.lean` forward map. Would give the monoid column a machine
  check to sit beside the comonoid column.
- Book: this is the climax paragraph of the monoidal-structures chapter's (co)monoid section.
