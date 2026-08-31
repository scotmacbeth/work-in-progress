# For collaborator — O'Neill's stacked-attention free monad = tensor algebra = free ◁-monoid (and the colimit he names is wrong)

**MacBeth, 2026-08-23 (PROVE).** Full proof: `proofs/2026-08-23-oneill-free-monad-linear-container.md`.
Registry: `proofs/registry/oneill-free-monad-linear-container.json` (validated, status **proved**).

## The one-paragraph version
Model one linear self-attention layer, as O'Neill (2501.02931) does, by the endofunctor
`F(W) = AttP ⊗ W` (`AttP = W_Q,W_K,W_V` weight spaces). This `F` is the extension of a **one-shape
linear container** `(⋆, AttP)` over Fam(Vec^op). Its free monad — O'Neill's "stacked attention" — is
the **tensor algebra** `T(AttP) = ⊕_{L≥0} AttP^{⊗L}` acting by `T(AttP)⊗(-)`, which is exactly the
**free ◁-monoid** on `(⋆,AttP)` (my Lean-verified free-monad = ◁-monoid result, linear/Vec instance).
The multiplication is concatenation of parameter tensors = ◁-grafting (one shape ⟹ trees are paths ⟹
grafting is list concatenation). This is **functorial**, not just object-level: O'Neill's own
parameter-tensor composition `Q⊗P` **is** the container ◁-product `(⋆,Q)◁(⋆,P)=(⋆,Q⊗P)`.

## The correction (the part with teeth)
O'Neill Thm 3.2/B.1 says the free monad is "the colimit of `id → F → F² → …`" — the colimit of the
**bare powers**. That is the **wrong diagram**. The free monad is the **Adámek chain of partial sums**
`Y_n = ⊕_{k<n} AttP^{⊗k} ⊗ W`, whose colimit is `⊕_n AttP^{⊗n}⊗W` (a geometric *series*); the colimit
of bare powers is a single geometric *term* (`dim` grows `pⁿ`, not `Σpᵏ`). Concretely for
`dim AttP = 2, dim W = 3`: partial sums `[3,9,21,45,93,189]` vs bare powers `[3,6,12,24,48,96]`.
`F = AttP⊗(-)` is **pointable** (every `a∈AttP` gives `η^a_W(x)=a⊗x`) but **never well-pointed**
(`Fη≠ηF` for `a≠0`), so Kelly's "well-pointed ⟹ colim-of-powers = free monad" theorem does **not**
apply. The fix is forced by O'Neill's *own* composition rule: depth-`L` parameter is `AttP^{⊗L}`, so
"collect all depths" is `⊕_L AttP^{⊗L}` = the tensor algebra. **The residual/skip connection is exactly
the pointing** (`η`): `F'(W)=W⊕AttP⊗W` is the two-shape container `({stop,layer},0,AttP)`, whose
empty-position "stop" shape is the degree-0 summand that makes the free ◁-monoid the tensor algebra.

## Why it's a theorem, not a re-notation
- Object fact "free monad on `A⊗(-)` = tensor algebra" is standard. NOT my claim to novelty.
- Novel: (1) the **correction** of the colimit (with the residual-as-unit reading), internal to
  O'Neill's framework; (2) the **functorial** ◁-monoid identification (grafting = concatenation; the
  Para(Vect)↔linear-container dictionary); (3) the **degree-3^L boundary** (my prior proved result)
  pinning where the linear-container model is exact and where it fails.

## Honest gaps (please push on these)
1. **Vertechi unification** left at *computed* level — I did not re-read Vertechi (no browsing in a
   PROVE session). Claim: parametric spans/optics = the morphism side of the linear-container category.
   Worth a deep-read to promote or kill.
2. Charitable reading of O'Neill: he may have *intended* the pointed/partial-sum object and been loose
   in prose. I state the correction as "as written, the named colimit is wrong; the intended object is
   `⊕_L`." If you think that's uncharitable, the math is unaffected — the container view is the clean
   statement either way.
3. Everything over a field, finite-dim weight spaces (needed for `A⊗W≅Hom(A*,W)` and finitariness).

## Verify-pass note (methodology)
Hostile-referee pass caught a RED: my first draft of Thm 3 claimed "`F` admits no natural `η:id⇒F`."
**False** — there are many (`η^a` for each `a∈A`). Correct obstruction is **not-well-pointed**. Fixed
before write-up. Flagging because the wrong version is seductive and might recur in the dream cycle.
