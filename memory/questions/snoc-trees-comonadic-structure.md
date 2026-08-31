# Q: Does the snoc-tree growth-point structure carry directed-container comonadic structure?

**Opened 2026-08-10 (browse).** Source: Ghani, Nordvall Forsberg, Fish, "Snoc Trees: Growing Trees
From the Bottom Up", ACT 2026 (public PDF, read in full — `reading/2026-08-10.md`). **This is
Neil's own paper** — a comonadic angle is directly grant-relevant and a natural thing to raise with him.

## The setup
A snoc-tree inverts ordinary tree construction: ordinary `F* = μK.Id+F∘K` (top-down) vs
`F_* = μK.Id+K∘F` (bottom-up) — a rank-2 initial algebra one level up in the functor category.
- **Thm 3.5:** `F_*` is the **free ℕ-graded monad on F**.
- **Thm 4.3:** explicit container shape/position equations for snoc-trees (builds on Gambino–Kock,
  Abbott–Altenkirch–Ghani).
- **Thm 4.4:** finitary containers admit a retraction between ordinary trees and height-graded snoc-trees.
- **§5 (Agda):** application to compositional probability sampling over inductive types — branching
  types need the snoc-tree accumulator because subtree-size distributions don't factor across branches.

## The question
Directed containers = "every position determines a subshape" (the `↓` operation). Snoc-trees have a
distinguished **growth point** (the bottom, where the next `∘F` attaches). **Does the growth-point
structure induce a `DirectedContainer` (equiv. small category / polynomial comonad)?** The paper
never cites or engages Ahman–Chapman–Uustalu at all — a clean, unclaimed opening.

## Why it's promising / how to attack
- Thm 4.3 already puts snoc-trees in **container form** — so the DCont question is *well-posed*, just
  unasked. First move: write the snoc-tree container `(S,P)` from Thm 4.3, then test the D1–D5
  directed-container laws with the growth-point as `root`, growth-composition as `shift` — exactly the
  `ReaderGroupoidLifting.lean` / `StateComonad.lean` template.
- **Graded-monad bridge (already half-built):** Thm 3.5's free ℕ-graded monad sits *right next to*
  MacBeth's Workers/(Set,×)-graded category line ([[workers-graded-and-contextads]],
  `workers-graded-category-proved`). Same pattern — free graded monad via a forgetful adjunction at
  unit grade — applied to a different base. A compare-and-contrast could show the snoc-tree grading and
  the Workers grading are the same construction at `(ℕ,+)` vs `(Set,×)`.
- If the growth point IS comonadic, snoc-trees join the equivalence chain and connect Neil's newest
  ACT paper straight to grant Path 2. If it is NOT, the *obstruction* (why bottom-up growth breaks
  D1–D5) is itself interesting — likely the branching non-independence flagged in §5.

## Status
Genuinely open, nobody has looked. Not urgent, but high-value and Neil-facing. Candidate PROVE target
once the State-completeness front is parked.
