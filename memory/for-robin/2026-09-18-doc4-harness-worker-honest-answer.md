# Doc #4 "The Harness is a Worker" — rewritten to your honest question, pushed

**For:** Robin (and Neil). **From:** MacBeth, 2026-09-18 (write session).
**File:** `papers/harness-is-a-worker.tex` / `.pdf` (5 pp), pushed to work-in-progress.
**URL:** https://github.com/scotmacbeth/work-in-progress/blob/main/papers/harness-is-a-worker.pdf
**Content-commit:** `75e98d6` (stamped on page 1); stamp-commit `d426136` on `main`.

This replaces the 16 Sep interface draft (`6b7971c`). That earlier draft was a general
"everything composes" exposition; your UID-184 correction redirected the doc, so I rewrote it to
answer the one question you actually posed — **does the store-comonad worker buy anything over
stalin's explicit state-threading, or just rename it?** — instead of assuming the answer.

## The answer the doc earns (two halves, both on page 1)
1. **Single worker: buys nothing.** `Store_S X = S × (S→X)` is literally the curried form of
   threading `s:S`. On the lens fragment it is just `get:S→A`, `put:S×B→S`. If Kodamai stopped at
   one worker the comonad would be a rename and I say so plainly (§2, Prop 1).
2. **Interacting composite: buys compositional correctness.** Two workers that *share* the ledger
   are not the free tensor `Δ(S×T)` (that models two firms with no shared books) — they are a
   Zappa–Szép weld, which needs a **comonad distributive law** `λ` fixing how the two stores
   interleave. Comonads don't compose for free. Whether a consistent `λ` exists is `[ω]∈H²`; given
   (L), the weld exists iff `[ω]=0`; the smallest re-entrant model is `[ω]=ε∈ℤ/2`, "does the worker
   mutate shared state the other depends on" (Lean-checked). A wrong `λ` is exactly the re-entrancy
   / state-divergence defect (Path-5). Threading doesn't escape `λ` — it hides it, one reasonable
   line at a time, until the per-site choices are globally inconsistent, i.e. `[ω]≠0`, found at run
   time. The comonad **names** `λ` once and makes `[ω]=0` one check, up front. §§3–4.

Net (the honest ledger, §5): not single-worker convenience, and **not** automatic composition
(the composite can genuinely fail to exist — no formalism conjures it). What it buys is *where and
when* the interleaving decision is made and checked. For many interacting workers — an agentic
business — that is the compositional-correctness guarantee the grant is about, and it is a genuine
**addition** to stalin, because stalin has no state store today.

## Your correction, folded in (§1)
I no longer conflate the `morphisms.ts` existential with hidden state. The doc states it correctly:
`∃ j:Shape<D>.(PosAt<D,j>→PosAt<C,s>)` = Ghani's `Σ(j:Q).(Tj→Ps)`, the **codomain shape** chosen
per call + amalgamate leg (Church-encoded via the rank-2 `delegate(s,k)`; "j becomes a scope, not a
type"). That is the Σ in the hom, not `ΔS`. Hence stalin's `state.ts` (Stocks/Workforce/grades) is
plain visible domain data, and a store-comonad worker is real new structure. This is why the
question is honest and the answer is "genuine addition," not "re-description."

## Honesty notes (please read before quoting)
- **One verified math invocation only:** `[ω]=ε` (`Reentrancy.lean`, sorry-free). The doc draws the
  Lean boundary explicitly (Remark 1): Lean certifies the finite 𝔽₂ class computation
  (`ω(ε)` is a coboundary ⟺ `ε=0`); the *reduction* of the categorical obstruction to that complex
  stays pen-and-paper (analytic note, Prop 3.1), **not** formalised.
- `ΔS⊗ΔT=Δ(S×T)` vs `ΔS◁ΔT` (4y⁴ vs 8y⁴, a retract): proved + Lean (`WorkersRetract.lean`).
- DL ⟺ ZS/bicrossed and (G)⟺`[ω]=0`: proved elsewhere; group-level anchor Kassel/Brin. No new
  theorem is claimed; no arXiv citation is load-bearing (citation footprint clean).
- The §4 stalin example (Production writes Stocks / Hiring writes Workforce, sharing the ledger) is
  **schematic and labelled as such** — it is the *shape* of the addition and where `λ` would sit,
  not a description of present code.

## [PROVE TODO] flagged in the doc, not hand-waved
The reduction "store-comonad interleaving = distributive law of directed containers" is invoked at
the directed-container level (`ΔS` is one). A *bespoke store-comonad restatement* of `[ω]` is not
needed for this note; if you or Neil want it as a standalone lemma, it's a prove-session item, not a
claim I've made here.

## One open offer
The 16 Sep interface exposition (tool=container, harness runs the `⟦p⟧`-coalgebra, whole trace =
cofree comonad `𝔠_p`, orchestration = `◁`/`⊗`) is good material that this rewrite deliberately set
aside to keep the honest question in focus. It survives in git at `6b7971c`. If Neil wants the
interface/cofree story foregrounded for the Path-5 grant application, I'll spin it out as its own
note rather than reviving it here. Say the word.

*(Per write-session rules I did not email this; it will go in the daily digest.)*
