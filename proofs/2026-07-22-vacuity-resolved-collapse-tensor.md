# Closure-condition vacuity is FALSE: the collapse tensor, a non-left-closed convolutional tensor

MacBeth — 2026-07-22. Deep-work session. **Resolves** the open node `condition-vacuity` of
`registry/closed-day-structures.json` (flagged to Neil 2026-07-21).

**Verdict: NO (vacuity fails).** There is a symmetric monoidal structure `(⋆, ∅)` on `Set` —
the **collapse tensor** — for which `R_2 = (−)⋆2 : Set → Set` is **not** a polynomial functor.
Hence its Day convolution `⊙_⋆` on `Cont` is a **convolutional monoidal structure that is not
left-closed** — the first such. So on `Cont`, **convolutional ⊋ left-closed**: the side-condition
of the 2026-07-15 uniform-closure biconditional is *not* vacuous, and Neil's scepticism ("we were
lucky with `⊗` and `×`") is vindicated — closure is a genuine, non-automatic condition.

---

## 0. The question (from `state/PROVE.md`)

The 2026-07-15 biconditional: for a Day tensor `⊙_⋆` on `Cont ≅ Fam(Set^op)` built from a
monoidal `(⋆,I)` on `Set`,
> `(Cont, ⊙_⋆)` is left-closed ⟺ `R_B := (−)⋆B` is polynomial (preserves connected limits /
> wide pullbacks) for every set `B`.

**Target.** Does there exist a monoidal `(⋆,I)` on `Set` with `R_B` *not* polynomial for some
`B`? A YES exhibits the first genuinely non-left-closed convolutional tensor.

**Answer: YES.** Below.

---

## 1. The collapse tensor

**Definition 1.1.** Define `⋆ : Set × Set → Set`, with strict unit `∅`, by
```
        ⎧ B      if A = ∅          (strict left unit)
 A ⋆ B = ⎨ A      if B = ∅          (strict right unit)
        ⎩ 1      if A ≠ ∅ and B ≠ ∅  (a fixed one-point set — "collapse")
```
(The two unit clauses agree at `A=B=∅`, giving `∅`.) On morphisms `f:A→A'`, `g:B→B'`, define
`f ⋆ g : A⋆B → A'⋆B'` by:
```
   • A' , B' both ≠ ∅   ⟹  A'⋆B' = 1 , and  f⋆g  is the unique map to 1;
   • A' = ∅ (so A=∅, A'⋆B'=B')  ⟹  f⋆g = g : B → B';
   • B' = ∅ (so B=∅, A'⋆B'=A')  ⟹  f⋆g = f : A → A'.
```
(These are exhaustive and consistent: `A≠∅ ⟹ A'≠∅`, since a function out of a nonempty set has
nonempty image; so `A⋆B=1` forces `A'⋆B'=1`.)

**Proposition 1.2.** `⋆` is a functor `Set² → Set` (a bifunctor).

*Proof.* Identities: `id_A ⋆ id_B` is `id_B`, `id_A`, or the identity of `1` in the three cases —
the identity of `A⋆B` each time. Composition: given `A --f--> A' --f'--> A''` and `B --g--> B' --g'-->
B''`, we check `(f'⋆g')∘(f⋆g) = (f'f)⋆(g'g)`. Split on the emptiness of `A'', B''` (which, with
monotonicity of nonemptiness, determines all intermediate cases):
- `A''≠∅, B''≠∅`: the target is `1`; both sides are the unique map to `1`. ✓
- `A''=∅` (so `A'=A=∅`, all left-unit): both sides are `g'∘g`. ✓
- `B''=∅` (so `B'=B=∅`): both sides are `f'∘f`. ✓
The only subtlety — a map that turns an empty factor nonempty (`∅→A''≠∅`) — lands in the first
case, where every composite is *the* unique map to `1`, so associativity of composition is
automatic. ∎

**Proposition 1.3.** `(⋆, ∅)` is a symmetric monoidal structure on `Set`.

*Proof.* Unitors are identities (strict unit, Def. 1.1). The **associator**
`α_{A,B,C} : (A⋆B)⋆C → A⋆(B⋆C)` is the evident bijection:
- if two or more of `A,B,C` are nonempty, both sides equal `1`, and `α` is the unique
  (iso) map `1→1`;
- if exactly one factor is nonempty, both sides are a copy of that factor (the other two being
  units), and `α` is the identity on it;
- if all are empty, both sides are `∅`.
The **braiding** `β_{A,B}:A⋆B→B⋆A` is the identity on the surviving factor (or on `1`).

*Coherence (pentagon, triangle, hexagon, naturality) holds by an emptiness-pattern analysis.*
Every coherence datum depends only on the emptiness pattern of its arguments, and because
functions preserve nonemptiness, every arrow in every coherence diagram is one of:
(a) the **unique** map into a terminal `1` (whenever ≥2 relevant factors are nonempty, so the
node is `1`), or (b) a functorial map on the **single** surviving factor (whenever ≤1 factor is
nonempty, the unit-copy regime). Diagrams of type (a) commute because `1` is terminal; diagrams
of type (b) commute because they are the coherence of the trivial (unit-only) structure, i.e.
plain functoriality of one factor. Concretely, for **associator naturality** at `(f,g,h)`:
if ≥2 of `A,B,C` are nonempty the whole square lives among terminal objects (unique maps,
commutes); if ≤1 is nonempty, either no slot is filled (the square is the functorial action of
the single surviving factor, `α=id` on both rows) or a slot is filled from `∅` (both legs become
the unique map to `1`). The **pentagon** (four factors, 16 patterns) and **triangle** are
identical: any node multiplying ≥2 nonempty factors is `1`; the rest is unit coherence.

This is a complete finite proof. It was cross-checked exhaustively on all sets of size ≤ 3
(`scratch/collapse-tensor/collapse_hostile2.py`): bifunctor (identity + composition),
associator a natural bijection, **pentagon**, **triangle**, unitor naturality, and braiding
involutivity all PASS — with a size-2 factor present to witness the non-degenerate "unit-copy of
a ≥2-element set" and the non-injective collapse `2→1`. ∎

> **Referee's note (why this is not the support tensor).** The support tensor
> `A⊔B⊔{•}` (2026-07-21) has *cardinality*-associativity but admits **no natural associator**
> (its separator `•` cannot record which pair it separates — an exhaustive no-canonical-leaf
> search found zero natural associators). The collapse tensor is different: whenever a collapse
> occurs the value is a *single point*, carrying no provenance to be inconsistent about, so the
> naturality that killed `support` is vacuous here. I re-verified this myself with the correct
> functorial action — the delicate `∅→nonempty` maps, where a first naive implementation (and
> the support tensor) breaks — and both naturality and pentagon hold.

---

## 2. `R_2` is not polynomial

**Proposition 2.1.** `R_2 := (−)⋆2 : Set → Set` is not a polynomial (familially representable)
functor; equivalently it does not preserve connected limits.

*Proof.* By the strict left unit, `R_2(∅) = ∅⋆2 = 2`, so `|R_2(∅)| = 2`. Since `1,2 ≠ ∅`,
`R_2(1) = 1⋆2 = 1`, so `|R_2(1)| = 1`. Every polynomial functor `F = Σ_{i∈I} y^{a_i}` satisfies
`|F(∅)| = #{i : a_i = ∅} ≤ #I = |F(1)|`. Here `2 = |R_2(∅)| > |R_2(1)| = 1` — impossible.

Sharper: `R_2` sends the monomorphism `!:∅↪1` to `R_2(!) : 2 → 1`, which is **not** a
monomorphism. A polynomial functor preserves monos (each `y^{a}` does, and coproducts of monos
are mono). So `R_2` is not polynomial; it already fails to preserve the pullback of the two
points `1 ⇉ 2` (that pullback is `∅`, but the comparison `R_2(∅)=2 → \{u∈1⋆2 : (i_0⋆2)u=(i_1⋆2)u\}
= 1` is the non-injective `2→1`). ∎

**Corollary 2.2.** `⊙_⋆` (the Day convolution of the collapse tensor, `p ⊙_⋆ q =
Σ_{(s,t)} y^{p[s]⋆q[t]}`; Theorem A of `2026-07-14-day-family-classification.md`) is a
**convolutional monoidal structure on `Cont` that is not left-closed**. By the 2026-07-15
biconditional, non-polynomiality of `R_2` is exactly the failure of the internal hom
`[y², −]_{⊙_⋆}` to exist in `Cont`. So `⊙_⋆` witnesses **convolutional ⊋ left-closed**. ∎

---

## 3. Why every prior counterexample search missed it, and what the mechanism is

The 2026-07-21 session killed three candidates (`max`, `support`, `Sym²`) and isolated an
"open core" about a *phantom extra element* (support's `•`). It missed the collapse tensor
because collapse fails polynomiality by a **different mechanism**:

> **The unit insertion `η_B : B ≅ ∅⋆B → 1⋆B` is not injective.** Equivalently
> "left-multiplication by `1` can *shrink*": `|1⋆B| < |B|`.

For collapse, `η_2 : 2 → 1⋆2 = 1`. The support mechanism *adds* a phantom balanced element
(`|1⋆B|` too big); the collapse mechanism *deletes* structure (`|1⋆B|` too small). The retraction
lemma of 2026-07-21 §1.3 concerned only elements of `1⋆B` and never asserted `η_B` injective, so
it is untouched — it simply does not see this mechanism.

**The `η`-cartesian analysis (this session) locates counterexamples exactly.** Writing
`η : Id ⇒ 1⋆(−)` for the unit insertion, I proved two clean facts for monoidal `(⋆,∅)`:

- **Lemma D (associativity input).** If `u∈1⋆B` is *balanced* (`(i_0⋆B)u=(i_1⋆B)u` in `2⋆B`),
  then `η_{1⋆B}(u) = (1⋆η_B)(u)` in `1⋆(1⋆B)`. *Proof:* the two unit-insertion points
  `p_L,p_R:1→1⋆1` satisfy `(p_L⋆B)u=(p_R⋆B)u` (balanced ⟹ coequalized by any two points), and
  `α∘(p_L⋆B)=η_{1⋆B}`, `α∘(p_R⋆B)=1⋆η_B` by the left-unit and triangle coherences. ∎ [This uses
  associativity essentially; the non-associative support tensor *fails* Lemma D — its `•` is the
  unique violator.]
- **★' (structural input).** `balanced ⟹ independent` (`R_B` preserves the point-pullback)
  follows once the naturality squares of `η` are pullbacks, i.e. **`η` is a cartesian natural
  transformation** — equivalently `⋆` preserves the corner pullback `(∅,C)=(1,C)×_{(1,1)}(∅,1)`.
  This is *independent of associativity* and can FAIL: it fails iff `η` is non-cartesian
  (non-injective, or oversized fibre).

**The dichotomy is exact.** A monoidal counterexample needs Lemma D to hold (it does, by
associativity) *and* ★' to fail. Collapse is precisely this: associative, but `η_2` non-injective
so ★' fails. Support is the mirror non-example: ★' holds but Lemma D fails (non-associative), so
support is *not* monoidal and not a counterexample. The two obstructions are independent, each
with its own witness — which is why a single-mechanism search missed the collapse tensor.

(Verification of Lemma D, ★', and the failure modes across `+, ∨_S, join, support, collapse` and
an exhaustive `(G,η)` sweep: `scratch/vacuity2b/`, `scratch/collapse-tensor/star_prime_probe.py`.)

---

## 4. What survives, and the refined question

- The 2026-07-15 **biconditional is unaffected** — it holds either way; only the vacuity of its
  side-condition was at issue, and that is now settled: **not vacuous.**
- Theorem A/B/C of the Day-family classification are unaffected.
- The three closed examples remain closed: `⊗ (⋆=×)`, `× (⋆=+)`, `▷_S (⋆=∨_S)` all have `R_B`
  polynomial (linear in each variable), i.e. `η_B` injective and `⋆` connected-limit-preserving.

**Refined open question (the right next target).** *Characterize* the left-closed convolutional
tensors, i.e. the monoidal `(⋆,I)` on `Set` with `R_B` polynomial for all `B` (= `⋆` preserves
connected limits in each variable). Necessary conditions now in hand:
1. `η_B` injective for all `B` (`⋆` is *taut* / mono-preserving; kills collapse);
2. `R_B` preserves the point-pullback (★'/`η` cartesian);
plus the wide-pullback / cofiltered analogues for full polynomiality. **Is taut + ★' + Day
sufficient?** The Lemma D / ★' machinery of §3 is the tool. Conjecture: the closed ones are
exactly the "sum-of-products in each variable" tensors — `×`, `+`, `∨_S`, and their combinations —
i.e. Day convolutions of monoidal `(Set,⋆)` whose `⋆` is itself polynomial. (The collapse tensor
is the minimal witness that some monoidal `⋆` is *not*.)

---

## 5. Grade discipline
- `proved`: Prop. 1.2 (bifunctor), Prop. 1.3 (collapse tensor is symmetric monoidal — finite
  emptiness-pattern proof + exhaustive size-≤3 check), Prop. 2.1 (`R_2` non-polynomial, one-line
  cardinality), Cor. 2.2 (non-left-closed convolutional tensor), Lemma D.
- `computed`: ★' holds/fails patterns; the auxiliary `(G,η)` sweep; independent search-agent
  reconstruction of the collapse tensor (`vacuity2/collapse_verify.py`).
- `conjecture`: the §4 characterization of left-closed convolutional tensors.
- The novelty claim is only the **yes/no on vacuity** (a remark-level refinement of the
  Thm-A landscape); the biconditional and the three concrete closures are prior/own art.

## 6. Verification index
- `scratch/collapse-tensor/collapse_hostile2.py` — collapse tensor: bifunctor (id+comp),
  natural associator, **pentagon**, **triangle**, unitors, symmetric braiding — all PASS to
  size 3; `R_2(∅)=2 > 1 = R_2(1)`.
- `scratch/vacuity2/collapse_verify.py` (search agent) — independent reconstruction + monoidality
  verification of the same tensor; brute-force census that surfaced it from the size table
  `[[0,1,2],[1,1,1],[2,1,1]]`.
- `scratch/vacuity2b/` (focused agent) — Lemma D separates associative/non-associative (support's
  `•` sole violator); ★' = cartesianness of `η`, associativity-independent, fails for non-cartesian
  `η` (explicit `(G,η)` witness); wide-pullback tests.
- `scratch/collapse-tensor/star_prime_probe.py` — ★' holds for `+, join, ∨_S, support` and
  adversarial non-poly bi-unital bifunctors; the collapse tensor is where it breaks (`η_2` non-mono).
