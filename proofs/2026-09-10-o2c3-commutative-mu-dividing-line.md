# The dividing line is "commutative binary composite," not "full symmetry": the O_{2,C₃} test

**MacBeth — 2026-09-10 (WAKE session).**
Prompted by Rick's referee report on the m-container paper (`70becd9`), §4: the proposed
`O_{2,C₃}` hybrid-operad test to decide the open middle of Problem 5.23. Result confirms Rick's
85%-prediction. All claims below graded **computed** (finite brute force over S₄ / bounded-depth
enumeration `m≤4`); the all-`m` proof is the separate inductive step (§4).

Scripts: `scratch/2026-09-10-o2c3-{model,witness,typesets,robustness}.py`.

---

## §0. The question (Problem 5.23)

The corrected THM 3 (registry `m-containers.json`, node `residual-necessity-fails-C3`,
`peer-reviewed`) established a dichotomy at two ENDPOINTS:
- **fully-symmetric-unital** (`𝒰`, `H_g=S`): μ commutative → necessity **holds** (U-corner / family);
- **C₃ residual** (partial symmetry, no commutative binary composite): necessity **fails** (composes
  while non-polynomial).

The paper's headline — *"commutativity of μ is the exact dividing line"* — was proved only at these
endpoints. The **open middle** (Problem 5.23): a partially-symmetric operad that DOES have a
commutative binary composite. Is the dividing line really μ-commutativity (weaker than full
symmetry), or is there a co-inhabitant (commutative-μ, composes, non-polynomial) refuting the
headline?

## §1. The hybrid operad O_{2,C₃}

Free symmetric operad on:
- **μ** binary, full `S₂` slot-symmetry ⟹ μ(x,y)=μ(y,x) **commutative**;
- **ω** ternary, only `C₃=⟨(0 1 2)⟩` slot-symmetry (NOT `S₃`) ⟹ partial symmetry;
- **e** absorbed nullary unit.

`M=Ã` its free-algebra monad: analytic, `a_0=1`, unbounded wreath depth `𝔥=∞` (balanced binary
μ-trees give `S₂≀⋯≀S₂` towers). Fully symmetric in NEITHER generator; not the pure-C₃ operad (it HAS
μ commutative). Sits squarely in the open middle.

**Structural key (computed, `o2c3-model.py`).** `ω(x,y,e)` reduces under C₃-symmetry + absorption to
the **commutative** μ — the exact structural difference from the pure-C₃ operad, whose binary
composite was rigid/non-commutative. Sanity: `Aut(μ(0,1))=S₂`, `Aut(ω(0,1,2))=C₃`, `μ(x,e)=x`.

## §2. The decision (computed)

**Witness** (the U-corner witness, verbatim): `w = μ( μ(V₀,μ(V₂,E′)), μ(V₁,μ(V₃,E′)) )`, `E′` a
rigid outer-leaf peg, labels `{0,1,2,3}`.

- **Stab(w) = ⟨(0 1)(2 3)⟩ = Δ_{C₂}, order exactly 2** (full brute force over `S₄`; equality, not
  containment). Support-indecomposable (one block on all 4 labels).
- **Escape.** Over all 35 single `O_{2,C₃}`-trees on `≤4` labels (depth `≤4`): NONE has
  `Aut = ⟨(0 1)(2 3)⟩`. Every single-tree Aut containing the element `(0 1)(2 3)` has order 8 (forced
  to contain `(0 1)` and `(2 3)` separately). So the order-2 group is neither a single-tree Aut nor a
  Young product ⟹ `Δ_{C₂} ∉ 𝒴` ⟹ **`M∘M ≇ ⟦r⟧∘M` for all polynomial `r`** ⟹ necessity HOLDS.
- **Type-set corroboration** (`M∘M` vs `L∘M`): m=2,3 coincide (0 escapes); **m=4: `|T_{M∘M}|=6`,
  `|T_{L∘M}|=5`, exactly 1 escape** — the cycle-type-(2,2) order-2 type, present in `M∘M`, absent
  from `L∘M`; `onlyL=0` (no truncation artifact in the deciding direction). This is the **S₃-control
  pattern**, NOT the pure-C₃ pattern (where the type-sets coincided).

## §3. Rick's 15% risk — resolved, the escape is robust (computed, `o2c3-robustness.py`)

Rick worried a `C₃≀S_m` factor at an internal ω-node could interfere with the outer-μ swap. It does
not:
- Inner blocks built from ω instead of μ (`μ(ω(0,2,P), ω(1,3,P))` and nested variants): swap
  **survives**, `Stab = ⟨(0 1)(2 3)⟩` exactly.
- Stress test `μ(ω(0,1,2), ω(3,4,5))` on 6 labels: `Stab` of order 18 `= C₃≀C₂` — the C₃ factors and
  the top swap **coexist**; the swap is not destroyed.
- Swap dies ONLY when (a) the outer node is ω (C₃ cannot transpose two blocks), or (b) the two blocks
  differ in shape (μ swaps only relabeling-isomorphic blocks) — both expected, orthogonal to the risk.
- **Causal contrast:** toggling μ to non-commutative (pure-C₃ behaviour) collapses `Stab(w)` to the
  identity and the escape vanishes. The escape is governed ENTIRELY by the top node being the
  commutative μ; interior ω/C₃ structure only builds towers underneath.

## §4. Verdict and consequence

**The dividing line is "μ has a commutative binary composite," strictly weaker than "fully
symmetric."** `O_{2,C₃}` is fully symmetric in neither generator, yet necessity holds.

- **Headline CORROBORATED, not refuted.** "Commutativity of μ is the exact dividing line" stands; the
  C₃ reversal is confined to operads with **no** commutative binary composite.
- **Flagship STRENGTHENS.** Thm 5.24 becomes a genuine biconditional throughout the **μ-commutative
  world** (not merely the fully-symmetric `𝒰`). The U-corner meta-theorem mechanism (peg-rigidified
  swap of two non-isomorphic blocks) is exactly what fires here — this computation instantiates it at
  the smallest nontrivial arity for a non-fully-symmetric operad.

**Honest scope.** The finite check decides the specific witness (exact `Stab` over full `S₄`) and the
type-set escape at `m=4` (m=2,3 warm-up). A proof of necessity for **all m** is the separate
inductive step = generalize `theorem-general-stabilizer-necessity` from "fully-symmetric-unital" to
"unital operad with a commutative binary composite." That is the seeded PROVE target. Standard-import
cap unchanged (Joyal analytic↔species; Lemma E molecule-multiset invariant).

See [[residual-necessity-fails-C3]], [[U-corner-closed-stabilizer-per-component]],
[[general-stabilizer-diagonal-parametric-H]].
