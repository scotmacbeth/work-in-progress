# ⋉/⋊ are the Dialectica tensors — Poly ↔ linear logic

**Crown-jewel cross-domain bridge (Path 3 ↔ linear logic / Dialectica).
✅ NOVELTY CLEARED — sweep run 2026-07-17, verdict (C) CLEAR (see flag at bottom).**
Established 2026-07-17 (prove).
Proof: `proofs/2026-07-17-ltimes-rtimes-dialectica.md`. Registry `other-cont-monoidal-tensors`
(**computed**, trustcheck green). Collaborator note `for-collaborator/2026-07-17-ltimes-rtimes-dialectica.md`.

## The claim
Dorta–Jarvis–Niu (**arXiv:2305.05655 §6**) exhibit two extra monoidal structures **⋉/⋊** on `ΣΠC`
and **explicitly leave open** what they mean. At `C=1` (= Poly = Cont), in container coordinates
(shapes `S_p×S_q`):

```
  (p ⋉ q)[(s,t)] = p[s]^{S_q} × q[t]^{S_p}      (p ⋊ q)[(s,t)] = p[s]^{S_q} × q[t]
```

An exponential indexed by the **opposite** shape set. That is the Dialectica hallmark, and it lands:

- **⋉ = de Paiva's Dialectica tensor**, extended off the homogeneous slice `Hmg(2) ≃ Dial(Set)`
  (DJN Prop 2.13) to all of Poly. On homogeneous inputs the direction `A^J × B^I = X^V × Y^U` is
  *exactly* de Paiva `(U,X,α)⊗(V,Y,β) = (U×V, X^V×Y^U, …)`. The linear-logic (multiplicative
  conjunction ⊗) content of `Dial(Set)` lives in **⋉**, NOT in DJN's Day `⊗` (which restricts to
  Gödel conjunction, challenge `X×Y`).
- **⋊ = the directed variant.** `n`-fold closed forms: ⋉ exponentiates each factor by the product of
  *all other* shape sets (symmetric); ⋊ only by the shape sets **to the right** (triangular ⇒
  associative, NOT symmetric). Game reading: ⋉ = both players respond adaptively; ⋊ = one-way
  dependency (one problem answered in response to the other, played blind).

## Why it matters (the associations)
1. **Answers DJN's stated open question** (§6, "we would like to know if there are interpretations").
   DJN is [[dorta-jarvis-niu-neighbour]] — the closest published neighbour to my Day-family
   classification; this closes a gap *they* flagged.
2. **The four canonical + Day family do NOT exhaust Cont's monoidal structures.** ⋉/⋊ are
   **non-convolutional** (direction depends on the *global opposite* shape set, not on the fibres),
   so **Theorem A cannot reach them** ([[monoidal-structures-on-cont]], [[day-family-classified]]).
   They are also **non-cocontinuous** (no distribution over `+`) and **non-closed** — the *first*
   non-closed monoidal structures on Cont, complementing the closed ⊗ / cartesian family in
   [[closed-structures-are-spivaks]]. This is a genuine boundary on the Day story, not a footnote.
   **★ NON-CLOSURE now PROVED (2026-07-18, `proofs/2026-07-18-dialectica-tensors-non-closed.md`,
   registry child `ltimes-rtimes-non-closed` = proved).** Thm 1: `(Cont,⋉,y)` is neither left- nor
   right-closed (witness `p=q=y²`; `p⋉(−)`, `(−)⋉q` fail to preserve `y+y`, profile ⟨4,4⟩≠⟨2,2⟩ ⇒ no
   right adjoint, Mac Lane V.5). Thm 2: `(Cont,⋊,y)` is **not right-closed** — **BUT `(−)⋊q` DOES
   preserve binary coproducts** (exponent `S_q` fixed): the closure obstruction is **one-sided /
   directed**, mirroring ⋊'s asymmetry, and this CORRECTS the companion note's blanket "same
   computation kills ⋊". Method: contrapositive of "left adjoint preserves colimits" via
   non-ISO-of-objects + AAG container-iso profile invariant. **New Open Q (registry-tracked): is ⋊
   *left*-closed?** Coproduct obstruction vanishes; needs all-colimit preservation or explicit
   `[p,−]_⋊`. Conjecture YES ⇒ ⋊ a genuinely *directed-closed* monoidal category.
3. **Bridges Path 3 to linear logic.** Poly's monoidal zoo now touches de Paiva's Dialectica
   categories directly — the same category theorists (Trotta, Spivak, Hedges, Capucci) circle both.
   A Poly↔Dialectica dictionary would feed the grant's "one framework, many dialects" spine and
   Neil's four-monoidal programme (⋉/⋊ = two *more* structures on Set beyond the four canonical).
4. **Feeds Neil's interaction chapter** as the honest answer to "are there other monoidal structures
   on Set?" — yes, and the extra ones are the linear-logic tensors, sitting outside the convolutional
   world Thm A classifies.

## ✅ Novelty cleared + one standing honesty flag
- **Novelty CLEARED — sweep 2026-07-17, verdict (C) CLEAR.** The identification appears genuinely
  novel and answers DJN's own stated open question, **provided** it is framed as identifying a KNOWN
  tensor (de Paiva's) with DJN's uninterpreted ⋉ — **NOT** "first Dialectica-on-Poly" (false). Two
  neighbours to cite and distinguish:
  - **Lucatelli Nunes–Vákár, arXiv:2405.07724** — Dialectica-*formula* monoidal-*closed* structure on
    Grothendieck constructions, instantiated to containers (Ex. 9.16); their tensor is the fibred
    product and the Dialectica twist lives in the internal hom **⊸** (Thm 9.19), not in a tensor like
    ⋉; does not produce ⋉, does not cite DJN, does not address DJN's open question. **Neighbour, not
    scoop.** (Also a new neighbour for the closed-structures + fibrational / von Glehn programme — its
    ⊸ may bear on whether ⋉ is closed.)
  - **Capucci–Gavranović–Malik–Rios–Weinberger, MFPS 2024** — unifies lenses/optics/Dialectica as one
    fibrational construction `Dial(P)=Sum(Prod(P))` at the *category* level, not a monoidal tensor;
    thanks DJN in acknowledgements but never interprets ⋉/⋊. **Neighbour, not scoop.**
  - **Reviewer pre-empt:** DJN's abstract says they "extend ... dialectica categories", but their §3
    tensor is the non-twisting parallel product (directions `A×B`); the twisting multiplicative tensor
    `(U×V, X^V×Y^U)` is ⋉, which they left uninterpreted.
- **Registry graded `computed`, not `proved`**, on purpose — the identification rests on matching to
  de Paiva's published tensor formula, which is itself still `unclassified` in sources.json.

→ [[dorta-jarvis-niu-neighbour]], [[monoidal-structures-on-cont]], [[closed-structures-are-spivaks]],
[[read-poly-before-claiming]]

## Independent reinforcement — browse sweep 2026-07-17 (afternoon)
Four parallel browse agents (arXiv, community forums, web, citation trails) ran a second, independent
novelty sweep, dispatched *before* reading the above PROVE-session verdict. All four converged clean,
adding evidence the PROVE sweep didn't have:
- **DJN 2305.05655 has 0 reverse citations** on Semantic Scholar — nobody has touched the §6 open
  problem in two years.
- **The one team best-positioned to find this got there first and stopped short.** Nelson Niu's Topos
  Institute blog post "Dialectica categories and polynomial functors (Part 1)" (2022-07-12) builds the
  ΣΠ𝐂 unification (Poly = ΣΠ𝟙, Dialectica = ΣΠ(walking-arrow)) and explicitly promises a "Part 2" on
  monoidal structures induced by a monoidal structure on `C` — exactly this question. **That Part 2
  was never published**; the material instead matured into DJN 2305.05655, whose §6 leaves ⋉/⋊
  uninterpreted. Confirmed independently by two agents (direct 404 + blog-listing check).
- nLab's "Dialectica category" and "Chu construction" pages have zero mentions of polynomial functors,
  containers, Poly, or Spivak.
- arXiv:2407.01849 (Spivak-Srinivasan, the closest live LDC-territory paper) re-read pp.1-5: no
  mention of Dialectica/Chu/de Paiva anywhere.
- de Paiva's own recent output shows no connection to Poly beyond what DJN already synthesizes (one
  unread 35pp talk PDF saved locally as a residual check, low risk — talks without papers are a known
  weak signal per BROWSE.md filters).

**Net effect: verdict (C) CLEAR is now corroborated by a second, independently-dispatched sweep.**
No change to the registry grade (`computed`, pending de Paiva's tensor classification) or the framing
rule (identify a KNOWN tensor, never claim "first Dialectica-on-Poly").

**Watch-item RESOLVED (2026-07-18 browse):** Spivak's density-comonad programme (arXiv:2503.21974 →
**arXiv:2607.15091 "Comonads as Spaces"**, Fairbanks–Carlson–Spivak, 152pp) was **full-read by two
agents → NOT a scoop** of DCont≅Cof or the density-comonad SEED Q5. It works one level up (comonads on
Set / ionads / topology), cites AU16 as a settled black box (quoted verbatim), never touches D1–D5,
Zappa–Szép, or comonoids-in-Poly. Its **retrofunctor double category recovers Clarke–Di Meglio** as a
special case (Thm 3.2.7) ⇒ **cite 2607.15091 + the Topos "Set-sets" primer (2025-11-21) as RELATED
WORK in the DCont≅Cof paper/chapter** — the closest possible neighbour, context not competition.
→ `reading/2026-07-18.md`, [[density-comonads-orthogonal-seed-q5]].
