# Workers section landed in the book — for Neil / Robin (2026-07-29 write session)

**File:** `projects/books/category-of-containers.tex` (working copy; the seed's own book stays
off GitHub — read it from the projects volume or ask me to email the source).
**Status:** compiles clean, **60 pp**, **0 undefined refs**, 0 font warnings. Backup at
`/tmp/coc-backup-workers.tex`.

## What I added
A new section **"Processes with state: the store comonad and the category of Workers"**
(`sec:moncomon-workers`), in the "Monads and comonads" chapter, right after the entwining
section — the natural "processes with state" capstone. It writes up the PROVED result in
`proofs/2026-07-28-delta-state-object-and-workers.md`:

- **State object** `ΔS=(S,s↦S)` = codiscrete category (via the object dictionary) ⟹ **store
  comonad** `S×X^S` (Uustalu–Vene); the reader `X^S` is the read-only shadow, the `S×` factor is
  your "something more" — the writeback.
- **Worker** `p→q` with state `S` = a container map `ΔS⊗p→q`; coordinates split the backward map
  into a **writeback** `f♯₁` and the ordinary position map `f♯₂`.
- **Lemma** `ΔS⊗ΔT=Δ(S×T)` (strict) ⟹ composition **multiplies the state to `S×T`**. Exactly your
  prediction. One-line remark on why `⊗` and not `×` (the product mis-sizes the fibre to `|S|+|T|`).
- **Theorem:** Workers = a category **graded by `(Set,×)`** = coKleisli of the graded comonad
  `S↦ΔS⊗−`. Tagged **Lean-verified** (`Workers.lean` + `StateComonad.lean`, both built) with the
  Preface footnote (files are in the `lean/` tree, not committed to the book tree).

## The two neighbour citations you flagged — both handled
1. **Capucci–Myers, "Contextads as Wreaths" (2410.21889)** — cited as the **nearest neighbour** in
   `rem:workers-para`. I self-identify Workers precisely by their **Example 3.24**: with `M=(Set,×)`
   it is the **trivially-fibred / colax-action corner** of their `Ctx` framework. Their **Theorem A.4**
   (left unproven) is the **opposite, dependency-essential corner** (dependent grade `X→S` over one
   monad's shapes, multiplying via `seq`). I say plainly: **we settle no fragment of A.4.** This one
   is load-bearing and rests on a **deep-read** source.
2. **Spivak, "Categories by Kan extension" (2503.21974)** — ONE neighbour sentence added to the
   entwining scope remark (`rem:entwine-scope`): different carrier (`(Set,◁)`), orientation
   (density comonad builds a *new base category*), and output. Flagged as not-prior-art.

## Honesty notes (please sanity-check)
- **Para** (S varies): I keep it as **computed / further work**, honest that `Δ` is functorial only
  on **bijections** (Core(Set)), so over all of `Set` it's a *graded* category, not a strict actegory.
- **Provenance debt:** the Spivak-Kan cite is only at **abstract** level and the Gavranović/Para cite
  is **unregistered** in my reading tracker — both flagged in-text and in the reading tracker as
  **deep-read TODOs**. A future browse session should upgrade them. The load-bearing neighbour
  (Capucci–Myers) is deep-read, so the one claim that matters is on solid ground.
- **Two axes** (grant): added a short paragraph — Workers = the **state axis** (context multiplies
  `S×T`, no obstruction, grade accumulates), dual to the ZS **directed axis** (`[ω]∈H²`, may fail).
- **Effect–coeffect** (your 07-29 steer): a forward-pointer teachbox only, `[in development]`. I was
  careful NOT to name `λ` as the compositor — per the 07-29 prove result the arrow compositor is the
  *reverse* law `κ` (branching-obstructed), so the box says "a distributive law relating the two
  feeds; which orientation, and under what condition, is the branching dichotomy, worked separately."

## Open questions for you
- Happy with "graded category over `(Set,×)` / coKleisli of the graded comonad" as the headline, with
  Para as a remark? Or would you rather Para be the headline?
- The Capucci–Myers Example-3.24 embedding is my own framing (not stated in their paper) — does it
  read correctly to you?
