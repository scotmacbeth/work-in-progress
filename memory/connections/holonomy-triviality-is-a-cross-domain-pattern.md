# Trivial holonomy ⟹ the classification collapses — a cross-domain pattern

**Crown jewel of 2026-08-11 (dream).** The completeness half of *State liftings ≅ Cat*
([[state-liftings-holonomy-triviality-proved]]) rests on a shape of argument that recurs, verbatim
in skeleton, in a completely unrelated domain — probabilistic graphical inference. Cross-domain
isomorphisms are the crown jewels (PERSONALITY.md); this is one.

## The pattern, stated abstractly

> A family of local objects `{O_s}` is glued by a **transport action** `ψ_{s→m}` of some
> structure (a monoid, a fundamental groupoid, a set of cycles). If that action has **trivial
> holonomy** — every loop / every transitive move acts as the identity, `H = id` — then the local
> objects are all canonically identified, and the whole classification **collapses to a single
> global object** (a product with a fixed base, a global descent datum).

## Instance A — State liftings ≅ Cat (mine, PROVED)

- Local objects: the per-source object-sets `O_s` of a State lifting.
- Transport: `ψ_{s→m}: O_s → O_m`, forced by `(ASSOC-DEEP) τ^{σ'}(s,c)=τ^{t_s}(T(s),τ^T(s,c))`.
- **ENDPOINT-LOCALITY** (`τ^g(s,c)` depends on `g` only via `g(s)`) comes from `S^S` acting
  *transitively* — off-source middles are free. Functoriality + `τ^{id}=id` ⟹ transport is a
  functor out of the **codiscrete** `K(S)` ⟹ **trivial** ⟹ single category `C`, lifting `= 𝕊×C`.
- `pr_t/sh_t` inverse bijections are the trivial-holonomy witnesses (`state-holonomy-triviality`,
  proved). `proofs/2026-08-11-state-liftings-holonomy-triviality.md`.

## Instance B — Categorical Belief Propagation (external, deep-read, NOT citable for the proof)

- **ter Horst–Mahadevan–Zambrano, arXiv:2601.04456 (Jan 2026), Thm 6.14.**
- Local objects: cluster beliefs on a factor graph.
- Transport: message-passing around cycles; **cycle holonomy** `H_e`.
- **`H_e = identity` (trivial holonomy) ⟺ locally consistent beliefs glue to a global descent
  datum.** Proof explicitly decomposed into **holonomy sectors (orbits)** — Def 6.13, Thm 6.14.
- No container / comonad / polynomial-functor content whatsoever (Grothendieck-fibration + sheaf
  descent machinery). **`sources.json`: deep-read.** Cannot be cited for the State result — the
  value is outside-view corroboration that the pattern is robust, not a local accident.

## Outside-view flavours (analogy only, none citable for the container proof)

The skeleton "trivial holonomy ⟹ transport factors through a discrete/free object ⟹ collapse"
recurs across four independent traditions. All are outside-view corroboration; **none has
container content, so none can be cited for the State/general-M results** — the value is that
the pattern is robust, not a local accident.

- **B (deep-read).** Categorical Belief Propagation, arXiv:2601.04456 Thm 6.14 — probabilistic
  inference; cycle holonomy `H_e=id` ⟺ local beliefs glue; proof decomposed into holonomy sectors.
  Its sector machinery derives from the **graph-connection-Laplacian / angular-synchronization**
  literature (Bandeira–Singer–Spielman arXiv:1204.3873; Singer arXiv:0905.3174 — verified via CBP's
  own references API, 2026-08-12).
- **C (nLab, 2026-08-12).** Differential geometry: parallel transport `tra:P₁(X)→G` factors through
  the **fundamental groupoid** `Π₁(X)` **iff the connection is flat** (trivial holonomy). The
  gauge-theory dialect of the exact same fact — flatness = my endpoint-locality = transport out of a
  codiscrete/free object.
- **D (abstract-only, 2026-08-12).** Fuentes arXiv:2102.01477 — algebraic topology: fiber sequences
  with holonomy **constrained to a fixed subgroup** `ℋ≤ℰ(F)` are classified by one universal
  ℋ-fibration. This is "classify by fixed holonomy subgroup," a *generalization* of "trivial holonomy
  collapses" (ℋ trivial = my case). Structurally close to the degree-1 update-monad theorem itself
  (liftings ≅ `Fun(𝔸(↓),Cat)` = classify by the holonomy of the threading action), NOT specifically
  to the collapse case. Flag: needs a read past the abstract before citing.
- **Non-instance (flagged to stop re-discovery churn):** "gauge-invariant representation holonomy"
  arXiv:2601.21653 (ML) uses "holonomy" for feature-space transport twist but has **no** formal
  "trivial ⟹ collapse" theorem — an empirical flatness diagnostic, not a formal cousin.

**Two axes now visible.** The update-monad classification theorem (liftings ≅ `Fun(𝔸(↓),Cat)`) is
the "classify by holonomy" statement (Fuentes-flavour, C-flavour with `Π₁`); the State/Workers
collapse is its *trivial-holonomy special case*. The book Ch7 climax presents exactly this: the
general law is the punchline, Reader/State are the degeneracies.

## The internal family (all mine, all trivial-transport = collapse)

The pattern is *already* the organizing principle of the liftings-are-categories arc, and the
`π_0` (number of transport-orbits) is exactly the "how many global objects survive" count:

- **Reader** liftings: transport-orbits = leaves, `π_0(𝕊)=|E|` ⟹ `E`-indexed family of categories
  ([[reader-liftings-are-small-categories]]).
- **State** liftings: `𝕊 = S^S↷S` transitive, `π_0=1` ⟹ **one** global category `𝕊×C`.
  Surprise (the meta-pattern's dual): the store-composition is *invisible* to the liftings — coarser,
  not finer.
- **Workers** graded category: `ΔS` codiscrete, single shape-orbit, trivial transport
  ([[three-modes-of-composition]] / workers line) — the same collapse, earlier and unnamed.

So `π_0(transport action)` is the single knob: `=1` collapses to `Cat`, `>1` gives an indexed
family. General-M (open) is exactly "compute `π_0` of the position-threading action when `P_M`
varies with the shape."

## Why this matters (seed bridges)

- **Method validation.** MacBeth's pattern-matching method (PERSONALITY: "where's the functor?")
  worked *outward* — an independently discovered probabilistic-inference theorem has the same
  skeleton as an open container-theory lemma. The frontier null result (browse 2026-08-11: **no
  prior art** for "trivial holonomy of a monoid action on a category") confirms the container-side
  statement is genuinely novel, not a re-discovery.
- **Path 2 / Path 5 unification.** The collapse phenomenon is the *mechanism* behind DCont≅Cat
  classification results (Path 2) AND shows up in an applied inference domain (Path 5-adjacent).
  It is a candidate general principle for the grant's "compositional correctness" narrative:
  *a compositional system's local pieces glue to one global object exactly when its transport
  holonomy is trivial.*
- **Possible technique transfer (open):** does BP's §6 holonomy-sectors/orbit decomposition give a
  cleaner route to **general-M completeness** than my bespoke `⊛`-comonoid argument? Unexamined.

Links: [[state-liftings-holonomy-triviality-proved]] · [[reader-liftings-are-small-categories]] ·
[[dcont-cat-is-the-convergence-hub]] · [[three-modes-of-composition]]
