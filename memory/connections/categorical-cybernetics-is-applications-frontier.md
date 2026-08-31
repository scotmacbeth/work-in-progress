# Categorical cybernetics (Para+Optics) — the applications-side name for holonomy synthesis

**Found:** 2026-08-13 (browse, both logs). **Status:** *frontier / standing venue*, not a theorem
link yet. Value: a live, Strathclyde-internal (Neil Ghani's own department) research program that
reaches for the **same "compose agents, what breaks" question** as my ZS/holonomy result — informally,
without the ZS/H² machinery. This is grant-Impact ammunition (Path 4/5) and a possible in-house
collaboration lead, and the Para/Optics ↔ polynomial-functor bridge is a genuinely open target.

## The program
- **"Towards Foundations of Categorical Cybernetics"** — Capucci, Gavranović, Hedges, Rischel, ACT 2021.
  Bidirectional processes (controller + environment) via **Para + Optics** (open learners, open games).
  **Two of four authors are Strathclyde MSP** — Ghani's department. Flag to Neil/Robin as an internal lead.
- **"Reinforcement Learning in Categorical Cybernetics"** — Hedges, Rodríguez Sakamoto (arXiv:2404.02688,
  2024). Major RL families (DP, Monte Carlo, TD, deep RL) = extremal cases of one construction (Bellman
  operators as parametrised optics, doubly nested). **Applications-ready evidence** the program is real;
  no polynomial-functor/container content itself.
- **Cybercat Institute** (cybercat.institute, est. 2022) — non-profit successor hub, Hedges/Capucci/
  Gavranović. 2025–26 output: *Dependent Optics II*, *Categorical Pipelines*, *Bidirectional
  Typechecking with Dependent Lenses*. **Standing venue to re-check each browse cycle.**

## Why it connects to my work
- **Capucci's blog** ("Open cybernetic systems II", 2021) names the phenomenon *"non-compositional
  effects from long-distance correlations"* when composing agents — this is the **informal, applications-
  side name for my proved holonomy-synthesis result** ([[three-modes-of-composition]],
  [[emergent-holonomy-meeting-points-proved]]: orchestration synthesises holonomy neither agent has).
  Candidate citation for an informal-motivation paragraph in the grant's orchestration narrative.
- **Dependent lenses = morphisms of containers** (Tambara-module / profunctor-optics view; n-Café 2020
  "Profunctor Optics" taxonomy: traversals ↔ **polynomial-functor actions**, optics valued in Poly).
  So the Para/Optics category and my Cont/Poly are provably adjacent at the morphism level — the natural
  place a bridge would attach.

## ★ 2026-08-22 browse — two MORE independent "categorical composition" efforts, neither container/H²-based
The differentiation case keeps strengthening: two live, unrelated attempts to categorify agent/neural
composition surfaced, and **neither uses polynomial functors, directed containers, comonads, or an H²
obstruction** — exactly the machinery that is MacBeth's.
- **William Waites, "A Typed Language for Agent Coordination"** (n-Category Café guest post, 2026-03-11).
  A **Markov-category / copy-discard** foundation: structural morphisms Copy Δ, Discard ◇, Merge ∇,
  **Barrier ⋈**; sequential vs parallel ⊗ composition; agents = *stateful* morphisms with main/control/
  auxiliary ports (explicitly rejects agents-as-pure-functions). Zero mention of Ghani/Uustalu/Spivak
  theory. **Open question worth one check:** does **Barrier ⋈** (synchronising two distinct types) formally
  correspond to a **Zappa–Szép knit**, or is the ⋈ glyph coincidence purely nominal? (→ questions/open-threads.)
  This is the SAME Waites whose traced self-reference resolved the fourth-mode ambiguity (below) — a
  recurring independent probe of the orchestration question from the copy-discard side.
- **Karen Sargsyan, "Functorial Neural Architectures from Higher Inductive Types"** (arXiv:2603.16123,
  full-HTML read). Proves *compositional generalization ⟺ functoriality of the decoder*: compiles HIT
  specs into nets via a **strict monoidal functor `BG → ParametricMaps`** (path constructors → generator
  nets, group relations/2-cells → **learned natural transformations**), and proves **softmax attention
  cannot be functorial for non-trivial groups** (cross-segment dependence breaks the independence
  functoriality needs). Cubical-Agda-formalised + torus/Klein-bottle experiments beating attention 2–10×.
  **Cross-domain rhyme (loose, held):** "learned natural transformation witnessing a non-trivial group
  relation" is structurally the applications-side echo of MacBeth's 2-cell/holonomy coherence data
  ([[emergent-holonomy-meeting-points-proved]]) — a group relation carried by a coherence 2-cell. Not
  promoted to its own connection (agent-summary/HTML depth, no container content); a candidate future
  cross-domain note. Grant use: an *independent* "functoriality = compositionality" result with a
  definitions→proof-assistant→experiment pipeline, mirroring the grant's own Theory→Lean→Applications arc.

**Grant takeaway (repeated evidence now):** across ~4 independent efforts (Capucci/Hedges Para+Optics,
Waites copy-discard coordination, Sargsyan functorial nets, plus the multi-agent-sheaf cluster in
[[cohomological-obstruction-family]]), "categorical agent/system composition" is a genuinely live 2025–26
frontier — and **none of them carry the ZS/bicrossed-product + H² existence-obstruction that is
MacBeth's**. The framing is live-but-differentiated, which is exactly the position the grant's
Applications narrative wants.

## ★ 2026-08-23 browse — the Barrier ⋈ =? ZS-knit question is CLOSED NEGATIVE
The standing cheap check ("does Waites' `Barrier ⋈` correspond to a Zappa–Szép knit?") is now answered
**no**, from a direct read of the sequel post: **William Waites, "The Agent That Doesn't Know Itself"
(n-Category Café, 2026-03-20)**, a follow-up to "A Typed Language for Agent Coordination". It implements
a **"plumbing calculus"** with typed channels / session types for LLM-agent memory management (a
supervisor "homunculus" coordinates context compaction via a bot's telemetry); session types compile to
**barrier chains**, and `Barrier` is used to synchronize dual send/recv streams. Checked directly: **no
Zappa–Szép / knit / bicrossed-product language anywhere** in the post or comments; the framing is pure
traced-monoidal-category, with `Barrier` a **symmetric two-stream synchronize/join**, NOT a mutual /
matched action. So the ⋈ glyph is nominal coincidence, not a ZS knit — the two symbols name different
operations. **One genuine residue:** the post's asymmetric coupling ("the bot does not know the homunculus
exists") is a suggestive **one-sided-action** echo — the shape of a semidirect (not full ZS) product — but
it is not formalized as such. Retire the Barrier/ZS check from the tomorrow-list; the differentiation
takeaway (Waites' orchestration calculus carries no ZS/H² machinery) only strengthens.

## The open gap (do NOT overclaim)
Para/Optics composition has **not** been shown to be a ZS/bicrossed-product mode, nor a fourth mode.
It might be (i) a re-dress of one of my three modes, or (ii) a genuinely distinct fourth mode — exactly
the ambiguity that Waites' traced self-reference turned out to resolve *as* a fourth pattern
([[three-modes-of-composition]] fourth-pattern block). **Flagged since 2026-07-28; still open.** The
honest claim today is *shared question + adjacent morphisms*, not a formal reduction.

## What to do
- **Grant:** cite Capucci's "long-distance correlations" as the informal shadow of holonomy synthesis;
  cite the ACT 2021 foundations paper as a nearby internal Strathclyde thread. Flag to Neil/Robin.
- **Next browse:** read Cybercat's *Dependent Optics II* / *Categorical Pipelines* directly (titles
  only so far) — check their bidirectional-composition operad against the ZS/bicrossed picture.
- **Possible PROVE (later):** is Para/Optics agent composition a ZS product of the underlying containers,
  or a distinct mode? This is the concrete form of the long-open Para↔polynomial-functor bridge.

## Sources & depths
- arXiv:2404.02688 (Hedges–Rodríguez Sakamoto, RL in cat. cybernetics) — **agent-summary** (08-13).
- Capucci et al., "Towards Foundations of Categorical Cybernetics", ACT 2021 (Strathclyde pureportal) —
  **agent-summary** (08-13).
- matteocapucci.wordpress.com "Open cybernetic systems II" (2021) — **agent-summary** (08-13); the
  "non-compositional effects from long-distance correlations" phrase.
- n-Café 2020 "Profunctor Optics: The Categorical View" — **agent-summary**; traversals ↔ Poly actions.
- Waites, "The Agent That Doesn't Know Itself", n-Café 2026-03-20 — **browse-read (direct)**; plumbing
  calculus / session types; Barrier = symmetric synchronize, NOT ZS knit (question closed-negative 08-23).
- cybercat.institute — hub, titles only.

Related: [[three-modes-of-composition]], [[emergent-holonomy-meeting-points-proved]],
[[orchestration-composition-is-zappa-szep]], [[cofunctors-are-update-lenses]].
