# Paper draft: "When does substitution exist? Admissibility of the composition product on Fam(C^op)"

**MacBeth — 2026-09-01 (WRITE session).** For Robin (and Rick, per PROTOCOL §4.2 before it moves).

## What it is
A self-contained research note turning five proved results into one publishable story: a **map of
the bases `C` over which `Fam(C^op)` carries the composition product `◁`**. Not a gradation — a
near-dichotomy with sharp mechanisms.

- **File:** `projects/papers/admissibility-composition-product.tex` (+ compiled `.pdf`).
- **Compiles:** `pdflatex`, clean — 17 pp, no undefined refs, no overfull boxes, amsart.
- **Audience:** category theorists who know Poly/containers (Spivak circle, Ahman/Uustalu, Neil).

## The one-sentence claim
On the extensive pole the *mere existence* of `◁` forces a connected unit (hence fully-faithful
extension, canonical `◁`, and the reindexing left adjoint for every `q`); the additive pole collapses
`◁` to `⊗`; the middle is thin but inhabited (`Set×Vec_fd`); and connectedness of the unit is
**necessary but not sufficient** — `Gl((−)²)` is a connected-unit topos that is still inadmissible
(Weichsel). Behind it all: connected unit ⟹ `◁` determined by `C`; disconnected ⟹ `◁` is a choice.

## What each section delivers
- Shape Lemma (the one necessary condition) → §3.
- Extensive rigidity (admissible ⟹ connected) + forced package (Thm 1 left adjoint) → §4.
- Collapse (all-tiny ⟹ disconnected; left adjoint iff |T|=1) → §5.
- Three inadmissible bases: Set×Set, Set_* (degree a=−4), **Gl((−)²)** (π₀ not multiplicative) → §6.
- Middle inhabited: Set×Vec_fd; Thm B not sharp; per-object "absorptive" reformulation → §7.
- Determinacy (the organising climax) → §8.
- Map summarised as a 6-row table in the introduction.

## Status / grades (honest)
- All numbered theorems **proved**. Set×Vec_fd admissibility is **proved on the finite-vec-support
  locus 𝒫** (explicit natural iso, both components built as maps, verified); full-`Vec` infinite
  case is **open** (stated as such). Decomposition (Conj 7.x) flagged as **conjecture**.
- Sources cited at **deep-read**: DJN 2305.05655, Niu–Spivak 2312.00990, Gambino–Kock 0906.4931.
  `citation_check.py --report footprint` → floor **deep-read** for all machine-detected cites.
- Classical named results cited as standard and **independently verified in code** (not browse-agent
  paraphrase): Weichsel 1962 (π₀(K×K)=2), Mac Lane–Moerdijk / Carboni–Johnstone (Artin gluing is a
  topos), Carboni–Lack–Walters (extensive-category basics), AAG (foundational). The note's
  "Provenance and status" paragraph says this explicitly.
- `◁` vs `◁_DJN` kept **distinct** throughout (their product is weighted; agrees only at C=1; their
  `⊗` does match mine). Remark 8.x states this; intro says Thm B answers a base-condition question
  DJN §6 leave open.

## What I am LEAST sure about (PROTOCOL §4.3–4.4 — not optional)
1. **Is the Shape Lemma sufficient (with extensivity)?** It is necessary; Gl((−)²) shows it can fail
   on a connected-unit extensive base. Whether "Shape Lemma + extensivity ⟹ admissible" holds is
   **open**. Sufficiency needs the *internal* distributivity identity, not just the external hom-set.
2. **Is there an irreducible (indecomposable) middle inhabitant?** Set×Vec_fd is a *product*. The
   irreducible case is pinned between two open doors (additive non-fg = full-Vec Gap 1; and the
   conjecture that every γ-non-injective closed base is inadmissible). I have **no** irreducible one.
3. **Novelty gate not exhaustively closed.** DJN disambiguation done; CLW E1/E2 likely folklore
   (claimed nothing); but "has anyone classified admissible bases for the *external-shape*
   construction specifically?" is not fully gated. Please have Rick sanity-check before it moves.
4. The two internal citations `[proofT1]`, `[proofconv]` are my own research notes, not yet external.
   When the paper moves to `publishable-result`, these become companion notes or appendices.

## Next step
Rick review (§4.2). Then, if clean, it moves to `scotmacbeth/publishable-result` (`.tex` **and**
`.pdf`) with a notification email carrying repo+commit, PDF link, title, one paragraph on readiness,
and the "least sure" list above — **you** send it out (§5), not me. I have NOT pushed anywhere this
session (write session; email/browse off).
