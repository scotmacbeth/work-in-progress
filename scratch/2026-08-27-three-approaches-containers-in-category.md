# Three approaches to "a container in a category" — orientation note

**Started 2026-08-27 (WAKE), on Neil's UID 125 steer ("a few days contemplating all approaches would be
valuable"). This is the contemplation artifact — a survey SKELETON + the discriminator thesis, gaps flagged.
Not a finished paper. Becomes the backbone of a `/expository` survey once the gaps close.**

Neil's framing (UID 125), reframed away from grants toward *understanding*: he wants the definitive map of
what "containers over a base other than Set" can mean, with **Fam(Vec^op) as the running core example** (the
one that "needs the first approach"). He names three routes and flags the enriched-Yoneda dependency.

---

## The three approaches

### (1) External families: `Fam(C^op)` — my current front
- **Object:** `(S, (P_s)_{s∈S})`, `S` a **SET** (external index), each `P_s ∈ C`.
- **Extension:** `⟦S,P⟧ = ∐^{Set}_s C(P_s, −) : C → Set` (or landing in `C` via copowers `∐_s P_s ·(−)` when `C`
  is copowered). The `∐` is an **external Set-coproduct**.
- **What's proved (mine):** T1 — `⟦−⟧` full-faithful ⟺ monoidal **unit connected** (`C(I,−)` preserves ∐), NOT
  extensivity; the copower test decides it over extensive bases [[fullness-unit-connectedness]],
  [[copowers-gap-writer-monad-extensive]]. T2 — Dirichlet `⊗` closed ⟺ `Φ` familially representable; closed on
  cartesian bases + `Fam_fin(Vec_fd^op)` only [[t2-day-closedness-famcop]]. `◁_DJN`-comonoids = enriched categories
  (DJN `2305.05655` Thm 4.3). ⚠ **2026-08-31:** `◁_DJN` is *weighted* (outer `u` multiplied in, Def 3.5/Lemma 3.6
  p. 89) and equals my `◁` **only at `C=1`**; whether my Vec instance is a case of their theorem is therefore an
  **OPEN question at `speculative`**, not a settled subsumption. Their `⊗` does agree with mine exactly.
- **Reaches Fam(Vec^op) DIRECTLY** — the external `∐` doesn't need `C` to have internal coproducts matching, and
  the non-extensive collapse `∐⊊⊕` becomes a *feature* (biproduct = "either prompt = both")
  [[extensivity-is-container-boundary]], [[vec-biproduct-collapse-proved]].

### (2) Indexed / dependent-polynomial over an LCCC: `I ← P → S → O`, Σ-Π-Δ — Neil's UID 125 "other canonical approach"
- **Object:** a diagram `I ←^s P →^f S →^t O` in a base `𝒞`; **semantics** = the composite slice functor
  `𝒞/I →^{Δ_s} 𝒞/P →^{Π_f} 𝒞/S →^{Σ_t} 𝒞/O` (reindex, dependent product, dependent sum). This is the
  **Gambino–Hyland / Gambino–Kock dependent polynomial functor** (arXiv `0906.4931`; Gambino–Hyland 2004).
- **Requires `𝒞` LCCC** — the `Π_f` (dependent product / right adjoint to pullback) needs local cartesian
  closure. Setting `I = O = 1` gives ordinary endofunctors `𝒞 → 𝒞`; then a "container in 𝒞" = `S ← P` internal.
- **Neil's expectation:** replacing Set by an LCCC keeps everything working and the container category is
  **extensive**. Plausible for LCCC-and-extensive bases (Set, any topos, any LCC pretopos).
- **THE TENSION (the survey's crux):** **Vec is NOT locally cartesian closed** — no dependent products `Π`, so
  approach (2) *cannot form the semantics at all* over Vec. Gambino–Kock explicitly place `Fam(Vec^op)` outside
  the classical machinery [[reference_dorta_jarvis_niu_generalized_poly]]. So (2) **cannot see Fam(Vec^op)** — which
  is exactly why Neil says returning to Fam(Vec^op) "needs the first approach." **This is the discriminator.**
- De Pascalis–Uustalu–Veltrì `2509.25879` is the *composition-monoid* refinement of the I-indexed corner of this
  (single common index, Set base, dropping GK's cartesianness); my `M◁−` = its I=1 fibre
  [[my-Mtriangle-is-I1-fibre-of-indexed-icms]]. Same lineage as (2), Set base.

### (3) Fibrational: positions as a fibration over shapes — Neil's UID 125 "feels more fibred"
- **Object:** replace `P → S` by a **fibration** `p : ℰ → 𝔹` with `S ∈ 𝔹` and the position data living in the fibre
  `ℰ_S`; use **comprehension** `{−}` to pull the total-category data down over the base, OR give semantics
  directly in the total category `ℰ`.
- **Most general; the "logic over containers" angle.** Contravariance IS the fibrewise op already
  [[contravariance-is-fibrewise-op]] (`Cont = ∫_Set (cod)^op`, von Glehn TAC 33); the Dialectica tensors `⋉/⋊`
  live here [[ltimes-rtimes-are-dialectica]]. A comprehension category / fibration with (co)products is the natural
  home. This subsumes (1) and (2): (1) = the family fibration `Fam(C) → Set`; (2) = the codomain fibration
  `cod : 𝒞^→ → 𝒞` of an LCCC.
- **Why it matters:** it decouples "what indexes shapes" (the base `𝔹`) from "where positions live" (the fibres),
  so it can host BOTH the external-Set-indexed (1) and internal-LCCC (2) pictures as instances of one scheme, and
  it's where predicate-logic / verification structure attaches (Dialectica, subobject vs codomain fibration
  [[neil-prefers-fibration-language-not-proof-relevance]]).

---

## The discriminator thesis (the spine of the survey)

**Extensivity + local-cartesian-closure of the base is the axis that separates the three approaches; a base can
have one without the other, and Fam(Vec^op)'s base Vec is the case that has NEITHER internal Π nor extensivity.**

| Base `C` | extensive? | LCCC? | (1) Fam(C^op) reaches it | (2) Σ-Π-Δ semantics exists | (3) fibrational |
|---|---|---|---|---|---|
| Set, any topos | ✓ | ✓ | ✓ (full-faithful, closed) | ✓ (and extensive, per Neil) | ✓ (both fibrations) |
| Vec (fin/gen) | ✗ (`∐⊊⊕`) | ✗ (no Π) | ✓ (external `∐`; collapse=feature) | ✗ **cannot form Π** | ? (family fibration `Fam(Vec)→Set` exists, but no cod-fibration Π) |

- **When the base is extensive-and-LCCC, all three agree** — this is the classical convergence (containers ≃
  directed containers ≃ Poly-comonoids ≃ categories), and the choice among (1)/(2)/(3) is presentational.
- **When the base is neither (Vec), only (1) survives** — because (1) uses *external* Set-indexing and never asks
  `C` for internal `Π` or a well-behaved `∐`. This is the honest reason Neil's "return to Fam(Vec^op)" forces
  approach (1). It also re-reads my T1/T2: the fullness/closedness obstructions over Vec are exactly the *shadow*
  of Vec failing the extensive-LCCC hypotheses that (2)/(3) would need up front.
- **The fibrational view (3) is the referee:** it says (1) and (2) are two fibrations (family vs codomain), so the
  "which approach" question = "which fibration models your positions," and non-extensive/non-LCCC bases are the
  ones where the two fibrations genuinely diverge.

---

## Answer to my own question-back to Neil (do it BEFORE he replies, so I'm not idle)
Yes — Fam(Vec^op) is the sharpest discriminator, and the reason is now precise: it fails **both** hypotheses that
(2) and (3)-via-codomain-fibration need (extensivity AND local cartesian closure), so it isolates approach (1) as
the unique route. The survey should run Fam(Vec^op) as the worked example in every section.

## Gaps to close over the next few days (the "contemplation")
1. **(2) letter-perfect:** write out the `Σ_t Π_f Δ_s` composite and the `I=O=1` reduction to endofunctors
   cleanly; confirm the precise LCCC hypotheses (pullback + right adjoint `Π_f`). Pull Gambino–Hyland 2004 +
   Gambino–Kock `0906.4931` at source (research agent).
2. **(3) precise:** which comprehension-category / fibration-with-products axioms; does the family fibration
   `Fam(Vec)→Set` give a *usable* container notion that agrees with my (1) `Fam(Vec^op)` (note the op!), and where
   does the missing cod-fibration `Π` actually bite?
3. **Enriched-Yoneda dependency (Neil flagged):** the `C→Set` functor view of `Fam(C^op)` (each object as a
   presheaf) needs enriched Yoneda to state full-faithfulness intrinsically — reconcile with my set-level T1 proof
   (which avoided it). Is the enriched statement strictly stronger, or the same content repackaged?
4. **Left-closedness (Neil's explicit ask):** separate PROVE target — his hint "left Kan preserves representability
   ⟹ just coproducts." Since `⊗` is symmetric (left=right), pin down whether he means the **`◁` left internal hom**
   (Cont has `◁` right-coclosure = DCont, no `◁`-closure — so what does the left-Kan argument actually deliver?) or
   a cleaner left-Kan re-proof of the `⊗` closedness. → `state/PROVE.md`.
5. **Aberlé `2604.01303`:** park as a Path-5/6 application/formalization comparison point (verification = monoidal
   functor Spec→Int + lax-presheaf nat transf); NOT part of the foundations survey. Its `DepPoly` is a Hoare-triple
   decoration, not the GK dependent polynomial (terminology clash — note it so I don't confuse them later).
</content>
