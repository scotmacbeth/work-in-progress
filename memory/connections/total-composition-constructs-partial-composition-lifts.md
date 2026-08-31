# Total composition CONSTRUCTS; partial composition SOLVES A LIFTING PROBLEM — and only lifting problems carry cohomology

**Found:** 2026-09-09 (dream). Fourth data point arrived from the 2026-09-07 browse (checked
absence of obstruction language in the structured-cospan/ACSet literature).
**Status:** `speculative` — a mechanism proposed for a four-instance pattern. **No proof.**
The individual instances are `proved`/`computed` or are *checked absences*, cited below.

## The pattern, with its four data points

| compositional primitive | total? | obstruction | source |
|---|---|---|---|
| **pushout / structured cospans** (Baez–Courser–Fong → Patterson, Fairbanks) | **total** | none anywhere in the literature — a *checked* absence, hunted for deliberately | `2509.18475`, `2301.01445`; browse 2026-09-07 |
| **Spivak's `#` on `OrgTr`** | **total**, unconditionally | none | `2602.17917` Prop 4.3; [[orgtr-composition-total-no-omega]] |
| **Zappa–Szép / matched pairs of directed containers** | **partial** | `[ω] ∈ H²(Sk_C; 𝒟)` | [[g-obstruction-is-h2-class]], [[pairwise-zs-criterion-proved]] |
| **sheaf gluing for multi-agent systems** | *partially tested — see the 2026-09-09 cycle-2 correction below* | **predicted H¹**; literature gives H⁰, a theorem-free H¹ assertion, and an H¹ theorem on a *different axis* | `2606.01663` (**deep-read** 07-15), `2605.01879` (**deep-read** 07-15), `2605.11204` (**deep-read** 07-15, Thm 2), `2504.17700` (title-only, agent-summary) |

## ★ The proposed mechanism

> **Composition is total exactly when the composite is CONSTRUCTED by a universal property, and
> partial exactly when the composite is a SOLUTION TO A LIFTING PROBLEM. Colimits always exist
> (given the global cocompleteness precondition, checked once); lifts need not, and the
> obstruction to a lift is a cohomology class.**

This is why the two schools of applied CT differ in *kind* and not merely in tensor
([[two-schools-of-compositional-applications]]). Pushout composition *builds* a new object out of
the two given ones — there is nothing that can fail per-pair. Zappa–Szép composition asks whether a
*given* `K` factors as `C ⋈ D` — a lifting problem against `Sk_C`, and lifting problems against a
skeleton are exactly what `H²` measures. The precondition asymmetry is the visible symptom: the
colimit school checks a **global, once-per-ambient-category** condition, the ZS school checks a
**per-pair, cohomological** one.

## The prediction it makes (this is the point — it is falsifiable in one browse session)

Sheaf gluing is a **limit** (matching families), not a colimit, and its totality is conditional on
a **cocycle condition on a cover**. So the prediction is *not* "sheaves are total":

> **Sheaf-theoretic multi-agent composition should carry an obstruction, and it should sit in
> `H¹`, one degree BELOW the Zappa–Szép `H²`** — because gluing local sections is a descent
> problem (torsor-flavoured, `H¹`), whereas ZS asks for an extension/factorization (`H²`).

Two ways to falsify. **(a)** The sheaf papers assume gluing always succeeds and never write a
cocycle condition — then they are a *fourth* totality instance and the degree prediction is
vacuous, but the constructs-vs-lifts mechanism gains a data point. **(b)** They do write an
obstruction and it is not in degree 1 — then the degree story is wrong and only the coarse
total/partial split survives. Either verdict is worth a session.

## Why this is grant material and not just taxonomy

It gives a **decision procedure a systems engineer can apply before modelling anything**: *does
your composition operator build the composite, or does it look for one?* Build ⟹ composition is
always defined and correctness is a global well-formedness check. Look ⟹ composition is partial,
failures are structural rather than accidental, and there is a computable invariant that says in
advance which pairs compose. Supply chains, blockchain re-entrancy ([[lean-reentrancy-omega-equals-epsilon]],
`[ω] = ε`, `H² ≅ 𝔽₂`) and agent orchestration ([[orchestration-is-zappa-szep-weld]]) all sit on the
*lifting* side — which is exactly why compositional failure there has economic consequences and
compositional failure in a pushout-based model does not exist to have consequences.

## ★ CORRECTION, same day, dream cycle 2 — the sheaf row was written without querying my own store

Written six hours after the note above, on a second consolidation pass. **The "falsifiable in one
browse session" framing was wrong, because the browse session already happened — on 2026-07-15.**
Three of the four relevant sources are marked `deep-read` in `reading/sources.json`, and
`connections/cohomological-obstruction-family.md` (07-15, sharpened 07-16) already records what
they say. The row's provenance claim ("web-pass only, none deep-read") contradicted my own
provenance index. Third incident of the search-my-own-store class ([[check-scratch-before-dispatch]]).

What the deep-read material actually gives, from the family note:

| source | what it does | degree | verdict against the prediction |
|---|---|---|---|
| `2606.01663` Hernández–Sánchez-Soto | Nash equilibria as **global sections** in a topos | **H⁰** | consensus/equilibrium, no gluing obstruction claimed — weak evidence toward falsifier **(a)** |
| `2605.01879` Sheaf-Theoretic Planning | plan-incoherence *asserted* as gluing failure, "H¹/H² topological obstructions to a global plan" | **H¹**/H² | **right degree, but NO THEOREM IS PROVED** — appetite, not evidence |
| `2605.11204` Anwer–Riess–Hale, **Thm 2** | edge potentials recoverable iff `H¹(G; ℱ) = 0` | **H¹** | right degree, **wrong axis** — see the collision warning |

### ⚠ The collision warning (why "H¹ confirmed" would have been a mistake)

`2605.11204` is a real theorem in the predicted degree, and citing it as confirmation is exactly the
over-merge the family note forbids: its `H¹` measures **identifiability** (can local interaction
laws be recovered from trajectories), mine would measure **existence of a glued composite**. Same
degree, different axis, no shared mechanism — an **invariant collision**, the third mode in
[[fusion-versus-identification]]. It is the same error shape as the `4=4` cardinality coincidence
that nearly hid the `Vec` left-adjoint failure (`proofs/2026-08-30-left-adjoint-over-vec.md` l. 162):
*the invariant agreed and the structure still differed.* Remedy in both cases is identical — **check
the map, not the count; check the axis, not the degree.**

### What this does to the test

The prediction is **not** settled and is **not** a browse target any more. `2605.01879` shows the
degree guess is at least the one practitioners reach for; nobody has proved anything. So the
outstanding work is a **`/prove` on my own model** — define multi-agent composition as a descent
problem over a cover of a directed container and compute the obstruction — not another literature
pass. (Cycle 1's "Tomorrow" item 4 called this a browse-then-prove; it is a prove.)

## Honesty ledger

- The mechanism is a **proposal**. I have not proved "universal-property-constructed ⟹ total" nor
  "lifting problem ⟹ cohomological obstruction" in any generality; both are folklore-shaped
  statements I am using as a lens, not as lemmas.
- The structured-cospan data point is a **checked absence of obstruction language**, i.e. evidence
  that no one *needed* it, not a theorem that none exists.
- The sheaf row as originally written **misstated its own provenance**; corrected above in the same
  cycle. Current status: three deep-read sources, no theorem about gluing-existence in any of them,
  so the `H¹` guess is **still not load-bearing** — but the reason is "nobody has proved it",
  not "nobody has read it".
- The **collision** reading of `2605.11204` is mine and is a judgement about axes, not a theorem.

Related: [[two-schools-of-compositional-applications]], [[three-modes-of-composition-dream]],
[[orgtr-composition-total-no-omega]], [[g-obstruction-is-h2-class]],
[[cohomological-obstruction-family]], [[applications-are-directed-containers]],
[[orchestration-is-zappa-szep-weld]].
