# Lean: ΔS state comonad / codiscrete category — DONE (2026-07-28 lean session)

**File:** `lean/Containers/Containers/StateComonad.lean` (wired into `Containers.lean`; whole
library `lake build` green, zero warnings).

**What landed (all machine-checked):**
- `deltaS S : Container` — shapes `S`, positions `fun _ => S` (⟦ΔS⟧ X = S × X^S).
- `deltaDC S : DirectedContainer` — codiscrete category: `root s = s`, `sub s p = p`,
  `shift s p q = q`. **D1–D5 all `rfl`** — `deltaDC` is **axiom-free** (`#print axioms` clean).
  This is the cleanest DCont instance in the repo: the codiscrete category is genuinely defeq.
- Store comonad, inherited from `Containers.Directed`:
  - `deltaDC_counit`:  `ε ⟨s,v⟩ = v s`  (rfl, axiom-free)
  - `deltaDC_comult`:  `δ ⟨s,v⟩ = ⟨s, fun p => ⟨p, v⟩⟩`  (rfl, axiom-free)
  - `deltaDC_left_counit`, `deltaDC_right_counit`, `deltaDC_coassoc` — the 3 comonad laws,
    reused directly from `DirectedContainer.left_counit/right_counit/coassoc` (`Quot.sound`-only,
    via funext, matching the whole Directed.lean development).
- Lemma 3.1 (state multiplies), as **strict container equalities**:
  - `deltaS_tensor : deltaS S ⊗ deltaS T = deltaS (S × T)`  (rfl, axiom-free)
  - `deltaS_unit : deltaS Unit = Container.y`  (rfl, axiom-free)
  Uses the Dirichlet `⊗` from `Containers.Dirichlet`.

**Registry:** `proofs/registry/state-object-delta.json` — added two `lean-verified` children:
`t1-lean` (under `t1-codiscrete-store`) and `t3-lemma31-lean` (under `t3-workers-graded-category`).
Validates (`trustcheck ... validate ... --files-dir proofs` → OK).

**Why this and not MULT-backward.** LEAN.md primary target was `freeExtPos_mult`'s node step —
its **5th** session. Per standing discipline (don't bash a 4×-resisted target) I took the fresh,
guaranteed-tractable fallback instead. MULT-backward remains open; its status is unchanged. The
diagnosis of where the node step breaks is in `for-collaborator/free-monad-mult-backward-lean.md`
(untouched this session).

**What is NOT yet Lean'd (honest gaps, for a future cycle):**
- The **Worker graded-category** laws of T3 (composition `w' ∘ (id⊗w)`, associativity/unitality up
  to the `(Set,×)` associator/unitors). Only Lemma 3.1 — the *state-multiplies* backbone — is Lean'd.
  The composition is defeq-shaped (functoriality of `⊗` + `deltaS_tensor`) and should be a clean
  follow-on, but it needs the `⊗`-on-morphisms action (`Container.dir₂`, already in Dirichlet.lean).
- The Para / `Core(Set)`-actegory identification (registry `para-identification`, still `computed`).

Next Lean candidate: formalise Worker composition + the graded-category unit/assoc laws, reusing
`Container.dir₂` and `deltaS_tensor`. That would promote the T3 core to lean-verified.
