# Orchestration composition = Zappa–Szép product — the dictionary is now COMPUTED

*2026-07-19 deep-work (PROVE). Deliverable: `proofs/2026-07-19-orchestration-zs-instantiation.tex`
(4pp, compiles), registry `proofs/registry/orchestration-zs.json` (validates, computed),
scripts `scratch/orchestration_zs{,2,3}.py` (all machine-checked).*

## What this session did

The orchestration=ZS thread was **speculative** — the abstract theorems existed but the dictionary
("a supervisor/worker pattern literally presents as a directed container and its concurrency as a
distributive law") had **no worked instantiation**. This session builds the smallest non-trivial case
and computes it. Grade moves speculative → **computed**.

## The model (one bit decides everything)

Supervisor–worker orchestration as a small category: roles `S,W,R`; supervisor holds a 1-bit **turn
token** `τ` (τ²=1, so `End(S)⊇Z/2`); dispatches `p,pτ:S→W`; two worker outcomes `s,s₂:W→R`
(`s`=normal return, `s₂`=**re-enters** before returning); results `q,qτ:S→R`. Prescribed right factor
`D` = supervisor-internal token moves `{1_S,τ,1_W,1_R}`.

**The only thing that varies is one composite** — how a worker outcome sits relative to the token:
- **bug (unprotected re-entry):** `s∘p=q` but `s₂∘p=qτ` — the re-entrant branch **mutates the
  supervisor's shared state** (flips the token).
- **ok (locked):** `s₂∘p=q` too — outcome decoupled from token.

## Results (all machine-checked)

| topology | verdict | invariant |
|---|---|---|
| independent supervisors (read-only workers) | **composes** | K=C×D, trivial law δ=swap |
| two supervisors, coherent nontrivial interleave | **composes** | K=S₃=Z/3⋊Z/2, non-abelian join |
| re-entry, state-protected (lock) | **composes** | #SFS=2 (Z/2 torsor), [ω]=0 |
| re-entry, **unprotected** | **OBSTRUCTED** | #SFS=0, **[ω]=generator of Z/2** |

- **K_bug ≅ the rigid twist** (explicit iso matching D, verified) ⇒ (L) holds, (G) fails,
  `H²(Sk;Z/2)≅Z/2`, `[ω]`=generator — transferred verbatim from the g-obstruction proof (T3).
- K_ok's extracted distributive law satisfies ZS1–ZS4. The two SFS = the Z/2 torsor ⇒ `[ω]=0`.
- Hand-computation reconciles exactly with the code (the R-basis can hold q **or** qτ, never both;
  `s∘p=q, s₂∘p=qτ` forces both ⇒ contradiction ⇒ (G) fails).

## The one-sentence payoff (for the grant Impact narrative)

**The single bit that flips "composable" to "obstructed" is whether a worker's outcome mutates the
supervisor's shared state.** If it does, the distributive law `δ:D◁C→C◁D` becomes multivalued, (G)
fails, and the obstruction to a single consistent joint agent is the nonzero `[ω]∈H²(Sk_C;𝒟)`. This
is the SEED's "Ethereum re-entrancy = failed distributive law", now an explicit computed H² generator
on a handoff category — and the degree-axis contrast with MAS sheaf-Laplacian methods (H⁰ consensus /
H¹ identifiability on the *communication* graph vs H² composability on the *handoff* category) is exact.

## Honesty ledger

- **Cited, not mine:** T1 Ahman–Uustalu (DCont≅Cat, Lean), T2 pairwise-ZS (mine, proved), T3
  Rosebrugh–Wood/Baues–Wirsching/Pirashvili (H²). interface=container, dynamics=coalgebra = Spivak.
- **New (computed):** the instantiation + the topology→composable table. **No new cohomology.** Models
  are minimal faithful abstractions — I do **not** claim any named framework (LangGraph etc.) *is*
  literally one of these (that node is a dead-end in the registry; the GA-style empirical validation is
  the future step, not done here). S₃ two-supervisor reading is illustrative.

## Next / open

- Empirical analogue (the GA move): map an actual orchestration trace onto `(S◁P,o,↓,⊕)` and observe
  the obstruction — turns computed → validated. Candidate WRITE / grant-Impact subsection pending Neil.
- Verify-first hinge still open: Fairbanks 2607.15091 "Comonads as Spaces" (comonads generalise DCont
  AND sheaves) held only at agent-summary depth — read before leaning on it as the reason the two
  universes (handoff-H² and communication-sheaf) must meet.
