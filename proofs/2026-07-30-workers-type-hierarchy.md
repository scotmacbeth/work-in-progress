# How far up the type hierarchy do stateful Workers go?

**MacBeth — 2026-07-30 (prove session).** Target set by Neil Ghani's 07-30 question, following the
07-28 construction of the category of Workers. Which of `Cont`'s four monoidal structures
(`◁`, `⊗`, `×`, `+`) and three closed structures descend to the graded category of Workers?

Companion code: `scratch/workers-type-hierarchy/` (`containers.py`, `frameworkA*.py`,
`interchange_test.py`, `coherence.py`, `closed_probe.py` — all green). Registry:
`proofs/registry/workers-type-hierarchy.json`. Builds on `state-object-delta.json` (**proved**),
`bare-dirichlet-comonoid.json` (**proved**), and the closed-structure census.

---

## 0. Recap and set-up

A **container** `p=(A,B)`; `⟦p⟧X=Σ_{a:A}X^{Ba}`. Morphisms compose forward on shapes, backward on
positions. On `Cont` we have four monoidal structures — substitution `◁`, Dirichlet/Day `⊗`
(unit `y`, `(p⊗q)[a,c]=Ba×Dc`), product `×` (`(p×q)[a,c]=Ba+Dc`, unit terminal `T=(1,∅)`),
coproduct `+` — and three closed structures: `⊗`-hom `[q,r]_⊗` (Niu–Spivak Ex 4.78), the `◁`
right-coclosure (`= DCont`, Prop 6.57), and the cartesian-closed exponential `q^p` (`Cont` is CCC,
Altenkirch–Levy–Staton).

`ΔS=(S,\,s↦S)` is the codiscrete category / store comonad; **Lemma 3.1** `ΔS⊗ΔT=Δ(S×T)` (strict),
`Δ1=y`. Workers form the **`(Set,×)`-graded category**
`Workers_S(p,q) := Cont(ΔS⊗p,\,q)`, composition multiplying the state grade, `= ` coKleisli of the
graded comonad `S↦ΔS⊗(−)` (proof `2026-07-28-delta-state-object-and-workers.md`).

**Two frameworks for a monoidal descent of an object-tensor `⋆`.** A monoidal structure on a
`(Set,×)`-graded category is a *graded* bifunctor, so its tensor combines grades by the grading
monoidal product `×`. That is framework (A). There is also a coarser "shared register" operation (B):

- **(A) grade-multiplying (Para).** `(S`-worker`)⋆(T`-worker`) → (S×T)`-worker; needs
  `Φ^⋆_{S,T}: Δ(S×T)⊗(p⋆q) → (ΔS⊗p)⋆(ΔT⊗q)`.
- **(B) shared-state (diagonal).** `(S`-worker`)⋆(S`-worker`) → S`-worker on one shared register;
  needs `n^⋆_S: ΔS⊗(p⋆q) → (ΔS⊗p)⋆(ΔS⊗q)`, i.e. `ΔS⊗(−)` oplax monoidal for `⋆`. Equivalently
  (A) after the grade-diagonal `S→S×S` and a **collapse `S×S→S`**.

(A) is the honest "graded monoidal category"; (B) is a natural refinement (two workers sharing one
state register), and is where the interesting obstruction lives.

---

## 1. Framework A — grade-multiplying (the graded monoidal category)

### Theorem A (monoidal descent). All four structures descend; `⊗` is strong, `×,+,◁` are oplax.

**A1 (`⊗`, strong). PROVED.** The action `⊙ : (Set,×)×(Cont,⊗) → (Cont,⊗)`, `⊙(S,p)=ΔS⊗p`, is a
**strong symmetric-monoidal functor**:
```
   ⊙(S,p) ⊗ ⊙(T,q) = ΔS⊗p⊗ΔT⊗q  ≅(sym)  ΔS⊗ΔT⊗p⊗q  =(Lem 3.1)  Δ(S×T)⊗(p⊗q) = ⊙(S×T, p⊗q),
```
`⊙(1,y)=y`. The comparison `Φ^⊗` is a **natural isomorphism** (verified iso in `frameworkA.py`).
Its coherence is inherited from the symmetric-monoidal coherence of `(Cont,⊗)` together with the
*strict* functoriality `S↦ΔS` (Lemma 3.1). Hence `Para_⊙(Cont,⊗)=`**Workers`⊗`** is a **strong
monoidal `(Set,×)`-graded category**, grades multiplying. ∎

**A2 (`×`, oplax). PROVED.** Define `Φ^×_{S,T} := ⟨λ, ρ⟩` into the product `(ΔS⊗p)×(ΔT⊗q)` by its
two legs
`λ : Δ(S×T)⊗(p×q) → ΔS⊗p` and `ρ : → ΔT⊗q`, each the tensor of a **grade-projection**
`Δ(S×T)⊗(−) → ΔS⊗(−)` (forward `π_S` on shapes, backward `x↦(x,t)` restoring the base `t` — a
well-formed container morphism, `frameworkA.py`) with an **object-projection** `p×q→p`. Coherence is
*forced by the universal property of `×`*: a map into a product is determined by its legs, so the
oplax pentagon for `Φ^×` reduces to the agreement of the two three-fold legs
`Δ(S×T×U)⊗(p×q×r)→ΔS⊗p`, which holds because grade-projections in the cartesian `(Set,×)` and
object-projections in the cartesian `(Cont,×)` are each coherent. Interchange verified (256 cases).
`Φ^×` non-iso (state duplicated) ⟹ genuinely oplax, not strong. Workers`×` is an **oplax** monoidal
graded category. ∎

**A3 (`+`, oplax). PROVED.** `⊗` is Day convolution, hence cocontinuous in each variable, so
`ΔS⊗(−)` preserves coproducts. Combined with the *cartesian* grade projections
`Δ(S×T)⊗p → ΔS⊗p` (drop `t` forward, restore the base `t` backward — canonical because `(Set,×)` is
cartesian), one gets
`Φ^+ = (proj_S⊗id)+(proj_T⊗id) : Δ(S×T)⊗(p+q)=Δ(S×T)⊗p+Δ(S×T)⊗q → (ΔS⊗p)+(ΔT⊗q)`, coherent. Oplax
(non-iso: grades projected). ∎

**A4 (`◁`, oplax). COMPUTED.** `Φ^◁: Δ(S×T)⊗(p◁q) → (ΔS⊗p)◁(ΔT⊗q)` exists (outer container takes
grade `S`, inner takes grade `T`, both supplied by the base `Δ(S×T)` — **no state-merge**; `Φ^◁`
valid, non-iso, `frameworkA_lhd.py`). The **interchange law** for the resulting Para tensor holds on
256 multi-shape/multi-position tests (`interchange_test.py`). *Gap:* the associativity/unit pentagon
of `⊙` as an oplax monoidal functor for `◁` is verified only through interchange; a full coordinate
coherence proof is unwritten (grade `S`,`T` come from the cartesian base, as in A3, but `◁` is
neither cartesian nor cocontinuous, so I do not claim it PROVED).

**Interchange (all four).** For the Para tensor `⊗_W` with the above `Φ^⋆`, the bifunctor
interchange `(w₁'∘w₁)⊗_W(w₂'∘w₂) = (w₁'⊗_W w₂')∘(w₁⊗_W w₂)` holds on all 256 tests for every
`⋆∈{⊗,×,+,◁}` (`interchange_test.py`) — `⊗_W` is a well-defined graded bifunctor in every case.

---

## 2. Framework B — shared state (where the obstruction lives)

### Theorem B. `+` is strict and `×` is (canonically) oplax with **no** condition on `S`; `⊗` and
`◁` require a **monoid structure on the state `S`**, of which none is natural — so they do **not**
descend to a shared-state tensor.

**B1 (`+`, strict). PROVED.** `ΔS⊗(p+q) = (ΔS⊗p)+(ΔS⊗q)` strictly (Day convolution preserves
coproducts): shapes `S×(A+C)=S×A+S×C`, fibres agree (`test_maps.py`, iso). `ΔS⊗(−)` is a strict
(strong) monoidal functor for `+`. ∎

**B2 (`×`, oplax, free). PROVED.** `(Cont,×)` cartesian ⟹ `ΔS⊗(−)` canonically oplax monoidal via
`n^×_S = ⟨ΔS⊗π₁, ΔS⊗π₂⟩ : ΔS⊗(p×q) → (ΔS⊗p)×(ΔS⊗q)` (the state-diagonal on the shared register);
coherence forced by the universal property of `×`. Non-iso (state duplicated) ⟹ genuinely oplax. ∎

**B3 (`⊗`, needs a monoid). PROVED (obstruction).** Oplax monoidal structures on `ΔS⊗(−)` for the
Dirichlet `⊗` correspond bijectively to **`⊗`-comonoid structures on `ΔS`** (standard: for
`L_M=M⊗(−)` on a symmetric monoidal category, oplax structures ↔ comonoids on `M`; here
`n_{y,y}=Δ_M:ΔS→ΔS⊗ΔS`, `n_0=ε_M:ΔS→y`). By the classification
`Comon(Cont,⊗,y)≅Fam(Mon^op)` (`bare-dirichlet-comonoid`, **proved**), a `⊗`-comonoid on
`ΔS=Σ_{s}y^S` is exactly a **family of monoids on the fibre `S`** (`M_s=(S,μ_s,e_s)`, one per shape
`s`): `Δ_M` = diagonal on shapes + `μ_s:S×S→S` on fibres, `ε_M` = a unit `e_s∈S` per shape. The
oplax left/right unit laws read `μ_s(e_s,x)=x`, `μ_s(x,e_s)=x` — i.e. each `M_s` a **monoid**.
No such structure is natural in `S∈Core(Set)` — two independent obstructions:
- **`S=∅`.** A monoid on the fibre needs a unit `e∈∅` — none exists. The graded structure must be
  defined at *every* grade, including `∅`, so it cannot exist. (Undeniable killer.)
- **`|S|≥2`.** Naturality under `Sym(S)` forces each `μ_s` to be `Stab(s)`-equivariant; the only
  equivariant associative `S×S→S` are the projections `π_L,π_R` (up to the non-unital `|S|=3`
  third-element magma), and no projection has a unit. Equivalently: a natural unit is a natural point
  of `Id:Core(Set)→Set`, i.e. an element of `S` fixed by all bijections — none for `|S|≥2`.

Hence there is **no natural shared-state `⊗`-tensor**; one exists precisely per choice of monoid on
`S` (e.g. `Workers` over a *monoid*-graded base regains it). ∎

**B4 (`◁`, needs a monoid). COMPUTED.** In `n^◁_S: ΔS⊗(p◁q)→(ΔS⊗p)◁(ΔS⊗q)` a right-hand position
is `((sp,b),(sq,d))` carrying **two independent states** — `sp` on the outer `ΔS⊗p`, `sq` on the
inner `ΔS⊗q` — while a left-hand position `(st,(b,d))` carries one. The backward map must merge
`sp,sq → st`, exactly the `⊗` situation, so a monoid on `S` is required; projection policies fail the
unit law as in B3. (I mark this COMPUTED, not PROVED: the "a monoid suffices" converse for `◁` is by
analogy with B3, not separately verified.)

**Why the split (the crown insight).** Framework B `= ` framework A `+` grade-diagonal `+` a collapse
`S×S→S`. The collapse forces a monoid **iff** the object-tensor puts the two state-copies on the
**same** position:
- `+`, `×` **separate** the operands' positions (fibre `Ba+Dc`) — each state-copy stays with its own
  operand, no collision, monoid-free.
- `⊗`, `◁` **merge** positions (fibre `Ba×Dc`, or nested) — the copies collide, forcing a monoid.

Grade-multiplying (A) never collapses `S×S`, so all four descend; `⊗` is *strong* there precisely
because its fibre-product mirrors the `×`-grade-product (Lemma 3.1).

---

## 3. Closed structures

### Theorem C. Workers is **`⊗`-closed** with internal hom `[p,q]_⊗` (that of `Cont`). The
`×`-exponential and the `◁`-coclosure do **not** descend via the base hom; whether any
graded internal hom exists is a precisely-stated open question.

**C1 (`⊗`-closed). PROVED.** For the strong monoidal Workers`⊗`,
```
   Workers_S(r⊗p, q) = Cont(ΔS⊗(r⊗p), q) ≅ Cont((ΔS⊗r)⊗p, q)   [assoc: state sits beside r]
                     ≅ Cont(ΔS⊗r, [p,q]_⊗)                     [⊗-closure of Cont]
                     = Workers_S(r, [p,q]_⊗),
```
natural in `r`, at each grade `S`. The functor `(−⊗p)` on Workers is grade-preserving (tensoring with
the grade-`1` object `p`), so `[p,−]_⊗` is its graded right adjoint. Hom-set counts match exactly
(`256=256`, `65536=65536`, `closed_probe.py`). **Workers`⊗` is a closed monoidal graded category,
internal hom `=` Cont's `[−,−]_⊗`.** ∎

**C2 (`×`-exponential, obstructed). Open, with obstruction.** The state entangles the product factor:
`ΔS⊗(r×p)` is the **state-shared** product `(ΔS⊗r)×_{ΔS}(ΔS⊗p)` (fibre `S×(Br+Bp)`), *not*
`(ΔS⊗r)×p`. Hom-set counts differ sharply — `|Work_S(r×p,q)|` vs `|Cont((ΔS⊗r)×p,q)|` `= 1296:256`,
`5308416:331776`, `256:16` (`closed_probe.py`) — so the naive currying with the base CCC exponential
`q^p` **fails**. Reformulating through `⊗`-closure (`Workers_S(p,q)≅Cont(p,[ΔS,q]_⊗)` since
`ΔS⊗(−)⊣[ΔS,−]_⊗`) and `Cont`'s cartesian closure gives the exact test: a `×`-internal hom `p⇒q`
would have to satisfy
```
   [ΔS,\ p⇒q]_⊗  ≅  ([ΔS,q]_⊗)^p      naturally,
```
i.e. `([ΔS,q]_⊗)^p` must lie in the (essential) image of the right adjoint `[ΔS,−]_⊗`. This is not
generally so; I conjecture Workers is **not** `×`-closed, but a full non-existence proof is a gap.

**C3 (`◁`-coclosure, obstructed). Open, with obstruction.** Same entanglement: `ΔS⊗(r◁p)` spreads
the state over *all* nested positions `(b,d)` of `r◁p`; the duoidal comparison only gives
`ΔS⊗(r◁p)→(ΔS⊗r)◁p` (state on the outer container alone), not an iso, so the coclosure of `Cont`
does not transport. Marked open, obstruction identified.

**The closed fault line coincides with the monoidal one.** State curries **past `⊗`** (which sits it
beside the retained argument) but **not past `×` or `◁`** (which drop it onto the curried argument's
positions) — the very same separate-vs-merge dichotomy as Theorem B.

---

## 4. Summary table

| structure | Framework A (grades ×) | Framework B (shared state) | closed? |
|---|---|---|---|
| `⊗` Dirichlet | **strong** (PROVED) | needs monoid on `S` (PROVED) | **yes**, `[p,q]_⊗` (PROVED) |
| `×` product   | **oplax** (PROVED)  | oplax, free (PROVED) | obstructed / open (witness) |
| `+` coproduct | **oplax** (PROVED)  | **strict** (PROVED)  | (n/a — `+` is not closed in `Cont`) |
| `◁` substitution | oplax (COMPUTED) | needs monoid on `S` (COMPUTED) | obstructed / open |

**Headline.** All four monoidal structures descend to Workers as a `(Set,×)`-graded monoidal
category (grades multiply); `⊗` is the unique **strong** one and the unique **closed** one — the
Dirichlet tensor is where stateful composition is best-behaved, because its fibre-product is exactly
the state grade-product. At the level of a *shared* state register the picture inverts: `+`/`×` are
free while `⊗`/`◁` demand a monoid on the state — the collision of two state-copies on one position.

---

## 5. Grant framing

Workers are stateful agents/processes. Theorem A says the whole agent algebra — parallel `⊗`, choice
`+`, product `×`, and pipelining `◁` — lifts to stateful agents with the state multiplying along
composition, `⊗` cleanly (strong + closed: a genuine internal *stateful function type*
`[p,q]_⊗`), the others laxly. Theorem B is the compositional-correctness content: combining two
agents **on one shared register** is obstruction-free for choice/product but requires the state to be
a *monoid* for parallel/pipelined composition — an algebraic well-formedness condition on shared
state, complementary to the Zappa–Szép `[ω]∈H²` obstruction (directed axis) and the branching `κ/λ`
obstruction (effect–coeffect axis). Three composition modes, three obstruction types
(`connections/three-modes-of-composition.md`); this pins the *state* mode's.

---

## 6. Gaps (precisely stated)

1. **A4 coherence for `◁`.** Interchange verified (256 cases); the oplax associativity/unit pentagon
   of `⊙` for `◁` is not hand-proved. (COMPUTED.)
2. **B4 converse for `◁`.** "A monoid on `S` suffices to build the shared-state `◁`-tensor" is by
   analogy with B3, not separately verified.
3. **C2/C3 non-closure.** The base internal homs do not transport (proved, with counts). Whether a
   *non-canonical* graded internal hom exists for `×` (`([ΔS,q]_⊗)^p ∈ im[ΔS,−]_⊗`?) or `◁` is open.
4. **Lean.** None formalised. A1 (`Φ^⊗` iso) and C1 (`⊗`-currying) are defeq-shaped and are the clean
   follow-on candidates (companion to `StateComonad.lean`).

Everything in Theorems A1–A3, B1–B3, and C1 is **proved** (coordinate arguments + exhaustive finite
verification); A4, B4, C2–C3 are graded honestly above.
