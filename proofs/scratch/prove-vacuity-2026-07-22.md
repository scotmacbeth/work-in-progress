# PROVE scratch — closure-condition vacuity (day 2), 2026-07-22

**Target.** Is every monoidal `(Set,⋆,I)` such that `R_B=(−)⋆B` preserves connected limits
(= polynomial) for all `B`? YES ⟹ Day-tensor closure on Cont is unconditional (vacuous side
condition). NO ⟹ first genuinely non-left-closed convolutional tensor.

Prior session (`2026-07-21-closure-condition-vacuity.md`): reduced to "every monoidal ⋆ on Set
preserves connected limits in each variable"; killed max / support / Sym² candidates; open core =
"balanced ⟹ independent" for elements of `1⋆B`.

---

## NEW REFORMULATION (2026-07-22 morning) — the open core is a single limit-preservation

Work unit-initial (`I=∅`); the retraction lemma (§1.3 prior) handles the injective half for ANY
unit. Fix `B`. Write `R_B(X)=X⋆B`, `η_B := R_B(!): R_B(∅)=∅⋆B → R_B(1)=1⋆B` where `!:∅→1`.
Since `∅` is the unit, `∅⋆B ≅ B` and `η_B` is the "unit-insertion" `B ≅ ∅⋆B → 1⋆B`
(in the coproduct example `A⋆B=A+B` this is `B ↪ 1+B`).

### Def. `u∈1⋆B` is **balanced** iff `(i₀⋆B)(u)=(i₁⋆B)(u)` in `2⋆B` (`i₀,i₁:1→2` the two points).
### Def. `u` is **independent** iff `u∈im(η_B)`.

Independent ⟹ balanced always (both legs factor through `∅→2`). Core Lemma = converse.

### Lemma A (balanced ⟹ constant probes — pure functoriality, no associativity).
If `u` balanced then for EVERY set `X` and every pair of points `f,g:1→X`,
`(f⋆B)(u) = (g⋆B)(u)`.
*Proof.* Pick `h:2→X` with `h∘i₀=f`, `h∘i₁=g`. Then `(f⋆B)(u)=(h⋆B)(i₀⋆B)(u)=
(h⋆B)(i₁⋆B)(u)=(g⋆B)(u)`. ∎

### Lemma B (the Yoneda picture). For any `u∈1⋆B` the family
`Φ_u^X: X → X⋆B, x ↦ (x⋆B)(u)` (x:1→X) is a natural transformation `Id_Set ⇒ R_B` with
`Φ_u^1 = u`. (This is just Yoneda `Id=Set(1,−)`, `Nat(Id,R_B)≅R_B(1)=1⋆B`.)
**`u` balanced ⟺ `Φ_u^X` is a constant map for every nonempty `X`.**
Write `c_X∈X⋆B` for the constant value (`X≠∅`); then `c_1=u` and by naturality
`(h⋆B)(c_X)=c_Y` for every `h:X→Y` (X,Y≠∅). So a balanced `u` yields a **compatible family**
`{c_X∈X⋆B}_{X≠∅}` — i.e. an element of `lim_{X∈Set∖∅} R_B(X)` with 1-component `u`.
Conversely the 1-component of any such element is balanced. Hence

> **{balanced u} = image of the projection `lim_{Set∖∅} R_B ─proj₁→ 1⋆B`.**

### Lemma C (independent = extension across ∅).
`Set` has initial object `∅`, so `lim_{Set} R_B ≅ R_B(∅) = ∅⋆B`, and its `proj₁` is exactly
`η_B`. Hence

> **{independent u} = image of `lim_{Set} R_B ─proj₁→ 1⋆B` = im(η_B).**

Also `lim_{Set∖∅} Id_{Set} = ∅` (a connected limit: `Set∖∅` is connected; any compatible family
`{x_X∈X}` forces, from `1→Y`, `x_Y=`(every point) ⟹ impossible for `|Y|≥2`).

### THE CRUX, restated cleanly.
> **Core Lemma ⟺ `R_B` preserves the connected limit `lim_{Set∖∅} Id = ∅`,**
> i.e. the canonical map `∅⋆B = R_B(∅) → lim_{Set∖∅} R_B` is surjective onto the balanced set
> at component 1. Equivalently: **every compatible family `{c_X∈X⋆B}_{X≠∅}` extends across the
> initial object** (∃ `v∈∅⋆B` with `(∅→X ⋆B)(v)=c_X`).

Injective half is FREE (retraction lemma). The whole open core is this ONE surjectivity /
extension-across-∅. `Set∖∅` is **connected but NOT cofiltered** (parallel `1⇉2` has empty
equalizer), which is exactly why polynomial functors (which preserve it) and non-polynomial ones
(β, `[·≠∅]`, Sym², which have "phantom" families and don't extend) part ways here.

### Why non-poly functors are hard to realize as R_B (the composition constraint).
`R:(Set,⋆,∅)→(End Set,∘,Id)`, `B↦R_B`, is **strong monoidal**: `R_∅=Id`, `R_B∘R_C≅R_{C⋆B}`,
`R_B(∅)=∅⋆B≅B`. A non-poly `R_B` would need e.g. β or `[·≠∅]`; but `R_B(∅)≅B` and `R_∅=Id` and
composition-closure rule these out (β(∅)=∅≠B; `[·≠∅]∘[·≠∅]` not of the form `(−)⋆C`; etc.).
This is the structural reason to believe vacuity, and the target of the associativity attack.

---

## PLAN
1. [background agent] broad brute-force: small associative-unital bifunctors on FinSet (incl.
   non-symmetric, various units), test R_B polynomiality (pullback-of-points lens) + check unit∈{∅,1}
   + verify reformulation (balanced=compatible-family) on examples.
2. [me] Attack the extension-across-∅ using associativity. Lead: the two canonical points
   `p_L,p_R:1→1⋆1` (unit-insertions) let a triple `α` bite on the balanced family.
3. Wide-pullback generalization for full connected-limit preservation (sufficiency), or record gap.

## ATTEMPTS LOG

### Attempt 1 (Yoneda/compatible-family reformulation) — DONE, reframed, injective half free.
See reformulation above. Crux = extension across ∅ (surjective half). Didn't close alone.

### Attempt 2 (associativity bootstrap via p_L) — the unit-insertion point lands trivially in
the independent part; no traction on *detecting* dependence. Dead end as stated.

### Attempt 3 (associator naturality → Lemma D → cartesian square) — ★ BREAKTHROUGH.

Setup: monoidal `(Set,⋆,∅)`, `u∈1⋆B` balanced. `η_C := (!⋆C)∘λ^{-1}: C ≅ ∅⋆C → 1⋆C`
(`!:∅→1`), a natural transformation `η: Id ⇒ 1⋆(−)`. Independent = `u∈im(η_B)`.

**Two canonical points of `1⋆1`:** `p_L: 1≅∅⋆1 --(!⋆1)--> 1⋆1` (left unit-insertion) and
`p_R: 1≅1⋆∅ --(1⋆!)--> 1⋆1` (right unit-insertion).

**Lemma D.** *For balanced `u∈1⋆B`:  `η_{1⋆B}(u) = (1⋆η_B)(u)` in `1⋆(1⋆B)`.*
*Proof.* Three coherence facts (all standard Mac Lane, functoriality only):
- (A) `α_{1,1,B}∘(p_L⋆B) = η_{1⋆B}` — naturality of `α_{−,1,B}` in slot 1 along `!:∅→1`;
  top row `α_{∅,1,B}` = id under unitors (left-unit/λ associator coherence).
- (B) `α_{1,1,B}∘(p_R⋆B) = 1⋆η_B` — naturality of `α_{1,−,B}` in slot 2 along `!:∅→1`;
  top row `α_{1,∅,B}` = id under unitors (TRIANGLE axiom).
- (C) balanced ⟹ `(p_L⋆B)(u)=(p_R⋆B)(u)` — Lemma A with the two points `p_L,p_R:1→1⋆1`.
Apply `α_{1,1,B}` to (C) and use (A),(B):  `η_{1⋆B}(u) = (1⋆η_B)(u)`. ∎
[Verified rigorously; each step re-derived. Uses associativity essentially — this is why the
non-associative support tensor evades it: Lemma D FAILS there (η_{1⋆B}(•)≠(1⋆η_B)(•)).]

**The finish.** Consider the naturality square of `η: Id ⇒ 1⋆(−)` at the morphism
`η_B: B → 1⋆B`:
```
     B   --η_B-->   1⋆B
    η_B |             | 1⋆η_B
    1⋆B --η_{1⋆B}--> 1⋆(1⋆B)
```
It commutes (naturality of η). Lemma D says `(u,u)` (with `u` in BOTH copies of `1⋆B`) lies in
the pullback `P = {(x,z): η_{1⋆B}(x)=(1⋆η_B)(z)}`.

> **If this square is a PULLBACK, then `B ≅ P` via `v↦(η_B v, η_B v)`, so `(u,u)=(η_B v,η_B v)`
> for some `v∈B`, i.e. `u = η_B(v) ∈ im(η_B)` — INDEPENDENT. Core Lemma done.**

Square = pullback ⟺ **`η: Id ⇒ 1⋆(−)` is a cartesian natural transformation** (at least at this
square). CHECKED by hand: pullback for coproduct AND for support (support's • is simply not in
`P` because Lemma D fails there — fully consistent). So the picture is:
- square-is-pullback: holds structurally (no associativity needed — property of η/unitors);
- Lemma D: needs associativity (fails for non-monoidal support);
- balanced ⟹ (D) ⟹ `(u,u)∈P` ⟹ (pullback) ⟹ independent. ∎ (modulo square-pullback lemma)

**REMAINING PIECE: prove `η: Id ⇒ 1⋆(−)` is cartesian (this one square is a pullback).**
This is now THE crux and it's clean/finite-flavoured. If it FAILS for some exotic ⋆ (while D
holds) ⟹ that's the counterexample. Testing + abstract proof next.

**Alternative finish (simpler, needs B≠∅):** if `η_B: B→1⋆B` is a split mono with retraction
`r:1⋆B→B`, apply `1⋆r` to Lemma D and use naturality of η in its subscript:
`(1⋆r)∘η_{1⋆B} = η_B∘(∅⋆r)` (naturality of η at r), so
`u = (1⋆r)(1⋆η_B)(u) = (1⋆r)(η_{1⋆B}(u)) = η_B((∅⋆r)(u)) ∈ im η_B`. Done.
So Core Lemma also follows from: **η_B splits for nonempty B** (B=∅ trivial: R_∅=Id). Two routes.

### Attempt 3, continued — REDUCTION TO ★' (⋆ preserves one small pullback). ★★

**Cartesian criterion (rigorous).** For `η: Id ⇒ G` (`G=1⋆(−)`), η is cartesian ⟺ for every
set `C` the naturality square at `!_C:C→1` is a pullback. [Proof in notebook: given the `!_C`,
`!_D` squares are pullbacks, the square at any `f:C→D` is a pullback — uses `!_D∘f=!_C`,
θ mono, and `G(!_D)θ_D=θ_1`. Airtight.]

**The `!_C`-square is the bifunctor image of a Set²-pullback.** Under unitors, η's naturality
square at `!_C` is exactly `⋆` applied to the square
```
(∅,C) --(id,!_C)--> (∅,1)
(!,id)|                | (!,1)
(1,C) --(id,!_C)--> (1,1)
```
in `Set²`. And `(∅,C)` IS the pullback of `(1,C)→(1,1)←(∅,1)` in `Set²` (componentwise:
`∅=1×_1∅`, `C=C×_1 1`). So:

> **★' (THE WHOLE CRUX).** For every set `C`, the bifunctor `⋆` **preserves** the pullback
> `(∅,C) = (1,C) ×_{(1,1)} (∅,1)`, i.e. the canonical map `∅⋆C → (1⋆C) ×_{1⋆1} (∅⋆1)` is a
> bijection. Equivalently: `η_C:C→1⋆C` is mono and `im(η_C) = (1⋆!_C)^{-1}(p_L)`,
> where `p_L = η_1(∗) = im(∅⋆1→1⋆1) ∈ 1⋆1`.

**MASTER CHAIN.** ★' (∀C) ⟹ η cartesian ⟹ the `η`-naturality square at `η_B` is a pullback
⟹ [+ Lemma D, which needs associativity] balanced `u` ⟹ `(u,u)∈` that pullback ⟹ `u∈im η_B`
= independent. **Core Lemma (point-pullback preservation) proved.**

Checked by hand: ★' holds for coproduct AND support (`im η_C` = the C-fibre over p_L both
times), even though support fails Lemma D. So the two ingredients are cleanly separated:
- **★'** = a pullback-preservation property of the bifunctor+unitors (maybe needs assoc, maybe
  not — TEST);
- **Lemma D** = the associativity input.

## ★★★ RESOLVED — VACUITY IS FALSE. Counterexample: the COLLAPSE TENSOR.

`A ⋆ B := B if A=∅ ; A if B=∅ ; 1 (terminal) if A,B≠∅.` Unit ∅, symmetric.
- Monoidal: verified (bifunctor id+comp, natural associator, pentagon, triangle, unitors,
  symmetric) exhaustively to size 3 (`collapse_hostile2.py`) + emptiness-pattern genericity
  proof (every coherence instance is a diagram of unique-maps-to-1 or single-factor functorial
  maps — commutes). Independently found + verified by search agent (`vacuity2/collapse_verify.py`).
- **`R_2 = (−)⋆2` non-polynomial:** `R_2(∅)=∅⋆2=2` (unit law) but `R_2(1)=1⋆2=1`. Every
  polynomial `F=Σ_i y^{a_i}` has `|F(∅)|=#{i:a_i=∅} ≤ #{i}=|F(1)|`; here `2>1`. ∎ (one line)
- So by 07-15 biconditional, `⊙_collapse` on Cont is **convolutional but NOT left-closed** —
  the FIRST such. **convolutional ⊋ left-closed.** Answers Neil's "lucky with ⊗,×": YES.

**The Lemma D / ★' framework PREDICTED this.** Collapse is associative ⇒ Lemma D holds; but
`η_2:∅⋆2=2→1⋆2=1` is NON-INJECTIVE ⇒ ★' FAILS (agent 2b's "η non-injective / oversized fibre"
failure mode). My master chain needs ★'; collapse violates exactly ★'. Mechanism = **the unit
insertion η_B is not injective ("multiplying by 1 shrinks")** — a NEW mechanism, distinct from
support's phantom-separator (07-21) and orthogonal to the retraction lemma (which only concerned
elements of 1⋆B, never η_B's injectivity). Consistency: support satisfies ★' but fails Lemma D
(non-assoc); collapse satisfies Lemma D but fails ★' — the two ingredients are independent and
each has its own counterexample witness.

REFINED OPEN QUESTION (forward): characterize the left-closed convolutional tensors = monoidal
⋆ on Set preserving connected limits in each variable. Necessary: η_B injective (⋆ "taut"/mono-
preserving). Is taut + point-pullback (★') sufficient? The Lemma D/★' analysis is the tool.

### (superseded) NEXT
- [agent B, focused] Test across many ⋆ (associative: +, ×[unit 1 analog], ∨_S, join;
  non-assoc unital: support, random): does ★' hold? does Lemma D hold (assoc only)? Try to BREAK
  ★' with a unital non-assoc bifunctor — if ★' can fail without assoc, it needs assoc; if it
  holds for a ★' that then combines with a *false* Lemma D... Report. Also WIDE version of ★'
  (preserve `(∅,C)=(J,C)×_{(J,1)}(∅,1)` for `|J|` arbitrary → wide pullback).
- [me] prove ★' for monoidal ⋆ (may use associativity). This is now a concrete pullback-
  preservation lemma — the entire vacuity question modulo the wide/cofiltered generalization.
