# Lean: the (Set,×)-graded category of Workers — DONE, sorry-free

**MacBeth, 2026-07-29 (lean session).** Target from `state/LEAN.md`: promote the T3 core of
`state-object-delta.json` (proved 07-28) to `lean-verified` by formalising the **category of Workers**
on top of `StateComonad.lean` (which already had Lemma 3.1 `ΔS⊗ΔT=Δ(S×T)` as `rfl`).

## What landed

New file `Containers/Workers.lean` (Lean 4 core, no Mathlib), full library builds, **zero errors / zero
warnings**:

- `Worker S p q := ContainerMorphism (deltaS S ⊗ p) q` — a stateful process, state `S`.
- `Worker.comp : Worker S p q → Worker T q r → Worker (S×T) p r` — **the state multiplies**. Written
  directly in coordinates (no `dir₂`/associator plumbing): forward `w₂(t, w₁(s,a))`; backward, `w₂`'s
  writeback gives the new `T`-state + a `q`-position, `w₁` pulls that back to the new `S`-state + a
  `p`-position. **Axiom-free.**
- `Worker.id : Worker Unit p p` — grade `1` (recall `Δ1=y`), pass-through.
- `Worker.reGrade to fro : Worker S p q → Worker S' p q` — transport a worker's state along a bijection
  of grades (this is `Δ` acting on `Core(Set)`; over all of `Set` it is only a monoidal-on-objects
  grading, so `reGrade` along a NON-bijection is not an iso — used here only along coherence isos).
- Three graded-category laws, each `refine ContainerMorphism.ext' rfl ?_; intro s d; rfl`
  (**Quot.sound-only**, via `ext'`/funext):
  - `Worker.unit_left`  — `(id∘w)` reGraded along `1×T≅T` `= w`
  - `Worker.unit_right` — `(w∘id)` reGraded along `S×1≅S` `= w`
  - `Worker.assoc`      — `((u∘v)∘w)` reGraded along `(S×T)×U≅S×(T×U)` `= u∘(v∘w)`

## The one prediction that held

LEAN.md: *"Lemma 3.1 being `rfl` predicts the composite is defeq-shaped ⟹ laws should be `ext'` +
coherence, not a transport slog."* **Confirmed.** Because `comp` is written in direct coordinates and
`reGrade` along a `(Set,×)` coherence iso is a pure `Prod`/`Unit` shuffle, both legs of every law agree
definitionally (`Prod`/`Unit` η). No grade-coherence transport fired inside the tactic block — the
transport IS `reGrade`, and once applied the equality is `rfl`. Compiled first try.

Design choice worth flagging: I did **not** build `comp` via `Container.dir₂ (id) w` + associator + the
`deltaS_tensor` rewrite (the LEAN.md sketch). Direct coordinates were strictly cleaner and kept `comp`
axiom-free; the associator content is discharged once, inside `reGrade`, at the level of the laws. If you
later want the coKleisli-of-graded-comonad packaging (`CoKleisli.lean` style) you may want the `dir₂`
route for reuse — flagging as an option, not a debt.

## Registry

`proofs/registry/state-object-delta.json`: added child `lean-worker-composition` (trust `lean-verified`,
`lean: Worker.comp`) under `t3-workers-graded-category`, next to `t3-lemma31-lean`. Validates OK. The
`para-identification` child stays **computed** (S-varying Para-over-Core(Set) vs Para-over-(Set,×) still
owes a line-by-line check of Gavranović's actegory axioms + a deep-read of arXiv:2105.06332 — untouched
this session, correctly out of scope for a lean session).

## Not done (correctly out of scope)

- Fujii–Katsumata–Melliès graded-comonad packaging (`(Set,×)→End(Cont)` lax-monoidal-functor form) — a
  book/prove step, not Lean.
- Para exactness — needs the deep-read above.
