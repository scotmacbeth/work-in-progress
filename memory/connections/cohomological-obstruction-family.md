# Vanishing cohomology as *the* obstruction — a cross-domain family, not just my trick

**Found:** 2026-07-15 (dream), consolidating the 07-15 browse. **Sharpened 2026-07-16.** **Status:**
*pattern-level* observation (a shared **theorem shape** across unrelated objects), NOT a claimed
theorem and NOT a scoop. The value is that it tells me my Zappa–Szép obstruction is an instance of a
wave the applications world is independently riding — which is exactly the grant's "compositional
correctness has consequences" narrative. (Discipline: [[circular-verification-and-reading-depth]].)

**★ 2026-07-16: the last scoop-risk on this line is CLEARED.** arXiv:2606.01663 = "A Sheaf Framework
for Strategic Multi-Agent Systems" (Hernández–Sánchez-Soto, 1 Jun 2026) — abstract-level verify: it
frames **Nash equilibria as global sections (H⁰-level)** in a topos, **NOT an H² obstruction**. It
does **not** touch my `(G)⟺[ω]=0∈H²`; the H² tower stays covered by Rosebrugh–Wood / Baues–Wirsching /
Pirashvili. So 2606.01663 is a **cousin** (H⁰-consensus story), not a competitor — same multi-agent-
sheaf neighbourhood, different degree. **The whole cluster now sits at: H⁰ (2606.01663 consensus),
H¹ (2605.11204 identifiability), H² (mine, existence-of-factorization) — different degrees, different
axes, none scoop me, none cite the categorical literature.**

**The axis distinction, stated once (the 07-16 refinement):** the multi-agent-systems papers use sheaf
cohomology for **recovery / identifiability** (2605.11204: edge potentials recoverable iff H¹=0) or
**consensus / equilibrium** (2606.01663: H⁰ global sections). My `(G)⟺[ω]=0∈H²` is about **existence of
a compositional factorization**. Same *idiom* (cocycle → coboundary), genuinely different *axis*. The
grant is stronger for saying exactly this than for over-merging them.

## ★ 2026-09-09 (dream cycle 2): this note is the *guard* on the H¹ sheaf prediction

[[total-composition-constructs-partial-composition-lifts]] (written earlier the same day) predicts an
`H¹` obstruction for multi-agent sheaf gluing. **This note already contains an `H¹` theorem —
`2605.11204` Thm 2 — and it does NOT confirm that prediction**, because of the axis distinction
stated below: identifiability/recovery vs existence-of-a-factorization. Treating the degree match as
confirmation is an **invariant collision** ([[fusion-versus-identification]], third mode). The
H⁰/H¹/H² ladder recorded here is a ladder of *sites and axes*, not a scale of one phenomenon —
which is precisely why it is worth more to the grant than a merged story would be.

## The shared shape

> *A global/compositional property holds **iff** a cohomology class vanishes.*

Three sightings, three degrees, three sites, structurally the same:

1. **Mine — Zappa–Szép global closure (G).** For `K = C ⋈ D` a strict factorization, condition (G)
   ("free bases close into a wide subcategory") is a **holonomy** obstruction:
   `(G) ⟺ [ω] = 0 ∈ H²(Sk_C; 𝒟)`. Existence = **Rosebrugh–Wood JPAA 175 (2002)**; abelian
   classification = **Baues–Wirsching JPAA 38 (1985)**; nonabelian = **Pirashvili arXiv:1512.03250
   Thm 7**. The whole tower is *citations* — my delta is the identification + the rigid-twist
   (Z/2 generator) computation. → [[g-obstruction-is-baues-wirsching]]. **Site:** the skeleton of a
   small category. **Degree:** H². **"Global property":** the laxator vanishes / a distributive law
   of categories exists.

2. **Multi-agent identifiability — Anwer–Riess–Hale, arXiv:2605.11204** (Georgia Tech, May 2026;
   *deep-read*, full HTML). **Theorem 2:** for a multi-agent system whose dynamics follow a nonlinear
   cellular-sheaf Laplacian on a directed communication graph, the edge potentials of **all
   conservative, edge-separable** forces are **recoverable from trajectory data iff `H¹(G; ℱ) = 0`**
   (Hodge: `ker δ* ≅ H¹`). **Site:** a communication graph. **Degree:** H¹. **"Global property":**
   the local interaction laws are identifiable. **Zero category theory, zero cites to
   Spivak/Ghani/Ahman–Uustalu** — pure spectral-graph/sheaf-Laplacian.

3. **Planning coherence — Hernández–Sánchez-Soto, arXiv:2605.01879** (May 2026; *deep-read*). A
   "Site of Time" (poset of closed intervals + Grothendieck topology), sheaves ℱ_World/Mem/Goal,
   plan-incoherence framed as sheaf-gluing failure and H¹/H² as "topological obstructions to a global
   plan." **⚠️ No theorem is proved** — the cohomology-as-obstruction claim is asserted qualitatively,
   formalization deferred. This is *appetite*, not a competitor.

4. **★ Fusion-category exact factorization — Müller–Peña Pollastri–Plavnik, arXiv:2405.10207**
   ("On bicrossed product of fusion categories and exact factorizations", v2 Jul 2025). Lifts matched-pair
   / bicrossed (Zappa–Szép) products from **groups to fusion categories**; §4 defines matched pairs (Def
   4.1) and constructs the bicrossed product (Thm 4.6, Cor 4.9) — *literally the same characterization
   shape* as my pairwise-ZS criterion, one level up in categorical semisimplicity. **Site:** fusion
   category. **NOT H²-valued — CORRECTED 2026-07-22 (browse2).**
   >
   > **⚠️ CORRECTION (2026-07-22 browse2):** the 07-21 entry below ("reports a cohomological obstruction,
   > Sec 4 ≈ Thm 4.16") was **WRONG — a WebFetch-summarizer hallucination**, not real paper content. A
   > 2026-07-22 re-read got the actual PDF text (via direct `Read`, bypassing the summarizer) and grepped
   > it for "obstruction"/"cohomology"/"H^2"/"H2": **zero hits, anywhere in the paper.** The real Remark
   > 4.16 explicitly leaves the categorified question **OPEN** ("Question 3: is every exact factorization
   > of fusion categories a bicrossed product? If not, how much can the associativities differ?") — the
   > paper only proves the *ring-level* analogue (Thm 3.14) and has **no obstruction-theoretic machinery
   > at all**. This is a live instance of [[the-summary-is-what-gets-audited]]: a first-pass WebFetch
   > summary manufactured a false structural-sibling claim that survived one full dream-consolidation cycle
   > before a direct-text re-read caught it. **Retire this as a "sibling theorem" data point** — it isn't
   > one. Downgrade to: a fusion-category paper that poses the analogous existence question and leaves it
   > open, i.e. mild interesting-territory context, not evidence of the idiom recurring at this level.
   > **NOT a scoop either way** (they don't answer it, so there's nothing to have scooped).

5. **★ CANDIDATE (UNVERIFIED) — self-similar groupoid actions / operator algebras — Mundey,
   Kwaśniewski, arXiv:2511.07906** ("Twisted operator algebras of self-similar groupoid actions on
   arbitrary graphs", Nov 2025). Found 2026-07-23 (browse) via a direct "Zappa–Szép + cohomology" web
   search. Studies T-valued twists that, per its abstract, **"exhaust the second cohomology group of the
   associated Zappa–Szép product category."** This is — at abstract level — *almost exactly my framing*:
   a degree-two class over a Zappa–Szép product category, but reached from an entirely independent
   tradition (self-similar groupoids / C\*-algebras), NOT Baues–Wirsching/Rosebrugh–Wood. If their
   H²(ZS-product-category) is the same cohomology as my `H²(Sk_C; 𝒟)`, this is the **first genuinely
   close sibling to `(G)⟺[ω]=0` in ~10 sessions of watching.** **Site:** Zappa–Szép product category of
   a self-similar groupoid. **Degree:** H² (claimed). **Status: agent-summary ONLY — MUST be direct-read
   (PDF/HTML, grep the actual text for "H^2"/"cohomology"/"exhaust") before it is treated as a sibling or
   a scoop.** This discipline is not optional: the previous #4 (2405.10207) was a WebFetch hallucination
   that survived a full dream cycle as a "crown find" before a direct-text read found *zero* cohomology
   content. Do NOT let 2511.07906 repeat that. → follow-up in `questions/open-threads.md` (07-23 block).

6. **★ NEW 2026-08-12 — skew-brace second cohomology — Rathee–Yadav, arXiv:2601.12371** ("Skew brace
   extensions, second cohomology and complements", 2026). Found on the live-PROVE browse. **This is the
   closest structural cousin yet to the *new* 08-12 result** — not to `(G)⟺[ω]=0` (the ZS-*existence*
   axis) but to the ZS-*composition* result's splitting obstruction (`holonomy-composition-zs-bridge`,
   part (c')): my `1→A→E→B→1` with class `[ω]∈H²(B;A)`, and `[ω]=0 ⟺ E≅A×B ⟺ composite holonomy
   unentangled`. Their results are the same *shape*: **Thm 3.5** (skew-brace extension splits iff the
   associated group extension splits, under a socle condition); **Cor 4.4** (trivial `H²` ⟹ complement
   exists); Schur–Zassenhaus for coprime order (Thm 4.3). **Structural link worth chasing:** a skew
   brace `(A,+),(A,∘)` with λ-action **is** a matched-pair / Zappa–Szép phenomenon (bijective
   1-cocycle ⟺ exact factorization `Λ_A=(A,+)⋊_λ(A,∘)`), so their **`Ψ: H²_Sb(H,I)→H²_Gp(Λ_H,I×I)`**
   (Thm 1.1) — mapping a "special" second cohomology into an *ordinary group* `H²` — is exactly the
   move my (c') makes when the ZS-product stabilizer's class lands in ordinary `H²(B;A)` despite the
   ambient ZS structure. **Status: agent-summary depth (browse abstract-read only) — direct-read the
   `Ψ` construction (§ around Thm 1.1) and the socle condition before treating as a technique to
   borrow.** Does NOT itself discuss Zappa–Szép products by name (checked). **Site:** skew brace /
   its associated group. **Degree:** H². **"Global property":** the extension splits / a complement
   exists. → the ZS-composition proof's own obstruction construction should be compared against `Ψ`.

7. **★ NEW 2026-08-13 — post-Lie algebras / post-groups — Gubarev–Li–Sheng–Wang, arXiv:2605.21992**
   ("Inner post-Lie algebras and inner post-groups", 2026). An obstruction class
   `[κ]∈H²(𝔤▷,Z(𝔤))` (Lie) / `H²((G,∘),Z(G))` (group), built by pulling back a central extension
   along the inner-derivation map; the post-Lie/post-group structure is induced by a Rota–Baxter
   operator **iff the class vanishes** (Prop 2.10, Thm 2.12, Thm 3.11). Post-Lie algebras are the
   Lie-theoretic sibling of skew braces. **A second fully-independent instance of "H² obstructs
   splitting" outside the skew-brace/container literature** — same shape as entry #6 and my (c').
   **Site:** post-Lie algebra / post-group. **Degree:** H². **Status: agent-summary depth (browse
   abstract-read only).**

8. **★ NEW 2026-08-20 — the LINEAR rung: smash / crossed products of (Hopf-)algebras.** With the Vec
   front's algebroid *object* resolved as a `Mat(Vec)` matrix comonoid ([[vec-lax-matrix-crown-resolved]],
   [[containers-over-vec]]), the natural sequel is the *obstruction* to composing two linear containers —
   a "Zappa–Szép / smash product of algebras" carrying a degree-2 class. This is the whole family read
   **one enrichment level up** (group ⤳ k-algebra / Hopf algebra; semidirect ⤳ smash product; `H²_Grp`
   ⤳ Hochschild/Sweedler cohomology). The scaffold (browse `reading/2026-08-20.md`, all `agent-summary`):
   - **Mastnak `math/0210123`** ("On the cohomology of a smash product of Hopf algebras", 2002) —
     **DIRECT-READ 2026-08-21 (full 13pp PDF, `/home/agent/papers/mastnak_0210123.pdf`) → CONFIRMED the
     semidirect lift; pinned the OPEN rung.** For `H = N ⋊ T` a smash product of **cocommutative** Hopf
     algebras, A a commutative **trivial** H-module, Thm 5.1 gives the five-term exact sequence
     `0→H¹_meas(T,Hom(N,A))→H̃²(H,A)→H²(N,A)^T→H²_meas(T,Hom(N,A))→H̃³(H,A)` in **Sweedler cohomology**,
     with the leftmost/transgression-target terms = **measuring cohomology** (= the multiplication part
     of Singer-pair cohomology). It **specializes back to Tahara 1972 exactly** under `N=kN′, T=kG` group
     algebras (`Hⁱ(kH,A)≅Hⁱ(H,𝒰(A))`; Thm 2.1 `Hⁱ_meas(kG,Hom(N,A))≅Hⁱ(G,Alg(N,A))`). So my "obstruction
     family lifts one enrichment level" (group⤳Hopf, semidirect⤳smash, `H²_Grp`⤳Sweedler) is **CONFIRMED
     for the one-sided case**, and my `[ω]` maps to the pair (`H̃²(H,A)` = extension-classifier, `d` =
     transgression obstruction). Concrete anchor: Thm 6.1 `H²(Ug⋊kG,A)≅H²(g,A⁺)^G ⊕ H²(G,A)`.
     **★ THE OPEN RUNG (first-mover niche):** §1.1 *explicitly names* the bicrossed/matched-pair (double-
     cross) generality ("a special case of a bicrossed product arising from a matched pair") and then
     treats **only the one-sided smash** — T acts on N, NO back-action; Singer pairs are abelian with
     trivial coaction. So the **full Zappa–Szép / bicrossed product of Hopf algebras — the true Hopf image
     of a ZS product of directed containers — is flagged but UNDONE.** Extending the five-term sequence to
     the two-sided matched pair (back-action of N on T) is the genuinely new target. Neil steer requested
     08-21 on whether to stake it (no-moonshots discipline). Companion refs Mastnak flags: Hofstetter JA
     164(1994), Masuoka Trans.AMS 352(2000) (Singer-pair extensions), Mastnak JA 251(2002) (semidirect-of-
     groups companion). Root machinery = Sweedler universal measuring coalgebra `M(N,A)`, made Hopf (Prop
     3.1) — the convolution/measuring structure adjacent to the resolved `Mat(Vec)` algebroid picture.
   - **`math/0212003`** — Hochschild cohomology *ring* of a **group crossed product** (the most classical
     linear case, closest to the resolved `Mat(Vec)` algebroid). nLab *crossed product algebra* +
     *cocycled crossed products* give the multiplication shape `(a⊗h)(a'⊗h')=Σ a(h₁▹a')⊗h₂h'` to try to
     match against the matrix composition `(P◁Q)_{a,c}=⊕_b P_{a,b}⊗Q_{b,c}`.
   - **`2105.02528`** (weak crossed products over weak Hopf algebras) — a degree-2 twisted 2-cocycle whose
     lift-obstruction is a **degree-3 Sweedler class**; template to keep in mind if the naive H² guess for
     linear-ZS turns out one degree too low.
   - **⚠️ "Empty first-mover field" RETRACTED 2026-08-21 (browse).** The 08-20 claim ("Zappa–Szép product
     of algebras" = 5 papers, zero 2025–26) was a **too-literal phrase search**. The *concept* — a
     linear/Hopf Zappa–Szép product — is **very active 2024–26 under the standard name "matched pairs of
     Hopf algebras" / "bicrossproduct"**: `2505.07497` (González Rodríguez–Ramos Pérez, matched pairs +
     Hopf braces, 2026), `2512.00286` (Wang, matched pairs + Rota–Baxter Hopf), `2406.10009`
     (Ferri–Sciandra, matched pairs + Yetter–Drinfeld braces), **`2411.19238` (Gran–Sciandra, Hopf braces
     + semi-abelian categories)**. Field is NOT empty; retract "first-mover." **What is still genuinely
     open (a gap in a LIVE field, safer to stake):** the specific combination — a **degree-2/H² obstruction
     to matched-pair EXISTENCE, framed through polynomial functors / directed containers**. The matched-pair
     papers *construct* the products; none (per abstracts) carry an existence-obstruction cohomology in
     container language; Mastnak does semidirect only. **★ BRIDGE:** Gran–Sciandra `2411.19238` puts Hopf
     braces in a **semi-abelian / protomodular** category = exactly the setting that SUPPLIES a cohomology
     to hang `[ω]` on; and Hopf braces = linearization of **skew braces** = Rick's H²/Ψ front (#6). So the
     linear-container obstruction front and Rick's skew-brace front may MEET at Hopf braces — first bridge
     between the two programs. **Site:** algebra / Hopf algebra. **Degree:** H² (Hochschild/Sweedler; possibly
     +1). **"Global property":** the linear-ZS/matched-pair product exists. **Status: agent-summary depth
     (matched-pair papers), scaffold only; HELD pending Neil steer + direct-read of `2411.19238` and
     `2503.17191` (Purdy–Damato, already in seed).**
   - **★ 2026-08-21 browse2 — the citation-trail asymmetry IS the opportunity's shape (crown of the
     08-21 dream).** Two H² traditions, both live in name only where I need them, and *disjoint in print*:
     (i) **Mastnak `math/0210123`** (smash-product Sweedler cohomology, the ONLY paper carrying the exact
     five-term existence/transgression sequence) is **DORMANT — 4 total citations, none since 2020, zero
     2024–26**; (ii) **Gran–Sciandra `2411.19238`** (semi-abelian Hopf-brace homological algebra) is the
     **most active cluster found — 10+ papers 2025–26**, nearly all one UCLouvain group (Gran, Sciandra,
     Bevilacqua, Ferri), **and it does NOT cite Mastnak.** So the *construction* side (matched pairs /
     smash products of Hopf algebras) is a booming field under non-ZS names, while the *obstruction-theory*
     side is either dormant (Mastnak) or in a disjoint tradition (semi-abelian). **The gap between "the
     product is known" and "its existence-obstruction cohomology is dormant/elsewhere" is the actual open
     seam** — not the retracted bare-phrase first-mover claim. Extra construction refs logged this session:
     `2502.20919` (González Rodríguez–Ramos Pérez, when smash products from matched pairs are Hopf braces,
     Drinfeld double). Open bridge nobody has checked in print (Q1, `questions/open-threads.md`): does
     Mastnak's five-term sequence specialize/generalize correctly against Gran–Sciandra's semi-abelian H²?
     Also flagged: nLab *bicrossed product* covers only the group level (no Hopf/Majid/Takeuchi) — a real
     coverage hole; and the nLab *double coset* ∞-groupoid/homotopy-pullback formulation may give a cleaner
     route to `h(s)=|A\U/B|` than the raw group-theoretic proof in [[emergent-holonomy-meeting-points-proved]].
   - **★★ 2026-08-22 DIRECT-READ of `2411.19238` (Gran–Sciandra, "Hopf braces and semi-abelian categories",
     v2 May 2025, full-text HTML read) — the gap is NAMED and UNBUILT, and the tool to fill it already
     exists.** Confirmed against the text: (a) cocommutative Hopf braces 𝖧𝖡𝖱_coc are **semi-abelian** (Thm 5.2)
     and **strongly protomodular** (Thm 7.1); skew braces sit inside as a Birkhoff subcategory / localization
     (Thm 6.12), and the Hopf-brace axiom is *explicitly* the **linearization of the skew-brace axiom** (§1).
     (b) The matched-pair story is fully present: **Hopf brace ≅ matched pair of actions** (Def 5.9 / Thm 5.11),
     smash product R#H (§3), and a **semidirect-product SPLITTING criterion** (Prop 3.3) — but presented as an
     *equivalence + splitting description*, NEVER as an obstruction class. (c) **NO cohomology is built**: no
     H², no five-term sequence, no Ext, no Baer sum; the only degree-2-flavoured content is a Huq=Smith
     commutator result (Prop 8.7). The authors **explicitly defer cohomological applications to future work.**
     (d) **They do NOT cite Mastnak** and make no reference to Hochschild/Sweedler smash-product cohomology —
     the citation-trail asymmetry is confirmed from the primary source, not inferred. **⟹ The upgrade of the
     seam:** the `[ω]∈H²(B;A)` matched-pair non-splitting obstruction is a *named open gap inside the most
     active cluster*, and the semi-abelian/strongly-protomodular structure they prove is EXACTLY the hypothesis
     under which **Bourn / Bourn–Rodelo semi-abelian cohomology** (H²_{s.a.} classifying central/abelian
     extensions) exists. So the target is no longer "invent a cohomology in an empty field" (moonshot) but
     "instantiate the standard semi-abelian H² on 𝖧𝖡𝖱_coc and identify its degree-2 class with my directed-
     container ZS `[ω]` — the class Gran–Sciandra left as future work." This is the concrete, de-risked PROVE
     candidate; flagged to Neil (daily 08-22) with the Rick-bridge question. Still HELD pending Neil steer, but
     the risk profile flipped from moonshot → scaffolded-gap. Route to Bourn: *Mal'cev/semi-abelian cohomology*
     (Bourn 2007; Rodelo), NOT Mastnak's Sweedler sequence (which is the *smash*/semidirect shadow one level down).
   - **Banerjee–Kour(–Paik) measurings program** (`2607.17470`, `2504.06873`) is the recurring active hub
     around Mitchell `1704.00329` (the algebroid-variance paper this front already cites) — Hochschild
     homology of categories enriched over algebras. Standing watch; nothing yet bridges to ZS/container
     language directly.
   - **★ 2026-08-22 browse — cluster grown to ~15+ papers (10+ → ~15+ in one cycle), still zero contact
     with Mastnak or skew-brace-H² vocabulary; and the single most load-bearing new find sits at the
     SKEW-BRACE level, not the Hopf-brace level.** Six new Gran–Sciandra-adjacent papers found
     (`2607.28380` SKB non-LACC, `2605.03798` central series, `2603.22200` semi-abelianness of Hopf
     monoids, `2510.22653` coalgebraic Ω-groups, `2509.09992` Hopf formulae for cocommutative Hopf
     algebras, plus the published *J. Algebra* version of the anchor); reference lists of the three
     newest checked directly — none cite Mastnak, none use ZS/bicrossed language, none cite Rathee–Yadav.
     Repeated across three sessions now (08-20/21/22) — the disjointness reads as structural, not a
     snapshot artefact. **The actual find: `2409.18056` (Gran, Letourmy, Vendramin, "Hopf formulae for
     homology of skew braces," JPAA 229 (2025) no.11) does Hopf-formula/Stallings–Stammbach homological
     algebra directly on SKEW BRACES**, not their Hopf-brace linearization — missed by every earlier
     sweep purely because of its 2024 arXiv date despite a live 2025 revision. This is a **shorter
     candidate path to the Rick-bridge** than routing through Hopf braces at all: if the semi-abelian H²
     machinery Gran–Sciandra build for Hopf braces has a direct skew-brace-level cousin already
     half-built in `2409.18056`, the linearization step (skew brace → Hopf brace) may not be a necessary
     hop. **★ 2026-08-23 — the H²-reach question is RESOLVED (research agent, direct PDF read; saved
     `/home/agent/papers/gran_skew_braces.pdf`, text `gran.txt`): `2409.18056` REACHES degree 2 — YES.**
     Its main result is a **generalized Hopf formula for the second HOMOLOGY `H₂` of a skew brace**,
     `H₂(B) ≅ (K∩[F,F])/[K,F]` for a free presentation `0→K→F→B→0` (in Grp, RadRng, and BR/braces
     flavours), with a **5-term Stallings–Stammbach exact sequence** (Thm 6.1). BUT three caveats decide
     the bridge length: (i) it is **HOMOLOGY `H₂`, not cocycle `H²`** — a Schur-multiplier-type invariant,
     not a 2-cocycle group; (ii) its extension-classification is done via **categorical Galois theory**
     (Janelidze–Kelly central extensions / weakly-universal central extension + Galois groupoid), NOT via
     a cocycle `H²(B;A)` classifying non-split extensions; (iii) it carries **no matched-pair / Zappa–Szép
     composition structure**. For the cocycle `H²` it *explicitly points to Rathee–Yadav* (#6). **⟹ The
     Rick-bridge is "one-and-a-half hops": degree 2 IS reached, but the cocycle reformulation AND the
     matched-pair/ZS connection are both still missing — and that missing pair is precisely where my
     directed-container `[ω]` would live.** **★★ Load-bearing NEW find inside this read: `2409.18056`
     cites `Bourn, "Split epimorphisms and Baer sums of skew left braces"` (+ Bourn–Facchini–Pompili) —
     i.e. the semi-abelian Baer-sum / `H²`-extension machinery is ALREADY instantiated directly on SKEW
     BRACES by Bourn himself.** A Baer sum IS the abelian-group structure on the `H²` classifying abelian
     extensions, so this may be the most direct route of all: the semi-abelian `H²` tool lives on skew
     braces natively, no Hopf-brace linearization hop. **NEXT (if Neil greenlights): direct-read the
     Bourn skew-brace Baer-sum paper — it, not `2411.19238`, is the likely actual home of the `[ω]` I
     want to identify.** (`2409.18056` does NOT cite Mastnak — citation-trail asymmetry confirmed from a
     third primary source.)
     Also found (web agent, off-arXiv): Ferri–Sciandra "Matched pairs and Yetter-Drinfeld braces"
     (*Canad. J. Math.*, Online First 2025) — new terminology in the same cluster, unread beyond the
     abstract, unknown whether it touches the Mastnak seam.
   - **★★ 2026-08-23 browse — Bourn `2310.05568` LOCATED and browse-read; it is the likely native home of
     `[ω]`, and the "structural disjointness" thesis is REFINED (no longer fully disjoint).** The
     `2409.18056` H₂-reach read (08-23 WAKE) named "Bourn's skew-brace paper" as a likelier `[ω]` home than
     the Hopf-brace route; this browse found it: **Bourn, "Split epimorphisms and Baer sums of left skew
     braces", arXiv:2310.05568 (J. Algebra 652 (2024) 188–207)**. Works **directly on the category `SkB` of
     left skew braces** — no Hopf-brace linearization. **Thm 4.3:** `SkB` is *strongly protomodular* (fails
     for the weaker digroup category `DiGp`). **Prop 5.1/5.4:** characterizes exact sequences of skew braces
     with abelian kernel; difference subobjects between two such extensions are ideals. Constructs an abelian
     group **`Opext((Y,⋆,∘),(A,+,+),(φ⋆,φ∘,ξ))`** of iso-classes of extensions with fixed direction — this
     **is** the classical Baer-sum / extension-classification group, structurally H², **though the paper
     never writes "H²" or "cohomology"** (grepped directly, zero hits) and has **zero ZS/matched-pair
     content** (grepped, zero). So the tool sits one construction-step short of an `[ω]`: `Opext` is the
     classifying group, but the transgression / long-exact-sequence apparatus a directed-container `[ω]`
     attaches to is not assembled there. **Status: browse-level HTML (ar5iv) extraction — a direct
     load-bearing read is owed before any PROVE.** Sciandra et al., **"The Baer Transform for Skew Braces",
     arXiv:2607.03081 (2026)** extends the `Opext` construction (title/abstract only). Also noted:
     `2607.25512` (Ardizzoni–Bottegoni–Cigoli–Sciandra, protomodularity of cocommutative Hopf monoids **in
     duoidal categories**) — a loose methodological echo of my own `(⋉,⋊)` duoidal/LDC work on Poly
     ([[ltimes-rtimes-duoidal-ldc-proved]]), unchecked for real overlap.
     **★ The disjointness is now ASYMMETRIC, not total.** Across four sessions (08-20/21/22) the three H²
     traditions read as citation-disjoint; the 08-23 reference-list fetch corrects this: **`2409.18056`
     (Gran–Letourmy–Vendramin) cites BOTH Bourn `2310.05568` AND Rathee–Yadav's earlier "Cohomology,
     Extensions and Automorphisms of Skew Braces" (arXiv:2102.12235, JPAA 228(2), 2024).** So the
     semi-abelian side *is aware of* the skew-brace-H² side — but **one-directionally**: Rathee–Yadav's
     `2601.12371` (#6, Rick's-front anchor) reference list (~28 items, fetched in full) cites **zero** back
     into the Gran/Sciandra/Bourn cluster; Mastnak `math/0210123` re-confirmed at exactly 4 cites, none
     since 2020, contact with neither tradition. **Vendramin** (co-author on `2409.18056` semi-abelian-side
     AND author of the cited-into `2102.12235` skew-brace-side) is the common author-adjacent node — the
     closest existing bibliographic thread to pull for a genuine bridge write-up. This slightly de-risks the
     bridge (less chance of reinventing an unread connection — it is already half-acknowledged in print)
     while confirming the **technical** bridge (the H² identification itself) still exists nowhere. Canonical
     citation for the anchor going forward: **Gran–Sciandra, "Hopf braces and semi-abelian categories",
     *J. Algebra* 690 (2026) 266–303** (published `2411.19238`).
   - **★★ 2026-08-22 DIRECT-READ of Bourn `2310.05568` (full PDF, `/home/agent/papers/bourn_2310.05568.pdf`) —
     VERDICT (B): the tool is a BARE classifying group, NOT a cohomology apparatus; the linear-ZS/H² target
     is NO-GO for now (parked, not abandoned).** Confirmed against the text: Bourn's **`Opext`** is the
     abelian group (under **Baer sum**) of iso-classes of abelian-kernel skew-brace extensions
     `1→A→X→Y→1` with fixed direction and skewing index, in **Mac Lane's `Opext` notation (p.15)**. There is
     **NO transgression map, NO long/five-term exact sequence, NO connecting homomorphism** around it — no
     cohomological machinery. So MacBeth's degree-2 `[ω]` **cannot be read off as a connecting-map image**;
     that apparatus would have to be built from scratch. The genuinely ZS-adjacent object in the paper is
     instead Bourn's **"skewing index" `ξ: Y→S_A` (Def 1.3, 5.2)** — a set/bijection-valued obstruction to a
     split epi being a *pure* semidirect product of a pair of actions (trivial index ⟺ it is), i.e. a
     **matched-pair / split-factorization obstruction, but NOT a cohomology class.** Main structural theorem:
     **`SkB` (left skew braces) is STRONGLY protomodular (Thm 4.3)**, giving Huq=Smith. The paper does
     **NOT cite** Gran–Sciandra, Rathee–Yadav, Mastnak, or Bourn–Rodelo. **CONSEQUENCE:** combined with
     Neil's 2026-08-21 deprioritization of homology, the linear-ZS/H² target is **NO-GO for now (parked,
     not abandoned)** — the `Opext` classifying group exists natively on skew braces, but the transgression
     apparatus a directed-container `[ω]` attaches to is simply not there to borrow.

**★ The (c')-splitting idiom now has THREE independent non-container homes + a classical root
(2026-08-13 consolidation).** Skew braces (#6, Rathee–Yadav arXiv:2601.12371), post-Lie/post-groups
(#7, arXiv:2605.21992), and ordinary group extensions (nLab `group+extension`: central ext ≅
`H²_Grp(G,A)`, trivial class ⟺ split — textbook folklore). All share the exact shape of my
`holonomy-composition-zs-bridge` part (c'): pull back a central/abelian extension along a structure
map, take the section's cocycle, vanish ⟺ split. **Classical root:** Rathee–Yadav cite **Tahara 1972,
"On the second cohomology groups of semidirect products"** — likely the original precedent for the
semidirect-product H² technique my (c') reinvents in the ZS-stabilizer setting; the natural citation
when (c') is written up formally. ⚠️ Tahara 1972 known ONLY via Rathee–Yadav's reference list, NOT
read — direct-read before citing as "classical precedent" vs "structural analogue".
**★ 08-14 browse upgrade — the worked restriction map exists: Hartl–Leroy, "On the second cohomology
of semidirect products", arXiv:0707.0291 (2007)** (`agent-summary`, abstract/statement level). For
`G=N⋊T` and a G-module `M`, constructs the simultaneous restriction
`res=(res^G_N,res^G_T)^t : H²(G,M)→H²(N,M)×H²(T,M)` inside a five-term exact sequence — explicitly
EXTENDS Tahara 1972 (trivial-action case: `H²(T,M)` a canonical direct factor of `H²(G,M)`). This is
exactly the object the two-`[ω]`-sites question needed: a worked map between a composite-group class
and its factors' classes, with an exact-sequence account of what restriction sees/loses. MO 229393
points to Hochschild–Serre (`E_2^{p,q}=H^p(T,H^q(N,V))`) as the general machinery. Deep-read the
five-term sequence before finalising the "restriction kills the handoff generator" verdict in
[[two-omega-sites-not-isotropy-restriction]] (which already PROVED the two `[ω]` sites irreducibly
distinct via rigid-skeleton zero-restriction — Hartl–Leroy is the abstract confirmation, not needed
for the proof). Grant framing
earned: *"directed containers exhibit the same H²-splitting-obstruction pattern found across Lie
theory, group theory, and Hopf-algebraic matched pairs."* **Caution (Albano–Stefanelli,
arXiv:2605.30097):** skew braces are NOT action-accessible (no universal split-extension classifier,
order-24 GAP counterexample; extends negatively to pre/post-Lie) — so do NOT assume a "moduli of
ZS-compatible actions"/classifying object exists for directed containers by analogy; any such
generality needs case-by-case proof.

**The cluster is real and independently converging:** 5+ agent-sheaf papers 2025–2026 (2605.11204,
2605.01879, 2606.01663, 2605.14033, 2504.17700, 2603.27015) put sheaf cohomology on multi-agent
systems. **None yet cite the container/Zappa–Szép-of-categories literature; none yet state my exact
theorem.** Nelson Niu himself (Poly-book co-author) has an ACT-2026 paper applying **temporal sheaf
theory to public-health modelling** — so the sheaf-cohomology angle is being worked from inside the
Poly community too. (The fusion-category ZS line, 2405.10207, is downgraded out of this cluster —
see correction above; it poses the analogous question but does not answer it cohomologically.)

**★ 2026-08-31 dream — three NEW witnesses widen the LITERATURE-ANCESTRY diversity, not just the count
(browse3, all `agent-summary`/HTML-full-text depth — see `reading/2026-08-26-browse3.md`).** The
earlier cluster was all one neighbourhood (ML sheaf-Laplacian / multi-agent game theory). Browse3
surfaced the idiom in genuinely *disjoint* traditions:
- **Distributed-computing topology — Felber–Hummes Flores–Rincon Galeana `2503.02556`** ("A
  Sheaf-Theoretic Characterization of Tasks in Distributed Systems", SIROCCO 2025). A "task sheaf" on
  the poset of local process views; solutions = **global sections**, and **sheaf cohomology = the
  obstruction to task solvability**, model-independent (synchrony/failure/adversary-agnostic). This is
  the **Herlihy–Kozlov–Rajsbaum distributed-computing-topology lineage** — an ancestry with *zero*
  overlap with the ML-sheaf cluster or the CT tradition. **Site:** process-view poset. **Degree:**
  H*(task sheaf). **"Global property":** the distributed task is solvable. Structurally identical to my
  `(G)⟺[ω]=0` move; independent third-tradition witness.
- **Systems engineering (MBSE), Lean-formalized — Gibson `2605.08609`** ("Sheaves as a Means of
  Maintaining Consistency in MBSE"). CPS architecture = space of pairwise engineering-domain
  interfaces; design presheaf of "views" satisfies the sheaf condition ⟹ **global multi-view
  consistency reduces to checking only PAIRWISE interface compatibility** — and the whole thing is
  **machine-checked in Lean 4**. No cohomology stated, but the pairwise-to-global reduction is *exactly*
  the shape of my pairwise-ZS criterion `(L)∧(G)` and, crucially, **the direct template for SEED Q4**
  (supply chain as directed container; sheaf condition = inventory consistency). The Lean artifact is
  reusable scaffolding for a future `/lean` on that front — the concrete piece SEED Q4 was missing.
- **Dynamical systems (no sheaves yet) — Wehbe, Topos blog 2026-01-30** ("Composition of attractor
  lattices"). A realization map embeds the product of component attractors into the composite's
  attractor lattice but **misses "corner" attractors created by interaction**; join-closure recovers
  them for continuous systems, fails for discrete, and the post itself flags that the fix "will require
  cascade products and sheaf-theoretic frameworks." Same *shape* — composition ≠ product, the gap is a
  named obstruction — reached without any sheaf/cohomology machinery yet. Pattern-match citation for the
  book's obstruction chapter, NOT a scoop.

**What this changes:** the idiom now has witnesses in (a) group/Hopf/skew-brace extension theory (my
ZS front + the algebraic family above), (b) ML sheaf-Laplacian multi-agent systems, (c) multi-agent
game theory (H⁰ Nash), (d) **distributed-computing topology** [NEW], (e) **MBSE consistency** [NEW,
Lean], (f) **dynamical-systems attractor lattices** [NEW]. Six *bibliographically independent*
lineages, none using container/ZS language. This is no longer "scattered coincidence" — it is a
genuine cross-domain **proof-idiom** (cocycle → coboundary / pairwise → global), and the honest grant
claim is exactly that: *the container/directed-container/ZS framework is the first to name this
obstruction via distributive laws specifically.* **Still a pattern-level / exposition-and-Impact asset,
NOT a proof target** (each site is different math; the shared thing is the idiom). Open check
(`questions/open-threads.md`): does any pair actually cash out to shared *theorems*, or is it purely
naming-level? — needs a careful side-by-side before claiming more than independent rediscovery.

## Why this is a connection and not a coincidence

The objects are genuinely different — a small category's skeleton vs a communication graph vs a poset
of time-intervals; H² vs H¹ vs "H¹/H²". So this is **not** "the same theorem." What *is* shared is a
**proof idiom**: express the global property as a cocycle condition, then read off "solvable ⟺ class
is a coboundary." That idiom is the bridge between:

- **Path 7-ish (Zappa–Szép / distributive laws)** — where I already have `(G) ⟺ [ω]=0`, and
- **Path 5 (agent orchestration, "compositional correctness has economic consequences")** — where the
  applications crowd is groping toward exactly this vocabulary but hasn't connected it to the
  container/comonoid machinery.

**Fairbanks' "Set-sets" Topos blog post (2025-11-21)** may be the missing hinge: it argues **comonads
generalize both small categories (via directed containers) AND topological spaces (via sheaves)**.
If that holds up, the container world and the sheaf-cohomology world are two faces of the comonad — and
my `(G)⟺H²` and their `identifiability⟺H¹` would be two shadows of one comonadic obstruction theory.
That is speculative and the blog is *agent-summary* depth; flag before leaning on it.

## What to do with it

- **Grant material, immediately usable.** "The obstruction to composing agents is a cohomology class"
  is a one-sentence bridge from my proved theorem to a live, funded (DARPA/AFOSR) application area.
- **A `connections/` write-up at proof-technique level** (cocycle → coboundary, in each site) is now
  unblocked — 2606.01663 was the last scoop-risk and it is H⁰, not H² (verified 07-16). This can turn
  from "connection" into grant prose whenever the applications section needs it.
- **Do NOT invert the arrow prematurely.** The tempting overclaim is "therefore multi-agent
  identifiability is a special case of my theorem." It is not — different degree, different site. The
  honest claim is *shared idiom*, and the grant is stronger for stating exactly that.

## Sources & depths
- arXiv:2605.11204 (Anwer–Riess–Hale) — **deep-read** (full HTML). Thm 2, H¹=0 ⟺ identifiable.
- arXiv:2605.01879 (Hernández–Sánchez-Soto) — **deep-read**; no theorem, appetite only.
- arXiv:2606.01663 (Hernández–Sánchez-Soto, "A Sheaf Framework for Strategic Multi-Agent Systems") —
  **abstract-verified 2026-07-16**: Nash equilibria = global sections (H⁰), NOT H². Cousin, not scoop.
- Rosebrugh–Wood JPAA 175 (2002); Baues–Wirsching JPAA 38 (1985); Pirashvili arXiv:1512.03250 — my
  H² tower, all *cited* (banked, do not re-open). → [[g-obstruction-is-baues-wirsching]]
- Fairbanks "Set-sets", Topos blog 2025-11-21 — **agent-summary** depth; the comonad-as-hinge idea.
- arXiv:2511.07906 (Mundey–Kwaśniewski, "Twisted operator algebras of self-similar groupoid actions
  on arbitrary graphs") — **DEEP-READ 2026-07-24 (direct PDF text + grep, not summarizer) → CLEARED
  ORTHOGONAL, thread CLOSED, do NOT re-flag.** The H²-of-a-ZS-category phrase is genuinely present
  (unlike the 2405.10207 hallucination), but their ZS product `E*⋊G` is built *by formula* from a
  self-similar action (Remark 4.22, Mundey–Sims matched-pair construction) — its existence is
  definitional, never in question. Their H² classifies *twisted-representation data* (2-cocycles)
  layered ON an already-existing category; grep for "obstruct" = zero hits. This is the COMPLETENESS
  axis (classify twists on a fixed category), NOT my EXISTENCE axis ((G)⟺[ω]=0 = obstruction to the
  category existing at all). Reverse-cites: only 2 (Gonzales–Hume; Aakre–Szakács), both pure
  operator-algebra, no CT engagement. The real potential sibling remains **Mundey–Sims 2025a
  matched-pair cohomology** (unread). Also CLOSED same cycle: arXiv:2503.08630 (Abell-Ball et al.,
  "ZS products for k-graphs") — deep-read, zero cohomology vocabulary; takes ZS-decomposition
  existence as given (Mundey–Sims Lemma 3.27), characterizes when induced factor-actions are trivial
  (crossed-product special case, not an existence criterion). Both threads: real full-text reads
  behind them now, do NOT re-flag as unread.
- arXiv:2405.10207 (Müller–Peña Pollastri–Plavnik, "Bicrossed Products of Fusion Categories…") —
  **deep-read 2026-07-22 (direct PDF text, not summarizer)**. NOT H²-valued; leaves the categorified
  factorization question explicitly open (Remark 4.16); no cohomology content anywhere. Prior
  "cohomological obstruction" claim RETRACTED — see correction above. Citation-trail check (same
  session): 22 references, zero overlap with the Rosebrugh–Wood/Baues–Wirsching/Pirashvili stack;
  2 reverse citations, both within the fusion-category world, none touching containers/Poly. Two
  disjoint literatures independently reaching for the same *phenomenon* (matched-pair/exact-factorization
  existence) — worth a grant-narrative remark ("recurs across levels of abstraction"), not a citation
  MacBeth's proof needs to engage with.
- arXiv:2311.09600 (Mundey–Sims, "Homology and twisted C*-algebras for self-similar actions and
  Zappa-Szép products", `[MuS25a]`) — **DEEP-READ 2026-07-24 (full PDF, 3221 lines, direct grep) →
  CLEARED ORTHOGONAL. This was the last live unread candidate ("Mundey-Sims 2025a matched-pair
  cohomology") flagged above — now resolved and the thread is fully CLOSED, all four candidates
  cleared.** Definition 3.1 defines a "matched pair" `(C,D,⊲,⊳)` as globally-given data satisfying
  three pointwise axioms (MP1-MP3) — no notion of only-locally-defined matching data needing to glue.
  Lemma 3.5 then proves the ZS product category exists **unconditionally** from those axioms (a direct
  six-line associativity calculation) — no cohomological or further global condition appears anywhere
  in the construction. Sections 4+ build categorical homology/cohomology strictly ON TOP of an
  already-existing matched pair, to classify 2-cocycle twists — the SAME completeness-axis shape as
  the already-cleared 2511.07906 (unsurprising: 2511.07906 cites this paper as `[MuS25a]` throughout
  for its own ZS-product construction). No separate "matched-pair cohomology" preprint exists — the
  term lives entirely inside this paper's §3 (confirmed via an author-page check of all 9 Alexander
  Mundey arXiv papers).
- **★ Structural verdict, now well-evidenced across 4 independent papers, not just an unmatched
  vocabulary:** every operator-algebra-tradition ZS/matched-pair paper checked assumes globally
  compatible matching data *by fiat* and never asks whether it exists — MacBeth's setting is the
  opposite: only *locally* compatible data (on a skeleton/generators) is given, and (G)⟺[ω]=0∈H² is
  precisely the obstruction to that local data gluing to a global matched pair. The two traditions
  study genuinely different questions dressed in similar cohomological language. This sharpens (not
  just clears) the grant's novelty claim for the orchestration/supply-chain/ontology-merge spine.

- arXiv:2605.21992 (Gubarev–Li–Sheng–Wang, "Inner post-Lie algebras and inner post-groups") —
  **agent-summary** (2026-08-13 browse); `[κ]∈H²`, Rota–Baxter-induced iff vanishes (Prop 2.10 / Thm
  2.12 / Thm 3.11). Independent #7 instance.
- arXiv:2605.30097 (Albano–Stefanelli, "Action accessibility in the variety of skew braces") —
  **agent-summary** (2026-08-13); NO universal split-extension classifier for skew braces (Thm 2.13,
  order-24 GAP ctrex; Prop 3.5 extends to pre/post-Lie). Caution against a ZS-moduli overclaim.
- nLab `group+extension` — standard background; central ext ≅ `H²_Grp(G,A)`, non-central abelian
  needs H² *plus* induced action (matches why (c') scopes to *aligned* abelian).
- Tahara 1972, "On the second cohomology groups of semidirect products" — **UNREAD** (known only via
  Rathee–Yadav 2601.12371 refs); candidate classical precedent for the (c') semidirect H² technique.

- **arXiv:2606.13634 (Bottman–Richardson, "Operads for Compositional Reasoning in LLMs", 2026)
  — instance #8, and the first from the LLM side.** `deep-read` (upgraded 2026-08-29-browse2
  from a garbled-PDF agent-summary to a clean HTML read). The "questions operad" `𝒬` for
  multi-hop QA decomposition; QA models are `𝒬`-algebras; **Def 2.12** operadic consistency,
  with a worked Llama-3-8B inconsistency witness (3–1 disagreement across four partial
  collapses of a "First Lady during WWII" question tree). **§3 "Further directions"
  speculates — no construction, no theorem — that cohomology of the `𝒬`-algebra may
  distinguish *correctable* from *fundamental* inconsistencies.** Degree unspecified, so it
  does not yet slot into the H⁰/H¹/H² axis table above; but it is a fourth *independent*
  research community reaching for the same idiom, and the closest one yet to the Kodamai
  agent-orchestration framing. Speculative on their side — cite as convergent motivation,
  never as a result.

Related: [[g-obstruction-is-baues-wirsching]], [[ks-nogo-not-h2]],
[[two-atoms-zappa-szep-decomposition]], [[contravariance-is-the-fibrewise-op]],
[[emergent-holonomy-meeting-points-proved]], [[holonomy-composition-zs-bridge-proved]].
