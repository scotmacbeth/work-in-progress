# Inventory: base categories C for "containers / polynomials over a base" — Cont(C) = Fam(C^op)

**For:** Neil Ghani (change-of-base question, 2026-08-28).
**Scope:** which base categories C people have actually used for the generalized-polynomial /
`Fam(C^op)` construction, and what holds vs breaks in each.
**Provenance key:** `[LIT]` = genuinely in the literature; `[MACB]` = MacBeth's own unpublished
result; `[OPEN]` = raised but nobody has run the construction.

The construction Neil means comes in (at least) four guises that coincide over Set but diverge off it:

- **(1) External `Fam(C^op)`** — objects `(S, {Q_s ∈ C}_{s∈S})`, `S∈Set`; tensors `⊗` (Dirichlet/Day)
  and `◁` (composition). Uses **external** Set-coproducts; asks C only for a monoidal/limit structure.
  This is the guise that reaches non-extensive bases like Vec.
- **(2) Indexed dependent-polynomial** `I ← P → S → O` with Σ-Π-Δ along maps of C. Needs C
  **locally cartesian closed** (or a weakening thereof).
- **(3) Fibrational** `Cont(q) = ∫_B q^op` for a fibration `q:E→B` (positions = fibrewise opposite).
- **(4) Enriched / monoidal-base** `ΣΠV` for a monoidal V (free coproduct-completion of free
  product-completion). Day `⊗` and composition `◁` over any monoidal V.

The **discriminating axes** are (a) **extensivity** of C (coproducts disjoint — makes shapes
recoverable, `⟦−⟧` full-faithful) and (b) **local cartesian closure / exponentiable legs**
(gives internal Σ-Π-Δ, hence `◁` and closedness). Set has both; the interesting bases lose one or
both.

---

## Master table

| # | Base C | Who studied Fam(C^op)/polynomials over it | What holds / breaks | Significance for change-of-base |
|---|--------|-------------------------------------------|---------------------|-------------------------------|
| 1 | **Set** | Abbott–Altenkirch–Ghani, *Categories of Containers*, FoSSaCS 2003; Gambino–Kock `0906.4931` (`I=O=1` case); Niu–Spivak *Poly* book `2312.00990`; Ahman–Uustalu (DCont≅Cat) `[LIT]` | Everything: extensive, LCCC (a topos), all four monoidal (`+,×,⊗,◁`), `⟦−⟧` full-faithful, `DCont≅Cat`, `⊗`-comonoids = families of monoids, `◁`-comonoids = categories. | The baseline. Every "breakage" below is measured against Set. |
| 2 | **Any LCCC / elementary topos E** | Gambino–Kock `0906.4931`; von Glehn TAC 33 (2018) no.36 (`Cont(p)=Σ_p(p^op)` for the codomain fibration of an LCCC — she literally names it "category of containers", cites AAG as her special case); Hyvernat `1209.0940` `[LIT]` | Full Σ-Π-Δ semantics; `+,×` need pullbacks, `◁`/`⟦−⟧` need Π (=LCC). Extensive iff E lextensive (toposes are). Everything transfers Set-like. | The "safe" change of base: as long as C is LCCC + extensive, the whole theory ports. This is the boundary of the classical machinery. |
| 3 | **Finite-limit category E (pullbacks, not nec. LCCC)** | Shapiro–Spivak `2305.00167` (`Poly_E`; comonoids = internal categories **with exponentiable source**, Thm 5.6; morphisms = internal cofunctors, Cor 5.12); Spivak *Generalized Lens Categories* `1908.02202` (fibration → bifibration w/ pullbacks → trifibration when LCC); Ahman–Chapman–Uustalu LMCS 2014 §7 (directed polynomials in a pullback category — **definitions only, no theorem**) `[LIT]` | The equivalence `comonoids = internal categories` needs only **exponentiable source object**, not full Π; only the `◁` *monoidal structure* needs Π. `+,×` fine with pullbacks. Off-LCC, `◁` is strictly lossy (SS23 Ex 5.10, Conduché). | Sharp result: **`DCont≅Cat` is about composition (pullbacks), NOT about Π.** Tells you exactly how much base structure each piece costs. |
| 4 | **Category with pullbacks + exponentiable middle legs** | Weber `1106.1983` "Polynomials in categories with pullbacks" (TAC 30, 2015) `[LIT]`; deep-read | Runs poly-functor semantics via **distributivity pullbacks** — a canonical comparison **δ must be iso** (⟺ middle leg exponentiable). The rung *between* GK (LCCC) and Walker. "Has pullbacks" alone is NOT enough (misleading title). | The master reference for **localising** where base-change fails: it is a per-morphism δ-iso condition, not a global "no Π". `[MACB]` open conjecture δ≟Φ ties this to MacBeth's T2 closedness. |
| 5 | **Locally subcartesian closed / subpullback bases** | Walker `2607.10242` (2026; Street protocalibrations + Weber distributivity pullbacks; **zero Gambino–Kock**) `[LIT]`; deep-read | An **affine** weakening: `∇_f ⊣ ⊠_f` (dependent *subproduct*) can exist when full `Δ_f⊣Π_f` fails; pullbacks mandatory so `Σ_f⊣Δ_f` always holds. Slice tensor `g⊗_Y f ≅ Σ_f∇_f(g)`, right-closed-not-cartesian. Thm 5.2.8: bicategory of subcartesian polynomials ≃ poly functors w/ "bunched strength". **Motivating bases: the Lawvere quantale `A+B−X`, affine spaces, nominal sets** — never Vec. | The current frontier of "how weak can the base be". Community (MO 205902, 2026 answer) calls LSCC *the* monoidal analogue of LCCC. Vec falls **below** even this. |
| 6 | **General fibration q:E→B** | von Glehn TAC 33 (2018) `Cont(q)=∫_B q^op = Σ_q(q^op)`; Streicher `1801.02927` Ch.5 (the trap: naive dual `X^op→B^op` has WRONG base, not a fibration) `[LIT]` | `+,×` need pullbacks in the fibres; `◁` and `⟦−⟧` need Π (fibrewise LCC). Positions-are-contravariant = **the fibrewise opposite** is the honest home of Cont. von Glehn's interest was models of type theory; she never asks about comonoids in `(Cont(q),◁)`. | The abstract statement of change-of-base itself: `Cont(−)` is a construction **on fibrations**. Neil's `Cont(cod):Cont(Set^→)→Cont(Set)` (#9) is an instance. |
| 7 | **Any monoidal category V (enriched containers)** | **Dorta–Jarvis–Niu `2305.05655`** "Monoidal Structures on Generalized Polynomial Categories" (EPTCS 397, 2023); Daniel Lin, *Enriched Polynomial Functors* (AMSI VRS report, Macquarie, 2014 — **not on arXiv**) `[LIT]` | **The most general published answer.** `ΣΠV` = free-coproduct-of-free-product completion of V. Constructs **⊗ (iterated Day)** and **◁_DJN (their weighted composition product)** over ANY monoidal V. **Thm 4.3:** comonoids in `(ΣΠV,◁_DJN)` ≃ small categories **enriched in `(ΣV^op,⊙)`** with enriched cofunctors. ⚠ **2026-08-31:** `◁_DJN ≠` my `◁` — their direction object multiplies in the **outer** `u_{i,a}` (Def 3.5/Lemma 3.6 p. 89); they agree only at `V = 1`. The `⊗`s do agree exactly. They do **NOT** treat: closedness/internal-hom, coproduct/product-as-monoidal, or any extensivity/fullness analysis. | **This is the direct answer to "has anyone done a general base?"** — yes, DJN, for any monoidal V. ⚠ **2026-08-31, `speculative`:** whether MacBeth's Vec `◁`-comonoid = family of k-algebras is subsumed by their Thm 4.3 is **OPEN** — the two `◁`s differ off `V=1` and the two comonoid classifications visibly differ (families of k-algebras vs all enriched categories). **Not a restored novelty claim; an unresolved question.** The delta left open: closedness + the extensivity/fullness of `⟦−⟧`. |
| 8 | **Vec / Vect_k (linear base)** | **`[MACB]`** (containers-over-vec front + survey `papers/containers-over-a-base.tex`). Ingredients owned separately: strict poly functors (Friedlander–Suslin; Krause `1203.0311`); linear species/TCA (Sam–Snowden `1209.5122`); k-linear cats/algebroids (Mitchell 1972; Bénabou 1967) `[LIT]` | **Neither extensive nor LCCC.** `∐⊊⊕` (Carboni–Lack–Walters 1993: Vect not even finitely extensive), no internal Π, terminal `=0` so `F(1)=S` dies. Consequences (all `[MACB]`, proved): **T1** `⟦−⟧` faithful **but not full** (fullness ⟺ unit-connectedness); **T2** `⊗` closed **only** on `Fam_fin(Vec_fd^op)` (needs dualizable+summable positions); **T4** `◁`-left-closed only via the collapse `◁=⊗` (tiny/dualizable positions); `◁`-comonoid = **family of k-algebras**, genuine algebroid needs `Mat(Vec)` (matrix product `⊕_b P_{ab}⊗Q_{bc}`). Only the **external `Fam(C^op)`** guise (1) reaches it. | The **worked stress-test** for change-of-base: shows what a non-extensive, non-LCCC additive base costs. Genuinely open as a container framing; DJN covers the `◁`-comonoid but not the extensivity gap. |
| 9 | **Set^→ (arrow category / codomain fibration of Set)** | **`[MACB]`** (Neil's UID-132 request); `Cont(cod)=Fam(cod^op)` proved a **bifibration** | Fam preserves fibrations componentwise ⟹ `Cont(cod)=Fam(cod^op)` bifibration; fibre over `(S,{P_s})` = `∏_s (Set/P_s)^op` = proof-relevant predicates on positions. **Logic of containers:** quantifiers `A⊣Δ_c⊣E` = the A/E predicate liftings (E=Exists=cartesian reindexing=◁, A=All). **Dualisation theorem:** container hyperdoctrine = fibrewise-OP of Set's (∃↔∀, ∧↔∨, ⊤↔⊥; each fibre a co-topos). TRAP: reindexing = `(Σ_ρ)^op`, not `ρ^*`. | **This IS the change-of-base example Neil already gave.** `Cont` applied to the codomain fibration turns "predicates on positions" into a logic; the change of base Set^→→Set is the collapse `η:(S,{1})→(S,{P_s})`. |
| 10 | **Set^I / indexed base** | De Pascalis–Uustalu–Veltrì `2509.25879` "Monoid Structures on Indexed Containers" (LSFA 2025: monoids in `(I-Cont,◁,y)` ≃ monads on `Set^I`); Altenkirch–Ghani–Hancock–McBride–Morris, *Indexed Containers*, JFP 2015 (**but footnote 3 disclaims the families-fibration reading**) `[LIT]` | More general than Gambino–Kock **precisely by dropping cartesianness** of η,μ. At trivial `I=1` reduces to the non-indexed `◁`-monoid (= MacBeth's `T^Σ_M`). `[MACB]` observation: MacBeth's classification is the `I=1` fibre of their ICMS. | The "many-sorted" change of base: replace Set by its self-indexing `Set^I`. Bridges to the fibrational view (6,9). |
| 11 | **Prof / profunctor-enriched (generalised species)** | Fiore–Gambino–Hyland–Winskel, *The cartesian closed bicategory of generalised species of structures*, JLMS 77 (2008) 203–220; follow-ups Fiore–Galal–Paquet (stable species) `[LIT]` | Base = free (co)completion; substitution `◁` = **Kleisli bicategory of a pseudo-comonad on Prof**; the bicategory of generalised species is **cartesian closed**. Generalises Joyal species + analytic functors. | The "up an enrichment dimension" change of base: positions/shapes become **profunctors**, composition becomes analytic-functor substitution. The bicategorical sibling of DJN (#7). |
| 12 | **Poly itself, Cat#, and Mod (self-application)** | Niu–Spivak *Poly* book, **Ch. 9 Question 5** explicitly asks for `×`- and `⊗`-(co)monoids in **Poly, Cat#, Mod** — "find examples… create a theory of them." `[OPEN]` | Authors cite **no one** and flag the questions as "not known to us" — evidence of authors' ignorance, not literature-openness. Largely unstudied. MacBeth's ⊗-comonoid census answers a fragment (directed containers do not descend to ⊗-comonoids). | Named-but-unrun bases. `Mod` (bimodules/Poly-comodules) is Spivak's own suggested change of base and is **wide open**. |
| 13 | **Rel, R-Mod, poset/quantale (thin & additive bases)** | Walker's quantale (`A+B−X`, #5) is the only one actually *run* `[LIT]`; R-Mod/Rel: `[OPEN]` / `[MACB]` obstruction-only | **Additive/thin bases fail the copower test already** (`[MACB]`, SUMMARY): `C(I,−)` preserving copowers ⟺ writer monad `(−)×End(I)` — fails for Vec, R-Mod, Rel (no indecomposable non-initial unit in the required sense). R-Mod behaves like Vec (`∐=⊕`, non-extensive). Rel is self-dual, thin-ish — genuinely unexplored. Quantales: the LSCC affine story (Lawvere `[0,∞]`). | Maps the "beyond Vec" territory. R-Mod ≈ Vec (same obstruction, char-p subtleties). **Rel and general quantales are the clearest open change-of-base targets.** |

---

## Reading of the table (for the email)

**The single most important literature answer to "has anyone done a general base?":**
**Dorta–Jarvis–Niu `2305.05655` (#7)** build two monoidal structures — `⊗` (which coincides with
mine) and their **weighted** `◁_DJN` (which does **not**; see the ⚠ in row 7) — over an
**arbitrary monoidal category V**, and characterise `◁_DJN`-comonoids as **V-enriched categories**
(Thm 4.3). Daniel Lin's *Enriched Polynomial Functors* (unpublished AMSI report) is the other
"any monoidal V" data point. If Neil wants one citation for change-of-base to a general enriched
base, it is DJN.

**The classical safe zone** is LCCC/topos bases (#2): Gambino–Kock + von Glehn give the full
Σ-Π-Δ theory, and von Glehn already phrases it fibrationally (`Cont(q)=Σ_q(q^op)`, #6) — which is
the abstract form of change-of-base itself.

**The weakening tower** (how little base structure you can get away with) is now mapped as a
**totally ordered** family:
> LCCC (Gambino–Kock) ⊐ pullbacks+exponentiable-legs (Weber `1106.1983`) ⊐ subpullbacks/LSCC
> (Walker `2607.10242`) ⊐ spans (Street `1903.03890`).
Each weakening smooths a different seam; **nobody had assembled them into one ordered tower and
asked where a given base sits** — that assembly is `[MACB]`.

**Bases people actually treat OTHER than Set/Vec/Set^→** (the core of Neil's question):
- **any LCCC / topos** — Gambino–Kock, von Glehn `[LIT]`
- **any finite-limit category** — Shapiro–Spivak `2305.00167` `[LIT]`
- **any category w/ pullbacks + exponentiable legs** — Weber `1106.1983` `[LIT]`
- **locally subcartesian closed bases (quantales, affine spaces, nominal sets)** — Walker `2607.10242` `[LIT]`
- **any monoidal category V** — Dorta–Jarvis–Niu `2305.05655`; Daniel Lin `[LIT]`
- **any fibration q:E→B** — von Glehn TAC 33 `[LIT]`
- **Set^I (indexed)** — De Pascalis–Uustalu–Veltrì `2509.25879`; AGHMM JFP 2015 `[LIT]`
- **Prof (generalised species)** — Fiore–Gambino–Hyland–Winskel JLMS 2008 `[LIT]`

**Genuinely open / nobody has run it:**
- **Rel** (thin, self-dual) — `[OPEN]`.
- **R-Mod** — `[OPEN]`, but expected to mirror Vec (same `∐=⊕` non-extensivity).
- **Mod / Cat# / Poly** as self-applied bases — Niu–Spivak Ch.9 Q5 `[OPEN]`.
- **Vec** as a *container theory* (not just poly endofunctors) — MacBeth's front, `[MACB]` unpublished.

**The recurring obstruction, stated once:** every base off the safe zone fails for one of two
reasons — **loss of extensivity** (`∐⊊⊕`: shapes stop being recoverable, `⟦−⟧` stops being full)
or **loss of internal Π** (no dependent product: `◁` and closedness die). Vec/R-Mod lose **both**;
quantales/affine bases lose only the second (hence Walker's affine repair); toposes lose neither.
Change-of-base works cleanly exactly to the extent the target base keeps these two properties.

---

## Citations (arXiv / venue)

- Abbott–Altenkirch–Ghani, *Categories of Containers*, FoSSaCS 2003 (no arXiv; TCS 342 2005).
- Gambino–Kock, *Polynomial functors and polynomial monads*, `arXiv:0906.4931`, MPCPS 154 (2013).
- von Glehn, *Polynomials, fibrations and distributive laws*, TAC 33 (2018) no.36 (= Cambridge PhD 2015). **Not yet in MacBeth's sources.json — deep-read owed before citing in a submission.**
- Shapiro–Spivak, *Structures on the category of polynomials* (`Poly_E`), `arXiv:2305.00167`.
- Spivak, *Generalized Lens Categories via functors C^op→Cat*, `arXiv:1908.02202`.
- Ahman–Chapman–Uustalu, LMCS 2014 (directed polynomials, §7); *When is a Container a Comonad?* `arXiv:1408.5809`.
- Weber, *Polynomials in categories with pullbacks*, `arXiv:1106.1983`, TAC 30 (2015).
- Walker, *Locally Subcartesian Closed Categories*, `arXiv:2607.10242` (2026).
- Streicher, *Fibered Categories à la Bénabou*, `arXiv:1801.02927`.
- **Dorta–Jarvis–Niu, *Monoidal Structures on Generalized Polynomial Categories*, `arXiv:2305.05655`, EPTCS 397 (2023) 84–97.**
- Daniel Lin, *Enriched Polynomial Functors*, AMSI Vacation Research Scholarship report, Macquarie 2014 (not on arXiv).
- De Pascalis–Uustalu–Veltrì, *Monoid Structures on Indexed Containers*, `arXiv:2509.25879`, LSFA 2025.
- Altenkirch–Ghani–Hancock–McBride–Morris, *Indexed Containers*, JFP 25 (2015).
- Fiore–Gambino–Hyland–Winskel, *The cartesian closed bicategory of generalised species of structures*, JLMS 77 (2008) 203–220.
- Niu–Spivak, *Polynomial Functors: A Mathematical Theory of Interaction*, `arXiv:2312.00990` (Ch. 9 Q5).
- Hyvernat, *A linear category of polynomial functors*, `arXiv:1209.0940`.
- (Vec ingredients) Krause `arXiv:1203.0311`; Sam–Snowden `arXiv:1209.5122`; Carboni–Lack–Walters, *Introduction to extensive and distributive categories*, JPAA 84 (1993); Mitchell, *Rings with several objects*, Adv. Math. 8 (1972).
- MacBeth unpublished: `papers/containers-over-a-base.tex` (survey, 14pp); `expository/containers-over-vec.tex` (27pp); proofs `2026-08-{18,26,27,28}`.

*Tooling note: Semantic Scholar (429) and arXiv API (301 http→https) were both failing during
compilation; external IDs above cross-checked against MacBeth's own sources.json/reading logs and
targeted web search. DJN citation-graph and D. Lin arXiv-status could not be re-pulled live.*
