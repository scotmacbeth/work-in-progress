# Reader/State census — REFUTED; book needs no change (WRITE session sign-off)

**MacBeth, 2026-08-06 WRITE.** For Neil / Robin. This is the write-session record; the full
mathematics lives in the two sources linked below — read those, not a re-summary here.

## What this session did
A **correction-only** pass. The pre-PROVE census — *"Reader `X^E` and State `(S×X)^S` are
∏-Mendler non-cartesian monads, witnessing `cartesian ⊊ ∏-Mendler`"* — was **refuted** earlier
today. This session audited the book's stratification box against the refutation and made
**no edit**, because the box was already correct.

## The refutation, in one line
Reader and State are **not ∏-Mendler**: their ∏-cointerpretation lift `T_M` has a unit but **no
multiplication** — `μ` drops leaves, so the reindexing `κ_μ : I(mm) → lv(μ mm)` is **not total**
and the mult-laxator `j` does not exist. So they never sat on the ladder. The classical witness
for `cartesian ⊊ ∏-Mendler` is **Pf** (powerset, `μ=∪` merges leaves), and it is untouched.

Corrected boundary — a **trichotomy of non-cartesian μ** by how `κ_μ` breaks:

| failure | `κ_μ` | ∏-Mendler? | witness |
|---|---|---|---|
| **MERGE** | total, non-injective | **inside** (witnesses `cartesian ⊊ ∏-Mendler`) | `Pf` |
| **DROP** | non-total | **outside** | `Reader`, `State` |
| **SYMMETRY** (`P^⋆` ill-defined) | — | **outside** | `Bag` |

Slogan: **"∏-cointerpretation tolerates merging, not dropping."**

## Book audit — no change
`books/category-of-containers.tex`, teachbox *"The fibration stratifies the monad zoo"*
(§Monads-and-Comonads, `sec:moncomon-fibration`, lines ~2792–2825): **already correct.**
- Names **Pf** as the `cartesian ⊊ ∏-Mendler` witness (Pf = flagship ∏-lifting at line 2500;
  "μ=∪ merges leaves … outside even [cartesian]" at lines 2814–2816).
- Never lists Reader/State as ∏-Mendler. The one ∏-context reader mention (line 2501) already
  says "the reader monad `A^K` is *not* one"; the later Reader/State material (2882–3040) is the
  `ΔS`/store-comonad/Workers thread, a different construction.
The false rung never entered the book — nothing to delete, nothing to compile.

## Logged for a FUTURE book-writing pass (out of scope for a surgical correction)
The box's top rung is labelled *"polynomial / ∏-Mendler monads"*. Post-refutation the slash is
loose: Reader (`=y^E`) and State are **polynomial** monads but **not ∏-Mendler**, so
polynomial ⊋ ∏-Mendler. A proper write pass should rename the rung "∏-Mendler monads" and add one
clause naming the droppers (Reader, State) and the symmetric Bag — the natural home for the
trichotomy slogan. This *adds* content, so it was **not** done here.

## Sources (authoritative — cite these, not this note)
- Proof: `proofs/2026-08-06-state-reader-ladder-census.md` (refutation §2; Lemma 1 Yoneda
  reindexing criterion; item (C) general uniform witness closed).
- Fuller collaborator note (variance-error diagnosis, unit-vs-mult correction to the crown,
  grant/book framing): `for-collaborator/2026-08-06-state-reader-outside-pi-mendler.md`.
- Item-(C) closure (drop uniform in `|E|,|S|≥2` at `|X|≥2`; Reader≡State one mechanism):
  `for-collaborator/2026-08-06-reader-state-drop-item-C-closed.md`.
- Lean (finite DROP core): `for-collaborator/2026-08-06-lean-reader-state-drop.md`.
