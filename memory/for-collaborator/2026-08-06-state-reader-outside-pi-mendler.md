# Reader & State are OUTSIDE ∏-Mendler — the census hypothesis was wrong (μ drops leaves)

**MacBeth, 2026-08-06 PROVE.** For Neil/Robin, and for the dream cycle.
Full proof: `proofs/2026-08-06-state-reader-ladder-census.md`. Verified: `scratch/pi-mendler-boundary/kappa_test.py`.

## The one-paragraph version

This cycle's PROVE task asked me to upgrade "Reader `X^E` and State `(S×X)^S` are ∏-Mendler,
non-cartesian monads, witnessing `cartesian ⊊ ∏-Mendler`" from *computed* to *proved*. **It's false.**
Reader and State are **not ∏-Mendler**. Their ∏-cointerpretation lift `T_M(S,P)=(MS,P^⋆)` is a
well-defined endofunctor and even has a unit, but it has **no multiplication `μ^T`**. So they are not
monads on `Cont` at all via this construction, and they cannot sit on the ladder between `cartesian` and
the ∏-Mendler boundary. The crown's classical witness for `cartesian ⊊ ∏-Mendler` — **`Pf` (powerset)** —
is untouched and remains the right one.

## Why the compute pass was wrong (a clean variance error)

The multiplication laxator a monad `T_M` needs is `j:P^⋆(μ mm)→(P^⋆)^⋆(mm)`, running
`∏_{lv(μ mm)} → ∏_{I(mm)}` (few leaves → many inner-leaf tokens). **By Yoneda, every natural such map is
a reindexing along a *total, label-preserving* function `κ_μ:I(mm)→lv(μ mm)`** — and it exists *iff* such
a `κ_μ` does. (If any inner-leaf label is absent from `μ mm`, there is literally no natural map to that
coordinate — the Yoneda hom-set is empty.)

- **Pf**: `κ_μ(i,x)=x` — total, non-injective ⟹ `j` exists, `μ^T` non-cartesian. ✓ ∏-Mendler.
- **Reader**: `μ` = diagonal `μG(e)=G(e)(e)`. The off-diagonal inner token `(e,e')` (`e≠e'`) has label
  `G(e)(e')`, which for generic `G` is not any diagonal label ⟹ `κ_μ` **not total** ⟹ **no `j`**.
  Witness: `G=((0,0),(1,0))`, `μG=(0,0)`, dropped label `1`.
- **State**: same — threading reads one inner leaf per outer, drops the rest.

The compute pass had spotted a *single-valued* map `δ:E→E×E, e↦(e,e)` and called it "the ∏-Mendler
`i_P`". That is (a) about `μ` not the unit, and (b) the **wrong variance** — it is a *section* of `κ_μ`,
pointing `lv(μ mm)→I(mm)`, not the `κ_μ` that `j` reindexes along. Its single-valuedness is irrelevant.

## The correction to my own crown notes (honesty)

The crown (`2026-08-05-crown-gap-closure.md`, Lemma 1.3) excluded Reader/State from ∏-Mendler for the
**right conclusion but the wrong reason** ("no unit `i_P` / it would have to be an iso"). In fact a natural
**unit** laxator `i_P` *does* exist for Reader (project to any leaf; `Nat(∏_{lv(η s)}ev_s,ev_s)=lv(η s)≠∅`).
The real gate is the **multiplication** `j`. I've appended the correction to the crown note (§8) and to the
registry node `crown-boundary-table`; the crown's stratification and its `Pf` witness are unaffected.

## What we actually get (better than the conjecture)

A **trichotomy of non-cartesian `μ`**, by how the leaf-covering `κ_μ` breaks:

| failure | `κ_μ` | ∏-Mendler? | witness |
|---|---|---|---|
| **MERGE** | total, non-injective | **inside** (witnesses `cartesian ⊊ ∏-Mendler`) | `Pf` |
| **DROP** | non-total | **outside** | `Reader`, `State` |
| **SYMMETRY** (`P^⋆` ill-defined) | — | **outside** | `Bag` |

So ∏-Mendler = polynomial-functor monads whose `μ` **drops no leaf** and has **rigid labels** — *merging is
allowed* (that is the whole content of `cartesian ⊊ ∏-Mendler`). Reader/State are the canonical
**leaf-dropping** monads, sitting outside on the polynomial side, symmetrically opposite `Bag` (analytic).
This is a cleaner, more honest boundary than the deleted "extra rung".

## For the grant/book

- `cartesian ⊊ ∏-Mendler` is real and witnessed — by **`Pf`**, not Reader/State. No change to the ladder.
- The reusable slogan: **"∏-cointerpretation tolerates merging but not dropping."** Effectful monads that
  *reuse/thread* an environment (Reader, State) are exactly the leaf-*droppers* — a crisp reason they resist
  the container-monad lift, worth one sentence in the book's boundary discussion.
- Triggers updated: LEAN now targets the DROP fact (κ_μ non-total, `decide`); WRITE is correction-only
  (do not add the false rung).

## Book audit (WRITE session, 2026-08-06) — no change needed

I checked the stratification payoff box (`books/category-of-containers.tex`, teachbox
"The fibration stratifies the monad zoo", §Monads-and-Comonads, lines ~2792–2825). **It is
already correct** and needs no edit: it names **Pf** as the `cartesian ⊊ ∏-Mendler` witness
(μ=∪ merges leaves), never lists Reader/State as ∏-Mendler, and the one ∏-Mendler-context
Reader mention (line 2501) already says "the reader monad $A^K$ is *not* one." The State
mentions elsewhere are the `ΔS`/store-comonad/Workers thread, a different construction. So
the false census rung never entered the book — nothing to delete.

**One residual imprecision, logged for a future book-writing pass (not this correction
pass):** the box labels its top rung "polynomial / ∏-Mendler monads". Post-refutation that
slash is loose — Reader and State *are* polynomial monads (P1) but *not* ∏-Mendler, so
polynomial ⊋ ∏-Mendler. Optional one-clause fix when someone next edits the box prose: name
the top rung "∏-Mendler monads" and add "(polynomial monads whose μ drops no leaf and has
rigid labels — excluding the droppers Reader, State and the symmetric Bag)". That is the
natural home for the trichotomy slogan, but it *adds* content, so it is out of scope for a
surgical correction and I left it.

## Open / mechanical
- State's non-total `κ_μ` proven at `|S|=3`; the general `|S|≥2` off-state-drop is the identical mechanism.
- A–B Def 6.2 internal wording ("laxators `i_P`, `j` + coherence"): my verdict is derived directly from
  "`T_M` is a monad on `Cont`", which forces the laxator directions, so it doesn't hinge on re-reading their
  coherence diagrams — but pinning "their `j` = my `κ_μ`-reindexing, their class = κ_μ-total + label-rigid"
  from the paper text is a clean follow-up if anyone wants the A–B-internal statement.
