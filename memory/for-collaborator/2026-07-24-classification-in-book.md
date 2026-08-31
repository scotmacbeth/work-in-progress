# The closed convolutional tensors are classified — folded into the book (Ch3 §sec:closed)

**For:** Neil, Robin — 2026-07-24 write session
**File:** `projects/books/category-of-containers.tex`, new subsection **"The complete list"**
(`sec:classification`), inside §"Closing the structures". Compiles clean, 40 pp.

## What changed

The closed-structures section already had the arc: **biconditional** (⊙_⋆ left-closed ⟺ (−)⋆B
polynomial ∀B) → **collapse tensor** (so the condition is a real restriction). It ended with a
*conjecture* about which tensors survive. That conjecture is now a **theorem** — I replaced it.

**Theorem (the complete list, bounded arity) [MacBeth].** A *symmetric* monoidal structure
(Set,⋆,I) with (−)⋆B polynomial for every B and **bounded arity** is isomorphic to either

- **×** (unit 1) → the Dirichlet tensor **⊗** on Cont, or
- **∨_S** (unit ∅) for a unique set S → the **▷_S** family (∨_∅ = + → the product × on Cont).

So the three closures we already knew — cartesian, Dirichlet, Spivak's ▷_S — are the **entire**
list in the bounded case. Your instinct that they're a law and not a coincidence is a theorem.

## The proof, in three moves (all in the book, compute-first)

1. **The unit is small:** |I| ≤ 1. (R₁(I) = I⋆1 = 1 against the polynomial normal form of R₁.)
2. **Degrees multiply:** d(C⋆B) = d(C)·d(B), from R_B∘R_C ≅ R_{C⋆B} (associativity). Hence a
   finite arity ≥ 2 would give d(B⋆B) = κ² > κ — impossible against the global max. So every R_B
   is **affine**, X⋆B = C_B + D_B×X.
3. **The heart — the symmetry identity.** For unit ∅, X⋆B = B + D_B×X, and symmetry gives
   **B + D_B×X ≅ X + D_X×B**. The right side is affine in B, so D_B must be affine in B:
   D_B = 1 + S×B, giving X⋆B = X + B + S×X×B = ∨_S. (Unit 1 gives × directly.) This is the one
   genuinely new lemma; I've stated it on its own (`lem:symid`).

## The honest gap — written as Further Work (per your "no moonshots" steer)

The bound κ < ∞ is load-bearing and I did **not** remove it. The infinite-arity case is a
**genuine open problem**, and with meaningful probability the conjecture there is *false*. I've
written this straight into a `Remark[the infinite-arity boundary]`, not dressed as a near-certainty:

- κ² = κ for infinite cardinals, so the Move-2 counting engine dies.
- "Affine" = "preserves connected **colimits**", while closure only buys connected **limits** —
  independent for polynomial functors, so no categorical shortcut.
- R₂ = y + y^λ (λ infinite) is a formal **fixed point** of the arity recursion → counting is
  provably blind. Any real obstruction is an element-level pentagon computation, not settled here.
- The non-symmetric case (left-closed but not right-closed) is likewise flagged open.

## Provenance / housekeeping

- Theorem + symmetry-identity lemma + infinite-arity remark tagged **[MacBeth]** / **[MacBeth;
  open problem]**. The families ×, ∨_S / ⊗, ▷_S are already attributed to Spivak/Garner upstream
  in the same section — I added **no new citation**, so no provenance regression. Whole-book
  citation floor is unchanged (`agent-summary` from 2405.13157, pre-existing, for a future browse).
- Sources: `proofs/2026-07-23-closed-convolutional-tensors-classification.md` (bounded theorem),
  `proofs/2026-07-24-arity-gap-further-work.md` (why the gap is open). Registry
  `closed-tensor-classification`: `main-theorem-bounded` = proved, `gap-infinite-arities` = open.

Robin can read the section directly from the projects volume. Happy to spin the classification out
as a short standalone note for the grant's "theory" section if useful — it's the sentence that
turns three known closures into a completeness statement.

— MacBeth
