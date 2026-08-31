# Free/cofree universal properties reduce to the laws of the *given* object

**Found:** 2026-07-25 (dream), consolidating the 07-24 free-monad-UP PROVE and the 07-25
cofree-comonad-UP PROVE into one structural moral. **Status:** cross-result *pattern* (both halves
now proved in container coordinates), NOT a new theorem — both adjunctions are prior art
(Gambino–Kock 0906.4931 Thm 4.5; Spivak 2202.00534 eqs 244–264; Niu–Spivak 2312.00990
Prop 8.18/8.33/Thm 8.45). The contribution is the two coordinate proofs and the observation that
they are mirror images.

## The pair (both PROVED in coordinates this window)

- **Free monad** `F ⊣ U : Cont ⇄ Mon(Cont,◁)`, `F : X ↦ m_X`, unit = insertion of generators.
  Proof by **W-type induction** on trees. `proofs/2026-07-24-free-monad-universal-property.md`,
  registry `free-monad-universal-property` = **proved**. → [[free-monad-universal-property-proved]].
- **Cofree comonad** `U ⊣ 𝔠 : Comon(Cont,◁) ⇄ Cont`, `𝔠 : p ↦ 𝔠_p`, counit = read-root.
  Proof by **M-corecursion** on shapes + finite path-recursion on positions.
  `proofs/2026-07-25-cofree-comonad-universal-property.md`, registry `cofree-comonad` = **proved**.
  → [[cofree-comonad-up-proved]].

## The shared shape (why this is a connection, not two results)

> **The (co)universal property of the free/cofree (co)monoid reduces entirely to the (co)monoid
> laws of the object given at the *other* end of the adjunction — no law of the free/cofree object
> is ever re-proved.**

- **Free (left adjoint):** the induced monoid morphism `ĝ : m_X ⇒ M` is a homomorphism *because*
  the **target** monoid `M` satisfies its laws — **base case = M's unit law, inductive step = M's
  associativity**, in both the shape and position components. The free object `m_X` contributes only
  its recursion principle (W-type), never a law of its own. (Mirror of the grafting note: the free
  monoid's own laws ↔ `graft_assoc`.)
- **Cofree (right adjoint):** the induced comonoid morphism `ĝ : D ⇒ 𝔠_p` is a comonoid morphism
  *because* the **source** comonoid `D` satisfies its **five directed-container laws** — forward/shape
  half ← D1+D4 (Lemma U), backward/position half ← D2+D5 (Lemma S), triangle ← D3. The cofree object
  `𝔠_p` contributes only its corecursion principle (M-type / finality), never a law of its own.

So the two proofs are **the same proof read in a mirror**: replace "target monoid `M`" by "source
comonoid `D`", "induction / W-type / μ / initiality" by "coinduction / M-type / ν / finality", and
"insertion of generators" by "read-root". This is exactly the **syntax ↔ behaviour** adjoint pair the
book's Ch6 frames (free = syntax = `μ`, cofree = behaviour = `ν`).

## The load-bearing asymmetry — positions stay finitely inductive on BOTH sides

The coinduction in the cofree proof is **confined to the shapes** (the M-type tower). Positions are
**vertices** of a tree, and vertex-sets are **finitely inductive on both sides** — free *and* cofree.
This is why the two position-layer proofs (`ĝ♯` by finite path recursion, using `⊕`) look identical,
and it is the reason [[cofree-comonoid-scooped-and-wrong]] insisted **positions = vertices, not
leaves**: get that wrong and the finiteness (hence the whole backward layer) collapses. Uniqueness:
forward = coinduction (finality of `tree_p`) / induction; backward = path induction / `split`-
bijectivity, on both sides.

## Where it bridges the seed paths

- **Path 1 (containers)** ↔ **Path 3 (Poly)**: `⟦m_X⟧(A)=μY.(A+⟦X⟧Y)` and `⟦𝔠_p⟧(A)=νY.(A×⟦p⟧Y)`
  are the free monad / cofree comonad on the *functor* `⟦X⟧`/`⟦p⟧`; the container coordinate proof
  descends to the Poly statement via `⟦–⟧` strong-monoidal + AAG full-faithful.
- **Path 2 (directed containers)**: the cofree comonad **is a directed container** (why Ch6 sits
  after Ch5 DCont≅Cat) — its five D-laws are exactly the source-`D` laws the UP reduces to.
- **Path 6 (Lean)**: the asymmetry is *only in the formalisation*, not the maths. Free side is
  W-type ⟹ core-Lean tractable (`FreeUniversal.lean`: triangle + unit + object-uniqueness +
  MULT-forward-shape machine-checked); cofree side is M-type ⟹ **infra-blocked** on Mathlib
  `PFunctor.M`/`bisim` (core Lean has no coinduction). Robin/Neil infra call outstanding.
  → [[lean-free-monad-up-partial-and-cofree-blocked]].

## Sources & depths
- Gambino–Kock arXiv:0906.4931 Thm 4.5 — **deep-read**; "free monad on a polynomial is polynomial".
- Spivak arXiv:2202.00534 v14 eqs 244–264 — **deep-read / full-PDF** (re-read 2026-07-24, downloaded
  `~/papers/2202.00534.txt`; the prior-dream `agent-summary` source-depth flag on lines 3899–3995 is
  now **DISCHARGED**). States both `𝔪⊣U` (ordinal colimit) and `U⊣𝔠` (limit tower `𝔠p=lim p_k`,
  `p_{k+1}=(p◁p_k)×y`) as established fact — two independent anchors, NOT a scoop.
- Niu–Spivak arXiv:2312.00990 Prop 8.18/8.33/Thm 8.45 — cofree = subtree comonoid, prior art
  (the `[MacBeth]` novelty tag was correctly stripped in the Ch6 draft).
- Mathlib `PFunctor.M` = `CofixA`-tower inverse limit — **independently realises** Spivak's `𝔠p=lim p_k`
  recipe; no comonad structure built on it yet (genuine Lean gap).

Related: [[free-monad-universal-property-proved]], [[cofree-comonad-up-proved]],
[[lean-free-monad-up-partial-and-cofree-blocked]], [[cofree-comonoid-scooped-and-wrong]],
[[book-ch6-monads-comonads-drafted]], [[free-monad-grafting-laws-done]],
[[position-op-turns-monads-into-comonads]] (07-26: the transfer is the *pointwise* face of this same op).
</content>
</invoke>
