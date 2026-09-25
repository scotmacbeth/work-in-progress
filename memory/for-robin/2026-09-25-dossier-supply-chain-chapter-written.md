# Dossier: supply-chain chapter body written out (2026-09-25 WRITE)

**What:** The supply-chain application chapter of the grant dossier was a stub
(3.9 KB, "body not yet written"). It is now a full chapter, on par with the GA
and blockchain siblings.

**Where:**
- File: `papers/dossier/staging/app-supply.tex` (`\input` into `dossier.tex`, Applications part)
- Pushed: `work-in-progress` repo, `main`, commit **b5c45e2**
  <https://github.com/scotmacbeth/work-in-progress/commit/b5c45e2>
- Built PDF: `papers/dossier/dossier.pdf` — **104 pp** (was 100), pdflatex clean, 0 undefined refs.

**Source (not re-proved — assembled):**
- `proofs/2026-07-23-supply-chain-zs.tex` (the computed worked example)
- `proofs/registry/supply-chain-zs.json` (grade of record)
- machine-check `scratch/supply_chain_zs.py` (8 (n,ε) pairs)

**The math it now presents:**
1. Base chain `Src<Mfg<Dst` as an explicit directed container (object-level dividend of DCont≃Cat).
2. Warehouse family `W_{n,ε}` with a cyclic **lot-cursor** τ of order n at the shared node;
   right factor D = warehouse-internal relabellings.
3. (L) + abelian-vertex hypothesis hold uniformly in ε ⟹ criterion applies.
4. Orbit category, `H²(Sk_C;Z/n) ≅ Z/n`, and the headline **`[ω] = ε`** — the class *measures*
   the inventory discrepancy **in units**, not just a yes/no bit.
5. Dichotomy: `W_{n,ε} = C ⋈ D` exists ⟺ ε=0 ⟺ both routes agree on lot-provenance
   (#SFS = n vs 0 cross-check).
6. Why Z/n not parity: B²=⟨(1,1)⟩ = freedom to choose "slot zero"; only the difference ε
   is observable = flat Z/n-bundle trivial iff holonomy vanishes. n=2 = the proved re-entrancy bit.
7. Olog-merge sibling at n=2 (schema naming-convention clash = [ω]=1).

**Honesty (unchanged from registry):** general theorems cited at their grades and NOT re-graded
(DCont≃Cat lean-verified; pairwise ZS + (G)=[ω] proved; n=2 anchor proved). Domain instantiation
= **computed**. Object-level fidelity ("a real supply chain *is* a category", SEED Q4) kept
**OPEN** — faithful minimal abstraction, not a fidelity claim.

**Citations:** only `AU16` (Ahman–Uustalu) and `rw` (Rosebrugh–Wood) — both already in the
dossier bib, both published; no new bibitems, citation floor deep-read.

**Notes / small stale-comment flag:**
- The security chapter (`app-security.tex`) was already a full body (done 2026-09-24), so the
  P4b "STILL OWED: supply + security bodies" line is now fully cleared. WRITE.md updated.
- `app-security.tex` has a trailing *comment* claiming the blockchain chapter "currently carries
  no \label{ch:blockchain}". That is **stale** — the label is present (app-blockchain.tex line 2)
  and all refs resolve. Comment only; harmless. Left for a future tidy pass.
- Tax chapter stays GAP/illustrative (untouched, as briefed).

**Still owed on the dossier (not this session):** browse-TODOs — register arXiv:2009.06835
(Clarke, eqchain sub-floor) and reconcile the 2601.22968 Chen id-collision so M5/M6 can carry a
formal bibitem.
