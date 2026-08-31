# The branching obstruction IS Atkey's index

**Claim.** MacBeth's non-branching dichotomy for effect–coeffect arrows is not a new
kind of obstruction — it is the *collapse of Atkey's index*. The sharper statement of
[[effect-coeffect-arrows-first-strength]] is:

> **M non-branching ⟺ `Arr_M` collapses from a (closed) *indexed* Freyd category to a
> genuine (non-indexed) Freyd category.**

## Why

Atkey, *What is a Categorical Model of Arrows?* (MSFP 2008 / **ENTCS 229, 2011**, 18pp,
deep-read via the n-Café "Burrito Monads" guest post 2025-08-28) settles the folklore
"Arrows = Freyd categories" as **false**: Hughes Arrows are *strictly more general*
because an Arrow admits a **second, possibly comonad-structured input** that a Freyd
category lacks. The correct theorem is **Arrows ≅ closed *indexed* Freyd categories**.
His §2 gives the exact **BiKleisli Arrow**: comonad `W`, monad `T`, distributive law
`λ:WT→TW` ⟹ `Ar(x,y)=[Wx→Ty]` is an Arrow (citing Uustalu–Vene).

That `Ar(x,y)=[Wx→Ty]` is **verbatim** MacBeth's `Arr_M(p,q)=Cont(G_M p, T_M q)` with
`W=G_M`, `T=T_M`, `λ=κ`. So the question "is `Arr_M` a genuine (non-indexed) Freyd
category?" is exactly Atkey's index-collapse question. MacBeth's answer — *yes iff M is
non-branching* — locates the branching obstruction inside a **named 20-year-old
landscape** rather than presenting it as sui generis.

## Value

- **Sharper framing, now book Ch4** (the standalone paper was PAUSED by Neil 08-04 →
  everything folds into the "Monads and Comonads" book chapter; see SUMMARY):
  state the dichotomy against Atkey's indexed/non-indexed distinction; his Fig. 1
  (monad ⊂ Freyd ⊂ indexed-Freyd ⊂ Arrow landscape) is a ready pedagogical anchor. The
  object-level shadow of the index-collapse is the profunctor reframing
  [[arr-profunctor-free-category-costs-branching]]: *closed indexed Freyd = profunctor with
  a second input; genuine Freyd = the profunctor composes.*
- **★ Primary source secured (08-04 browse, closes a polish thread since 07-31):**
  **Power–Thielecke, "Closed Freyd- and κ-Categories", ICALP 1999** (deep-read via CiteSeerX;
  `sources.json`) is the citable origin of "closed indexed Freyd category" — four equivalent
  λc-model presentations incl. closed Freyd `J:C→K` and closed κ-category `H:C^op→Cat`.
  **⚠️ κ FALSE-FRIEND:** their κ = Hasegawa's stack-passing κ-calculus, UNRELATED to my
  compositor `κ:GT⇒TG`; the Plumbing/Baez–Waites orchestration post uses the *same* Hasegawa κ.
  Three-way collision — disambiguate in the book. (Details in the profunctor note.)
- **★ Dichotomy is now iff at FULL-morphism level (08-04 prove).** The 07-31 Lean negative
  witness was fibre-only; [[branching-full-morphism-lift]] proves branching non-associativity
  as full `Cont`-morphisms (`M=Pf`, composites differ at one leaf) ⟹ "`Arr_M` genuine Freyd
  ⟺ M non-branching" holds at the full-morphism level, not merely fibrewise.
- **Attribution is already correct** — Atkey ENTCS 229 + Uustalu–Vene are cited by name
  in the existing `effect-coeffect-arrows` proofs; the browse independently verified this
  (zero scoop risk). The find is a *strengthening*, not a correction.
- **Open (worth one wake pass):** does Atkey's "closed indexed Freyd category" already
  have a name for the *degree* of index-nontriviality that would refine "non-branching"
  into a graded statement (arity 1 vs arity ≤ n)?

## The arity axis is uncrowded — three independent corroborations

Same 07-31 browse: the field is actively building graded/Freyd machinery, but along
**other axes**, never arity/branching:
- **Earnshaw–Nester–Román, arXiv:2603.16375** (full-text): PCM-graded monoidal cats;
  **cartesian PCM-graded ≅ Freyd categories (Thm 4.23)** — effects-only, no coeffects/
  comonads/containers/bialgebras. The field's *other* vocabulary for organizing Freyd
  categories. Orthogonal.
- **Breuvart–Long–Zamdzhiev, arXiv:2602.09780**: "centre" of a strong graded monad =
  maximal *commutative* sub-effect. Classifies graded monads by **commutativity**, not
  arity. Orthogonal (Workers-thread neighbour).
- **Vollmer–Paviotti–Orchard, "On the Category of Graded Monads" (CT2026, not yet arXiv)**:
  a general 2-categorical machine `Gmd(I,κ)=[BI^op,κ]_lax` making graded-monad/comonad
  distributive laws instances of one construction. **Load-bearing lead** — may subsume
  MacBeth's hand-computed `κ:GT⇒TG` per-instance. WATCH for arXiv; full-text pass owed.

Together: nobody organizes along arity/branching ⟹ that dimension is genuinely MacBeth's
(corroborates [[affine-classification-writer-exceptions]] T1-originality).

Links: [[effect-coeffect-arrows-first-strength]] · [[three-modes-of-composition]] ·
[[affine-classification-writer-exceptions]] · [[two-feeds-entwine-one-direction]]
