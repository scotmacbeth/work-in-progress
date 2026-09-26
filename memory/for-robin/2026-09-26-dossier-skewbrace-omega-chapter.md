# Note for Robin — skew-brace [Ω] dossier chapter drafted (2026-09-26 WRITE)

**What:** The owed skew-brace decomposition-obstruction chapter now exists as a standalone
staging fragment: `papers/dossier/staging/app-skewbrace-omega.tex` (~11pp of chapter body,
13pp with the standalone title/TOC). It is **NOT yet `\input` into `dossier.tex`** — per
WRITE.md, held reversibly pending Neil's steer on whether the [Ω] lane becomes its own pillar
chapter or stays a research thread feeding the ZS-existence spine.

**Verify it compiles:** `pdflatex _standalone-omega.tex` (twice) in `papers/dossier/staging/`.
Clean build, 0 errors, 0 undefined refs/citations, 0 overfull boxes. Readable PDF at
`staging/_standalone-omega.pdf`. The wrapper `_standalone-omega.tex` supplies the dossier
preamble + the two bib entries; the fragment uses `\providecommand` guards so it will also
compile once `\input` into the dossier.

**The chapter's arc (three theorems, honest grades inline):**
1. **Identification** [peer-reviewed, Rick]: [Ω] = Rathee–Yadav H²_Sb class (trivial-kernel SH);
   [Ω]=0 ⟺ bicrossed product ⟺ sub-skew-brace complement. No coprimality.
2. **Bilinearity** [proved]: [Ω] strictly finer than both group Schreier classes — the product
   map Φ=(φ∘,φ₊) has a kernel (W4 = Z2×Z4, both group extensions split, no common complement).
   Base-localised (heap-transport refuted; star complement is the right invariant).
3. **Independence** [proved]: residue [ν] is an orthogonal direct factor; Ext ≅ R × Ω⁰ with Ω⁰
   residue-independent. Gauge-orbit product is FALSE (orthogonality at the class level only).
   Non-trivial kernels don't disturb [Ω]. The |G|=16 corner (Z2×Z8, L={1,5}⊊Aut(D)) is the
   genuine witness that this isn't a |D|=4 size artifact — graded [computed]; the one open step
   (surjectivity of the residue map for [β]≠0) is stated precisely and does NOT touch the
   product structure.

**Honesty handling you'll want to know about — matches your commit 6d32c50 exactly:**
- **Socle claim deleted.** The peer-reviewed proof file still carries a "separation requires
  D⊄Soc(G)" gloss; I did NOT reproduce it (your Rick-referee witness: sb#1 has D=Soc(G) exactly
  yet separates). The chapter's honesty ledger records the deletion explicitly.
- **No Letourmy–Vendramin.** One proof file's open-gap note referenced a phantom LV deep-read;
  since (per your commit) that = the RY self-cite 2102.12235, I phrase the general non-trivial-
  kernel housing as *native/unpublished* and cite nobody for it.
- **Citation floor = deep-read.** I do NOT cite 2102.12235 (only `agent-summary` in sources.json,
  below the write-session floor). β=dθ is attributed to the deep-read RY extension paper
  2601.12371 instead. `citation_check --report footprint` on the fragment: floor deep-read. There
  is a **browse-TODO** left in a comment: deep-read 2102.12235 if we ever want to cite it precisely.
- **On merge:** the fragment needs one new bibitem added to the dossier bib —
  `\bibitem{RatheeYadavExt}` (2601.12371). `\cite{ferri-qsb}` is already there. The suggested
  bibitem is in a comment at the top of the fragment.

**Answers Ferri Rmk 3.20** (group-theoretic reformulation of quiver-skew-brace prunability):
prunability = vanishing of the single bilinear class [Ω]; and the bilinearity theorem explains
*why* no single-operation group criterion can suffice.

Scratch/decisions: `scratch/write-2026-09-26.md`. — MacBeth
