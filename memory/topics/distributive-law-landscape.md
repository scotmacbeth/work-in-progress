# Topic: the distributive-law / Zappa–Szép landscape (two levels, one structure)

The grant's technical heart (SEED Q2/Q3) is: *when do two compositional systems
compose, and what obstructs it?* The answer is a **distributive law / Zappa–Szép
product**, and as of 06-11 browse the landscape has resolved into **two levels of one
abstract structure**, with named owners and clear collaboration/competition targets.

## The two levels
| Level | Object | Criterion / structure | Owner |
|---|---|---|---|
| **Small categories** | K = C ⋈ D | **(L) free hom-presheaf ∧ (G) global closure**; DL of categories λ: DC⇒CD; ZS1–ZS4 ⟺ assoc | **MINE** (pairwise ZS, PR #9; Lean PR #8) |
| **Monadic containers** | DL between (S◁P) monads | **twelve dependent equations** (u₁,u₂,v₁,v₂) | **Purdy–Damato** (CALCO 2025) |

These are not rivals — they are **two altitudes of the same ZS/DL structure**. The
natural joint paper: *"The Zappa–Szép Distributive Law: from Monadic Containers to
Small Categories."* See [[two-atoms-zappa-szep-decomposition]].

## The distributive-law zoo (4 cases)
monad/monad · comonad/comonad · monad-over-comonad · comonad-over-monad.
- **Purdy–Damato (arXiv:2503.17191)** cover all four at the *monadic-container* level,
  Cubical Agda. Their **Example 4.9 explicitly cites ZS matched pairs of monoid actions
  (Brin 2004)** — the bridge to my categorical level.
- **comonad/comonad** is the one case still thin in the literature — and DCont ≅ Cof
  means *my* ZS-for-categories IS the comonad–comonad story. Under DCont ≅ Cof, their
  **mixed §6 laws (directed-over-monadic) become cofunctor–monad distributive laws** —
  apparently unexplored. A clean novel target.

## No-go boundary (when NO law exists)
- **Zwart–Marsden** no-go: some composable monads admit no distributive law (Purdy–Damato §7).
- **Karamlou–Shah "No-Go Theorems"** (LICS 2024): most directed containers cannot
  distribute over the **probability monad** — a hard boundary on ZS existence. Relevant
  to q-calibration (SEED Q3) and to any "agents composing under uncertainty" application.
- My (L∧G) is the *finite/decidable* boundary inside the cases where a law can exist;
  Zwart–Marsden/Karamlou–Shah are the *categorical* boundary of where to even look.

## ★ The converging no-go / obstruction cluster (2026-08-13, spotted by TWO agents)
My ZS-product + `[ω]∈H²(B;A)` result (composing update monads, stabilizer extension —
[[holonomy-composition-zs-bridge-proved]], [[emergent-holonomy-meeting-points-proved]]) sits **inside
one actively-converging research cluster**, all versions of the same question — *when does composing
two (co)monadic container/polynomial structures stay well-behaved, and what classifies the failure?*:
- **Zwart–Marsden** "No-Go Theorems for Distributive Laws" (2019, LICS/LMCS) — general monad⊗monad.
- **Karamlou–Shah** LICS 2024 — specialises to directed containers ⊗ distribution monads.
- **Purdy–Damato** CALCO 2025 (arXiv:2503.17191) — extends AU16 to monadic containers + mixed cases,
  Cubical-Agda. **Closest technical neighbour** (Agda-formalised like my Lean, direct AU16 extension).
- **Spivak** "Categories by Kan extension" (2025) — builds categories via DLs of monads over comonads.
- **Spivak** arXiv:2602.17917 (2026, = SEED's "Coinductive Polynomial Trees") — **cites Zwart–Marsden
  directly**, places the interfaces-reshape line in the same obstruction cluster; built on the cofree-
  comonad adjunction (my Ch7 territory). → [[orgtr-dcont-constant-trees]].
**Group-level folklore anchor:** the n-Café 2017 "Distributive Laws" thread + nLab `bicrossed+product`
state "distributive law ⟺ ZS/bicrossed product of monads `H×−`,`K×−`" as standard citable material
(Kassel; Brin math/0406044) — a textbook base case for the ZS weld, independent of the container-level
generalisation. **Grant framing:** my result is a *specific named instance* inside a live, converging
cluster — not an isolated trick.
- **Open (both threads, 2026-08-13):** does Purdy–Damato §6's "functional monoid action" (mixed
  monadic/directed DL) specialise to or generalise my pure-directed ZS product for update-monad
  composition? And does De Pascalis–Uustalu–Veltrì's indexed-container monoid classification
  (arXiv:2509.25879) specialise to my `T^Σ_M=M◁−` one level up? **Revive the Purdy–Damato collaboration
  idea** (joint paper on the comonad–comonad case, my freeness criterion as necessary condition).

## The generating machine
**Spivak "Categories by Kan Extension" (arXiv:2503.21974)**: density comonad =
polynomial comonad when the carrier is polynomial (resolves SEED-Q5). Builds Δ^op,
Lawvere theories, "selection categories" from **distributive laws of monads over
comonads** — an abstract machine for *generating* ZS-type constructions. Open question:
does my freeness criterion (L) characterise *which* categories Spivak's machine produces?

## Cohomological classification (the obstruction, classified)
(G) existence = Rosebrugh–Wood (DL ⟺ SFS). (G) *classification* = **H²** — proved
06-11 as [ω] ∈ H²(Sk_C;𝒟), conjecturally **Baues–Wirsching cohomology**. See
[[g-obstruction-is-baues-wirsching]]. Nonabelian boundary = Kac/Masuoka matched-pair H².

## Graded-monad / Freyd-category neighbourhood (2026 browse)
The effect–coeffect arrow work ([[effect-coeffect-arrows-first-strength]],
[[branching-obstruction-is-atkeys-index]]) sits beside a fast-moving graded-monad
literature — all organizing along axes **other than** arity/branching, which corroborates
that MacBeth's arity dimension is uncrowded:
- **Atkey ENTCS 229 (2011)**, *What is a Categorical Model of Arrows?* — Arrows ≅ *closed
  indexed* Freyd categories (folklore "Arrows = Freyd" is FALSE). His BiKleisli Arrow
  `Ar(x,y)=[Wx→Ty]` from `λ:WT→TW` = MacBeth's `Arr_M`. Branching obstruction = his
  index-collapse. Already cited by name in the arrow proofs. **Object-level shadow =
  the profunctor reframing** [[arr-profunctor-free-category-costs-branching]].
- **★ Power–Thielecke, "Closed Freyd- and κ-Categories" (ICALP 1999)** — deep-read 08-04
  (CiteSeerX; `sources.json`). **PRIMARY citable source** for "closed indexed Freyd category":
  closed Freyd `J:C→K` (`J(A⊗−)` has a right adjoint) + closed κ-category `H:C^op→Cat`
  (generic maps, indexed right adjoint). **⚠️ κ FALSE-FRIEND** — their κ is Hasegawa's
  stack-passing κ-calculus, unrelated to my compositor `κ:GT⇒TG`; same symbol also used by
  the Plumbing/Baez–Waites orchestration post. Book must disambiguate all three κ's.
- **Earnshaw–Nester–Román, arXiv:2603.16375** — PCM-graded monoidal cats; **cartesian
  PCM-graded ≅ Freyd (Thm 4.23)**. Effects-only, no coeffects/containers. Orthogonal cite.
- **Breuvart–Long–Zamdzhiev, arXiv:2602.09780** — centre of a strong graded monad =
  maximal *commutative* sub-effect. Commutativity axis, not arity. Workers-neighbour.
- **★ Vollmer–Paviotti–Orchard, "On the Category of Graded Monads" (CT2026, not yet
  arXiv)** — general 2-cat machine `Gmd(I,κ)=[BI^op,κ]_lax`; graded-monad/comonad DLs as
  instances. **May subsume the hand-computed `κ:GT⇒TG` per-instance.** WATCH arXiv;
  full-text pass owed vs `workers-type-hierarchy` + `effect-coeffect-arrows`.

## Collaboration / competition map (ACT 2026, Tallinn, July 6–10)
- **Purdy–Damato** — monad-level mirror. Joint paper target; also potential competition
  (they could extend to categories). Cubical Agda vs my Lean = complementary formalisation.
- **Bumpus, Capucci et al.** — presheaf-cohomology obstructions; engage on (G) = H².
- **Bryce Clarke** (now at **Strathclyde**, Ghani's group) — delta-lens/cofunctor; in-house.
- **Aberlé** — compositional program verification (Agda); dependent-polynomial specs.
- **Spivak / Topos** — OrgTr, Cat#, the generating machine.
- C*-algebra ZS community (**Abell–Ball k-graphs 2503.08630; Bedős et al. 1712.09432**) —
  have ZS-for-small-categories examples but apparently NOT the (L∧G) criterion. Check
  whether they already knew freeness/closure; mine their k-graph examples as a test bed.

## Neighbour — "categorified semidirect product" (08-05 browse)
- **Ahman, Reimaa, Coraglia, Castelnovo, Loregian, Martins-Ferreira, "Fibrations of
  algebras" (arXiv:2408.16581, 2024).** Bundles F-algebra categories over a parameter
  category 𝒜 into ONE fibration the authors themselves call a **"categorified semidirect
  product" `𝒜⋉^F𝒳`** (monadic case `𝒜⋉^T𝒳` via a parametrized monad `T:𝒜→Mnd(𝒳)` and
  EM-algebras). Results: monadic over 𝒜×𝒳 (Prop 4.1); bifibration criterion (Thm 4.4);
  converse Thm 5.13 (every "pruned" fibration arises so). **A ONE-SIDED cousin of the
  ZS/orchestration weld — NO two-sided matched pair, NO H² content ⟹ cite as neighbour, not
  scoop** ([[orchestration-is-zappa-szep-weld]]). Also in the fibrational-framing vocabulary
  of the 08-05 crown (`T_M` as monad opfunctor lying over base monad `M`; general Σ/Π-reindexing
  toolkit alongside Jacobs/Hermida/Katsumata). **Author overlap:** Danel Ahman (directed
  containers) + Fosco Loregian (profunctor CT).
- **✅ CLEARED 08-06** (deep-read, `reading/2026-08-06.md`): the semidirect product is **one-sided**
  by the authors' own gloss ("acting on another via a **representation**"); `𝒳` does not act back ⟹
  degenerate case my two-sided ZS generalises, **no H²**. **Thm ~4.4 does NOT sharpen a rung** — it's
  a bifibration criterion (adjoints-to-reindexing via AFT under terminal-`𝒳`/identity-monad-at-initial),
  about (co)completeness, silent on branching or cartesian-preservation. Also the "lying over" is the
  WRONG shape: their `T` is a parametrized FAMILY on a fixed carrier `𝒳` (monadic over `𝒜×𝒳`), NOT a
  monad on the total category lying over a base monad (my `T_M`/Street lifting). Net: **cite as neighbour
  for vocabulary only; zero proof leverage, zero scoop.** [[fibrations-of-algebras-2408-cleared-neighbour]].

## The effect–coeffect ladder is a stratification, not a DL collapse (08-05)
- The fibrational crown TFAE is **FALSE**; the effect–coeffect zoo resolves into a strict
  4-rung ladder (pure-writer ⊊ non-branching ⊊ cartesian ⊊ ∏-Mendler). The arrow/κ mixed-DL
  ([[effect-coeffect-arrows-first-strength]]) is only the *second* rung, distinct from
  λ-invertibility (bottom) and cartesian-`M` (third). → [[fibration-stratifies-monad-zoo]],
  [[crown-tfae-strict-chain]]. Reinforces the standing rule: hoped equivalences over containers
  keep resolving into ladders (cf. [[atkey-index-degree-negative]] Boolean dichotomy).

## Watch / bibliography (08-04 browse)
- **"Comonads on Set" (Carlson–Fairbanks–Spivak, forthcoming)** — Topos blog "Set-sets"
  (2025-11-21) previews it: general (non-polynomial) comonads on Set relate to **topological
  spaces** as categories relate to preorders; extends DCont≅Cat *one level up*, cites AU16.
  Sits exactly in the book Ch6/Ch7 DCont≅Cat territory. WATCH for the drop; read in full then.
- **Book Ch4 entwining bibliography** (nLab-sourced): entwining structures = the mixed
  monad-comonad DL variant; standard refs **Brzeziński–Majid 1998**, **Van Osdol 1973**,
  **Power–Watanabe 2002**. Add alongside the existing Ch4 citations.

## Open / next
- **OFS-on-Cof ↔ SFS-witnessing-C⋈D** (community observation): does the orthogonal
  factorization system (bij-on-objects, discrete-opfibration) on Cof *equal* the strict
  factorization system that witnesses K=C⋈D? Bij-on-obj ↔ (L), DOpf ↔ (G). If yes, the
  whole (L∧G) criterion is a corollary of OFS structure on Cof. **Verify in a wake
  session — may reduce to definitions.** Not on nLab.
- Nonabelian (G): Kac/matched-pair H² of the RW law λ (next prove target).

Links: [[two-atoms-zappa-szep-decomposition]] · [[g-obstruction-is-baues-wirsching]] ·
[[equivalence-chain]] · [[cofunctors-are-update-lenses]]
