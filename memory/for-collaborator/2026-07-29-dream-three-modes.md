# For Neil — three modes of composition, and your arrow synthesis is open (07-29 dream)

Two things from tonight's consolidation, both grant-facing.

## 1. The grant's Path-5 question now has a clean table

*"When do two compositional systems compose, and what obstructs it?"* — three modes, three
obstruction **types**, all proved (rows 1–2 Lean-verified):

| Mode | Weld | Composition | Obstruction | Always exists? |
|---|---|---|---|---|
| Directed (ZS) | `C⋈D` categories | Zappa–Szép product | `[ω]∈H²(Sk_C;𝒟)` | No |
| State (Workers) | `ΔS⊗p→q` | grade × `S×T` | none | Yes (grade accumulates) |
| Effect–coeffect | `Cont(G_M p,T_M q)` | reverse entwining `κ` | branching (M arity ≥ 2) | No — iff M non-branching |

I am deliberately **not** merging these into one master obstruction — H², nothing, and a Boolean
arity condition don't unify. The distinctive grant claim is *three modes, three obstructions, one
question* — nobody in the effect/coeffect or ZS literature has assembled it.

## 2. Your Plotkin–Turi question — answered, with a twist

The 07-27 entwining and the 07-29 effect–coeffect arrows are **two faces of one structure**, split
by branching:
- **Bialgebra / Turi–Plotkin face** `λ:T_MG_M⇒G_MT_M` — exists for **all M** (`G_M` lifts to
  `T_M`-alg, `T_M` to `G_M`-coalg). **This is your Plotkin–Turi question: YES.**
- **Arrow / Freyd face** `κ:G_MT_M⇒T_MG_M` — the biKleisli category of effect–coeffect arrows,
  exists **iff M is non-branching**.

So "arrows unify effects and coeffects for containers" is true *unconditionally as bialgebra*, but
the *categorical/arrow* packaging is obstructed exactly by branching (Pf = explicit non-associative
witness; Maybe, Writer/ℤ₂ = genuine categories).

## 3. The arrow synthesis you proposed appears genuinely open

I scouted the literature hard. The ingredients all exist separately — arrows-as-monoids (Heunen–
Jacobs MFPS 2006), coeffects-as-indexed-comonads (Petricek–Orchard–Mycroft ICALP 2013), graded
effect+coeffect distributive laws (Gaboardi et al. arXiv:2112.14966), a Chu-space/Day-convolution
alternative unification (Katsumata–Rivas–Uustalu arXiv:1912.13477), a modern higher-order Plotkin–
Turi continuation (Goncharov et al. arXiv:2405.16708) — but **nobody has assembled them for
containers/Poly, and none is framed as an arrow category.** We already own the hard core.

**One question for you:** Katsumata–Rivas–Uustalu frame monad–comonad interaction as monoid objects
in Chu over (Endofunctors, Day convolution). Since Day convolution is already load-bearing in our
Dirichlet-tensor work, I think reframing the entwining as a Chu-space monoid object (route b) may be
more tractable than building the Freyd category by hand (route a). Do you have a preference for which
route the effects⊗coeffects paper should take first?

(Full write-up: `connections/three-modes-of-composition.md`.)
</content>
