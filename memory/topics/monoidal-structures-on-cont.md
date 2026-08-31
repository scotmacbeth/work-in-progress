# Monoidal structures on Cont — the Day family

**The centre of gravity of Neil's steer** (2026-06-11, unchanged 2026-07-14): the book's spine is
"the four monoidal structures on `Cont`", each as *"(Cont, ⊗, I) is a monoidal category"* + *"⟦–⟧ is
a monoidal functor"*. `◁` is called the **sequential operator** throughout, per his instruction.

As of 2026-07-14 the four are **no longer a census — they are the worked instances of a
classification.**

## The one idea

**`Cont ≅ Fam(Set^op)` — the FREE COPRODUCT COMPLETION of `Set^op`.** A container *is* a family of
sets. Consequences, all immediate once you see it:

- Day convolution on `Cont` needs **no coend** — it is just "extend by coproducts":
  **`p ⊙_⋆ q = (S_p × S_q,  (s,t) ↦ p[s] ⋆ q[t])`**.
- **Shapes always multiply. The monoidal structure on `Set` only ever shows up in the POSITIONS.**
- A tensor preserving coproducts in each variable is *determined* by its restriction to
  representables — which is what makes the classification possible at all.

## The taxonomy (a theorem, not a list)

| tensor | unit | Day? | pointwise? |
|---|---|---|---|
| `+` | `0` | **no** | yes |
| `×` | `1` | **Day of `(Set,+,0)`** | **yes — and uniquely so** |
| `⊗` Dirichlet | `y` | **Day of `(Set,×,1)`** | no |
| `◁` sequential | `y` | **no** — but `⊗` is its Day-ification | no |

- **`+` is not Day, and fails for a triviality:** every Day tensor annihilates `0` (`S × ∅ = ∅`) and
  the coproduct never does.
- **`◁` is the near miss** — it satisfies (D2) exactly and (D1) in the *left* variable only, and
  restricts to `(A,B) ↦ A×B` on representables, *the same restriction as `⊗`*. Hence Thm C.

## The theorems (2026-07-14 PROVE; `proofs/2026-07-14-day-family-classification.md`)

Registry: `day-family-classification` [proved] + children, validator green.

- **Thm A (classification).** Day is an **equivalence** {monoidal structures on `Set`} ≃
  {**convolutional** structures on `Cont`}, where convolutional = **(D1)** preserves coproducts in
  each variable + **(D2)** representables closed. *The literature states only EXISTENCE* — "for any
  `⋆` on Set there IS one on Poly", **Niu–Spivak arXiv:2312.00990 Prop 3.79**. No converse, no
  essential image, no fullness anywhere. *(Lemma 3.2: representability of the unit is a
  consequence of (D1)+(D2), not an assumption.)*
- **Thm B⁺ (uniqueness).** **The categorical product is the UNIQUE pointwise monoidal structure on
  `Cont`** — among *all* of them, no Day hypothesis needed. Effective test (B′): unit initial +
  canonical `κ : A+B → A⋆B` bijective. **Being pointwise is the rare thing, not the generic one.**
- **Cor 5.5 (sharpness).** A **proper class** of pairwise non-iso convolutional structures (Spivak's
  `▷_S` from `A ∨_S B = A + A×S×B + B`), **all sharing the product's unit** (terminal `1 = y^∅`).
  Exactly one (`S=∅`) is the product. **No cheap invariant singles the product out** — not the unit,
  not coproduct-preservation, not semicartesianness. Only `κ`. *(I do not claim `∨_S` is symmetric —
  hexagon unverified, and not needed.)*
- **Thm C (the comparitor).** `p ⊗ q → p ◁ q` is the **counit of a coreflection**:
  `p ⊗ − = Lan_J((p ◁ −)∘J)`, the **terminal coproduct-preserving approximation to `p ◁ −`**. So
  **`⊗` is the Day-ification of `◁`.** *Lemma 2.6 (the fix the referee-pass forced): `p ◁ −` does
  **not** preserve coproducts, so the free-completion property is the wrong justification for
  `(Lan_J G)(q) = Σ_t G(q[t])`; it holds against arbitrary functors, proved via the comma category
  (splits over shapes, each fibre has a terminal object).*

## Novelty, honestly

**Prior art:** the Day family's *existence*, the formula, `×`=Day(+), `⊗`=Day(×), the `∨_S` family,
**and the comparitor map itself** — six independent statements, incl. **Spivak arXiv:2202.00534
`Indep`, Eq. 32** (from the `⊗`/`◁` duoidal interchange, **Eq. 29**; iso when `p` linear or `q`
representable, **Eq. 33**) and **Niu–Spivak `o_{p,q}`, Ex. 6.85**. Spivak's Topos blog (2023-09-21)
states "⊗ is the Day convolution of × on Set, and × on Poly is the Day convolution of + on Set"
*plainly*, three years early.

**Mine:** Thm A, Thm B/B′/B⁺, Lemma 4.4 (rigidity of `+`), Cor 5.5, **Thm C's universal property**,
Prop 6.2's exact trichotomy.

## The dead end, and why it was forced

The 06-13 claim *"φ = identity, ⟦–⟧ is **strict** monoidal for `⊗`"* is **DEAD** — a category error
(`⊗_Dir` was *defined* by transporting along `⟦–⟧`, so "preservation" was circular). `⟦–⟧` is
**strong**, not strict. And *"`⊗` isn't pointwise **because** Day"* is false: **`×` is also Day and
IS pointwise.** Real criterion: does the corepresentable split the domain tensor?
`y^(A+B) ≅ y^A × y^B` yes; `y^(A×B)` no. **Cor 4.5 explains the whole dead end:** `⟦–⟧` is strong
monoidal into the *pointwise* product **iff** the tensor is the cartesian one. No version of the
claim could have been true. See [[circular-verification-and-reading-depth]].

## Lean status (all machine-checked, 2026-07-14)

`Monoidal.lean` — all four are `MonoidalCategory` instances (hand-rolled class): pentagon, triangle,
naturality; plus `⟦–⟧`'s comparison isos. 16 jobs, 0 errors, 0 warnings, zero `sorry`.
**The joke:** `contDirichletMonoidal` needs **no axioms at all** (every coherence `rfl`); the other
three need `Quot.sound`. The structure I called "the subtle one" is the *tamest* in Lean.
**Semantic subtlety and syntactic subtlety are unrelated.**

`Comonoid.lean` — **M3: a directed container is a comonoid in `(Cont, ◁, I)`** (`lean-verified`).
Converse `m3b` = `in-progress`, fully scoped.

`DirichletClosed.lean` — **`(Cont, ⊗, y)` is a CLOSED monoidal category** (`lean-verified`). Internal
hom, both round-trips, naturality in both variables, `dirEval`, triangle. **Zero axioms; every proof
`rfl`.** The two negative controls *fail to typecheck*. See the closed-structures section above.

## The CLOSED structures — requested by Neil 2026-07-14, NOT deferred

**The 06-13 line "closed structure deferred by Neil" is DEAD.** He **asked for the closed structures**
by email on 2026-07-14. Registry: `closed-day-structures` [in-progress].

**`(Cont, ⊗, y)` is a machine-checked CLOSED monoidal category** — `DirichletClosed.lean`,
`lean-verified`. Internal hom: **shapes of `[q,r]` = the container morphisms `Cont(q,r)`; positions
at `f` = `Σ_t r[f₁ t]`.** Both round-trips, naturality in **both** variables, counit `dirEval`,
triangle identity. **`#print axioms`: no axioms at all — every proof is `rfl`.**
Verified computationally too (`scratch/dirichlet_closure_check.py`): 5197 triples / 0 failures;
1,248,025 naturality squares / 0 failures; **all three negative controls caught** — *not a mirror*.
Two negative controls **fail to typecheck**, as they must: the wrong position family, and currying
out of the **categorical product** instead of `⊗` — because `(p×q)[s,t] = p[s] + q[t]` is a **SUM**
and has no projections. **Lean states the `×`-vs-`⊗` distinction as a type error.**

**The mathematics is PRIOR ART. DO NOT CLAIM IT.** Niu–Spivak **Ex. 4.78 / Eq. 4.79**; Spivak
**2202.00534 Eq. 44**. My derivation reproduces Eq. (4.79) character-for-character. What is mine is
the **proof object** — believed the first machine-checked Dirichlet closure. Likewise the
`◁`-**co**closure (`Poly([q◁p],p') ≅ Poly(p,p'◁q)`) is **Spivak Eqs. 68–69 / Niu–Spivak Prop. 6.57,
credited to Josh Meyers**. *And my own notes of 2026-06-12 already had the Dirichlet closure filed as
a citation — I re-derived it a month later. **Grep your own notes first.*** → SUMMARY, "Dead ends".

**The salvage, and it is the real theorem here — THE UNIFORM CLOSURE FORMULA** (`computed`; no
write-up on disk yet, which is exactly why it is not `proved`): for a Day-convolutional `⊙_⋆`,

> **`[p,q]_⋆ = Π_{I ∈ p(1)} q ◁ (p[I] ⋆ y)`**, i.e. `[p,q]_⋆(A) = Π_I q(A ⋆ p[I])`.
> **Exists iff `R ⋆ (−)` is POLYNOMIAL (preserves wide pullbacks) for every set `R`** — *not*, as
> first claimed, that `⋆` be closed on Set.

`⋆ = +` ⟹ cartesian closure (**Thm 5.31**); `⋆ = ×` ⟹ Dirichlet closure (**Eq. 4.79**); `⋆ = ∨_S` ⟹
Spivak's third family. **Spivak's Eqs. (38)/(39)/(40) are these three side by side — the general
theorem is never stated. That gap is the claim.** Corollary (`speculative`, necessity direction
unargued): {monoidal `⋆` with `R ⋆ (−)` polynomial} ≃ {closed convolutional structures on Cont}.

### ⚠️ The claim that DIED here — and the one that LIVED (they look identical; do not confuse them)

- **DIED:** *"`⊙_⋆` is **closed** iff the corepresentable `Set(R,−)` **preserves** `⋆`"*, plus the
  "pointwise/closed duality" narrative. **REFUTED same day.** `×` is Day-of-`(Set,+,0)`; `Set(R,−)`
  does **not** preserve `+`; yet **Cont IS cartesian closed** (Thm 5.31). **No duality exists — `×`
  is both pointwise AND closed.** Registry: `closed-iff-corepresentable-preserves-star` [dead-end].
- **LIVED:** *"does the corepresentable **SPLIT** the domain tensor?"* — `y^(A+B) ≅ y^A × y^B` yes,
  `y^(A×B)` no. **That is the POINTWISENESS criterion (Thm B⁺), and it stands.**
- **Closedness is not pointwiseness.** One line apart in the prose; one of them is false.

## Where it goes next

- **The comparitor's variance is predictive** — container monads descend to Dirichlet monoids;
  directed containers do **not** descend to Dirichlet comonoids. This joins Neil's Phase 1 (the four
  structures) to his Phase 2 (free monad / cofree comonad) at a single point.
  **→ [[comparitor-points-the-wrong-way]]** (the crown jewel; novelty unaudited).
  **★★ Niu–Spivak Remark 3.78 (p. 70) parks "monoids in Poly w.r.t. `⊗`" as FUTURE WORK.** This lives
  in exactly that lane — **an open lane the book's own authors say is open. Highest-value target.**
- **Thm A survives a full-PDF novelty check:** **Prop 3.79 states only the FORWARD direction**; there
  is **no converse, injectivity, uniqueness or classification** in the book. The equivalence is
  **unscooped**. ⚠️ But **Ex. 3.82** already runs 3.79 on an exotic `A ★ B ≔ A + AB + B`, so **do not
  claim "a third convolutional tensor" as new** — they treat 3.79 as a general machine.
- **Open with Neil:** flat-four vs Day-family framing. The Day-family framing says *why there are
  four*; the flat four is what he asked for.

## Closure & the vacuity question (2026-07-15 → 07-22: RESOLVED, vacuity FALSE)

- **Uniform closure biconditional (proved 07-15, `2026-07-15-uniform-closure-day-tensors.md`):**
  `(Cont, ⊙_⋆)` left-closed ⟺ `R_B := (−)⋆B` polynomial ∀B; internal hom `⟦[p,q]⟧R = Π_i ⟦q⟧(R⋆p[i])`.
  Registry `closed-day-structures` = **proved**.
- **Π-form = morphism-form (Lean, 07-21):** `Container.ihomPiIso : ihom q r ≅ Π_i (r◁q[i]·y)` machine-
  checked, **axiom-free, both round trips `rfl`** (`DirichletHomPi.lean`). Closes the "Π-formula
  unformalised" caveat given to Neil. Only `⋆=×` formalised.
- **★ Is the side-condition ever false? RESOLVED 07-22: it is FALSE (`2026-07-22-vacuity-resolved-collapse-tensor.md`).**
  The 07-21 vacuity conjecture (below) was WRONG. The **COLLAPSE TENSOR** `A⋆B := B if A=∅ / A if B=∅ /
  1 if A,B≠∅` (unit ∅, symmetric) is genuinely monoidal (associator+pentagon+triangle+unitors+braiding;
  emptiness-pattern proof + size≤3 exhaustive), yet `R_2=(−)⋆2` is **non-polynomial** (`R_2(∅)=2 > 1=R_2(1)`,
  violating `|F(∅)|≤|F(1)|`). So `⊙_collapse` is **convolutional but NOT left-closed** ⟹ **convolutional ⊋
  left-closed** (answers Neil's "lucky with ⊗,×" = YES). Mechanism = **unit insertion `η_B` non-injective
  ("×1 shrinks")** — the failure mode the 07-21 three-candidate search never considered (it hunted the
  support tensor's *phantom-extra*; collapse *shrinks to the point* instead). **η-cartesian framework
  LOCATES all counterexamples:** Lemma D (proved) ∧ ¬★' (balanced⟹independent ⟺ η cartesian). Registry
  `closed-day-structures.condition-vacuity` = **proved (NO)**. **→ [[vacuity-false-collapse-tensor]]**.
  The `polynomiality=provenance=coherence` slogan survives as *intuition* (why the closed tensors track
  provenance) but the "closure is free" reading is dead → [[polynomiality-is-provenance-is-coherence]].
- **★ Precedent/foil for the book write-up (n-Café 2009 "Monoidal Closed Categories and Their Deviant
  Relatives") — RESOLVED 2026-07-22 (browse2), full thread read.** Baez–Stay ask whether "internally
  closed" (currying iso, no adjunction) ⟹ genuinely closed. **Theo's** counterexample (constant functor
  `a⇒y=0` for all `a,y`) mechanism = coherence-satisfied-vacuously-without-representability — a
  definitional critique, not a collapsing map. **Cisinski's** (Bousfield localization, `Hom(1,X)≃UF(X)`)
  mechanism = unit/counit of a *monoidal adjunction between two different categories* failing to be iso —
  an idempotent-monad compression across categories. **Neither shares collapse's exact mechanism**
  (a single-category representability failure via non-injective unit-insertion `η_B` breaking
  polynomiality of `R_2` *within* Poly/Cont). Same broad genus ("monoidal but the naive candidate right
  adjoint doesn't work"), three distinct specific mechanisms. **Verdict: cite as precedent for the
  phenomenon class** ("coherence/naive-formula without genuine representability has been noted before,
  e.g. this 2009 thread"), **not as a scoop** — no retraction or reframing of the collapse-tensor result
  needed. Ships clean to /write. **New PROVE target (refined, still open):** characterize which
  convolutional `⋆` ARE left-closed = monoidal `⋆` preserving connected limits per variable; necessary
  conditions = taut / η injective + ★'. (Neil-gated; asked in the 07-22 daily.)
- **Dichotomy (now sharper):** convolutional ⊋ left-closed *even inside the Day family* (collapse witnesses
  it); AND the only closed tensors are `⊗` + the `▷_S` family (bounded-arity, `closed-convolutional-tensors-classified`),
  while the non-convolutional `⋉/⋊` (Dialectica line) are non-closed from *outside* the family. Three ways
  to miss closure, one book paragraph.

**Output:** `papers/four-monoidal-structures.tex` (18pp), local. **Share by email — the seed is off
GitHub (Robin's call: confidential Kodamai material); there are no PRs and no push access, and that
is policy, not breakage.** The book itself is local: `git/ghani-containers/books/category-of-containers.tex`
(`\author{MacBeth}` — *not* `books/book.tex`, which is Robin's).
