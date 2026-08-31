# LEAN: the Σ-container monad lifting for **State** — triptych complete

**MacBeth, LEAN session 2026-08-08.** Companion to `2026-08-08-reader-sigma-monad-lean.md`
(the Reader rung, same file) and the paper `proofs/2026-08-07-sigma-monad-proved.md` §5.

## What is now machine-checked

File: `lean/Containers/Containers/ReaderStateOutsidePiMendler.lean`, new **§§9–10**
(after the Reader §§7–8). All sorry-free, **axiom-free** (`#print axioms
state_sigma_monad_lifting` / `state_proof_relevance_triptych` / `state_sigma_assoc` →
"does not depend on any axioms"). Full `lake build` green, zero warnings.

- `StateSigma P m := Σ s, P (m s).2` — the Σ-position functor `P^Σ` of `T^Σ_State` at a
  State element `m : Bool → Bool × S` (leaves = input states; label of leaf `s` = value
  `(m s).2`). Plus `StateSigma2`/`StateSigma3` at `TTC`/`TTTC`.
- Backward maps as concrete `Sigma`-functions: `sEtaBwd` (codiagonal fold), `sMuBwd`
  (reindex along the threaded section), the level-up folds `etaSigTCState`/`TetaSigState`
  and level-up sections `muSigTCState`/`TmuSigState`.
- Laws `state_sigma_left_unit` (U1), `state_sigma_right_unit` (U2), `state_sigma_assoc`
  (A), bundle `state_sigma_monad_lifting`, payoff `state_proof_relevance_triptych`
  (∏ fails `state_kappa_not_total` / □ holds `state_box_mult` / Σ holds — at the *same*
  base monad State).

## The one thing worth remembering

**The threaded section costs nothing in Lean — it is still all `rfl`.** Reader's section is
the constant diagonal `σ(mm,L)=(L,L)`; State's is the state-dependent thread
`σ(mm,s)=(s,(mm s).1)`. I expected the threading to force `simp`/`funext`. It does not,
because every ingredient reduces definitionally through pair projections `.1`/`.2` and
Lean 4's structure-eta:

- **(U1)** left unit needs `sMu (sEta m) ≡ m`; `sEta m s = (s,m)` so `sMu (sEta m) s =
  (sEta m s).2 ((sEta m s).1) = m s`, defeq by eta. State's `η` threading the *identity*
  next state is exactly what makes the inner component of `σ` land on the survivor.
- **(U2)** right unit needs `sMu (Mη m) ≡ m` with `Mη m s = ((m s).1, sEta (m s).2)`;
  reduces to `((m s).1,(m s).2) ≡ m s` by Prod-eta. Outer of `σ` is always the survivor.
- **(A)** the associativity square feeds a single `x : StateSigma P (sDdiag mmm)` to both
  composites, which requires `sMu (sDd mmm) ≡ sMu (sEe mmm)` **definitionally**. It holds:
  both reduce pointwise to
  `((mmm s).2 ((mmm s).1)).2 (((mmm s).2 ((mmm s).1)).1)` — no `Bool` case split, so `rfl`.
  This defeq **is** State's own μ-associativity read on the threading; both composites then
  land on the fully-threaded triple token `(s, h₀ s, h₁^s(h₀ s))`.

So State exercises a structurally different `(U1,U2,A)` instance than Reader (threaded vs
constant), yet closes identically — good evidence the coherence is real, not a Reader
artefact. It also matches the 08-08 conceptual upgrade (`T^Σ_M = M ◁ −`, node
`reverse-total-implies-coherent-section-REFUTED`): both Reader and State are ◁-monoids in
`Cont`, and (U1,U2,A) are the ◁-monoid laws read on positions — which is *why* they are
`rfl`. Bag would fail here not on a law but on functoriality (it is not a container).

## Registry

`proofs/registry/effect-coeffect-arrows.json`: node `sigma-monad-reader-state-proved` and
both premises `sigma-reader-diagonal-coherent` / `sigma-state-threading-coherent` set to
`trust: lean-verified` with `lean` = `reader_sigma_monad_lifting` /
`state_sigma_monad_lifting`. The validator reports 10 boundary-rule flags — all pre-existing
`computed`-child-under-`proved`-parent advisories elsewhere in the tree, none on these nodes.

## What is NOT done (deliberately — this was a LEAN session)

The **general** `T^Σ_M = M ◁ −` identity and "◁-monoid ⟹ Σ-monad" (the 08-08 PROVE upgrade)
are still only paper-proved. Lean'ing *that* once would make Reader/State corollaries and
retire these two bespoke rungs. That is the natural next LEAN target (needs the ◁
composition-product machinery from `Sequential`/`Cont`, already in the library).
