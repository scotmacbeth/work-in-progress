# Q4: Is Weber's familial-but-not-opfamilial the SAME seam as my one-sided joint BC?

**Date:** 2026-08-30. **Verdict: DIFFERENT AXES** (with one genuine, weaker structural parallel — see §5).

**Provenance / honesty statement.** I READ the primary source. The PDF is on disk at
`/tmp/browse/weber-fam2fun.pdf` (recovered 2026-08-29 from the author's mirror
`https://webercat.au/fam2fun.pdf`), with a `pdftotext -layout` extract at
`/tmp/browse/weber-fam2fun.txt` (3942 lines). I re-downloaded the PDF today and confirmed
`md5 = 939593036bb2ed20f2f8b0232e711803` for both copies — same file, so the extract is
faithful to what the mirror currently serves. Everything in §§1–3 below is **quoted verbatim**
from that extract with line locators. §§4–5 are my **inference**, marked as such.

⚠ Note on locators: Weber numbers sequentially across a section, so **§5.9 is a *subsection
heading*** ("Fam as a familial 2-functor") that *contains* 5.10–5.16. The non-opfamiliality
argument sits in unnumbered prose between Cor 5.14 and Prop 5.15, i.e. inside subsection 5.9,
just after Prop 5.13. MacBeth's "§5.9/5.13" pointer is correct.

---

## 1. What "familial"/"opfamilial" means — Def 5.2 (VERBATIM, txt lines 1847–1853)

> **5.2. Definition.** A 2-functor `T : A→B` between finitely complete 2-categories is familial
> when it is p.r.a and the 2-functor
>                    `T1 : A → B/T1`
> factors through `U_{T1} : Spl(T1)→B/T1`. `T` is **opfamilial** when the 2-functor
> `T^co : A^co →B^co` is familial¹⁵. A 2-monad is familial (resp. opfamilial) when its
> underlying 2-functor is familial (resp. opfamilial), and its unit and multiplication are
> cartesian.
>
> ¹⁵ *In other words just reverse all the 2-cells in the definition of "familial" to define
> "opfamilial". Note that this includes replacing split fibrations by split opfibrations.*

Weber's gloss (lines 1857–1866):
> "As in the one dimensional case p.r.a-ness for `T : A→B` asks more of the assignment
> `A ↦ T t_A : TA→T1`, namely, that it is the object map of a right adjoint. **Familiality asks
> further that `T t_A` be a split fibration**, or more precisely that this right adjoint factor
> through `Spl(T1)`. […] In the example of `Fam` discussed below, `T t_A` is one of the most
> well-known examples of a split fibration: it is the functor `Fam(A) → Set` which sends a
> family of objects to its indexing set."

**So: `opfamilial` differs from `familial` ONLY by the orientation of 2-cells — split fibration
vs split opfibration.** It is a *2-dimensional orientation* axis, not a quantifier-interchange axis.

## 2. The positive half — Prop 5.13 (VERBATIM, lines 2187–2192)

> **5.13. Proposition.** `Fam` is a familial 2-functor. Moreover `f : B→Fam(A)` is `Fam`-generic
> iff it endows `B` with elements.
>
> *Proof.* If `f` endows `B` with elements then it is generic by lemma(5.12). Thus by
> lemma(5.11) `Fam` is p.r.a. Moreover by that lemma if `f` is generic, then you can factor it
> as `Fam(h)g` where `g` endows `B` with elements. But this implies that `g` is itself generic,
> and so `h` is an isomorphism, whence `f` also endows `B` with elements.

Supporting definition (5.10, lines 2082–2090):
> **5.10. Definition.** A functor `f : B→Fam(A)` **endows `B` with elements** when:
> 1. For all `a ∈ A`, there is a unique `b ∈ B` and a unique `i ∈ I_b` such that `f b(i) = a`.
> 2. For all `α : a1→a2`, there is a unique `β : b1→b2` in `B` and `i ∈ I_{b1}` such that
>    `(fβ)i = α`.
> In other words, `f` endows `B` with elements when each object and each arrow of `A` is used
> exactly once as a label by `f`.

And Cor 5.14 (lines 2193–2196):
> **5.14. Corollary.** `Fam` is a polynomial 2-functor: `Fam ≅ P_τ`, where `τ : Set_• → Set` is
> the forgetful functor from the category of pointed sets.

## 3. THE COUNTEREXAMPLE TO OPFAMILIALITY (VERBATIM, lines 2201–2213)

This is the whole argument, word for word:

> "To see that familiality is stronger than p.r.a'ness, note that by theorem(6.2) below,
> familial 2-functors preserve discrete fibrations, and dually, opfamilial 2-functors preserve
> discrete opfibrations. However applying `Fam` to the discrete opfibration `τ : Set_• → Set`
> does not give a discrete opfibration. Consider for instance a set `S` with 2 distinct elements
> `x` and `y`. Then the 2-element family of pointed sets `((x,S),(y,S))` is sent by `Fam(τ)` to
> the 2-element family `(S,S)`. There is a unique chosen `Fam(t_Set)`-cartesian map
> `f : (S,S)→(S)` in `Fam(Set)`, where `(S)` denotes the singleton family consisting of the set
> `S`, and this map admits no lifting to a map `((x,S),(y,S))→((z,S))` in `Fam(Set_•)`:
> **if such a lifting existed we would have `x = z = y`, but `x` and `y` are different.** Thus
> `Fam` is familial but not opfamilial, and dually the endo-2-functor of `CAT` whose object map
> is `X ↦ Fam(X^op)^op` is **opfamilial but not familial**. An example of a p.r.a 2-functor which
> is neither familial nor opfamilial is `Φ_B`, the underlying endofunctor of the fibrations
> 2-monad of subsection(3.1). Even in the case `K = CAT` one can easily verify that `Φ_B` is
> neither familial nor opfamilial."

Mechanism cited (Thm 6.2, line 2456, VERBATIM):
> **6.2. Theorem.** Let `T : A→B` be a familial 2-functor between finitely complete
> 2-categories. Then `T` preserves fibrations, bifibrations, iso-fibrations and one-sided
> discrete fibrations.

---

## 4. THE DECIDING COMPARISON (my analysis — INFERRED, but from the verbatim text above)

### 4a. What my ∃-obstruction actually is
From `proofs/2026-08-28-joint-bc-cont-cod.md` Thm 5.1(i), the ∃-side cross-BC failure is

```
LHS at ρ  =  ∐_{p ∈ τ⁻¹(ρ)}  ∏_{s}  n^{(s)}_p          (sum of products)
RHS at ρ  =  ∏_{s}  ∐_{p ∈ τ⁻¹(ρ)}  n^{(s)}_p          (product of sums)
witness:  n^(1)=(a,b), n^(2)=(c,d)  ⇒  ac+bd  ≠  (a+b)(c+d) = ac+ad+bc+bd
```

Structural features, all essential:
- **TWO distinct index sets** — positions `τ⁻¹(ρ)` and shapes `s` — being *interchanged*.
- The canonical comparison is the **distributivity map** `∐∏ → ∏∐`; it is injective, never
  surjective once both index sets have ≥2 elements.
- The failure is **quantitative** (a cardinality inequality `ac+bd < ac+ad+bc+bd`).
- The failure would persist for *any* choice of labels; it is about the SHAPE of the formula.

### 4b. What Weber's non-opfamiliality obstruction actually is
Unwinding the quoted argument: a lift of the source over `j ∈ J` along `(k,k̄):(I,f)→(J,g)` is
an element `z_j ∈ g(j)` satisfying `z_{k(i)} = k̄_i(x_i)` for **every** `i ∈ k⁻¹(j)`. So the set
of lifts over `j` is an **equaliser of `|k⁻¹(j)|` parallel constraints** — equivalently, it asks
the **diagonal** `g(j) → g(j)^{k⁻¹(j)}` to hit the given tuple. Weber's `S` with `x ≠ y` is exactly
the statement `Δ : S → S×S` is not surjective: *"if such a lifting existed we would have
`x = z = y`, but `x` and `y` are different."*

Structural features:
- **ONE index set** — the fibre `k⁻¹(j)` of a single function.
- The comparison map is the **diagonal / equaliser**, not a distributivity map.
- **There is no coproduct anywhere in the argument.** No `∐` is being interchanged with a `∏`.
  Nothing is being summed. There is no second index set to interchange with.
- The failure is **structural, not quantitative**: it is `x ≠ y`, a failure of a *limit over a
  non-singleton fibre* to be trivial. (Note it also fails for `k⁻¹(j) = ∅`, where the lift is
  free rather than over-determined — the *opposite* kind of failure, existence-vs-uniqueness.
  A distributivity gap has no such empty-fibre mode.)

### 4c. Verdict
**DIFFERENT AXES.** The check MacBeth named in advance returns NO. Weber's counterexample to
opfamiliality is *not* a `∐∏` vs `∏∐` distributivity failure. It is a failure of a **diagonal /
equaliser over a non-singleton (or empty) fibre**, in a construction where no coproduct is
being interchanged with anything. The two obstructions differ on every diagnostic that matters:
number of index sets (2 vs 1), comparison map (distributivity vs diagonal), failure mode
(cardinality gap vs `x ≠ y` / free choice), and dimension (1-categorical quantifier calculus vs
the orientation of 2-cells).

This makes it **four refutations in a row** on "are these two conditions the same?".

## 5. What IS genuinely shared (weaker, and worth banking) — INFERRED

Do not overclaim this, but do not throw it away either. Two real parallels:

**(i) The same *move*: the fibrewise op swaps which side is well-behaved.**
Weber, verbatim: *"dually the endo-2-functor of `CAT` whose object map is `X ↦ Fam(X^op)^op`
is opfamilial but not familial."* That is precisely my "contravariance IS the fibrewise op"
(`Cont(cod) = Fam(cod^op)`, `Cont = ∫_Set (cod)^op`). My co-hyperdoctrine result is exactly the
statement that the fibrewise op *moves* Frobenius+BC from the left adjoint (`Σ_!`, classical
Lawvere) to the right adjoint (`E = (Σ_!)^op`, co-Frobenius). Weber's dichotomy is the same
*operation* — apply the fibrewise op, the good side flips — applied to a different property.
So: **same op, two different properties it toggles.** That is a shared mechanism at the level of
the duality, NOT a shared obstruction.

**(ii) A cheap, citable corollary I can now assert.** My ambient construction
`Fam(C^op)` / `Cont(cod)` is literally Weber's dual 2-functor `X ↦ Fam(X^op)^op`. By the quoted
sentence, that 2-functor is **opfamilial but not familial**. So the container/co-hyperdoctrine
setting sits, by Weber's own classification and in his own words, on the *opfamilial* side of
the dichotomy — a primary-source-backed placement of my construction inside his taxonomy.
(Caveat, honestly flagged: Weber's statement is about `X ↦ Fam(X^op)^op` as an endo-2-functor of
`CAT`; matching that against `Fam(cod^op)` fibred over `Set` is a *plausible but unverified*
identification. Do not let this become load-bearing without checking it.)

**(iii) A shallow coincidence to explicitly NOT count as evidence.** Both obstructions vanish
when every fibre is a singleton. That is true of essentially every fibre-aggregation obstruction
in category theory and carries no information.

## 6. Consequence for the Q4 entry

Q4 should be closed as **DIFFERENT AXES / second independent asymmetry** — the outcome MacBeth
predicted and the one he called more valuable. Weber's asymmetry is *2-dimensional and
orientational* (split fibrations vs split opfibrations, Def 5.2 fn 15); mine is
*1-dimensional and distributive* (`∐∏ ≠ ∏∐` in `(Set/P)^op`). They are not two vocabularies for
one seam. The residue worth carrying forward is §5(i)–(ii): the shared fibrewise-op *move*, and
the placement of `Fam(C^op)` on Weber's opfamilial side.
