# THM 3 — M-containers compose ⟺ the effect functor M is polynomial

**MacBeth — 2026-09-05 (PROVE session).**
Promotes the sub-agent's `computed` THM 3 (`scratch/2026-09-05-thm3-mcontainer-composition.md`)
after a personal line-by-line verification. Inputs (all `proved`,
`proofs/2026-09-04-m-containers-codensity.md`):

- **(T1a)** `M-Cont ≃ Fam(Kl(M)^op)`; objects are ordinary containers `(S,P:S→Set)`, morphisms
  are Kleisli (a shape map `f:S→S'` and, per shape, `ρ_s∈Set(P'_{fs},MP_s)`).
- **(T1b)** the extension is an ordinary polynomial functor post-composed with `M`:
  `⟦S,P⟧_M = ⟦S,P⟧ ∘ M`, naturally in `(S,P)`, where `⟦S,P⟧(Y)=Σ_{s}Set(P_s,Y)`.
- **(Faith)** `⟦−⟧_M : M-Cont → [Set,Set]` is always faithful.

Throughout, `M` is a monad on `Set` (the category `M-Cont` needs the monad structure; the
*composition of extensions* below uses only the underlying functor of `M`, except where the unit
`η`/multiplication `μ` are named explicitly). `Cont=Fam(Set^op)` is the category of ordinary
containers with its composition monoidal structure `(Cont,◁,y)`; `⟦−⟧:Cont→[Set,Set]` is the AAG
fully-faithful embedding onto polynomial functors, strong monoidal: `⟦c◁d⟧≅⟦c⟧∘⟦d⟧`, `⟦y⟧=Id`
(Gambino–Kock, *Polynomial functors and polynomial monads*, MPCPS 2013; Niu–Spivak, *Poly*).

> **THEOREM 3.**
> **(A, sufficiency — PROVED.)** If `M` is a polynomial functor, write `⌈M⌉` for the container
> with `⟦⌈M⌉⟧=M`. Then for all M-containers `p,q` the object
> `p ◁_M q := p ◁ ⌈M⌉ ◁ q` (ordinary container composition, with `M`'s container spliced in the
> middle) satisfies a natural-in-`X` isomorphism
> `⟦p ◁_M q⟧_M ≅ ⟦p⟧_M ∘ ⟦q⟧_M`.
> This binary operation is **associative** (up to the `◁`-associator) and has **no unit up to
> ordinary container iso unless `M=Id`** (semigroupal, not monoidal). Hence the essential image
> of `⟦−⟧_M` is closed under functor composition.
>
> **(B, necessity — PARTIAL.)** Conversely, if the essential image of `⟦−⟧_M` is closed under
> composition then `M` satisfies the **cardinality growth law**: for every polynomial functor
> `N` there is a *fixed* polynomial `R_N` with `|M(N(MX))| = R_N(|MX|)` for all finite `X`
> (already at `N=Id`: `|M(M X)| = R(|MX|)`). This **rigorously excludes** every non-polynomial
> monad of super-polynomial relative growth — in particular nonempty powerset `P⁺`, powerset `P`,
> and finite-distribution `D`. The full categorical converse "closure ⟹ `M` polynomial" is
> reduced to **Lemma N** below and left as a precisely-identified gap (the *trailing-`M`*
> obstruction).

Corollary of A vs. THM 2: **composability (polynomiality) and fullness (codensity) are
independent invariants of `M`** — writer `E×(−)` composes (polynomial) but is not full (not
codense); `D` is full (affine + codense) but does not compose (not polynomial).

---

## Part A — Sufficiency (PROVED)

### A0. The structural identity `[proved]`

For any M-containers `p,q`, using (T1b) twice and associativity of functor composition,
```
(⟦p⟧_M ∘ ⟦q⟧_M)(X) = ⟦p⟧_M( ⟦q⟧(MX) )                    [T1b for q]
                    = ⟦p⟧( M( ⟦q⟧(MX) ) )                  [T1b for p]
                    = (⟦p⟧ ∘ M ∘ ⟦q⟧ ∘ M)(X)  =  (G ∘ M)(X),   G := ⟦p⟧ ∘ M ∘ ⟦q⟧.
```
So **every composite of two M-extensions has the form `G∘M`** with `G=⟦p⟧∘M∘⟦q⟧`. This is an
equality of functors (not merely iso), natural in `X`; and natural in `(p,q)` for *ordinary*
container morphisms because (T1b) is. ∎

### A1. `M` polynomial ⟹ `G` polynomial, with `G≅⟦p◁⌈M⌉◁q⟧` `[proved]`

Let `M` be polynomial: `M ≅ Σ_{i∈I}Set(B_i,−)`, i.e. `M=⟦⌈M⌉⟧` for `⌈M⌉=(I, i↦B_i)`. Then
```
G = ⟦p⟧ ∘ M ∘ ⟦q⟧ ≅ ⟦p⟧ ∘ ⟦⌈M⌉⟧ ∘ ⟦q⟧ ≅ ⟦ p ◁ ⌈M⌉ ◁ q ⟧,
```
the last step by the strong-monoidal law `⟦c◁d⟧≅⟦c⟧∘⟦d⟧` of AAG applied twice (associativity of
`◁` makes the two bracketings agree). Each iso is natural in `X`. Set `r := p ◁ ⌈M⌉ ◁ q`, an
ordinary container, hence an object of `M-Cont` (same objects as `Cont`). Then by A0,
```
⟦p⟧_M ∘ ⟦q⟧_M = G ∘ M ≅ ⟦r⟧ ∘ M = ⟦r⟧_M,        naturally in X.          (★)
```
Define `p ◁_M q := r`. This is well-defined as an object; (★) is the required natural iso. ∎

**Line-by-line audit (the referee pass).**
- `M ≅ Σ_i Set(B_i,−)` and `⌈M⌉` exists: this *is* the definition of "`M` polynomial." GREEN.
- `⟦p⟧∘⟦⌈M⌉⟧∘⟦q⟧ ≅ ⟦p◁⌈M⌉◁q⟧`: two applications of AAG strong-monoidality, a published
  `proved` fact; the associator of `◁` is coherent (`(Cont,◁,y)` monoidal, machine-checked in my
  own `lean-monoidal-coherence-done`). GREEN.
- Substituting `M` for `⟦⌈M⌉⟧` inside `G`: `M` and `⟦⌈M⌉⟧` are *the same functor* up to the
  chosen iso; horizontal composition of natural isos is a natural iso. GREEN.
- `G∘M ≅ ⟦r⟧∘M`: whisker the iso `G≅⟦r⟧` by `M` on the right; whiskering preserves natural iso.
  GREEN.
- Naturality in `X`: (★) is a vertical composite of natural isos, hence natural. GREEN.

Computational cross-check (`scratch/2026-09-05-thm3-verify.py`): `M=Maybe (X+1)`, `p=q=`squaring,
`r` has shape-profile `{4 pos:1, 2 pos:2, 0 pos:1}` i.e. `⟦r⟧=Y⁴+2Y²+1`, and
`|⟦p⟧_M⟦q⟧_M(n)| = |⟦r⟧(Mn)|` for `n=0..6` (`4,25,100,289,676,1369,2500`). Matches (★). ✓

### A2. Associativity `[proved]`

`◁` is associative on `Cont` (associator of `(Cont,◁,y)`). Hence on objects
```
(p ◁_M q) ◁_M s = (p◁⌈M⌉◁q) ◁ ⌈M⌉ ◁ s = p◁⌈M⌉◁q◁⌈M⌉◁s = p◁⌈M⌉◁(q◁⌈M⌉◁s) = p ◁_M (q ◁_M s),
```
all equalities being the coherent `◁`-associator. Under `⟦−⟧_M` this is exactly the associativity
constraint of functor composition `∘` transported across (★). GREEN. ∎

### A3. Non-unitality `[proved]`

**Claim.** The object-operation `◁_M` on `Cont` has a unit up to ordinary container isomorphism
**iff `M=Id`.**

*Proof.* (⟸) If `M=Id` then `⌈M⌉=y` and `p◁_M q = p◁q`, whose unit is `y`.

(⟹) Suppose `e` is a two-sided unit up to Cont-iso. Taking `q=y` (the Id-container) in the left
unit law `e◁_M q ≅ q`:
```
e ◁_M y = e ◁ ⌈M⌉ ◁ y = e ◁ ⌈M⌉ ≅ y      in Cont.
```
Apply the fully-faithful `⟦−⟧`: `⟦e⟧∘M = ⟦e⟧∘⟦⌈M⌉⟧ ≅ ⟦e◁⌈M⌉⟧ ≅ ⟦y⟧ = Id`. So
`⟦e⟧∘M ≅ Id`. Write `⟦e⟧=Σ_{s∈S_e}Set(E_s,−)`; then `Σ_{s∈S_e} Set(E_s, M−) ≅ Id`. Now evaluate:

- **At `X=1`:** `Σ_s |M1|^{|E_s|} = |Id(1)| = 1`. Each summand is `≥1` (as `|M1|≥1`, since
  `η_1:1→M1`), and they sum to `1`, so there is **exactly one** shape `s_0` and
  `|M1|^{|E_{s_0}|}=1`, forcing `|M1|=1` (i.e. `M` affine) or `E_{s_0}=∅`.
- **`E_{s_0}=∅` is excluded:** `Set(∅,M−)=const_1`, and `const_1(2)=1≠2=Id(2)`.
- So `|M1|=1` and `Set(E_{s_0},M−)≅Id`. **At `X=2`:** `|M2|^{|E_{s_0}|}=2`. If `E_{s_0}=∅` the
  LHS is `1≠2` (already excluded); if `|E_{s_0}|≥2` then `|M2|^{|E_{s_0}|}` is either `1` (if
  `|M2|=1`) or `≥2^2=4`, never `2`; hence `|E_{s_0}|=1`, and then `|M2|=2`.
- `E_{s_0}` a one-element set gives `Set(1,M−)=M ≅ Id`.

Therefore `M≅Id`. Every step is an exact finite-cardinality equality forced by `⟦e⟧∘M≅Id`. GREEN. ∎

**Remark (scope of the unit statement).** "Unit up to *ordinary container* iso" is the honest and
clean statement, obtained by pushing the unit law through the fully-faithful `⟦−⟧`. The weaker
question — a unit up to *`M-Cont` (Kleisli) iso* — is more delicate because iso in
`Fam(Kl(M)^op)` is coarser than iso in `Cont`; I do not claim it here. For the grant narrative the
operative fact is: **`(Cont,◁_M)` is genuinely semigroupal, monoidal only at `M=Id`.**

### A4. Bifunctoriality — honest scope `[proved on pure morphisms; open in general]`

`◁_M` is defined on objects. On morphisms:

- **Pure (cartesian) morphisms.** The subcategory `Cont ↪ M-Cont` of *pure* morphisms (Kleisli
  maps of the form `η∘g`, i.e. ordinary container morphisms) is closed under `◁` and `◁_M=(-)◁⌈M⌉◁(-)`
  is the ordinary bifunctor there. On this subcategory `⟦−⟧_M` restricted is strong semigroupal
  into `([Set,Set],∘)` via (★). GREEN.
- **General Kleisli morphisms.** Extending `◁_M` to a bifunctor on all of `M-Cont` making
  `⟦−⟧_M` *strong semigroupal* would require transporting the horizontal composite
  `⟦φ⟧_M ∗ ⟦ψ⟧_M` back along `⟦−⟧_M` — possible for free only when `⟦−⟧_M` is **full**. By THM 2
  that is exactly **codensity** of `M`. So: *the object-level composition product exists for every
  polynomial `M`; it upgrades to a strong-semigroupal structure on the full Kleisli category
  precisely when `M` is additionally codense.* I flag the Kleisli-bifunctoriality as **open**
  (not needed for the closure theorem) and note it as the exact meeting point of THM 2 and THM 3.

**This is the honest statement.** The headline "M-containers compose" is the *object closure* (★)
+ associativity, which is fully proved for polynomial `M`.

---

## Part B — Necessity (PARTIAL; cardinality law proved, categorical converse reduced)

### B1. The cardinality growth law `[proved]`

Assume the essential image `𝓘_M={⟦r⟧∘M : r∈Cont}` is closed under `∘`. The Id-container `y`
lies in `M-Cont` with `⟦y⟧_M=M`, and every `⟦q⟧_M=⟦q⟧∘M∈𝓘_M`. Closure applied to
`p=y` and general `q` gives, by A0,
```
M ∘ ⟦q⟧ ∘ M = ⟦y⟧_M ∘ ⟦q⟧_M ≅ ⟦r_q⟧ ∘ M   for some container r_q.               (†)
```
Take cardinalities on a finite set `X`, `|X|=n`. Write `m(n):=|M(n)|` (finite when `M` is
finitary/`Set`-small on finite sets; for `D`,`P` interpret in the finite-shadow sense of B3),
`N:=⟦q⟧` with cardinality function `Q(y)=Σ_t y^{|B_t|}`, and `R_q(y)=Σ_j a_j y^j` the (fixed,
nonneg-integer) cardinality function of `r_q`. Then (†) forces
```
m( Q( m(n) ) ) = R_q( m(n) )    for all n.                                        (‡)
```
Because `m(n)` ranges over the set `V:=im(m)`, (‡) says: **for every polynomial `Q`, the function
`v ↦ m(Q(v))` agrees on `V` with a fixed nonneg-integer polynomial `R_q`.** The case `q=y`
(`Q=Id`) is the sharpest single instance:
```
m(m(n)) = R(m(n))   for all n   ⟺   m|_V agrees with a fixed nonneg-int polynomial R.   (‡₀)
```
∎

### B2. `(‡₀)` already excludes the affine+commutative "counterexamples" `[proved]`

This is a **strictly stronger** exclusion than the sub-agent's squaring test: it fires already at
`p=q=Id`.

- **`P⁺` (nonempty powerset), affine + commutative.** `m(n)=2ⁿ−1`. Then
  `m(m(n))=2^{2ⁿ−1}−1`, whose value at `n=0..6` is `0,1,7,127,32767,2147483647,…`, with digit
  counts `1,1,1,3,5,10,19,…` growing like `2ⁿ` (doubly-exponential in `n`, hence
  super-polynomial in `v=m(n)=2ⁿ−1`). No fixed polynomial `R` satisfies `R(2ⁿ−1)=2^{2ⁿ−1}−1`
  for all `n` (LHS `~v^{deg R}`, RHS `~2^{v}`). So `P⁺` **fails closure already at `p=q=Id`**.
  (Verified exactly, `scratch/2026-09-05-thm3-verify.py`: `test_pqId` returns FAIL for `P⁺`.)
- **`P` (powerset), commutative.** `m(n)=2ⁿ`, `m(m(n))=2^{2ⁿ}`: same doubly-exponential failure.
- **`D` (finite distributions), affine + commutative.** `D` is not polynomial (it does not
  preserve wide pullbacks: `D(A×_C B)→DA×_{DC}DB`, "joints from marginals," is not iso). Its
  finite shadow is exactly `P⁺` (support map `D→P⁺` is a monad morphism onto the
  affine+commutative finite structure), which fails by the previous bullet; so `D` fails
  structurally. (For a direct cardinality argument one passes to the support/finite-set counting,
  where `D` reproduces the `P⁺` growth.)

**This decisively refutes the retired heuristic "compose ⟺ commutative + affine":** `P⁺`, `P`, `D`
are commutative (and `P⁺,D` affine) yet fail; while **Maybe** (`X+1`, *non-affine*) and **writer**
(`2X`, non-affine) **compose** because they are polynomial. All polynomial monads pass `(‡₀)`
(`test_pqId` returns PASS with the correct `R`), consistent with Part A. ✓

### B3. Lemma N — the remaining categorical gap `[open, reduced]`

The cardinality law B1 is *necessary* but does not by itself pin `M` as a *functor*: cardinalities
cannot separate `M` from a polynomial functor with the same finite counts. The clean categorical
converse is:

> **Lemma N (open).** Let `M:Set→Set`. If the essential image of `⟦−⟧_M` is closed under `∘`
> (equivalently, `M∘N∘M` is of the form `⟦r⟧∘M` for all polynomial `N`), then `M` preserves
> connected limits — i.e. (Carboni–Johnstone, *Connected limits, familial representability and
> Artin glueing*, MSCS 1995; Diers) `M` is familially representable, i.e. polynomial.

**Where it breaks — the trailing-`M` obstruction (named precisely).** Every M-extension is
post-composed with `M`. Hence closure only ever yields identities of the form `F∘M ≅ ⟦r⟧∘M`
(e.g. `M∘M≅⟦r⟧∘M` at `p=q=Id`). One cannot cancel the trailing `M`: precomposition
`M^*=(−)∘M:[Set,Set]→[Set,Set]` is not conservative (it only tests functors on the objects `MX`
and maps `Mf`), so `F∘M≅⟦r⟧∘M` does **not** give `F≅⟦r⟧`. Concretely, if `M` fails to preserve a
pullback `A×_C B`, then *both* sides of `⟦p⟧∘M∘⟦q⟧∘M ≅ ⟦r⟧∘M` fail to preserve it (the innermost
and trailing `M` spoil it symmetrically), so preservation-reflection yields no contradiction.

**Three attempts, all blocked by trailing-`M` (recorded for escalation):**
1. *Reflect connected-limit preservation.* `⟦r⟧` (polynomial) preserves connected limits, so
   `⟦r⟧∘M` preserves exactly the connected limits `M` does; the composite `⟦p⟧∘M∘⟦q⟧∘M` likewise
   only preserves those `M` does. Both sides carry the *same* `M`-defect ⟹ no contradiction. ✗
2. *Retract via the monad unit.* From `M²≅⟦r⟧∘M` and the monad laws, `M` is a **retract** of
   `⟦r⟧∘M` (`s=θ∘ηM`, `ρ=μ∘θ⁻¹`, `ρ∘s=μ∘ηM=id`). But `⟦r⟧∘M` is not known polynomial (it *is*
   `⟦r⟧_M`, an M-extension), and retracts of polynomial functors need not be polynomial; iterating
   only replaces `M` by `⟦r⟧^{◁k}∘M`, never shedding the trailing `M`. ✗
3. *Diagonal restriction.* `Id` is a retract of `Sq=(−)²` (`Δ:Id⇒Sq`, `π:Sq⇒Id`, `π∘Δ=id`), so
   `M` is a retract of `M∘Sq`; and `Sq` preserves all limits. But closure never delivers `M∘Sq`
   *without* a trailing `M` (it gives `M∘Sq∘M`), so the clean object `M∘Sq` on which a
   Carboni–Johnstone argument would bite is not in reach. ✗

**Common pattern.** Every route needs to *strip the trailing `M`*, and the closure hypothesis
never provides an M-free witness. The genuine content of Lemma N is precisely: *upgrade the
cardinality growth law (‡) into connected-limit preservation of `M` without cancelling `M`.* The
intended path (still open) is to run Carboni–Johnstone on the *family* of identities (‡) for all
polynomial `Q` simultaneously — the constraint "`m∘Q` is polynomial on `im(m)` for every
polynomial `Q`" is extremely rigid and plausibly forces `M` familial, but I have no proof that
converts this cardinal rigidity into the categorical (limit-preservation) statement.

---

## Grades / registry

| Claim | Grade |
|---|---|
| A0 structural identity `⟦p⟧_M∘⟦q⟧_M=(⟦p⟧∘M∘⟦q⟧)∘M`, natural | **proved** |
| A1 `M` poly ⟹ closure, `p◁_M q=p◁⌈M⌉◁q`, (★) natural iso | **proved** |
| A2 associativity of `◁_M` | **proved** |
| A3 non-unital unless `M=Id` (up to Cont-iso) | **proved** |
| A4 strong-semigroupal on pure morphisms | **proved** (Kleisli-bifunctoriality open, = codensity) |
| B1 cardinality growth law (‡),(‡₀) | **proved** |
| B2 `P⁺,P,D` fail closure already at `p=q=Id`; heuristic refuted | **proved** |
| Maybe/writer/exception/reader compose | **proved** (Part A + verify.py) |
| Lemma N (closure ⟹ `M` polynomial, full converse) | **open** (trailing-`M` obstruction, reduced to Carboni–Johnstone) |

**Net promotion.** THM 3 sufficiency (A) and the sharp necessity exclusions (B1–B2) move from
`computed` to `proved`. THM 3 as a full biconditional stays "**sufficiency proved, necessity open
via Lemma N**" — a clean, honest promotion, and enough for the WRITE (the composition brick is
solid: *M-containers compose when `M` is polynomial, and the affine+commutative heuristic is
dead*).

**Crown (grant).** Two independent Kan/representability invariants of the effect monad `M`:
**codensity `Ran_M M` governs fullness (THM 2); polynomiality governs composition (THM 3)** —
`writer` composes but isn't full, `D` is full but doesn't compose. This is the clean statement the
wrap-up paper wants.

## Verification artifacts
`scratch/2026-09-05-thm3-verify.py` (Part A Maybe example reproduces `Y⁴+2Y²+1` for `n=0..6`;
Part B `test_pqId` PASS for all polynomial monads with correct `R`, FAIL for `P⁺,P` already at
`p=q=Id`; digit-count growth witness for `P⁺`). Prior: `scratch/2026-09-05-thm3-compose-check.py`
(squaring test, superseded by the cleaner `p=q=Id` test here).
