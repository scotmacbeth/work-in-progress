# House-doc #4: "The Harness is a Worker" — draft ready

**For:** Robin (and Neil). **From:** MacBeth, 2026-09-16 (write session).
**File:** `papers/harness-is-a-worker.tex` / `.pdf` (6pp), pushed to work-in-progress.
**URL:** https://github.com/scotmacbeth/work-in-progress/blob/main/papers/harness-is-a-worker.pdf
**Content-commit:** `6b7971c` (stamped on page 1; a real ancestor of current `main`).

This turns Neil's remark — relayed by you (UID 179) — that **"the harness is a worker"** into a typeset
Kodamai house-doc, matching the style of #1–#3. It is the *interface* reading (one tool = a container),
**not** the memory/skills/context reading; that distinction is the point of §5. Your Claude is the intended
implementer, so it is written operationally: signatures spelled out, one `dungeon`-monster worked example,
the two composition rules.

## The four moves (the doc's spine)
1. **A tool is a container** `p = S ▷ P`: shapes `S` = admissible calls, positions `P(s)` = possible
   responses. A `dungeon` monster is exactly this (`S` = moves, `P(s)` = outcomes). *Using* a tool is a
   container morphism `α : A → p`: forward = delegate a call `α(a)`, backward = interpret the response.
2. **The harness runs the coalgebra.** An agent driver is a `⟦p⟧`-coalgebra `run : W → Σ_s (P s → W)`:
   emit a call, consume a response, transition. The harness is the *matter* that resolves each emitted
   call against the world. The whole interaction trace is the **cofree comonad** `𝔠_p` on the tool
   (`⟦𝔠_p⟧X ≅ νZ.(X × ⟦p⟧Z)`) — "pattern runs on matter" (Spivak).
3. **Same object ⟹ same composition.** `◁` = dependent/sequential pipelines (one response picks the next
   call); `⊗` (Dirichlet) = independent/parallel tools. Payoff: **an agent is a tool for a meta-agent** —
   nesting is just `◁`/`⊗`, no new machinery. Trust boundaries sit where the Zappa–Szép weld's `[ω]∈H²`
   could fail to vanish (smart constructor on the orchestration morphism).
4. **The clean split.** Interface `(S,P)` = this doc. Carried **state** = the orthogonal tensor factor
   `ΔS = S ▷ (λ_.S)` store-comonad worker (doc #3). Memory/skills/context = matter the harness runs on,
   *not* part of `(S,P)`. "Harness is a worker" = interface half; "state via the tensor" = state half;
   they are the two factors of `ΔS ⊗ p → q`.

## Honesty notes (please read before quoting)
- **Cofree comonad UP** is proved *on paper* (container-coordinate note, 2026-07-25) but **not** Lean-
  verified — its shape layer needs `M`-types/coinduction that the Lean core lacks. The doc says so
  explicitly (Remark 1) and flags a **LEAN TODO**. What *is* machine-checked is the dual **free** monad
  (`Free.lean`, zero `sorry`). I did not claim the cofree side is formalised.
- Everything else cited (workers graded category / `ΔS⊗ΔT=Δ(S×T)`, the retract, `[ω]=ε` reentrancy) is
  proved and, where stated, Lean-checked. No new theorem is claimed — this is exposition.
- Citation footprint clean (floor `verified-quote`; only external arXiv id is Spivak 2202.00534).

## Open question for you / Neil
The doc treats the "trust boundary = smart constructor at `[ω]≠0`" only as a pointer (one paragraph in
§4). If that framing is what Neil wants foregrounded for the grant's Path-5 application, I can promote it
to its own house-doc #5 rather than a paragraph here. Say the word.

*(Per write-session rules I did not email this; it will go in the daily digest. If your 2026-09-16 reply
already redirected this WRITE, treat the doc as superseded.)*
