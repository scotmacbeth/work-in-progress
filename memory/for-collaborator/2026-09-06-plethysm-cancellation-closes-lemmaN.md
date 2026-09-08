# For Neil/Robin — the Plethysm-Lemma residual is dissolved (a_0=0 world), THM 3 analytic converse essentially closed

**2026-09-06 PROVE session.** Full write-up: `proofs/2026-09-06-lemmaN-plethysm-cancellation.md`.

## The one-line story
The last gap in THM 3's converse (**M-containers compose ⟺ M polynomial**) for analytic monads was
the *Plethysm Lemma* — a delicate molecular statement about wreath vs. Young stabilizers in `A•A`.
I found we never needed it. For every analytic monad with **`M(∅)=∅`**, the converse follows from a
clean algebraic fact:

> **Plethysm right-cancellation.** In the cycle-index ring `ℚ[[p_1,p_2,…]]`, if `H` has zero
> constant term and nonzero `p_1`-coefficient, then `F ↦ F∘H` (plethysm) is injective.

Since `M∘M ≅ ⟦r⟧∘M` gives `Z_M ∘ Z_M = Z_{⟦r⟧} ∘ Z_M`, cancelling the (right) plethystic action of
`Z_M` forces `Z_M = Z_{⟦r⟧}`. But `⟦r⟧` polynomial ⟺ `Z_{⟦r⟧}` uses only `p_1`-powers, whereas a
non-polynomial (non-flat) `M` has a genuine `p_{k≥2}` term. Contradiction. Done — **with no bound on
degree or on wreath depth.**

## Why this is the good proof
The scary residual cases were the **unbounded-wreath-depth** monads — free commutative magma / free
operad-algebra monads, whose balanced `2^k`-leaf structures carry iterated wreaths `S_2≀⋯≀S_2`. No
stabilizer/degree bookkeeping can touch those. But they are exactly the **free-algebra monads of a
signature without constants**, so `M(∅)=∅` — and cancellation dispatches them all in one line.
(Verified: free comm. magma has `M[n]=(2n−3)!!`, `a_0=0`.) The old method got `𝕄` (bounded wreath
depth, `S_n` primitive); the new one gets the hard cases the old one couldn't.

## Full coverage of THM 3 necessity now
- non-analytic super-polynomial monads (`P,P⁺,D,β,…`): cardinality law (09-05).
- **analytic, `M(∅)=∅`, ANY degree/wreath depth: Theorem P (new).**
- **analytic, bounded degree, any `M(∅)`: Theorem S (new; support-indecomposable factor invariant,
  cycle-index-free, subsumes the 09-05 `𝕄`/`D_4` argument).**
- analytic, `M(∅)≠∅`, unbounded, symmetric-power/commutative (incl. `𝕄`): 09-05 §4.

**Only open corner:** analytic, `M(∅)≠∅` *finite*, unbounded degree, **and** unbounded wreath depth.
I argue (conjecture, strong evidence, §4) this is **vacuous** for finitary analytic monads: building
unbounded wreath depth from a nonempty constant part forces `M(∅)` infinite (drop the constant →
Theorem P; keep it → non-finitary). This explains *why no known monad inhabits the gap*.

## What I'd like a second pair of eyes on
1. §4 structural obstruction — is "finitary analytic + unbounded wreath depth ⟹ `M(∅)∈{∅,∞}`"
   provable? That would make the analytic converse **unconditional**. Feels like an operad/PROP fact.
2. Whether the analyticity hypothesis itself can be dropped: is every monad satisfying the THM 3
   cardinality law (09-05 §B1) either super-polynomial or analytic? (The gap = polynomially-bounded
   non-analytic monads — do any exist?)
3. Provenance: Theorems P/S invoke Joyal ff + the plethysm-substitution identity from memory. Nodes
   are capped at `computed` in `m-containers.json` until I re-read BLL Ch.1–2 / Joyal 1986. The
   cancellation engine P0 and the support-splitting lemmas S1/S2 are self-contained + code-verified.

Registry: `proofs/registry/m-containers.json`, node `necessity-lemma-gap` (children
`theorem-P-plethysm-cancellation`, `theorem-S-bounded-degree`). Validator green.
