# Book Ch "Algebraic structure on Cont" — new "Closing the structures" section (2026-07-21 write session)

**For Neil / Robin.** This is the write-up you steered on 07-21 (UID-71): the closed-structure
material for the book, at the honesty level of the email "closed structure spelled out."

## Where it lives
`projects/books/category-of-containers.tex`, section `\label{sec:closed}` ("Closing the
structures"), inserted into the *Algebraic structure on Cont* chapter **immediately before**
the (co)monoid table — which stays the chapter's closer, as you asked. It **replaces** the old
one-paragraph `Definition[Closed structures]` placeholder (that placeholder cited only Spivak's
*Functorial Aggregation*, which I have read at abstract-grade only; it is now gone from this
section). Book compiles clean: 36 pp, no undefined refs/citations.

## What the section does, in order (compute-first, book voice)
1. **The Dirichlet closure as a hom of morphisms.** I compute the transpose by hand and land on
   your morphism form: `[p,q] = (Cont(p,q), f ↦ Σ_{i∈S_p} q[f₁ i])` — shapes *are* morphisms, a
   position is a p-shape plus a q-position over the delegated shape. Prompt/response reading
   included. **Attributed plainly** to Niu–Spivak Ex 4.78 (4.79) and Spivak 2202.00534 Eq (44);
   the mechanisation `DirichletClosed.lean` is flagged as mine.
2. **The same hom as a product of composites:** `[p,q] ≅ Π_{i∈S_p} q ◁ (p[i]·y)`, via ΠΣ≅ΣΠ.
   This is now **Lean-verified** (`DirichletHomPi.lean`, `Container.ihomPiIso`, axiom-free,
   finished today) — so the Π-form is no longer paper-only; that closes the caveat I gave you.
3. **The uniform criterion (the one new bit).** For a Day tensor ⊙_⋆: **left-closed ⇔ (−)⋆B is
   polynomial for every set B**, and then the internal hom is `Π_i q ◁ (p[i]⋆y)`. Your objection
   — the internal hom is a right-Kan-type object and need *not* be a container — is stated as the
   motivation, and the polynomiality side-condition is exactly the answer to "when it is." The
   **necessity is one line** (evaluate closure at `[y^B,y]_⋆`, read off `(−)⋆B` by co-Yoneda).
   The three concrete closures (×, ⊗, ▷_S) are attributed as prior art; only the biconditional +
   necessity reduction are claimed.
4. **"Is the condition ever really a condition?"** — the vacuity question, **honestly open**. I
   did *not* claim it resolved. Instead the pedagogical beat you'll like: a teachbox
   **"provenance = polynomiality = coherence,"** with the **support tensor** as the cautionary
   example — a bifunctor that passes pentagon *and* triangle on cardinalities yet has **no natural
   associator**, because its single separator point can't record which elements it separated. That
   failure *is* the reason polynomiality and coherence are the same constraint.
5. **The other three, briefly:** × cartesian-closed (= the criterion at ⋆=+) but not locally CC;
   ◁ not left-closed but with Meyers' right coclosure (+ the NS/Spivak naming clash).
6. **Boundary:** one paragraph pointing at ⋉/⋊ (Dialectica, DJN 2305.05655) as non-convolutional —
   ⋉ not closed, ⋊ directed-left-closed — flagged as the edge of the census, full treatment deferred
   to the fibrational chapter per your steer.

## Honesty ledger
- No originality claimed for the three concrete closures. Morphism form = Spivak/NS; Π-form is a
  repackaging (the identity + its Lean proof are mine). **New = the uniform biconditional + the
  one-line necessity.** Vacuity = open.
- Handedness fixed vs. the old `four-monoidal-chapter.tex` draft: the condition is left-slot
  `(−)⋆B` polynomial, matching the formula `R⋆p[i]`. (The old draft had the necessity as
  `[speculative]` and the condition on the wrong slot; both corrected.)

## Two things for you
- **Sharing:** repo push is still 404 for me (policy). The section is in the projects volume you
  can read directly; the shared `scotmacbeth/ghani-containers` mirror is the fallback if you want it
  pushed — say the word and I'll target that in a non-write session.
- **Citation hygiene flag (not this section):** the whole-book citation floor is `agent-summary`,
  coming from Shapiro–Spivak 2405.13157 in the DCont≅Cof chapter. My closed section is clean
  (all ≥ deep-read). That one wants a deep-read in a browse session before the book ships.

Scratch/decisions: `scratch/write-2026-07-21-book.md`.
