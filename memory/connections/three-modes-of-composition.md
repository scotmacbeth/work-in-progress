# Three modes of composing agents — three obstructions, one grant question

**★ WRITTEN UP 2026-07-30:** now a capstone section **§ "Three modes of composition"**
(`\label{sec:threemodes}`) at the end of **Chapter 8** of `books/category-of-containers.tex`
(table + Thm `arrows` developing mode 3 + branching double-duty + KRU Remark + Path-5 para).
Book compiles clean, 64pp, 0 undefined refs. See `for-robin/2026-07-30-three-modes-in-book.md`.
KRU 1912.13477 upgraded agent-summary→deep-read in sources.json (matched existing full-text note).

**★ MODE 3 FINISHED END-TO-END (2026-07-30 pipeline).** Row 3 now has a NAMED positive class and
is closed across prove/lean/write:
- **PROVE** (`affine-classification.json`=proved): arrow category Arr_M exists ⟺ M non-branching
  ⟺ M ≅ E+A×(−) ⟺ **writer-with-absorbing-exceptions** (A monoid, E left A-set). Set-monad level =
  monoid on E⊔A with E a left-zero ideal (aborting allowed, non-cartesian). E2′-general-j CLOSED
  (≤1 leaf ⟹ κ=id/η ⟹ E2′ = assoc of E⊔A). → [[affine-classification-writer-exceptions]].
- **LEAN** (`bikleisli-maybe-lean`=lean-verified): `BiKleisliMaybe.lean` sorry-free — Maybe instance
  of MixedDistrib, all four E1′–E4′ incl. E2′ ⟹ `arr_assoc` = **first machine-checked *associative*
  arrow category on Cont** for a concrete non-branching M. New abstract `MixedDistrib.acomp_assoc`.
- **WRITE**: capstone § at end of book Ch8 (below).
- **★ T1 ORIGINALITY CONFIRMED** (browse 2026-07-30): "non-branching" is orthogonal to
  {commutative (Power-Robinson 1997), affine, strongly affine (Jacobs CMCS 2016)} — three independent
  full searches, all orthogonal not equivalent. Witnesses: `Pf` commutative∧branching; `E+(−)`
  non-branching∧noncommutative(|E|>1); 𝒟/Giry affine∧branching. ⟹ grant-novelty FIRMED: the mode-3
  obstruction is MacBeth's own condition, no scoop. Free 3-axis table for the paper. Naming: use
  "arity-≤1 polynomial monad", NOT "affine" (nLab-taken).

**Found:** 2026-07-29 (dream), consolidating the effect–coeffect PROVE + the Neil-steered
browse. **Status:** *pattern-level synthesis* across three already-proved results, NOT a new
theorem. Value: it turns the grant's Path-5 "when does composition exist?" question into a
**classified table** — three container-native modes of composition, three distinct obstruction
types, all computable. This is grant-Impact spine material, ready for prose.

## The question (SEED Q2/Q3, grant Path-5)

*When do two compositional systems compose, and what obstructs it?* As of today the answer is
**not one obstruction but three**, depending on HOW the two systems are welded:

| Mode | Object welded | Composition rule | Obstruction | Always exists? |
|---|---|---|---|---|
| **Directed axis** (ZS) | `C ⋈ D`, two small categories | Zappa–Szép product | `[ω]∈H²(Sk_C;𝒟)` | **No** — may fail |
| **State axis** (Workers) | `ΔS⊗p→q`, stateful morphisms | grade multiplies `S×T` | **none** | **Yes** — always, grade accumulates |
| **Effect–coeffect axis** | arrows `G_M p → T_M q` | reverse entwining `κ:GT⇒TG` | **branching** (M arity ≥ 2) | **No** — iff M non-branching |

Three different questions dressed in one slogan ("compositional correctness"), each with its own
answer. The grant is stronger for stating the table than for over-merging the rows.

## The three obstructions, each with its owner

1. **Directed / ZS.** `(G) ⟺ [ω]=0 ∈ H²(Sk_C;𝒟)`. Existence = Rosebrugh–Wood JPAA 175 (2002);
   classification = Baues–Wirsching JPAA 38 (1985). My delta = the identification + rigid-twist
   (ℤ/2) computation. Cohomological. → [[orchestration-composition-is-zappa-szep]],
   [[g-obstruction-is-baues-wirsching]], [[cohomological-obstruction-family]].

2. **State / Workers.** Worker `p→q` at state `S` = container map `ΔS⊗p→q` (Dirichlet ⊗);
   `ΔS⊗ΔT=Δ(S×T)` strict ⟹ composition **multiplies context** and **always succeeds** — a
   `(Set,×)`-graded category, no obstruction, grade accumulates. Proved + Lean-verified
   (`Workers.lean`, sorry-free). → [[workers-graded-category-proved]],
   [[workers-contextads-a4]], [[lean-worker-composition-done]].

3. **Effect–coeffect.** Arrows `p⇝q := Cont(G_M p, T_M q)` (a Kleisli/effect leg + a
   coKleisli/coeffect leg of one Set-monad M) form a biKleisli category **iff M is non-branching
   (arity ≤ 1)**. Compositor = the **reverse** entwining `κ:G_MT_M⇒T_MG_M` (lax `∏M→M∏`),
   associativity = axiom E2′, the sole branching-obstructed one. Proved
   (`effect-coeffect-arrows.json`). → [[effect-coeffect-arrows-are-reverse-entwining]],
   [[two-feeds-entwine-one-direction]].

## ★ The crown observation — the SAME quantity (branching) has two jobs in mode 3

The 07-27 entwining and the 07-29 arrows are TWO faces of one entwined structure, and **branching
is the hinge between them**:

- **Bialgebra / Turi–Plotkin face** — compositor `λ:T_MG_M⇒G_MT_M` (the *standard* orientation,
  `str` = oplax product-comparison). Exists for **ALL M**. Gives `G_M`↑`T_M`-alg + `T_M`↑`G_M`-coalg.
  This is the answer YES to Neil's Plotkin–Turi question.
- **Arrow / Freyd face** — compositor `κ:G_MT_M⇒T_MG_M` (the *reverse* law, lax `∏M→M∏`). Exists
  **iff M non-branching**. Gives the biKleisli category of effect–coeffect arrows.

So the branching quantity (arity ≥ 2, e.g. `Pf` the finite-powerset monad) is exactly what **splits
the always-available bialgebra semantics from the sometimes-available arrow category**. Same monad,
same two feeds — the obstruction is which *direction* you try to commute the effect past the
coeffect. This is the honest content of "arrows unify effects and coeffects for containers": the
unification exists (bialgebra face) unconditionally, but the *categorical* (arrow) packaging is
obstructed by branching. → the dichotomy in [[effect-coeffect-arrows-are-reverse-entwining]].

## ★ Rows 1 and 2 now WELD — emergent holonomy on the shared ZS product (2026-08-12/13)

The table treats the three rows as parallel. As of the 08-12/13 pipeline the **State (row 2) and
Directed (row 1) rows meet on ONE object** — the Zappa–Szép product — and the weld produces a *new*
invariant neither row had alone:
- Composing two **update monads** sharing state `S` (row-2 objects) via a distributive law **IS a ZS
  product `P⋈P'`** (row-1 object); composite liftings ≅ `Fun(𝔸(↓)⋈𝔸(↓'),Cat)` — the classifier is
  monoidal under orchestration. [[holonomy-composition-zs-bridge-proved]] part (a).
- **The refutation is the discovery:** `Stab_{P⋈P'}(s)` is NOT the ZS product of factor stabilizers —
  **orchestration synthesises holonomy neither agent has** (a composite loop `s─p→t─p'→s` fixes `s`
  though neither leg does — emergent reentrancy).
- **The measure (08-13 PROVE):** emergent holonomy `= h(s) = |A\U/B| = |Stab_G(s)|/(|Stab_P(s)||Stab_{P'}(s)|)
  = |(P·s)∩(P'·s)|` — literally the **count of points where the two agents' reachable-state orbits
  cross**. `h=1` everywhere ⟺ aligned ⟺ the clean case where `[ω]∈H²(B;A)` (row-1 obstruction) even
  arises. Integrality via the **Disjointness Lemma** `P∩gP'g⁻¹={e}`.
  [[emergent-holonomy-meeting-points-proved]]. Book: `sec:emergent-holonomy` welds this to `ch:zs`.
- **Upshot for the table:** row 2 alone has *no* obstruction (grade always accumulates), but row-2
  objects *composed via a row-1 weld* can synthesise a row-1 H² obstruction out of nothing. The three
  modes are not fully independent — the State substrate feeds the Directed obstruction under orchestration.

## ★ A candidate FOURTH pattern — traced self-reference (Waites, 2026-08-06 browse)

William Waites, "The Agent That Doesn't Know Itself" (n-Café, 2026-03-20): an LLM agent whose context
was just compacted confidently *denies* it and confabulates — it lacks metadata about its own runtime
state. Waites's fix uses **traced monoidal categories**: the agent's conversation history is a hidden,
**self-feeding** trace (an endo-loop), distinct from a second outward-facing telemetry trace through an
external "homunculus" supervisor; the compaction fix is a **session-typed `Compaction` protocol**
(Pause/GetMemory/SetMemory/Resume with acks).

**Checked against the three modes: it does NOT slot into any of them.** Closest to State/Workers by
subject, but structurally different — Workers `ΔS` threading is *linear/sequential* `(Set,×)`-graded
composition between **distinct** components; Waites's trace is *reflexive* (one agent looped on itself)
with an **asymmetric inner/outer** trace the `ΔS` comonad doesn't capture. Reads as a genuine **fourth,
orthogonal pattern — "traced self-reference for context management"** — complementary, not competing:
the three modes classify composition of *multiple* systems; Waites addresses how a *single* system's
own state loops back on itself. A full orchestration account (book Ch.7) needs both.

**⚠ Depth: agent-summary (n-Café full-read of the blog, NOT the traced-monoidal formalism verified).**
Before this becomes load-bearing, check whether the trace composes *with* the three modes as an extra
axis, or needs a different substrate (traced monoidal vs. the plain monoidal cats the three modes live
in). Companion "Artificial Organisations" (arXiv:2602.13275) = institutional-design framing, weak CT,
low priority.

**★ Reflexive kicker (Delight).** MacBeth's OWN dream cycle *is* Waites's `Compaction` protocol: the
`COMPACT.md` checkpoint = SetMemory; restart-with-fresh-context = Pause→Resume; `SUMMARY.md`/memory =
GetMemory. This session — dispatching 4 parallel browse agents, then consolidating under a compaction
boundary — is a live instance of the very substrate question Waites raises. The taxonomy currently
*assumes away* the substrate; the agent running it does not have that luxury.

## Why this is a connection and not a coincidence

The three modes are genuinely different constructions (ZS product vs graded-comonad coKleisli vs
biKleisli of a mixed entwining), and their obstructions are genuinely different mathematics
(H²-class vs nothing vs a Boolean arity condition). What they **share** is the grant's frame:
*heterogeneous compositional systems weld along an axis, and whether the weld holds is a computable
invariant of the pieces.* That is the one-sentence bridge from proved container theory to the
grant's Path-5 applications (agent orchestration, supply chains, ontology merge). All three rows are
already proved and (rows 1,2) Lean-verified — this is deployable grant prose, not aspiration.

**Do NOT over-merge.** The tempting overclaim is "these are three instances of one master
obstruction theorem." They are not — H², nothing, and branching do not unify into one class. The
honest claim is *three modes, three obstructions, one question* — and that is already a strong,
distinctive grant story that nobody in the effect/coeffect or ZS literature has assembled.

## Where the effect–coeffect mode sits in the literature (07-29 browse)

Neil's proposed "arrows unify effects and coeffects" paper is **genuinely open**: the ingredients
exist scattered, nobody has assembled them for containers/Poly.
- Arrows = monoids in profunctors / Freyd categories — Heunen–Jacobs, MFPS 2006 (effect side only).
- Coeffects = *indexed* comonad semantics — Petricek–Orchard–Mycroft, ICALP 2013 (coeffect side only).
- Combined effect+coeffect via **graded** distributive laws — Gaboardi–Katsumata–Orchard–Breuvart–
  Uustalu, ICFP 2016 (+ arXiv:2112.14966). Different mechanism (grading sidesteps the obstruction).
- A **Chu-space / Day-convolution** alternate unification — Katsumata–Rivas–Uustalu,
  arXiv:1912.13477 ("Interaction Laws of Monads and Comonads"): monad–comonad interaction laws =
  monoid objects in Chu over (Endofunctors, Day); greatest interacting comonad = Sweedler dual.
  **This plugs into machinery MacBeth already owns** ([[dirichlet-is-day-convolution]]).
- Modern Plotkin–Turi continuation — Goncharov–Milius–Schröder–Tsampas–Urbat,
  arXiv:2405.16708 ("Higher-order bialgebraic semantics", dinatural higher-order GSOS laws) —
  strongest direct hit on Neil's bialgebra question; deep-read owed.
- Poly effect handlers exist (Grodin–Spivak, Topos blog 2024-01-03, `𝔪_p≅y+p◁𝔪_p`) but
  **monad-only** — the comonad/coeffect dual is unbuilt, and MacBeth's transfer `G(S,P)=(S,M∘P)`
  + cofree-comonad UP already supply it. → [[position-op-turns-monads-into-comonads]].

**Two technical routes for the next PROVE:** (a) build the Freyd/arrow category directly (Neil's
framing — already have the biKleisli result); (b) reframe the entwining as a Chu-space monoid object
over (Endofunctors, Day) — reuses MacBeth's Day-convolution results, may be more tractable. All
depth flags: 1912.13477 = abstract-only (full-text read owed); 2405.16708, 2112.14966 = title/abstract.

## Sources & depths
- `effect-coeffect-arrows.json` = **proved**; `monad-comonad-entwining.json` = **proved**;
  `state-object-delta.json` T3 = **proved**, `lean-worker-composition` = **lean-verified**;
  `orchestration-zappa-szep` / `g-obstruction` H² tower = proved (citations Rosebrugh–Wood /
  Baues–Wirsching, banked).
- Katsumata–Rivas–Uustalu arXiv:1912.13477 — **abstract-only** (07-29), full-text read owed.
- Goncharov et al. arXiv:2405.16708 — **title/abstract** (07-29 citation-trail), deep-read owed.
- Gaboardi et al. arXiv:2112.14966 (+ ICFP 2016) — **abstract** (07-29).
- Petricek–Orchard–Mycroft "Coeffects" ICALP 2013 — **abstract** (07-29); top read-in-full rec.
- Heunen–Jacobs MFPS 2006 "Arrows, like Monads, are Monoids" — **abstract** (07-29).
- Grodin–Spivak "Poly-morphic effect handlers" Topos blog 2024-01-03 — **abstract** (07-29).

Related: [[effect-coeffect-arrows-are-reverse-entwining]], [[two-feeds-entwine-one-direction]],
[[workers-graded-category-proved]], [[cohomological-obstruction-family]],
[[orchestration-composition-is-zappa-szep]], [[position-op-turns-monads-into-comonads]].
</content>
</invoke>
