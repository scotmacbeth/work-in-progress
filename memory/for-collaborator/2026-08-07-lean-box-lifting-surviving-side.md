# LEAN cert — the □ predicate monad lifting (surviving side of the proof-relevance boundary)

**MacBeth, LEAN session 2026-08-07.** Companion note to `for-robin/` grant material.

## What got machine-checked

I extended `lean/Containers/Containers/ReaderStateOutsidePiMendler.lean` (previously the DROP-failure
certificate) with **the surviving side** of the proof-relevance boundary — the exact thing Neil
challenged in UID-91 ("are you really saying there's *no* predicate lifting for Reader/State?").

Answer, now Lean-verified: there **is** a predicate monad lifting — the `□` necessity lifting
`□P(m) = ∀ leaf. P` — it just isn't the proof-relevant Ahman–Bauer `∏` one. Both directions of the
boundary now live in one file.

New declarations (`Containers.ReaderStateOutsidePiMendler`), all with `P : Lbl → Prop` a **genuine
proposition**:

- `reader_box_unit` — `P x → □P (η x)`.
- `reader_box_mult` — `□□P mm → □P (μ mm)`, **unconditional** in `mm` and `P` (term `fun h e => h e e`,
  the diagonal instantiation). This is the direct contrast to `reader_kappa_not_total` in the same file.
- `reader_box_mult_iff_reverse_total` — for a fixed `mm`, the box-mult law (∀ `P`) is **equivalent**
  to reverse-totality of `mm`. Forward direction instantiates the single test predicate
  `P₀ y := ∃ token i, lab i = y` (= `Lab(I(mm))`), exactly the symbolic argument in
  `proofs/2026-08-07-proof-relevance-boundary.md` §3.4.
- `reader_reverse_total_always` — reverse-total holds for **every** `mm` (each diagonal leaf `e`
  *is* the token `(e,e)`, `rfl`). This is *why* `□` survives where `∏` dies.
- State mirror: `state_box_unit`, `state_box_mult`, `state_box_mult_iff_reverse_total`,
  `state_reverse_total_always` (threading token `(s₀, (F s₀).1)`).
- Contrast bundles: `reader_proof_relevance_boundary`, `proof_relevance_boundary_reader_state` —
  FAIL(`∏`/κ) vs HOLD(`□`) at the **same** monad.

## Trust level

- Root `lake build` green: 47 jobs, **zero errors, zero warnings, zero `sorry`**.
- **All 8 new declarations depend on NO axioms at all** (`#print axioms` — not even `propext`).
  The box laws are pure terms / `rw` / `obtain`; because `P` is a real `Prop` there is no
  `Fin`/`propext` detour (contrast the DROP side, which used `decide` on a bespoke `Lbl ≅ Fin 3`).
- Registry: `effect-coeffect-arrows.json`, new child `proof-relevance-box-lean` under
  `proof-relevance-boundary`, `trust = lean-verified`,
  `lean = Containers.ReaderStateOutsidePiMendler.proof_relevance_boundary_reader_state`.

## Grant hook

"Predicate lifting exists, container monad does not" is now **not hand-waving** — it is a
type-checked, axiom-free Lean fact for both Reader and State, on the same object where the `∏`
`T_M`-monad provably has no multiplication. Clean deliverable for the Formalisation pillar and a
direct, verifiable answer to Neil's question.

## Honestly still open (not touched here — a prove/lean target)

The `Σ`-container lifting (the *proof-relevant* candidate that also survives, per §4.3 /
`sigma-monad-coherence-open`) has only its multiplication laxator checked, not full monad coherence.
Do **not** claim "Reader has a proof-relevant monad lifting" until that's done. The `fourfold-z2-grading`
bonus remains `computed`. Both are flagged in the registry.
