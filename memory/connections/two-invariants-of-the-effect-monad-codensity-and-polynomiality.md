# Two independent invariants of the response monad: codensity governs fullness, polynomiality governs composition

**Status:** consolidated 2026-09-19 (dream); necessity ESSENTIALLY CLOSED 2026-09-06 (PROVE). Grade of
the underlying math: THM 1/2 `proved`, THM 3 **sufficiency `proved`** (2026-09-05 PROVE), necessity
(Lemma N) now **closed for every analytic monad except one conjecturally-vacuous corner**:
- 2026-09-05 PROVE (`proofs/2026-09-05-lemmaN-retract-and-beta.md`): Lemma R0 proved (M monad ⟹ split
  retract of M∘M ⟹ M poly ⟺ M∘M preserves connected limits); β and 𝕄 both ELIMINATED (cardinality /
  Aut(X)-stabilizer-wreath dichotomy).
- **2026-09-06 PROVE (`proofs/2026-09-06-lemmaN-plethysm-cancellation.md`) — the residual is DISSOLVED,
  not narrowed.** Theorem P0 (plethysm right-cancellation in `ℚ[[p_1,p_2,…]]`) proves the converse for
  **all analytic monads with `M∅=∅`, any degree / any wreath depth** (incl. free magmas/operads no
  stabilizer method could reach); Theorem S closes all bounded-degree analytic monads. Only open corner:
  analytic, `M∅≠∅` finite, unbounded degree AND unbounded wreath depth.
  The old "Plethysm Lemma" (decomposition-shaped) was never needed — see
  [[decomposition-from-composition-is-the-wrong-shape]].
- **2026-09-06 PROVE-2 (`proofs/2026-09-06-conjecture-V-refuted.md`) — that corner is NOT vacuous.**
  Conjecture V (corner vacuity) is FALSE: the free commutative **unital** magma `U` inhabits it
  (`a_0=1`, `U[n]=(2n−3)!!`, `S_2≀⋯≀S_2` depth). Necessity is closed for every analytic monad EXCEPT
  the sharp `a_0>0 ∧ unbounded-wreath-depth` corner, canonical member `U`, converse genuinely **OPEN**
  (not conjecturally-vacuous). "Essentially closed" now honestly means "closed bar one inhabited corner."
  See [[conjecture-V-refuted-unital-magma]], [[lemmaN-beta-two-outcome]].
Registry `m-containers.json` root `proved`; nodes `theorem-P-plethysm-cancellation`/`theorem-S-bounded-
degree` at `computed` (provenance cap: Joyal ff + plethysm-substitution identity cited from memory,
`agent-summary`). Written up in `papers/mcontainers-codensity-polynomiality.tex` (18 pp now, §5.7
cancellation trichotomy + vacuity conjecture; local, routes through Rick before `publishable-result`).
See [[lemmaN-beta-two-outcome]], [[plethysm-cancellation-closes-lemmaN]].

## The pairing (the crown of the 2026-09-05 cycle)
For an M-container (M a monad on Set), extension `⟦S,P⟧_M = ⟦S,P⟧∘M`:
- **Full-faithfulness of `⟦−⟧_M` ⟺ M is CODENSE** (invariant = codensity monad `Ran_M M`). THM 2, proved.
- **`M-Cont` composes (`⟦p◁_M q⟧_M ≅ ⟦p⟧_M∘⟦q⟧_M`) ⟺ M is POLYNOMIAL** (familially representable /
  preserves connected limits). THM 3, computed 2026-09-05.

These are **genuinely independent** — the four-cell table (each invariant fires or not, orthogonally):
- **D (distributions):** codense (FULL) but not polynomial (does NOT compose).
- **Maybe / error / writer:** polynomial (COMPOSES) but not codense (NOT full).
- **Id:** both (full and composes — trivially).
- **Reader `X^R` (|R|≥2):** REVISED 2026-09-19 — reader **is polynomial** (`= y^R`, one shape / R
  positions) ⟹ **COMPOSES**; affine (`M1=1`) so connected. So reader sits in the **polynomial-not-codense
  cell WITH Maybe/error**, NOT in a "neither" cell. (Corrects the 09-05 WAKE stub, which wrongly filed
  reader as "neither" by asserting it non-polynomial.) *Open sub-point, not re-derived this cycle:* that
  reader is genuinely NOT codense (⟹ not full) — plausible as the dual of the writer failure (writer
  refuted "preserves coproducts" for `|E|≥2`), but its codensity monad was not computed here; treat the
  "not full" claim for reader as inherited from the writer analogy, not independently checked.

So the honestly-verified table has THREE occupied cells: **both** (Id), **codense-not-polynomial** (D),
**polynomial-not-codense** (Maybe/error/writer/reader). A confirmed "neither" witness is now OPEN — the
old reader entry was the presumed neither, and it moved. Finding a genuine neither (not full AND doesn't
compose) is a clean small dream-surfaced question.

Trade-off slogan: **probability keeps faithfulness but loses composability; error keeps composability but
loses faithfulness.** For orchestration/Impact: an agent that "may decline" (Maybe lift) still composes;
the price of declining is paid in fullness (on-the-nose representability), not composability.

## Why this is a real ASSOCIATE target
Both invariants are Kan-extension / representability conditions on the SAME object M, pulling in opposite
directions. Is there a single higher statement subsuming both? Candidate framing: `⟦−⟧_M = ⟦−⟧∘M`
factors the M-container functor as (polynomial part) ∘ (effect part); fullness tests the effect part's
codensity (how M sees Set), composition tests whether the effect part is itself in the polynomial image
(whether M sees Set the way a container does). Codensity = "M's natural operations are no bigger than M";
polynomiality = "M is built from Set-homs". Worth relating to Leinster codensity + Garner/Weber familial
representability in one diagram. Possible COLLISION check (cf. [[fusion-versus-identification]]): are
"codense" and "polynomial" ever conflated in the literature for the same monad? They are distinct here —
good, no collision — but confirm.

## New ASSOCIATE target (2026-09-20 browse): recast THM 2 as completeness in Kura's λeff framework
"Codensity" has **zero prior footprint** in this program before 2026-09-20, and the browse found it is
suddenly active in PL/semantics — but **none of the three touch effect-handler *composability*** (the
exact angle THM 3 owns):
- **Kura, "Complete Categorical Semantics for Effect Handlers", arXiv:2602.03275** (Feb 2026, deep-read).
  Sound-and-complete semantics for a deep-handler calculus λeff (models = cartesian cat + indexed family
  of strong monads + operation/handle interpretations; Thm 4.4/4.9). **Prop 5.3: free monads on
  polynomial endofunctors on Set are λeff-models** — puts my container-style free-monad construction
  ([[oneill-free-monad-tensor-algebra-linear-container]], [[free-monad-grafting-laws-done]]) inside a
  general handler-completeness theorem. Codensity absent; handler *composition* left OPEN.
- **STACS 2026, Lenke–Wittrock–Milius–Urbat, "Demystifying Codensity Monads via Duality"**
  (LIPICS vol. 364, abstract-level). Codensity of F ≅ monad of an adjunction whenever F≅R∘G^op∘E with G
  dense ("codensity = density + duality"); recovers ultrafilter, Giry, Radon, Kantorovich uniformly. The
  clean citable modern statement of codensity machinery **if THM 2 is ever written up standalone.**
- **"Strong Dinatural Transformations and Generalised Codensity Monads", arXiv:2510.06777** (abstract).
  Dicodensity monads (codensity for mixed-variant bifunctors), CPS/System-F motivated. Adjacent, not
  handler-composability.

**The question to carry:** could THM 2's "M codense ⟺ ⟦−⟧_M full" be recast as a
completeness/composability statement inside Kura's λeff-model class? Prop 5.3 already links the
*polynomial* side (composition, THM 3) to λeff-models; the codensity side (fullness, THM 2) is the piece
λeff-semantics has NOT connected. This is genuinely unclaimed territory adjacent to my own two invariants.
→ [[codensity-effect-handler-composability]].

## Hygiene flag for the dream (unrelated, but log it)
`/home/agent/projects/PROGRESSIVE_DISCLOSURE.md` has grown to **~262 KB** — far past a "Level 0 map".
It errors on a plain Read (exceeds 256KB). It needs the same chronology→journal compression the SUMMARY
got on 2026-08-30 (keep the Level-0 pointers, move dated bullets to the dream journal). Dream-cycle task.

Related: [[neil-k-container-monad-lift-is-fam-kleisli]], [[fusion-versus-identification]],
[[fullness-unit-connectedness]].
