# Uniform closure of Day tensors on Cont — PROVED (both directions)

**MacBeth, 2026-07-15 (PROVE session).** Full write-up:
`proofs/2026-07-15-uniform-closure-day-tensors.md`. Registry: `closed-day-structures.json`
(status `proved`, validator clean).

## What was open, what is now closed

The PROVE brief asked me to prove **sufficiency** (the formula `[p,q]_⋆ = Π_i q◁(p[i]⋆y)` is a
right adjoint when `⋆` is polynomial), and to *settle or honestly downgrade* **necessity** (the
classification corollary, graded `speculative`). Both are now **proved**, and necessity is
easy — one line — once phrased right. Registry grades moved:
`uniform-closure-formula` computed → **proved**; `closed-convolutional-classification`
speculative → **proved**.

**The theorem.** For monoidal `(⋆,I)` on `Set`:
> `(Cont, ⊙_⋆)` is **left closed** ⟺ `(−) ⋆ B : Set→Set` is **polynomial** for every set `B`,
> with internal hom `⟦[p,q]_⋆⟧(R) = Π_{i∈S_p} ⟦q⟧(R ⋆ p[i])`.

- **Sufficiency**: co-Yoneda `Cont(y^R,q)≅⟦q⟧R`, hom-out-of-coproduct, and `Poly` closed under
  `◁` (composition) and small products. `[p,q]_⋆` is a container because
  `R↦Π_i⟦q⟧(R⋆p[i])` is a product of composites of polynomials.
- **Necessity**: take `p=y^B, q=y`. The right adjoint's value satisfies
  `⟦[y^B,y]_⋆⟧R ≅ Cont(y^R⊙_⋆y^B, y) = Cont(y^{R⋆B}, y) ≅ R⋆B`. So `(−)⋆B` *is* the extension of a
  container `[y^B,y]_⋆`, hence polynomial. Closure evaluated at one hom = the polynomial condition.
- **Classification corollary**: immediate — restrict Theorem A (Day = equivalence onto
  convolutional structures) to the matching sub-collections.

## Two honest corrections you should know about

1. **Handedness bug in the brief.** PROVE.md paired the formula `A⋆p[i]` (left slot varies) with
   the condition `R⋆(−)` (right slot). Mismatched. The correct pairing is formula `R⋆p[i]` ↔
   condition **`(−)⋆B` polynomial**. Invisible for symmetric `⋆` (`+`, `×`), so the cartesian and
   Dirichlet instances never exposed it. The right-closed mirror carries `A⋆(−)`. Details §4.

2. **No EM step.** The brief expected "the same pointed-domain split as the chain rule (classical
   EM)." It does not appear. The only infinitary ingredient is `ΠΣ≅ΣΠ` distributivity in `Set`
   (choice-function reindexing), which is constructively valid. I report the absence rather than
   manufacture a split. §5, Remark 5.2. *(This is worth a second look in the dream cycle — is the
   chain rule's EM step also avoidable, or is there a real asymmetry?)*

## What's genuinely new vs prior art

Prior art (novelty pre-audited, `memory/closed-structures-are-spivaks.md`): the three instances and
the formula itself = Spivak's Eqs. 38/39/40 (cartesian = Niu–Spivak Thm 5.31 / ALS; Dirichlet =
Ex. 4.79). **New:** the general biconditional uniform in `⋆`, the necessity reduction, and killing
the old corepresentable criterion. This is a **remark-level bolt-on to Theorem A**, not a paper —
holding to the grading the memory note insisted on.

## The one open thing (sub-Q 6.1)

Is the polynomial condition **vacuous**? Every monoidal `⋆` I can name (`+`, `×`, `∨_S`) is
polynomial in each slot ⟹ closed. Is there a monoidal structure on `Set` with `(−)⋆B` *not*
polynomial — i.e. a convolutional tensor on `Cont` that is genuinely not left closed? If not, the
closed family = the whole convolutional family. Natural place to look: a `⋆` built from a
non-polynomial functor (full powerset) that still satisfies associativity + unit. **Nothing in the
theorem depends on the answer** — I flag it as the residue, not a gap.

## For the grant / book

This finishes the "four monoidal structures + their closures" story on the theory side: closure of
a convolutional tensor on containers is *polynomiality of a set-level operation*, seen through the
extension. Book sentence in §7 of the write-up. Verified: `scratch/day-family/task6_closure.py`
(2704/2704 core iso, 64/64 necessity witness, teeth confirmed).
