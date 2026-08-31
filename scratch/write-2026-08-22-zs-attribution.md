# Write session 2026-08-22 — ZS re-attribution audit

## Task (from WRITE.md, honesty-driven bounded edit pass)
A 2026-08-25 full-text direct read CONFIRMED the core "agent composition = ZS
product of directed containers" is the HEADLINE THEOREM of **Ahman & Uustalu,
"Distributive laws of directed containers," Progress in Informatics 10 (2013),
pp. 3–18**. Not novel to me. No obstruction theory there ⟹ my `[ω]∈H²` is the
clean delta. INSERT that citation wherever the ZS construction is stated/relied
on; re-scope novelty to (i) applied reading + (ii) obstruction.

## The systemic error found
ALL my writeups cite only **"Directed containers as categories" (2016)** for the
ZS construction, and credit the *construction itself* to my own **"pairwise
Zappa–Szép criterion"** note. Two distinct problems:
- Wrong AU paper: the DCont≅Cat equivalence (2016) is cited correctly for T1, but
  the *distributive-law → ZS product* construction is the OTHER paper, AU **2013**.
- Over-claim: "distributive law ↔ matched pair ↔ ZS product" is presented as
  mine/pairwise, but it is AU 2013's. My genuine deltas: (L)+(G) *existence*
  criterion, the applied identification, and [ω]∈H².

## Canonical new bibitem
`D.~Ahman, T.~Uustalu. Distributive laws of directed containers.
Progress in Informatics, No.~10 (2013), pp.~3--18.`  (no arXiv/DOI; precursor CMCS 2012)

## Files to edit (mine, in projects/)
1. papers/containers-for-orchestration.tex — FLAGSHIP. add bibitem AU2013; cite at
   interleaving/ZS; re-scope T2 remark + dictionary star row + concl.
2. papers/applications-outlook.tex — "we have proved this product exists iff…";
   cite AU2013 for the construction, keep [ω] as delta.
3. papers/convergence-hub.tex — "Our own composition law … ZS weld C⋈D"; credit
   AU2013 for construction, scope novelty to obstruction.
4. expository/emergent-holonomy-is-ext.tex — mentions ZS as setup; add citation
   note where it introduces "orchestration is a ZS product."

## NOT edited (flagged for Robin instead)
- papers/category-of-containers.SEED-COPY.tex — a DEAD COPY of the seed book
  chapter "Composing systems: Zappa–Szép and distributive laws". Editing my copy
  doesn't reach the book. Robin maintains the seed. → note in for-robin/.
- Seed book drafts (git/ghani-containers/**) — Robin's; do not edit. → for-robin/.

## Changelog — DONE

### sources.json — NO edit needed
Entry `ahman-uustalu-2013-distributive-laws-directed-containers-pi13` ALREADY exists
at **deep-read** (full 18pp text obtained 2026-08-26; read log 2026-08-26.md; DOI
**10.2201/NIIPI.2013.10.2**). Also the CMCS-2012 extended-abstract twin
`ahman-uustalu-2012-distributive-laws-directed-containers` at deep-read. WRITE.md item 4
(registration) was already satisfied; I only propagated the DOI into the bibliographies.

### papers/containers-for-orchestration.tex (flagship) — 7 edits
- NEW `\bibitem{AhmanUustaluDL}` (PI 10, 2013, DOI).
- Abstract: parenthetical crediting the distributive-law construction to A.--U.
- Intro "The result": construction is A.--U.'s (\cite{AhmanUustaluDL}); pairwise criterion
  re-scoped to the *existence* question.
- Dictionary ★ row: construction A.--U.; **obstruction: this note**.
- §sec:zs preamble: T2's construction is A.--U.; author's part is only (L)+(G) existence.
- "Functor vs distributive law": weld-assembly credited to A.--U.
- "Status, honestly": T2 construction A.--U., author = (L)+(G) criterion.
Compiles: 10pp, 0 undefined.

### papers/applications-outlook.tex — 4 edits
- NEW `\bibitem{au-distlaw}` (DOI).
- "the classical problem" → construction is A.--U.'s \cite{au-distlaw}; we add *when* it exists.
- "What is ours / borrowed": ZS-product construction moved to borrowed (A.--U.); ours =
  existence-and-obstruction layer.
- §payoff "the part that is ours" → "existence-and-obstruction layer that is ours" + credit.
Compiles: 7pp, 0 undefined.

### papers/convergence-hub.tex — 4 edits
- NEW `\bibitem{AhmanUustaluDL}` (DOI).
- Convergence-discipline para: weld = A.--U.'s, we read into agents + add H².
- §Ours: weld-assembly credited to A.--U.; obstruction is the author's.
- Prop:contrast (ii): "the Zappa--Szép weld of Ahman--Uustalu, adding an obstruction in H²".
Compiles: 7pp, 0 undefined.

### expository/emergent-holonomy-is-ext.tex — 3 edits
- Intro: "that composing two directed containers this way is a ZS product is due to
  A.--U. \cite{au-distlaw}"; Ext content sits on top.
- NEW `\bibitem{au-distlaw}` (DOI).
- `macbeth-zs` internal-note title annotated "(after Ahman--Uustalu \cite{au-distlaw})".
Compiles: 10pp, 0 undefined.

## Provenance footprint (citation_check.py --report footprint)
- convergence-hub, applications-outlook, expository: floor deep-read (or no arXiv cites). CLEAN.
- containers-for-orchestration: floor = **agent-summary**, caused SOLELY by pre-existing
  citation `2605.12239` (Banu, "Harness Engineering as Categorical Architecture"). NOT touched
  by this pass, NOT ZS-related. Fixing needs a deep-read (browse session) — flagged, not fixed.

## Flagged for Robin (seed — I must not edit)
- papers/category-of-containers.SEED-COPY.tex — Ch "Composing systems: Zappa--Szép and
  distributive laws" (~L530--616): pairwise criterion is headline; needs the same A.--U. 2013
  credit for the distributive-law/matched-pair *construction*. (L615--616 already distinguishes
  the AU update-monad reading — good, but the core construction credit is missing.)
- git/ghani-containers/books/book.tex and papers/pairwise-zappa-szep.tex, dcont-cof.tex:
  same construction-credit gap; Robin maintains these on the host.
- Memory connection note connections/orchestration-is-zappa-szep-weld.md link (2) — the
  reference node already flags RE-ATTRIBUTE; a dream/wake cycle should apply it.

## Not done (correctly, per session rules)
- No email (staged nothing; wake session sends). No browsing. No new proofs. No Lean.
- The [ω]∈H² build is HELD (Neil's lowest priority) — untouched.
