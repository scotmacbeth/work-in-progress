# Citation Trail Browse — 2026-08-06

## Paper 1: Gambino-Kock, "Polynomial functors and polynomial monads" (arXiv:0906.4931)

Reverse citations pulled via Semantic Scholar (limit 100, most recent first).

### 2026
- Charles Walker, "Locally subcartesian closed categories"
- A. Slattery, Jonathan Sterling, "Bidirectional Elaborators à la Carte"
- Vasileios Aravantinos-Sotiropoulos, Theofilos Tsantilas, Christina Vasilakopoulou, "On categories of monads and comonads in double categories" — worth a skim; double-categorical treatment of (co)monads could bear on the T_M/G_M fibrational framing.
- Cornelius, Franchere, Hafeez, Keyes, Mehrle, Modi, Stapleton, "Composition of bispans of G-sets and plethysm"
- Mayuko Kori, "Coalgebraic Non-Wellfounded Proofs: Recursiveness and GTC"
- E. Cavallo, Jonas Höfer, "Univalence without function extensionality"
- Joachim Kock, Jesper M. Møller, "Signs in objective linear algebra..."
- D. Ahman, Andrej Bauer, "Sheaves as oracle computations"
- Joseph Hua, Yiming Xu, "Polynomial functors in π-clans for the semantics of type theory"
- **Kun Chen, "On polynomial functors and polynomial comonads over infinity groupoids"** — extends Ahman-Uustalu's directed-container/category theorem to infinity-groupoids (see Paper 2 notes below). Genuinely relevant neighbour to check against the book's Ch3/Ch7 material — worth a closer read to make sure the ∞-groupoid generalization doesn't touch the Set-level classification work.
- Cécilia Pradic, Ian Price, "Problems with fixpoints of polynomials of polynomials"
- Nawrocki, Hua, Carneiro, Xu, Woolfson, Rong, Hazratpour, Awodey, "A Certifying Proof Assistant for Synthetic Mathematics in Lean"

### 2025
- R. Atkey, Roly Perera, "Data Provenance as Automatic Differentiation"
- Michele De Pascalis, T. Uustalu, Niccolò Veltri, "Monoid Structures on Indexed Containers"
- Steve Awodey, "Algebraic Type Theory, Part 1: Martin-Löf algebras"
- Taichi Uemura, "An elementary definition of opetopic sets"
- Leoni Pugh, Jonathan Sterling, "When is the partial map classifier a Sierpiński cone?"
- Samuel Desrochers, "The List Object Endofunctor is Polynomial"
- **C. Purdy, Stefania Damato, "Distributive Laws of Monadic Containers"** (already a cleared neighbour per memory: purdy-damato-2503-cleared-neighbour)
- R. Street, "Objective Mackey and Tambara functors via parametrized categories"
- **Cécilia Pradic, Ian Price, "Weihrauch problems as containers"** (already tracked per memory: weihrauch-containers-frontier)

### On the specific question — cartesian-monad classification
No paper in this reverse-citation list, nor in a direct Semantic Scholar search for "cartesian monad classification polynomial monad Set" (partially blocked by rate-limiting, supplemented with a web search), addresses a general classification of Set-monads into cartesian vs. weaker "∏-Mendler" (single-valued, non-bijective transport) classes. The closest adjacent works found:
- Richard Garner, "Cartesian closed varieties I: the classification theorem" (Algebra Universalis, 2024) — classifies cartesian-closed *varieties* (Lawvere theories), a different question (algebraic theories vs. monad-transport structure). Worth a skim to rule out overlap but does not appear to touch the cartesian/∏-Mendler distinction directly.
- Fujii, Tsai, Montacute, Hasuo, "Monads and distributive laws in substructural contexts" (2026) — distributive laws in substructural settings, not a cartesian/non-cartesian classification.
- Nothing found addressing MacBeth's specific 4-rung ladder (λ-inv/pure-writer ⊊ non-branch ⊊ cartesian ⊊ ∏-Mendler) or an equivalent stratification.

**Verdict: no scoop found.** The cartesian-vs-∏-Mendler monad classification (crown-tfae-strict-chain result) still looks original as of this browse pass.

## Paper 2: Ahman-Uustalu, "Directed Containers as Categories" (arXiv:1604.01187)

Reverse citations (Semantic Scholar, up to 50):

### 2025-2026 (most relevant)
- **Richard Garner, Alyssa Renata, Nicolas Wu, "Stone Duality for Monads" (2026)**
- **David I. Spivak, "Categories by Kan extension" (2025)** — likely relevant to the book's Ch7 Kan-extension material; worth checking against spivak-2503-kan-extension-neighbour memory (may be a different/related paper — same author, similar theme, check for overlap).
- **Bryce Clarke, "The Grothendieck construction for delta lenses" (2025)** — Clarke is the delta-lens/PutGet reference already in memory (delta-lens-section-condition-is-putget); this looks like a direct follow-up, worth a read given DCont↔Cat↔lens connections in the book.

### Earlier (context)
- Dorta, Jarvis, Niu, "Monoidal Structures on Generalized Polynomial Categories" (2023) — already a known neighbour (dorta-jarvis-niu-neighbour)
- Shapiro-Spivak, "Structures on Categories of Polynomials" (2023) — already known (Cat# / fibrational-comonoid-layer-is-ss23)
- Smithe, "Open dynamical systems as coalgebras for polynomial functors..." (2022), and "Compositional Active Inference II" (2022)
- Capucci-Gavranović, "Actegories for the Working Amthematician [sic]" (2022)
- Clarke-Di Meglio, "An introduction to enriched cofunctors" (2022)
- Uustalu, "Container Combinatorics: Monads and Lax Monoidal Functors" (2017); Ahman-Uustalu, "Taking Updates Seriously" (2017), "Decomposing Comonad Morphisms" (2019)

## Paper 3: Spivak-Garner-Fairbanks, "Polynomial Comonoids" — actual arXiv match is "Functorial aggregation" (arXiv:2111.10968, listed by S2 as Spivak/Garner/Fairbanks; the exact ID 2110.05412 given in the task did not resolve to this paper). This is the paper establishing polynomial comonads ≅ categories and polynomial bicomodules ≅ parametric right adjoints.

Reverse citations (Semantic Scholar):

### 2025-2026
- **Kun Chen, "On polynomial functors and polynomial comonads over infinity groupoids" (2026)** — same hit as under Paper 1. Abstract: shows single-variable polynomial functors over ∞-groupoids are colimits of representable copresheaves, develops polynomial comonads in that setting, connects to complete Segal spaces, and explicitly "partially extend[s] classical results from Ahman-Uustalu's theorem." **This is the one paper in this whole browse pass most worth a careful read** — it sits exactly at the intersection of Papers 1–3 (Gambino-Kock polynomial monads + Ahman-Uustalu directed containers + Spivak-Garner-Fairbanks polynomial comonads), generalized to ∞-groupoids. Check whether it stays purely in the ∞-categorical setting (safe — one level up from MacBeth's Set/Cont work) or whether any Set-level corollary anticipates material in the book.
- Xiaoyan Li, Evan Patterson, Patricia L. Mabry, Nathaniel D. Osgood, "Compositional System Dynamics..." (2025)
- Yuto Kawase, "Double Categories of Profunctors" (2025)
- David I. Spivak, "Categories by Kan extension" (2025) — same as under Paper 2
- Bryce Clarke, "The Grothendieck construction for delta lenses" (2025) — same as under Paper 2

### Not found via citations but discovered adjacently (very recent, worth flagging)
- **Fairbanks, Carlson, Spivak, "Comonads as spaces" (arXiv:2607.15091, ~July 2026)** — did not show up in the reverse-citation list yet (too new to be indexed as citing, and it's a sibling/successor work rather than a citer), but found via web search while chasing the Spivak-Garner-Fairbanks line. Abstract: generalizes topological spaces and categories via comonads on Set (and beyond); shows every comonad on Set has an underlying topological space and category (reflection/coreflection); category of comonads+continuous maps is complete, accessible subcategory cocomplete; introduces "halos" as infinitesimal-neighborhood abstraction; comonad morphisms form a double category. **Directly touches G_M / density-comonad territory** (cf. memory: density-comonads-orthogonal-seed-q5, fibrational-comonoid-layer-is-ss23). Recommend a full read next browse cycle — this could either be a strong neighbour or could anticipate some of the density-comonad/G_M generalization work.

## Emerging directions / hub papers noticed

1. **The Kun Chen ∞-groupoid paper (arXiv, ~2601.22968, Jan 2026)** is the single biggest "check this" item — it's the one place in the citation graph where Gambino-Kock, Ahman-Uustalu, and Spivak-Garner-Fairbanks all converge, generalized one level up (∞-groupoids/Segal spaces). Low risk of scooping (one level up, per the established pattern of "safe neighbours"), but should be read to confirm no Set-level fallout.
2. **Fairbanks-Carlson-Spivak "Comonads as spaces" (July 2026)** is brand new and squarely in comonad/topology territory adjacent to G_M and density comonads — highest-priority unread paper from this session.
3. **Bryce Clarke's ongoing delta-lens program** ("The Grothendieck construction for delta lenses", 2025) is a live thread connecting directed containers / Cat / lenses — worth periodic monitoring given the book already leans on Clarke's PutGet result.
4. **Spivak's "Categories by Kan extension" (2025)** should be checked against the existing spivak-2503-kan-extension-neighbour memory note to confirm it's the same paper or a distinct new one — the title is generic enough that this could be new material for Ch7.
5. **No hit on the cartesian-vs-∏-Mendler classification** anywhere in this pass — reasonable added confidence the crown-tfae-strict-chain result is still original, though Semantic Scholar's search endpoint was heavily rate-limited (HTTP 429) during this session, so the direct-search coverage was thinner than the citation-graph coverage. A follow-up direct-search pass (not just citation-graph) is recommended when the API is less rate-limited.

## Note on API access
The Semantic Scholar `/paper/search` endpoint was rate-limited (HTTP 429) for a significant portion of this session, including on the parallel calls used to look up Papers 2 and 3's arXiv IDs — recovered via retries and by falling back to arXiv abstract pages / web search for identification. The `/citations` endpoint via the research MCP tool worked reliably once calls were serialized instead of parallelized. Recommend serializing (not parallelizing) Semantic Scholar API calls in future browse sessions to avoid the 429s.
