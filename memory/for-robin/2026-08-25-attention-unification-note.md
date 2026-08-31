# For Robin / Neil — attention unification note drafted (WRITE, 2026-08-25)

**File:** `projects/papers/vec-attention-unification.tex` (+ `.pdf`, 8pp, compiles clean).
**Title:** *The attention layer is not where the depth is: a stacking law for categorical accounts of attention.*

This is the note WRITE.md asked for, written to Neil's depth bar (UID 121: "if these attention
papers say nothing deep about LLMs, I'm not interested"). It is grant-facing, in the plain register
of `vcont-plain-note.tex`, with proved / reported / proposal flagged throughout.

## The argument in one line
The single attention layer is where every categorical account agrees and where none says anything a
transformer engineer doesn't already know; the mathematics that *matters* is how the layers **stack**,
and that is a free monoid whose unit is the residual connection and whose only obstruction to collapse
is a polynomial degree that triples with depth.

## The two things that clear Neil's bar (a practitioner didn't have these)
1. **Residual = the algebraic unit.** Stacking linear self-attention is the free ◁-monoid on the
   one-shape linear container `(⋆,AttP)`, i.e. the tensor algebra `⊕_L AttP^{⊗L}`. The skip connection
   is exactly the degree-0 unit; drop it and a stack stops being a sum-over-depths and becomes one
   non-terminating tower. En route this **corrects O'Neill's published Thm 3.2**: the free monad is the
   coproduct `⊕_L F^L` (Adámek partial sums), not the colimit of bare layer-powers `F^L` he names — F is
   pointable but not well-pointed, and the residual is the pointing. (Proofs: 08-23; Lean `Free.lean`
   sorry-free.)
2. **Degree exactly 3^L.** A live (trained, data-dependent) depth-L linear-attention stack with identity
   feature map is homogeneous of degree exactly 3^L in its inputs — a hard obstruction to the common
   "deep attention is one big matrix" intuition. The in-context / KV-cache regime is pinned as the exact
   exception where depth *does* collapse (to the Mat(Vec) product ⊙, contexts by ⊕). Softmax is further
   out again (Sargsyan: not functorial; Mahadevan §10.6: not representable). (Proof: 08-22.)

## Honesty decisions you should know about
- **Only 3 of the 5 lineages are cited.** O'Neill, Vertechi, Mahadevan-KET are all `deep-read` in the
  ledger. Maruyama and Hedges (generalized-transformers / autodiff) are only `agent-summary`, and the
  session citation rule forbids citing a browse-agent paraphrase as a reference. I did **not** force the
  five-count: they go in a one-line "reported, not verified this cycle — neither cited nor relied on"
  footnote. The note's value is the depth law + degree bound, which stand regardless of the lineage count.
  If you want the full five in the bibliography, the fix is a browse session deep-reading
  arXiv:2511.18417 (Maruyama) and the two Hedges pieces; then I upgrade and re-cite.
- **The full unification is a PROPOSAL, not a theorem.** O'Neill is proved-inside. Vertechi is placed at
  the computed level; Mahadevan's coend is read as the representable-rung case (his §10.6 caveat = the
  linear/nonlinear boundary). I state this as thesis-with-evidence and say so in §5.
- **Prior art credited, not re-claimed.** The ◁-monoid / comonoid-=-enriched-category machinery is
  Dorta–Jarvis–Niu (arXiv:2305.05655, Thm 4.3) over a general base. ⚠ **2026-08-31 rescoping:** their
  composition product is the **weighted `◁_DJN`** (outer `u` multiplied in, Def 3.5/Lemma 3.6 p. 89) and
  coincides with my `◁` **only at `C=1`**; their `⊗` does coincide with mine. DJN remains the prior art for
  the general-base *construction*, but not for a composition-representing `◁` over a general base. My delta is the *attention instance*
  + the depth-composition law + the degree bound, not the machinery. Said explicitly in the intro.
- **One ledger fix.** O'Neill's `sources.json` entry was keyed by a slug, so `citation_check --report
  footprint` couldn't resolve `2501.02931` and flagged it UNREGISTERED even though it is genuinely
  deep-read (read log 2026-08-26). I added an arXiv-id-keyed alias `2501.02931` mirroring the deep-read
  record. (There are ~88 slug-keyed sources in the ledger generally — a broader housekeeping item, not
  touched this session.) Footprint now: floor `deep-read`, all four arXiv cites resolve.

## Open TODOs (for later PROVE/browse sessions, NOT done here)
- Deep-read Vertechi's actual paper (only lecture slides are in the ledger) and Maruyama/Hedges, to
  promote the proposal toward a theorem and expand the bibliography honestly.
- The general-φ degree statement is left open (only φ=id is proved exactly 3^L); flagged in-text.

Grant fit: this is an **Applications**-section piece — a published transformer construction placed inside
the Kodamai container framework, with a correction to the literature and a quantitative boundary. Happy to
turn it into an arXiv note or fold into the grant narrative on your steer.

— MacBeth
