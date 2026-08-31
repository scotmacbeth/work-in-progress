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

---

## ★ 2026-08-31 — A FOURTH COLLISION, AND IT IS A NEW SPECIES: THE SHARED SYMBOL

The three collisions on record were **numerical**: the `4 = 4` cardinality that nearly hid the `Vec`
left-adjoint failure, the `H¹` degree shared by gluing-existence and identifiability, and the 07-22
`2405.10207` correction. Today's is not a number. It is a **notation**.

**Dorta–Jarvis–Niu's `◁` is not my `◁`.** Under `ΣΠC = Fam((ΠC)^op)` the positions agree and the
direction *indexing* agrees; the direction **object** differs by an outer weight:

    mine   ∏_{a∈A_i} ∏_{b∈B_{ja}}  v_{ja,b}
    DJN    ∏_{a∈A_i} ∏_{b∈B_{ja}} (u_{i,a} · v_{ja,b})

They agree **exactly at `C = 1`**, where `y·y = y` annihilates the factor — and `C = 1` is the case
everyone checks, because it is the case that reproduces `Poly`. Non-presentational on three grounds:
my `⊗` *does* match theirs under the same identification (so the base identification is sound and only
`◁` breaks); their Thm 4.3 proof requires `µ_{b,c}: |cb| → |b|·|c|`, which **is** the weight; and the
comonoid outputs differ (families of k-algebras vs all enriched categories).

**Why this species is worse than the numerical one.** A cardinality collision at least requires you
to *compute something* before it can deceive you — and the remedy (*build the map, don't count*)
fires at the moment of computation. A symbol collision deceives you **before any computation at
all**. It is inherited silently the moment you adopt someone's notation, it survives every
consistency check inside each framework separately, and it is *invisible in the place it does damage*
— the compressed summary, where "DJN build `⊗` and `◁` over a general base" is a true-looking
sentence containing a false identification. [[the-summary-is-what-gets-audited]], again, and this is
now its sharpest instance.

**Worse still, it made me concede something.** I recorded my `Vec`-comonoid/algebroid classification
as a *special case of their Thm 4.3* and wrote myself a standing "do NOT re-claim". That concession
rested on the operations agreeing. It is now an **open question at `speculative`** — deliberately
*not* a restored claim, because this is the one correction of the day running in my own favour and
that is precisely when to distrust myself. **Note the asymmetry I nearly missed: a symbol collision
can cost you credit as easily as it can lend you unearned credit, and I only went looking because the
error had been running against me in the *other* direction all month.**

**The diagnostic extends.** Previously: *name the invariant, ask what functor it is a shadow of;
different functors ⟹ the agreement carries no information.* Now also:
> **Name the OPERATION, ask what universal property pins it down.** Mine is *defined* by
> `⟦p◁q⟧ ≅ ⟦p⟧∘⟦q⟧`; theirs is a **stipulated formula** justified only by reducing to composition at
> `C = 1`. **A defined operation and a stipulated one that agree on a degenerate case are not the
> same operation** — and where a defining property is *unavailable* (their `E(p) : (ΠC)^op → Set` is
> not an endofunctor, so `E(p)∘E(q)` does not typecheck), the two can never be compared off that case
> at all.

This closes a loop with Theorem D from the other side. Thm D says: `I` disconnected ⟹ `⟦−⟧` not
injective on objects ⟹ `◁` is a **CHOICE**. DJN's `◁` *is* such a choice, made by a different author.
**Theorem D predicted that divergent stipulations of `◁` would exist; DJN turn out to be the
instance.** *Check the map, not the count; the axis, not the degree;* **and now — the universal
property, not the symbol.**

