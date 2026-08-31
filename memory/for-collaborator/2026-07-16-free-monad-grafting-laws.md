# Free monad on a container as a ◁-monoid: the grafting-monoid laws spelled out

**MacBeth, 2026-07-16 (prove session).** For Robin / Neil.

## One-line

Wrote out the three monoid laws of the **free monad on a container** `(S◁P)` — the checks
Gambino–Kock (arXiv:0906.4931 Thm 4.5) call *"lengthy but routine"* and **omit** (pp. 30–31) — as
explicit **container-coordinate** morphism equations, proved by structural induction on trees.
File: `proofs/2026-07-16-free-monad-grafting-laws.md`. Registry `free-monad-grafting` (proved,
trustcheck green).

## What is and isn't claimed (novelty guard held)

- **NOT claimed:** the construction (positions = trees, directions = **leaves**, `μ` = grafting,
  `⟦S*◁P*⟧ ≅` free-monad functor). That is Gambino–Kock Thm 4.5, 2009 — prior art, deep-read.
- **The contribution** is *only* the omitted calculation, in coordinates: the monoid `(S*◁P*,
  graft, lf)` in `(Cont, ◁, I)`, each law as (forward-on-shapes, backward-on-positions), matched
  to the standard unitors/associator taken verbatim from my `Composition.lean`. This is the monoid
  **mirror** of my M3/M3b comonoid work (directed container = ◁-comonoid), same `◁`, opposite
  variance — `δ : m ⇒ m◁m` there, `μ : m◁m ⇒ m` here.

## The mathematics, compressed

Carrier `m = (S* ◁ P*)`: `S*` = closed `P`-trees; `P*(t) = leaves(t)`. `μ = graft`, `η = lf`.

Four lemmas, all inductions on the outer tree `t`:

- **Lemma A (leaf bijection):** `leaves(graft(t,u)) ≅ Σ_{ℓ∈leaves(t)} leaves(u_ℓ)` by path
  concatenation; inverse = split at the **unique** `t`-leaf prefix. *Consequence worth flagging:*
  `μ♯` is **forced** — a proper extension of a leaf-path is never a leaf-path, so there is exactly
  one place to cut; nothing to get wrong once you commit to the `t`-leaf boundary.
- **Lemma B:** `graft(t, λℓ.lf) = t` — the forward half of the **right-unit** law.
- **Lemma C:** `graft(graft(t,u),v) = graft(t, λℓ.graft(u_ℓ,v_ℓ))` — grafting is associative, the
  forward half of **associativity**; this is the real substance.
- **Lemma D:** the associator-square backward coherence = **associativity of list concatenation**
  (every doubly-grafted leaf is a *unique flat path* `ℓ·w·x`, Cor A′).

The unit laws then collapse to base clauses of `graft`/`split`; assoc = Lemma C (fwd) + Lemma D (bwd).

## Confidence

- Computationally exhaustive: 6 containers (binary trees, lists, several mixed-arity), all closed
  trees ≤ 3 internal nodes, **all** label functions — every law holds in *both* components.
- The leaf-split is a **verified bijection** (inverse = concatenation), thousands of leaves.
- **Negative controls fire** (so it's not a mirror): an identity-substitution "wrong graft" is
  caught by the assoc forward check; an information-losing "wrong split" is caught by the assoc
  backward check. (A naive "deepest-prefix" wrong split does *not* fire — correctly, because
  Lemma A shows the prefix is unique, so it equals the real map.)
- Reconciled against a hand-worked binary-tree instance.

## Where this points (my recommendation)

The **strongest-novelty artifact is the Lean formalisation** (LEAN.md target): there is no
machine-checked proof that the free monad on a container is a polynomial monad with grafting `μ`
and verified monad laws (checked: Aberle arXiv:2604.01303 uses a free-monad AST in Agda but does
*not* formalise the G-K positions=trees/directions=leaves iso). This note is the paper-level
companion — the four lemmas above are exactly the Lean proof obligations (carrier as a W-type,
`graft` by well-founded recursion, Lemmas B/C by structural induction, A/D by the same), dual to
`Comonoid.lean`/`ComonoidConverse.lean`. I've set the LEAN trigger to it.

**Question for Neil:** does this belong in the book's Phase-2 (free monad / cofree comonad)
chapter as the worked "grafting laws" section, paired with the cofree-comonad mirror? It reads as
the natural monoid counterpart to the M3 comonoid chapter.
