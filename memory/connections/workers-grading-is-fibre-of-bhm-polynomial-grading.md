# Workers `ΔS`-grading is NOT a fibre of BHM's grading — it is a RETRACT (different products: ⊗ vs ▷)

**Status: conjecture REFUTED 2026-08-29; retract now `proved` (PROVE session same day).**
The retract `(σ,r)` is a theorem — `r∘σ=id` as genuine Poly morphisms, `σ` oplax /
`r` lax coherent, `r∘δ=Δ(d)` (⊗ = diagonal collapse of ▷), and `Δ` is NOT an oplax
monoidal functor on full `(Set,×)` (store comonad is internal). Registry
`workers-retract-of-bhm-grading` (`proved`, verified n≤3); proof
`proofs/2026-08-29-workers-retract-of-bhm-grading.md`; collaborator note
`for-collaborator/2026-08-29-workers-retract-of-bhm-proved.md`; memory
[[workers-grading-retract-not-fibre-of-bhm]]. The cheap `X▷ΔS` check
(`scratch/2026-08-29-workers-bhm-triangle-vs-dirichlet.md`, dispatched + independently
hand-verified by MacBeth) settles the open question below: the naive fibre conjecture is
FALSE. Workers grades by the **Dirichlet tensor `⊗`**; BHM grade by the **composition
product `▷`**; these are different monoidal structures on the `ΔS` family.

## THE RESULT (`computed`, 2026-08-29)
At `|S|=|T|=2`: `ΔS▷ΔT = 8·y⁴` (shapes `S×T^S = |S|·|T|^|S|`, positions `T×S`) but
`ΔS⊗ΔT = Δ(S×T) = 4·y⁴` (shapes `|S×T|`, positions `S×T`). General:
`(ΔS▷ΔT)(X)=Σ_{s∈S}Σ_{g:S→T}X^{T×S}`. Composition **blows up the shape count by `|T|^{|S|}`**;
they coincide only in the degenerate `|S|=1` or `|T|≤1`. So Workers' `(ΔS,⊗,Δ(S×T))`-grading
is **not** the `P=ΔS` fibre of BHM's `X↦X▷P`.
**Honest refinement worth keeping:** `Δ(S×T)=ΔS⊗ΔT` is a canonical **retract** of `ΔS▷ΔT`
— section `(s,t)↦(s,const_t)`, retraction `(s,g)↦(s,g(s))` (self-evaluation), `r∘σ=id`.
`⊗` is the **diagonal collapse** of the `▷` shape-blowup (the store comonad's non-invertible
comultiplication `ΔS→ΔS▷ΔS`). So the two gradings are complementary with a precise relating
map — a sharper, more publishable position than "citation subsumption." *(Retract morphism
directions VERIFIED as genuine Poly morphisms in the 08-29 PROVE session — the variance is the
content: backward position maps compose in reverse, both identities. `computed`→`proved`.)*

**Superseded framing below (kept for provenance — the conjecture it states is now refuted):**
Sources deep-read (`sources.json`:
`act2026:braithwaite-hedges-mihejevs-polylang`,
`act2026:braithwaite-hedges-mihejevs-substructural-poly`).

## The two objects

- **Mine (proved):** Workers form a `(Set,×)`-graded category via the store/state
  comonad `ΔS`, with `ΔS ⊗ ΔT = Δ(S×T)` (Lean-checked at comonad level,
  `lean-lemma31-comonad-level-done`). Grading object = a **state object `S`**.
  [[workers-graded-category-proved]], [[workers-type-hierarchy]].
- **Theirs (Braithwaite–Hedges–Mihejevs, ACT 2026, "Polylang" + "Substructural
  Type Theories Modelled by Polynomial Functors"):** the composition product on
  Poly is modelled by a **noncommutative graded monad `T_P(X) = X ▷ P`** (stack
  push/pop), graded by an **arbitrary polynomial `P`** — not merely a state
  object. (`▷` = their notation for `◁`/`⊙`.)

## The claim

`ΔS`-grading is the special case `P = ΔS = S·y^S` (the representable/store
polynomial) of BHM's `T_P(X)=X▷P`. So **Workers' `(Set,×)`-graded category is the
representable fibre of a strictly more general Poly-internal grading MacBeth had
not considered.** Direction of generality goes THEIR way — this is prior-art I
should cite, not re-claim, if the specialization checks out.

## Why it is more than a coincidence — the fibredness seam lines up

BHM state explicitly that the composition product `▷` (=`◁`) is **"not fibred in
its left variable"**, and that this is *why* they avoid Pradic–Price's
fibred-endofunctor fixpoint machinery (`2601.15420`).

That is the SAME obstruction my proved **T4-left** work locates from the other
side: `◁`-closure fails generically and collapses to closed **only when positions
are tiny** (= dualizable = the `[Z,−]`-preserves-`∐` condition).
[[t4-left-closedness-lhd-famcop]]. Two independent groups, two vocabularies, one
seam: **`◁` breaks fibredness/closure in its left variable, repairable only at a
degeneracy (tininess / representability).** This is another instance of
[[contribution-is-the-delta-prior-work-fused-away]] — but here the delta may be
*theirs*, so the honest move is to cite.

## The open question (→ `questions/workers-grading-vs-bhm-polynomial-grading.md`)

1. Is Workers `(Set,×)`-graded category exactly the `P=ΔS`-representable instance
   of `T_P(X)=X▷P`, or does the generality run the other way for some structural
   reason (Workers carries `ΔS⊗ΔT=Δ(S×T)` multiplicativity that a general `P`
   need not)?
2. Is BHM's "`▷` not fibred in its left variable" the **same mechanism** as
   T4-left's tininess collapse — i.e. does the state grading survive precisely
   because `ΔS` is representable = tiny in the relevant sense?
3. Cross-check against **Ghani–Nordvall Forsberg–Fish "Snoc Trees"** (ACT 2026,
   deep-read, `act2026:ghani-nordvallforsberg-fish-snoc-trees`): their Thm 3.5
   says `F_*` is the **free `ℕ`-graded monad on `F`**. Three graded-monad pictures
   now converge on my Workers line — Snoc (free `ℕ`-graded), BHM (`P`-graded
   composition product), Workers (`ΔS`, `(Set,×)`-graded). Are they three fibres
   of one construction? This is a candidate unification and Neil's own paper is
   one of the three.

## Load-bearing citations (do not compress away)

- BHM Polylang: `T_P(X)=X▷P`, "`▷` not fibred in its left variable"
  (`act2026:braithwaite-hedges-mihejevs-polylang`, deep-read).
- BHM Substructural: Benton-LNL model inside Poly's `(×,⊗)`
  (`act2026:braithwaite-hedges-mihejevs-substructural-poly`, deep-read).
- Ghani et al. Snoc Trees Thm 3.5 free `ℕ`-graded monad
  (`act2026:ghani-nordvallforsberg-fish-snoc-trees`, deep-read).
- Fixpoint-fibredness machinery avoided: Pradic–Price `2601.15420`.
- My side: [[workers-graded-category-proved]], [[t4-left-closedness-lhd-famcop]].
