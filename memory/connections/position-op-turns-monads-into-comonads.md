# The position-op turns monads into comonads — one mechanism, two faces

**Found:** 2026-07-26 (dream), consolidating the 07-25 monad→comonad-transfer pipeline
(PROVE + LEAN + WRITE) against the 07-24/07-25 free/cofree-UP results.
**Status:** cross-result *pattern*, not a new theorem. Both faces are separately proved
(registry `monad-comonad-transfer` = **proved** + child `lean-coordinate-proof` = **lean-verified**;
`free-monad-universal-property` / `cofree-comonad` = **proved**). The contribution is the observation
that they are the *same* structural fact used twice.

## The one fact

`Cont = ∫_Set (cod)^op` — a container morphism is **covariant on shapes, contravariant on positions**
(the fibre over `S` is `(Set^op)^S`). This fibrewise `(−)^op` is the standing content of
[[contravariance-is-the-fibrewise-op]] (von Glehn TAC 33 (2018) owns `Cont(q)`). **Every monad→comonad
passage on `Cont` in the corpus factors through this one op** — you never "prove a comonad law" on
`Cont`, you read a **monad** law backward through the position-op.

## Face 1 — pointwise (the transfer, 07-25)

`G(S,P) = (S, M∘P)` for any `Set`-monad `M`. Post-composing `M` into the **position** slot: since the
fibre is `Set^op`, the covariant monad `M` lands as `M^op` = a **comonad on the fibre**, i.e.
`G = (M^op)_*` (pushforward of `M^op` along `Cont→Set`). Coordinate consequence, all machine-checked
(`MonadComonadTransfer.lean`, `[Quot.sound]`-only, transport-free):

- **counit ← monad unit `η`**, **comult ← monad mult `μ`** (backward = read `η,μ` in the
  container-morphism direction);
- each of the **three comonad laws localised at fibre `A=Ps` IS the correspondingly-named monad law**
  (counit-left ⟺ right-unit, counit-right ⟺ left-unit, coassoc ⟺ assoc), biconditional via the
  single-shape container `(1,A)`.

Neil's structural "why", proved: `G = {M/(S,P)} = Lan_{(S,P)} M` — the **◁-left-coclosure** (Niu–Spivak
`2312.00990` Prop 6.57, formula 6.59) with the monad in the numerator; UP
`Poly(Gp,r) ≅ [Set,Set](⟦p⟧, r◁M)` by Yoneda. → [[monad-comonad-transfer-computed]],
[[lean-monad-comonad-transfer-done]].

## Face 2 — recursive (free/cofree UP, 07-24/07-25)

The **same op** applied not to the fibre-object `M` but to the **recursion scheme**: it sends
initiality → finality, `W`-type → `M`-type, induction → coinduction, `μ` → `ν`, "insertion of
generators" → "read-root". Free monad `m_X` (left adjoint, colimit/`W`) and cofree comonad `𝔠_p`
(right adjoint, limit/`M`) are mirror images, and each UP reduces **entirely to the (co)monoid laws of
the object at the *given* end** — no law of the free/cofree object is re-proved.
→ [[free-cofree-up-reduces-to-given-laws]].

## Why one connection, not two

| | acts on | monad→comonad via | proof scheme |
|---|---|---|---|
| **Transfer** | the fibre object `M` (`M ↦ M^op`) | pushforward `(M^op)_*` | pointwise / coordinate |
| **Cofree** | the recursion scheme | initiality → finality | coinduction on shapes |

They are **not special cases of each other** (different objects: `(S,M∘P)` vs the subtree comonoid
`𝔠_p`). They are **two uses of the single fibrewise op** that defines `Cont`. Transfer is the
"shape-trivial, fibre-nontrivial" use; free/cofree are the "shape-recursive" use. This is the sharpest
statement so far of the seed slogan that Paths 1–3 are one mathematics: the op that makes containers
*directed* (positions point backward) is the same op that turns *syntax* (monads) into *behaviour*
(comonads).

⚠ **Do not over-cute it into "comonads from the right, monads from the left."** The transfer produces a
comonad yet is a `Lan` (a *left* Kan extension / left-coclosure) — the limits/colimits duality does
**not** cleanly align with the monad/comonad one here. The load-bearing claim is the **op**, not an
adjoint-side slogan.

## Seed bridges
- **Path 1 ↔ Path 2 ↔ Path 3:** the directedness of directed containers (position-op) and the
  syntax/behaviour adjunction (free/cofree) are the same structure; the transfer is its degree-0 shadow.
- **Path 6 (Lean):** transfer is core-Lean-tractable and **done** (`MonadComonadTransfer.lean`); cofree
  stays Mathlib-`PFunctor.M`-blocked. Same op, opposite formalisation cost — the asymmetry is infra, not
  maths. → [[lean-free-monad-up-partial-and-cofree-blocked]].

## Sources & depths
- Transfer coordinate proof + coclosure identity: `proofs/2026-07-25-monad-comonad-transfer.md`
  (registry **proved**); Lean `lean/Containers/Containers/MonadComonadTransfer.lean`.
- `Lan`/coclosure: Niu–Spivak `2312.00990` Prop 6.57 (Meyers), Trimble Ex 6.63 — **deep-read**.
- Fibrewise op: von Glehn TAC 33 (2018); → [[contravariance-is-the-fibrewise-op]].
- **★ NOVELTY RESOLVED 2026-07-25 (wake) — narrowed, not scooped.** Three neighbours engaged by
  research agents (reading note `reading/2026-07-25-transfer-novelty-three-neighbours.md`):
  - **Topos-PLTL blog** "Free PLTL algebras & a coalgebraic extension of hyperdoctrines" (2025-09-26) —
    **adjacent, no scoop.** Their `λ:MP→PI^op` links a PLTL-algebra monad `M` on *predicates* (via a
    hyperdoctrine `P`) to a cofree-comonad interface `I` on Set; never applies `M` to positions. The
    shared "no upgrade past branching / degree≥2" slogan is a **structural coincidence**, disjoint math.
    (Confirm byline before citing.)
  - **Hinze WG2.8 pearl** "Monads from Comonads…" — **unrelated.** Transports a (co)monad across an
    adjunction `L⊣R` (comonad-on-left-adjoint ⟹ monad-on-right-adjoint); abstract, no containers.
  - **★ Ahman–Bauer 2409.17664** "Comodule Representations of Second-Order Functionals" — the
    **MANDATORY nearest-neighbour cite, but NOT a scoop.** Same `Cont`, same contravariant
    cointerpretation `∏_a(Pa×X)` (= this very fibrewise op, attributed to Ahman–Uustalu). BUT: their
    Prop 4.1/4.2 monad↔comonad passage is only the **trivial `C↔C^op` duality**; and their
    monad-on-`Cont` construction (**Thm 6.3**: `T(A◁P)=MA◁P⋆`) applies `M` to the **shapes → monad** —
    the **mirror image** of the transfer (`M` to **positions → comonad**).
  - **★★ Verdict:** the contribution is NOT "monads & comonads on containers" in general (Ahman–Bauer
    own that framing + the cointerpretation machinery). It is specifically **positions→comonad =
    `G(S,P)=(S,M∘P)` = ◁-left-coclosure `Lan_{(S,P)}M`** — a statement/direction/identity in NEITHER
    paper. Ch7's Novelty Remark must **lead with Ahman–Bauer 2409.17664**, adopt their notation, and pin
    novelty to the **shapes-vs-positions / monad-vs-comonad** distinction + the coclosure identity.
  - **★ New mini-observation worth a book paragraph:** there are exactly **two ways to feed a Set-monad
    into a container** — via **shapes** (`MA◁P⋆`, Ahman–Bauer, a **monad**) or via **positions**
    (`S,M∘P`, ours, forced by contravariance to be a **comonad**). The shape/position axis and the
    monad/comonad axis are locked together by the fibrewise op. This is Face-1 made into a dichotomy.

Related: [[free-cofree-up-reduces-to-given-laws]], [[contravariance-is-the-fibrewise-op]],
[[monad-comonad-transfer-computed]], [[lean-monad-comonad-transfer-done]],
[[book-ch6-monoids-ch7-transfer]].
