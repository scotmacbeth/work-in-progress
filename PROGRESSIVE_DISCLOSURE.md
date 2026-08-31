# What's In My Projects

> I maintain this file. Update it whenever I produce significant new work.
> Progressive disclosure: Level 0 first, drill into sections when needed.

> **2026-09-09 (DREAM) — THE `◁` GENERALITY QUESTION HAS THE WRONG SHAPE; and two ways distinctions vanish.**
> Consolidation cycle. **Audit first: no registry grade changed and SUMMARY overstated nothing** — every phase had already filed its own result correctly, including PROVE #3 as the `gap3-converse` subtree. Three new crown connections, all ASSOCIATE-phase, none new mathematics.
> **(1) `connections/admissibility-is-the-real-generality-question.md` (★★).** Neil's #1 priority asks "which `C` support the four monoidal structures?" For `⊗` that is graded and real. **For `◁` it is the wrong question, because `◁` mostly does not exist:** on an infinitary-lextensive ccc base, admissibility ⟹ unit connected (Thm B) ⟹ `⟦−⟧` full+faithful (T1) ⟹ left adjoint ∀`q` (Thm 1) — **one bit, and the pole is rigid**; off it `◁` is a **stipulation** and Thm D removes object-injectivity, so left-adjointness is a property of the **choice**. **This explains the anti-diagonal instead of recording it:** a *forced* structure is rigid in one variable, a *chosen* one in the other. Real generality can only live in **Gap 1** (admissible ∧ non-collapse ∧ non-cartesian) — named, empty so far. Novelty gate stays OPEN (DJN `2305.05655` indexed; Carboni–Lack–Walters).
> **(2) `connections/fusion-versus-identification.md` (★★).** **FUSION** = independent conditions coincide *on this base*, escapable by changing base (extensivity; `Fam(Vec^op)` is the instrument). **IDENTIFICATION** = non-isomorphic objects present the same thing, so the question stops referring — **no escape**. My instance is Thm D; the external one is Simon Henry's Cauchy-completeness answer on **MO 365271** (Spivak 2020, community source), which the 09-08 browse flagged as a possible threat to my probes — **resolved as orthogonal, with a reason**: his lives at the bicategory level, mine one level down where `Set`-side `⟦−⟧` is injective on objects. **Diagnostic = T1.** Upgrades the standing "`◁:=⊗` is a definition" caveat from cosmetic to structural. **★ Cycle-2 addition: a THIRD mode, COLLISION** — a *lossy invariant* (cardinality, cohomological degree) agrees across genuinely different structures. Fusion lives in the base, identification in the representation, **collision in my own description**, so it is the mode summaries manufacture. Instances: the `4=4` cardinality that nearly hid the `Vec` left-adjoint failure; the `H¹` degree in (3) below. *Check the map not the count, the axis not the degree.*
> **(3) `connections/total-composition-constructs-partial-composition-lifts.md` (★, `speculative`).** *Total composition CONSTRUCTS by a universal property; partial composition SOLVES A LIFTING PROBLEM, and lifting problems carry cohomology.* Four data points — pushout/structured-cospans (**checked absence** of obstruction language, browse 09-07, `2509.18475`/`2301.01445`), OrgTr `#` total (`2602.17917` Prop 4.3), ZS partial (`[ω]∈H²`), sheaf multi-agent. **Prediction: sheaf gluing carries an obstruction in `H¹`, one degree below ZS — TESTED against the literature in dream cycle 2 and NOT confirmed:** `2606.01663` (deep-read) is **H⁰**; `2605.01879` (deep-read) asserts H¹/H² for plan-gluing but **proves no theorem**; `2605.11204` **Thm 2** is a genuine `H¹` theorem on the **wrong axis** (identifiability, not gluing-existence) — an *invariant collision*. **The remaining work is a `/prove` on my own model, not another browse.** The note also had its provenance corrected (it claimed these were unread; `sources.json` says otherwise — 3rd search-my-own-store incident).
> **(4) Two negatives from opposite directions are one negative.** Browse spent two sessions proving *no cleaner statement of familial representability than Weber Def 5.2 exists* (Fujii–Lack `2507.05529` verbatim, Arkor–McDermott `2404.01281` zero hits, Shapiro `2111.14796` independent apparatus); PROVE independently proved *my probes were never a p.r.a. condition* (wrong adjoint side). Same fact. **Weber trail DROPPED from the browse rotation** after three negative audits; `2305.04042` parked for a `Fam(V)` session.
> **(5) `for-collaborator/2026-09-09-hedges-parallel-program.md`.** Hedges has now paralleled me **four** times (Poly-the-language graded monad ≈ Workers/BHM; System L tensor+sequence ≈ `(⋉,⋊)` duoidal/LDC; additive-lenses CCC ≈ biproduct collapse; applicative transformers ≈ Front B). Front B's thesis one level up. He is the natural first reader for the BHM note; two cheap compare-passes named.
> Journal `memory/dream-journal/2026-09-09.md`; SUMMARY Front A + housekeeping updated; `questions/weber-pra-boundary.md` mostly closed; memory [[admissibility-is-the-real-generality-question-mem]], [[fusion-versus-identification]], [[total-composition-constructs-partial-lifts]]. `trustcheck sources` green (321 sources); all 15 arXiv IDs cited in the new notes verified present in `sources.json`.

> **2026-08-30 (LEAN) — `F_q ⊣ (−)◁q` MACHINE-CHECKED: THE LIBRARY'S FIRST ADJUNCTION.**
> `lean/Containers/Containers/CompLeftAdjoint.lean` (wired into the `Containers.lean` root; `lake build` green, 58 jobs, **0 errors / 0 warnings / 0 sorries**); registry `pra-vs-probe-method.json` child `lean-adjunction` (`attempt`, `lean-verified`, `trustcheck` OK); scratch `scratch/lean-2026-08-30-compleftadjoint.md`; collaborator note `for-collaborator/2026-08-30-lean-comp-left-adjoint.md`; memory [[lean-comp-left-adjoint-triangles]].
> **All of L1–L4 landed on the FIRST build.** `leftAdj`/`leftAdjMap` (+`_id`,`_comp`), `adjUnit`, `adjCounit`, **both triangles** (`triangle_leftAdj`, `triangle_seq`), and the hom-set bijection `Cont(F_q r,p) ≅ Cont(r,p◁q)` as `adjTranspose`/`adjUntranspose` with both round trips. `#print axioms` = **`[Quot.sound]` only** on all six theorems. Unit/counit transcribed verbatim from §4.4 of `2026-08-30-pra-vs-probe-method.md`.
> **(A) VARIANCE CONFIRMED — the reason for formalising.** `F_q`'s action on morphisms runs `⟦q⟧` over the **backward** leg, `Ext.map (φ.onPos ρ) : ⟦q⟧(U'(hρ)) → ⟦q⟧(U ρ)`. The forward reading the object formula `(R, ρ↦⟦q⟧(U_ρ))` invites **does not typecheck at all**. Unlike `WorkersRetract.lean`, the informal proof was **right** — Lean confirmed rather than corrected.
> **(A2) SECOND PASS, same day — NATURALITY (gap closed).** The morning's pass proved the two
> triangles and both round trips, but `adjUnit`/`adjCounit` were only *families* of morphisms:
> naturality was never stated, so `F_q ⊣ L_q` was not certified as an adjunction **of functors**.
> Added to the same file: `whiskerRight_id`/`whiskerRight_comp` (`L_q` functorial — **axiom-free**),
> `adjUnit_naturality`, `adjCounit_naturality`, `adjTranspose_naturality_right`/`_left`
> (`[Quot.sound]` only). Registry child `lean-adjunction-naturality` (`attempt`, `lean-verified`,
> `trustcheck` OK); note `for-robin/2026-08-30-adjunction-naturality-lean.md`; memory
> [[lean-adjunction-naturality-independent-probe]].
>
> **(B2) ★ NATURALITY ⊥ TRIANGLES — INDEPENDENT PROBES.** The perturbed counit
> `ε'_p a = ⟨c a, fun z => ⟨a, !z⟩⟩` that **breaks `triangle_seq`** (find (B) below) still satisfies
> the **naturality square on the nose** — kept as the compiling theorem
> `adjCounitPerturbed_naturality`. Neither condition implies the other; certifying one leaves the
> other free to be wrong. Conversely, perturbing the unit square by `⟨w,z⟩ ↦ ⟨w,!z⟩` makes
> `adjUnit_naturality` fail **on the position leg with the shape leg still `rfl`** — so the squares
> are non-vacuous, and this is the **second independent confirmation** that the content lives in
> POSITIONS and a shape-level argument certifies wrong data just as happily.
>
> **(B) ★ THE FIND — NEGATIVE CONTROL.** Every law is `ContainerMorphism.ext' rfl (fun _ _ => rfl)`: no transport, fibres agree definitionally. To check that is not vacuous I perturbed `ε`'s backward map to inject at a **fixed** position `a₀` instead of at `a`. The **shape leg still passes**; only the **position leg fails**. So the triangles are non-vacuous, and — the transferable part — **the adjunction is a statement about POSITIONS, not shapes**: a shape-level argument certifies the wrong counit just as happily. That is the precise sense in which §4.3's two-line Yoneda proof is under-determined, and it is the warning to carry into any `Fam(C^op)` version.
> **NOT formalised (honest scope):** naturality of `F_q` **in `q`** (Theorem B flags it unchecked — cheap next LEAN target), the `Fam(Vec^op)` version (open), the right adjoint (does not exist for `|T|≥2` — formalising it would formalise a falsehood).
> **Repo note:** LEAN.md pointed at `Composition.lean`, which is **orphaned** (clashes with `Sequential` over `Container.I`). Live `◁` is `Container.seq` (`Sequential.lean`, `G ◁ F` = G outside, matching the paper verbatim); `ε_p ◁ q` is `Container.whiskerRight` (`Monoidal.lean`). `registry_validate` flags one **pre-existing** root-vs-`small-case-sweeps` trust advisory — left alone, `computed` is the honest grade for a script sweep.

> **2026-08-30 (PROVE #3) — GAP 3 CLOSED, AND MY OWN SAME-DAY DICHOTOMY REFUTED.**
> `proofs/2026-08-30-admissibility-and-the-connectedness-converse.md`; registry `left-adjoint-over-vec.json` subtree `gap3-converse` (validates, `proved`); code `scratch/connectedness-converse/verify.py` (5 blocks green); topic `memory/topics/triangle-admissibility.md`; collaborator note `for-collaborator/2026-08-30-admissibility-and-connectedness-converse.md`; memory [[triangle-admissibility-trichotomy]].
> **The question:** is connectedness of `I` **necessary** for `(−)◁q` to have a left adjoint (Gap 3 of PROVE #2), and does the §9bis dichotomy hold?
> **(A) `Set_*` REFUTES the dichotomy.** Pointed sets/smash have a **zero object** (`1_C≅0_C=∗`) so the copower criterion is vacuous — yet `◁` does **not** exist there: `p=⟨S^0∨S^0⟩`, `q=({1,2},(S^0,S^0))` give `⟦p⟧⟦q⟧X=(X∨X)²`, and matching `1+Σ_d((m+1)^{n_d}−1)` forces `b=4` summands at `n_d=2` and **`a=−4`** at `n_d=1`. `Set_*` is on **neither** pole (`S^0` tiny, `S^0∨S^0` not; wedge not disjoint). **`1_C≅0_C` is a symptom of the linear pole, not a characterisation.**
> **(B) THEOREM B — on the extensive pole, admissibility FORCES connectedness.** `C` nontrivial + infinitary lextensive + cartesian closed + `◁`-admissible ⟹ `1=I` **connected** ⟹ (Thm 1) left adjoint for every `q`. **A counterexample to Thm 1's converse cannot even be posed there.** Mechanism: `1≅A⊔B` ⟹ `C ≃ C/A × C/B`, and `[A,T·1]=(T·1₁,1₂)` while copowers of `1` are `(E·1₁,E·1₂)` with **one external `E`** ⟹ `E=1` ⟹ `|T|=1`. Prop 9.1 (`Set×Set`) is now an instance, visible at `p=⟨A⟩`. Ingredient **E1** (lextensive: `1≅1⊔Z` ⟹ `Z≅0`) is pretty and likely folklore — **no priority claimed**.
> **(C) LEMMA D — on the collapse pole the unit is ALWAYS disconnected**, by a chase with **no cardinality argument** (over `𝔽₂` at `dim(1,1)` both sides of `γ` have 4 elements — *second session running where the smallest case is a cardinality collision; BUILD THE MAP*). With Thm 2, Gap 3 closes here too, failing at `|T|=2`. **Bonus:** `κ_{B,Z}` **is `γ` with probe `B`**; connectedness = probe `I`, **fatal probe = `0_C`** — a two-line base-general reproof of Thm 2's necessity, and the house *one-functional-many-probes* method with the probe ranging over `C` itself.
> **(D) THEOREM D — the punchline.** `I` connected ⟹ `⟦−⟧` full+faithful (T1) ⟹ injective on objects up to iso ⟹ `◁` **determined** ⟹ left-adjointness is a property of `C`. `I` disconnected ⟹ `◁` is a **CHOICE** (`Vec_fd`: `({∗},k²)` and `({1,2},k)` both present `X↦X⊕X`, non-isomorphic). **Theorem 1's hypothesis is simultaneously what makes its converse true and what makes its converse MEANINGFUL** — so the `◁:=⊗` caveat can never be discharged, and of PROVE #2's two necessity proofs the **binary-product** one is robust, the terminal-object one is not.
> **TRICHOTOMY replacing §9bis:** extensive pole / collapse pole / **inadmissible** (`Set×Set`, `Set_*`). **Open:** the middle region (admissible, non-collapse, non-cartesian) — lead: `I≅I_1⊔I_2` ⟹ `X≅(X⊗I_1)⊔(X⊗I_2)`, an idempotent-splitting shape; is Lemma S *sufficient*?; **novelty ungated for Thms A/B/D**; and **does DJN `2305.05655`'s indexed formulation dodge Thm B?** — top of the browse list.

> **2026-08-30 (PROVE #2) — THE SUCCESSOR RAN AND CAME BACK AGAINST THE BRIEF ON BOTH COUNTS.**
> `proofs/2026-08-30-left-adjoint-over-vec.md`; registry `left-adjoint-over-vec.json` (validates, `proved`); code `scratch/left-adjoint-vec/verify.py` (8 blocks green); topic `memory/topics/left-adjoint-over-vec.md`; collaborator note `for-collaborator/2026-08-30-left-adjoint-over-vec.md`; memory [[left-adjoint-lhd-gate-is-unit-connectedness]].
> **(1) The predicted summability gate DOES NOT OCCUR.** On the collapse locus (`◁=⊗`) the left adjoint to `(−)◁q` exists **iff `|T|=1`**; the comparison map fails at `dim P_s = 1` with `|T|=2` and `T` **finite**, where the two sides even have **equal cardinality** (4=4 over `F_2`) — `κ` double-counts `0` and misses `e_0+e_1`. *A cardinality-only check would have passed it.* Over `Vec_fd` left-adjointness **strictly implies** the closure/summability condition. **Still three instances of the probe method, not four.**
> **(2) ★ THE `Set` PROOF'S LOAD-BEARING STEP WAS MISIDENTIFIED — BY ME, THIS MORNING.** `(†)` is Set-distributivity as written, but the adjunction never uses it. **Theorem 1:** `I` connected (`C(I,−)` preserves ∐) ⟹ `F_q = Fam(⟦q⟧^op) ⊣ (−)◁q` for **every** `q` over **any** closed symmetric monoidal cocomplete base — four lines, `γ` twice, presentation-independent. `γ` is verbatim T1's map ⟹ **T1 (fullness of `⟦−⟧`) and the `◁`-coclosure are ONE LEMMA APPLIED TWICE.** Extensivity is **not** the invariant on the left: `Set×Set` is lextensive with a **disconnected** unit. Distributivity of `Set` belongs to *constructing* `◁`, not to the adjunction. **Novelty gate OPEN on the general-base form** (the `Set` instance is Meyers/NS Prop 6.57, gate closed).
> **(3) p.r.a. and left-adjointness COME APART off `Set`** — the pre-flagged zero-object caveat fired. `1=⟨0⟩`, `1◁q=(T,0) ≇ 1`; but `Fam/(T,0)≅∏_T Fam`, `(L_q)_1 p=(p⊗Q_t)_t`, left adjoint `∐_t F_{Q_t}` ⟹ **`L_q` is p.r.a. for every `q` over `Vec` too.** This morning's "p.r.a. ⟺ left adjoint" was **base-specific**; the culprit is that **`Set` has no zero object**, and `1◁q` measures the gap exactly. It *strengthens* the crown refutation: p.r.a. discriminates nothing on either base.
> **(4) THE ANTI-DIAGONAL (the surviving crown-shaped fact).** left adjoint: `Set` always / `Vec_fd` iff `|T|=1`; right adjoint (`◁`-closure): `Set` iff `|T|=1` / `Vec_fd` iff `#{t:Q_t≠0}<∞`. **The conditions SWAP SIDES.** In the `(V)⊊(C)⊊(F)` chain, left-adjointness ⟺ **(V)** over `Vec_fd` (bottom rung) and sits above all three over `Set`: **the chain inverts end to end.**
> **(5) Two secondaries.** *The EMPTY product is the binding probe*: for `q=(ℕ,k)` over `Vec_fd`, `L_q` preserves all **binary** products (`ℕ≅ℕ²`) but not the terminal object. *`◁` does NOT exist on `Fam((Set×Set)^op)`* (Prop 9.1): `⟦E,N⟧(1_C)=E·1_C` is diagonal, `⟦p⟧(T·1_C)=(T^A,T^B)` is not — so the intended separator base is unavailable; `Set` and `Vec` pass for **opposite degenerate** reasons (`1_C` a generator vs `1_C=0`). ⚠ scope: my *external* `Fam(C^op)`; DJN `2305.05655` may be indexed — **UNVERIFIED**, browse it.
> **(6) Standing caveat carried:** `◁:=⊗` on the collapse locus is a **definition** (over `Vec`, `⟦−⟧` is not faithful). The binary-product necessity proof is independent of it for finite `T`; the terminal-object one is not.

> **2026-08-30 (WAKE) — Q2 falsifier run: MY OWN CROWN REFUTED, one new `proved` theorem, three attribution corrections against myself, two variance bugs fixed.**
> **(1) `pra-vs-probe-method`, `proved`** — `proofs/2026-08-30-pra-vs-probe-method.md`, registry validates. `1◁q ≅ 1` for every `q` (`y^0` terminal since `∅` is terminal in `Set^op`) ⟹ Weber's p.r.a. slice `Cont/T1 ≅ Cont` collapses ⟹ **p.r.a. ⟺ has an honest LEFT adjoint**, which `(−)◁q` does, unconditionally: `F_q(R,U)=(R,ρ↦⟦q⟧(U_ρ))=Fam(⟦q⟧^op)`. Adjoint **constructed**, so the solution-set gap is never crossed. Sweeps `computed` (35797 hom-cardinality instances, 0 mismatches; 18 equalizer diagrams).
> **(2) ★ THE CROWN RE-FILING IS REFUTED.** "One functional, many probes" is **NOT** Weber-p.r.a.-failure across a slice. Diagnosis = **wrong adjoint side**: p.r.a. is *left*-adjoint existence (unconditional); every probe instance tests *right*-adjoint/closure existence (`|T|=1` over `Set`). The trap was named in the brief **before** dispatch, which is the only reason it was caught. Method survives as mine, `speculative`, 3 instances; **fusion mechanism remains EXTENSIVITY, not p.r.a.** — *amended same day by PROVE #2: extensivity is the right invariant on the RIGHT-adjoint side only; on the left it is unit-connectedness* → `connections/one-representability-functional-two-probes.md` §"Falsifier: RUN".
> **(3) NOVELTY GATE: `F_q` is KNOWN — CITE, DO NOT CLAIM.** Josh Meyers' `◁`-coclosure, **Niu–Spivak Prop 6.57** (`⌜q/p⌝=Σ_i y^{q(p[i])}`, Eq. 6.59 = `F_q` verbatim); also SGF Prop 2.16/Eq. 18, Spivak `2202.00534` §5, LSS Def 2.12. **I already held ≥5 pointers**, including an `equivalence-chain` node reading "NOVELTY: NONE … DO NOT CLAIM". Retrieval failure: I grepped "left adjoint to `(−)◁q`"; it is filed under *coclosure*. → memory [[check-scratch-before-dispatch]] 2nd incident; rule amended to require a **synonym list** before any novelty search. Gate report `scratch/2026-08-30-novelty-gate-left-adjoint-Fq.md`.
> **(4) Pradic–Price attribution CLOSED, against me** — see the reattribution in the PROVE block below. Mine after subtraction: **Cor A′ (Theorem A proves their unproved Remark 16, p. 14)** and **Theorem B (outside their lextensive scope, p. 7)**. ★ Their standing lextensivity hypothesis is **corroboration of the extensivity thesis** — prior work assumes the condition under which the seams fuse, so it cannot see the separation.
> **(5) Weber Q4 ANSWERED NEGATIVE — DIFFERENT AXES.** Non-opfamiliality = failure of the **diagonal** `S→S×S` (`x≠y`), **no coproduct anywhere**; my one-sided BC = `∐∏≠∏∐`. Fourth consecutive "surely these are the same" → no. `scratch/2026-08-30-weber-opfamilial-vs-onesided-bc.md`; `questions/weber-pra-boundary.md` Q4 marked RESOLVED.
> **(6) TWO VARIANCE BUGS FIXED in my own corpus** (both had the coclosure as a *right* adjoint to the *wrong variable*): `proofs/2026-08-27-t4-left-closedness-lhd-famcop.md:51`, `books/category-of-containers.tex:1420` (`q` in the wrong hom slot), plus the same slip in `SUMMARY.md` and in this file at L82. Correct statement: `⌜q/−⌝ ⊣ (−)◁q` — a **LEFT** adjoint to the **same** variable as the closure; the two differ by SIDE, not variable.
> **Triggers seeded:** PROVE = does `(−)◁q` keep its left adjoint over `Fam(Vec^op)`, or does **summability** gate it? (`Set`-distributivity used exactly once, at `(†)`; a 4th crown occurrence and the **first on the left-adjoint side** if it lands; caveat: `Vec` has a **zero object**, so the slice-collapse step may itself fail ⟹ p.r.a. and left-adjointness could come apart off `Set`). LEAN = formalise `F_q ⊣ (−)◁q` (unit/counit/triangles; variance in the backward leg is the point).
>
> **2026-08-30 (PROVE) — sub-Q2 ANSWERED, `proved`: BHM's "`▷` not fibred in its left variable" is NOT my T4-left `◁`-closure obstruction. Over `Set` all conditions coincide (⟺ `|T|=1`); over `Vec_fd` **vertical ⊊ closed ⊊ fibred**, strictly.**
> Proof `proofs/2026-08-30-fibredness-vs-left-closure.md`; registry `fibredness-vs-left-closure.json` (validates, `proved`); code `scratch/fibredness-vs-closure/verify.py` (6 checks green); collaborator note `for-collaborator/2026-08-30-fibredness-vs-left-closure.md`; memory [[bhm-fibredness-vs-t4-left-separable]] upgraded computed→proved.
> **Setting:** shape fibration `π:Fam(C^op)→Set`, `π(S,P)=S`; **(V)** `πL_q≅π`, **(F)** `πL_q≅F_0π`, **(C)** right adjoint to `L_q=(−)◁q`. **Thm A (Set):** `(V)⟺(F)⟺(C)⟺|T|=1`. **Thm B (Vec_fd):** `(F)` always, `(V)⟺|T|=1`, `(C)⟺#{t:Q_t≠0}` finite ⟹ strict chain; witnesses `q=(2,k)` closed-not-vertical and `q=(ℕ,k)` **fibred-not-closed**. Two-sided ⟹ answer NO under **either** reading of "fibred".
> **★ BONUS — REATTRIBUTED 2026-08-30, NOT MINE:** `◁` **IS** fibred in its **RIGHT** variable for every `q`, base functor literally `⟦q⟧` (`π(q◁p)=Σ_t(πp)^{Q_t}`) = **Pradic–Price `2601.15420` Lemma 15** (p. 14, proof p. 31, same base functor); and **both** variables preserve cartesian morphisms **unconditionally** = **Niu–Spivak Prop 6.88** (which PP themselves cite) ⟹ non-fibredness is purely a failure of **base-functoriality**, never of cartesianness. (So `μX.1+q◁X` *is* fibrationally constructible — shapes = W-type `μS.1+⟦q⟧S`; Rem 2.3: BHM's stated reason doesn't block the three fixpoints they list, only their own `T_P(X)=X▷P`.)
> **★ DIAGNOSIS — one test, two probes.** Both conditions = "is `G_r(Z)=Fam(⟨Z⟩◁q,r)` familially representable?" at different `r`. Shape probe `r=(R,0)` ⟹ `G_r(Z)=R^{π(⟨Z⟩◁q)}` (over `Set` this **is** fibredness ⟹ closed⟹fibred conceptually); position probe `r=⟨I⟩` ⟹ summability. **Fibredness = COLLAPSE; closure = collapse + SUMMABILITY in the base.**
> **Two of my own theorems strengthened:** Workers Thm 2 superseded (least-support Lemma 3.4 replaces the counting argument ⟹ covers **all** `|T|≥2` finite *or infinite*, plus `|T|=0`); T4-left Thm 3.1(2) sharpened (`Vec_fd` boundary = "infinitely many **non-zero** positions", not "`T` infinite"). **Method, 3rd occurrence** (after δ≟Φ, T2 A/B): two "canonical-map-iso" conditions constraining different legs of one formula — now a method, not a coincidence.
> **Honesty:** BHM = corroboration only; `◁:=⊗` on the tiny locus is a *definition* (`⟦−⟧` not full over `Vec`) so Thm B is literally about `(−)⊗q`; **attribution gap narrowed not closed** — PP `2601.15420` is `deep-read` in `sources.json` and its framing IS recorded as the fibrewise-op of `cod` (= my `π`), but that read was grep-targeted at derivative/chain-rule and my 07-29 log still lists the identity as OPEN; **cheapest discharge = fetch `2601.15420`, read the "fibred endofunctors" section**. Open: "closed ⟹ fibred" over an arbitrary base. Hostile-referee pass caught a wrong shape action in Lemma 2.1 (`τ∘φ^♯_s`, not the inverse) — found by the explicit-morphism functoriality check.
>
> **2026-08-30 (WAKE) — no new theorem; three consolidation wins.**
> (1) **Sub-Q2 scoped, `computed`, leaning NEGATIVE.** BHM primary source located and now local (`/home/agent/papers/BHM-polylang-ACT2026.pdf`) — a **2-page extended abstract** whose entire claim is ONE unproved parenthetical ⇒ corroboration, not a lemma. Variable alignment confirmed, but non-fibredness = failure of base-functoriality, NOT a missing adjoint; candidate separator over `Fam(Vec_fd^op)` (`T=ℕ`, tiny positions ⇒ fibred, yet T4-left Thm 3.1(2) ⇒ closure fails) gives **fibred ⇏ closed**. Question file `memory/questions/workers-grading-vs-bhm-polynomial-grading.md` §SUB-Q2; memory [[bhm-fibredness-vs-t4-left-separable]]; → `state/PROVE.md`.
> (2) **Peer registry opened for Clio** — `proofs/registry/clio-peer-claims.json` (validates): C4/C5 at `peer-claimed` with PDFs at `peers/clio/proofs/`, her domino/2-quotient reading at `speculative` with her own "I have not run any of (3)" quoted. Her Lyra endorsement recorded *together with its gap* (one leg not reimplemented); her `peer-reviewed` grade NOT inherited.
> (3) **Registry hygiene:** all "source not in index" warnings across every registry now cleared (`sources.json` 310 entries); one invalid `role: lean-verification` fixed to `attempt` in `monad-comonad-transfer.json`. Honest residue: `2006.16236` (Katharopoulos) sits at floor level `agent-summary` with title unrecorded — a flagged debt, not invented data. Three "refutation with no file" warnings remain, pre-existing.
>
> **2026-08-29 (PROVE) — Workers ⊗-grading is a RETRACT of BHM ▷-grading: `proved`. `r∘σ=id` as genuine Poly morphisms; `r∘δ=Δ(d)` = "⊗ is the diagonal collapse of ▷"; `Δ` oplax/lax only on the core groupoid (σ∘Δd is coassociative but not a comonad).**
> Proof `proofs/2026-08-29-workers-retract-of-bhm-grading.md`; registry `workers-retract-of-bhm-grading.json` (validates, `proved`); code `.claude/scratch/verify_retract.py`+`verify_p3.py` (verified n≤3); collaborator note `for-collaborator/2026-08-29-workers-retract-of-bhm-proved.md`; memory [[workers-grading-retract-not-fibre-of-bhm]] upgraded computed→proved. **P2** retract (σ=const-inclusion, r=self-evaluation, `r∘σ=id`, `σ∘r≠id`, idempotent e=σr collapses branch→self-eval). **P3a/b** σ oplax-hexagon + r lax-hexagon (self-evaluation associative) + unit + naturality-under-bijections. **P3c** `r∘δ=Δ(d)` (π₂): store comult is a lift of the ⊗-diagonal along r; off-diagonal `(1−e)δ` = failure of ▷ to be the ⊗-diagonal. **P3d** `σ∘Δd=δ'` coassociative but right-counit FAILS ⟹ not a comonad ⟹ Δ not oplax on full (Set,×), oplax(σ)+lax(r) on core groupoid only; store comonad is internal. Possible LEAN next (finite defeq identities). Prior WAKE entry (retract on shapes only, `computed`) now subsumed.
>
> **2026-08-29 (WAKE) — "Workers = fibre of BHM" conjecture REFUTED (`computed`); it's a RETRACT (⊗≠▷); three graded-monad pictures don't converge to one construction. No new proof — orchestration + one honest self-correction.**
> Inbox empty of unread (everyone quiet; Neil still owes word on T1 flagship + attention note). **Verified the owed Rick support-variety reply was ALREADY SENT 08-26** (mail/sent/20260826_114851) + follow-up 08-27 — dream-journal "owed" list was stale; renamed draft→`SENT-*`, did NOT resend (cross-check-before-outward-action). **Ran the queued `X▷ΔS` check** (compute agent + own hand-calc, agree): `ΔS▷ΔT=8·y⁴` (shapes `|S|·|T|^|S|`) ≠ `ΔS⊗ΔT=Δ(S×T)=4·y⁴` at n=2 ⟹ Workers grades by Dirichlet `⊗`, BHM by composition `▷`, DIFFERENT products; the "Workers=P=ΔS fibre of BHM" conjecture is FALSE. Honest refinement: `Δ(S×T)` is a canonical **retract** (diagonal collapse) of `ΔS▷ΔT` (σ:(s,t)↦(s,const_t), r:(s,g)↦(s,g(s)), r∘σ=id on shapes) — complementary, not subsumed. Working `scratch/2026-08-29-workers-bhm-triangle-vs-dirichlet.md`; updated `connections/workers-grading-is-fibre-of-bhm-polynomial-grading.md` + `questions/workers-grading-vs-bhm-polynomial-grading.md` (RESOLVED sub-Q1) + SUMMARY Workers line + memory [[workers-grading-retract-not-fibre-of-bhm]]. **Sent daily to Neil** (refutation + flag: Snoc/BHM/Workers = three graded-monad pictures on one line but THREE products; asked survey-vs-retract prioritization), CC Robin. **Triggers:** PROVE = the retract as a `Poly`-morphism theorem + grading-compatibility (lax/oplax `S↦ΔS:(Set,×)→(Poly,▷)?`), self-contained no-gate; parked T2=p.r.a. (Weber TAC 18) as browse-gated alt. WRITE = Front-D survey (kept, greenlit). LEAN unset (prove retract on paper first).
>
> **2026-08-28c (PROVE, fallback) — Cont(cod) is a CO-HYPERDOCTRINE: shape Fam-Kan quantifiers + JOINT (shape×position) BC/Frobenius settled ONE-SIDED. `proved`.**
> Proof `proofs/2026-08-28-joint-bc-cont-cod.md`; verification `scratch/verify_joint_bc.py` (exhaustive finite Set, all claims); registry `joint-bc-cont-cod.json` (validator-clean);
> collaborator note `for-collaborator/2026-08-28-joint-bc-cont-cod.md`; memory [[cont-cod-is-a-co-hyperdoctrine]]. Closes the `shape-level-hyperdoctrine` gap of the parent fibration proof.
> ∃_j⊣j^*⊣∀_j exist (Lan/Ran); exchange square = genuine Poly pullback; ∀/E-side co-Frobenius(∧↦∨)+BC HOLD, ∃/A-side FAIL by co-topos non-distributivity (∑∏≠∏∑).
> **★ CORRECTED parent §6.2** in place (co-Frobenius is E=(Σ_!)^op, right adjoint — NOT A). Main PROVE target (T2=p.r.a., Weber TAC 18) untouched: reading gate unmet (browsing off, summary-only source).
>
> **2026-08-28b (WAKE) — δ≟Φ REFUTED (DISTINCT, `computed`); base-category inventory compiled for Neil (UID 134); Robin taught "fibres not sets".**
> Inbox: 4 unread (Neil UID 132/134/135, Robin UID 133). **δ≟Φ explicit-map check** (dream's top move) via agent → verdict **DISTINCT**: Weber's distributivity δ
> tests LEFT positions (=T4-left tininess, `1106.1983`), my T2 Φ tests RIGHT positions/target (=Weber p.r.a., TAC 18 2007); two-way separable over Vec ⟹ the
> conjecture "T2 = Weber-distributivity" is refuted; survivable increment = a two-way RE-FILING (T2 on a SEPARATE familial-functor axis, not the LCCC tower).
> Working `scratch/2026-08-28-delta-vs-phi-check.md`; memory [[weber-delta-vs-t2-phi-distinct]] (both memory systems) + question file RESOLVED + SUMMARY Front D updated.
> **Inventory (Neil UID 134):** `scratch/2026-08-28-base-category-inventory.md` — provenance-tagged master table of bases for `Fam(C^op)` (DJN `2305.05655` = general
> monoidal-V answer; von Glehn fibrational; Shapiro–Spivak finite-limit; Weber/Walker weakening tower; Set^I DPUV; Prof FGHW; my Vec/Set^→; open Rel/R-Mod/Mod).
> Sent to Neil. **Robin (UID 133):** replied with a teaching letter — Day convolution on Set (coend/Lan formula) + the "fibres not sets" bridge (Niu–Spivak Prop 3.79,
> Dirichlet ⊗ = Day; worked micro-example `(y+y²)⊗y³=y³+y⁶`), CC Neil. Morning daily to Neil sent. **Triggers:** WRITE.md = survey (NEW INPUTS section: inventory +
> δ≟Φ re-filing + §5 proved); PROVE.md re-pointed (old cont-cod target now proved) → **T2/Φ = parametric-right-adjointness** (upgrade the re-filing to `proved`),
> fallback = Cont(cod) shape×position joint BC/Frobenius; LEAN unset. No new proof/paper — orchestration + one `computed` resolution + one inventory + teaching.
>
> **2026-08-28 (PROVE) — Cont(cod) is a BIFIBRATION; its quantifiers ARE the A/E liftings; container hyperdoctrine = FIBREWISE OP of Set's (∃↔∀, ∧↔∨, co-topos). `proved`.**
> Proof `proofs/2026-08-28-cont-cod-fibration.md`; registry `cont-cod-predicate-fibration.json` (validator-clean); collaborator note `for-collaborator/2026-08-28-cont-cod-logic-of-containers.md`;
> verification `scratch/verify_cont_cod.py` + `verify_bc_frob.py` (all pass). **Lemma 2.1** (Fam-cartesian ⟺ componentwise p-cartesian, in full) ⟹ Fam preserves (bi)fibrations;
> `cod` opfibration ⟹ `cod^op` fibration ⟹ **`Cont(cod)=Fam(cod^op)` bifibration**; fibre = `∏_s(Set/P_s)^op`. **THE TRAP corrected:** reindexing = `(Σ_ρ)^op` (dualised postcomp), NOT `ρ^*`.
> **Thm 5.1:** along collapse η, `A⊣Δ_c⊣E`, `E=Exists=◁=`cartesian reindexing, `A=All` — the proved UID-94 liftings. **Thm 5.2 (increment):** container hyperdoctrine = fibrewise op of
> Set's; ∃↔∀ roles swapped vs Π/Σ operations; co-topos/subtractive fibre. BC + co-Frobenius dualised. Gaps: shape-level joint BC/Frobenius, truncation preservation. Front D approach-(3) now PROVED.
> Memory [[logic-of-containers-cont-cod-fibration]] updated to proved.
>
> **2026-08-28 (WAKE) — Neil UID-132: survey greenlit + NEW ask "logic of containers"; Cont(cod) verified a fibration; PROVE set; Front D approach-(3) populated.**
> Inbox: one unread — Neil UID-132 reply. (a) Survey greenlit ("do the survey, use Vec as example"); (b) NEW research ask: turn `cod:Set^→→Set`
> into a *logic of containers*, apply Cont to a fibration for `Cont(Set^→)→Cont(Set)`, `Cont C=Fam(C^op)`. Dispatched a research agent (verified
> at computed/folklore): **`Cont=Fam(−^op)` preserves fibrations; `cod` bifibration over Set ⟹ `cod^op` fibration ⟹ `Cont(cod)` IS a fibration**
> (key lemma componentwise cartesian lift, Hermida/Jacobs); fibre over `(S,{P_s})` = `∏_s(Set/P_s)^op` = **proof-relevant predicates on positions**
> (von Glehn fibrewise op); reindexing quantifiers `Σ⊣ρ*⊣Π` = **my proved A/E=∏/Σ liftings** (UID-94) — loop closed. Delta: von Glehn ancestor,
> Aberlé `2604.01303` only gestures (Def 0.4). SENT daily to Neil (full construction + proof-relevant-vs-subobject fork question), CC Robin.
> Orientation `scratch/2026-08-28-logic-of-containers-cod-fibration.md`; memory [[logic-of-containers-cont-cod-fibration]]. **Triggers:** PROVE.md set
> (`cont-cod-predicate-fibration` — rigorous Fam-preserves-fibrations + Beck–Chevalley + Frobenius + dualised first-order structure); WRITE.md
> (survey) kept, approach-(3) fibrational leg now points at the PROVE result; LEAN unset. SUMMARY Front D + Neil line updated. No new proof/paper —
> orchestration + one substantive PI answer + PROVE target set.
>
> **2026-08-27 (WAKE) — Front D Q1 DECIDED (Walker/Vec-subcartesian = NO); Robin taught (Day-lifts); Rick C_{p^n} data; survey trigger set.**
> Inbox: Robin thread UID 127–130 (Day convolution / four-lifts table / Kan extensions — help re-categorify, six confusions,
> RH line) + Rick UID 131 (Ψ⤳Ext census decider + b=4 datum +27; optional C_{p^n} h-data). **Front D research outcome:**
> direct-read of Charles Walker `2607.10242` "Locally Subcartesian Closed Categories" (`/home/agent/papers/walker_lscc.pdf`)
> RESOLVES the dream-journal Q1 — **Vec is NOT locally subcartesian closed (leans NO)**: closure needs genuine right adjoints
> `⊠_p` not unique-if-exists (refutes my "Vec slips through" hunch), pullbacks mandatory so only the TOP adjoint `Δ⊣Π`→`∇⊣⊠`
> weakens, nearest cousin (affine spaces, Rem 4.0.2/fn 15) obstructed by "cross-fiber combinations" = `∐⊊⊕`; Thm 5.2.8 = GK-style
> biequivalence not a recognition criterion. ⟹ the **sharper-negative** discriminator (Vec fails even the affine weakening) →
> EXPOSITION line for the survey, NOT a PROVE target. Updated `questions/vec-subcartesian-closure.md` + SUMMARY Front D.
> **Robin:** sent full teaching letter (Kan = induction, LR rule IS a Kan-extension formula; Day = "multiply-by-inducing"
> `Lan_⊗(F⊠G)`; four-lifts functor category = Schur functors; the hard column = non-cartesian/non-extensive tensor = MY container
> boundary, k[−] = my T3; answered Russell/Set^op≃CABA/F_1-isotropic/RH-line). Note `for-robin/2026-08-27-day-lifts-kan-and-six-confusions.md`.
> **Rick:** computed h=|A\U/B| on C_{p^n} (compute agent, 58/58 brute-force == p^{n−max(a,b)}, `scratch/2026-08-27-cyclic-pgroup-holonomy.py`,
> `computed`) + honest resolution warning (cyclic bed is a total chain ⟹ h collapses to index of larger subgroup, low resolution,
> can't co-vary richly with Schur-rank; steer him to D_8/V_4 antichain lattices). Daily to Neil sent (T4-left + Front-D negative +
> asked survey-vs-prove). Triggers: **WRITE.md = three-(four-)approaches survey** (Neil UID-125 contemplation deliverable, all
> inputs ready); PROVE/LEAN unset (contemplation-first per Neil; survey to surface next PROVE target = Front C or Walker-Q2). No new proof/paper — orchestration + one research decision + teaching.
>
> **2026-08-27 (PROVE) — T4-left DONE, `proved`: `proofs/2026-08-27-t4-left-closedness-lhd-famcop.md`; registry `t4-left-closedness-lhd-famcop.json` (valid).**
> The `◁` LEFT internal hom (= `◁`-closure = **right** adjoint to `(−)◁q`, the one `Cont` LACKS unless `|T|=1`; distinct from the known `◁`-**coclosure** = Meyers / Niu–Spivak Prop 6.57 = `⌜q/−⌝ ⊣ (−)◁q`, a **LEFT** adjoint to the *same* variable, which DOES exist unconditionally. *Variance corrected 2026-08-30 — the two differ by SIDE, not by variable; the old "=DCont" gloss is unverified, do not cite it from here.*)
> EXISTS on `Fam_fin(Vec_fd^op)` — because over a tiny/rigid base `◁` COLLAPSES to `⊗` (Prop 2.1: `[Z,−]` additive ⟹ preserves ∐ ⟹
> `⟦p◁q⟧=⟦p⊗q⟧`; the Vec_fd instance is my proved Prop 4.1), so the left hom = T2's `⊗`-hom `(R^T,(⊕_t M_{ρt}⊗Q_t^*))`. Fails on
> `Fam(Vec_fd^op)`/`Fam(Vec^op)` (T2's conjuncts B/A). **CROWN:** extensivity is OPPOSED to `◁`-closedness — over `Set` the distributive
> law branches (`T^Z` shapes), `◁≠⊗`, closure obstructed (Workers Thm 2); non-extensivity, villain of T1/T2, is the repair. Synthesis of
> 3 proved results; verified 20000/20000 collapse + 3000/3000 adjunction (F_2). For-collaborator + email Neil (UID-125 answered).
>
> **2026-08-27 (WAKE) — Neil UID-125 big steer processed; Front C RESOLVED; three-approaches survey oriented; left-closedness PROVE set.**
> Inbox: Neil UID 124 ("do T2 generally" — already DONE) + **UID 125 (the steer): reframe AWAY from grants ("most knowledgeable
> agent on containers"); wants LEFT-closedness (hint: left Kan preserves representability ⟹ coproducts); introduces THREE approaches
> to containers-over-a-base (Fam(C^op) / indexed Σ-Π-Δ over LCCC / fibrational), Fam(Vec^op) as running example, "few days
> contemplating"; flags enriched-Yoneda; shared `2604.01303`.** Rick UID 122/123/126: F=A·B + density + global-uniform-sign all proved
> his side, §2/§3 accepted, census question (does my h = his (b−1)!! matching count?) — no rush (FPSAC Nov 15). **SENT:** daily to Neil
> (T2 done, fails over BOTH Vecs, three-approaches plan + question-back) + Rick reply (census = right question, honest "no bridge w/o
> Ψ⤳Ext functor", b=2→−3 vs my D₈ deg-0=3 test), both CC Robin, Clio NOT CC'd. **Front C RESOLVED:** research agent extracted De
> Pascalis–Uustalu–Veltrì `2509.25879` (Def 3.3 ICMS + Lem 3.2, NOT "Thm 3.5") — at I=1 `Pe_≡`+`↑` trivialize ⟹ = my `T^Σ_M=M◁−`
> (their I=1 fibre; recognition NOT new maths; DELTA = my branching-chain refines their cartesian/general). Notes
> `connections/my-Mtriangle-is-I1-fibre-of-indexed-icms.md`, memory [[my-Mtriangle-is-I1-fibre-of-indexed-icms]]. **Three-approaches
> ORIENTATION** `scratch/2026-08-27-three-approaches-containers-in-category.md`: discriminator thesis = extensivity+LCCC of base is the
> separating axis; Vec has NEITHER ⟹ only Fam(C^op) reaches Fam(Vec^op) (why Neil says it "needs the first approach"). Aberlé
> `2604.01303` = Poly program-verification (Agda), PARKED as Path-5/6 (its "dependent polynomial" = Hoare decoration, NOT GK dependent
> poly). Triggers: PROVE = `◁` LEFT-closedness on Fam(C^op) (disambiguated from known right-coclosure; via left-Kan/representability;
> Vec test); WRITE/LEAN unset (survey needs more contemplation first per Neil). SUMMARY Front C rewritten + Front D added + Neil line
> updated. No new proof/paper — orchestration + orientation.
>
> **2026-08-26 (PROVE) — T2 DONE, `proved`: `proofs/2026-08-26-t2-day-closedness-famcop.md`; registry `t2-day-closedness-famcop.json` (valid).**
> Closedness of the Dirichlet ⊗ on `Fam(C^op)` ⟺ `Φ(Z)=∏_t∐_r C(M_r,Z⊗Q_t)` **familially representable** (Thm 1.1, elementary
> reduction — def of adjunction + Set-distributivity `∏∐=∐∏` + connectedness of corepresentables; Day LNM 137 Thm 3.3 consistent
> but NOT directly applicable since enriched domain `A=C` is LARGE — the representability refinement is the T2 delta DJN omit).
> Two conjuncts (A) single-factor fam-rep, (B) product-closure `∐_t N_t` exists. Two regimes: **(I) cartesian ⟹ closed free**
> (recovers Poly Dirichlet hom Niu–Spivak Ex 4.78); **(II) dualizable positions ⟹ `(R^T,(∐_t M_{ρt}⊗Q_t^*)_ρ)`**. **Linear
> dichotomy (Thm 3.2, DELIVERABLE):** over Vec single-factor fam-rep ⟺ Q fd (Lem 3.1) ⟹ closed on `Fam_fin(Vec_fd^op)` ONLY;
> **CORRECTS the prediction** — fails over BOTH `Fam(Vec_fd^op)` (∞-shapes break B) and `Fam(Vec^op)` (∞-dim positions break A),
> by dual mechanisms; load-bearing = simultaneous dualizable-and-summable. ⊥ T1 fullness; NOT the `∐⊊⊕` seam (§4). Verified
> 2000/2000 Vec_fd + 2000/2000 Set (`scratch/2026-08-26-t2-closedness-verify.py`). Collaborator note + question-back to Neil:
> `memory/for-collaborator/2026-08-26-t2-closedness-famcop.md`. Gaps: general non-cartesian/non-rigid classification (i), Lem 3.1
> generality (ii), ◁-coclosure untouched (iii). Memory [[t2-day-closedness-famcop]].
>
> **2026-08-31 (WAKE) — Neil greenlit T2 "generally"; Day source CORRECTED (LNM 137 Thm 3.3, not 0705.3485); emails sent; triggers reset.**
> Inbox: Neil (UID 124) "try and do T2 generally" ⟹ T2 (Day-⊗ closedness over `Fam(C^op)`) UNPARKED, sole active PROVE trigger,
> general theorem not Vec-only. Rick (UID 122/123) `F=A·B` + A002620 density now proved his side, confirms my
> cancellation-direction caveat, no rush (FPSAC Nov 15). SENT: morning update to Neil + the owed support-variety reply to
> Rick (PDF attached, CC Robin, Clio correctly NOT CC'd). **Key correction banked:** the checkable Day closedness hypotheses
> live in the **1970 LNM 137 report Theorem 3.3** (`/home/agent/papers/DayReport.pdf`), NOT arXiv `0705.3485` (a contentless
> 3-page summary — my 08-30 dream note had this reversed). Conditions extracted (i base SMC+complete+cocomplete / ii
> representability / iii ends+coends + (⋆)-closedness + Fubini); **named break for compute-first PROVE:** convolution internal
> hom = an INFINITE end `∏_n[X_n,Y_{m+n}]` ⟹ predicted closedness HOLDS over `Fam(Vec^op)`, FAILS over `Fam(Vec_fd^op)`
> (completeness), = the `⊗≠×` seam. Wrote `state/PROVE.md` (T2-general) with Day's conditions + the `Fam(C^op)↔[A,V]`
> translation hazard flagged first; archived stale WRITE.md (support-variety shipped) + copowers PROVE.md (discharged
> `proved` last arc). No new proof/paper this session — planning + orchestration. SUMMARY Front-A/T2 + Neil/Rick
> collaborator lines updated; `questions/open-threads.md` 08-31 block supersedes the 08-30 T2 bullet.
>
> **2026-08-26 (WRITE) — `papers/support-variety-schur-rank.tex` (5pp, compiles clean; provenance clean — my proof notes + Rick email + classical rep-theory refs, no browse-source below deep-read).**
> The cross-collaborator note owed to Rick (his email 2026-08-25, requests 1–3). Makes precise that **his Schur-rank
> dichotomy = my Mackey/Shapiro Ext-support stratification**: rank-1/per-Schur/e₃ᶜ ↔ TRANSVERSE stratum (all
> A∩gBg⁻¹ trivial, Ext in deg 0 only, support V_r(M)∩V_r(N) a point); multi-Schur/Pieri/e₁ᶜ ↔ COINCIDENT stratum
> (higher tower survives, positive-dim support, Benson–Carlson–Rickard locus). Answers request 2 YES with the
> geometric side. **Honesty crux (§3, per WRITE.md guardrail): the STRATA match but "cancellation" names a DIFFERENT
> invariant on each side** — Rick's = top-weight support loss (absent on rank-1 stratum); mine = strict gap
> deg0 > tower = #transverse cosets (present on that same stratum). Tabulated separately; NO bijection claimed.
> Request 3 witness: **D₈, A=B=⟨s⟩** — Ext=[3,2,2,…], deg0=3 > tower=2, one transverse coset, genuinely non-abelian
> (computed 2 ways). Grades honest: dictionary **proved** (`proofs/2026-08-20-emergent-holonomy-is-ext-tower.md`),
> D₈ **computed** (`proofs/2026-08-21-d8-nonabelian-ext-tower.md`), Rick's Ψ-sweeps/EGF cited **as his reported result**.
> Ready-to-send draft reply: `peers/rick/DRAFT-reply-2026-08-26-support-variety-schur-rank.md` (send next email session, CC Robin).
> No functor Ψ⤳Ext claimed; "c ↦ subgroup-move B(c)" flagged heuristic → next prove target. Scratch: `scratch/write-2026-08-26.md`.

> **2026-08-25 (WRITE) — `papers/vec-attention-unification.tex` (8pp, compiles clean, provenance floor deep-read).**
> The attention-unification note from WRITE.md, executed to Neil's DEPTH BAR (UID 121: "if these attention papers
> say nothing deep about LLMs I'm not interested"). Thesis: the SINGLE attention layer is where every categorical
> account agrees (span/Vertechi, endofunctor/O'Neill, Kan-ext/Mahadevan) and where none says anything an engineer
> doesn't know; the uncontested delta is the DEPTH-COMPOSITION LAW none of them supplies. Two bar-clearing facts:
> (i) stacking = free ◁-monoid on `(⋆,AttP)` = tensor algebra `⊕_L AttP^{⊗L}`, with the RESIDUAL connection = the
> algebraic UNIT (degree-0 term); correction to O'Neill (free monad = coproduct `⊕_L F^L`, NOT colimit of bare
> powers); (ii) live depth-L stack degree EXACTLY 3^L ⟹ no collapse to one matrix, with in-context/KV-cache regime
> pinned as the exact ⊙-collapse exception. Prior-art credited: Dorta–Jarvis–Niu 2305.05655 Thm 4.2 (the ◁-monoid/
> enriched-cat machinery is THEIRS; my delta = the attention instance + depth law + degree bound). HONESTY: only
> 3 of the 5 lineages verified at full text (O'Neill/Vertechi/Mahadevan deep-read); Maruyama + Hedges are
> agent-summary ⟹ folded into a "reported, not cited" footnote, NOT the bibliography. Full 5-way unification stated
> as PROPOSAL not theorem. Citations deep-read: 2501.02931, 2603.16123 (Sargsyan softmax-not-functorial),
> 2605.27259 (KET §10.6 representability caveat), 2305.05655, Ahman–Uustalu, my vcont notes + Free.lean.
> Ledger fix: added arXiv-id alias `2501.02931` for the slug-keyed O'Neill entry so citation_check resolves it.
> Scratch `scratch/write-2026-08-25.md`; note `memory/for-robin/2026-08-25-attention-unification-note.md`.
> Sources: `memory/connections/vec-attention-precedents-need-unification.md`, proofs `2026-08-23-oneill-free-monad-linear-container.md` + `2026-08-22-linear-attention-odot-composition.md`.

> **2026-08-25 (PROVE) — FLAGSHIP T1: container extension `⟦−⟧` fully faithful ⟺ monoidal unit CONNECTED; NOT extensivity (Set×Set counterexample).**
> Neil's #1 (UID 120) settled. For closed symmetric monoidal `C` with small coproducts, `⟦−⟧:Fam(C^op)→C\text{-}[C,C]`,
> `⟦S,P⟧=∐_s[P_s,-]`, acts on homs by `∏_s` of the canonical `γ:∐^{Set}_t C(I,X_t)→C(I,∐^C_t X_t)`. **Fully faithful ⟺
> `C(I,-)` preserves small coproducts (unit connected)** (enriched co-Yoneda + Nat-out-of-coproduct, set-level, no
> completeness). **TWO honest corrections:** (1) NOT extensivity — `Set×Set` (l)extensive but not full (unit `(1,1)`
> disconnected; witness 2 container morphisms vs 4 nat transfs); (2) "faithful always" FALSE — Vec not faithful (zero
> collapse). Reconciliation: full-faithfulness (a) = unit-connectedness of the enrichment base vs Diers reconstruction (b)
> = extensivity of codomain Set; fuse at C=Set. Does NOT contradict Gambino–Kock (theirs is fully-internal poly over LCCC;
> mine is mixed `Fam(C^op)`, external `∐`). **T3 (change of base = change of enrichment) PROVED**; **T2 (closedness)
> CONJECTURED w/ gaps.** Verified `F_3`/finite. `proofs/2026-08-25-fullness-unit-connectedness.md`; registry
> `fullness-unit-connectedness.json` (validates, proved); memory `[[fullness-unit-connectedness]]`; for-collaborator note
> to Neil/Robin. Generalizes the Vec instance `2026-08-18-linear-containers-vec.md`.

> **2026-08-26 (PROVE) — the T1 COPOWERS GAP discharged. `proofs/2026-08-26-copowers-gap-writer-monad.md`; registry
> `copowers-gap-writer-monad.json` (validates, proved).** Does `C(I,-)` preserving copowers `κ·I` upgrade to all
> coproducts? **(A) copowers-of-unit ⟺ the copower adjunction's Set-monad is the WRITER MONAD `(-)×End(I)`;**
> `EM=M-Set`, comparison `K:C→M-Set` (points + precomposition), and **(C) all-coproducts ⟺ K preserves coproducts**.
> **Extensive `C` ⟹ (A)⟺(C)⟺ `I` indecomposable & non-initial** — so the one-parameter copower test DECIDES fullness
> over Set, all presheaf/Grothendieck toposes, Set×Set. Additive/thin bases fail (A) already; Day/gluing `Gl((-)²)`
> satisfy both (verified). Residual (Q′) = a non-extensive separator, reduced + obstruction identified (mixed point
> non-lifting through `∐ε`), left OPEN. memory `[[copowers-gap-writer-monad-extensive]]`; for-collaborator note asks
> Neil whether to stop (applications covered) or push (Q′). Parent gap node updated to proved.

> **2026-08-23 (WRITE) — `papers/dcont-constant-tree-fragment.tex` (6pp, compiles clean, provenance floor deep-read).**
> The constant-tree positioning note from WRITE.md. Two Spivak facts (Prop 4.6/Cor 4.8 embedding `Org ↪ OrgTr`
> = constant/time-invariant trees; Prop 4.3 composition `(S,α)#(T,β)=(S×T,α#β)` unconditionally total) + one honest
> negative + my synthesis: (i) directed containers = static-interface corner = constant-tree objects
> (Obs 4.1, MINE); (ii) `[ω]∈H²(Sk_C;𝒟)` is a strictly downstairs invariant of the ZS *welding* `⋈` of comonoids,
> with NO adaptive-level counterpart, because `#` composes 1-cells not objects (Obs 4.3, MINE — resolves the
> apparent tension). Rem 3.17 Zwart–Marsden `u◁u`-monad no-go noted as orthogonal. All 9 prop numbers re-verified
> against the PDF this session. Citations at deep-read: OrgTr 2602.17917, AU 1604.01187, AU-DL, Niu–Spivak;
> Shapiro–Spivak 2205.03906 + Zwart–Marsden ZM19 included ONLY as Spivak's own attributions (framed in-text +
> bib), NOT my paraphrase. Scratch `scratch/write-2026-08-23.md`; note `memory/for-robin/2026-08-23-constant-tree-note.md`.
> Sources: `memory/connections/orgtr-dcont-constant-trees.md`, `memory/questions/orgtr-omega-obstruction.md`.

> **2026-08-27 (WAKE) — OrgTr `[ω]` crown REFUTED (composition total); O'Neill free-monad VERIFIED (linear-F); Rick aligned-regime Ext table computed.**
> Load-bearing close-read of Spivak 2602.17917: OrgTr's `#` composition `(S,α)#(T,β)=(S×T,α#β)` is **Prop 4.3**
> and **unconditionally total** — no matching-pair gate ⟹ **no `[ω]` obstruction lives one level up**; the 08-26
> dream crown is retracted (recorded negative in `memory/questions/orgtr-omega-obstruction.md`). Constant-tree
> embedding DCont↪OrgTr survives (Prop 4.6/Cor 4.8, corrected from a mis-cited 6.10). O'Neill `2501.02931`
> verified full-text ("Self-Attention as a Parametric Endofunctor," C. O'Neill ANU, Jan 2025): stacking = free
> monad (Thm 3.2) on a Para(Vect) endofunctor with params (W_Q,W_K,W_V) — but **LINEAR (deg-1)**; score contraction
> + softmax deferred. ⟹ my degree-3^L is a clean COMPLEMENT; O'Neill has no containers/Poly/◁. Rick's auto-agent
> hallucinated a computation; corrected data = 0 top-weight cancellations b=2,3,4; my sweep (D₈/V₄/V₈, all rows
> LHS-resolution == RHS-Mackey) confirms `(deg-0−Ext¹)=0` in the aligned regime (sharpest D₈ A=B=center [4,4,4,4,4]);
> registry `aligned-regime-sweep` (computed) under `emergent-holonomy-is-ext-tower.json`; table
> `scratch/ext-mackey-general/2026-08-27-aligned-regime-table.md`. Triggers: PROVE = O'Neill-complement
> (linear-container free monad = ◁-monoid, Neil #1 front); WRITE = constant-tree DCont↪OrgTr note; LEAN unset.

> **2026-08-23 (PROVE) — O'Neill's stacked-attention free monad = tensor algebra `T(AttP)` = free ◁-monoid on a linear container; his `colim Fⁿ` CORRECTED.**
> The speculative crown of 2026-08-22 is now a **theorem** (full-text deep-read of O'Neill). `F(W)=AttP⊗W` = extension of the
> one-shape linear container `(⋆,AttP)` over Fam(Vec^op); free monad = free ◁-monoid = **tensor algebra `⊕_L AttP^{⊗L}`**,
> mult = concat = ◁-grafting. **Functorial:** O'Neill's parameter-tensor `Q⊗P` IS the ◁-product `(⋆,Q)◁(⋆,P)=(⋆,Q⊗P)` (currying).
> **Correction:** free monad = Adámek **partial-sum** chain `⊕_n Fⁿ` (series `[3,9,21,45,93,189]`), NOT O'Neill's **bare-power**
> colimit (single term `[3,6,12,24,48,96]`); `F` pointable but NOT well-pointed (Kelly inapplicable); **residual = the unit η**.
> Boundary = degree-3^L (live layer deg 1→3 ≠ degree-1 container). Verify pass caught a RED (wrongly claimed "no natural η").
> GAP: Vertechi unification at computed-level (no re-read in PROVE). `proofs/2026-08-23-oneill-free-monad-linear-container.md`;
> registry `oneill-free-monad-linear-container.json` (validates, proved); `scratch/verify_three_facts.py`;
> for-collaborator `2026-08-23-oneill-free-monad-is-tensor-algebra.md`. Instantiates [[lean-free-monad-unit-laws-done]] in Vec.

> **2026-08-22 (PROVE) — Linear attention = ⊙ in Mat(Vec) EXACTLY at fixed context; strong "stack=one matrix" REFUTED (degree 3^L).**
> Tested Neil's "find a use for VCont" hope that a depth-L linear-attention stack = a single Vec-matrix/iterated ⊙.
> **Refuted for real self-attention:** a live φ=id depth-L stack is homogeneous of degree **exactly 3^L** (Thm D:
> one layer `out_i=(W_V XᵀX W_Kᵀ W_Q)x_i` deg-3, ×3 per layer; measured 3,9,27) — a ⊙-composite is deg-1, so the
> stack is one Vec-matrix only for L=0. **Theorem in the FIXED-CONTEXT/KV-cache regime**, two functors:
> ⊕(contexts, `S(C·C')=S(C)⊕S(C')`, §4 menu = linear-RNN) and ⊙(depths, frozen heads = full sub-bicategory
> of Mat(Vec), §4 pipeline). One head's readout = one ⊙ over the FEATURE index (grounds §3's `b`; reassociation).
> Boundary: softmax NOT ⊙ (non-homog+bounded; Sargsyan 2603.16123 corroborates); nonlinear φ ⟹ ⊙ only in
> feature space. **★★ Speculative crown:** degree-3^L explains why O'Neill `2501.02931` models stacking as a
> **free monad** (non-collapsing tower) not one morphism — needs deep-read of O'Neill. Honest deltas = degree-3^L
> + fixed-context ⊕/⊙ pair (single-layer-as-matrix is Vertechi/O'Neill). `proofs/2026-08-22-linear-attention-odot-composition.md`;
> registry `vec-attention-composition.json` (validates, proved); scripts `.claude/scratch/attn_toy{,2,3}.py`;
> for-collaborator `2026-08-22-linear-attention-odot-degree-3L.md`. Refines [[vec-lax-matrix-crown-resolved]].

> **2026-08-21 (PROVE) — Workers closure column COMPLETED: × CLOSED (conjecture flipped), ◁ obstructed.**
> `Workers_S(a,q)=Cont(ΔS⊗a,q)`. **×-closed** with hom `[p⇒q]_×=∏_{s_p}q◁(y⊕c_{S×P_p s_p})`
> (`⟦⟧Y=∏_{s_p}⟦q⟧(Y+S×P_p s_p)`), via `⟦[ΔS,r]_⊗⟧X=⟦r⟧(S×X)^S` + ⊗-closure + CCC + Yoneda; state
> entangles the curried arg `P_p↦S×P_p` but REPRESENTABLY (old 1296≠256 used wrong candidate q^p).
> **Uniform:** Workers ⊙_⋆-closed iff `S×(A⋆K)` is a functor of `S×A` — ⋆=+ (→×), ⋆=× (→⊗) both hold
> (uses my `2026-07-15-uniform-closure-day-tensors.md`). **◁ NOT closed:** the `(−)◁p` hom is forced
> non-polynomial (`|H([n])|≥2^{2^n}`; R=Id `n^{2^n}`) — **Cont itself lacks a ◁-closure** (only a
> ◁-COclosure), so the obstruction is inherited, not a state effect; single-shape p escapes.
> `proofs/2026-08-21-workers-x-closed-lhd-obstructed.md`; `scratch/workers-type-hierarchy/{xclosed_resolve,lhd_cardinality}.py`;
> registry `workers-type-hierarchy.json` C2/C3 resolved (proved, validates).

> **2026-08-21 (PROVE) — D₈: the FIRST non-abelian Mackey/Shapiro Ext tower, verified.**
> `(⋆) Ext^n_{kD₈}(k[G/A],k[G/B]) = ⊕_{g∈A\G/B} H^n(A∩gBg⁻¹)` confirmed non-abelian by an
> independent minimal free resolution over genuine `k[D₈]` (6/6 cases, deg 0..6; resolutions
> validated exact). **Correction:** the two Klein-four subgroups are both NORMAL ⟹ single coset
> ⟹ `[1,1,1,…]` COLLAPSE — not the intended non-collapse. **Genuine example** `A=B=⟨s⟩` (non-
> normal): `[3,2,2,…]` with `deg-0=h=3 STRICTLY > tower=2` (a transverse meeting drops out above
> degree 0) — the new non-abelian signature; `deg0−Ext¹ = #transverse cosets`.
> `proofs/2026-08-21-d8-nonabelian-ext-tower.md`; engine `scratch/rick-d8-ext/`; registry node
> `d8-nonabelian-crosscheck` (computed, validates); for-collaborator note to Rick; memory
> `[[d8-nonabelian-ext-tower-computed]]`. Refines the degree-0 result below.

> **2026-08-20 (PROVE) — EMERGENT HOLONOMY IS Ext⁰, a degree-0 rank (not a higher class).**
> Proved & 17-case-verified the Mackey/Eckmann–Shapiro/Nakaoka formula
> `Extⁿ_{kG}(k[G/A],k[G/B]) ≅ ⊕_{g∈A\G/B} Hⁿ(A∩gBg⁻¹;k)` (★) — own exact F_p engine
> `scratch/ext-mackey-general/` computes BOTH sides independently (LHS = direct minimal free
> resolution over kG; RHS = Mackey double cosets), agreeing on V₄/S₃/A₄/D₄/S₄ (p=2) and ℤ/3 (p=3).
> **DELTA (the contribution):** (1) `dim Ext⁰_{kU}(k[U/A],k[U/B]) = |A\U/B| = h(s)` — the
> emergent-holonomy count IS Ext, in degree 0. (2) **Concentration (Thm 4):** in the holonomy
> setting Lemma-1 transversality (`A∩uBu⁻¹={e}` ∀u∈U) forces the higher tower to VANISH
> identically — `Ext^*_{kU}=[h,0,0,…]` — so h is the RANK of Ext⁰, not a higher class. (3) CORRECTS
> "higher tower detects alignment": witness W2 (S₄=A₄·⟨(12)⟩, U=S₃, A=A₃, B={e}) has h=2>1 yet tower
> [2,0,0,0]. Resolves Rick's Ext²-bet (void above degree 0). (★) itself is CLASSICAL → its write-up
> routes to `/expository`; the dictionary is the claim. Proof
> `proofs/2026-08-20-emergent-holonomy-is-ext-tower.md`; registry
> `emergent-holonomy-is-ext-tower.json` (proved, validates); for-collaborator note to Rick; memory
> `[[emergent-holonomy-is-ext-degree0]]`.
> **✍ WRITE DONE (2026-08-20):** written up as standalone expository note
> **`expository/emergent-holonomy-is-ext.tex`** (8pp, compiles clean). Route = option (a) of WRITE.md.
> Structure: intro (orchestration → h(s) → "is it cohomological?" → answer: yes but degree 0, tower
> vanishes, corrects the working hypothesis) → prelims (perm modules, group cohomology, exact-fact
> setup, transversality Lemma) → §3 the three classical ingredients assembled into (★) (flagged
> classical, proved-as-assembled) → §4 THE DELTA (Cor: h=dim Ext⁰; Thm: degree-0 concentration; Cor:
> twist-stability) → §5 the 17-case verification table with W1/W2 decisive rows → conclusion
> ("detection is degree 0, nothing deeper to audit"; separates emergent holonomy from the general
> p-divisible-overlap tower). Honesty guardrail respected throughout: (★) NOT claimed new, headline is
> the dictionary + concentration. Citations = Benson + Brown (textbooks) + own internal notes only —
> no browse-agent-summary provenance to verify. Note for Robin in `memory/for-robin/`.
> **✍ EXTENDED (2026-08-20, later WRITE):** added closing **§6 "The full dichotomy:
> `Ext = h·H*(A∩B)` over an abelian group"** (now 10pp, still compiles clean). Writes up the
> non-transverse computation (`scratch/rick-v4-ext-nontransverse/`). Cor: for abelian G,
> `Ext^n ≅ H^n(A∩B)^⊕h`, `h=[G:AB]` — separation of variables (meeting count × overlap-cohomology);
> the degree-0 concentration is the transverse corner `A∩B={e}` (Thm 12 NOT subsumed — needs
> all-conjugates transversality). V₄ table (deg 0–6). Two structural readings (Rick Q1/Q2):
> intrinsically-a-sum over double cosets; support = `V_r(M)∩V_r(N)`, transverse=disjoint points→
> vanish, non-transverse=same point→survive. Support-variety facts (Carlson/Avrunin–Scott/Benson II)
> cited not reproved; abelian factorisation = corollary of classical Mackey, not claimed new.

> **2026-08-20 — LINEAR-CONTAINER FRONT CLOSED (WAKE/scoping).** The sharpened lax/bimodule-◁ crown
> RESOLVED: the genuine algebroid = a monoid (via fibrewise op, comonoid) in the **bicategory of
> Vec-MATRICES** — objects `(S,(P_{a,b})_{S×S})`, matrix composition `(P◁Q)_{ac}=⊕_b P_{ab}⊗Q_{bc}`
> (the `⊕_b` restores the extensivity coproduct `∐⊊⊕`); the strict single-index `◁`
> (`Comon_◁≅Fam(Alg_k^op)`) is its DIAGONAL degeneration. Crown guess "algebroid" RIGHT — needed
> double-indexing. Mathematics CLASSICAL (Bénabou 1967 / Mitchell / arXiv:1704.00329) ⟹ contribution =
> container-theoretic DIAGNOSIS only ⟹ EXPOSITORY not PROVE (WRITE trigger set: closing § of
> `expository/containers-over-vec.tex`). Registry node `lax-matrix-crown-resolved` (computed) in
> `linear-containers-vec.json`. Memory `[[vec-lax-matrix-crown-resolved]]`.
> **✍ WRITE DONE (2026-08-19):** written up as **Part 4 (§sec:algebroid) of
> `expository/containers-over-vec.tex`** (now 22pp, compiles clean). Reframe → matrix comp `⊙` →
> Bénabou/Mitchell (co)monoid=algebroid → diagonal-embedding Prop (single-index = diagonal fragment,
> the container diagnosis) → "single obstruction stated once" (non-extensivity). Also: Prop
> `prop:comonoid` upgraded computed→**proved** (companion `2026-08-19-vec-comonoids-algebras.md`); table,
> open-Q2 ("resolved, then sharpened"), abstract, grant-para updated; boxed provenance caveat in-section.
> Note for Robin in `memory/for-robin/`. ✅ CLEARED FOR CIRCULATION (2026-08-21): direct-read of
> D. Lin "Enriched Polynomial Functors" (AMSI VRS report, supv. Mark Weber — NOT arXiv) = NO SCOOP,
> DISJOINT. Lin's §4 writes the same V-Mat matrix composition `∐_j M(i,j)⊗M(j,k)` + "monad in V-Mat =
> V-category" but explicitly as *well-known classical* Bénabou, over general V (never Vec), monad side
> not comonoid side; contains none of my linear-container / extensivity-obstruction / collapse-to-Id^N
> content. Optional: add one-line Lin citation for the V-Mat observation, but primary cite stays
> Bénabou/Mitchell. Safe to circulate.
> **✍ WRITE DONE (2026-08-21):** two additions to `expository/containers-over-vec.tex`
> (now **27pp**, compiles clean, 0 warnings) per Neil's 08-21 Vec email. (1) NEW §2 "The
> structure of Vec, for the container-minded" — orienting Set/Vec recap (HAS: 0-object,
> biproducts, abelian/KS, self-enrichment; LACKS: extensivity ∐⊊⊕ CLW93, disjoint
> injections, Ω, shape-detecting terminal), no proofs, all forward-pointing. (2) NEW §9
> "Application: handling either prompt is the biproduct" — the ML hook: prompt = one-shape
> linear container ({*},A); **Prop 9.2** coproduct of prompts has extension
> `h_A⊕h_B≅h_{A⊕B}` = corepresentable at the biproduct A⊕B, so *either*=*both*
> (self-duality); proof = existing Lemma h only. Collapse re-read as feature (global Id^N
> vs local either=both, one eqn opposite valuations); tie forward to §8 algebroid (⊕_b
> matrix product = across-prompt composition, k-algebra = within-prompt; biproduct double
> duty). Novelty = framing + either=both reading ONLY (biproduct standard; CLW/Bénabou/
> Mitchell classical); no new arXiv cites. Also: table row, abstract clause, roadmap,
> grant-para. Note `memory/for-robin/2026-08-21-vec-either-prompt-writeup.md`; scratch
> `write-2026-08-21-vec-either-prompt.md`.
> **★ Rick's V₄ Ext¹ test (compute, triple-checked): `dim Ext¹_{kV₄}(k[V₄/A],k[V₄/B])=0` char 2**
> (transverse A≠B ⟹ Res_A N free ⟹ H¹=0; Ext¹(M,M)=2, Hom=1) — NONE of Rick's {1,2,8}. ⟹ emergent
> holonomy `h=|A\U/B|` is NOT dim Ext¹ off-diagonal. Artifacts `scratch/rick-v4-ext/`; emailed Rick.
> Memory `[[rick-v4-ext-vanishes-transverse]]`.
>
> **2026-08-18 — NEW FRONT (Neil steer):** containers over `Fam(Vec^op)`. Orientation +
> biproduct-collapse read in `scratch/vec-containers-orientation.md`; triggers PROVE/WRITE set.
> **★ PROVE DONE (2026-08-18): `proofs/2026-08-18-linear-containers-vec.md`** — Part 1 biproduct
> collapse PROVED (finite linear container `≅ Id^N`, classified by `N=Σ dim P_s`, shapes invisible at
> terminal `⟦S,P⟧(0)=0`, Krull–Schmidt uniqueness); Part 2 the extensivity crux PROVED as
> negative-with-remedy (`Nat = ∏_s ⊕_t Vec(Q_t,P_s)` vs container-hom `∏_s ∐_t`; `⟦−⟧` NOT full; the
> gap `∐ ⊊ ⊕` IS the failure of extensivity — object-collapse and morphism-collapse are one
> phenomenon); Part 3 `◁ = (S×T, P⊗Q)` PROVED. Registry `linear-containers-vec.json` (validated, `proved`).
> Monads/comonads line declared "done". See memory `[[vec-containers-new-front]]`, `[[vec-biproduct-collapse-proved]]`.
>
> **★ PROVE DONE (2026-08-19): `proofs/2026-08-19-vec-comonoids-algebras.md`** — Part 3 comonoid axis
> upgraded COMPUTED→PROVED. `◁`-comonoid in `(Fam(Vec_fd^op),◁,I)` = family `(A_s)` of unital assoc
> k-algebras, one per shape; **`Comon_◁ ≅ Fam(Alg_k^op)`** (cocommutative ↔ `Fam(CAlg_k^op)`). Counit
> forces `δ_shape=diagonal`; position-contravariance ⟹ `δ♯_s=μ_s`, `ε♯_s=η_s`; laws ⟺ unit+assoc.
> Algebroid guess REFUTED in fin-dim (diagonal ⟹ no off-diagonal `P_a⊗P_b` ⟹ disjoint one-object cats).
> Hypotheses sharpened: **f.d. positions only, S arbitrary**. Verify `scratch/vec-comonoids/verify.py`
> (F_2, 4/4, diagonal forced). Registry node `part3-comonoid-algebras` (proved). Memory
> `[[vec-comonoid-algebra-family-proved]]`; collaborator note `for-collaborator/2026-08-19-vec-comonoids-algebras.md`.
>
> **★ SCHUR-COINCIDENCE RESOLVED (2026-08-19, `computed`): `expository/2026-08-19-vec-schur-coincidence.md`.**
> Verdict = PARTIAL MISMATCH, NOT a scoop. My linear containers `⊕_s Vec(P_s,−)≅Id^N` are the FORCED
> homogeneous degree-1 corner of the Schur = polynomial-species world (a Vec-functor is automatically
> additive/degree-1; degree-≥2 Schur `S_λ` aren't even Vec-functors — act as `λ^{|λ|}` on scalars).
> The only degree-1 Schur functor is `S_(1)=Id`, so the Young-diagram classification DEGENERATES to
> "one indecomposable `Id`, functor `Id^N`" = the biproduct collapse. Schur classifies the ANALYTIC
> (tensor) lifting; mine is the additive (Hom) lifting = its `n=1`/`M_1⊗W` truncation. Neither the
> morphism-layer extensivity crux `∐⊊⊕` nor the `◁`-comonoid axis is touched by Schur → crown target's
> classification half DE-RISKED. **Correction banked:** object-collapse needs COCONTINUOUS (Eilenberg–
> Watts), not merely additive/finitary. Settles question `[[vec-schur-coincidence]]`.
> **★ Side track (Rick's line, `computed`): `scratch/rick-ext-check/results.md`.** Verified S₃ (U=C₂,h=2)
> + A₄=V₄·C₃ (U=C₃,h=3); `dim H¹(U;k)=[char∣∣U∣]` ⟹ the emergent-holonomy class is supported exactly at
> primes dividing `|U|` (S₃→char2, A₄→char3, confirms Rick). BUT `h=|U|·dim Ext¹` is TAUTOLOGICAL on
> these A=B={e}, cyclic-U points — a real test of Rick's `Ext¹_{kU}(k[P/A],k[P'/B])` formula needs a
> nontrivial-stabiliser / non-cyclic-U witness + his module-structure spec. Replied to Rick (CC Robin).

## Level 0 — Overview

| Category | Path | What's there |
|----------|------|-------------|
| Proofs | `proofs/` | LaTeX proofs with PDFs — two-atoms ZS, dcont morphisms, ZS criterion, chain rule, monoidal coherence, KS nogo. **★ `2026-07-14-day-family-classification.md` — Cont=Fam(Set^op); Thm A: Day convolution CLASSIFIES the convolutional tensors (literature has existence only); Thm B⁺: the product is the UNIQUE pointwise monoidal structure on Cont; Thm C: the comparitor ⊗→◁ is a coreflection counit**. **★ `2026-07-14-comonoid-layer-over-fibration.md` — answers Neil's task C: "directed container = internal category" is about COMPOSITION not Π (SS23 Rmk 3.16), TRUE but SCOOPED in full; the 7th METHOD-caught reproof**. **★ `2026-07-15-uniform-closure-day-tensors.md` — PROVED both directions: `(Cont,⊙_⋆)` left closed ⟺ `(−)⋆B` polynomial ∀B, with uniform hom `Π_i q(A⋆p[i])`; necessity is one line (closure at `[y^B,y]` = the functor `(−)⋆B`); handedness-fixed; no EM step; unifies Spivak Eqs 38/39/40. Registry `closed-day-structures.json`**. **★ `2026-07-16-free-monad-grafting-laws.md` — the free monad on `(S◁P)` as a ◁-monoid: the three grafting-monoid laws (unit-L/unit-R/assoc) in container coordinates (fwd shapes + bwd positions), the omitted G-K (arXiv:0906.4931 Thm 4.5) "lengthy but routine" checks; Lemmas A (leaf bijection, μ♯ forced) / B / C (graft assoc) / D (split coherence = concat assoc); construction is prior art, only the law-spelling is mine; MONOID MIRROR of M3/M3b comonoid. Registry `free-monad-grafting.json` = **lean-verified** (all 3 laws in `Free.lean`, zero sorry, 2026-07-17).** **★ `2026-07-17-ltimes-rtimes-dialectica.md` — DJN §6's two extra tensors ⋉/⋊ on Cont INTERPRETED (answers their open problem): `(p⋉q)[(s,t)]=p[s]^{S_q}×q[t]^{S_p}`, `(p⋊q)=p[s]^{S_q}×q[t]`; **⋉ = de Paiva's Dialectica tensor** extended off `Hmg(2)≃Dial(Set)` to all of Poly (dir `=X^V×Y^U`), **⋊ = directed variant** (n-fold: ⋉ symmetric = ∏ all-other shape sets, ⋊ triangular = ∏ right-only). Non-convolutional (Thm A can't reach ⇒ 4 canonical+Day DON'T exhaust Cont), non-cocontinuous, **non-closed (first on Cont)**. Target B (closure sub-Q 6.1) reduced+conjectured NO. ⚠️ NOVELTY NOT cleared (no-browse) ⇒ registry `other-cont-monoidal-tensors` = **computed**. Collaborator note + `/lean` target `(Cont,⋉,y)` proposed.** **★ `2026-07-17-bare-dirichlet-comonoid.md` — BARE ⊗-comonoids in Poly (no ◁) = **families of monoids** `Σ_s y^{M_s}`, each `M_s` an *arbitrary* monoid; comult forced diagonal on shapes (× cartesian) + fibrewise binary op on directions, counit=unit, coassoc=assoc, **no cocommutativity**. `Comon(Cont,⊗,y) ≅ Fam(Mon^op)` (cocomm = `Fam(CMon^op)`) — the monoid-enriched upgrade of `Cont≅Fam(Set^op)`; morphisms = fwd reindex + bwd monoid hom per fibre. **Answers Niu–Spivak Ch9 Q5 Poly/⊗ slice (OPEN in the book).** Three-layer table: ◁-comonoid=category, ⊗-comonoid=family of monoids, double=commutative monoids (strictly larger than double; gap = the ◁-side Eckmann–Hilton). Brute-force `scratch/bare-comonoid/` (y^1/2/3, [1,2] all match unfiltered monoid count). **CORRECTS double-comonoid §7's "Spivak owns the ⊗-comonoid classification" — WRONG (Q5 open; Rmk 3.78=⊗-monoids future work; §8.2.4/Prop 8.79=⊗-on-Cat#).** Registry `bare-dirichlet-comonoid` (proved, validates). → LEAN forward dir next.** **★ `2026-07-19-dirichlet-monoid-classification.md` — the DUAL, PROVED: bare ⊗-MONOIDS in Poly = a **monoid `(S,·,e)` on shapes** + an **oplax monoidal functor `P:(S,·,e)→(Set,×,1)`** on fibres (`φ_{s,t}:c[s·t]→c[s]×c[t]`, forced `ε:c[e]→1`; assoc + 2 unit coherences). Shape part of each monoid law ⟹ monoid on S; fibre part ⟹ oplax functor. **§5: NOT a mirror of the comonoid case** — comult maps INTO `S×S` (counit forces diagonal, shapes trivial ⟹ family of monoids), mult maps OUT OF `S×S` (any monoid free ⟹ monoid+oplax); same cartesian fact trivialises one layer, liberates the other. **Thm B: `×`-monoid = SAME theorem, fibre target `(Set,×,1)↦(Set,⊔,∅)` + `c[e]=∅`** (η:1→c forces empty identity fibre; generic containers admit none; all-fibres-empty ⟹ monoids on S; 1,4,33). ⟹ **the whole monoid column is ONE theorem** parameterised by the tensor's fibre monoidal structure. Answers Niu–Spivak **Rmk 3.78** (⊗-monoids = flagged future work); ORTHOGONAL to DUV 2509.25879 (◁-monoids). Two independent enumerations agree (`c6_oplax.py`, `times_monoid.py`). Registry `dirichlet-monoid-classification` = **proved** (validates). → LEAN forward dir (mirror `DirichletComonoid.lean`).** **★ `2026-07-20-ltimes-rtimes-duoidal-ldc.md` — answers PROVE.md LDC question YES and upgrades it: **`(Poly,⋉,⋊,y)` is a NORMAL DUOIDAL category** and `⋉/⋊` carry a **linearly-distributive** structure with distributor `δ:A⋉(B⋊C)→(A⋉B)⋊C` (id-on-shapes; dir=(id,id,**const** `C[c]→C[c]^{S_A}`); genuinely NON-iso ⇒ real LDC). Interchange `ζ:(A⋊B)⋉(C⋊D)→(A⋉C)⋊(B⋉D)` (middle-four swap); `δ`=`ζ` via shared-unit normality. PROOF = the **REINDEXING CALCULUS**: every `⋉/⋊`-composite has dir `∏_i p_i[s_i]^{S(A_i)}`, `A_i⊆atoms`; every structural map (assoc/unit/symmetry/ζ/δ + `⋉/⋊`-images) = id-on-shapes-up-to-`(Set,×)`-coherence + factor-wise precompose with product-projection `S(A_i^src)↠S(A_i^tgt)` (exists iff `A_i^tgt⊆A_i^src`); subsets form a POSET (≤1 arrow) ⇒ ALL duoidal + Cockett–Seely LDC diagrams commute FOR FREE. Also `∂^R` from `⋉`-symmetry. Full container-level Python verify (`scratch/ldc-duoidal/`: δ,ζ natural 729+378, both LDC pentagons, 3×2 & 2×3 interchange-assoc, δ=ζ-induced, normality). Registry node `ltimes-rtimes-duoidal-ldc` = **proved** (validates). ⚠️ NOVELTY UNVERIFIED (no-browse) — (⋉,⋊) analogue of Spivak–Srinivasan 2407.01849's `(⊗_Day,◁)`; `⋊`≠Dialectica par (shapes `S_p×S_q`, not dual) ⇒ fresh pairing, do NOT claim priority. → Cont(C) chapter §, or Lean the reindexing calculus.** **★ `2026-07-21-closure-condition-vacuity.md` — the `condition-vacuity` open node (SEED §6.1): is there a monoidal ⋆ on Set with (−)⋆B non-polynomial ⇒ a non-left-closed convolutional tensor? **NOT resolved but reduced to: does every monoidal Set preserve connected limits in each variable?** No counterexample; the 3 natural candidates KILLED each by a DIFFERENT axiom: **max** (|A⋆B|=max, non-poly) fails BIFUNCTORIALITY (interchange: F(t,i0) both rank≤1 via pinch 1⋆1 and rank 2; not a bifunctor); **support tensor** `A⊔B⊔{• iff both≠∅}` is a bifunctor + cardinality-assoc + pentagon ✓ + triangle ✓ but has **NO natural associator** (exhaustive; fails at empty-slot fill ∅→1 — separator can't record provenance); **Sym²/deg-2 extra** fails ASSOCIATIVITY by growth (deg 4 vs 2). Moral: **polynomiality = provenance-tracking = coherence** (∨_S coherent ⟺ normal form keeps a term per leaf-subset = the exponent). Rigorous tools: **retraction lemma** (any monoidal ⋆ on Set: (u,v)∈(1⋆B)² equalizing into 2⋆B ⇒ u=v; proves injective half of connected-limit preservation, reduces rest to "independence of 1st slot" = OPEN core); **unit-terminal⟹⋆≅×** (A×B natural retract of A⋆B; GAP: retract≠subfunctor, closes via Fox if μ monoidal-natural). Biconditional UNAFFECTED. Registry `closed-day-structures.json` node `condition-vacuity`+5 children (validates). scratch/{max_tensor,witness,support_no_assoc,support_monoidal_full,pullback_lens,vacuity_growth}.py.** **★★ `2026-07-22-vacuity-resolved-collapse-tensor.md` — `condition-vacuity` RESOLVED: **NO, vacuity FAILS.** The **COLLAPSE TENSOR** `A⋆B := B if A=∅ / A if B=∅ / 1 if both≠∅` (unit ∅, symmetric) is a genuine monoidal structure on Set (bifunctor + natural associator + pentagon + triangle + unitors + braiding — emptiness-pattern proof + exhaustive size≤3; the delicate `∅→nonempty` action is where a naive impl & the support tensor break, verified correct myself) with `R_2=(−)⋆2` **NON-polynomial** (`R_2(∅)=∅⋆2=2 > 1=1⋆2=R_2(1)`; `|F(∅)|≤|F(1)|` for poly F; also sends mono `∅↪1` to non-mono `2→1`). ⟹ `⊙_collapse` on Cont is **convolutional but NOT left-closed** (first such): **convolutional ⊋ left-closed**; answers Neil's "lucky with ⊗,×" = YES. Mechanism = **unit-insertion η_B non-injective ('×1 shrinks')**, distinct from support's phantom-separator & orthogonal to the retraction lemma. **The η-cartesian framework LOCATES it: Lemma D (assoc input, balanced⟹`η_{1⋆B}(u)=(1⋆η_B)(u)`, via unit-points p_L,p_R:1→1⋆1) + ★' (structural, balanced⟹independent ⟺ η:Id⇒1⋆(−) cartesian ⟺ ⋆ preserves corner pullback (∅,C)=(1,C)×_(1,1)(∅,1)); monoidal counterexample = Lemma D holds ∧ ★' fails; collapse realises exactly this, support is the mirror (★' holds, Lemma D fails ⟹ not monoidal).** Refined open Q: characterize left-closed convolutional = monoidal ⋆ preserving connected limits in each var (necessary: taut/η injective + ★'). Registry `closed-day-structures.json` node `condition-vacuity`=**proved** (validates). scratch/collapse-tensor/{collapse_hostile2,star_prime_probe}.py, scratch/vacuity2{,b}/.** **★★ `2026-07-23-closed-convolutional-tensors-classification.md` — CLASSIFICATION of left-closed convolutional tensors (the refined target after collapse). Symmetric monoidal `(Set,⋆,I)` with `R_B=(−)⋆B` polynomial ∀B ⟹ (bounded-arity case, PROVED) `⋆≅×` (I=1→`⊗`) or `⋆≅∨_S` (I=∅→`▷_S`; `∨_∅=+→×_Cont`) — the three known closures are the COMPLETE list. (1) **Lemma 1** `|I|≤1` (`R_1(I)=I⋆1=1` + poly normal form; else 1-line unit contra; corroborated by cardinality: no unit≥2 op). (2) **Prop 2** `d(C⋆B)=d(C)d(B)` (`R_B∘R_C≅R_{C⋆B}` + composition arity formula). (3) **Key Lemma** κ=sup arity finite≥2 ⟹ `d(B⋆B)=κ²>κ` contra ⟹ all `R_B` AFFINE. (4) **Reconstruction** affine+unit+symmetry+assoc: symmetry identity `B+D_B X≅X+D_X B` forces `D_X=1+S×X` ⟹ `∨_S` (S unique); I=1 ⟹ `×`. **GAP (honest):** Key Lemma bounded only — `κ²=κ` for infinite cardinals ⟹ infinite/unbounded arities NOT excluded; counting args tautological, real obstruction = associator naturality (support/Sym² deaths); both families κ=1 so families complete, only exhaustiveness conditional. Non-symmetric/one-sided OPEN. Cardinality classification (`scratch/cardinality-classification.py`, SymPy deg 2–4 + brute force): sym/assoc/unital poly ops on ℕ = `x+y+sxy` (unit 0), `xy` (unit 1) ONLY. `scratch/verify_reconstruction.py` all pass. Registry `closed-tensor-classification` (validates, in-progress; gap keeps open). Collaborator note `2026-07-23-closed-tensors-are-times-and-vee-S.md`.** **★ `2026-07-24-arity-gap-further-work.md` — the GAP, sharpened to Further Work (Neil "no moonshots"): now believe it may be FALSE (an infinite-arity closed convolutional tensor could exist). **Lemma A** affine = preserves connected COLIMITS; **Prop B** closure ⟺ preserves connected LIMITS only (via `Cont≅Fam(Set^op)`), independent ⟹ no shortcut, bounded case worked only by `κ²>κ`; **Prop C (key)** the arity recursion `A_{C⋆B,(b,φ)}=Σ A_{C,φ(i)}` is a FIXED POINT at infinite seed `R_2=y+y^λ`→`R_{2⋆2}=y+2^λ·y^λ`, associator natural-in-X ⟹ cardinality/1-var-naturality PROVABLY blind (explains multi-session stuckness); finite seed n≥2 grows n→n²→ (re-derives Key Lemma). Only pentagon/hexagon jointly-in-all-vars left = coherence, not counting. `scratch/arity-gap/recursion_selfconsistency.py`; registry `gap-infinite-arities` stays speculative + 3 proved children. Collaborator note `2026-07-24-arity-gap-why-counting-fails.md`.** **★★ `2026-07-24-free-monad-universal-property.md` — the free-monad UNIVERSAL PROPERTY in container coordinates (Neil's Ch4 milestone-3 gap, grafting note §6 gap #3, CLOSED). `U:Mon(Cont)→Cont` has **left adjoint** `F:X↦m_X`, unit `α_X` = insertion of generators (`α₁ s=nd s(λp.lf)`, `α♯_s:leaves≅P s`). Induced `ĝ:m_X⇒M` by W-type recursion (`ĝ₁ lf=e_M`, `ĝ₁(nd s κ)=μ_M(g₁ s,λq.ĝ₁(κ(g♯_s q)))`, `ĝ♯` via `μ_M♯`). **STRUCTURAL MORAL:** UP of the free monoid reduces by tree-induction to the monoid laws of the TARGET `M` — base(lf)=M-unit, step(nd)=M-assoc, EACH in both fwd(shape)+bwd(position) comps; no law of M re-proved (M given). Mirror of the grafting note (free monoid's own laws↔graft-assoc). Triangle `α;ĝ=g` uses M's **RIGHT**-unit (both comps; compute-confirmed); **uniqueness FORCED by bijectivity of `split`** (Lemma A double duty). Part 2: `⟦−⟧` strong-monoidal+AAG ff ⟹ preserves free monoid; GK 4.5 ⟹ `⟦m_X⟧(A)=μY.(A+⟦X⟧Y)`. Theorem=Gambino–Kock 4.5 prior art; contribution=coordinate proof. Verified `scratch/free_monad_up_verify.py` (Writer ℤ/3, Reader nontrivial-bwd, free m_Y; triangle+MULT fwd/bwd+uniqueness; 306 exhaustive (t,u); neg controls fire). Registry `free-monad-grafting.json` node `free-monad-universal-property`=**proved** (validates). Collaborator note `for-collaborator/2026-07-24-free-monad-universal-property.md`. NEXT=Lean (ĝ as PTree recursor → first end-to-end machine-checked free-monad adjunction incl. UP).** **★★ `2026-07-25-cofree-comonad-universal-property.md` — the COFREE comonad couniversal property in container coordinates (exact DUAL of the free-monad UP; Ch4 cofree milestone). `U:Comon(Cont)→Cont` has **right adjoint** `𝔠:p↦𝔠_p`, counit `ε_p` = read-root (`ε_{p,1}(t)=root t`, `ε_p♯_t(i)=inr(i,inl∗)` the depth-1 vertex). Induced `ĝ:D⇒𝔠_p` by M-**corecursion** (`ĝ₁`=anamorphism of `γ(τ)=(g₁τ,λi.τ↓g♯_τ i)`; `ĝ♯_τ(inl∗)=o_τ`, `ĝ♯_τ(inr(i,w))=g♯_τ(i)⊕ĝ♯_{τ_i}(w)` by **finite path recursion**). **STRUCTURAL MORAL:** couniversal property reduces to the FIVE directed-container laws D1–D5 of the SOURCE `D` — fwd(shape) comps ← D1(base)+D4(step) [Lemma U], bwd(position) comps ← D2(base)+D5(step) [Lemma S], triangle ← D3; uniqueness-fwd = **coinduction** (finality of `tree_p`), uniqueness-bwd = path induction. Free↔cofree duality = **W-type/M-type on shapes, leaves/vertices on positions**; the coinduction is CONFINED to shapes, positions stay finitely inductive BOTH sides (why positions=VERTICES-not-leaves matters — leaves aren't closed under `⊕`). Cor: `⟦𝔠_p⟧(A)=Σ_t(vtx(t)→A)≅νZ.(A×⟦p⟧Z)` = cofree comonad on `⟦p⟧` (direct vertex count + `⟦−⟧` preserves the ω^op connected cofree tower, Ch3). Construction+theorem = Niu–Spivak Prop 8.18/8.33/Thm 8.45 + Spivak 2202.00534 Eq.(244)–(249) (direct-read this session, PRIOR ART cited); contribution = the coordinate proof. Verified `scratch/cofree_up_verify.py` (walking-arrow `D`, nontrivial `g`; corecursion+triangle+Lemma U(20)+Lemma S(70)+comonoid law assembled INDEPENDENTLY via ◁-on-morphisms(22+70)+uniqueness-determinacy(20) to path length 4; 3 neg controls fire). Registry `cofree-comonad.json`=**proved** (validates). Collaborator note `for-collaborator/2026-07-25-cofree-comonad-universal-property.md`. NEXT=Lean (portable backward/position layer now; shape layer awaits M-types/Mathlib `PFunctor.M`).** **★★ `2026-07-25-monad-comonad-transfer.md` — Neil's Ch4 item 2 PROVED: a monad `M` on Set transfers to a comonad `G(S,P)=(S,M∘P)` on Cont; each comonad law, localised at fibre `A=Ps`, IS the correspondingly named monad law (counit-left⟺right-unit, counit-right⟺left-unit, coassoc⟺assoc) — biconditional via the single-shape container `(1,A)`. Fibred mechanism: `G` = pushforward `(M^op)_*` along `Cont→Set` (fibre `(Set^op)^S`); "positions contravariant" = the op turning monad→comonad; dual gives comonad `W`→monad `H(S,P)=(S,W∘P)`. **Neil's why PROVED**: `G(S,P)={M/(S,P)}=Σ_s y^{M(Ps)}` is Meyers' ◁-**left-coclosure** (Niu–Spivak Prop 6.57, formula 6.59) with `M` in the NUMERATOR; universal property `Poly(Gp,r)≅[Set,Set](⟦p⟧,r◁M)` proved by Yoneda (counting-verified); `=Lan_{(S,P)} M` (Trimble Ex 6.63) — exactly Neil's "left Kan extension from the ◁-left-coclosure." Poly descent `⟦G(S,P)⟧(A)=Σ_s(MPs→A)`. NOVELTY CLEARED (absent from Ahman–Uustalu/Purdy–Damato/Niu–Spivak; = fibred-category folklore). Registry `monad-comonad-transfer.json`=**proved** (validates). Compute `scratch/monad-comonad-transfer/check.py`. Collaborator note `for-robin/2026-07-25-monad-comonad-transfer-proved.md`. NEXT=Lean (core, no-Mathlib, mirrors `DirichletComonoid.lean`) + WRITE into Ch4.** **★★ `2026-07-27-monad-comonad-entwining.md` — the TWO FEEDS of one Set-monad `M` ENTWINE (PROVE trigger). `T_M(S,P)=(MS,P⋆)` (A–B 2409.17664 Thm 6.3 shapes→monad, ∏-cointerpretation Mendler algebra `P⋆(m)=∏_{leaf b}P(x_b)`) and `G_M(S,P)=(S,M∘P)` (transfer positions→comonad). The oplax product-comparison `str:M(∏_b Z_b)→∏_b M Z_b` (EVERY functor has it) is the backward map of a **mixed distributive law `λ:T_M G_M⇒G_M T_M`** (STANDARD `TG⇒GT` orientation) — all 4 entwining axioms for every ∏-Mendler `M`: E3=nat(η), E1=`i`=id on singleton ∏, E4=nat(μ), E2=nat(str) w.r.t. product-reindexing (=A–B Def 6.2 `j`-naturality, machine-verified incl. branching `Pf`). `(T_M,G_M,λ)`=entwining ⟹ `G_M` lifts to `T_M`-alg, `T_M` to `G_M`-coalg. `λ`="M oplax-preserves products, on positions"; fibrationally Beck–Chevalley (`G_M`=(M^op)_* vertical, `T_M` covers base monad `M`). **★ PROVE.md's guessed orientation `GT⇒TG` FAILS** on branching `M`: lax `∏M→M∏` breaks T-multiplication; **obstruction = BRANCHING not commutativity** (`Pf` commutative & fails, *union-of-products≠product-of-unions*, witness `X=({a,b},a:2,b:1)`); arity≤1 (`Maybe`,`Writer`) both coincide (str=lax=iso). Deep-read A–B §6 (Def 6.2+Thm 6.3), sources→deep-read. Harness `scratch/monad-comonad-transfer/entwine.py` (forward 12/12 PASS, str non-iso, natural). Registry `monad-comonad-entwining.json`=**proved** (validates). Collaborator note `for-collaborator/2026-07-27-two-feeds-entwine.md`. Gaps: general-`j` chase (mechanical), non-∏ Mendler (open), named Set-descent (open). NEXT=Lean (`str` entwining, extends `MonadComonadTransfer.lean`) or WRITE into Ch4. → [[two-feeds-entwine-one-direction]].** **★★ `2026-07-28-delta-state-object-and-workers.md` — the **category of WORKERS** (Neil's Ch4 07-27 target) PROVED. **T1:** the state object `ΔS=(S,s↦S)` is the **codiscrete category** on `S` under DCont≅Cat (forced directed structure `o_s=s, s↓p=p, p⊕p'=π₂`, D1–D5 ✓); `⟦ΔS⟧=S×(−)^S` = **store/costate comonad** (Uustalu–Vene): `ε(s,v)=v(s)`, `δ(s,v)=(s,λp.(p,v))`. **T2:** `⟦ΔS⟧=S×Reader_S`; the reader `X^S` = position fibre (read-only shadow), the `S×` factor = writeback = Neil's "something more." **T3 (target):** a **Worker** `p→q` with state `S` = container morphism `ΔS⊗p→q` (Dirichlet ⊗); the key **Lemma 3.1** `ΔS⊗ΔT=Δ(S×T)` STRICT (`Δ1=y`) ⟹ composition `w'∘(ΔT⊗w):Δ(S×T)⊗p→r` **MULTIPLIES the context to `S×T`** — exactly Neil's prediction. ⟹ **Workers = category graded by `(Set,×)`** (identity grade 1, composition grade ×, coherence = `(Set,×)` associator/unitors) = **coKleisli of the graded comonad `S↦ΔS⊗−`**. Assoc + unit PROVED in coordinates + exhaustively verified (512+1369 associativity triples, unit laws, 400×256 valid composites). **⊗ forced** (negative control): product tensor gives `ΔS×ΔT` fibres `|S|+|T|≠|S×T|`, state would NOT multiply. **S-varying = Gavranović Para** of the action `S·p=ΔS⊗p`. **GAPS (identifications only, core maths proved):** (1) Para literal only over `Core(Set)` (Δ functorial on bijections only) — graded **computed**; (2) FKM graded-comonad packaging unwritten. Verified `scratch/state-object-delta/{verify,run_tests,stress,negcontrol}.py` all green. Registry `state-object-delta.json`=**proved** (validates). Collaborator note `for-collaborator/2026-07-28-workers-graded-category.md`. NEXT=Lean (Lemma 3.1 defeq-shaped, mirror `MonadComonadTransfer.lean`); Neil Qs (graded-vs-Para statement in Ch4; Core(Set) home?). → [[applications-are-directed-containers]].** **★★ `2026-07-29-effect-coeffect-arrows.md` — Neil's 07-29 steer PROVED. Effect–coeffect **ARROWS** `p⇝q:=Cont(G_M p, T_M q)` (coeffect comonad source / effect monad target) form the **biKleisli category** (id `η^T∘ε`, comp `μ^T∘Tg∘κ_q∘Gf∘δ_p`) **⟺ M is NON-BRANCHING (arity≤1)**. **★ The compositor is NOT the proved entwining `λ:T_MG_M⇒G_MT_M` — it's the REVERSE `κ:G_MT_M⇒T_MG_M`** (lax `∏M→M∏` on positions; "commute `T` out of `G`": `G(Tq)→T(Gq)` is `GT⇒TG`), correcting PROVE.md's orientation guess. **Theorem A:** category ⟺ `G_M` lifts to `Kl(T_M)` ⟺ `κ` mixed-DL axioms E1′–E4′ ⟺ M non-branching; unit laws=E1′/E3′, **associativity=E2′** (the sole branching-obstructed axiom, 07-27). Direct arrow-level confirmation (`bikleisli.py` builds the composite as a real Cont-morphism): **Maybe** category (1536/1536 assoc triples+unit laws+well-typed), **Writer/ℤ₂** category (4608/4608); **Pf NON-ASSOCIATIVE**, explicit witness triple `f,g,h:G(A1)→T(A1)` (differ at shape `b` pos `(1,0)`: `∅` vs `{0}`) — tellingly unit laws still hold, only assoc breaks. **Dichotomy** (the honest "unification"): **arrow/Freyd face** (`κ`, non-branching, biKleisli/Hughes) vs **bialgebra/Turi–Plotkin face** (`λ`, ALL M, `G_M`↑`T_M`-alg + `T_M`↑`G_M`-coalg) — coincide only arity≤1. **Answers Neil's Plotkin–Turi Q: YES for the `λ`-direction (all M); the arrow face is its operational dual, killed by branching.** Neighbour diff-engine: Katsumata–Rivas–Uustalu 1912.13477 (Chu/Day interaction laws, a *pairing* not a compositor). GAPS: E2′ general-`j` chase (inherited, mechanical); full **Arrow** (`first`/premonoidal) needs `T_M` strong+`G_M` costrong on `⊗`/`×` (not checked, next target); `Cont(Set^→)→Set` logic angle open. Registry `effect-coeffect-arrows.json`=**proved** (validates). Collaborator note `for-collaborator/2026-07-29-effect-coeffect-arrows.md`. → [[two-feeds-entwine-one-direction]], [[orchestration-is-zappa-szep-weld]].** **★★ `2026-07-29-effect-coeffect-arrows-first.md` — the arrow's `first`/Freyd interface (route (a), sequel to the morning). With tensor = **cartesian `×`** on Cont, `Arr_M` is a **genuine Hughes arrow / Freyd category** (`arr(φ)=η^T∘φ∘ε` id-on-objects functor; `first(f)=τ∘(f×id)∘σ`) **⟺ M non-branching.** **Lemma 2:** coeffect comonad `G_M` is **always costrong** (`σ_G:G(p×c)→Gp×c` natural ∀M — positions are a single M-structure, `M(inl)`+`η∘inr`, no product-over-leaves). **Lemma 3 (T2 core, CORRECTED):** effect monad `T_M` is a **strong monad for `×` ⟺ M non-branching**; backward = distributivity `∏_b(A_b⊔C)→(∏_b A_b)⊔C`; **Yoneda** forces `d|_{A=∅}=leaf-projection π_i` (verified: exactly 2 nat maps `C²→C`, both proj), then leaf-**transposition** (Pf) or **reindexing** (List) contradicts the fixed `i`. ★ My a-priori "no total strength" was WRONG: total strengths EXIST (priority/leftmost, even passes strength-MULT) but BREAK naturality ⟹ obstruction = **leaf-SYMMETRY**, genuinely DISTINCT from assoc/E2′ (=μ-merging). ⟹ **branching disables the arrow via TWO independent axioms.** Hughes laws L3–L8 exhaustive PASS for `Maybe`+`Writer/ℤ₂` (span affine `MX≅E+A×X`; L5 up to 1024/1024); packaging cites Uustalu–Vene/Power–Robinson/Atkey/JHH. KRU 1912.13477 Thms 1/2/3 (extensive collapse) = same boundary, different engine. Resolves Gap 3 of the morning result. `scratch/monad-comonad-transfer/arrows_first.py`. Registry `effect-coeffect-arrows.json` node `arrow-freyd-costrength`=**proved** (validates). Collaborator note `for-collaborator/2026-07-29-arrows-first-strength.md`. Gaps: symbolic L3–L8 for arbitrary affine M (mechanical); single uniform (⇒) for all branching M (done by 2 symmetry-types). → [[effect-coeffect-arrows-first-strength]], [[three-modes-of-composition-dream]].** **★★ `2026-07-30-affine-classification.md` — FINISHES the arrows result (T1 positive classification + T2 E2′ gap). **T1:** for cartesian M, arrow category exists ⟺ M non-branching ⟺ M≅E+A×(−) ⟺ **M = writer-with-absorbing-exceptions** (A a monoid, E a LEFT A-set; η(x)=(e,x); μ = writer-multiply on A, throw-and-absorb on E, log acts a⊙e∈E) — mode-3 obstruction gets a NAMED positive class. **Two-level monad pin (CORRECTS PROVE.md "A a monoid"):** at *Set-monad* level, monad-on-`E+A×(−)` ⟺ **monoid on N=E⊔A, unit in A, E a two-sided ideal of LEFT ZEROS** (A need NOT be a submonoid — γ:A×A→E+A may ABORT, e.g. nilpotent z²=0, M=1+2X); the *polynomial/cartesian* sub-class (where Ahman–Bauer `T_M` lives) = **non-aborting** = A submonoid + E an A-set. Aborting monoids are valid Set-monads but μ^M DESTROYS a leaf ⟹ non-cartesian ⟹ T_M's μ has no canonical backward map ⟹ outside arrow story. Bijection machine-verified (`affine_classify.py`, EXACT, 0 mismatch, 911250 cands up to |E|=3,|A|=2 & |A|=3). **T2 (E2′ general-`j` CLOSED):** non-branching ⟹ every P⋆ product has ≤1 factor ⟹ κ = id (unary)/η^M (nullary) ⟹ E1′–E4′ all hold, E2′ = associativity of N; the ≥2-leaf union-of-products≠product-of-unions obstruction never forms. Verified `2+3×X`(A=ℤ/3, the |E|≥2,|A|≥2 case) & `1+2×X`(A=ℤ/2): all κ-axioms PASS on U1,A1({a:2,b:1}),A3({a:2,b:2}); biKleisli arrow-assoc 0 violations (15625, 729) — `affine_e2prime.py`. **"Affine" clash flagged:** arity≤1 (M1 unrestricted) ≠ Kock-affine (M1≅1, forces Id). Registry `effect-coeffect-arrows.json` node `affine-classification`=**proved** (validates). Collaborator note `for-collaborator/2026-07-30-affine-classification-and-e2prime.md`. Gaps: line-by-line E1′/E3′/E4′ nullary chase (degenerate, machine-verified not written); Dirichlet-⊗ arrow + Lean of the bijection = next. → [[affine-classification-writer-exceptions]].** **★★ `2026-07-30-workers-type-hierarchy.md` — Neil's 07-30 Q: how far up the type hierarchy do stateful Workers go? **Which of Cont's four monoidal (◁,⊗,×,+) & three closed structures descend to the (Set,×)-graded Workers `Workers_S(p,q)=Cont(ΔS⊗p,q)`.** TWO frameworks: **(A) grade-multiplying/Para** (S-worker ⋆ T-worker → S×T-worker; the native graded-monoidal notion, Φ:Δ(S×T)⊗(p⋆q)→(ΔS⊗p)⋆(ΔT⊗q)) and **(B) shared register** (two S-workers→one S-worker; = A + grade-diagonal + collapse S×S→S). **Framework A — ALL FOUR descend:** ⊗ **STRONG** (PROVED: ⊙=ΔS⊗(−) strong monoidal functor V×C→C via Lem 3.1 ΔS⊗ΔT=Δ(S×T), Φ^⊗ iso); ×,+ **OPLAX** (PROVED: cartesianness of (Set,×)/(Cont,×) resp. cocontinuity of ⊗ + functorial cartesian grade-projections Δ(π)); ◁ **OPLAX** (COMPUTED: interchange verified 256 cases, pentagon unwritten). Interchange of the Para tensor HOLDS 256×4 (checker discriminates: 56/64 non-eq). **Framework B — the tensor SPLITS:** + strict, × oplax-free, but **⊗ and ◁ require a MONOID on the state S** (PROVED for ⊗ via Comon(Cont,⊗)≅Fam(Mon^op) + NO natural monoid — S=∅ has no unit, killer since grade must exist ∀S; |S|≥2 no bijection-fixed element; COMPUTED for ◁ by two-independent-states merge). **Closed — same fault line:** Workers is **⊗-CLOSED**, internal hom = Cont's [p,q]_⊗ (PROVED: state curries PAST ⊗ (sits beside retained arg), counts 256=256, 65536=65536); **×-exponential & ◁-coclosure OBSTRUCTED** (state entangles curried arg, ×-witness 1296≠256; exact open test via ⊗-closure: ×-closed ⟺ ([ΔS,q]_⊗)^p ∈ im[ΔS,−]_⊗). **★ CROWN:** framework B collapse S×S→S needs a monoid IFF the object-tensor MERGES the two operands' positions (⊗,◁ fibre Ba×Dc/nested) vs SEPARATES them (+,× fibre Ba+Dc); same separate-vs-merge dichotomy governs closure. Grant: state-mode obstruction pinned = monoid-on-register (parallel/pipeline) vs free (choice/product); slots into [[three-modes-of-composition-dream]] beside directed=[ω]∈H², effect-coeffect=branching κ/λ. Code `scratch/workers-type-hierarchy/` all green. Registry `workers-type-hierarchy.json`=**proved** (validates). Collaborator note `for-collaborator/2026-07-30-workers-type-hierarchy.md`. Gaps: ◁ framework-A pentagon; ◁ framework-B monoid-suffices converse; ×/◁ non-existence-of-any-hom; Lean A1+C1 (defeq-shaped). NEXT=book Ch4 § + Lean. → [[graded-workers-para]].** **★★ `2026-07-31-branching-commutativity-affine-independence.md` — hardens the standalone paper's "Related conditions" novelty remark to a PROVED Proposition: **P1 non-branching** (`M≅E+A×(−)`, arity≤1), **P2 commutative** (Kock double strength), **P3 affine** (`M1≅1`, Jacobs) are **PAIRWISE logically independent** on Set-monads — all three 2×2 faces realised by explicit machine-verified witnesses ⟹ non-branching is provably NOT a restatement of commutativity/affineness. **Sharper (2 bonuses): Theorem C** = the cube's ONLY hole is `non-branching ∧ affine ⟹ commutative` (M=Id or constant-1), i.e. **non-commutative affine ⟹ branching** (pairwise- but not jointly-independent; the lone implication points the "wrong way"). **Lemma A** = full commutativity criterion for the class: `E+A×X` comm ⟺ `A` comm ∧ `|E|≤1` ∧ trivial action = **THREE independent non-comm sources** (writer / exception "which-error-wins" left-vs-right / nontrivial action); exhaustive sweep all 73 structures |A|≤3,|E|≤2, 0 mismatches. **Load-bearing DONE:** Writer over non-comm `N₃={1,a,b}` non-comm as a monad (`Ψ=(a·b,·)=(a,·) ≠ Φ=(b·a,·)=(b,·)`). ⚠ Banked caution: left-zero band `a*b=a` is non-comm as an *algebra* but its monad IS commutative (**medial**) — monad-non-comm = **medial-law failure**, not `a*b≠b*a`. **Lemma B** = magma witnesses (free magma FFF / free idempotent magma FFT) non-comm via Kock (comm monad ⟹ ops are homs ⟹ binary `*` medial in all algebras) + exhibited finite medial-violating models (2-elt; 3-elt idempotent). Witnesses: Id / Maybe / Writer-N₃(+exc `2+(−)`) / `P⁺`,`𝒟` / `Pf` / idempotent-magma / free-magma. Harnesses `scratch/branching-commutativity/{commutativity,criterion_sweep,magma_search,assemble}.py` all green. Registry `effect-coeffect-arrows.json` node `branching-commutativity-independent`=**proved** (validates). Collaborator note `for-collaborator/2026-07-31-branching-commutativity-affine-independence.md`. NEXT=drop into paper "Related conditions"; LEAN Lemma A or Thm C. → [[branching-commutativity-affine-independent]].** **★★ `2026-07-31-atkey-index-degree.md` — the PROVE.md 'graded Freyd tower' conjecture RESOLVED NEGATIVE: the branching dichotomy is BOOLEAN, not graded. (Cor2.3) index-collapse to a PLAIN Freyd cat = coeffect W=G_M trivial = **M=Id** (Prop2.1), STRICTLY inside non-branching (Maybe/Writer have W≠Id) ⟹ {M=Id}⊊{non-branch}⊊{all}; Atkey's index measures the COEFFECT (M≠Id), orthogonal to & coarser than branching (corrects 'non-branch=index collapse'). (Thm3.1) ARITY GAP: cartesian max-arity∈{≤1,∞}, self-plug n→n²>n, no finite rung≥2 ⟹ dichotomy Boolean bc invariant two-valued. (§4) natural (ℕ,×) leaf-grade destroyed by merging (Pf uniform arrows still non-assoc); ∏-coint ties branching↔merging so Thm A stands. Registry node atkey-index-degree (proved). OPEN: coeffect graded comonad (VPO Gmd, no-browse).** **★★ `2026-08-04-branching-full-morphism-lift.md` — the branching non-associativity UPGRADED computed→proved: the fibre `E2′` failure NECESSARILY LIFTS to a genuine non-associative triple of FULL `Cont`-morphisms. `M=Pf`/`A₁`: `f,g,h` (all fwd `a↦{a},b↦{a,b}`) with `(h⋆g)⋆f ≠ h⋆(g⋆f)`, agreeing on shapes (Lemma F: fwd of ⋆ = relational comp in `Kl(Pf)`, associative) and on every backward entry except `(b,(1,0))`: `∅` vs `{0}`. PROOF = forced finite 5-stage calc (indep. re-derived) + identification (both bracketings pass the SAME overlap `{{a,b},{a}}`, `μ^T` merges leaf `a`; differ only in `κ`/`μ^T` order = the sec2 4-vs-2 gap) + no-downstream-cancellation (transport maps are single-leaf bijections). ⟹ "arrow category ⟺ non-branching" is an iff at the FULL container-morphism level, not merely fibrewise. **Prop 0**: PROVE.md's `M=1+X²` is NOT a cartesian monad (arity gap `2↦4`), corrected to `Pf`; `Reader²` excluded (repeated leaf labels break `μ^T`). Registry node `branching-full-morphism-lift` (proved). → [[atkey-index-degree-negative]], [[effect-coeffect-arrows-first-strength]].** |
| Scratch | `scratch/` | Python computations, counterexample searches, Lean planning notes. **★ `dirichlet_closure_check.py` + `dirichlet-closure-check.md` — the ⊗-closure adjunction on 5197 triples (0 fail), 1,248,025 naturality squares (0 fail), all 3 negative controls caught. ★ `2026-07-14-fibrational-containers-derivation.md` — `Cont(q) := ∫_B q^op` (von Glehn's; derived, then checked before claiming)** |
| Papers | `papers/` | Publication drafts. **★ `which-functors-are-containers.tex` (2026-07-16, 7pp, compiles clean) — book chapter for Neil's uid-63: opens `Cont ≅ Fam(Set^op)`, then the core content — **which functors are containers** (F container ⟺ preserves connected limits [Gambino–Kock; orig. Diers/Carboni–Johnstone]) and **position recovery**. Two surprises: covariant powerset fails by one-line counting; the fibre of `F(2)→F(1)` computes `2^{P(s)}` (POWERSET) not `P(s)` — the honest correction to Neil's guessed formula. §4 products/coproducts Lean-verified (`Cont.lean`); `⟦–⟧` preserves connected limits + (co)products but not coequalisers. All CLASSICAL, no novelty claimed, citation floor deep-read. **REVISED 2026-07-17 (referee pass): fixed a real error — the old "connected not finite" box wrongly said containers preserve the empty limit; they don't (F(1)=S⇏1), the empty diagram is disconnected. Box reframed as "connected = between wide-pullbacks-only and all"; see memory `containers-preserve-connected-not-empty`.** TODO: pin Abbott-thesis coequaliser ref. See `for-robin/2026-07-16-which-functors-are-containers.md` (+07-17 addendum) + `scratch/write-2026-07-17.md`.** Also `four-monoidal-*.tex`, `dcont-cof.tex`. |
| Expository | `expository/` | Write-ups from /expository sessions. **★ `containers-over-vec.tex` (2026-08-18, Schur resolution merged 2026-08-19, 17pp, compiles clean) — the NEW FRONT landscape note: linear containers `Fam(Vec^op)`, extension `⟦S,P⟧W=⊕_s Vec(P_s,W):Vec→Vec`. Headline: `Set` extensive, `Vec` not; the single inclusion `∐⊊⊕` drives BOTH the object-collapse (`⟦S,P⟧≅Id^N`, Thm 4.1, KS uniqueness) and the morphism-collapse (`⟦−⟧` faithful not full, Thm 5.3) as ONE phenomenon. Composition flattens (Prop 6.1); `◁`-comonoid = family of k-algebras NOT algebroid (Prop 6.3, marked `computed`). §7 carry-over table; **NEW §8 "The analytic lifting: Schur functors and the degree-one corner"** — two liftings side by side (additive/Hom deg-1 vs analytic/tensor Schur–species deg-|λ|; `S_λ(λ·id)=λ^|λ|id` ⟹ k-linear-on-homs iff |λ|=1), Prop 8.1 additive lifting = degree-1 slice `M_(1)⊗Id=Id^N`, Ex 8.2 deg-1-vs-2 table (Sym²/Λ² not containers), verdict = NOT a scoop, char-p trap Rem 8.4; §9 honest neighbours ledger (strict-poly-functors own the objects; framing=delta) with boxed provenance caveat (neighbour cites + §8 rep-theory facts NOT deep-read); §10 open Qs. **Cocontinuous fix (2026-08-19):** Rem 4.x — additivity alone ≠ Id^N (`Vec(P,−)` dim∞, `W↦W**`); correct hypothesis = cocontinuous (Eilenberg–Watts), single clean E–W statement. Writes up `proofs/2026-08-18-linear-containers-vec.md` + `expository/2026-08-19-vec-schur-coincidence.md`; note `memory/for-robin/2026-08-19-vec-schur-merge.md`; scratch `write-2026-08-19.md`. Memory: [[vec-biproduct-collapse-proved]], [[vec-containers-new-front]], [[extensivity-is-container-boundary]].** Also **★ `preliminaries-representables-yoneda-day-kan.tex` (VERIFIED+POLISHED 2026-07-16, 12pp, clean) — Chapter 0 "The Machinery": representables/Yoneda, Kan extensions, Day convolution, closed structure. Proves Neil's obs (i) [⟦−⟧=Lan_Y y^(−), free coproduct completion] and obs (ii) [closure DETERMINED on representables by density — NOT transported free: removed a false over-generalisation, added k[−] counterexample; Dirichlet hom of two reps = ∐-of-reps "shapes are morphisms", Niu–Spivak Ex 4.78, not y^{b^a}]. Fixed Day variance/base. NO originality claimed. Deliverable for Neil UID-61 — staged email in for-robin/2026-07-16 (write-session forbids send). See scratch/write-2026-07-16.md + memory strong-monoidal-not-strong-closed.** |
| Lean | `lean/` | Local Lean 4 formalisations. **This is the ONLY copy — there is no upstream repo (see "GitHub" below).** |
| Memory | `memory/` | Dream journal, connections, reading logs, topics, for-collaborator notes |
| Code | `code/` | Trust registry tools (trustcheck.py, macbeth.json) |
| Peers | `peers/` | Peer claims from Clio and Rick |
| For Alastair | `for-alastair/` | Materials prepared for Alastair Poole |

## Level 1 — Memory

- `memory/SUMMARY.md` — top-level summary (dream cycle keeps this current)
- `memory/dream-journal/` — 5 entries (2026-06-09 … 2026-06-12, 2026-07-14)
- `memory/connections/` — 7 cross-domain isomorphisms (cofunctors=update-lenses, duplicate=futures-with-provenance,
  g-obstruction=baues-wirsching, orgtr-dcont-constant-trees, two-atoms-ZS-decomposition,
  **comparitor-points-the-wrong-way**, **circular-verification-and-reading-depth**)
- `memory/topics/` — distributive-law-landscape, equivalence-chain, **monoidal-structures-on-cont**
- `memory/reading/` — daily browse logs, feeds, citation-ready notes
- **`memory/reading/poly-book-index/`** (2026-07-14) — **★ the antidote to the reproof pattern.** A
  greppable, page- and equation-numbered index of every definition, proposition and **exercise** in
  Niu–Spivak *Polynomial Functors*: `ch1-3.md` (done), `ch4-5.md`, `ch6-end.md` (in progress).
  **Grep this — and `memory/` + `scratch/` — BEFORE claiming novelty.** Half my "theorems" were
  exercises in a book I already owned.
- `memory/reading/2026-07-14-fibrational-containers.md` — browse log: `Cont(q) := ∫_B q^op`; **von
  Glehn TAC 33 (2018) no. 36 owns it in full** (§4.1 literally says "the category of containers");
  Streicher 1801.02927 Ch. 5 (the naive dual has the wrong base); Spivak 1908.02202 Ex. 3.5 (the
  fibration → bifibration → trifibration ladder). **⛔ THE COMONOID LAYER IS NOT OPEN — RESOLVED &
  SCOOPED 2026-07-14: Shapiro–Spivak arXiv:2305.00167 (Thm 5.6 / Cor 5.12 / Rmk 3.16). See
  `proofs/2026-07-14-comonoid-layer-over-fibration.md`. Only the ∞-version (Chen Conj 7.2) is open.**
- `memory/for-collaborator/` — 19 notes for Robin/Neil (Lean milestones, paper results, discoveries)
- `memory/for-robin/` — chain rule section
- `memory/questions/` — open threads

## Level 1 — Key Proofs

- **★★ `2026-08-05-cartesian-preservation-nonbranching.md` + `2026-08-05-crown-gap-closure.md` — the
  fibrational "crown TFAE" is FALSE: a STRICT 4-level chain `writer A×(−) ⊊ writer+exc E+A×(−) =
  non-branching ⊊ cartesian ⊊ polynomial/∏-Mendler`, only `(4)⟺(5)` a biconditional. Splitters
  List/Maybe/Pf/Reader. **Gap-closure (hb3) PROVES both former-computed joints:** (1)⟺(2) within
  ∏-Mendler via Lemma 1.1 `T_M(u,f)` backward `=(∏f)∘(u_*)^*` bijective ⟺ leaf-tracking `u_*` bijective
  (the `T_M`-shadow of Lean `onMor_cartesian`) + `κ_μ` bijective (surj=support/parametricity, inj=cartFun
  label-freeness); Reader=general (1)≠(2) split (polynomial functor, non-cartesian μ, no `i_P`). (3)⟹(5)
  all arities via `str` image shape-correlation ⟹ non-surjective at `|M1|≥2`, `|M1|≥2` automatic from
  unary unit. Registry `effect-coeffect-arrows.json` nodes `crown-boundary-table` +
  `lambda-inv-implies-nonbranching-general` = **proved**. **hb4 adversarial re-audit (§7): found+closed a
  gap in Thm 1's Lemma 1.4** — `cartFun⟹polynomial` is FALSE (witness `Bag`=multisets: cartFun ∧ leaf-cartMu
  but NOT a cartesian monad — fails connected pullback `{a,a'}→z₀←{b,b'}`, 10↛9); rescued by **Lemma 1.4′
  (label-rigidity)**: ∏-Mendler forbids label-fixing leaf symmetry ⟹ cartFun⟺polynomial. `Bag` = the
  analytic level OUTSIDE ∏-Mendler, opposite `Reader`. Conclusion unchanged; scripts `bag_probe.py`,
  `bag_pimendler_obstruction.py`.**
- **★★ `2026-08-06-state-reader-ladder-census.md` — REFUTES the state-monad census.** Reader `X^E`/State
  `(S×X)^S` are **NOT ∏-Mendler**: `T_M` has a unit but **no multiplication** — the mult laxator
  `j:P^⋆(μ mm)→(P^⋆)^⋆(mm)` is (by **Yoneda**, Lemma 1) a reindexing along a **total** label-preserving
  `κ_μ:I(mm)→lv(μ mm)`, and Reader's diagonal μ / State's threading **DROP** off-diagonal inner leaves
  (labels absent from `μ mm`) ⟹ `κ_μ` non-total ⟹ no `j`. The compute pass's `δ:E→E×E` "single-valued
  i_P" was the **wrong-variance section** of `κ_μ`. **`cartesian ⊊ ∏-Mendler` keeps witness `Pf`** (merge:
  `κ_μ` total, non-injective), NOT Reader/State. **Corrected crown Lemma 1.3:** a natural UNIT laxator
  `i_P` DOES exist — the gate is `j`. **Boundary = TRICHOTOMY of non-cartesian μ:** MERGE (`Pf`, inside) /
  DROP (`Reader,State`, outside) / SYMMETRY (`Bag`, outside). Registry node `state-reader-outside-pi-mendler`
  = **proved**; crown notes + node `crown-boundary-table` corrected. Script `pi-mendler-boundary/kappa_test.py`.**
- **★★ `2026-08-07-proof-relevance-boundary.md` — the PROOF-RELEVANCE boundary (answers Neil UID-91).**
  Reader/State **have** the `□` predicate MONAD lifting `M̂(X,P)=(MX,∀leaf.P)` on `Sub(Set)` but **not** the
  proof-relevant `∏` `T_M`-monad. Two liftings = two opposite total-directions of the same label-matching
  `R⊆I(mm)×lv(μ mm)`: `∏`⟺**forward**-total (Yoneda), `□`⟺**reverse**-total (proved general by single test
  predicate `P₀=Lab(I(mm))`). Reader (diag) / State (thread) are reverse-total for EVERY mm (each surviving
  leaf IS a token) but forward fails ⟹ **boundary = proof-relevance** (data sourced at codomain vs entailment
  discharged at conclusion). **★★ ℤ/2 grading fell out** (`fourfold.py`): `direction=(is-limit) XOR
  (is-proof-relevant)`, `{∏,◇}`→fwd `{Σ,□}`→rev ⟹ Reader/State DO admit a proof-rel lifting — the
  `Σ`-container one, not `∏`. Node `proof-relevance-boundary`=**proved** under `state-reader-outside-pi-mendler`.
- **★★ `2026-08-07-sigma-monad-proved.md` — the Σ side, PROVED a genuine monad for Reader (all E) + State (all St).**
  Multiplication = reindex along the section `σ` (Reader diagonal, State threading); unit = codiagonal fold.
  **Reduction lemma (dual of the ∏-census Yoneda reduction):** every backward position map is a
  coproduct-pushforward `Σ_α` along a label-preserving index function, and `Σ` is FAITHFUL (test at the
  constant singleton family `P≡1`) ⟹ **each monad law ⟺ ONE index-function identity**; forward parts are
  `M`'s own unit/assoc. Content = three backward identities **(U1)** `inner(σ(η_{MS}m,L))=L`, **(U2)**
  `outer(σ(M(η)m,L))=L`, **(A)** section pentagon. Reader: const diagonal ⟹ U1,U2 free, diag∘diag=triple ⟹ A.
  State: outer always `=L` ⟹ U2, η-next-state=id ⟹ U1, threading-assoc = State μ-assoc ⟹ A. Verified
  exhaustively (State St=2: all 16384 depth-3 nestings). **HONEST:** general "reverse-total ⟹ Σ-monad" NOT
  proved — reverse-total gives σ pointwise (mult defined) but (U1,U2,A) coherence is strictly stronger;
  Reader/State supply it canonically (Thm 3.1 = Σ-monad iff shape-natural section satisfying U1,U2,A; open
  child `reverse-total-implies-coherent-section-OPEN`). Node `sigma-monad-reader-state-proved`=**proved**.
  **★★ [lean-verified 2026-08-08] Reader Σ side** — `ReaderStateOutsidePiMendler.lean` §§7–8: `RSig/RSigSig/
  RSig3` position functors (general `S,P : Type u`, realising Cor 2.3's "all `C`"), backward maps `rEtaBwd`
  (fold)/`rMuBwd` (diagonal σ), lifted `etaSigTC/TetaSig/muSigTC/TmuSig`; laws `reader_sigma_left_unit`(U1)/
  `_right_unit`(U2)/`_assoc`(A) all `rfl`, bundle `reader_sigma_monad_lifting`, payoff
  `reader_proof_relevance_triptych` (∏✗/□✓/Σ✓ at same Reader). **Axiom-free**, zero warnings.
  **★★ [lean-verified 2026-08-08] State Σ side — TRIPTYCH COMPLETE** — same file §§9–10: `StateSigma/
  StateSigma2/StateSigma3`, backward maps `sEtaBwd/sMuBwd/etaSigTCState/TetaSigState/muSigTCState/TmuSigState`,
  collapses `sDd/sEe/sDdiag`; laws `state_sigma_left_unit`(U1)/`_right_unit`(U2)/`_assoc`(A) all `rfl` (threaded
  section `σ(mm,s)=(s,(mm s).1)` reduces through pair projections; key defeq `sMu(sDd)≡sMu(sEe)` = State
  μ-assoc), bundle `state_sigma_monad_lifting`, payoff `state_proof_relevance_triptych`. **Axiom-free**, zero
  warnings. Registry `sigma-monad-reader-state-proved` + both coherence premises now `lean-verified`. Only
  general `T^Σ_M=M◁−`/Thm 3.1 still paper-only. Collaborator note
  `memory/for-collaborator/2026-08-08-lean-state-sigma-monad.md`.
- **★★ `2026-08-08-sigma-monad-is-triangle-monoid.md` — the Σ-lifting IS `M ◁ −`; `reverse-total ⟹ Σ-monad` REFUTED.**
  `T^Σ_M(C)=M◁C` (Prop 2.1: shapes `MS`, positions `∐_{lv}P` = composite-polynomial positions; `η^Σ=η_M◁-`,
  `μ^Σ=μ_M◁-`). **Thm 3.1: `T^Σ_M` monad ⟺ `M` a ◁-monoid in `Cont` (container monad) ⟺ `M` a Set-monad with
  polynomial structure** (via `Cont≃Poly↪[Set,Set]` ff strong-monoidal). The section `σ` = `μ_M`'s backward map;
  (U1,U2,A) = the ◁-monoid laws on positions → automatic; recovers 08-07 Reader/State as the ◁-monoid special
  case. **Refutation:** `Bag` (finite multiset) is leaf-supported + reverse-total (`μ`=leaf-bijection, `σ=id`)
  but NOT a container (fails connected pullback `A→1←B`: `|Bag(2×2)|₂=10≠9`, witness `{(0,0),(1,1)}`≠`{(0,1),(1,0)}`
  same `(π_A,π_B)`), so `T^Σ_Bag` isn't even a functor on `Cont`. Real content over reverse-total = ◁-monoid
  structure = polynomial-not-analytic. Verified `scratch/sigma-monad-coherence/bag_not_container.py` (List, a
  container, passes the same test). Node `reverse-total-implies-coherent-section-REFUTED`=**proved**, registry valid.
  Collaborator note `memory/for-collaborator/2026-08-08-sigma-monad-is-triangle-monoid.md`.
- **★★ `2026-08-08-A-E-predicate-liftings.md` — Neil UID-94: `All`/`Exists`=`∏`/`Σ`, `E=◁`; both flags proved.**
  **(P1)** `A=All=T_M` functorial in 1st arg ⟺ CARTESIAN: Yoneda Lemma 1 `Nat(∏_{p'}B(φp'),∏_p B(p))≅∏_p φ⁻¹(p)`
  = sections of the backward `φ`; non-surjective⟹NONE (the "A not on all polynomial functors" flag), bijective⟹
  unique canonical `φ⁻¹`. `E=Σ` pushes fwd covariantly (no section) ⟹ `E=◁` a bifunctor, `A` not. **= `T_M`-lifts-
  ⟺-`M`-cartesian one level down (α=μ_M).** 2nd-arg functorial ∀ morphisms (ρ pointwise inside factors).
  **(P2)** `A X(A Y C)=A(E X Y)C=A(X◁Y)C` STRICT: positions Fubini `∏_p∏_q=∏_{(p,q)}`, shapes AC+currying, unit
  `A y C=C` ⟹ **`A`= LEFT action/left module of `(Cont,◁,y)=(Cont,E,1)`** (functorial on `Cont_cart`). Dual
  `E X(EYC)=E(◁)C`=◁-assoc. Strict & base-monad-free; **Orestis oplax `Λ-join⊆`** = the base-monad-`join` layer
  (`=`→`⊆`, back to `=` iff base μ cartesian). **(P3)** mixed `A X(EYC)` vs `E(AXY)C` NOT strict; iso **iff `X`
  LINEAR (|P_X s|=1 ∀s)** — finer than non-branching (≤1); empty shape breaks it (`Σ_∅=0≠1=Π_∅`). Verified
  `scratch/prove-A-E-verify.py` (all pass). Node `neil-A-E-predicate-liftings`=**proved**, registry valid.
  Gaps: Lean action-law rung + module coherence 2-cells. Collaborator note
  `memory/for-collaborator/2026-08-08-A-E-predicate-liftings.md`. Feeds greenlit book note.
- **★★ `2026-08-09-reader-liftings-are-categories.md` — Reader's proof-relevant monad liftings ARE SMALL CATEGORIES; ∏/Σ/mix REFUTED (7th instance).**
  Resolves PROVE.md `pi-sigma-dichotomy-exhaustive`. **Thm:** fibred proof-relevant POLYNOMIAL monad liftings of
  Reader `y^E` along the shape fibration ≅ **`E`-indexed families of small categories** `(C_v)_v`, via
  `L(B)=⊔_v⊔_{i∈Ob C_v}B_v^{C_v(i,→)}`, ε=identities, δ=composition (= `E`-indexed polynomial COMONADS = cats,
  one level down; monad-on-Cont ⟷ comonad-per-leaf-on-Set via fibrewise op). Proof: reduction (liftings ↔
  `(L,ε,δ)`+3 laws via generic cartesian) → δ⟹inner shapes pure (∏ has none ⟹ NO δ) → unit laws ⟹ every shape
  pure/single-leaf → pure-leaf part = poly comonad = category (AHU/Cat#). **∏ EXCLUDED** (R non-cartesian);
  **Σ_U=discrete cats**; **ℤ/2 groupoid** (`B_0²` swap)=genuine non-∏/non-Σ; **analytic killed by counit**
  (Sym²,Bag no ε — polynomial IS the boundary, 7-for-7). Verified TWICE independently: enum (monad laws) vs
  catcount (cat axioms) agree — `[2]→4=#Mon(2)`,`[2,1]→6`,`∏→0`,impure→0. `scratch/dichotomy-exhaustiveness/`.
  Node `reader-liftings-are-categories`=**proved**, registry valid. Gaps: `L polynomial` hypothesis; State +
  general-M ("categories fibred over M"). Collaborator note `memory/for-collaborator/2026-08-09-reader-liftings-are-categories.md`.
- **★★ `2026-08-10-state-liftings-holonomy-free.md` — State liftings are HOLONOMY-FREE; the grading COLLAPSES (8th
  instance, sign flipped: coarser not finer).** Resolves the State frontier of `state-general-M-reduction`. `𝕊` :=
  action category of the transformation monoid `S^S↷S` (transitive ⟹ connected ⟹ `π_0=1`). **PROVED (|S|=2, poly):**
  reduction (Prop A′), counit-on-`A_id`, threading `σ(s)=t_s(T(s))`=𝕊-composition, purity forced (inner=naturality,
  full=left-unit). **SOUNDNESS (constructed+machine-verified):** `Cat ↪ liftings` — `𝕊×C` is a lifting for EVERY
  small category `C` (all 3 monad laws via genuine finite-`Cont`-morphism engine `honest.py` + cross-validated
  sampling-assoc `lean_assoc.py`; verified Σ,BM=`Z/2`/`Z/3`/AND,walking-arrow,disc). Profile `[(2,0),(0,2)]` count =
  **4 monoids on 2 elts** = Reader's `B_0²→4` mechanism. **REFUTED (computed):** "categories over 𝕊 / discrete
  Conduché fibrations / copresheaves 𝕊→Set" — nontrivial 𝕊-action (representables `𝕊(0,-)`,`𝕊(1,-)`, twisted) breaks
  **associativity**; only trivial/product action lifts (grade σ=thread ≠ 𝕊-arrow `t_s∘T`). Per-state-different
  unroutable (𝕊 connected); vertical-only fails everywhere-defined. **CONJECTURE (completeness OPEN):** State
  liftings ≅ **Cat** via `C↦𝕊×C`; general-M ↔ π_0(position-threading)-indexed families of categories, holonomy-free.
  Node `state-liftings-holonomy-free`=**computed**, registry valid. Engines `scratch/general-M-liftings/`; note
  `memory/for-collaborator/2026-08-10-state-liftings-holonomy-free.md`.
- **★★ `2026-08-10-state-liftings-grade-independence.md` — the completeness CRUX (grade-independence) PROVED.**
  Follow-up to holonomy-free. **PROVED (|S|=2, poly):** object sets `J_t^s` are grade-independent, `A_t≅A_id`.
  Two pieces: **(P1)** `A_id` = **Reader-with-E=S** (grade `id` ⟹ trivial threading ⟹ `(id,(id))`-restricted
  structure IS Reader's comult/counit; State laws specialise to Reader's ⟹ by my Reader thm, `A_id`≅S-indexed
  family of small cats `(C̃_s)`); **(★)** `δ_out` is **functorial** = outermost-object component of associativity
  `μTμ=μμT`. Then `sh_t=δ_out^{(id,(t))}` (LU shadow) and `pr_t=δ_out^{(t,(t'_s)),thread=id}` are **inverse
  bijections** `J_t^s≅J_id^s=Ob C̃_s` — a chosen 3-fold datum collapses one side of (★) to the RU factorization
  `(t,(id))` whose `δ_out=id` (RU1). The store-monoid grades are a MIRAGE. Verified: (★) 32768 instances (Σ,𝕊×ℤ/2),
  tracks assoc under corruption (`conv4.py`); sh/pr inverse+degree-preserving on 𝕊×C. **Completeness now reduced to
  ONE residual lemma: holonomy-triviality** (source-independence `C̃_0≅C̃_1=C` + trivial 𝕊-transport; 𝕊 connected).
  Registry: **proved** node `state-grade-independence` (premises P1+★ proved); completeness stays **speculative**.
  Engines `scratch/general-M-liftings/{verify_star,sh_pr,verify_positions,conv4}.py`; note
  `memory/for-collaborator/2026-08-10-state-grade-independence-crux-proved.md`.
- **★★ `2026-08-11-state-liftings-holonomy-triviality.md` — COMPLETENESS: State liftings ≅ Cat (the LAST lemma).**
  The residual holonomy-triviality lemma is **proved** (object level rigorous+new; morphism level mirror+decisive
  enumeration). `C↦𝕊×C` is a bijection; the whole State-liftings program closes. **Engine — the deepest-object
  component of associativity:** for the transport `τ^g(s,c)` (object `c`@source `s` → source `g(s)` along grade `g`),
  `μTμ=μμT` on the innermost tower object gives **`(ASSOC-DEEP) τ^{σ'}(s,c)=τ^{t_s}(T(s),τ^T(s,c))`, `σ'(s')=t_{s'}(T(s'))`**
  (both formulas 0/196608 for generic random τ, `fit_general.py`). LHS sees only the middle `t_s` at source `s`; `σ'`
  mixes ALL middles ⟹ off-source middles free (`S^S` transitive) ⟹ **ENDPOINT-LOCALITY** (`τ^g(s,c)` depends on `g`
  only via `g(s)`; proof `T=id`, `t_{s'}=const_{g(s')}`, common RHS). Then `τ^{b∘a}=τ^b∘τ^a`+`τ^{id}=id` ⟹
  `ψ_{s→m}` bijections = functor out of CODISCRETE `K(S)` = coherent **trivial** iso-system ⟹ single `C`, lifting `=𝕊×C`
  (H1+H2). Morphism level: `enum_hom.py` FREE hom-transport ⟹ exactly **4 = #monoids-on-2, all trivial** (nsamp=1500);
  `twist_test.py`: `𝕊×ℤ/n` automorphism-twist lifts iff `α≡id`. Registry: **proved** node `state-holonomy-triviality`
  (children `state-endpoint-locality` proved, `state-morphism-holonomy-trivial` computed); validator OK. Engines
  `scratch/general-M-liftings/{fit_general,targeted,enum_hom,twist_test}.py`; note
  `memory/for-collaborator/2026-08-11-state-liftings-holonomy-triviality.md`.
- **★★ `2026-08-11-update-monad-liftings-holonomy-full.md` — general-M is HOLONOMY-FULL: the
  "π₀-indexed families / holonomy-free" conjecture is REFUTED.** Canonical varying-P class = **update
  monad** `Upd_{(S,P,↓)}` (Ahman–Uustalu TYPES 2013). Position-threading action (the definition
  `state/PROVE.md` flagged missing) = the monoid action `↓:P↷S`; **action category `𝔸(↓)`** (obj `S`,
  arrows `s--p-->s↓p`). **Theorem:** degree-1 poly monad liftings ≅ **`Fun(𝔸(↓),Cat)`** — HOLONOMY-FULL;
  ASSOC-DEEP `(COMP) ρ_{s,p⊕q}=ρ_{s↓p,q}∘ρ_{s,p}`. **Counterexample (EXHAUSTIVE / all 16384 Upd³ shapes
  + iso-check):** `P=ℤ/2` trivial action ⟹ `𝔸=Bℤ/2⊔Bℤ/2` ⟹ **4 pairwise-non-iso liftings** = `ℤ/2`
  holonomy per orbit. **π₀ ≠ invariant**: Reader (P=1,π₀=2)→1, Z2_triv (π₀=2)→4. Poles explained:
  Reader=discrete `𝔸`; State=overwrite has **RESET** elements ⟹ endpoint-locality ⟹ collapse (bounds
  `state-holonomy-triviality`). Registry: `reader-liftings-general-M-conjecture`→**dead-end**, new proved
  node `update-monad-liftings-holonomy-full`(+3 premises), validator OK. Engines
  `scratch/general-M-liftings/{update_engine,test_update}.py` (exhaustive); note
  `memory/for-collaborator/2026-08-11-general-M-is-holonomy-full.md`.
- **★★ `2026-08-12-holonomy-composition-zs-bridge.md` — the state/directed CROSS-MODE BRIDGE.**
  Composing two update monads sharing `S` (a DL) = **Zappa–Szép product `P⋈P'`** (Ahman–Uustalu 2013).
  **(a) PROVED:** composite liftings ≅ `Fun(𝔸(↓)⋈𝔸(↓'),Cat)` — classifier composes by ZS product of
  action categories. **(b) REFUTED (compute-first):** `Stab_{P⋈P'}(s)≅Stab_P(s)⋈Stab_{P'}(s)` FALSE;
  internal reframe `Stab_{P⋈P'}(s)≅Stab_G(s)`, factorization need not restrict to point stabilizer.
  Witness `S₃=A₃·⟨(12)⟩`/3-pts: `Stab_G=C₂` but factors trivial; sweep `S₃/S₄/A₄/D₄/Z2×Z2` 268/448
  proper, containment `⊆` always ⟹ **orchestration SYNTHESISES holonomy** (emergent reentrancy).
  **(c') PROVED (aligned abelian):** `[ω]∈H²(B;A)` obstructs the composite holonomy splitting UNENTANGLED;
  ℤ/2 witness ε=0→ℤ/2×ℤ/2 vs ε=1→ℤ/4 = stabilizer shadow of reentrancy `[ω]=ε` (distinct site, flagged).
  Degree gap resolved: H² governs whether two H¹ holonomies factor, never an equality. Engine
  `scratch/general-M-liftings/zs_holonomy.py`; registry `holonomy-composition-zs-bridge.json` (proved);
  note `memory/for-collaborator/2026-08-12-holonomy-zs-bridge.md`. **Welds state/isotropy + directed/ZS.**
- **★★ `2026-08-13-emergent-holonomy-meeting-points.md` — the 448-backbone UPGRADED to a general theorem.**
  Emergent-holonomy invariant `h(s) = |Stab_P(s)\Stab_G(s)/Stab_{P'}(s)| =
  |Stab_G(s)|/(|Stab_P(s)||Stab_{P'}(s)|) = |(P·s)∩(P'·s)|` — a positive integer = # crossings of the two
  factor orbits; `h(s)=1 ⟺` aligned `⟺` orbits meet only at `s` `⟺ (c')` applies. **Disjointness Lemma**
  `P∩gP'g⁻¹={e}` ∀`g` (3 lines) ⟹ uniform double cosets ⟹ ratio IS an integer; **intermediate-point
  bijection** `int(pp')=p'·s : A\U/B ≅ (P·s)∩(P'·s)`. Proves WHEN the (c') `[ω]∈H²` analysis applies
  (resolves 08-12 gap 2). Verified `zs_holonomy_L3.py` (2594+41064 checks, 0 mismatches); registry
  nodes `disjointness-lemma`/`emergent-holonomy-meeting-points`/`c-prime-hypothesis-characterized`
  proved; note `memory/for-collaborator/2026-08-13-emergent-holonomy-meeting-points.md`.
- **★★ `2026-08-14-two-omega-sites-isotropy-restriction.md` — the two `[ω]` sites are IRREDUCIBLY
  DISTINCT (closes gap #3 of the bridge).** (1) `Sk_C` automorphism-rigid ⟹ isotropy restriction
  `i_x*≡0` ⟹ naive "stabiliser = isotropy-restriction of handoff" FALSE. (2) DISCOVERY: aligned+normal
  ⟹ `E=A⋊B` splits ⟹ `[ω_st]=0`; `(ℤ/2,ℤ/2,ℤ/4)` geometrically impossible; non-aligned ⟹ `E/A≇B`
  ill-typed — the bridge §3 `ℤ/4` witness is abstract extension theory, not aligned ZS geometry
  (scope-correction of my own peer-reviewed file). (3) key lemma `i_a*F*=F_a*i_{Fa}*`; rigid target ⟹
  `i_s*F*[ω_h]=0` ∀`F:𝔸(↓_⋈)→Sk_C`. Both `ε`'s = one ZS bit under two incomparable maps (off-diagonal
  vs isotropy). Verified `scratch/two-omega-sites/{comp1_bw_isotropy,comp2_geometric_splitting}.py`;
  registry `two-omega-sites.json` (proved); note `memory/for-collaborator/2026-08-14-two-omega-sites-resolved.md`.
- **★ `2026-07-15-comparitor-double-comonoid.md` — Double comonoids in the duoidal `(Poly,◁,⊗)` =
  the SETS OF COMMUTATIVE MONOIDS (via a fibrewise Eckmann–Hilton collapse). REFUTES the PROVE target
  "= degenerate `y^A`/`Ay`" in both directions (`y^{S_3}` excluded, `2y²={ℤ/2,ℤ/2}` included).
  Registry `comparitor-comonoid-nogo` promoted `speculative → proved`. Novelty = the EH reduction +
  corrected classification; `Indep`/Eq.33/⊗-comonoid-classification are Spivak's.**
- **★ `2026-07-16-hedges-distributive-table.md` — Jules Hedges' 4×4 interchange table over `{⊗,×,+,◁}`
  on `Cont`, ALL 16 cells proved; agrees with Hedges 15/16. Convention DECODED (row=outer; (co)cartesian
  columns = preservation, tensor columns = duoidal interchanger; formal (co)limit gadgets dashed ⟹ `+`
  row & `×` column all `–`). `◁/+`,`◁/×` are LEFT-variable only (NS Ex 6.56; `2y²≇4y²`); only `⊗/+`,`×/+`
  two-sided. `×/⊗` CORRECTED to `–` (witness `(1,y,y,1)`⟹ impossible `1→y`); the genuine `⊗`–`×` map is
  the formal `⊗/×` — transposition flagged for Hedges via Neil. The one deep `L` (`⊗/◁`) = comparitor
  coreflection + Eckmann–Hilton. Registry `hedges-interchange-table.json` = proved.**
- `2026-06-09-two-atoms-zappa-szep` — Two-atom ZS product (PDF generated)
- `2026-06-10-zs-criterion-cocycle` — ZS criterion via cocycle condition
- `2026-06-11-cofree-free-containers` — Cofree/free container relationship
- `2026-06-12-container-chain-rule` — Container derivative chain rule
- `2026-06-12-ks-nogo-level-analysis` — KS nogo level analysis (PDF generated)
- `2026-06-13-monoidal-coherence-four-structures` — Four monoidal structures coherence (PDF generated).
  **ERRATUM 2026-07-14:** the Dirichlet *strictness* claim (φ = identity, ⟦–⟧ strict monoidal) is REFUTED — it was
  circular (⊗ read off the container presentation). ⟦–⟧ is STRONG, not strict; ⊗ is Day convolution of (Set,×,1),
  which is Niu–Spivak arXiv:2312.00990 Prop 3.79, *not* mine. Pentagon/triangle for ◁ are unaffected.
  See registry node `dirichlet-strict-monoidal` (dead-end, refutation: proved).

## Level 1 — Lean

- `lean/Containers/` — **local, and the only copy.** No upstream repo (policy — see "GitHub" below).
- Landed earlier: `Basic`, `Directed`, `ComonadConverse`, `Cofunctor`, `DContCat`, `ZappaSzep`
  (M1, M2, M2b, M4, ZS assoc).
- `Cont.lean` (Cont as a category; binary product & coproduct with universal properties),
  `Sequential.lean` (the sequential operator ◁ — renamed from "composition", per Neil),
  `Monoidal.lean` (`ContMonoidal` — pentagon, triangle, naturality for ◁).
- `Dirichlet.lean`, `FourMonoidal.lean` — all four monoidal structures on Cont machine-checked:
  `contCoprodMonoidal` (+,0), `contProdMonoidal` (×,1), `contDirichletMonoidal` (⊗,y), `ContMonoidal` (◁,I).
  Plus extension-functor comparison isos, and `dirToSeq : C ⊗ D ⟶ C ◁ D` (⊗ = the uniform fragment of ◁;
  not surjective). **The map `dirToSeq` is PRIOR ART — six independent statements. Do not claim it.**
- `Comonoid.lean` — **M3**: a directed container is a comonoid in `(Cont, ◁, I)` (forward).
- `ComonoidConverse.lean` — **M3b** (2026-07-15, `lean-verified`): a `◁`-comonoid **is** a directed
  container (`Container.Comonoid.toDirectedContainer`). Reduces to M2b via `seqExt`; counit laws by
  unitor-`hom` cancellation, coassoc by one `rw` (transport-free). One round trip done (`rfl`), the
  reverse round trip (comonoid→directed→comonoid) outstanding — outer-shape `C◁C` transport won't
  elaborate. → `memory/for-collaborator/2026-07-15-m3b-comonoid-converse-lean.md`
- **★ `Free.lean` (2026-07-16/17, `lean-verified`, ZERO sorry)** — the **monoid mirror**: the **free
  monad on a container** as a monoid in `(Cont, ◁, I)`. Carrier `PTree` (W-type `Tr(1)`, directions =
  LEAVES) + `graft`/`split` (μ) + `η`; `Container.Monoid` structure; `Container.freeMonoid` with **ALL
  THREE ◁-monoid laws PROVED** as container-morphism equations: unit-L, unit-R (Lemma B `graft_unit_right`,
  `leaves_nd_transport`, `split_unit_right`), and **assoc** (`graft_assoc` = Lemma C, `split_assoc` =
  Lemma D — assoc discharged **2026-07-17**). **All `Quot.sound`-only, axioms re-checked.** First
  machine-checked free-monad-on-a-container. Construction is Gambino–Kock 0906.4931 Thm 4.5 — proof
  object is mine. Registry `free-monad-grafting.json` = **lean-verified**. →
  `memory/for-collaborator/2026-07-16-lean-free-monad-unit-laws.md`
- **★ `FreeUniversal.lean` (2026-07-24, PARTIAL, ZERO sorry, `Quot.sound`-only)** — the free-monad
  **universal property** extending `Free.lean`. `freeInsert` = α_X; `freeExtShape`/`freeExtPos`
  packaged as `freeExtend` = **ĝ : X.free ⟶ M** (full morphism); **`freeExtend_triangle` = the FULL
  adjunction triangle `α;ĝ=g` (BOTH shape+position halves)** — position half via new
  `mult_right_unit_pos` extracting M's right-unit backward law through the generic
  **`ContainerMorphism.onPos_congr`** (projection inverse of `ext'`, turns a packaged morphism law
  into its coordinate/position fact); `freeExtend_unit` = ĝ preserves the unit; `freeExtShape_unique`
  = object-level uniqueness (recursion-consistent shape map is ĝ₁, transport-free). **MULT-FORWARD**
  (shape half `freeExtShape_mult` + `mult_assoc_shape`) landed 07-24 s2; **both M-law BACKWARD
  extractions** `mult_left_unit_pos` + `mult_assoc_pos` (duals of the forward ones via `onPos_congr`;
  `mult_assoc_pos` a one-liner, transport = literally `mult_assoc_shape`) landed 07-24 s3 — the two
  inputs the MULT-backward law (§4.3) consumes; its base case verified, node step remains. **REMAINING**
  (not yet Lean): MULT-backward node step (`split_assoc`×1.5, threads `mult_assoc_pos`) + backward
  uniqueness (needs `cat`/`split`-bijectivity) ⟹ node `free-monad-universal-property` stays **`proved`**
  (child `mult-bwd-mlaw-inputs-lean` = lean-verified). Handoff `for-collaborator/free-monad-mult-backward-lean.md`.
  **Also this session:** confirmed `lean/Containers` is **Mathlib-free core** ⟹ the **cofree comonad**
  (LEAN.md's named target) is NOT core-formalisable (needs coinductive `PFunctor.M`); flagged for a
  Mathlib-adds decision. → `memory/for-collaborator/2026-07-24-free-monad-universal-property-lean.md`
- **★ `SeqProdDistrib.lean` (2026-07-16, `lean-verified`, ZERO sorry, `Quot.sound`-only)** — the
  **first machine-checked Hedges-table cell**: `Container.seqProdDistrib` proves the `◁/×` LEFT
  distributive law `(P × P') ◁ Q ≅ (P ◁ Q) × (P' ◁ Q)` as a full `ContainerIso` (both round-trips).
  FIRST iso in the library whose shape map is only *propositionally* invertible (sum-domain currying →
  non-defeq `Sum.elim`-η); two reusable transport helpers born here — `ContainerMorphism.ext_id`
  (destructure-then-`subst` to collapse the fibre dependency) and `heq_sigma_mk` (`Sigma.mk` HEq-
  congruence under a change of fibre family). Registry `hedges-interchange-table.cell-comp-times` =
  **lean-verified**. → `memory/for-collaborator/2026-07-16-lean-seq-prod-distrib.md`
- **★ `SeqCoprodDistrib.lean` (2026-07-17, `lean-verified`, ZERO sorry, `Quot.sound`-only)** — the
  **second machine-checked Hedges-table cell**: `Container.seqCoprodDistrib` proves the `◁/+` LEFT
  distributive law `(P + P') ◁ Q ≅ (P ◁ Q) + (P' ◁ Q)` as a full `ContainerIso` (both round-trips).
  Sibling of `seqProdDistrib` but STRICTLY cleaner: coproduct shape is already a `Sum`, so the bijection
  just pushes the `inl`/`inr` tag across `◁` — the fibre `Sum.elim P.Pos P'.Pos (inl s)` IS `P.Pos s`
  definitionally, positions are `fun w => w`; **no `Sum.elim`-η rule, no transport**. Both round trips =
  `ContainerMorphism.ext_id` (reused from `SeqProdDistrib`) + `cases <;> rfl` / `cases <;> HEq.refl`.
  Registry `hedges-interchange-table.cell-comp-plus` = **lean-verified**. →
  `memory/for-collaborator/2026-07-17-lean-seq-coprod-distrib.md`
- **★ `TensorCoprodDistrib.lean` (2026-07-17, `lean-verified`, `Quot.sound`-only)** — the **third**
  Hedges-table cell: `Container.dirCoprodDistrib` proves the `⊗/+` law
  `(P + P') ⊗ Q ≅ (P ⊗ Q) + (P' ⊗ Q)`. Same tag-pushing bijection as `seqCoprodDistrib` with `⊗`
  (product positions) for `◁`; genuinely two-sided (⊗ symmetric). Registry `cell-ox-plus` = **lean-verified**.
- **★ `TimesCoprodDistrib.lean` (2026-07-22, `lean-verified`, ZERO sorry, `Quot.sound`-only)** — the
  **fourth machine-checked Hedges-table cell**: `Container.prodCoprodDistrib` proves the `×/+` LEFT
  distributive law `(P + P') × Q ≅ (P × Q) + (P' × Q)` as a full `ContainerIso` (both round-trips).
  Sibling of `dirCoprodDistrib`/`seqCoprodDistrib` with the categorical product `×` (whose positions are the
  **coproduct** `P s ⊕ Q t`) in place of `⊗`/`◁`. The tag-pushing bijection again needs no transport: the
  fibre `Sum.elim P.Pos P'.Pos (inl s)` IS `P.Pos s` definitionally, so each summand's position coproduct
  `P.Pos s ⊕ Q.Pos t` matches on the nose; positions are `fun w => w`, both round trips = `ext_id` +
  `cases <;> rfl` / `cases <;> HEq.refl`. `×` symmetric ⟹ two-sided cell. **Completes the "distributes over
  `+`" column in Lean** (`◁/+`, `⊗/+`, `×/+`). Registry `hedges-interchange-table.cell-x-plus` =
  **lean-verified**. → `memory/for-collaborator/2026-07-22-lean-times-coprod-distrib.md`
- **★ `DirichletComonoid.lean` (2026-07-18, `lean-verified`, `Quot.sound`-only)** — forward map of the
  bare ⊗-comonoid classification: `Container.DirichletComonoid.toFamilyOfMonoids` (⊗-comonoid ⟹ a monoid
  on every fibre). Counit laws force `δ` diagonal on shapes; assoc via the free-morphism lemma
  `dirichlet_mul_assoc` (cases δ + subst diagonal shape law collapses all transports). Exports the reusable
  `onPosOfEq`. Registry `bare-dirichlet-comonoid.lean-forward` = **lean-verified**.
- **★ `DirichletMonoid.lean` (2026-07-19, `lean-verified`, ZERO sorry, NO axioms at all)** — the
  **arrow-reversed dual**: forward map of the bare ⊗-**monoid** classification,
  `Container.DirichletMonoid.toShapeMonoidOplaxFibres` (⊗-monoid ⟹ a **monoid on shapes** + an **oplax
  monoidal functor** `P:(S,·,e)→(Set,×,1)` on fibres). `DirichletMonoid` (η:y⟶C, μ:C⊗C⟶C, unit laws, assoc)
  → `ShapeMonoidOplaxFibres` (smul/e/phi + shape monoid laws + oplax unit coherences `phi_one_smul`/
  `phi_smul_one` + oplax hexagon `phi_assoc`). **Cleaner than the comonoid: no `Quot.sound`** — shape mult
  is a *free forward map* (no forced diagonal to subst), so every law is `congrArg`/`onPosOfEq` of a law
  equation, transports collapse by `Eq` proof irrelevance; `phi_assoc = onPosOfEq M.assoc ((s,t),u) r`
  closes by `exact`. Reuses `onPosOfEq` from `DirichletComonoid`. The ⊗ column of the (co)monoid table is
  now machine-checked BOTH sides. Registry `dirichlet-monoid-classification.lean-forward` = **lean-verified**.
  → `memory/for-collaborator/2026-07-19-lean-dirichlet-monoid-forward.md`
- **★ `DirichletMonoidConverse.lean` (2026-07-20, `lean-verified`, `Quot.sound`-only, verified by MacBeth)** —
  the CONVERSE + both round-trips ⟹ the ⊗-monoid classification is a **full machine-checked isomorphism**
  `DirichletMonoid c ≅ ShapeMonoidOplaxFibres c`. Reverse map `toDirichletMonoid` rebuilds η/μ from
  (shape monoid + oplax φ); the 3 internal-`Cont` laws via `ext'` with shape-eq = monoid axiom
  (`one_smul`/`smul_one`/`smul_assoc`) and fibre goal = oplax coherence (`phi_one_smul`/`phi_smul_one`/
  `phi_assoc`) matched by `Eq` proof irrelevance — clean mirror of the forward `onPosOfEq`; both round-trips
  `rfl`. `lake build` green (29 jobs), no sorry, `#print axioms` = `[Quot.sound]` (via `funext` for `ext'`).
  Registry child `lean-converse` = **lean-verified**.
  → `memory/for-collaborator/2026-07-20-dirichlet-monoid-iso-lean.md`
- **★ `TimesMonoid.lean` (2026-07-20, `lean-verified`, `Quot.sound`-only, verified by MacBeth)** — the
  `×`-analogue of `DirichletMonoid.lean`: the FORWARD map for **Thm B**,
  `Container.TimesMonoid.toShapeMonoidOplaxFibresCoproduct` (a bare `×`-monoid for the categorical-product
  tensor `(Cont,×,1)` ⟹ a **monoid on shapes with empty identity fibre** `posEmpty:C[e]→Empty` + an **oplax
  functor into `(Set,⊔,∅)`**, routing `ψ:C[s·t]→C[s]⊕C[t]`). "One theorem parameterised by the fibre
  monoidal structure" made concrete — same skeleton, `⊔` for `×`, `∅` for `1`. The one new idiom: the `⊗`
  `congrArg Prod.snd` unit-coherence shortcut fails (fibre combiner is `⊕`); `onPosOfEq`'s unit-law content
  lands in `Empty⊕C[s]` (identity fibre through `η.onPos:C[e]→Empty`), recovered by `cases`+`Sum.inr.inj`+
  empty-fibre `.elim` — where `c[e]=∅` earns its keep. Assoc hexagon = raw `onPosOfEq M.assoc`. `lake build`
  green (31 jobs), no sorry, `#print axioms` = `[Quot.sound]`. Registry child `lean-times-forward` =
  **lean-verified**. OPEN: `×`-monoid converse (mirror `DirichletMonoidConverse.lean`).
  → `memory/for-collaborator/2026-07-20-lean-times-monoid-forward.md`
- **★ `DirichletComonoidConverse.lean` (2026-07-20, `lean-verified`, `Quot.sound`-only, verified by MacBeth)** —
  the CONVERSE + both round-trips ⟹ the bare ⊗-**comonoid** classification is a **full machine-checked
  isomorphism** `DirichletComonoid c ≅ FamilyOfMonoids c`. Reverse map `toDirichletComonoid` rebuilds ε/δ
  from a family of monoids (δ chosen **diagonal on shapes**); the 3 comonoid laws are therefore
  **transport-free** — `ext' rfl` + `one_mul`/`mul_one`/`mul_assoc` directly (the LEAN.md forced-diagonal
  transport prediction applies only to the *forward* dir). `DirichletComonoid.ext` (Prop law fields) reduces
  the round trips: `toDirichletComonoid_toFamilyOfMonoids` = `rfl`; `toFamilyOfMonoids_toDirichletComonoid`
  via `ext'` along `funext (fun s => (D.hdiag s).symm)` (the one surviving transport, matched by `Eq`
  proof irrelevance + `Prod`/`Unit` η). `lake build` green (30 jobs, no warnings), no sorry,
  `#print axioms` = `[Quot.sound]` (`ext` needs none). Registry child `lean-converse` = **lean-verified**.
  Whole ⊗ row now closed both columns. → `memory/for-collaborator/2026-07-20-dirichlet-comonoid-iso-lean.md`
- **★ `DirichletClosed.lean` (2026-07-14)** — **`(Cont, ⊗, y)` is a CLOSED monoidal category.** Internal hom
  (shapes = `Cont(q,r)`; positions at `f` = `Σ_t r[f₁ t]`), both round-trips, naturality in **both** variables,
  counit `dirEval`, triangle identity. **`#print axioms` → "does not depend on any axioms"; every proof is `rfl`.**
  The mathematics is **Niu–Spivak Ex. 4.78 / Eq. 4.79 — DO NOT CLAIM IT**; the **proof object** is mine, and is
  believed to be the first machine-checked Dirichlet closure. Negative controls (wrong position family; currying
  out of `×` instead of `⊗`) **fail to typecheck** — `(p×q)[s,t] = p[s] + q[t]` is a SUM with no projections,
  so **Lean states the ×-vs-⊗ distinction as a type error.**
- **★ `DirichletHomPi.lean` (2026-07-21, `lean-verified`, NO axioms at all, verified by MacBeth)** — the
  **Π-form** of the Dirichlet internal hom, `Container.ihomPiIso : ihom q r ≅ Πᵢ₌ₛq (r ◁ q[i]·y)`
  (`Container.ihomPi q r := piCont q.Shape (fun i => r ◁ monomialY (q.Pos i))`). Closes the 07-21 audit gap:
  the uniform closure formula I quote to Neil is now machine-verified to denote the *same container* as the
  morphism form (`DirichletClosed.ihom`). Both round trips are **`rfl`**; `#print axioms` = *no axioms* — the
  predicted `heq_sigma_mk`/choice transport (LEAN.md) never materialised, because the `ΠΣ≅ΣΠ` shape bijection
  is definitional under structure/`Sigma`/`Unit`-eta. New reusable defs: `Container.monomialY` (`A·y`) and
  `Container.piCont` (arbitrary-index container product — Shape `Πᵢ`, Pos `Σᵢ`; binary `prod` = `Bool` case,
  no Fintype). Scope: container identity only; the adjunction stays `dirichlet_closure`; only `⋆=×` formalised.
  Registry child `pi-form-equals-morphism-form` under `closed-day-structures.uniform-closure-formula` =
  **lean-verified**. → `memory/for-collaborator/2026-07-21-lean-dirichlet-hom-pi-form.md`
- **★ `MonadComonadTransfer.lean` (2026-07-25, `lean-verified`, `Quot.sound`-only, verified by MacBeth)** —
  **Neil's Ch4 item 2**: a monad on `Set` transfers to a comonad `G(S,P)=(S,M∘P)` on `Cont`. Abstract
  `SetMonad` structure (functor `obj`/`map` + `η`/`μ` + naturality + the 3 monad laws as fields, no Mathlib);
  transfer functor `SetMonad.G` (objects) + `onMor` (morphisms) with functor laws `onMor_id`/`onMor_comp`;
  counit `SetMonad.counit` (backward = `η`) + comult `SetMonad.comult` (backward = `μ`) as `ContainerMorphism`s;
  naturality `counit_natural`/`comult_natural`. The **three comonad laws** `counit_left`/`counit_right`/`coassoc`
  each reduce via `ContainerMorphism.ext' rfl` (**no transport** — `G`,`ε`,`δ` all identity-on-shapes) to ONE
  monad-law field: `right_unit`/`left_unit`/`assoc` respectively — the paper's §1.3 made literal (position-
  contravariance reverses arrows, so a monad law read backward is a comonad law). All seven results
  `#print axioms = [Quot.sound]`. Formalises the coordinate proof (`2026-07-25-monad-comonad-transfer.md` §1)
  ONLY; coclosure/left-Kan (§3) + Poly descent (§4) stay paper-only. Mirrors `DirichletComonoid.lean`. Registry
  child `lean-coordinate-proof` under `monad-comonad-transfer.coordinate-proof` = **lean-verified**. First
  machine-checked monad→comonad transfer on `Cont` in the corpus. → `for-collaborator/2026-07-25-lean-monad-comonad-transfer.md`
- **★ `DualTransfer.lean` (2026-07-25, `lean-verified`, `Quot.sound`-only, verified by MacBeth)** — the **exact
  dual**: a comonad `W` on `Set` transfers to a **monad** `H(S,P)=(S,W∘P)` on `Cont`. Abstract `SetComonad`
  structure (functor + counit `ε`/comult `δ` + naturality + the 3 comonad laws as fields); `SetComonad.H`
  (objects) + `onMor` (morphisms) with `onMor_id`/`onMor_comp`; unit `SetComonad.unit` (backward = `ε`) + mult
  `SetComonad.mult` (backward = `δ`); naturality `unit_natural`/`mult_natural`. The **three monad laws**
  `unit_left`/`unit_right`/`mult_assoc` each reduce via `ContainerMorphism.ext' rfl` (**no transport**) to ONE
  comonad-law field: `left_counit`/`right_counit`/`coassoc`. All seven `#print axioms = [Quot.sound]`. Registry
  child `lean-dual-transfer` under `monad-comonad-transfer.coordinate-proof` = **lean-verified**. Transfer now
  Lean-verified in BOTH directions. → `for-collaborator/2026-07-25-lean-dual-transfer.md`
- Axioms: `contDirichletMonoidal`, `DirichletClosed`, and `DirichletHomPi` need **none** (all coherences `rfl`);
  the other three need `Quot.sound` only. So ⊗ is the most definitionally well-behaved of the four — the
  opposite of what I expected.
- **★ `WorkersRetract.lean` (2026-08-29, `lean-verified`, ZERO sorry)** — the **Workers/BHM retract**:
  `A := ΔS ⊗ ΔT` (= `Δ(S×T)`, the Workers grading) is a **non-trivial retract** of `B := ΔS ◁ ΔT` (the BHM
  grading). `storeSection` σ (branch on `const t`) / `storeRetraction` r (**self-evaluation** `(s,g) ↦ (s, g s)`)
  as genuine container morphisms; `storeRetraction_storeSection` (**r∘σ = id**, `rfl`);
  `storeSection_storeRetraction_ne` (σ∘r ≠ id, `Bool` witness `⟨true, id⟩`); **`storeRetraction_coComult`
  (the collapse identity `r ∘ δ = Δ(d)`, `rfl`) — "⊗ is the diagonal of ◁"**, the composition-product companion
  of `deltaDC_prod` in `StateComonadTensor.lean`. Plus the impossibility: `storeDiagSection_coassoc` (δ' = σ∘Δd
  IS coassociative, `rfl`) but `storeDiagSection_not_right_counital` (right counit FAILS at `S=Bool`, shape
  `true`, position `⟨false,()⟩`) ⟹ δ' is not a comonad ⟹ `Δ : (Set,×) → (Cont,◁)` is oplax/lax only on the
  **core groupoid** `(Set_≅,×)`. Five of six theorems **axiom-free**; `storeDiagSection_coassoc` on `Quot.sound`
  alone. **Correction surfaced by the type checker:** the paper proof says both backward maps "are the identity,
  because all fibres are literally `S×T`" — in `Cont` they are the canonical **`Sigma`↔`Prod` swaps**
  (`B.Pos ⟨s,g⟩ = (q:S) × T`, a `Sigma`, is *not defeq* to `Prod S T`). Mutually inverse by structure η, so the
  theorem is unaffected, but the fibres are not literally equal. Registry `workers-retract-of-bhm-grading`:
  `P2-retract`, `P3c-diagonal-collapse`, `P3d-not-oplax-full-set` all upgraded to **lean-verified**, plus new
  child `L-lean-workers-retract`. NOT formalised: the P3ab hexagons (out of scope by design).
  → `for-collaborator/2026-08-29-lean-workers-retract.md`
- **Stale pointer, now recorded:** `Containers/Composition.lean` is deliberately **orphaned** (it redefines
  `Container.I`, clashing with `Sequential.lean`). The live `◁` is `Container.seq` in `Sequential.lean:49`.
- `lake build` clean: 0 errors, 0 warnings, zero `sorry`.

## Level 1 — Trust registry

- `proofs/registry/` — `equivalence-chain.json`, `pairwise-zs.json`, `README.md` (semantics).
- Chain (authoritative, `code/macbeth.json`): speculative < computed < peer-claimed < proved < peer-reviewed <
  published < lean-verified. Boundary at `proved`. Every non-root node carries `role: premise|attempt`.
- Validate with **`--root .`** (project root). The `read` paths in `sources.json` are stored **repo-root-relative** (`memory/reading/…`, `proofs/…`), so `--root memory` double-prepends `memory/` and yields ~130 spurious "read file missing" problems — a **FALSE alarm, not data rot** (diagnosed 2026-07-23; the lone `proofs/…` read ref proves the paths are project-root-relative). All 25 referenced source files exist; do NOT prune them.

```
python3 code/trustcheck.py --deployment code/macbeth.json --root memory \
  --sources memory/reading/sources.json \
  validate proofs/registry/equivalence-chain.json --files-dir proofs --registry-dir proofs/registry
```

## Level 1 — Papers (write sessions)

- **★★ `papers/containers-over-a-base.tex` (2026-08-27 WRITE; REVISED 2026-08-28 twice + 2026-08-29
  referee pass, amsart, 16pp, compiles clean, 0 undefined refs, citation floor deep-read).**
  [08-29 pass: fixed intro "connected" overload; tightened Set ◁-obstruction Prop; abstract grammar.
  Change log = `for-robin/2026-08-29-containers-survey-referee-pass.md`.] The **three-(four-)approaches survey** — Neil
  UID-125 contemplation deliverable. Thesis: **extensivity + local cartesian closure of the base are the
  two axes separating the rival notions of "a container in a category"; Fam(Vec^op) (neither property)
  forces the external approach.** §3 (**landscape of bases**, added 2026-08-28 2nd pass, NEW INPUTS 1+2):
  census table of ~10 base classes (Set/topos, finite-limit [Shapiro–Spivak], Weber pullbacks+exp-legs,
  Walker LSCC, any monoidal V [DJN], any fibration [von Glehn], Set^I [DPUV], Prof [FGHW], Vec/R-Mod,
  open Rel/Mod/Poly) on the two axes; **weakening tower** LCCC⊃Weber⊃Walker⊃spans as one ordered scale
  ([MACB] assembly, Vec falls off the bottom); **organising fact** (off good zone: lose extensivity OR
  internal Π); remark `rem:weberrefile` **δ/Φ re-filing** (`computed`): T4-tininess = Weber-δ (1106.1983),
  T2-familial-rep = Weber p.r.a. (TAC 18 2007) — different Weber papers, logically independent, T2 NOT on
  the tower. §4 (external `Fam(C^op)`) proves T1/T2/T4 in own words: **T1**
  full-faithful ⟺ unit connected (Set×Set extensive-but-not-full counterexample; corrects
  "extensive⟺full" folklore via Diers base-vs-codomain split); **T2** `⊗`-closed ⟺ familial-rep of Φ,
  closed only on `Fam_fin(Vec_fd^op)`, fails BOTH Vecs by dual mechanisms; **T4** `◁`-left-closed ⟺
  collapse `◁=⊗` (tiny positions), the CROWN inversion — extensivity OPPOSED to `◁`-closedness. §5
  (indexed Σ-Π-Δ) cannot form Π over Vec [Gambino–Kock]; **§6 (fibrational) NOW POPULATED (2026-08-28
  revision, Neil UID-132): referee (family vs codomain fibration) PLUS the logic of containers —
  `Cont(cod)=Fam(cod^op)` bifibration of proof-relevant predicates on positions; Fam preserves
  fibrations (Lem); fibred quantifiers = A/E liftings (E=Exists=reindexing, A=All); DUALISATION thm =
  container hyperdoctrine is the fibrewise op of Set's (∃↔∀,∧↔∨,⊤↔⊥, co-topos fibre); honest scope:
  position-level only, shape-level + joint BC/Frobenius OPEN. Cites von Glehn (ancestor), Jacobs CLTT,
  Hermida.** §7 (Walker LSCC) Vec NOT locally subcartesian closed (direct-read verdict, cross-fiber =
  `∐⊊⊕`, framed as reading-result). §8 two-axis discriminator theorem; §9 conclusion names the single
  open PROVE target: **does my 4-level branching chain lift index-wise to De Pascalis–Uustalu–Veltrì
  `IC_I`?** (seed for next PROVE.md). Cites DJN 2305.05655 / GK 0906.4931 / DPUV 2509.25879 / Walker
  2607.10242 / Weber 1106.1983 / Shapiro–Spivak 2305.00167 (all deep-read+). Scratch
  `scratch/write-2026-08-28.md`; notes `for-robin/2026-08-28-containers-survey-revision.md` +
  `for-robin/2026-08-28-survey-landscape-section.md`.
  **Provenance:** von Glehn debt DISCHARGED (now in sources.json at deep-read). Remaining non-arXiv flags
  for arXiv hygiene: FGHW (JLMS 2008, landmark, sources entry agent-summary, non-load-bearing census
  pointer) + Weber TAC 18 2007 (canonical p.r.a. paper, confirm pages). Jacobs/Hermida standard textbook
  refs (no arXiv ID, don't register in citation_check).

- **★★ `papers/effects-coeffects-containers.tex` (started 07-31; ADVANCED 2026-08-01; POLISHED 2026-07-31
  write → amsart, 19pp, compiles clean, 0 undefined refs, cite floor deep-read).** 07-31 polish pass
  (`scratch/write-2026-07-31-polish.md`): abstract tightened 270→185 words; Turi–Plotkin author-order
  standardized; 2 orphan macros dropped; §5 dichotomy-table 65pt overfull fixed. **SUBSTANTIVE CORRECTION:**
  the Atkey remark's old "non-branching = index-collapse" claim was FALSE per my own 07-31 PROVE
  (`proofs/2026-07-31-atkey-index-degree.md` Cor 2.3: index-collapse = M=Id ⊊ non-branching; Maybe/Writer
  are Freyd via STRENGTH not index-collapse) → rewrote `rem:atkey` to the honest orthogonal-axes statement +
  added a conclusion "graded refinement?" further-work bullet (natural arity/leaf gradings ruled out, Boolean
  dichotomy; coeffect-graded-comonad open, VPO uncited=not-yet-arXiv). 08-01 additions: §6 **related-conditions
  table** (Lemma A comm criterion + pairwise-independence Prop, 8-cell cube + Theorem C lone implication),
  Atkey remark after the arrow theorem (now honest orthogonal-axes framing; branching κ degrades *below*
  indexed-Freyd), and a
  **Purdy–Damato neighbour paragraph** in §Related work (2503.17191 CALCO 2025 = container DLs on Set vs mine
  on Cont, one level up ⟹ `G_M/λ/κ` SAFE novel; → memory `purdy-damato-2503-cleared-neighbour`). The
  **standalone effects-and-coeffects capstone** (Neil-steered 07-30; also lives
  as book Ch8). One monad `M` on Set, two container feeds: effect monad `T_M` (M on shapes, Ahman–Bauer
  2409.17664 Thm 6.3, **deep-read**) + coeffect comonad `G_M` (M on positions, the transfer). LEADS with
  the unrestricted face. (1) **Bialgebra face, ALL M** — mixed DL `λ:T_MG_M⇒G_MT_M` = oplax product-
  comparison `str`; Plotkin–Turi λ-bialgebra; nondeterminism/list included (**[proved]** E1/E3/E4, E2
  machine-verified incl. `Pf`). (2) **Arrow face, non-branching only** — reverse `κ:G_MT_M⇒T_MG_M` ⟹
  biKleisli/Hughes/Freyd over `(Cont,×)` iff M non-branching; obstructions E2′ (merging) + effect-strength
  (leaf-symmetry, Yoneda). (3) **Classification** — non-branching cartesian M = writer-with-absorbing-
  exceptions `E+A×(−)`. (4) **[lean-verified]** Maybe arrow assoc (`BiKleisliMaybe.lean`). Cites at
  **deep-read** floor: Ahman–Bauer, KRU 1912.13477; classical folklore (Hughes/Power–Robinson/Atkey/
  Jacobs–Heunen–Hasuo/Turi–Plotkin/Beck/Power–Watanabe/Brzeziński–Majid/Uustalu–Vene). **⚠ TWO citation
  TODOs (browse-blocked):** Goncharov 2602.18295 + DDR 1310.0605 are only `agent-summary` in sources.json
  → deliberately NOT formally cited (uncited "outline neighbour" §9); DDR's real title = "Patterns for
  computational effects arising from a monad or a comonad" (2013), not the JSC 2011 paper. Gaps flagged as
  Remarks (mult-T index-chase mechanical; ∏-scope; Dirichlet-⊗ open; finite branching+non-comm untested;
  general E2′ not yet Lean). Venue = arXiv → ACT/MFPS/CMCS (out to Neil). Scratch: `scratch/write-2026-07-31.md`;
  flag `for-robin/2026-07-31-effects-coeffects-paper-draft.md`. Share via projects volume (write = no email).

- **★★ `papers/applications-outlook.tex` (2026-07-23 write session, 6pp, compiles clean).** The **Path-5
  grant-Impact outlook**, staged for Neil's applications turn — **standalone, NOT the book, Neil-gated**.
  One argument: because a directed container *is* a small category (**[lean-verified]** `DContCat.lean`),
  composing supply chains / ontologies / orchestrated agents is one Zappa–Szép problem whose only
  obstruction is one class `[ω]∈H²(Sk_C;𝒟)` — **[proved]** existence `(L)∧(G)` + obstruction theorems —
  and that one class is inventory inconsistency = ontology-merge conflict = agent re-entrancy. Folds in
  the **[computed]** supply-chain ZS instance (`proofs/2026-07-23-supply-chain-zs.tex`; `[ω]=ε∈ℤ/n`, a
  bit refined to a unit-count) as the §4 illustration + the olog `n=2` sibling. **Grade discipline is the
  spine:** boxed grade-key up front; every domain row graded inline; object-level "a real supply chain
  *is* a category" stays **[open]** (SEED Q4); nothing about a domain exceeds [computed]. Provenance:
  Ahman–Uustalu hinge deep-read; Spivak ologs cited by name for the *definition* only with an explicit
  deep-read TODO (agent-summary in sources); morphism-level cofunctor/lens cites own connection note.
  Deliver via projects volume / email PDF at next wake daily (write-session = no email). Scratch:
  `scratch/write-2026-07-23.md`; flag note `for-robin/2026-07-23-applications-outlook-ready.md`.

- **★★ `papers/convergence-hub.tex` (2026-08-11 write session, 7pp, compiles clean; provenance floor
  deep-read).** The **Applications convergence-hub section** — thesis *"a composable agent, at the object
  level, IS a small category = directed container (DCont≅Cat)"*, defended by **four already-proved fronts**
  seen as one theorem: (1) classified INTO it (Reader/State liftings ARE categories, **[proved/lean]**,
  State-completeness flagged open, §3.1 scope remark); (2) cited AS infrastructure — **Smithe CAI II
  arXiv:2208.12173, verbatim Prop 2.7 "Famously ◁-comonoids correspond to categories [8]"**, [external,
  deep-read]; (3) generalized UPWARD (topos, anchored on *Comonads as Spaces* 2607.15091; Garner "Ionads"
  **signpost-only**, no formal bibitem — untracked); (4) bounded FROM OUTSIDE (Ch3 Bag 10≠9 + Fairbanks
  multigraph comonad, [proved/computed]). **§4 the careful contrast** (Prop "convergent peers"): convergence
  on the OBJECT, divergence on the COMPOSITION LAW — CAI II = Bayesian-lens/monoidal-bicategory-of-cilia
  (Def 3.8/3.15/3.21) vs my **ZS weld C⋈D, `[ω]∈H²`**; states CAI II is NOT distributive-law-free (Def 3.13
  = internal-hom-over-tensor, NOT a monad dist. law in Beck/ZS sense) and does NOT claim Smithe uses the
  weld. Self-contained; independent of the open State-completeness lemma. Reusable as a grant Applications
  passage. Scratch `scratch/write-2026-08-11.md`; flag `for-robin/2026-08-11-convergence-hub-section-ready.md`.
  From connection `dcont-cat-is-the-convergence-hub`.

- **★★ `proofs/2026-07-24-groupoid-zs-obstruction.{tex(7pp),md}` (PROVE) — the GROUPOID case of the ZS
  merge obstruction.** Seed conjecture *"connected groupoid ⟹ Sk_C contractible ⟹ `[ω]=0`"* **[refuted]**:
  a connected groupoid is a `K(Γ,1)`, so `H²(Sk_C;𝒟)≅H²(Γ;M)` is group cohomology. Over a one-object
  groupoid base the ZS defect **is the Schreier factor set** of `1→D→K→Γ→1`; merge exists ⟺ extension
  splits ⟺ `[ω]=0`; `#SFS=#complements`. **[computed]** obstructed witnesses `ℤ/4⊇ℤ/2` (base `B(ℤ/2)`),
  `Q8⊇`center (base `B((ℤ/2)²)`); split witness `ℤ/2×ℤ/2` (same base, merges). **[proved, general]**
  `cd(Sk_C)≤1 ⟹ [ω]=0 ∀D` — FREE groupoids always merge (Stallings–Swan). **Dividing line = freeness,
  not invertibility.** Social-net line **[computed]**: mutual-tie = free groupoid on the tie-graph ⟹ cd≤1
  ⟹ always merges (right reason: dimension 1); torsion identification can obstruct. Classical core
  (Schreier, BW=group-cohomology) cited; groupoid-ZS (Mundey–Sims) adjacent-not-scooped; object-level
  fidelity **[open]** (SEED Q4). Scripts `scratch/groupoid-zs/{groupoid_zs,dcont_check}.py`
  (F2 bar complex with correct `φ=conjugation`; reproduces `H²(V₄;ℤ/2)=(ℤ/2)³`; `(H)(ii)⟺D-normal`
  cross-checked on S3). Registry `groupoid-zs-obstruction.json` **[computed]**, validates.
  Collaborator + for-robin notes filed.

- **★ `books/category-of-containers.tex` §4.3–§4.4 (2026-07-19 write session, 33pp, compiles clean).**
  **§4.3 "Monoids and comonoids for the four structures"** — Neil's requested (co)monoid table (uid-65/66),
  presented as ONE boxed cartesian/cocartesian-collapse remark + the **◁/⊗ rows as a 2×2 of dualities**,
  climaxing on the ⊗ **lax/oplax duality = comonoid/monoid duality** (reversing the (co)mult arrow flips
  shape-map forced-diagonal↔free-monoid AND fibre-data lax↔oplax). Both ⊗ cells graded **[MacBeth, proved]**
  (⊗-monoid promoted computed→proved 2026-07-19), forward-Lean-verified, framed as elementary answers to
  Niu–Spivak Rmk 3.78 (monoid) / Ch9 Q5 (comonoid). ◁ cells cited (AU/DJN + GK/DUV), forward-ref Ch5.
  **§4.4 "the lens subcategory"** (uid-68) — monomials S·y^A ≅ bimorphic lenses (N–S Ex 3.41); closure
  Prop: products+terminal+initial-object CLOSED, coproducts+initial-algebras NOT — gently corrects Neil
  (products ARE present/monomial; the poorer side is colimits/recursion). New deep-read bibitems:
  NiuSpivak23 2312.00990, DJN 2305.05655, DUV 2509.25879. Note: `for-robin/2026-07-19-write-session-comonoid-table.md`.

- **★ `books/category-of-containers.tex` §"Closing the structures" (`sec:closed`, 2026-07-21 write session, 36pp, compiles clean).**
  New section in Ch "Algebraic structure on Cont", slotted BEFORE the (co)monoid table (per Neil uid-71 + WRITE.md).
  Replaces the old thin placeholder `Definition[Closed structures]` (which leaned on `Spivak21`=2111.10968, only
  `abstract`-grade). Arc (compute-first, book voice): (1) **Dirichlet closure as a hom of morphisms** — transpose by
  hand → `[p,q]=(Cont(p,q), f↦Σ_i q[f₁ i])`, shapes = morphisms, "prompt/response" reading; **cited** NS Ex 4.78 /
  Spivak Eq (44), MacBeth Lean `DirichletClosed.lean`. (2) **Same hom = product of composites** `[p,q]≅Π_i q◁(p[i]·y)`
  via ΠΣ≅ΣΠ; **[MacBeth, Lean-verified `DirichletHomPi.lean`/`ihomPiIso`]** (07-21). (3) **Uniform closure criterion**
  (the one NEW result): Day tensor ⊙_⋆ left-closed ⟺ (−)⋆B polynomial ∀B; internal hom `Π_i q◁(p[i]⋆y)`; **one-line
  necessity** via `[y^B,y]_⋆`; **[MacBeth, both directions]**, three instances cited (Spivak Eqs 38–40). (4) **"Is the
  condition ever really a condition?"** — RESOLVED 2026-07-22 write session: the **collapse tensor** `A⋆B := B/A/1`
  (unit ∅) is genuinely symmetric monoidal on Set yet `R_2=(−)⋆2` is non-polynomial (`|R_2∅|=2>1=|R_2 1|`), so
  `⊙_collapse` is **convolutional but NOT left-closed** — **convolutional ⊋ left-closed**; the side-condition bites.
  `Definition[collapse]`+`Proposition[collapse]` **[MacBeth]** ("Why in two breaths" proof), corrected teachbox
  **"why the collapse tensor slips through"** (collapses to THE point ⇒ no provenance to demand back), mechanism =
  `η_B` non-injective, and `Conjecture[which convolutional tensors close]` **[Conjecture, MacBeth]** (taut+η-cartesian
  ⟹ sums-of-products). Supersedes the old `[Open]` vacuity teachbox and the "support tensor no-associator" cautionary
  frame (support now only cited inside the corrected teachbox as the mirror non-example). Final "sentence to carry away"
  Remark updated: polynomial condition is a genuine dividing line. Source `proofs/2026-07-22-vacuity-resolved-collapse-tensor.md`;
  scratch `scratch/write-2026-07-22.md`; note `for-collaborator/2026-07-22-collapse-tensor-in-book.md`. (5) ×/◁ round-out: CCC (NS Thm 5.31, exp = criterion at ⋆=+)
  but not LCC; ◁ right-coclosure (Meyers). (6) forward pointer: ⋉/⋊ non-convolutional (DJN), ⋉ not closed, ⋊ directed-
  left-closed. New bibitem `SpivakRef` (2202.00534, verified-quote). Citations all ≥deep-read. Harvested+upgraded from
  `papers/four-monoidal-chapter.tex §sec:closed` (necessity was [speculative] there, now proved; handedness fixed to
  left-slot `(−)⋆B`). Scratch: `scratch/write-2026-07-21-book.md`; note `for-collaborator/2026-07-21-closed-structures-section.md`.
  ⚠️ Whole-book citation floor is `agent-summary` from `2405.13157` (SS2405) in the DCont≅Cof chapter — pre-existing,
  needs a deep-read in a future browse session (NOT touched this write session).

- **★ `books/category-of-containers.tex` §"Closing the structures" — CLASSIFICATION added (`sec:classification`
  subsection, 2026-07-24 write session, 40pp, compiles clean).** Turns the `sec:closed` arc from "here is a
  witness" to "here is the complete list, modulo one stated gap". **Replaces `Conjecture[which convolutional
  tensors close]`** (the taut+η-cartesian ⟹ sums-of-products guess) **with a THEOREM.** New subsection **"The
  complete list"**: compute-first (normal form `X⋆B=Σ X^{A_{B,u}}`, degree `d(B)=sup arity`), then three moves —
  **Move 1** `Lemma[the unit is small]` `|I|≤1`; **Move 2** degrees multiply `d(C⋆B)=d(C)d(B)` ⟹ `Lemma[bounded
  degree forces affine]` (`κ²>κ` trap); **Move 3** the HEART = `Lemma[the symmetry identity]` `B+D_B×X≅X+D_X×B ⟹
  D_B=1+S×B` ⟹ `∨_S`, and I=1 ⟹ `×`. **`Theorem[the complete list, bounded arity]` [MacBeth (bounded arity)]:**
  symmetric `⋆` polynomial-in-each-var + bounded arity ⟹ `×` (→`⊗`) or `∨_S` (→`▷_S`, `∨_∅=+→×_Cont`) — the three
  known closures are ALL of them. `Remark[the infinite-arity boundary]` **[MacBeth; open problem]** states the gap
  HONESTLY (Neil's "further-work not moonshot" discipline): `κ²=κ` defeats counting; affine = connected-COLIMIT
  preservation vs closure = connected-LIMIT only (independent, no shortcut); `R_2=y+y^λ` a formal fixed point ⟹
  counting provably blind; obstruction (if any) = element-level pentagon; non-symmetric (left⊉right closed) also
  open. Mechanism paragraph retargeted (tautness/cartesian η now hand off to the classification, not to a
  conjecture). NO new `\cite` (families already attributed upstream; theorem is `[MacBeth]`) ⟹ no provenance
  regression; whole-book floor still `agent-summary` from `2405.13157`, pre-existing. Sources
  `proofs/2026-07-23-closed-convolutional-tensors-classification.md` (bounded thm) +
  `proofs/2026-07-24-arity-gap-further-work.md` (gap); registry `closed-tensor-classification` (`main-theorem-bounded`
  = proved, `gap-infinite-arities` = speculative). Scratch `scratch/write-2026-07-24-book.md`; note
  `memory/for-collaborator/2026-07-24-classification-in-book.md`.

- **★ `books/category-of-containers.tex` NEW Chapter 6 "Monads and comonads: the free and cofree
  constructions" (2026-07-23 write session, 48pp, compiles clean, 0 new overfull).** Promotes+expands the
  old Phase-2 §7.1 seed into a full self-contained chapter, placed right after Ch5 (DCont≅Cat), before
  Zappa–Szép (which becomes Ch7; Phase-2 outline → Ch8, now derivative-only stub with a pointer). Arc
  (signature-lens, compute-first, book voice): (1) **The tools we borrow** — μF/νF, Adámek existence,
  accessibility, `T_F=μY.(X+FY)`, `D_F=νY.(X×FY)` [cited, tight; footnote: Neil wants these in a future
  Preliminaries chapter — flagged]; (2) **W-types and their duals** — `W S P`/`M S P` exist in Set; the
  cofree/M-type is the EASY side because container extensions **preserve connected limits** (reuse Ch3
  `thm:char`) ⟹ final-coalgebra sequence converges; indexed-W remark; (3) **Free monad of a container** —
  `C*=(S*,P*)`, trees+leaves, grafting monoid, tikz figure, Maybe/binary example; laws cite `Free.lean`
  (footnote: not committed ⟹ `[MacBeth]` not Lean-verified, per Preface); (4) **Free-monad Lemma** —
  `F⊣U`, α=insertion of generators, ĝ by W-recursion; **folds in the 2026-07-24 PROVE result** (base=M-unit,
  step=M-assoc, target's own laws applied); tag `[Cited: Gambino–Kock 4.5]`+footnote grading the coord proof
  `proved`/partial-Lean (`FreeUniversal.lean`); (5) **Cofree comonad = cofree DIRECTED container** — ★
  **STRIPPED the old `[MacBeth]` novelty tag**: cofree side is **Niu–Spivak 2312.00990 Prop 8.18/8.33/Thm
  8.45 PRIOR ART**; positions = ALL nodes (finite paths from root), not leaves; subtree category; Cofree.lean
  BLOCKED (core Lean no M-type, footnote); colist/binary example; (6) **Syntax and behaviour** — the duality,
  grant framing (Put through free monad of combined signature), two honest open ends. Citations all deep-read
  (G–K `0906.4931`, NS `2312.00990`); whole-book floor still `agent-summary` `2405.13157` (pre-existing,
  DCont chapter only — no new debt; `citation_check.py --report footprint` confirms). Scratch
  `scratch/write-2026-07-23-book.md`; note `memory/for-collaborator/2026-07-23-monads-comonads-chapter.md`.
  Backup of pre-edit file at `/tmp/coc-backup.tex`. Open q for Neil: final placement/numbering + Prelim chapter.

- **★ `books/category-of-containers.tex` REFRAMED Ch6 + NEW transfer section (2026-07-25 write session, 54pp,
  compiles clean, 0 undefined refs).** Executes Neil's 07-24 "Ch4 tasks" email. (1) **Ch6 retitled
  "Monoids and comonoids in Cont: directed containers, categories, and the free monoid"** — comonoid spine
  untouched; added closing section `sec:ch6-monoids` STATING the free ◁-monoid `prop:free-monoid-stmt`
  (`C*=(S',P')`, `S'=μY.(1+Σ_s(Ps→Y))`, `P'`=leaves, grafting, 3 laws; GK 4.5 + `Free.lean`) — **statement
  only**, UP deferred to Ch7 (per Neil "state here, prove there"); cross-linked both ways; S'/P' dependency
  handled by a footnote to `rem:indexed-w` + the 1+Σ initial-algebra presentation. Did NOT move Ch7's
  construction/figure (would gut the signature→syntax narrative). (2) **NEW Ch7 §"Monads on the base,
  comonads on Cont: the transfer"** (`sec:moncomon-transfer`): `prop:transfer` = monad→comonad transfer
  `G(S,P)=(S,M∘P)` **PROVED + Lean-verified** (`MonadComonadTransfer.lean`, registry `monad-comonad-transfer.json`
  status=proved); comonad laws ⟺ monad laws, dual H; fibrational teachbox; `rem:transfer-coclosure` = Neil's
  `G={M/(S,P)}=Lan_{(S,P)}M` (NS Prop 6.57/Ex 6.63); novelty Remark (AU/Purdy–Damato distinguished);
  Maybe example. **Item 1 (higher-order trees) = flagged STUB + browse TODO (Ghani–Kurz not read, content
  NOT asserted); items 3–5 (reader/Kleisli/oracle) = "on the horizon" teachbox, definitions only,
  [to be developed].** (3) **Ch3 fix:** coequaliser Prop `prop:coeq-fail` re-cited to AAG *Categories of
  containers* (FoSSaCS 2003, `\bibitem{AAGcat}`) Prop 4.3/Ex 4.4 — not the 2005 TCS paper. Citations all
  deep-read (NS 2312.00990, AU 1604.01187, GK 0906.4931); whole-book floor still `agent-summary` 2405.13157,
  no new debt. Backup `/tmp/coc-backup-refactor.tex`; scratch `scratch/write-2026-07-25.md`; note
  `memory/for-collaborator/2026-07-25-book-monoids-and-monads-on-cont.md`. Open qs for Neil: Ghani–Kurz
  paper id + placement; which of reader/Kleisli/oracle to work first.

- **★ `books/category-of-containers.tex` NEW Ch7 §"The two feeds entwine" + Neil's 07-27 additions
  (2026-07-28 write session, 58pp, compiles clean, 0 undefined refs).** Folds the PROVED entwining
  (`proofs/2026-07-27-monad-comonad-entwining.md`) into the transfer section as `\subsection{The two feeds
  entwine}` (`sec:moncomon-entwine`, after the Maybe example, BEFORE the forward-looking teachboxes so
  proved-precedes-stubs). Content: names `T=(MS,P⋆)` (A–B Thm 6.3) + `G=(S,M∘P)` (transfer); the oplax
  product-comparison `str:M(∏Z)→∏MZ` = backward map of `λ:TG⇒GT`; `Theorem thm:entwine` (entwining, 4 axioms
  = nat η/μ/str + Mendler i); teachbox "what λ is" (Beck–Chevalley); `Example ex:entwine-branching` (Pf
  breaks reverse orientation, union-of-products≠product-of-unions); dichotomy table (arity≤1 both / branching
  one-way); `Remark rem:entwine-scope` (∏-class only, general Mendler open). **Predicate-lifting language
  adopted** (Neil item 4: `P⋆` = universal Π-lifting). Neil's other additions: (item 3) **"One op, two
  faces" paragraph** in the outlook — transfer applies `(−)^op` to the fibre OBJECT, free/cofree to the
  recursion SCHEME; (item 5) **Workers `[to be developed]` line** added to the "on the horizon" teachbox;
  (item 2) **Ghani–Kurz teachbox** upgraded — DECODES the free-monad formula generically (C^*=finite terms;
  higher-order = function-typed arities) but keeps the exact n-dim signature as `[signature TODO — ask Neil]`
  (GK still not deep-read, no browsing this session); (item 1) literature sentences (Topos-PLTL, Hinze,
  A–B-first) were ALREADY landed in `rem:transfer-novelty` (07-25). **Honesty fix (referee pass):** the
  arity≤1 table cell said "str=iso" — WRONG (Maybe's exception shape gives str:M(1)→1, non-iso); corrected to
  "no overlap" (μ can't identify leaves ⟹ mult-T trivial). New bib: Beck 1969, Power–Watanabe 2002,
  Brzeziński–Majid 1998 (foundational entwining framework, cited from field knowledge; no new repo-source
  debt; whole-book floor still agent-summary 2405.13157). Backup `/tmp/coc-backup-entwine.tex`; scratch
  `scratch/write-2026-07-28.md`; note `memory/for-collaborator/2026-07-28-entwining-in-book.md`. **Standalone-note
  verdict for Neil (owed since 07-26): YES — the entwining earns a short self-contained note** (distributive
  laws = seed's core tool; the forced orientation + branching obstruction is a crisp 4–5pp story), but only
  AFTER the general-`j` chase or the Lean is done; flagged, not started.
- **★ `books/category-of-containers.tex` NEW §"Processes with state: the store comonad and the category of
  Workers" (`sec:moncomon-workers`, 2026-07-29 write session, 60pp, compiles clean, 0 undefined refs, 0 font
  warnings).** Folds the PROVED Workers result (`proofs/2026-07-28-delta-state-object-and-workers.md`) into
  Ch. `ch:moncomon` as the "processes with state" capstone, after the entwining section, before "Syntax and
  behaviour". Content: `Definition def:state-object` (`ΔS=(S,s↦S)`); `Proposition prop:store` (`ΔS`=codiscrete
  cat via `thm:objdict` ⟹ store comonad `S×X^S`, Uustalu–Vene); reader shadow `⟦ΔS⟧=S×(−)^S` (Neil's "something
  more"=writeback); `Definition def:worker` (`ΔS⊗p→q`, coords = writeback `f♯₁` + position map `f♯₂`);
  `Lemma lem:delta-mult` (`ΔS⊗ΔT=Δ(S×T)` strict, Lean); `Remark rem:why-otimes` (⊗ forced, × mis-sizes fibre);
  composition-multiplies-state display + coords; `Theorem thm:workers` ((Set,×)-graded category = coKleisli of
  `S↦ΔS⊗−`); `Remark rem:workers-para` (Para=Gavranović computed/further-work over Core(Set); **nearest
  neighbour Capucci–Myers `\cite{CapucciMyers}` — Ex 3.24 colax-action corner vs Thm A.4 dependency-essential
  corner, settle NO A.4 fragment**); "two axes" grant paragraph (state axis vs ZS directed axis `thm:h2`);
  effect–coeffect forward-pointer teachbox `[in development]` (compositor is a DL relating the two feeds; orient.
  = branching dichotomy, worked separately — NOT overclaimed as `λ`). **Lean tags:** `Workers.lean`+
  `StateComonad.lean` both built (`.olean`), tagged Lean-verified with the Preface footnote (files in `lean/`
  tree, not committed to book tree). **Also:** rewrote the "on the horizon" teachbox (Reader/Kleisli/Workers now
  DONE → point to new §; Oracle stays `[to be developed]`); ONE neighbour sentence for Spivak "Categories by Kan
  extension" `\cite{SpivakKanExt}` added to `rem:entwine-scope` (different carrier/orientation/output). New bib:
  UustaluVene08, CapucciMyers (2410.21889, deep-read), Gavranovic (2105.06332, deep-read TODO), SpivakKanExt
  (2503.21974, abstract). **Provenance (honest):** load-bearing neighbour = Capucci–Myers deep-read ✓; the two
  weaker cites (Spivak-Kan abstract; Gavranović UNREGISTERED) flagged in-text + tracker as deep-read TODOs; book
  floor unchanged (agent-summary, pre-existing 2405.13157). Backup `/tmp/coc-backup-workers.tex`; scratch
  `scratch/write-2026-07-29.md`.
- **★ `books/category-of-containers.tex` — profunctor `Arr_M` framing folded into `sec:moncomon-entwine`
  (2026-08-04 write session, 66pp, compiles clean, 0 undefined refs, 0 new overfulls, no new citations).**
  Per WRITE.md (paper PAUSED, Neil 08-02; UID-88 "lead with profunctor `Arr_M` on Cont"). AUDIT first: the
  two-feeds math was ALREADY fully in the book (transfer `sec:moncomon-transfer`, entwining `thm:entwine`,
  arrow classification `thm:arrows` in `sec:threemodes`, two-faces para) — so this session is placement/
  exposition, NOT new math. **Gap found & filled:** the concept *profunctor* appeared nowhere, and the
  reverse κ was presented only *negatively* ("fails mult-T") in the Monads-and-Comonads chapter where
  `G_M`/`T_M` live. Added a closing movement to `sec:moncomon-entwine`: `\paragraph{From a failed law to an
  arrow calculus}` (names κ), `Definition def:arrowprof` (`Arr_M(p,q)=Cont(G_M p,T_M q)` is a **profunctor**
  `Cont^op×Cont→Set` for EVERY M — immediate from functoriality of the two feeds; identity `η^T∘ε` + explicit
  biKleisli composite `μ^T·T_M g·κ·G_M f·δ`), a "profunctor-is-free / category-is-what-branching-costs"
  paragraph, and a teachbox landing the astonishment + the `E+A×X` (writer-with-exceptions) boundary answering
  Neil UID-85 restrictiveness worry. **Coherence edits:** `sec:threemodes` effect–coeffect para + `thm:arrows`
  statement now REFERENCE `def:arrowprof` (no re-introduction of κ/arrows as new) and use "profunctor"/"hom-
  profunctor of a category" language; two-faces arrow-face bullet says "turns the arrow profunctor `Arr_M` into
  a category". Honesty: profunctor claim tagged exposition (not a theorem); classification stays `thm:arrows`
  (MacBeth, proved). Scratch `scratch/write-2026-08-04-book.md`; note `memory/for-robin/2026-08-04-arr-profunctor-in-book.md`.

- **★ `books/category-of-containers.tex` NEW §"Two predicate liftings: All and Exists" (`sec:predicate-liftings`,
  2026-08-08 write session, 75pp, compiles clean, 0 undefined refs, 0 new citations).** The containers-chapter
  HOME Neil GREENLIT (UID-95), led by HIS A/E predicate liftings (UID-94 source note). Appended to end of the
  "Algebraic structure on Cont" chapter (`ch:algebra`), before the monoids/comonoids chapter. Beats: (1) define
  All=∏ / Exists=∐ liftings of a container from the extension functor + positions, worked binary-node×Maybe table;
  (2) **E = ◁** (`prop:E-is-comp`, prompts/replies hook — "sequencing is existential"); (3) **A cartesian-only
  bifunctor** (`thm:A-cartesian`, Yoneda section-count ∏_p f⁻¹(p): non-surjective ⟹ NO pushforward, bijective ⟹
  forced) = Neil's "can't define A on polynomial functors" flag made precise; (4) **A=T_M one level down**
  (`rem:A-is-TM`): "every Set monad lifts via T_M" FALSE — drop(Reader/State) kills, merge(Pf) non-canonical,
  cartesian(List) canonical; forward-ref to deep teachbox `sec:moncomon-fibration`; (5) **THE NEW RESULT —
  action law** A X(A Y C)=A(X◁Y)C (`thm:action-law`, from `proofs/2026-08-08-A-E-predicate-liftings.md`): A is a
  LEFT MODULE of (Cont,◁,y), Fubini ∏_p∏_q=∏_{(p,q)}, debate-prep intuition, mixed law iso iff X linear; (6)
  honesty remark (strict-=/rfl = flagged Lean rung; module pentagon/triangle NOT verified, only assoc+unit).
  "Proof-relevant" retired from prose, kept ONCE parenthetically. Tags: E=◁ [MacBeth, Lean-verified], boundary +
  action law [MacBeth, proved]. **Flags:** tone subject to Neil's UID-92 confirmation (no email in write session);
  `code/citation_check.py` absent at documented path (no new bibitems, so non-blocking). Scratch
  `scratch/write-2026-08-08b-book.md`; note `memory/for-robin/2026-08-08-book-predicate-liftings-section.md`.

- **★★ `books/category-of-containers.tex` NEW §"Which monads lift: the Σ-lifting is M◁(−)" (`sec:sigma-is-comp`,
  2026-08-09 write session, 77pp, compiles clean, 0 undefined refs, 0 new citations).** The CROWN identity of
  08-08 folded into `sec:moncomon-fibration` (`ch:moncomon`), placed as the culminating subsection right after
  the contravariant-caution remark, before the two forward-glance teachboxes. Source
  `proofs/2026-08-08-sigma-monad-is-triangle-monoid.md`. Beats: (1) `Proposition prop:sigma-is-comp`
  **T^Σ_M C = M◁C** (identity of endofunctors; η^Σ=η_M◁−, μ^Σ=μ_M◁−), shape/position computation done in the
  open (shapes=MS, positions=∐_{lv(m)}P(x_b)); **Lean-verified** `SigmaLift.lean` `sigmaLift_eq_seq`=rfl
  (definitional, sorry/axiom-free); (2) `Corollary cor:sigma-monad` **Σ-monad ⟺ M is a ◁-monoid (container
  monad) ⟺ ⟦M⟧ Set-monad w/ polynomial structure maps**, via Cont≃Poly↪[Set,Set] ff strong monoidal (⊗-monoid
  ⟹ ⊗ monad); "canonical section" σ = μ_M's backward map, coherence = ◁-monoid laws — so the 08-07 Reader/State
  proof is an EXAMPLE of a theorem (Reader=diagonal comonoid on E, State=store); (3) `Theorem thm:bag-refutes`
  **Bag refutes reverse-total ⟹ Σ-monad**: Bag reverse-total (μ=⊎ leaf-bijection, σ=id) but T^Σ_Bag not even a
  functor on Cont — Bag∉Cont (connected-pullback fail, |Bag(2×2)|₂=10≠9, {(0,0),(1,1)}∼{(0,1),(1,0)}); slogan
  reverse-total:◁-monoid :: analytic:polynomial :: forgets-provenance:tracks-provenance; (4) teachbox **both
  legs of the codomain fibration, clean criteria** (∏=T_M ⟺ cartesian / ∐=T^Σ ⟺ ◁-monoid; independent axes,
  List both, Reader/State ◁-monoid-not-cartesian) + Orestis oplax Λ-join ⊆ caveat = base-monad-join layer,
  separate from the strict object law. **ALSO resolved the "Open" flag** in the 2×2-grading teachbox
  (reverse-total⟹Σ-monad now marked FALSE, forward-ref cor:sigma-monad/thm:bag-refutes; parity-exhaustiveness
  stays open). No new bibitems (NiuSpivak23/AhmanBauer24/HermidaJacobs98/OrestisAgda all pre-existing deep-read).
  Scratch `scratch/write-2026-08-09.md`; note `memory/for-collaborator/2026-08-09-sigma-is-comp-book-section.md`.

- **★★ `books/category-of-containers.tex` NEW §"Which liftings, all of them: monad liftings are comonads over
  the base" (`sec:liftings-are-categories`, 2026-08-09 write session #2, 81pp, compiles clean, 0 undefined refs,
  0 new bibitems).** The CLASSIFICATION climax of `sec:moncomon-fibration` (`ch:moncomon`), inserted right after
  the both-legs teachbox, before the two forward-glances. Sources
  `proofs/2026-08-09-reader-liftings-are-categories.md` (centrepiece) + `2026-08-09-lifting-dichotomy-exhaustiveness.md`
  (unification lemma, general-M). Beats: (1) `Proposition prop:reader-reduction` fibred endofunctors over R=y^E ↔
  aggregators L:Set^E→Set; monad structure ↔ (ε counit, δ comult)+3 laws; (2) THE ASTONISHMENT — monad upstairs,
  comonad downstairs (μ^T backward ⟹ comultiplication; one-op-two-faces, forward-ref sec:moncomon-transfer);
  (3) `Lemma lem:monoid-comonoid` **∏ needs a monoid, ∐ needs nothing** (=T_M-cartesian boundary one level down;
  E has diagonal comonoid but no monoid ⟹ ∐ lifts, full-∏ dies); (4) `Theorem thm:reader-classification`
  **polynomial monad liftings of Reader ≅ E-indexed small categories** (L(B)=∐_v∐_{i∈Ob C_v}B_v^{C_v(i,→)}, ε=ids,
  δ=comp); table: ∏ excluded, Σ_U=discrete cats, ℤ/2 groupoid=genuine non-Σ/∏; (5) `Remark rem:analytic-excluded`
  polynomial IS the boundary (counit kills Sym²/Bag); (6) teachbox **the whole boundary lands on Cat** (liftings
  are small cats just as DCont was, `thm:objdict`, same equivalence read one level up); (7) teachbox **open
  frontier** State/general-M (Prop A′ family of aggregators A_σ threaded through shape monoid; State=S^S-graded/
  store-internal cat; ev_{s_0} not a monad morphism ⟹ ∏-transfer blocked; completeness NOT proved — flagged open).
  **Citation-floor fix:** the load-bearing "polynomial comonads ≅ small categories" step routes through the
  **deep-read** `thm:objdict`/`AU16` (Ahman–Uustalu 2016), NOT the abstract-only `ACU14` (1408.5809) — no new
  below-floor dependence introduced. Honesty preserved: `L polynomial` hypothesis flagged; classification NOT
  Lean'd (not claimed). Scratch `scratch/write-2026-08-09b.md`; note
  `memory/for-collaborator/2026-08-09-liftings-are-categories-book-section.md`.
- **★★ `books/category-of-containers.tex` CLIMAX REFRAME of the Ch7 liftings classification (2026-08-12
  write session, 87pp, compiles clean, 0 undefined refs, no new bibitems).** Promoted the general theorem
  from a hedged "humbling frontier" teachbox to the section CLIMAX; Reader/State demoted from "the two
  answers" to "the two degeneracies of one answer." Astonishment arc (fair-is-foul): (1) Reader liftings
  ARE categories → (2) State's store mult is INVISIBLE π₀=1 → (3) REVERSAL. Edits: (a) two-poles teachbox
  now ends by making the "π₀ classifies" conjecture EXPLICIT so the reader is complicit in the wrong guess.
  (b) NEW `\subsection{The general law: holonomy, and the two poles as its degeneracies}`
  (`sec:update-liftings-holonomy`): `Definition def:action-category` (update monad `Upd_{(S,P,↓)}` +
  position-threading action `↓:P↷S` + action category `𝔸(↓)`); the (COMP) deepest-object law `ρ_{s,p⊕q}=
  ρ_{s↓p,q}∘ρ_{s,p}` shown to BE functoriality of `ρ` on `𝔸(↓)`; `Theorem thm:update-classification`
  **liftings ≅ Fun(𝔸(↓),Cat)**, holonomy-full, with "Why it holds"; `Example ex:z2-holonomy` ℤ/2-trivial
  ⟹ 4 non-iso liftings (16384-shape census); teachbox **"trivial two ways"** (Reader=discrete 𝔸, nothing
  to transport ALONG; State=reset⟹endpoint-locality⟹codiscrete collapse, transport ERASED; free-ℤ/2=third
  road) — π₀ classifies IFF every component holonomy-trivial; MOVED CBP outside-view box here (now that
  "holonomy" is a defined character, + its converse ties to `ex:z2-holonomy`); NEW closing teachbox
  **"holonomy is a group representation"** (isotropy action = rep of `Stab(s)`; second-order datum, sibling
  of `[ω]∈H²` `\ref{ch:zs},\ref{thm:h2}`; grant orchestration payoff — composition remembers a group).
  Fixed one correctness slip in the theorem (discrete 𝔸 ⇏ constant functor; reworded to "trivial isotropy
  ⟹ π₀-indexed family of plain cats"). Citations sound: `AU16`/`CBP` deep-read; `AhmanUustalu13` = seed PDF
  `Ahman-Uustalu_Update-Monads..._2014.pdf`, cited for the standard `Upd` definition only, bibitem accurate.
  `citation_check.py` (WRITE.md) absent in env — provenance verified by hand. Scratch
  `scratch/write-2026-08-12-book.md`; note `for-robin/2026-08-12-ch7-climax-reframe.md`. Supersedes the
  08-11 entry below (whose frontier teachbox this replaces).

- **★★ `books/category-of-containers.tex` NEW §"When two of the modes meet: emergent holonomy"
  (`sec:emergent-holonomy`, 2026-08-13 write session, 91pp, compiles clean, 0 undefined refs, NO new
  bibitems).** The WELD between the Ch7 holonomy climax (`sec:update-liftings-holonomy`) and the ZS chapter
  (`ch:zs`). Placed as the LAST section of `ch:zs`, AFTER `sec:threemodes` — a "fair is foul" rug-pull on
  the three-modes table: the State and Directed rows are not disjoint. Arc: (1) recall one update agent's
  holonomy; (2) `Theorem thm:classifier-composes` — composing two update monads sharing S = ZS product
  `P⋈P'` acting on S, liftings ≅ `Fun(𝔸(↓)⋈𝔸(↓'),Cat)` (classifier monoidal under orchestration); (3) the
  naive guess `Stab_{P⋈P'}(s)≅Stab_P⋈Stab_{P'}` — containment always, PROPER generically; `Example
  ex:s3-emergent` the S₃/3-points witness WORKED (P=A₃,P'=⟨(12)⟩, s=1: both factor stabs trivial, composite
  =⟨(23)⟩≅ℤ/2, loop 1→(12)→2→(132)→1, neither leg fixes 1) = holonomy synthesised; (4) `Theorem
  thm:meeting-points` h(s)=|A\U/B|=|Stab_G|/(|Stab_P||Stab_{P'}|)=|(s·P)∩(s·P')|, h=1⟺aligned; teachbox
  "why the ratio is a whole number" (disjointness P∩gP'g⁻¹={e}); (5) `Theorem thm:emergent-h2` aligned-abelian
  [ω]∈H²(B;A), =0⟺E≅A×B⟺unentangled, ℤ/2 table (ℤ/2×ℤ/2 vs ℤ/4); teachbox "two H² classes that rhyme —
  and are NOT the same" (stabiliser H²(B;A) vs handoff H²(Sk_C;D) of `thm:h2` — DISTINCT sites, same ℤ/2,
  NOT identified). Grant close: "orchestration synthesises holonomy the parts lack; a degree-2 class certifies
  when the composite is a clean product" + operational reading (auditor counts orbit crossings, no cohomology
  to DETECT). Consistent with `prop:monoidanchor` (ZS of two monoids, not the corrected mis-reading). Sources
  `proofs/2026-08-12-holonomy-composition-zs-bridge.md`, `2026-08-13-emergent-holonomy-meeting-points.md`;
  cites `AhmanUustalu13`/`RW`/`BW85` (all pre-existing). Scratch `scratch/write-2026-08-13-book.md`; note
  `memory/for-robin/2026-08-13-emergent-holonomy-section.md`.

- **★★ `books/category-of-containers.tex` EXTENDED `sec:liftings-are-categories` with the STATE POLE +
  two-π₀-poles framing (2026-08-11 write session, 85pp, compiles clean, 0 undefined refs, +2 bibitems
  `CBP`/`AhmanUustalu13`).** REPLACED the outdated "open frontier: State" teachbox (which said State
  completeness was `[open]`) with: (1) `\subsection{The State pole: the store multiplication is invisible}`
  (`sec:state-liftings`) — `Theorem thm:state-classification` **State liftings ≅ Cat, C↦𝕊×C**,
  grade-independent aggregator; proof-sketch "the store multiplication is a mirage" (grade-independence via
  `sh_t`/`pr_t` ← outermost-object of assoc → ASSOC-DEEP asymmetry → endpoint-locality → functor out of the
  codiscrete cat → trivial holonomy → 𝕊×C); `Remark` copresheaf functorial-not-endpoint-local ⟹ fails assoc.
  Prov: object-level proved, morphism-level mirror+exhaustive |S|=2, soundness Lean'd `StateProductLifting.lean`.
  (2) teachbox **"one theorem, two poles"** — table Reader (discrete, π₀=|E|) vs State (codiscrete, π₀=1); THE
  astonishment = store mult contributes NOTHING. (3) teachbox **"outside view"** CBP `\cite{CBP}` (ter
  Horst–Mahadevan–Zambrano 2601.04456 Thm 6.14, deep-read) as structural resonance, NOT a container result.
  (4) teachbox **"the frontier: general container monads are holonomy-FULL"** (replaces naive compute-π₀
  cliffhanger) — today's PROVE result Upd liftings ≅ Fun(𝔸(↓),Cat), holonomy-full; Z2_triv π₀=2 but 4 liftings
  ⟹ π₀ does NOT classify; Reader/State = the two holonomy-trivial degeneracies (discrete / reset-collapse);
  open beyond Upd & higher degree. Sources `proofs/2026-08-11-state-liftings-holonomy-triviality.md`,
  `2026-08-10-state-liftings-grade-independence.md`, `2026-08-11-update-monad-liftings-holonomy-full.md`.
  **Flags:** `AhmanUustalu13` NOT yet in sources.json (cited for the update-monad DEFINITION only — deep-read
  in a browse session); Uustalu TTCS 2017 novelty-check on the Upd classification deferred. Scratch
  `scratch/write-2026-08-11-book.md`; note `memory/for-collaborator/2026-08-11-book-state-pole-section.md`.

- **★★ `books/category-of-containers.tex` NEW §"Two witnesses that are genuine (co)monads" (`sec:two-witnesses`,
  Ch3 `ch:which`, 2026-08-10 write session, 83pp, compiles clean, 0 undefined refs, 1 new bibitem `Fairbanks25`).**
  Makes the Ch3 non-closure boundary SYMMETRIC. Prior chapter had only the bare-functor coequaliser witness
  (Pair/swap→unordered pairs). New: a genuine MONAD and a genuine COMONAD both outside Cont, failing the SAME
  test (kernel pair of X→1). Beats: (1) `Prop prop:bag-not-container` **Bag∉Cont** (leaf-supported +
  reverse-total, μ a leaf-bijection, yet |Bag(2×2)|₂=10≠9; collision {(0,0),(1,1)}∼{(0,1),(1,0)}; my computation
  `bag_not_container.py`; forward-refs Ch7 `thm:bag-refutes`; Bag=list mod Sₙ); (2) `Prop prop:multigraph-comonad`
  **Fairbanks's undirected-multigraph comonad F(X)=(X³+X²)/2+X** = coequaliser (in comonads/Set) of id & edge-swap
  on the polynomial quiver comonad X³+X; fails kernel-pair-of-X→1 by Fairbanks's own line ((X³+X²)/2)²+X² ≠
  (X⁶+X⁴)/2+X² = F(X²), "squaring every summand ≠ substituting a squared variable"; F_dir's category = ·⇉·
  (source 3 arrows out→X³, target 1→X); (3) teachbox **"The boundary is two-sided"**: both = quotient of a
  container by a symmetry ⟹ provenance (pairing / orientation) lost = what polynomial must remember; "polynomial
  not analytic" is one two-sided law, one test; forward-refs Ch7 `rem:analytic-excluded` (Sym²/Bag₂ excluded as
  liftings for want of a natural counit — same boundary one level up). Also amended `sec:boundary` to name both.
  **Provenance:** VERIFIED Fairbanks MO 457580 verbatim (research agent, StackExchange API) BEFORE citing — browse
  note had functor wrong (X³+X²/2+X); corrected to (X³+X²)/2+X; `sources.json` `mo:457580` upgraded to deep-read.
  Bag half = own computation (no external cite). Scratch `scratch/write-2026-08-10-book.md`; note
  `memory/for-robin/2026-08-10-ch3-two-sided-boundary.md`.

- `papers/dialectica-tensors-deferred.tex` (**2026-07-19**, 6pp, compiles clean) — **held/deferred** §10 of
  the four-tensor chapter, pulled OUT per Neil (uid-65/68/69): ⋉/⋊ = Dialectica tensors belong to a later
  `Cont(C≠Set)` chapter, not the core three. Content intact; header carries the subgame-perfection lead and
  a **supersession flag** (its "neither tensor closed" is now refuted — ⋊ IS left/directed-closed, see
  `proofs/2026-07-18-rtimes-left-closed.md`), plus the depaiva89/lnv2405/capucci2024 deep-read TODO.

- `papers/ltimes-rtimes-dialectica-section.tex` (**2026-07-17**, 5pp, compiles clean; standalone, macros
  match `four-monoidal-chapter.tex` for pasting in) — **"The linear-logic tensors: ⋉ and ⋊ as Dialectica
  products."** Identifies DJN's two uninterpreted tensors (arXiv:2305.05655 §6) as the Dialectica tensors:
  ⋉ = de Paiva's multiplicative tensor extended off `Hmg(2)≃Dial(Set)` to all of Poly; ⋊ = its directed
  (triangular, associative-not-symmetric) variant. Payoff: ⋉/⋊ non-convolutional ⇒ **Theorem A does NOT
  exhaust Cont's monoidal structures** (linear-logic tensors sit outside the Day family) — answers Neil's
  "other structures on Set?". **Novelty sweep 2026-07-17 = (C) CLEAR** under the framing rule (identify a
  KNOWN tensor, not "first Dialectica-on-Poly"); neighbours Lucatelli Nunes–Vákár 2405.07724 +
  Capucci et al MFPS 2024 cited & distinguished. Registry `other-cont-monoidal-tensors` [computed].
  Source: `proofs/2026-07-17-ltimes-rtimes-dialectica.md`.
  **✅ INTEGRATED 2026-07-17** as §10 of `four-monoidal-chapter.tex`, then **⏏ RELOCATED OUT 2026-07-19**
  to `papers/dialectica-tensors-deferred.tex` (Neil deferred Dialectica to a later Cont(C) chapter). The
  four-tensor chapter now closes on the census + duoidal (25pp); this standalone remains the older source.
  ⚠️ REMAINING BROWSE-TODO: deep-read + register `depaiva89`, `lnv2405` (title conflict), `capucci2024`
  in sources.json, then drop the pending-verification footnote in the chapter's §Provenance. See
  memory `dialectica-section-integrated-cite-todo` + `for-robin/2026-07-17-dialectica-section-integrated.md`.

- `papers/four-monoidal-chapter.tex` (**2026-07-15**, 24pp; **local — share by email/projects volume,
  no PRs; SUPERSEDES the 07-14 draft**) — **"Four canonical monoidal structures on Cont: the
  classification behind the census, their closures, and how they interact."** The full chapter Neil
  asked for. = the 07-14 draft (Thms A/B⁺/C, ∨_S proper class, negative control) **plus**:
  §Closing — the Dirichlet internal hom [cited N–S Ex 4.78] with a **machine-checked closed monoidal
  category** (`DirichletClosed.lean`, all `rfl`, believed first Dirichlet closure); ◁ right-coclosure
  [cited Meyers, naming clash flagged]; Cont CCC-not-LCC [cited ALS10]; uniform closure formula
  `[p,q]_⋆=∏_I q◁(p[I]⋆y)` graded **[computed]**, converse **[speculative]**. §Interaction — normal
  duoidal (Cont,⊗,◁); **double comonoids = sets of commutative monoids** (Eckmann–Hilton; registry
  `comparitor-comonoid-nogo`=proved; corrects the "degenerate" guess both directions). §1.3 erratum
  now **3 items** (added the "pentagon is trivial"→`rfl`/pre-paid retraction). Sources:
  `proofs/2026-07-14-day-family-classification.md`, `proofs/2026-07-15-comparitor-double-comonoid.md`.
  All cited arXiv sources ≥ deep-read. Robin note: `memory/for-robin/2026-07-15-four-monoidal-chapter-extended.md`.

- `papers/four-monoidal-structures.tex` (**2026-07-14**, 18pp; **SUPERSEDED by the chapter above**)
  — **"The four monoidal structures on Cont: a census, and the classification behind it."**
  The monoidal chapter, rebuilt on the Day spine.
  Contains: the four with explicit associators/unitors (Lean-verified); **Theorem A** (Day
  convolution is an *equivalence* onto the convolutional structures — D1 coproducts in each
  variable, D2 representables closed); **Theorem B⁺** (the product is the UNIQUE pointwise monoidal
  structure on Cont, no Day hypothesis); **Theorem C** (the comparitor ⊗ → ◁ is the counit of a
  coreflection, `p ⊗ − = Lan_J((p ◁ −) ∘ J)`); the ∨_S proper class + negative control; the strict-vs-
  strong erratum in the author's voice. Source proof: `proofs/2026-07-14-day-family-classification.md`.
  **New during writing:** Lemma 2.6 — extension-by-coproducts *is* the left Kan extension along
  `y^(−)`, proved by the comma-category computation (needed because Theorem C applies the adjunction
  to `p ◁ −`, which does NOT preserve coproducts).
  **Not machine-checked:** Theorems A, B⁺, C themselves; ∨_S coherence. → next `/lean` target.
  **Novelty check (full-PDF, 07-14): Thm A SURVIVES** — Niu–Spivak Prop 3.79 states only the FORWARD
  direction; no converse/uniqueness/classification anywhere in the book. ⚠️ But **Ex. 3.82** already
  applies 3.79 to an exotic `A ★ B ≔ A + AB + B`, so **do not claim "a third convolutional tensor"**.

- **⚠️ MISSING ARTIFACT — the top write-up TODO.** The **uniform closure formula**
  (`[p,q]_⋆ = Π_I q ◁ (p[I] ⋆ y)`; exists iff `R ⋆ (−)` is polynomial) is registry-graded `computed`
  **partly because there is no file on disk**. Write it into `proofs/` and it promotes to `proved`.

## Level 0 — GitHub: no write access, BY POLICY (settled 2026-07-14)

- **Robin moved the seed OFF GitHub — it is confidential Kodamai material.** **No push, no clone, no
  PRs.** This is **policy, not breakage**; nothing is blocked on anyone.
- **Work stays local in `~/projects/`. Share with Neil and Robin by EMAIL.**
- PRs #18/#19 were closed **deliberately**; the Lean was **rescued into the local seed. Nothing was
  lost.** (The 5 July stacked-PR orphaning remains a real lesson — **never stack PRs** — but it is
  history, not a live problem.)
- **The book is `git/ghani-containers/books/category-of-containers.tex`, `\author{MacBeth}`.**
  `books/book.tex` is `\author{Robin Langer}` — not mine. ⚠️ **The seed's own
  `PROGRESSIVE_DISCLOSURE.md` states the authorship BACKWARDS. Check `\author{}`, not the map.**
  **Working copy is `projects/books/category-of-containers.tex` (per WRITE.md); edit there, share by email.**
- **★ 2026-07-18 (write session): added Chapter 3 "Which functors are containers?"** to
  `projects/books/category-of-containers.tex` (Neil uid-64 wide-pullback request). Adapted the
  standalone `papers/which-functors-are-containers.tex` into the book: added Neil's terminal-sequence
  motivation hook (final-coalgebra cofiltered limit `1←F1←FF1←⋯`), empty-diagram teaching box,
  position-recovery correction (`F(2)→F(1)` fibre = `2^{P(s)}` powerset, NOT `P(s)`). **Provenance fix:
  products/coproducts downgraded from "[Lean-verified: Cont.lean]" to "[MacBeth]"+footnote — Cont.lean
  is NOT committed to this repo's lean/ tree.** Compiles clean, 29pp, 7 chapters. Placed as Ch3 (after
  the morphism chapter it depends on), completing Neil's "first three chapters." Citation floor for the
  new material: Gambino–Kock 0906.4931 = deep-read ✓. Robin note: `for-robin/2026-07-18-book-chapter3.md`.
- **★ 2026-07-23 (wake): CHAPTERS 1–3 CLOSED (Neil's week-goal).** Audit: book compiles clean at 40pp,
  0 undefined refs, exactly ONE live gap — the Ch3 coequaliser `\prov` TODO (the "expect Abbott's thesis"
  reference). **RESOLVED** by rewording to clean further-work (mechanism already argued in prose:
  quotients add position automorphisms ⟹ analytic/species functors outside ⟦–⟧; dropped the promised
  theorem-number + unverified source, per Neil's no-moonshot discipline). Recompiled clean. Pending only
  Neil's OK that no extra Ch1–3 content is wanted.
- **★★ 2026-07-23 (wake): applications staging note** `memory/for-robin/2026-07-23-ologs-supply-chains-as-directed-containers.md`
  (emailed to Robin) — grant Path-5 spine: ologs/KG/supply-chains are directed containers via the
  lean-verified DCont≃SmallCat hinge; composing them = ZS product `C⋈D`, obstruction `[ω]∈H²` = SAME
  class as orchestration re-entrancy. Greenfield; honest-status table; Neil-gated (applications = next
  week). PROVE trigger = compute a minimal supply-chain ZS instance. → [[applications-are-directed-containers]].
- **NB — registry validate uses `--root .` NOT `--root memory`** (the old flag = ~130 spurious
  source-danglers, a false alarm; sources are live — do NOT prune).
- **★ 2026-07-18 (prove): `proofs/2026-07-18-dialectica-tensors-non-closed.md`** — ⋉/⋊ NOT closed,
  with explicit witness `y²` and the adjoint-functor consequence. Thm 1: ⋉ neither left- nor right-
  closed. Thm 2: ⋊ not right-closed, **BUT `(−)⋊q` preserves binary coproducts** (obstruction is
  one-sided/directed — corrects the companion note's blanket "same computation kills ⋊"). Registry
  child `ltimes-rtimes-non-closed` = proved.
- **★ 2026-07-18 (prove-2): `proofs/2026-07-18-rtimes-left-closed.md`** — resolves the resulting
  Open Question 5: **⋊ IS left-closed.** Explicit right adjoint `(−)⋊q ⊣ [q,−]_⋊` with
  `[q,r]=(Cont(q,r), (a,c)↦S_q×∐_t r[a t])` — internal-hom shape set = external hom `Cont(q,r)`.
  Natural iso proved (bijection + naturality in p), pointwise-adjoint criterion (Mac Lane IV.1),
  verified computationally (2000 hom-card trials; Θ injective on 4096-morphism case; `[y,r]=r`).
  **⋊ = directed-closed** (left yes, right no; closure handedness = tensor handedness). Registry
  child `rtimes-left-closed` = proved. Chapter §10 erratum owed; `/lean` target
  (`Adjunction.mkOfHomEquiv`) — first machine-checked one-sided-closed container structure.
  Collaborator note: `memory/for-collaborator/2026-07-18-rtimes-left-closed.md`.
- **★★ 2026-07-20 (prove, deep-work): `proofs/2026-07-20-orchestration-reentrancy-obstruction-analytic.tex`**
  (6pp PDF) — **PROMOTES orchestration-zs COMPUTED→PROVED** (registry now `status: proved`, validates).
  Analytic proof: parametrize the supervisor–worker category by the token-mutation bit ε∈ℤ/2 (s₂∘p=q·τ^ε),
  verify (L)+(H) for K_ε by hand, apply the *general* (T3) `(G)⟺[ω]=0` (rigid twist was only its example),
  compute Sk_C/presheaf/complex(C³=0⇒H²=(ℤ/2)²/diag)/defect ω_T=(0,ε) directly ⇒ **[ω(K_ε)]=ε·(generator)**
  in H²≅ℤ/2. **Corollary:** C⋈D exists **iff ε=0 iff worker fixes the token**; ε=1 ⇒ nonzero generator =
  unprotected re-entrancy. Kills the machine iso + brute #SFS. Cross-check `scratch/orchestration_zs_parametrized.py`;
  collab note `memory/for-collaborator/2026-07-20-orchestration-reentrancy-obstruction-analytic.md`.
- **★ 2026-07-19 (prove, deep-work): `proofs/2026-07-19-orchestration-zs-instantiation.tex`** (4pp PDF)
  — grounds the **orchestration = Zappa–Szép product** dictionary (SEED Path 5) from speculative to
  **computed** [now superseded on the core dichotomy by the 07-20 analytic proof above; retains the
  illustrative indep→C×D and S₃ regimes]. Supervisor–worker orchestration as a small category (T1 DCont≅Cat);
  composing two = a distributive law K=C⋈D (T2 pairwise-ZS); re-entrancy = (G)-failure = nonzero [ω]∈H²(Sk;Z/2) (T3).
  4-regime machine-checked table: independent→composes (C×D); coherent-nontrivial→composes (S₃=Z/3⋊Z/2,
  non-abelian); locked re-entry→composes (#SFS=2,[ω]=0); **unprotected re-entry→OBSTRUCTED (#SFS=0,
  [ω]=gen Z/2)**. Crux: `K_bug` (worker outcome flips supervisor turn token) ≅ **rigid twist** (explicit
  iso, verified) ⇒ H² transfers. The single bit flipping composable↔obstructed = *worker mutates shared
  supervisor state?* Scripts `scratch/orchestration_zs{,2,3}.py`. Registry `orchestration-zs.json` =
  **computed** (validates). T1–T3 cited, no new cohomology, models = minimal faithful abstractions
  ("named framework IS this" = registry dead-end). Collaborator note:
  `memory/for-collaborator/2026-07-19-orchestration-zs-instantiation.md`.
- **★ 2026-07-20 (write, REVISED 2026-07-21: differentiator landscape completed): `papers/containers-for-orchestration.tex`** (10pp
  PDF, amsart, compiles clean, citation floor = deep-read) — the grant-**Impact** note answering
  Neil's UID-70, **reframed on top of Aberlé (arXiv:2604.01303)** after the 07-21 deep-read. Main
  claim (the surviving delta): composing two shared-resource orchestrations = **Zappa–Szép product
  C⋈D** (not a functor), obstructed by **[ω]∈H²(Sk_C;𝒟)**; unprotected re-entrancy = nonzero gen Z/2;
  degree-axis contrast with MAS sheaf-Laplacian (H⁰/H¹ on *comm* graph vs H² composability on *handoff*
  category). **Now graded PROVED** (§4 follows the analytic proof `2026-07-20-...-analytic.tex`;
  `[ω(K_ε)]=ε·gen`, dichotomy proved; the two extra table regimes stay *computed illustration*;
  #SFS-enumeration and rigid-twist iso demoted to cross-checks). Honesty surgery: interface /
  free-monad-implementation / wiring-diagram-composition / dependent-spec mechanism = **Aberlé's,
  cited prominently** (new prior-art subsection + dictionary rows); H² tower = classical (cited). Banu
  2607.04240 differentiator added (operad parallel-assembly, orthogonal to sequential C⋈D). NB: WRITE
  named ArchAgents 2605.12239 but it's agent-summary — anchored the differentiator on the deep-read
  companion 2607.04240 instead. Handoff: `memory/for-robin/2026-07-20-orchestration-note-revised.md`.
  **07-21 completion:** §4 gained a *categorical-orchestration landscape* subsection + 4-row table
  (Aberlé / Banu / **Waites n-Café** / this note), positioning all three 2026 neighbours; sharp
  contrast = both Waites and we reach for "serialisation" but we characterise *when it is impossible*
  ([ω]=gen, K₁). Waites cited by URL (blog, read-in-full 07-21, not in sources.json — non-arXiv).
  Handoff: `memory/for-robin/2026-07-21-orchestration-paper-completed.md`.
  TODO (not-write): empirical framework instantiation (GA-analogue); Fairbanks 2607.15091 unifier
  (prove); ∞-version.
- **★ 2026-07-21 (lean): `lean/Containers/Containers/Reentrancy.lean`** (sorry-free, wired into root,
  full lib builds 0 warnings) — machine-checks the **finite 𝔽₂ class core** of the orchestration
  theorem. Models `C²=(Z/2)²` as `Bool×Bool` (xor=±), `d1 t=(t,t)`=coboundary `B²`=diag,
  `omega ε=(0,ε)`, class map `phi(a,b)=xor a b`. Key thms: **`phi_omega : phi(omega ε)=ε`**
  (sharp `[ω]=ε`), **`omega_inB2_iff_zero : InB2(omega ε) ↔ ε=0`** (`[ω]=0⟺ε=0⟺C⋈D exists`),
  `phi_ker_eq_inB2` (`ker φ=B²`) + `phi_surjective` (⟹ `H²≅Z/2`). Axioms: only `propext` (two thms),
  rest axiom-free; no Mathlib (pure core, project style). Checks the *finite class computation only*,
  NOT the categorical→complex reduction (stays paper's `proved`). Registry `orchestration-zs.json`:
  new `lean-verified` child `lean-omega-equals-epsilon` under `class-equals-bit`. Handoff:
  `memory/for-collaborator/2026-07-21-lean-reentrancy-obstruction.md`.
- **★ 2026-07-23 (prove): `proofs/2026-07-23-supply-chain-zs.tex`** (computed, 5pp, compiles) +
  `scratch/supply_chain_zs.py` (all claims machine-checked) + registry `supply-chain-zs.json`
  (status computed, validates `--root .`). **Supply-chain composition = Zappa–Szép product**, cloned
  from the proved orchestration template and **generalized Z/2 → Z/n** (inventory = cyclic lot-cursor).
  (A) `procure→manufacture→ship` written out as an explicit **directed container** `(S,P,o,↓,⊕)` with
  D1–D5 machine-checked (new object-level content; orchestration stayed category-level). (B) Warehouse
  family `W_{n,ε}`: `C⋈D` exists ⟺ ε=0 ⟺ routes agree on lot-provenance; `[ω]=ε ∈ H²(Sk_C;Z/n)≅Z/n`
  = quantitative unit-mismatch; `#SFS=n`/`0` cross-check; n=2 = proved orchestration bit (cited).
  (C) `Book→Author→Name` olog merge = same machine, Z/2 naming-convention conflict. **Grade
  discipline:** general theorems cited (proved/lean-verified), instantiation computed, object-level
  fidelity OPEN (SEED Q4). Handoff: `memory/for-collaborator/2026-07-23-supply-chain-zs.md`.

- `lean/Containers/Containers/StateComonad.lean` (2026-07-28) — ΔS state object as codiscrete-category
  directed container (`deltaDC`, D1–D5 all rfl, axiom-free); store comonad (counit/comult + 3 laws);
  Lemma 3.1 `ΔS⊗ΔT=Δ(S×T)` & `Δ1=y` (rfl). Backbone of `proofs/2026-07-28-delta-state-object-and-workers.md`.
- **★ `lean/Containers/Containers/Workers.lean` (2026-07-29)** — the **(Set,×)-graded category of Workers**,
  sorry-free, full library builds zero errors/warnings. `Worker S p q := ContainerMorphism (deltaS S ⊗ p) q`;
  `Worker.comp : Worker S p q → Worker T q r → Worker (S×T) p r` (**state multiplies**, direct coordinates,
  axiom-free); `Worker.id : Worker Unit p p` (grade 1); `Worker.reGrade` (state transport along a grade
  bijection). Three laws `unit_left`/`unit_right`/`assoc` each `ext' rfl` (Quot.sound-only). Promotes
  `state-object-delta.json` T3-core → **lean-verified** (child `lean-worker-composition`). Formalises
  Theorem T3 of `proofs/2026-07-28-delta-state-object-and-workers.md`.
- **★ `lean/Containers/Containers/BiKleisli.lean` (2026-07-29)** — the **biKleisli unit laws** of the
  effect–coeffect arrow calculus, sorry-free, zero warnings, in the root build. Abstract mixed
  distributive law over the Mathlib-free `Category` typeclass: `Comonad`/`Monad`/`MixedDistrib G T`
  (`κ:GT⇒TG`, axioms E1′–E4′ + κ-naturality); arrows `C(Gp,Tq)`, `arrId=ε≫η`, `acomp=δ≫Gf≫κ≫Tg≫μ`.
  **`MixedDistrib.unit_left`(=E1′) + `unit_right`(=E3′)** proved from ONLY the (co)monad unit laws +
  ε/η naturality + the two *unit* κ-axioms — never E2′/E4′ (the Lean witness that the unit laws are the
  unconditional, all-M part; `#print axioms` → NO axioms, pure). Anchors: `SetMonad.toComonad` repackages
  the Lean-verified transfer comonad `G_M` (Quot.sound); `Monad.identity` + `Comonad.coKleisliDistrib`
  give the **T=Id coKleisli** category (Workers/coeffect slice §3.1) with full `coKleisli_acomp_assoc`
  (propext only). Promotes `effect-coeffect-arrows.json` child `lean-bikleisli-unit-laws` →
  **lean-verified** (`lean: MixedDistrib.unit_left`). Formalises the (1)⇒(3) unit-law direction of
  Theorem A of `proofs/2026-07-29-effect-coeffect-arrows.md`.
  **UPDATE 2026-07-30:** added the general abstract **`MixedDistrib.acomp_assoc`** (biKleisli
  associativity from the FULL axiom set E1′–E4′; 7-rewrite chase) — it did not previously exist (the
  docstring's `BiKleisli.assoc` claim was corrected).
- **★ `lean/Containers/Containers/BiKleisliMaybe.lean` (2026-07-30)** — the biKleisli skeleton
  **instantiated end-to-end at `M=Maybe`**, sorry-free, zero warnings, in the root build. `Maybe:SetMonad`;
  the Ahman–Bauer effect monad **`T_Maybe(S,P)=(Option S, P⋆)` as a `Monad Container`** with the degenerate
  arity-≤1 Π (`P⋆(none)=PUnit`, `P⋆(some s)=P s`); the reverse compositor **`κ`** (id on `some`, empty-product
  η-pad `1→Option 1` on `none`); and **ALL FOUR mixed-DL axioms E1′–E4′ discharged for Maybe, incl. E2′**
  (`distrib_mult`, the branching-obstructed one — closes because the Π is over ≤1 leaf) → `mixedDistrib`.
  Composed with the abstract `acomp_assoc` this gives **`arr_unit_left`/`arr_unit_right`/`arr_assoc`** — a
  fully machine-checked **associative** effect–coeffect arrow category for a non-branching effect
  (`arr_assoc` → `[propext, Quot.sound]`). Machine-checks the "Maybe is a genuine category (1536/1536)" half
  of Theorem A. Registry node `bikleisli-maybe-lean` = **lean-verified** (`lean:
  Containers.BiKleisliMaybe.arr_assoc`). Next instance: Writer/ℤ₂ (positive arity-1, non-trivial `A`).
- **★ `lean/Containers/Containers/BiKleisliWriter.lean` (2026-07-30)** — the biKleisli skeleton
  **instantiated at `M=Writer` over an arbitrary monoid** (`Mon`; generalised past the ℤ/2 ask, with
  `Z2`=Bool/xor the concrete instance), the writer generator `A×(−)` of the affine class. `Writer W:SetMonad`;
  **`T_Writer(S,P)=(A×S, P∘π₂)` as a `Monad Container`** (single-fibre Π, arity 1, no nullary leaf); the
  reverse compositor **`κ` is the identity morphism** (`G_W T_W X` defeq `T_W G_W X` — cleaner than Maybe's
  η-padding); **ALL FOUR axioms E1′–E4′ discharged incl. E2′** → `mixedDistrib`. Composed with `acomp_assoc`:
  **`arr_unit_left`/`arr_unit_right`/`arr_assoc`** + concrete **`arr_assoc_Z2`** — a machine-checked
  associative arrow category for the writer generator (`arr_assoc_Z2` → `[propext, Quot.sound]`, sorry-free,
  zero warnings, root build 42 jobs). Only non-rfl step: the 3 monoid-shaped T-monad laws, transport absorbed
  by helper `heq_pos` + `eq_of_heq` (choice-free) — see `for-collaborator/2026-07-30-lean-bikleisli-writer-instance.md`.
  With Maybe (`E+(−)`) the pair now spans both generators `E+A×X` in Lean. Registry node
  `bikleisli-writer-lean` = **lean-verified** (`lean: Containers.BiKleisliWriter.arr_assoc`).
- **★★ `lean/Containers/Containers/BiKleisliAffine.lean` (2026-07-31)** — the biKleisli skeleton
  **instantiated at the WHOLE non-branching class `M X = E + A×X`** (arbitrary monoid `A`, arbitrary
  **left `A`-set** `E`), **fusing** the Maybe and Writer generators into ONE instance. `Aff` bundles
  `(A,E,one,mul,act,+5 laws)`; **`MAff W:SetMonad`** whose `μ` absorbs an outer exception, lets the log
  **act** on an inner exception (`inr(a,inl e')↦inl(a⊙e')` — the genuinely fused line, needs
  `one_act`/`mul_act`), and multiplies two logs; **`T_M(S,P)=(E+A×S, P⋆)` as a `Monad Container`** (a `Sum`
  case-split runs Maybe on `inl`, Writer on `inr`); **`κ`** = `η^M`-padding over `inl` + id over `inr`.
  **ALL FOUR axioms E1′–E4′ discharged incl. E2′** → `mixedDistrib`; **`arr_unit_left/right`, `arr_assoc`**,
  and concrete **`arr_assoc_Z2E2`** (A=Bool/xor, E=Bool, trivial action — the |E|=2,|A|=2 case PROVE.md
  flagged). `arr_assoc` → `[propext, Quot.sound]`, sorry-free, zero warnings, root build 42 jobs.
  Non-rfl beyond Writer's 3 monoid-laws: E1′-unary + E2′-deepest need `cases p` (reduce `M.map id`);
  **E4′ nullary needs `rw [one_mul]`** (Maybe's `rfl` becomes `mul one one = one`). Machine-checks T1+T2 of
  `affine-classification` — the arrow category for the entire classified family. Registry node
  `bikleisli-affine-general` = **lean-verified** (`lean: Containers.BiKleisliAffine.arr_assoc`); note
  `for-collaborator/2026-07-31-lean-bikleisli-affine-general.md`.
- **★★ `lean/Containers/Containers/BranchingObstruction.lean` (2026-07-31)** — the **NEGATIVE witness**
  completing the dichotomy iff in Lean: the ⟸ half (`M` **branching ⟹ `κ` fails E2′**), complementing
  the positive `E+A×X` class above. E2′ (`distrib_mult`) can only fail in the backward POSITION map
  (both sides act by `μ^M` on shapes); at a branching leaf it reads "**`κ` commutes with `μ`**":
  `ρ(A₁∪A₂)(B₁∪B₂) = ρA₁B₁ ∪ ρA₂B₂` (ρ = cartesian product-comparison, μ = union) — and it **FAILS** at
  off-diagonal `(0,1)`: product-of-unions (full 2×2) ⊋ union-of-products (diagonal). `Pf` modelled
  Mathlib-free by **characteristic functions** `Pf T := T→Bool` (= covariant powerset over a Fintype).
  Three decls, **NO axioms** (pure kernel `decide`): `kappa_distrib_mult_fails`,
  `kappa_not_distributive_over_union`, and the non-branching mirror `oneLeaf_E2_holds` (arity-≤1 leaf →
  κ=id → E2′ by `rfl`). **SCOPE (honest):** this is the position-FIBRE content, NOT the full
  container-level `distrib_mult` inequality (needs Pf as Cont-monad = Finset, unavailable Mathlib-free);
  full-morphism non-associativity stays computed-only (`bikleisli-pf-nonassoc`). Pf > `1+X²`: Pf is the
  minimal branching monad whose Ahman–Bauer `T_M` exists (idempotent+comm μ ⇒ distinct leaf labels ⇒
  `μ^T` well-defined). Root build 43 jobs, zero warnings. Registry node `branching-obstruction-lean` =
  **lean-verified** (`lean: Containers.BranchingObstruction.kappa_distrib_mult_fails`); note
  `for-collaborator/2026-07-31-lean-branching-obstruction.md`.

- **★★ `lean/Containers/Containers/AffineClassification.lean` (2026-08-04)** — the **POSITIVE classification**
  machine-checked: **Theorem T1 (Set-monad level)** of `2026-07-30-affine-classification.md`. A monad on the
  functor `M X = E + A×X` is *the same data* as a **monoid `⊗` on `N = E ⊔ A`** with unit in `A` and `E` a
  **two-sided ideal of left zeros**. Faithful Lean port of the Python harness `affine_classify.py`: for each
  small size `(|E|,|A|)` enumerate **every** candidate datum `(unit, σ, γ)` and machine-check
  `monad-laws ⟺ monoid-laws`, **0 mismatches** — the exact bijection. `MEl`/`Tbl` model the finite data with
  `Fin`/`List`/`Sum`; `mu` reads μ off the table (outer exc = left zero, `σ:A×E→E`, `γ:A×A→E⊔A` carries the
  leaf iff it lands in `A`). Kernel-`decide` theorems `bijection_0_1 … bijection_1_2` are **axiom-free**
  (`propext` only) and cover **every** paper example: `Maybe` (1,1), exception `E+(−)` (2,1), four 2-element
  monoids incl. writer ℤ₂ (0,2), and the **aborting nilpotent `1+2×X`** (`z²=0∈E`) at (1,2) — the
  non-cartesian counterexample. `bijection_2_2` (8192 cands) via `native_decide` (`Lean.ofReduceBool`).
  Prop-level `classification_1_1/_1_2/_2_2` extract the iff; named anchor witnesses `maybeTbl`, `writerZ2Tbl`,
  `abortingTbl` tie the abstract bijection to the running examples. SCOPE: the Set-monad↔monoid bijection of
  §2 only (matches `affine_classify.py`); the cartesian bifurcation (§2.3, `affine_e2prime.py`) is a separate
  check, out of scope. Root build 44 jobs, zero warnings. Registry node `affine-monad-monoid-bijection` =
  **lean-verified** (`lean: Containers.AffineClassification.classification_1_1`); note
  `for-collaborator/2026-08-04-lean-affine-classification.md`.

- **★★ `lean/Containers/Containers/TMCartesianBoundary.lean` (2026-08-05)** — the **`T_M`-side boundary**
  of cartesian preservation, companion to `FibredTransfer.lean` (the G_M side, `onMor_cartesian` ∀M).
  Machine-checks "`T_M` preserves cartesian ⟺ `M` cartesian" at the Maybe/Pf boundary (Thm 1,
  `2026-08-05-crown-gap-closure.md`). **POSITIVE:** `TMaybe_onMor_cartesian : IsCartesian φ → IsCartesian
  (Tmap φ)` — *fully general* (NO axioms), the T_M-mirror of `onMor_cartesian`, valid since Maybe's leaf
  map is always bijective (cartFun); reuses `IsCartesian`/`TwoSidedInverse` (FibredTransfer) + `Tmap`/`TObj`
  (BiKleisliMaybe). **NEGATIVE (`PfWitness`):** merging `u:{a,a'}→{c}`, shape `m={a,a'}`; `ustar_merges`
  (leaf map u_* **non-injective**), `ustar_surjective` (Pf drops no leaf), `fstar_injective` +
  `fstar_not_surjective` (induced product map = diagonal Bool→Bool², injective-not-surjective),
  `TPf_fails_cartesian_preservation`. **HONESTY FIX (propagate to book/paper):** LEAN.md's "T_Pf backward
  map not injective" is imprecise — the *leaf* map is non-injective; the *product* map fails **surjectivity**
  (reindexing lemma), proved both halves. Root build 46 jobs, zero warnings, [Quot.sound]/decide only, no
  sorry. Registry `monad-comonad-transfer.json` child `lean-tm-cartesian-boundary` = **lean-verified**
  (`lean: Containers.TMaybe_onMor_cartesian`); note `for-collaborator/2026-08-05-tm-cartesian-boundary-lean.md`.
- **★★ `lean/Containers/Containers/ReaderStateOutsidePiMendler.lean` (2026-08-06)** — the **DROP rung** of
  the non-cartesian-μ trichotomy, machine-checking the finite core of `2026-08-06-state-reader-ladder-census.md`
  (PROVE-refutation: Reader/State are **NOT** ∏-Mendler). Certifies the pointwise Lemma-1 `κ_μ`-totality
  criterion `ReaderKappaTotal G := ∀ i:Bool×Bool, ∃ e:Bool, G e e = G i.1 i.2` (μ=diagonal) and its failure:
  `reader_kappa_not_total` for `Gw=![![0,0],![1,0]]` (off-diagonal token `(true,false)` label `l1` matched by
  no diagonal leaf — all `l0` — `reader_diagonal_drops`) ⟹ no total `κ_μ` ⟹ no `j` ⟹ Reader ∉ ∏-Mendler;
  `state_kappa_not_total`/`state_threading_drops` the same for State (`S=Bool`, threading drops inner token
  `(false,true)` label `l2`); `reader_kappa_total_of_const` the honest non-vacuity (constant `G` IS total, so
  the failure is label-specific per census §2). Bundle `reader_state_outside_pi_mendler`. **Axiom-free** (all
  six theorems, `#print axioms` = none) via a bespoke 3-elt `Lbl` (`deriving DecidableEq`, ≅ Fin 3) that keeps
  `decide` off `Fin`'s propext route. Root build 47 jobs, zero warnings, no sorry. Completes the boundary
  trichotomy in Lean: cartesian (Maybe) + MERGE (Pf, INSIDE) [`TMCartesianBoundary`] + **DROP (Reader/State,
  OUTSIDE)** [here]; SYMMETRY (Bag) still paper-only. Registry `effect-coeffect-arrows.json` child
  `reader-state-drop-lean` = **lean-verified** (`lean:
  Containers.ReaderStateOutsidePiMendler.reader_state_outside_pi_mendler`); note
  `for-collaborator/2026-08-06-lean-reader-state-drop.md`.
- **★★ `lean/Containers/Containers/ActionLifting.lean` (2026-08-08)** — the **`A`-action rung** (P2 of
  `2026-08-08-A-E-predicate-liftings.md`, Neil UID-94): the `All`/`∏` predicate lifting `Container.actionAll`
  is a **left action of the `◁`-monoidal `(Cont,◁,I)` on `Cont`**. `actionAll X Y` shares `X◁Y`'s shapes;
  positions at `(s,g)` are the dependent function `(p:X.Pos s)→Y.Pos(g p)` — `∏` where `Container.seq` (`◁`)
  has `Σ`. **`Container.actionAll_assoc : ContainerIso (X.actionAll (Y.actionAll C)) ((X◁Y).actionAll C)`** —
  shapes = the `◁`-associator currying, positions = dependent-`∏` **Fubini** `∏_p∏_q≅∏_{(p,q)}` (curry/uncurry),
  transport-free (`cases`+`rfl`, the `associator` pattern); `#print axioms` = only `Quot.sound` (funext via
  `ext'`). Plus `actionAll_unit : A I C≅C` (Unit-collapse, **axiom-free**) and `actionAll_snd`(+`_id`/`_comp`):
  2nd-argument functoriality for **every** morphism (axiom-free `rfl`) — the positive half of the P1 asymmetry;
  the *first* argument needs cartesian morphisms, already Lean'd `T_M`-lifts-⟺-cartesian in `TMCartesianBoundary`.
  **Honesty:** stated as `ContainerIso` NOT `=` — the two shape sets are curried/uncurried nested `Σ`s,
  bijective not defeq (exactly why `◁`'s associator is an iso); the encoding-to-`rfl` question is the same one
  the paper §7 flagged, not a math gap. Root build 48 jobs, zero warnings, no sorry. Registry
  `effect-coeffect-arrows.json` node `A-module-action-fubini` = **lean-verified** (`lean:
  Containers.Container.actionAll_assoc`); note `for-collaborator/2026-08-08-lean-action-lifting.md`.

- **★★ `for-collaborator/2026-08-05-monad-lift-stratification.md` (2026-08-05, WRITE session)** — the
  **grant-narrative note** for the four-level stratification of Set-monads by how much structure survives
  the lift to `p:Cont→Set`: **pure writer `A×(−)` ⊊ writer+exception `E+A×(−)` ⊊ cartesian ⊊ polynomial**,
  detected by strict-BC (`λ` inv) / arrows-compose (reverse `κ`) / no-leaf-merge (`T_M` preserves cartesian)
  / has-support (`T_M` defined), witnessed by Id·Writer / Maybe·Exc / List / Pf. Frames the result as a
  **Theory-pillar contribution** (computable container-native refinement of "cartesian monad") for a
  monad-literate, fibration-naive grant reader; leads with the result, then the honest **refuted-TFAE**
  arc (`List`, `Maybe` as the two splitters). Drop-in block quote at top for the grant's "taxonomy of
  composable effects" section. Cites `2026-08-05-cartesian-preservation-nonbranching.md`,
  `2026-08-05-crown-gap-closure.md`, `effect-coeffect-arrows`, `affine-classification`,
  `FibredTransfer.lean`; external floor = **deep-read** (Ahman–Bauer 2409.17664). Robin pointer:
  `memory/for-robin/2026-08-05-monad-lift-stratification-grant-note.md`. Does NOT touch the book (aside
  awaits Neil).

- **★★ `lean/Containers/Containers/ReaderGroupoidLifting.lean` (2026-08-10)** — the **ℤ/2 groupoid**:
  the load-bearing witness of `reader-liftings-are-categories` that Reader's ∏/Σ/mix partition is FALSE.
  Built the honest way (crown Step E: monad lifting = per-leaf polynomial comonad = small category) as a
  `DirectedContainer` — `Shape=Unit` (one object), `Pos=Z2` (hom-set ℤ/2), `root=e`, `shift=Z2.mul`
  (composition); `Ext ≅ X²` = aggregator `L(B)=B^{ℤ/2}`. **The three comonad laws (inherited from
  `Directed.lean`) ARE the three ℤ/2 group axioms** — left counit⟸D1&D2=left-id, right counit⟸D3=right-id,
  coassoc⟸D4&D5=assoc; `Z2` hand-rolled ⟹ all `rfl` after `cases`, axiom-free. **Not Σ**
  (`readerGroupoid_not_sigma`: non-discrete — `g≠e`, `g·g=e`, vs discrete `deltaDC Unit` subsingleton hom).
  **Not ∏** (`readerGroupoid_not_pi`: reuses `reader_kappa_not_total` — `T_Reader` has no μ, `L` does).
  Bundle `reader_groupoid_is_neither_pi_nor_sigma` **axiom-free**; comonad-law wrappers use only `Quot.sound`
  (funext). Root build 50 jobs, zero warnings, no sorry. Registry `effect-coeffect-arrows.json` node
  `reader-groupoid-lifting-lean` = **lean-verified** (`lean:
  Containers.ReaderGroupoid.reader_groupoid_is_neither_pi_nor_sigma`); note
  `for-collaborator/2026-08-10-lean-reader-groupoid-lifting.md`. Scope: comonad=category face only; the
  monad-on-`Cont` is its fibrewise-op dual (documented); general-E is the paper result (open).

- **★★ `lean/Containers/Containers/StateProductLifting.lean` (2026-08-11)** — the **SOUND half** of
  *State liftings ≅ Cat* (`state-liftings-holonomy-triviality`): every small category `C ↦ 𝕊×C` is a State
  lifting. **`DirectedContainer.prod C D`** = the **product category** under DCont≅Cat: `Shape=C.Shape×D.Shape`,
  fibre = the **product** `C.Pos s × D.Pos t` (deliberately NOT `Cont.Container.prod`'s *coproduct* fibre
  `P s⊕Q t`, the Poly categorical product — different UP), `root/sub/shift` componentwise, D1–D5 hold,
  **axiom-free**. The dependent core is one lemma **`transport_prod`** (transport over `fun w=>F w.1×G w.2`
  factors componentwise, `cases h; rfl`, **axiom-free**) discharging the D2-along-D1 and D5-along-D4 transports.
  Concrete **`stateProduct=(deltaDC Bool).prod readerGroupoidLifting`** = `ΔBool×ℤ/2` (reuses the groupoid file
  as the `C` factor and `StateComonad.deltaDC` as `𝕊`); comonad laws inherited. **Distinguishing invariant:**
  `deltaDC_connected` — `ΔS` codiscrete, `∀s s' ∃p, sub s p=s'` (single shape-orbit `π₀(𝕊)=1`) vs Reader
  `π₀=|E|`; `stateProduct_state_connected`. Packaged `stateProduct_is_sound_state_lifting` (3 laws + orbit),
  footprint only `Quot.sound` (funext). Root build 51 jobs, zero warnings, no sorry. **Lean gotcha recorded:**
  never hand-write `h ▸ (x,y)` into `F a'×G b'` (motive undiscoverable, pair absent) — state the transport lemma
  over whole-pair vars via projections, route field proofs through `rw [transport_prod]`. **Not `lean-verified`
  in registry** (no JSON node yet covers state-liftings-≅-Cat; suggest `state-liftings-cat.json` w/
  `sound-embedding` child); ONTO/completeness is PROVE, deliberately unformalised. Note
  `for-collaborator/2026-08-11-lean-state-product-lifting.md`.
- **★★ `lean/Containers/Containers/EndpointLocality.lean` (2026-08-11)** — the **reusable COLLAPSE ENGINE**
  of the liftings-≅-Cat completeness proofs: *a functor out of the codiscrete category is a trivial
  iso-system*. `Codiscrete S` = chaotic cat (`Hom a b:=PUnit`, all `SmallCat` laws by `PUnit` **eta**=`rfl`);
  added local `SmallCat.Iso`/`SmallCat.Functor` (were absent). For any `F : Functor (Codiscrete S) C`:
  (1) `mapIso`/`mapIso_hom_eq` — every morphism ↦ iso, forward map literally `F.map f`;
  (2) `endpointIso_refl` (`ι a a=C.id`) + `endpointIso_comp` (`ι a b⬝ι b c=ι a c`) — coherent trivial-holonomy
  datum; (3) `collapse` — every `F.obj a≅F.obj a₀`, `π₀(K(S))=1`. Each proof = `map_comp.symm.trans map_id`;
  **AXIOM-FREE** (no `propext`/`Classical` either). `example` at `S=Bool` connects to `stateProduct=ΔBool×ℤ/2`.
  Registry: fresh **`proofs/registry/holonomy-triviality.json`**, 4 nodes `lean-verified`, validator green.
  Scope: abstract skeleton only; ASSOC-DEEP⟹endpoint-locality derivation stays informal. Root build green,
  0 warnings, 0 sorry. Note `for-collaborator/2026-08-11-lean-endpoint-locality.md`.
- **★★ `lean/Containers/Containers/EmergentHolonomy.lean` (2026-08-13)** — the **emergent-holonomy witness**:
  composing two trivial-isotropy agents synthesises `C₂` holonomy (the machine-checked heart of the 08-12
  bridge part (b)-refutation). Hand-rolled `S₃` (6 ctors) acting on `X={1,2,3}`; `mul` **certified = point-action
  composition** by `act_mul` (108 rfl) — so it is genuinely the symmetric group, not an arbitrary magma.
  Exact ZS factorisation `S₃=P·P'` (`P=A₃={e,r,r2}`, `P'={e,a=(12)}`): `P_inter_P'_trivial`, `factor_exists`,
  `factor_unique` (36-pair bash). Stabilisers at `1`: `stab_P_trivial`/`stab_P'_trivial` (both `{e}`),
  `stab_G_eq`/`stab_G_two_elements` (`Stab_G(1)={e,c}=⟨(23)⟩≅C₂`). Payoff `emergent_holonomy`: strict inclusion
  `Stab_P(1)⋈Stab_{P'}(1)={e} ⊊ Stab_G(1)`; `emergent_element_factorisation`: `c=(23)=r2·a` with **neither
  factor fixing 1** — holonomy created by interaction, not inherited. **AXIOM-FREE** — `#print axioms` = NONE
  on all key decls (no `Classical`, no `propext`, no `Quot.sound`). Third file of the bridge Lean story with
  `HolonomyWitness` (single-agent holonomy exists) + `EndpointLocality` (collapse). Registry
  `holonomy-composition-zs-bridge.json` node `emergent-holonomy-witness-lean` **lean-verified**, validator green.
  Root build green (54 jobs), 0 warnings, 0 sorry.
- **★★ `lean/Containers/Containers/Disjointness.lean` (2026-08-14)** — the **Disjointness Lemma in FULL
  generality**, the first *general* (non-witness) step of the ZS-bridge machine-checked. For an internal
  exact factorisation `G=P·Q` (subgroups, `P∩Q={e}`, every `g=p·q`) and **every** `g`:
  `P ∩ gQg⁻¹ = {e}` (`disjointness`; clean set form `disjointness_iff`). Forces every `(A,B)`-double
  coset in `U=Stab_G(s)` to uniform size `|A||B|`, so `h(s)=|U|/(|A||B|)=#(A\U/B)` is an honest positive
  integer — the backbone of `2026-08-13-emergent-holonomy-meeting-points.md` Lemma 1 + Cor 1.1. Where
  `EmergentHolonomy.lean` Lean'd only the `S₃` witness, this proves the **arbitrary-group** statement:
  no finiteness, no action, no fixed point. **Mathlib-free** (project convention): hand-rolls
  `class Group` (assoc/one/inv laws) + `structure Subgroup` (mem predicate closed under `1,*,⁻¹`), with
  derived `mul_inv_rev`/cancel simp lemmas. Crux `conj_pivot` (`p⁻¹((pq)z(pq)⁻¹)p=qzq⁻¹`, closes by
  `simp only` right-associate + cancel adjacent inverse pairs) and `pivot_recover`; the pivot `p⁻¹·a·p`
  lands in both `P` (closure) and `Q` (via `conj_pivot`), so `∈P∩Q={e}⟹=1⟹a=1`. Sorry-free,
  `#print axioms` = `[propext]` only. Registry `disjointness-lemma` node `proved→lean-verified`
  (`lean: Containers.Disjointness.disjointness`). Mathlib port (`Subgroup`/`IsComplement`/`Doset`)
  transfers line-for-line; general enough to be a Mathlib contribution. Gotcha logged: `set` is a
  Mathlib tactic, not core. Root build green (55 jobs), 0 warnings, 0 sorry. Note
  `for-collaborator/2026-08-14-lean-disjointness-lemma.md`.
