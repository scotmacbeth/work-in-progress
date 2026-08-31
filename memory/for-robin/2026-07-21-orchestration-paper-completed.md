# containers-for-orchestration.tex — completed (WRITE session 2026-07-21)

**File:** `projects/papers/containers-for-orchestration.tex` (+ `.pdf`, 10 pp, compiles clean, no
overfull/undefined). Readable from the host on the projects volume.

## What this session did
The 07-20 draft was already structurally complete. The WRITE.md gap was the **differentiator
material** — the 07-21 browse surfaced a *third* categorical-orchestration effort (Waites, n-Café
Mar 2026) that the 07-20 draft predated. I completed §4 accordingly:

- New subsection **"The categorical-orchestration landscape"** placing all three 2026 neighbours and
  a 4-row table (mechanism vs two-agent obstruction): **Aberlé** (parallel sum), **Banu 2607.04240**
  (operad, author checks — no ZS), **Waites** (copy–discard SMC + traced feedback + session types;
  failure = memory-compaction, patched with a mutex/serialisation gate). Then this note's row:
  distributive law / `C⋈D`, obstruction `[ω]∈H²`.
- The sharp one-liner (per Neil/Rick's "sharpest contrast" steer): **both Waites and we reach for
  "serialisation"** — Waites installs a gate as an engineering remedy; we characterise exactly *when
  serialisation is impossible* (the unprotected-re-entry regime `K_1`, `[ω]`=generator).

## Two citation corrections worth flagging
1. The draft's `banu` bibitem cites **2607.04240 "Biological Motifs for Agentic Control"** — this is
   **deep-read and correct**. (WRITE.md pointed me at ArchAgents 2605.12239, but that one is only
   *agent-summary* in sources.json, so citation discipline forbids citing it as a paper reference. I
   kept the deep-read sibling. I also removed the draft's stray "memory as coalgebraic state" phrase,
   which actually described 2605.12239, not 2607.04240.)
2. **Waites** is a blog post (two n-Café URLs), read in full first-hand on 07-21 and documented in
   `reading/2026-07-21-browse2.md`. It is **not** in `sources.json` because `validate_index` rejects
   non-arXiv keys; provenance lives in the read log. Cited by URL.

`citation_check.py --report footprint` → **provenance floor: deep-read**. Clean.

## Open follow-up (for a future browse session, not this one)
**ArchAgents arXiv:2605.12239 (Banu)** is still only agent-summary. If we want it as a formal
citation (it's a genuine differentiator — operads + coalgebraic memory), it needs a deep-read to
upgrade its `sources.json` entry first. Until then it stays uncited.

## Honesty ledger (unchanged, restated)
T1 (DCont≅Cat) = Ahman–Uustalu; T2 (pairwise-ZS) = mine; T3 ((G)⟺[ω]=0) cites RW/Baues–Wirsching/
Pirashvili — no new cohomology. The interface/free-monad/wiring-diagram/dependent-spec mechanism is
Aberlé's, cited, not reinvented. The delta is `C⋈D` + `H²` only. The two extra table regimes
(product, `S₃`) and the "real framework instantiates `K_ε`" reading are labelled *computed*, not
proved; empirical validation is explicit future work.

No email sent (write-session rule). Flag me if you'd like this pushed to
`scotmacbeth/ghani-containers` or mailed to Neil.
