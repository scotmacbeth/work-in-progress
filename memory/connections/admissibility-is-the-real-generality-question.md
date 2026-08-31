# `◁` is not a structure you transport — it is a CERTIFICATE that the base is `Set`-like

**Found:** 2026-09-09 (dream), by putting the three 2026-08-30 PROVE results side by side.
**Status:** synthesis of `proved` results (no new mathematics here); the reframe itself is mine
and `speculative` as a *research-direction* claim. Registry: `left-adjoint-over-vec`
(+ subtree `gap3-converse`), `fullness-unit-connectedness`, `t4-left-closedness-lhd-famcop`.

## The reframe

Neil's #1 priority (UID 120) has been asked as: **"do the four monoidal structures on `Poly`
generalize to `Fam(C^op)`, and what breaks?"** For `⊗` (Dirichlet/Day) and for the fibrational
logic that is the right question, and the answers are genuinely graded (T2's dualizable-and-
summable corner, `joint-bc-cont-cod`'s one-sided BC). **For `◁` it is the wrong question.**

Nothing "breaks" gradually, because `◁` mostly **does not exist**:

| base | `Fam(C^op)` closed under `◁`? | `I` connected? | `⟦−⟧` inj. on objects? | left adjoint to `(−)◁q` |
|---|---|---|---|---|
| `Set`, infinitary-lextensive ccc topos | yes ⟹ **forces** connected (Thm B) | ✓ forced | ✓ (T1) | **always** (Thm 1) |
| `Vec`, `Vec_fd`, tiny/additive (collapse) | yes, but `◁ := ⊗` is a **stipulation** | ✗ forced (Lem D) | ✗ (Thm D(ii)) | iff `\|T\|=1` (Thm 2) |
| `Set×Set` (lextensive ccc, `1` decomposable) | **no** (Thm B / Prop 9.1) | ✗ | — | question does not arise |
| `Set_*` (zero object, neither pole) | **no** (Thm A) | ✗ | — | question does not arise |
| admissible ∧ non-collapse ∧ non-cartesian | **UNCHARTED** (Gap 1) | ? | ? | ? |

## ★ The sentence

> **On the extensive pole, `◁`-admissibility is not a hypothesis you get to vary — it already
> implies unit-connectedness (Thm B), hence fullness of `⟦−⟧` (T1), hence a left adjoint to
> `(−)◁q` for every `q` (Thm 1). The whole package is one bit.** So the extensive pole offers
> **no generality**: every base there behaves exactly like `Set`, or `◁` is not there at all.

And symmetrically, off that pole: `◁` has to be *defined* (collapse `◁ := ⊗`), and by **Theorem D**
`⟦−⟧` stops being injective on objects (`({∗},k²)` and `({1,2},k)` both present `X ↦ X⊕X` over
`Vec_fd` and are non-isomorphic), so left-adjointness is a property of **the choice**, not of `C`.

> **Theorem 1's hypothesis is simultaneously what makes its converse TRUE and what makes its
> converse MEANINGFUL.** Where the hypothesis fails, the question stops being about `C`.

## Why this is the more useful framing for the grant

1. **It converts a survey question into a dichotomy theorem.** "Which bases support container
   composition?" has an answer with a proof, not a table of case studies: *the `Set`-like ones,
   where you learn nothing new, and the linear ones, where `◁` degenerates to `⊗` and everything
   inverts* (the anti-diagonal — [[left-adjoint-lhd-gate-is-unit-connectedness]]).
2. **It explains the anti-diagonal instead of merely recording it.** Left adjoint: `Set` always /
   `Vec_fd` iff `|T|=1`. Right adjoint (`◁`-closure): `Set` iff `|T|=1` / `Vec_fd` iff summable.
   The conditions swap because **on one pole `◁` is forced by the base and on the other it is
   imposed by me.** A forced structure is rigid in one variable; a chosen one in the other.
3. **It relocates the open territory precisely.** The only place where "generality" could be a
   real research programme is **Gap 1: admissible, non-collapse, non-cartesian-closed**. That is
   now a *named, empty-so-far* region with a concrete lead (`I ≅ I_1 ⊔ I_2` in closed monoidal
   `C` gives `X ≅ (X⊗I_1)⊔(X⊗I_2)`, an idempotent-splitting shape; if `I_i⊗I_j ≅ 0` for `i≠j`
   the Theorem B argument runs verbatim without cartesianness).
4. **It sharpens, not replaces, [[extensivity-is-the-container-boundary]].** That note said
   extensivity *carries* `Set` container theory. Theorem B says more: on an extensive ccc base,
   merely *having* `◁` implies the rest. Extensivity isn't the sufficient condition — it is the
   region where admissibility is a **single** condition.

## The novelty gate, kept attached (do not compress this away)

- Theorems A, B, D and Lemmas E1/E2 are **ungated**. E1/E2 (`1 ≅ 1⊔Z ⟹ Z ≅ 0` in a lextensive
  category) are plausibly folklore — **Carboni–Lack–Walters** is the place to check, and I claim
  no priority for them.
- **Dorta–Jarvis–Niu `2305.05655`** may dodge Theorem B entirely: their formulation is *indexed*,
  with one index set per component, where the "ONE external shape set" obstruction evaporates.
  If so Theorem B is a theorem about **my external-shape `Fam(C^op)`**, not about generalized
  polynomial categories as such. **UNVERIFIED — check before any novelty claim.**
- **Pradic–Price `2601.15420`** stand under "all categories in sight shall be lextensive" (§2.1
  p. 7) — i.e. inside the rigid pole, which is exactly why their framework cannot see this.

Related: [[fullness-unit-connectedness]], [[left-adjoint-lhd-gate-is-unit-connectedness]],
[[triangle-admissibility-trichotomy]], [[t4-left-closedness-lhd-famcop]],
[[extensivity-is-the-container-boundary]], [[one-functional-many-probes-method]],
[[contribution-is-the-delta-prior-work-fused-away]], [[reference_dorta_jarvis_niu_generalized_poly]].
