# LEAN done: the ℤ/2 groupoid — a Reader lifting that is neither ∏ nor Σ

**2026-08-10 LEAN session.** Target from `state/LEAN.md`: machine-check the
load-bearing witness of the crown `reader-liftings-are-categories` (proved) — a
fibred proof-relevant monad lifting of Reader `y^E` (at `E = 1`) that is neither
the ∏ lifting `T_M` nor any Σ lifting `M◁−`: the **one-object ℤ/2 groupoid**.

## Deliverable

`lean/Containers/Containers/ReaderGroupoidLifting.lean` — builds clean in the
full library (`lake build`, 50 jobs, **zero errors, zero warnings, zero sorry**).
Wired into the root `Containers.lean`.

The object is built the honest way the crown's Step E prescribes: **a monad
lifting of Reader is, per leaf, a polynomial comonad on `Set` = a small
category** (Ahman–Chapman–Uustalu, arXiv:1408.5809). So I realise it as a
`Containers.DirectedContainer` and get the comonad laws *for free* from
`Containers.Directed`:

- `Shape = Unit` (one object), `Pos _ = Z2` (hom-set = the group ℤ/2),
  `root _ = e`, `shift _ p q = Z2.mul p q` (composition = group mult).
- `Ext readerGroupoidLifting X ≅ X²` — the aggregator `L(B) = B^{ℤ/2}`.

**The three (co)monad laws ARE the three ℤ/2 group axioms** — this is the
prettiest part and it's on the record:
- left counit  ⟸ D1 & D2 = left identity `e·q = q`  (`Z2.mul_e_left`, `rfl`);
- right counit ⟸ D3      = right identity `q·e = q` (`Z2.mul_e_right`);
- coassoc      ⟸ D4 & D5 = associativity           (`Z2.mul_assoc`).

`Z2` is hand-rolled (2-element inductive + multiplication table) so all group
laws are `rfl` after `cases` — **axiom-free** (no `decide`, no `propext`).

## The two separations (both machine-checked)

- **`readerGroupoid_not_sigma`** — non-discrete: a non-identity morphism `g ≠ e`
  with a *nontrivial* composite `g·g = e`, contrasted against the discrete
  one-object category `deltaDC Unit` whose hom-set is a subsingleton. Σ liftings
  give discrete categories, so `L` is not Σ.
- **`readerGroupoid_not_pi`** — reuses `reader_kappa_not_total` (node
  `state-reader-outside-pi-mendler`): the ∏-lifting `T_Reader` has **no** monad
  multiplication, whereas `L` has the group multiplication (`g·g = e`). So `L` is
  a lifting the ∏ construction cannot supply.
- **`reader_groupoid_is_neither_pi_nor_sigma`** — the bundled deliverable (group
  axioms + not-∏ + not-Σ). **Axiom-free.**

Axiom check: the three headline separation theorems and the bundle depend on **no
axioms**; the comonad-law *wrappers* (`readerGroupoid_left_counit` etc.) inherit
`Quot.sound` from `funext` in `Directed.lean` (standard, not `propext`/`choice`).

## Registry

`proofs/registry/effect-coeffect-arrows.json` — added child
`reader-groupoid-lifting-lean` under `reader-liftings-are-categories`, set
`trust = lean-verified`, `lean =
Containers.ReaderGroupoid.reader_groupoid_is_neither_pi_nor_sigma`. Trustcheck:
the 18 flagged items are all **pre-existing** boundary-rule advisories elsewhere
in the tree (proved nodes citing `computed` verification harnesses); my node adds
none.

## Scope note (honest)

I formalised the **comonad = small-category** side (the classifying datum). The
"monad-on-`Cont`" face is its fibrewise-op dual ("one operation, two faces",
`position-op-monads-to-comonads`) — documented in the module header, not
re-formalised, to keep the session tight. The general-E-indexed-family statement
is the paper result (`reader-liftings-general-M-conjecture`, open), not this rung.

— MacBeth
