# Lean: (Cont, ◁, I) is a monoidal category — DONE (PR #17)

**Branch:** `lean-monoidal-coherence` (fork `scotmacbeth`), **base `lean-composition-product`** (PR #13).
**PR:** https://github.com/RaggedR/ghani-containers/pull/17
**File:** `lean/Containers/Containers/Monoidal.lean` (+ root import).

## What it proves
Closes the gap LEAN.md flagged: `Composition.lean` (PR #13) already had `◁`, `I`,
unitors, associator (transport-free isos). This adds the rest of the Mac Lane data and
certifies **(Cont, ◁, I) as a monoidal category**:

- `Container.comp₂` — bifunctor action of `◁` on a morphism pair; `comp₂_id`, `comp₂_comp`.
- `whiskerLeft` / `whiskerRight` (= `comp₂` with an identity).
- `associator_naturality`, `leftUnitor_naturality`, `rightUnitor_naturality`.
- `Container.pentagon`, `Container.triangle`.
- Hand-rolled `MonoidalCategory` typeclass (extends repo `Category`, **Mathlib-free**) +
  `CatIso` + `ContainerIso.toCatIso` coercion + instance **`ContMonoidal`**.

## Key fact
**Every law is `rfl`.** `comp₂` is transport-free (position fibres `F.Pos ((m u).2 v)`
agree definitionally with `F.Pos (k ⟨u,v⟩)`), so both pentagon legs flatten the fourfold
composite to the same right-nested normal form — exactly the informal proof's "flattening"
(Part A of `proofs/2026-06-13-monoidal-coherence-four-structures.tex`). Cleaner than the
LEAN.md prediction ("Quot.sound of a Sigma rearrangement"): the coherence *step itself* is
defeq. `#print axioms` → only `Quot.sound` (via `funext`, inherited from `Composition.lean`'s
iso-law proofs). No `sorry`. Zero warnings.

## For whoever extends this
- The `MonoidalCategory` class is **generic over any `Category`** — reuse it directly for
  the other three monoidal structures on Cont (`+`, `×`, Dirichlet `⊗`). Each will need its
  own `tensorHom` + coherence proofs; the Dirichlet case is the interesting one (its
  associator is Cartesian reassociation, and `⟦–⟧` is *strict* monoidal — see
  `monoidal-coherence-four-structures` memory).
- Next obvious Lean target: **`⟦–⟧` is a (strong) monoidal functor** for `◁`
  (`⟦G◁F⟧ = ⟦G⟧∘⟦F⟧` is already in `Composition.lean` as `compExt`/`compExtInv`); package the
  comparison as a monoidal-functor instance once we have a `MonoidalFunctor` class.

## Env note (bit me this session)
The container repo is **pure Lean 4 core, no Mathlib** (no `lake exe cache get`). The
toolchain was **not installed** at session start — had to `elan` + lean v4.30.0 fresh.
`export PATH="$HOME/.elan/bin:$PATH"` then `cd lean/Containers && lake build`.
