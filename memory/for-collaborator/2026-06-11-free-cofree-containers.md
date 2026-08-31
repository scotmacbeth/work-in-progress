# Free monad & cofree comonad of a container, as containers — 2026-06-11 (prove)

> # ⛔ SUPERSEDED — DEMOTED 2026-07-14 BY A FULL-PDF NOVELTY AUDIT. DO NOT SEND THIS NOTE.
>
> **The cofree half below is SCOOPED IN FULL — not "the fact is cited, the derivation is mine".**
> **Niu–Spivak, arXiv:2312.00990:**
> - **Prop. 8.18 (p. 297)** — carrier `𝔱_p ≔ Σ_{T ∈ tree_p} y^{vtx(T)}`.
> - **Prop. 8.33 (p. 306)** — **the category**: objects = `p`-trees; morphisms out of `T` = **rooted
>   paths**; **codomain = the subtree at the path's end**; **identity = the empty path (the root)**;
>   **composition = concatenation.** ⇒ **That IS `o`=root / `↓`=subtree / `⊕`=concat, item for item.**
>   The "subtree category" below is their `T_p`. **The D1–D5 packaging is NOT my contribution.**
> - **Thm. 8.45 (p. 314)** — `U : Cat♯ → Poly` has right adjoint `T_(−)`; `Poly(𝔠,p) ≅ Cat♯(C,T_p)`.
>   With **Remark 7.18** (polynomial comonoid = comonad) that **is** the cofree-comonad theorem.
>
> **⚠️ AND IT WAS FACTUALLY WRONG.** The directions are **ALL FINITE ROOTED PATHS ≅ ALL VERTICES**
> `vtx(T)` — **not leaves, not root-to-leaf paths.** "nodes-as-paths" below is right only if "node"
> means *every vertex*; it was being read as maximal paths. (A category whose morphisms out of `T`
> were only the maximal paths would have **no identities**.) Also: the book **never displays a
> fixed-point equation**; **Ex. 8.16** only says `tree_p` is the **terminal `p`-coalgebra**
> (uncredited; classically **Adámek/Barr**) — so `νY.…` is not the book's presentation.
>
> **★ THE FREE HALF SURVIVES AND IS PROMOTED.** The book **never constructs the free monad**, and
> **characterising monads in Poly is Chapter 9, Question 11 — an explicit OPEN QUESTION.** That is a
> LIVE TARGET (Neil's Phase 2). Read **Gambino–Kock arXiv:0906.4931** in full first — for the *free*
> monad the directions genuinely ARE the **leaves**.
>
> → SUMMARY §5 · `questions/open-threads.md` · [[cofree-comonoid-scooped-and-wrong]]
>
> *Everything below is the 2026-06-11 record, kept verbatim for the chronology. Its "Honesty" section
> is itself dishonest — it under-claimed the scoop.*

**For Neil / Robin.** On Neil's "category of containers / free-cofree" agenda. Output: new
section `\S sec:freecofree` in `papers/category-of-containers.tex` (Phase-2 chapter),
pushed to branch `book-category-of-containers` (commit 4ecb4ab). Full proof record:
`projects/proofs/2026-06-11-cofree-free-containers.md`. Scripts: `projects/scratch/cofree_*.py`.

## Result (one line)
For `C = S◁P`: the **free monad** `C* = (μ-tree-with-variable-leaves) ◁ (variable-leaf set)`;
the **cofree comonad** `C^∞ = (M-type tree) ◁ (nodes-as-finite-paths)`. The (co)monad laws
are *exactly* the monoid laws of tree **grafting** (free) and path **concatenation** (cofree).

## The pretty part (ties straight into Ch. comonoids)
`C^∞` is a **directed container**: root `o(w)=•`, sub-shape `w↓n = w/n` (subtree at node `n`),
shift `n⊕m = n·m` (concat). D1–D5 hold, the only non-formal one being `w/(n·m)=(w/n)/m`.
So by our own ACU theorem (`thm:comonad`) the cofree comonad *is* the cofree **directed**
container — and the book's general `δ(s,v)=(s,λp.(s↓p,λq.v(p⊕q)))` instantiates to
"relabel every node by its subtree". The corresponding small category is the **subtree
category**: objects = trees, morphism `w→w'` = a node `n` with `w/n=w'`, id = root, comp =
concat. For `C=1+X` this is the `head/tails` comonad on nonempty colists, category `(ℕ̄,≥)`.

## Honesty
NOT claiming novelty of the *fact*: cofree comonoid = tree comonoid is Spivak–Niu; polynomial
comonad = category is ACU. **MacBeth contribution** = the self-contained container-language
derivation (positions as variable-leaves / nodes-as-paths), the structure maps written as
container morphisms with exact backward maps (id-iso / root / concat), the law-reduction to
grafting/concat, and the D1–D5 directed-container packaging + exhaustive small-case checks.

## Verified
Comonad laws (counit×2, coassoc) and monad laws (unit×2, assoc) PASS by exhaustive enumeration
on Maybe and binary containers; D1–D5 PASS likewise. (Truncated finite trees; laws equational.)

## Open / asks
- **[cite-check]** exact theorem numbers in Spivak (2021, arXiv:2111.10968) and Spivak–Niu
  *Polynomial Functors* for the cofree comonoid / tree-polynomial statements — next browse.
- Natural **/lean** target: formalise "C^∞ is a directed container (D1–D5)" reusing the M2/M2b
  comonad↔dircont machinery — the laws are `o=•`, `↓=subtree`, `⊕=concat`; D4/D5 are
  `w/(n·m)=(w/n)/m` and concat-assoc. Low-risk, high grant value (verified cofree comonad).
- Dual question worth a look: free monad as the free `◁`-monoid — is there a clean
  "co-directed container" packaging mirroring D1–D5? (grafting unit/assoc as 5 laws.)
