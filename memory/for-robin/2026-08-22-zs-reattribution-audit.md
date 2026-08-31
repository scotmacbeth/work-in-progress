# ZS re-attribution audit — write session 2026-08-22

**Robin / Neil** — this closes the honesty item Neil was told about on 2026-08-25:
the core "agent composition = Zappa–Szép product of directed containers" line is **not
novel to me**. It is the headline theorem of

> D. Ahman & T. Uustalu, *Distributive laws of directed containers*, Progress in
> Informatics **10** (2013), 3–18, DOI 10.2201/NIIPI.2013.10.2.

Their **matching pair** = my `λ: N×P → P×N` mutual-action combinator; the single-shape
case specializes to the monoid ZS product. Their paper has **no** obstruction/cohomology
content (grep-confirmed), so my surviving delta is only **(i)** the applied re-reading
(agents/workflows/supply-chains) and **(ii)** the obstruction `[ω] ∈ H²(Sk_C; 𝒟)`
measuring when the composition fails / is non-associative (re-entrancy). The "strict
factorization system" packaging is mine; the matching-pair ↔ compatible-composition ↔
distributive-law *content* is theirs.

## What I edited (my projects/, all recompile clean)
| file | pp | edits |
|---|---|---|
| papers/containers-for-orchestration.tex | 10 | new bibitem + 6 in-text credits/re-scopes |
| papers/applications-outlook.tex | 7 | new bibitem + 3 re-scopes |
| papers/convergence-hub.tex | 7 | new bibitem + 3 re-scopes |
| expository/emergent-holonomy-is-ext.tex | 10 | new bibitem + 2 credits |

Full per-edit changelog: `scratch/write-2026-08-22-zs-attribution.md`.
`sources.json` already had the paper at **deep-read** (read 2026-08-26) — no change needed
there beyond propagating the DOI into the bibliographies.

## What I did NOT edit — needs you (host-side seed) or a later cycle
1. **papers/category-of-containers.SEED-COPY.tex** (a dead sync-copy) and the authoritative
   **git/ghani-containers/books/book.tex**, **papers/pairwise-zappa-szep.tex**,
   **papers/dcont-cof.tex** — the chapter *"Composing systems: Zappa–Szép and distributive
   laws"* (~L530–616 in the copy) presents the pairwise criterion as the headline and does
   **not** credit AU 2013 for the distributive-law/matched-pair *construction*. Same one-line
   fix: cite AU 2013 as the source of the construction, keep (L)+(G) and [ω] as the deltas.
   (L615–616 already correctly distinguishes the AU update-monad reading.)
2. **connections/orchestration-is-zappa-szep-weld.md** — link (2) still needs the
   re-attribution the reference node flags; a dream/wake cycle should apply it.

## One unrelated provenance flag (pre-existing, out of scope)
`containers-for-orchestration.tex` cites **Banu 2605.12239** ("Harness Engineering as
Categorical Architecture") at `agent-summary` provenance — below the deep-read floor.
Not ZS-related, not touched here; needs a browse-session deep-read before that paper stays
as a hard reference.

— MacBeth
