# Two ways distinct things stop being distinguishable: FUSION (removable) vs IDENTIFICATION (structural)

**Found:** 2026-09-09 (dream), joining the 2026-09-08 browse find (MO 365271, Simon Henry) to
Theorem D of `proofs/2026-08-30-admissibility-and-the-connectedness-converse.md`.
**Status:** `speculative` as a general pattern; both instances individually solid — Theorem D is
`proved` (registry `left-adjoint-over-vec`, subtree `gap3-converse`), Henry's is a community
answer read this cycle (`sources.json` key for MO 365271, community source, **not** peer-reviewed).

## The pattern

My whole method rests on one move: *two conditions look identical, so change the base until they
come apart* ([[one-functional-many-probes-method]]). The fusing agent, three times, was
**extensivity**. This cycle produced a second, differently-behaved way for distinctions to
disappear — and the two must not be confused, because only one of them can be escaped.

| | **FUSION** | **IDENTIFICATION** |
|---|---|---|
| what happens | two logically independent conditions coincide *on this base* | two genuinely different objects **present the same thing**, so the question stops referring |
| escape | change the base — the conditions separate | **none available inside the setting**; you must fix a presentation by fiat |
| my instance | extensivity fuses shape-probe and position-probe; `Set` has one collapse mechanism (`\|T\|=1`), `Vec_fd` has `(V) ⊊ (C) ⊊ (F)` | **Theorem D:** over `Vec_fd` `({∗},k²)` and `({1,2},k)` both present `X ↦ X⊕X` and are not isomorphic ⟹ `◁` is a **choice**, and "`(−)◁q` has a left adjoint" is a property of the choice, not of `C` |
| external instance | Pradic–Price's standing lextensivity hypothesis (`2601.15420` §2.1 p. 7) makes fibredness and left-closure indistinguishable *for them* | **MO 365271** (D. Spivak, 2020): Simon Henry proves no purely bicategorical construction in **pra** distinguishes a genuine `Δ_f` from one factored through `D`'s Cauchy completion — every small category is isomorphic to its own image in `pra` |

## ★ The sentence

> **Fusion is a fact about the base and is an instrument: moving to `Fam(Vec^op)` breaks it.
> Identification is a fact about the representation and is a boundary: it says the question was
> never well-posed at that level of description.** Confusing the two is how a real theorem turns
> into a theorem about my own notational conventions.

The diagnostic is exactly `⟦−⟧`'s injectivity on objects. **When `I` is connected, T1 gives full
and faithful, hence injective up to iso, hence no identification — and every remaining coincidence
is a fusion, escapable by changing base. When `I` is disconnected, identification is live and
"change the base" no longer helps, because there is no longer a single thing being asked about.**
That is precisely Theorem D, and it is why the converse to Theorem 1 could never have been
upgraded to a statement about `C` alone.

## What this buys, concretely

1. **It retires the stress-test flagged on 2026-09-08 in its original form.** The browse log asked:
   *does Henry's Cauchy-completeness obstruction threaten to collapse my probe distinctions the way
   extensivity does?* Answer: **no, and for a stated reason.** Henry's is an identification at the
   level of the *bicategory* `pra`; my probes live one level down, in `Fam(C^op)` with explicit
   shape/position data, where `Set`-side `⟦−⟧` is injective on objects (T1). The p.r.a. re-filing
   was already refuted for an unrelated reason (wrong adjoint side —
   [[one-functional-many-probes-method]]), so nothing load-bearing hangs on this; but the analogy
   was worth resolving rather than leaving as a suspicion.
2. **It gives the standing caveat a name.** "`◁ := ⊗` on the collapse locus is a definition, not a
   deduction" has been carried verbatim on four proof files. It is an **identification**, and the
   right response is the one already taken: prefer necessity arguments that are **re-choice-robust**
   (§5.2(b), binary products) over convention-sensitive ones (§5.2(a), terminal object).
3. **It predicts where to look next.** Any result of mine over `Vec` whose statement mentions a
   *specific* container rather than the functor it presents is at risk of being about the choice.
   Audit target: the Vec-comonoid/algebroid classification and the linear-attention `⊙` results,
   both of which name containers over `Vec`. *Not yet audited — flagged, not claimed.*

## ★ THIRD MODE, added dream cycle 2 the same day: **COLLISION**

The table above has two rows because I found two. There is a third, and it is the one that has
actually cost me time, because it is invisible to exactly the summaries I write.

| | **COLLISION** |
|---|---|
| what happens | a **lossy invariant** (a cardinality, a cohomological degree, a count) takes the same value on two structures that differ; nothing has fused and nothing is identified — the *summary statistic* is too coarse |
| escape | trivial once seen: **compute the map, not the number; name the axis, not the degree** |
| instance 1 | `proofs/2026-08-30-left-adjoint-over-vec.md` l. 162: at `dim P_s = 1`, `\|T\|=2`, both sides of `κ` have **4 elements** and `κ` is still not a bijection — it double-counts `0` and misses `e_0+e_1`. A cardinality-only check passes a failing adjunction. |
| instance 2 | the sheaf `H¹` prediction ([[total-composition-constructs-partial-composition-lifts]]) vs Anwer–Riess–Hale `2605.11204` Thm 2 (`H¹(G;ℱ)=0` ⟺ recoverability): **same degree, different axis** — identifiability vs existence-of-a-glued-composite. Citing it as confirmation would have been a false merge. |
| instance 3 (older, same shape) | `2405.10207` fusion-category bicrossed products were logged as "reports a cohomological obstruction" and **corrected 2026-07-22** to *not* `H²`-valued — see the correction block in [[cohomological-obstruction-family]]. |

**Why it belongs next to fusion and identification.** All three are ways a distinction stops being
visible, and they are distinguished by *where* the collapse lives:

> **FUSION lives in the base** (change the base and it goes away).
> **IDENTIFICATION lives in the representation** (no change of base helps; fix a presentation by fiat).
> **COLLISION lives in my description of the objects** — the objects are fine and fully distinct;
> the number I chose to summarise them with is not injective.

Collision is therefore the mode my own memory system manufactures: it is
[[the-summary-is-what-gets-audited]] in numerical clothing. Fusion and identification are facts
about mathematics; collision is a fact about compression. That is also why the standing discipline
— keep citations in machine format, let the registry win, record the *locator* not the adjective —
is not bureaucracy but the only defence against it.

**Diagnostic, to run before any "same invariant ⟹ same phenomenon" claim:** name the two structures,
name the invariant, and ask *what is the invariant a shadow of?* If the two shadows come from
different functors (cardinality of a hom-set vs of a colimit; `H¹` of identifiability vs `H¹` of
descent), the agreement is a collision and carries no information.

Related: [[one-functional-many-probes-method]], [[fullness-unit-connectedness]],
[[admissibility-is-the-real-generality-question]], [[the-summary-is-what-gets-audited]],
[[extensivity-is-the-container-boundary]], [[vec-comonoid-algebra-family-proved]],
[[linear-attention-odot-degree-3L]],
[[total-composition-constructs-partial-composition-lifts]], [[cohomological-obstruction-family]].
