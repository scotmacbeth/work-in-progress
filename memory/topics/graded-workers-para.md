# Topic: Workers, graded comonads, Para (Neil's Ch4 state axis)

Neil's 07-27 steer: a **category of Workers**, objects `ΔS⊗p→q`, composition
multiplying context `D(S×T)`, framed as **graded monads** graded by `(Set,×)`,
`S:Set` (not a monoid), pointing at Gavranović's **Para**. This is the *state*
axis of Ch4 "Monads and Comonads", complementary to the ZS/H² directed axis.

## Type hierarchy (2026-07-30, PROVED) — which of Cont's structures descend?
`proofs/2026-07-30-workers-type-hierarchy.md`, registry `workers-type-hierarchy.json` (proved).
Two frameworks: **(A) grade-multiplying** (S⋆T→S×T, the native graded-monoidal notion) and
**(B) shared register** (S⋆S→S = A + grade-diagonal + collapse S×S→S).
- **Framework A: ALL FOUR monoidal structures descend.** ⊗ **STRONG** (⊙ strong monoidal functor
  V×C→C via ΔS⊗ΔT=Δ(S×T)); ×,+ **OPLAX** (PROVED, cartesian/cocontinuous); ◁ **OPLAX** (COMPUTED,
  interchange 256 cases). Interchange holds all four.
- **Framework B: the tensor SPLITS.** + strict, × oplax-free; **⊗,◁ need a MONOID on state S**
  (PROVED ⊗ via Comon(Cont,⊗)≅Fam(Mon^op) + no natural monoid: S=∅ has no unit).
- **Closed (COLUMN COMPLETED 08-21, proofs/2026-08-21-workers-x-closed-lhd-obstructed.md):**
  - **⊗-closed** hom = Cont's [p,q]_⊗ (PROVED).
  - **×-CLOSED (08-21, conjecture FLIPPED — was "obstructed")**: hom `[p⇒q]_×=∏_{s_p}q◁(y⊕c_{S×P_p s_p})`,
    `⟦⟧Y=∏_{s_p}⟦q⟧(Y+S×P_p s_p)`. Via `⟦[ΔS,r]_⊗⟧X=⟦r⟧(S×X)^S` + Yoneda; state entangles arg
    `P_p↦S×P_p` but REPRESENTABLY. Old 1296≠256 used wrong candidate q^p.
  - **UNIFORM:** Workers ⊙_⋆-closed iff `S×(A⋆K)` is a functor of `S×A`; holds ⋆=+ (→×), ⋆=× (→⊗).
  - **◁ NOT closed (08-21, resolves open)**: `(−)◁p` hom forced non-polynomial `|H([n])|≥2^{2^n}`
    (R=Id, p=2sh: `n^{2^n}`); **Cont itself lacks ◁-closure** (only a ◁-COclosure/left adjoint) —
    obstruction INHERITED, NOT a state effect. Single-shape p = escape hatch.
- **★ Crown:** collapse S×S→S needs a monoid IFF the object-tensor MERGES the two operands' positions
  (⊗,◁ fibre-product/nested) vs SEPARATES (+,× fibre-sum); same fault line governs closure. State-mode
  obstruction = monoid-on-register, beside directed=[ω]∈H², effect-coeffect=branching κ/λ
  ([[three-modes-of-composition-dream]]).

## State of play (2026-07-28)

**PROVED** (`proofs/2026-07-28-delta-state-object-and-workers.md`, registry
`state-object-delta.json`):
- `ΔS=(S,s↦S)` = codiscrete category; `⟦ΔS⟧=S×(−)^S` store/costate comonad (Uustalu–Vene).
- `ΔS⊗ΔT=Δ(S×T)` strict, `Δ1=y` ⟹ Workers = `(Set,×)`-graded category = coKleisli
  of graded comonad `S↦ΔS⊗−`. Assoc/unit exhaustively checked. `⊗` **forced** (product
  tensor gives `|S|+|T|≠|S×T|`, neg-control).

**LEAN-VERIFIED** (`StateComonad.lean`, [[lean-state-comonad-delta-done]]):
`deltaDC` D1–D5 all **rfl / axiom-free** (cleanest DCont instance in repo); store
counit/comult + 3 comonad laws; **Lemma 3.1 `deltaS S ⊗ deltaS T = deltaS (S×T)` rfl**.
NOT yet Lean'd: the Worker graded-category composition laws (defeq-shaped follow-on
via `Container.dir₂`); the Para identification.

**Two honest gaps (identifications, `computed` not `proved`):**
1. **Para exactness** — `Δ` functorial only on **bijections** ⟹ literal Para over
   `Core(Set)`; strict `(Set,×)`-actegory reading needs a Gavranović-axiom check.
2. **FKM graded-comonad packaging** (Fujii–Katsumata–Melliès) — short, unwritten.

## Nearest neighbour — the load-bearing literature fact
**Capucci–Myers, Contextads as Wreaths (arXiv:2410.21889, App. A.2, deep-read
07-28).** Thm A.4 `Kl(T)≅Ctx(⊙)` for a polynomial monad `T`, grade `X→S`,
composition multiplying grade by `seq` — **left UNPROVEN**. See the sharp
open question in [[workers-graded-and-contextads]]: is Workers an instance
(⟹ my proof settles a case of A.4) or orthogonal (⟹ cite as neighbour)?

## Citation set for the writeup (no nLab crutches)
- Para: arXiv:2105.06332 (Capucci–Gavranović–Hedges–Rischel, ACT 2021); Gavranović
  thesis 2403.13001; blog "Towards Categorical Foundations of Learning" (2021-03-03);
  2402.15332 (Categorical Deep Learning). **No nLab "Para" page.**
- Graded monads: Katsumata POPL 2014 (term origin); Gaboardi et al. 2016 (coeffects);
  Fujii–Katsumata–Melliès (graded-comonad definition).
- Contextads lineage surfaced: Fong–Spivak–Tuyeras (Para origin), Gavranović 1907.08292.
- Adjacent-not-hit: Balan–Pantelimon 2509.13026 (graded monads / costrong / distributive
  laws — no Para/Poly/container); Femić 2510.26465 (Para for double categories — flag if
  `ΔS⊗p→q` needs a double-categorical Para).

## Open questions
- Workers stated as graded category or via Para collapse in Ch4? (asked Neil 07-28)
- Is `Core(Set)` the honest Para home, or is there a variance convention giving a
  strict `(Set,×)`-actegory? (asked Neil 07-28)
- Does `S↦ΔS⊗−` = Capucci–Myers `⊙` for a specific `T`? → [[workers-graded-and-contextads]]
