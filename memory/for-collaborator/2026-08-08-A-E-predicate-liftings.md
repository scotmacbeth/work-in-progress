# For Neil (and Robin): your UID-94 A/E predicate liftings — both flags proved

**MacBeth, PROVE 2026-08-08.** Full write-up: `proofs/2026-08-08-A-E-predicate-liftings.md`.
Registry node `neil-A-E-predicate-liftings` (proved) in `effect-coeffect-arrows.json` (validates).

Neil — your note handed us the two liftings under your own names, and both flags are now proved
cleanly. Short version:

**Setup.** For containers `X=(S_X,P_X)`, `Y=(S_Y,P_Y)`, evaluated at `(s,g)∈⟦X⟧S_Y`:
`All X Y (s,g)=∏_{p:P_X s} P_Y(g p)`, `Exists X Y (s,g)=Σ_{p} P_Y(g p)`. The two bifunctors share
shapes `Σ_s S_Y^{P_X s}` and differ only ∏ vs Σ on positions. **`E = Exists = X◁Y`** exactly.

**Flag 1 — "can't define A on polynomial functors" (P1).** Yoneda gives the whole story in one line:
a natural pushforward `A X Y → A X' Y` along `α=(u,φ)` is a **section of the backward position map
`φ`**, and the set of them is `∏_p φ⁻¹(p)`. So:
- non-surjective `φ` (any leaf-dropping morphism): **no map exists at all** — this is the decisive
  reason `A` doesn't extend to all polynomial functors;
- bijective `φ` (cartesian): **unique canonical** section `φ⁻¹` → genuine functor.

`∏` is contravariant in its index set; a container morphism reindexes it the wrong way. `E=Σ` pushes
forward covariantly along `φ` and needs no section — that's why `E=◁` is a bifunctor and `A` is not.
And this **is** our crown boundary "`T_M` lifts ⟺ `M` cartesian" one level down: take `α = μ_M`. Your
functoriality flag and our multiplication-drop are literally one statement. (Note the asymmetry:
`A` *is* functorial in the **second** argument for all morphisms, because there `ρ` acts pointwise
*inside* each ∏-factor rather than reindexing it.)

**Flag 2 — the action law `A X (A Y C) = A (E X Y) C` (P2).** True, and strict. Positions:
`∏_p ∏_q = ∏_{(p,q)}` (Fubini). Shapes: distributivity (`∏` over `Σ`) + currying. Unit `A y C = C`.
So — and this is the clean statement I'd put in the book note — **`A` is a left action (left module)
of the `◁`-monoidal `(Cont, E, 1)` on `Cont`.** Object-level action law unconditional; as a
*functorial* action it lives on `Cont_cart × Cont` (Flag 1). Dually `E X (E Y C) = E (X◁Y) C` is just
`◁`-associativity — worth stating side-by-side: `E` acts by its own monoidal structure, `A` rides
alongside but only cartesian-functorially.

**One convention flag for you:** I called it a **left** module (`(X◁Y)•C = X•(Y•C)`, monoid on the
left). My daily email said "right ◁-module" — slip; the maths is the standard left-module axiom.
Tell me if you want the other convention.

**Orestis cross-check (matters for the book note).** Your `A X(A Y C)=A(E X Y)C` is the **pure,
base-monad-free, STRICT** object law (Fubini). Orestis has only the **oplax** `Λ-join : Λ P ∘ join ⊆
Λ(Λ P)` (`Effects/PredicateLiftings.agda:19`) — but that is a *different layer*: the interaction of
`All` with a **base monad's** `join`. The clean picture: **the composition law is strict; once a
base monad's `μ` enters, it degrades to Orestis's `⊆`, and it becomes `=` again exactly when that
`μ` is cartesian** — the boundary once more. So his `⊆` and your `=` are not in tension; they are two
rungs of the same ladder.

**Bonus (P3) — where ∏ and Σ refuse to commute.** The mixed law `A X(E Y C)` vs `E(A X Y)C` is **not**
an equality; the comparison is the distributivity/`κ`-entwining map, an iso **iff every shape of `X`
has exactly one position** (`X` linear, `⟦X⟧≅S_X×(−)`). This is strictly finer than non-branching
(`≤1`): an empty-position shape breaks it (`Σ_∅=0 ≠ 1=Π_∅`). A small surprise the computer caught —
the empty shape is the culprit, not branching per se.

**Status / honest gaps.** P1, P2, and P3's exact condition are proved (Yoneda + Fubini, plus a clean
finite corroboration: `scratch/prove-A-E-verify.py`, all checks pass). Not done: (i) a Lean rung for
the action-law Fubini (flagged, the natural next `/lean`); (ii) the module *pentagon/triangle*
coherence 2-cells — automatic for a strict/`rfl` encoding, otherwise open. I did not overclaim these.

This is exactly the greenlit book-note material (two liftings over the `Cont→Set` fibration, retire
"proof-relevant" for your subobject/codomain vocabulary, Hermida–Jacobs + the Orestis witness). I'll
draft it next.
