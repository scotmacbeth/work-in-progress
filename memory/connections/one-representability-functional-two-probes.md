# One representability functional, many probes — and extensivity is what *fuses* them

**Found:** 2026-09-06 (dream), consolidating the 08-30 PROVE (`fibredness-vs-left-closure`)
against the 08-29-browse2 recovery of Weber's p.r.a. paper.
**Status (updated 2026-08-30):** the three instances are individually `proved`/`computed`
(registry ids below) and the **method stands**. The *unification* under Weber's
parametric-right-adjoint machinery — the conjectural re-filing this note was opened to
propose — was **REFUTED on 2026-08-30** by the falsifier named at the bottom. The method is
therefore mine, at `speculative`, with three instances, and is **NOT** underwritten by
Weber. See "Falsifier: RUN" below. The 09-05 lesson held: the dream crown manufactured
conviction, and naming the falsifier in advance is what caught it
([[the-summary-is-what-gets-audited]]).

## The recurring situation

Three times now I have met two conditions that both read *"a canonical map is invertible"*
or *"this adjoint exists"*, both failing over `Vec`, both repaired exactly at
representability/tininess, and both plainly about the same formula. Three times the naive
identification was **wrong**, and three times the same move resolved it.

| # | the two conditions | verdict | where |
|---|---|---|---|
| 1 | T2's conjuncts **(A)** single-factor familial representability (`Q_t` dualizable) vs **(B)** product-closure (`∐_t N_t` exists in `C`) | **distinct**; `Fam(Vec_fd^op)` fails B, `Fam(Vec^op)` fails A — *dual* mechanisms | `proofs/2026-08-26-t2-day-closedness-famcop.md`, registry `t2-day-closedness-famcop` (`proved`) |
| 2 | Weber's **δ** (distributivity-pullback comparison, `1106.1983`, TAC 30 2015) vs my T2 **Φ** | **distinct**, two-way separable over Vec; conjecture REFUTED | [[weber-delta-vs-t2-phi-distinct]] (`computed`), `topics/weber-delta-vs-t2-phi-distinct.md` |
| 3 | BHM's "`▷` not fibred in its left variable" vs my T4-left `◁`-closure obstruction | **distinct**; over `Set` `(V)⟺(F)⟺(C)⟺|T|=1`, over `Vec_fd` **`(V)⊊(C)⊊(F)` strictly** | `proofs/2026-08-30-fibredness-vs-left-closure.md`, registry `fibredness-vs-left-closure` (`proved`); [[bhm-fibredness-vs-t4-left-separable]] |

Instance 2 constrains **different legs of one formula**: δ tests the LEFT position (`P_s`
exponentiable/tiny = my T4-left collapse); Φ tests the RIGHT position **and** the target
(`Q_t` dualizable + summable) and never sees `P_s`. Instance 3 is the same shape one level
up, with the separating witness `q=(ℕ,k)` over `Vec_fd`: **fibred but not closed**.

## The method (the actual, transferable content)

> **Write down the single formula both conditions are about, then identify which factor of
> that formula each condition constrains.**

Instance 3 is where the method got its sharpest form. Both conditions are the *one* question
"is `G_r(Z) = Fam(⟨Z⟩◁q, r)` familially representable?", asked at different **probes** `r`:

| probe | `r` | what it sees |
|---|---|---|
| **shape probe** | `(R, 0)` — all positions initial, `C(0,X)=1` | `G_r(Z)=R^{π(⟨Z⟩◁q)}`: the shape object only |
| **position probe** | `⟨I⟩` | whether the forced position object exists in the base |

> **Fibredness = the shape object COLLAPSES. Left-closure = collapse AND the collapsed
> coproduct is SUMMABLE inside the base.**

## ★ The new sentence (why the coincidences kept looking convincing)

Over `Set` the shape probe is binding and there is exactly **one** collapse mechanism,
`|T|=1`, which trivialises summability too. Over a linear base collapse is *generic*
(tininess), the shape probe goes vacuous, and the obstruction migrates to the position
probe. So:

> **Extensivity is not only what carries container theory ([[extensivity-is-the-container-boundary]]) —
> it is what makes logically independent conditions INDISTINGUISHABLE.** Over `Set` the probes
> fuse; off `Set` they separate.

This is the mechanism behind my own search strategy. The crown meta-pattern
([[contribution-is-the-delta-prior-work-fused-away]]) says my contribution is always the
seam prior work fused away. *Why* does prior work keep fusing? Because it works over an
extensive base, where the seam is genuinely invisible. Moving to `Fam(Vec^op)` is a
**fusion-breaking instrument**, not merely a generalisation — which is the honest reason
Neil's "use Vec as the running example" instruction keeps paying.

Same moral, independently, in the T2 conjuncts (instance 1): over cartesian-closed bases
closedness holds unconditionally and A/B are never seen apart.

## The conjectural upgrade (NEW this cycle)

"Familially representable" is **Weber's** vocabulary, and the primary source is now on file:
Weber, *"Familial 2-functors and parametric right adjoints"*, **TAC 18(22):665–732 (2007)**,
DOI `10.70930/tac/9l84qqh9` (no arXiv ID; `sources.json` key
`weber-2007-familial-2-functors-pra`, `deep-read` 2026-08-29). **Def 2.3:** `T:A→B` is
*parametric right adjoint* when `T` restricted along `A/1` has a left adjoint `L_T`.
**Ex 2.4:** polynomial functors are always p.r.a. (`T=h_!f^*g_*`, `L_T=g_!f^*`).

A p.r.a. condition is **by construction a slice-indexed family of representability
conditions**. So the conjecture:

> **My "probes" are objects of that slice, and the two-probe calculus is the generic way a
> p.r.a. condition fails non-uniformly across its slice.**

If true, the method stops being a three-times empirical pattern and acquires a citable home
and a name. Note this is the *same* re-filing already flagged for instance 2: δ ↔ Weber
`1106.1983` (distributivity pullbacks), Φ/T2 ↔ Weber TAC 18 (p.r.a./familial) — a separate
axis, not one tower.

**Cheapest falsifier (run before this becomes load-bearing).** Over `Set`, decide whether
`L_q=(−)◁q` is p.r.a. as an endofunctor of `Fam(Set^op)=Cont`. Substitution-flavoured
functors are p.r.a. in Weber's Ex 2.4 style; if `L_q` is p.r.a. for **every** `q` while my
probes fail for every `|T|≥2`, then the probes are *not* the slice objects of one p.r.a.
condition and the re-filing is wrong. One `Set`-level session. → `questions/weber-pra-boundary.md`.

## ★ Falsifier: RUN 2026-08-30 — the Weber re-filing is REFUTED

Verdict **(α)**, and stronger than (α) required. Over `Set`, `(−)◁q` does not merely satisfy
Weber's p.r.a. condition — it has an **honest left adjoint for every `q`**, with no condition
on `|T|` whatsoever. Registry `pra-vs-probe-method` (`proved`),
`proofs/2026-08-30-pra-vs-probe-method.md`.

Two independent reasons the re-filing was never going to work:

1. **WRONG ADJOINT SIDE — the diagnosis.** Weber p.r.a. is about a **LEFT** adjoint to `L_q`.
   Every one of my three probe instances tests a **RIGHT** adjoint / closure condition
   (`|T|=1` over `Set`, summability over `Vec`). These are opposite sides of `L_q`. The two
   were never the same question, and the resemblance came entirely from both being phrased as
   "a canonical map is invertible". *This is the trap the PROVE brief named in advance,
   which is the only reason it was caught rather than absorbed.*
2. **The left adjoint is PUBLISHED and UNCONDITIONAL** — Josh Meyers' `◁`-coclosure,
   Niu–Spivak **Prop 6.57** (arXiv:2312.00990, §6.3.2 p. 204), `⌜q/p⌝ = Σ_i y^{q(p[i])}`
   (6.59) = my `F_q` verbatim; restated in Spivak–Garner–Fairbanks Prop 2.16/Eq. (18) and
   Spivak `2202.00534` §5. A thrice-published unconditional adjunction **cannot discriminate**
   between my instances, so no slice-indexed reading of it could have unified them.

**What survives, and it is the useful part.** Weber's machinery still names each probe
condition *individually*: `G : C → Set` p.r.a. ⟹ `G` familially representable with index
`G(1)` (converse given coproducts). So Weber gives a vocabulary for the probes one at a time
— he does **not** give the fusion. The fusion mechanism remains my own:
**extensivity**, not parametric right adjointness.

**Successor, seeded as `state/PROVE.md` 2026-08-30 — ★ RUN THE SAME DAY, and it came back
against the seed on BOTH counts.** Proof `proofs/2026-08-30-left-adjoint-over-vec.md`, registry
`left-adjoint-over-vec` (`proved`), topic [[left-adjoint-over-vec]].

- **The predicted fourth occurrence DOES NOT HAPPEN.** On the collapse locus the left adjoint
  exists **iff `|T|=1`**, not iff `∐_t` is summable. The comparison map fails at `dim P_s = 1`
  with `|T|=2` and `T` **finite**, where summability is automatic and where *both sides even have
  the same cardinality* (4=4) — `κ` double-counts `0` and misses `e_0+e_1`. Over `Vec_fd`,
  left-adjointness **strictly implies** the closure/summability condition: they are ordered, not
  independent. **There is no left-adjoint instance of the summability pattern.**
- **The seed's premise about `(†)` was also wrong, and this is the more valuable correction.**
  `(†)` is Set-distributivity *as written*, but the adjunction never uses it. **Theorem 1:** if the
  monoidal unit `I` is **connected** (`C(I,−)` preserves ∐) then `F_q = Fam(⟦q⟧^op) ⊣ (−)◁q` for
  every `q`, over any closed symmetric monoidal cocomplete base — four lines, `γ` twice, no
  distributivity and no choice of presentation for `◁`. Distributivity of `Set` is what makes
  `Σ_s T^{P_s}` the shape set of `p◁q`; it belongs to the *construction* of `◁`, not the adjunction.
- **⚠ THE FUSION SENTENCE ABOVE NEEDS A CAVEAT, not a retraction.** "Extensivity fuses" is right for
  the three right-adjoint instances. On the **left** side the invariant is strictly finer:
  **unit-connectedness**, which is exactly T1's condition ([[fullness-unit-connectedness]]) — and
  `Set×Set` is lextensive with a **disconnected** unit, so extensivity is demonstrably *not* what
  keeps the left adjoint alive. **T1 and the `◁`-coclosure are one lemma applied twice.** Read
  "extensivity" in this note as shorthand for "the `Set`-like pole", and prefer unit-connectedness
  whenever the statement is about `⟦−⟧` or about the left adjoint.
- **The flagged zero-object caveat FIRED.** `1◁q = (T,0) ≇ 1` over `Vec`, so the slice does not
  collapse — **and p.r.a. and left-adjointness genuinely come apart off `Set`**. `L_q` is p.r.a. for
  every `q` over `Vec` as well (`Fam/(T,0)≅Fam^T`, `(L_q)_1 p=(p⊗Q_t)_t`, left adjoint
  `∐_t F_{Q_t}`). **This strengthens the refutation above:** p.r.a. of `L_q` holds on *both* bases
  for *every* `q`, so it discriminates nothing anywhere, while the probes separate on both.
- **The anti-diagonal is the surviving crown-shaped fact.** left adjoint: `Set` always / `Vec_fd`
  iff `|T|=1`; right adjoint: `Set` iff `|T|=1` / `Vec_fd` iff summable. The conditions **swap
  sides**, and in the `(V)⊊(C)⊊(F)` chain left-adjointness sits on **(V)** over `Vec_fd` (bottom)
  and above everything over `Set`. The chain inverts.

## Honesty ledger (carried, do not drop in compression)

- BHM (*Polylang*, ACT 2026, `/home/agent/papers/BHM-polylang-ACT2026.pdf`) is a **2-page
  extended abstract**; the non-fibredness claim is one unproved parenthetical in §3.
  Corroboration only — the definition and both proofs are mine.
- `◁ := ⊗` on the tiny locus is a **definition**, not a deduction (`⟦−⟧` is not full over
  `Vec` — my T1), so Theorem B is literally about `(−)⊗q`.
- Pradic–Price `2601.15420` — **DEBT CLOSED 2026-08-30.** Paper fetched, on disk at
  `papers/pradic-price_2601.15420_fixpoints-poly-of-poly.pdf` (+ `.txt`); verbatim extraction in
  `scratch/2026-08-30-pradic-price-fibred-def.md`; full accounting in §8 of
  `proofs/2026-08-30-fibredness-vs-left-closure.md`. Four findings:
  **(1) SCOOPED.** Right-variable fibredness of `◁` with base functor literally `⟦q⟧` — my §2
  "Bonus" — **is their Lemma 15** (p. 14, proof p. 31), same base functor
  (*"`J ↦ Σ_{i:I} J^{A_i}` is clearly polynomial"*). Re-attributed, not mine. And the refinement I
  had reserved as mine — cartesianness preserved in **both** variables unconditionally — is **also
  prior art**: Niu–Spivak `2312.00990` Prop. 6.88 (p. 213), which PP cite by name at p. 31. What
  survives as mine over `Set` is only the *isolation* (cartesianness free ⟹ the left-variable
  failure is **purely** base-functoriality), plus the `Fam(C^op)`/`Vec_fd` half of Lemma 2.1.
  **(2) I PROVE THEIR UNPROVED REMARK.** Their **Remark 16** (p. 14, entire: *"On the other hand,
  `X ↦ P ⋆ X` is not fibred."*) is stated with **no proof anywhere in the paper or its 25 pp of
  appendices** (only occurrences: p. 14 statement, p. 18 back-reference; App. B.1 proves Lemmas 14,
  15, 49 only). Theorem A supplies one for `C = Set` — *we supply a proof of a remark stated without
  proof in [PP26]*. Recorded as Corollary A′. BHM's parenthetical is downstream of this remark.
  **(3) NOTATION — do not re-derive.** Their `Q ⋆ P` **=** my `P ◁ Q`; their left argument is my
  right. The flip cancels, so "**left variable**" denotes the *same* variable in Pradic–Price, in
  BHM and in my notes.
  **(4) SCOPE.** Over `Set` their `shape` fibration **is** my `π` (§2.2, pp. 8–9: *"exactly the
  fibrewise opposite of the codomain fibration"*), and their Def 13 clause 1 (p. 14) is my (F) but
  with **strict** `shape ∘ F = F_0 ∘ shape^k` (*"uniquely determined `F_0`"*) where I allow a natural
  iso — so **PP-fibred ⟹ (F)** and Theorem A holds *a fortiori*. **Off `Set` they differ:** PP's
  `Cont(C)` internalises shapes in `C` under the standing hypothesis *"all categories in sight shall
  be lextensive"* (§2.1, p. 7), while `Fam(C^op)` keeps shapes external over `Set`; the two agree iff
  `C = Set`. `Vec_fd` is not lextensive, so **Theorem B is outside PP's scope** — no conflict, but no
  support either, and "fibred" there means my `π`-fibredness, not theirs.
- **Corroboration (not a claim about PP's intentions):** PP's standing lextensivity hypothesis
  (§2.1, p. 7) is precisely the assumption under which fibredness and left-closure cannot be told
  apart — so prior work that assumes lextensivity is *structurally unable* to see the separation
  `(V) ⊊ (C) ⊊ (F)` that Theorem B exhibits, since its witnesses live over the non-extensive
  `Vec_fd`. Direct support for `extensivity-is-container-boundary` /
  `one-functional-many-probes-method`: **extensivity FUSES logically independent conditions.**
- Genuinely open: is "closed ⟹ fibred" true over an **arbitrary** base? Prop 5.2 gives only
  the shape-probe necessary condition; the `Set` upgrade uses a `Set`-specific lemma.

Related: [[left-adjoint-over-vec]], [[fullness-unit-connectedness]],
[[weakenings-of-sigma-pi-delta-vec-fails-all]], [[extensivity-is-the-container-boundary]],
[[contribution-is-the-delta-prior-work-fused-away]], [[workers-grading-is-fibre-of-bhm-polynomial-grading]],
[[contravariance-is-the-fibrewise-op]].

---

## ★ UPDATE 2026-09-09 (dream) — FUSION is not the only way distinctions vanish

The 2026-09-08 browse surfaced **MO 365271** (D. Spivak, 2020) and Simon Henry's answer: in the
bicategory **pra**, no purely bicategorical construction distinguishes a genuine `Δ_f` from one
factored through `D`'s Cauchy completion. The browse log flagged this as a possible second
collapse mechanism threatening my probes. **It is a different phenomenon and it does not bite** —
the separation, and the reason `⟦−⟧`'s injectivity-on-objects is the diagnostic, is written up in
[[fusion-versus-identification]]. In one line: *fusion is a fact about the base and is an
instrument (change base, they separate); identification is a fact about the representation and is
a boundary (the question stops referring).* **Theorem D** of the admissibility file is my own
identification instance, and it is what makes the standing `◁ := ⊗` caveat structural rather than
cosmetic.
