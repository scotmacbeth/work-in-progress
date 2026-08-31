> Archived July 2026 daily blocks, moved verbatim out of SUMMARY.md on 2026-08-10 (housekeeping). Chronology also lives in dream-journal/; index in MEMORY.md.

## 2026-07-31 (lean) — NEGATIVE witness machine-checked: branching κ fails E2′ (⟸ half of the dichotomy)
- **★★ `lean/Containers/Containers/BranchingObstruction.lean`** ([[lean-branching-obstruction-negative-witness]]).
  Lean previously owned only the **⟹** half (positive class `E+A×X`, `BiKleisliAffine`, all four axioms).
  This adds the **⟸** half: for a *branching* `M`, `κ` **fails E2′** (`kappa_distrib_mult_fails`,
  axiom-free kernel `decide`). E2′ can only fail in the backward POSITION map (both sides act by μ^M on
  shapes); at a branching leaf it reads "**κ commutes with μ**" `ρ(A₁∪A₂)(B₁∪B₂)=ρA₁B₁∪ρA₂B₂` and FAILS
  (product-of-unions ⊋ union-of-products). Pf modelled Mathlib-free by char-functions `T→Bool`.
  **SCOPE:** fibre-level, NOT full container `distrib_mult` (needs Finset); full-morphism non-assoc stays
  computed-only. Registry `branching-obstruction-lean`=lean-verified; note `for-collaborator/2026-07-31-lean-branching-obstruction.md`.

## 💤 2026-07-31 (dream) — the branching obstruction IS Atkey's index; the arity axis is provably uncrowded
- Consolidates the 07-31 pipeline (WAKE scoop-checks cleared + venue asked / PROVE pairwise
  independence + Thm C + Lemma A / LEAN whole `E+A×X` class fused / WRITE paper started / BROWSE
  graded-monad neighbourhood). Math already banked below; dream extracted the connection + a lead.
- **★★ CROWN — the branching obstruction = Atkey's index-collapse** ([[branching-obstruction-is-atkeys-index]]).
  Atkey ENTCS 229 (2011, deep-read via n-Café Burrito post) proved "Arrows = Freyd categories" FALSE:
  Arrows ≅ *closed indexed* Freyd cats, the extra generality = a second (comonad-structured) input; his
  BiKleisli Arrow `Ar(x,y)=[Wx→Ty]` from `λ:WT→TW` is **verbatim** my `Arr_M(p,q)=Cont(G_M p,T_M q)`.
  So "M non-branching ⟺ `Arr_M` is a genuine (non-indexed) Freyd category" IS Atkey's index-collapse —
  a sharper paper statement, locating the obstruction in a named 20-yr landscape. My Atkey+Uustalu–Vene
  cites verified correct (zero scoop risk; browse *strengthened* the attribution).
- **★★ The arity axis is UNCROWDED — 3 independent 07-31 corroborations.** Field is building graded/Freyd
  machinery along OTHER axes: Earnshaw–Nester–Román 2603.16375 (cartesian PCM-graded ≅ Freyd, Thm 4.23,
  effects-only); Breuvart–Long–Zamdzhiev 2602.09780 (graded-monad *centre* = commutativity); Vollmer–
  Paviotti–Orchard CT2026 (general 2-cat DL machine). NONE touch arity/branching ⟹ today's pairwise-
  independence PROVE publishes clean, arity is genuinely MacBeth's. → topic `distributive-law-landscape.md`.
- **★ LOAD-BEARING LEAD — Vollmer–Paviotti–Orchard "On the Category of Graded Monads" (CT2026, not yet
  arXiv).** `Gmd(I,κ)=[BI^op,κ]_lax`, graded monad on 2Cat; graded-monad/comonad DLs as instances — **may
  subsume the hand-computed `κ:GT⇒TG` per-instance.** WATCH for arXiv; full-text read owed. No registry
  changes; no demotions. Day: `dream-journal/2026-07-31.md`.

## 2026-07-31 (lean) — the WHOLE non-branching class `E+A×X` arrow category, machine-checked (Maybe+Writer FUSED)
- **LEAN-VERIFIED** (`lean/Containers/Containers/BiKleisliAffine.lean`; registry node
  `bikleisli-affine-general` under `effect-coeffect-arrows.json`, `lean-verified`). The abstract biKleisli
  skeleton instantiated at the **entire** cartesian non-branching class **`M X = E + A×X`** — arbitrary
  monoid `A`, arbitrary **left `A`-set** `E` — **fusing the Maybe (`E+(−)`) and Writer (`A×(−)`) generators
  into one instance**. `Aff` bundles the monoid+action datum; `MAff W:SetMonad`'s `μ` absorbs an outer
  exception, **lets the log act on an inner exception** (`inr(a,inl e')↦inl(a⊙e')`, the genuinely fused
  line — needs `one_act`/`mul_act`), and multiplies two logs. `T_M(S,P)=(E+A×S,P⋆)` a `Monad Container`
  (Sum split: Maybe on `inl`, Writer on `inr`); `κ` = `η^M`-pad over `inl` + id over `inr`. **All four
  E1′–E4′ incl. E2′** ⟹ `arr_unit_left/right`, `arr_assoc`, + concrete `arr_assoc_Z2E2` (A=Bool/xor,
  E=Bool, trivial action — the |E|=2,|A|=2 case PROVE.md flagged). Axioms: `arr_assoc` `[propext,Quot.sound]`,
  `mixedDistrib` `[Quot.sound]`, **no sorryAx/Choice**; whole lib green (42 jobs), zero warnings.
- **Machine-checks T1+T2 of `affine-classification`** — the arrow category exists for the *whole* classified
  family, subsuming Maybe (`A=1`) + Writer (`E=∅`). Non-rfl beyond Writer's 3 monoid-laws: **E1′-unary +
  E2′-deepest** need `cases p` to reduce `M.map id`; **E4′ nullary needs `rw [one_mul]`** (Maybe's trivial
  monoid made this `rfl`; here `μ^M` multiplies `one·one`). Note
  `for-collaborator/2026-07-31-lean-bikleisli-affine-general.md`. See [[lean-bikleisli-affine-general-done]].
  ⟹ **all three LEAN increments of the effects⊗coeffects arc now done** (Maybe → Writer → fused class).

## 2026-07-31 (wake) — daily sent; inbox clean; two scoop-checks CLEARED; triggers reset toward the paper
- **Morning daily to Neil SENT** (CC Robin): 07-30 recap (Workers type hierarchy classified + Writer/ℤ₂
  arrow category Lean'd ⟹ **three-modes crown fully closed** across prove/lean/write; T1-originality firmed
  = non-branching provably ≠ commutativity/affineness); today = **start the standalone effects⊗coeffects
  paper**; flagged the Weihrauch frontier lead; asked Neil for a **target venue**. **Inbox EMPTY** (latest =
  Neil UID 82, 07-30, already processed — no new steer).
- **★ Both pre-paper scoop-checks RE-CONFIRMED CLEAR (finer WebFetch read).** **Goncharov 2602.18295**
  ("Higher-Order Bialgebraic Denotational Semantics", ICFP 2026) = **ORTHOGONAL** (behaviour-bifunctor
  locally-final coalgebras; no coeffect comonad, no containers, no mixed DL — shares only "bialgebraic"/PT
  lineage). **Dumas–Duval–Reynaud 1310.0605** = **NEIGHBOUR** (cite): dual monad/comonad *proof-patterns*
  via Kleisli/coKleisli adjunction, NOT a mixed DL, no containers. Drop-in cite sentence banked in
  [[effects-coeffects-scoop-checks-cleared]] and `state/WRITE.md`. ⟹ paper novelty is safe.
- **Triggers reset** (07-30's PROVE=Workers-hierarchy + LEAN=Writer/ℤ₂ both ran & are done; WRITE=standalone
  paper still pending, kept):
  - **WRITE** = **start the standalone effects-and-coeffects paper** (`papers/effects-coeffects-containers.tex`),
    Neil-endorsed; lead with the λ/bialgebra face (all M), arrow face (non-branching) as the affine-fragment
    bonus; scoop-cites folded in. Reuse book Ch8.
  - **PROVE** = the **branching × commutativity 2×2 independence** proposition (paper-hardening: prove
    non-branching ⊥ commutativity ⊥ affineness, one witnessed monad per cell; the one owed computation =
    `A×(−)` over a non-comm monoid is a non-commutative monad). Registers `branching-commutativity-independent`.
  - **LEAN** = the **general non-branching arrow category `M := E+A×(−)`** (fuse Maybe + Writer generators
    into the whole classified family, machine-checked); registers `bikleisli-affine-general`.

## 2026-07-31 (prove) — non-branching ⊥ commutative ⊥ affine, PAIRWISE INDEPENDENT (paper-hardening DONE)
- **PROVED + machine-verified** (`proofs/2026-07-31-branching-commutativity-affine-independence.md`;
  registry node `branching-commutativity-independent` = **proved**, validates). The standalone paper's
  "Related conditions" novelty remark is now a clean Proposition: **P1 non-branching**, **P2 commutative**
  (Kock), **P3 affine** (`M1≅1`) are **pairwise logically independent** — all three 2×2 faces realised.
- **Sharper than the ask (2 bonuses):** (i) **Theorem C** — the cube's *only* hole is
  `non-branching ∧ affine ⟹ commutative` (= `Id` or constant-`1`), i.e. **non-commutative affine ⟹
  branching**; so pairwise- but not jointly-independent, and the lone implication points the "wrong way"
  for expressing non-branching. (ii) **Lemma A** — the full commutativity criterion for the class:
  `E+A×X` comm ⟺ `A` comm ∧ `|E|≤1` ∧ trivial action = **three independent non-comm sources** (writer /
  exception "which-error-wins" / action); exhaustive sweep of all 73 structures, 0 mismatches.
- **Load-bearing owed computation DONE:** Writer over non-comm `N₃` is non-comm as a monad
  (`Ψ=(a·b,·)≠(b·a,·)=Φ`). ⚠ Banked caution: left-zero band is non-comm as an *algebra* but its monad is
  *commutative* (it's **medial**) — monad-non-commutativity = **medial-law failure**, not `a*b≠b*a`.
- Witnesses: Id / Maybe / Writer-N₃ (+exc `2+(−)`) / `P⁺`,`𝒟` / `Pf` / idempotent-magma / free-magma.
  Magma non-comm via Lemma B (Kock: comm monad ⟹ ops are homs ⟹ `*` medial; exhibited medial-violating
  models). Harnesses `scratch/branching-commutativity/`. See [[branching-commutativity-affine-independent]].

## 2026-07-30 (lean) — Writer/ℤ₂ biKleisli arrow category, machine-checked
- **LEAN-VERIFIED** (`lean/Containers/Containers/BiKleisliWriter.lean`; registry node
  `bikleisli-writer-lean` under `effect-coeffect-arrows.json`, `lean-verified`). Second concrete
  instance of the abstract biKleisli skeleton after Maybe: **M := Writer over an arbitrary monoid**
  (generalised past the ℤ/2 ask; `Z2`=Bool/xor is an instance, `arr_assoc_Z2` the concrete witness).
  All four mixed-DL axioms E1′–E4′ discharged (incl. E2′) ⟹ machine-checked *associative* arrow
  category. With Maybe (`E+(−)`) the pair now spans the two generators `E+A×X` of the affine class,
  both in Lean. **κ is literally the identity morphism** (no nullary leaf ⟹ `G_W T_W X` defeq
  `T_W G_W X`; cleaner than Maybe's `η`-padding). Only non-rfl step: the 3 monoid-shaped T-monad
  laws — shape map rearranges `mul`, so ext' transport is non-`rfl`; absorbed by helper
  `heq_pos : HEq (h ▸ p) p` (subst) + `eq_of_heq` (choice-free). `arr_assoc_Z2` deps
  `[propext, Quot.sound]`; whole lib green (42 jobs), zero warnings. Note
  `for-collaborator/2026-07-30-lean-bikleisli-writer-instance.md` (documents the transport pattern
  for future effect-monad instances). NEXT Lean: general affine `E+A×X` (both generators fused).

## 2026-07-30 (prove) — Workers type hierarchy classified (Neil's 07-30 Q)
- **PROVED** (`proofs/2026-07-30-workers-type-hierarchy.md`; registry `workers-type-hierarchy.json`,
  validates). Which of Cont's 4 monoidal (◁,⊗,×,+) + 3 closed structures descend to graded Workers
  `Cont(ΔS⊗p,q)`. **Framework A (grade-mult/Para): ALL FOUR descend** — ⊗ **STRONG**, ×/+ **OPLAX**
  (PROVED via cartesian/cocontinuous), ◁ oplax (COMPUTED, interchange 256). **Framework B (shared
  register): ⊗,◁ need a MONOID on state S** (PROVED ⊗ via Comon(Cont,⊗)≅Fam(Mon^op); S=∅ killer);
  +/× free. **Closed: Workers is ⊗-CLOSED** hom=[p,q]_⊗ (PROVED); ×/◁ obstructed (state entangles).
  **★ Crown:** collapse S×S→S needs monoid IFF object-tensor MERGES operands' positions (⊗,◁) vs
  SEPARATES (+,×); same fault line for closure. State-mode obstruction pinned = monoid-on-register,
  beside directed=[ω]∈H², effect-coeffect=branching κ/λ. Code `scratch/workers-type-hierarchy/` green.
  Note `for-collaborator/2026-07-30-workers-type-hierarchy.md`. NEXT: book Ch4 §, Lean A1+C1 (defeq).

## 💤 2026-07-30 (dream) — MODE 3 FINISHED end-to-end; its "non-branching" condition is provably ORIGINAL
- Consolidates the 07-30 pipeline (WAKE finish-arrows / PROVE affine-classification T1+T2 / LEAN
  BiKleisliMaybe / WRITE three-modes into book Ch8 / BROWSE T1-orthogonality + Weihrauch). All banked
  below; dream extracted the two connections + a frontier lead.
- **★★ CROWN — the three-modes crown's row 3 (effect–coeffect) is now CLOSED across prove/lean/write.**
  It was the only mode with an unnamed obstruction; today it gains a NAMED positive class
  (**writer-with-absorbing-exceptions `E+A×(−)`**), a closed E2′ gap, a machine-checked *associative*
  arrow category (Maybe, `BiKleisliMaybe.lean`), and a book §. Rows 1 (ZS/H²) + 2 (Workers) already
  closed ⟹ the three-modes table is now fully load-bearing grant-Path-5 prose. → [[three-modes-of-composition]].
- **★★ T1 ORIGINALITY FIRMED — grant novelty sharpened.** Three independent full searches confirm
  "non-branching" (arity ≤1) is **orthogonal** to all three named classical conditions, NOT a
  restatement: commutativity (Power-Robinson 1997), affine + strongly-affine (Jacobs CMCS 2016).
  Clinching witnesses: `Pf` commutative∧BRANCHING; `E+(−)` non-branching∧noncommutative(|E|>1);
  𝒟/Giry/expectation affine∧BRANCHING. ⟹ non-branching ⟺ `E+A×(−)` is MacBeth's OWN contribution,
  scoop-hunt closed; free 2×2 (branching×commutative) table for the paper. **Naming:** use "arity-≤1 /
  width-1 polynomial monad", NOT "affine" (nLab-taken, opposite) nor "monad with arities" (BMW =
  accessibility). → [[affine-classification-writer-exceptions]].
- **★ NEW FRONTIER LEAD — Weihrauch problems as containers** (Pradic–Price arXiv:2501.17250, deep-read):
  ◁ = Weihrauch `⋆`; their weakly-LCC base shows where MY LCC hypothesis bites; their "∂p ↔ ?" row LEFT
  OPEN = unclaimed connection to [[container-chain-rule-proved]]. A computable-analysis applications
  angle for the grant, distinct from supply-chains/blockchain/GA. → [[weihrauch-containers-frontier]].
- **★ T2 technique banked:** Goncharov et al. 2405.16708 Thm 3.7 = reduce an all-X (di)naturality
  condition to the terminal object, lift back up (structurally right shape; E2′ already closed by ≤1-leaf).
- **Scoop-checks owed before the effects⊗coeffects PAPER:** arXiv:2602.18295 (Goncharov sequel);
  Dumas–Duval–Reynaud 1310.0605 (title on-target, abstract-only). No registry changes; no demotions.
  Day: `dream-journal/2026-07-30.md`.

## 2026-07-30 (lean) — biKleisli skeleton INSTANTIATED at Maybe; abstract associativity proved
- **LEAN DONE** (`Containers/BiKleisliMaybe.lean`, new; + one addition to `BiKleisli.lean`; full build
  green, sorry-free, zero warnings). Registry node `bikleisli-maybe-lean` = `lean-verified`
  (`Containers.BiKleisliMaybe.arr_assoc`). Collaborator note `for-collaborator/2026-07-30-lean-bikleisli-maybe-instance.md`.
- `Maybe:SetMonad`; `T_Maybe(S,P)=(Option S, P⋆)` as `Monad Container` (`P⋆(none)=PUnit`, `P⋆(some s)=P s`
  — the degenerate arity-≤1 Π); `κ` (id on `some`, η-pad `1→Option 1` on `none`); **all four mixed-DL
  axioms E1′–E4′ discharged for Maybe, incl. E2′** (the branching-obstructed one, closes because Π ≤1 leaf).
- **NEW abstract theorem `MixedDistrib.acomp_assoc`** (general biKleisli associativity from E1′–E4′, 7-rewrite
  chase E2′@r·μnat@h·assoc@s·coassoc@p·δnat@f·E4′@q·κnat@g) — did **not** exist before (BiKleisli.lean docstring
  wrongly claimed it; corrected). ⟹ `arr_unit_left/right/assoc` = full **associative** arrow category for Maybe
  = machine-checked "Maybe is a genuine category" half of Theorem A.
- Axioms `[propext,Quot.sound]`. Trick: definitional proof-irrelevance for `Eq` absorbs non-`rfl`
  `Option.join/map` shape identities in `ext'`; `Option.map id p` needs `cases p`. Branching (Pf) side still
  computed-only (intended). Next instance: Writer/ℤ₂.

## 2026-07-30 (prove) — arrows result FINISHED: positive class = writer+absorbing-exceptions; E2′ closed
- **PROVE T1+T2 DONE** (`proofs/2026-07-30-affine-classification.md`; registry node
  `affine-classification` = proved, validates). The mode-3 obstruction now has a **named positive class**.
- **T1.** For cartesian `M`, TFAE: arrow category exists ⟺ `M` non-branching ⟺ `M ≅ E+A×(−)` ⟺
  **`M` = writer-with-absorbing-exceptions** (`A` a monoid, `E` a **left `A`-set**; μ = writer-multiply
  on `A`, throw-and-absorb on `E`). **Two-level pin (corrects PROVE.md "A a monoid"):** at *Set-monad*
  level, monad-on-`E+A×(−)` ⟺ **monoid on `N=E⊔A`, unit in `A`, `E` a two-sided ideal of LEFT ZEROS**
  (aborting `γ:A×A→E+A` allowed, e.g. nilpotent `z²=0`); the *cartesian/polynomial* sub-class (where
  `T_M` lives) = **non-aborting** = `A` submonoid + `E` an `A`-set. Aborting monads are valid Set-monads
  but `μ` destroys a leaf ⟹ non-cartesian ⟹ `T_M` undefined ⟹ outside the arrow story. Bijection
  machine-verified (`affine_classify.py`, 0 mismatch, 911250 cands).
- **T2 (E2′ gap CLOSED).** For non-branching `M` every `P⋆` product has ≤1 factor ⟹ `κ`=id (unary)/`η^M`
  (nullary) ⟹ E1′–E4′ all hold, E2′ = associativity of `N`; the ≥2-leaf product-comparison obstruction
  never forms. Verified `2+3×X`(A=ℤ/3) & `1+2×X`(A=ℤ/2): all axioms PASS on `U1,A1,A3`, arrow-assoc 0
  violations (`affine_e2prime.py`).
- **"Affine" clash flagged:** arity≤1 (`M1` unrestricted) ≠ Kock-affine (`M1≅1`, forces `Id`).
- Next: LEAN the Set-monad⟺monoid bijection / instantiate `MixedDistrib` at concrete `Writer/ℤ₂`.

## 2026-07-30 (wake) — daily sent; inbox clean; triggers reset to FINISH the arrows result (no new front)
- **Morning daily to Neil SENT** (CC Robin): effects⊗coeffects pipeline complete — arrows = genuine
  Hughes/Freyd category ⟺ M non-branching (first/costrength: G_M always costrong, T_M strong-for-× ⟺
  non-branching; branching disables via TWO axioms — E2′ merging + leaf-symmetry); BiKleisli.lean unit
  laws axiom-free = the unconditional part; Plotkin–Turi YES for the λ face. Asked ONE new Q: paper as
  standalone note vs book-Ch7 capstone. **Inbox EMPTY** (latest = Neil UID 81, already processed).
- **Trigger audit:** 07-29 pipeline consumed PROVE (route (a) arrows+first) and LEAN (biKleisli unit
  laws); **WRITE (three-modes table) still pending** (LAST_WRITE 10:47 < WRITE.md 15:33; not in book —
  book last touched 07-29 10:45 = Workers-into-Ch7). All three modes' registry nodes VALIDATE
  (`effect-coeffect-arrows`/`monad-comonad-entwining`/`state-object-delta` = proved) ⟹ three-modes table
  citable. **Triggers reset (supporting increments, NOT moonshots — Neil's close-out posture):**
  - **WRITE** = KEEP the three-modes-of-composition table into book Ch7 capstone / grant Path-5.
  - **PROVE** = FINISH the arrows result: (T1) positive classification of mode 3 — arrow category exists
    ⟺ M non-branching ⟺ M ≅ affine/exception–writer `E+A×(−)` (arity ≤1 polynomial monad), pin the
    monoid-action monad structure; (T2) close E2′ general-`j`. Gives the branching obstruction a NAMED
    class. Retreat = (ii)⟺(iii) at functor level + `/expository` on affine monads.
  - **LEAN** = instantiate `MixedDistrib` at M := Maybe (concrete `T_Maybe`, reverse κ, discharge E2′/E4′)
    ⟹ first machine-checked *associative* arrow category on `Cont` for a concrete non-branching M.
- Dream "tomorrow" deep-reads (1912.13477 full, Goncharov 2405.16708) deferred to the browse phase.

## 2026-07-29 (lean) — biKleisli **unit laws** machine-checked (`Containers/BiKleisli.lean`)
- **LEAN.md target DONE.** Abstract biKleisli skeleton over the Mathlib-free `Category` typeclass:
  `Comonad`/`Monad`/`MixedDistrib G T` (κ:GT⇒TG, axioms E1′–E4′ + κ-nat); arrows `C(Gp,Tq)`,
  `arrId=ε≫η`, `acomp=δ≫Gf≫κ≫Tg≫μ`. **`MixedDistrib.unit_left`(=E1′) + `unit_right`(=E3′)** proved
  from ONLY (co)monad unit laws + ε/η naturality + the two *unit* κ-axioms — **never E2′/E4′**, the
  Lean witness that the unit laws are the **unconditional** part (all M). `#print axioms`: unit laws
  depend on **NO axioms** (pure).
- **Anchored:** `SetMonad.toComonad` repackages the Lean-verified transfer comonad `G_M` (Quot.sound);
  `Monad.identity` + `Comonad.coKleisliDistrib` give the **T=Id coKleisli** category (Workers/coeffect
  slice §3.1) with full `coKleisli_acomp_assoc` (coassoc + δ-nat; propext only). Sorry-free, zero warnings,
  in the root build. Registry `effect-coeffect-arrows.json` child `lean-bikleisli-unit-laws` → **lean-verified**
  (`lean: MixedDistrib.unit_left`).
- **NOT done (next Lean increment):** concrete Ahman–Bauer `T_M` + reverse `κ` as `Cont` data ⟹ (3)⇔(4)
  non-branching step stays computational. Gotchas: core `conv => rhs; arg 2` (not `conv_rhs`); declare
  coKleisli homs as plain `Category.Hom (G.obj p) q` to keep rw's index matching syntactic.
  Note `for-collaborator/2026-07-29-lean-bikleisli-unit-laws.md`. → [[effect-coeffect-arrows-are-a-category]] [[lean-monad-comonad-transfer-done]].

## 2026-07-29 (prove) — route (a) DONE: effect–coeffect arrows are a genuine Hughes arrow / Freyd category ⟺ M non-branching
- **PROVE session (route (a), the queued Freyd/arrow interface).** Tensor = **cartesian `×`** on Cont.
  `arr(φ)=η^T∘φ∘ε` (id-on-objects functor, Prop 1); `first(f)=τ∘(f×id)∘σ`. **Main:** `Arr_M` is a
  Hughes arrow / Freyd category **⟺ M non-branching** (Thm A category + Thm B laws).
- **Lemma 2:** coeffect comonad `G_M` **always costrong** (σ_G ∀M). **Lemma 3:** effect monad `T_M`
  **strong for `×` ⟺ M non-branching** — Yoneda forces a fixed leaf-projection, leaf-symmetry breaks it.
- **★ Self-correction banked:** my first guess "no *total* strength" was WRONG — total strengths exist
  (priority rule, even passes strength-MULT) but break **naturality**. So the strength obstruction is
  **leaf-SYMMETRY**, DISTINCT from assoc/E2′ (=μ-merging): **branching disables the arrow via TWO
  independent axioms.** L3–L8 exhaustive (Maybe, Writer/ℤ₂; L5 1024/1024). `arrows_first.py`. Registry
  `arrow-freyd-costrength`=proved (validates). Note `for-collaborator/2026-07-29-arrows-first-strength.md`.
  Resolves Gap 3 of the morning result. → [[effect-coeffect-arrows-first-strength]].

## 2026-07-29 (wake-2) — daily sent (answers Plotkin–Turi); route (b) KILLED, route (a) queued; triggers reset toward the effects⊗coeffects paper
- **Morning daily to Neil SENT** (CC Robin): effect–coeffect **arrows PROVED** (biKleisli iff M non-branching,
  compositor=reverse κ); answered his **Plotkin–Turi Q — YES for the λ/bialgebra face** (∀M), branching only
  obstructs the *arrow packaging* face; the three-modes/three-obstructions crown; asked framing (effects-and-
  coeffects vs bialgebraic-semantics). Inbox clean (Neil's 07-29 steer already processed).
- **★ Browse (2 agents) — route (b) DEAD.** KRU 1912.13477 deep-read: interaction laws are *pairings*
  `TX×DY→X×Y`, NOT compositors ⟹ entwining ≠ KRU Chu/Day monoid object; do NOT re-attempt. Salvage: their
  Thms 1/2/3 branching no-go = *extensive-category sibling* of my criterion (cite); Sweedler-dual toolkit =
  separate speculative lead. → [[kru-interaction-laws-are-pairings-route-b-dead]].
- **★ Strongest NEW lead — arXiv:2607.23228** (sectional invariants / functorial databases): LS-category
  **integer** obstruction to global sections of a discrete opfibration — parallel to my `[ω]∈H²` story with a
  DIFFERENT invariant. Close-read next browse (second obstruction number? scoop-risk?). Four smaller neighbours
  logged (`reading/2026-07-29-browse2.md`). INFRA: research MCP arxiv tools broken (301) — flagged to Robin.
- **Triggers RESET:** PROVE = route (a) **Freyd/arrow interface** (`arr`/`first`/costrength → Freyd id; E2′
  general-j; KRU cross-check). LEAN = **effect–coeffect arrow composition + unconditional unit laws** (reuse
  `MonadComonadTransfer.lean`'s `G`; assoc only for Maybe). WRITE = **three-modes table** into book Ch7 /
  grant Path-5 (branching double-duty paragraph + KRU 2-sentence cite).

## 💤 2026-07-29 (dream) — Composition has THREE modes, three obstructions; branching splits the arrow face from the bialgebra face
- Consolidates the 07-29 pipeline (WAKE Workers-vs-A.4 closed orthogonal + Neil effects⊗coeffects
  steer / PROVE effect–coeffect arrows / LEAN `Workers.lean` / WRITE Workers→Ch7). All banked live
  below; dream extracted the connection + mapped the literature landscape.
- **★★ CROWN — three modes of composing agents, three obstruction TYPES, one grant question**
  (`connections/three-modes-of-composition.md`): **directed axis** ZS `[ω]∈H²(Sk_C;𝒟)` may fail;
  **state axis** Workers *none* (always composes, grade accumulates `S×T`); **effect–coeffect axis**
  obstruction = **branching** (M arity ≥ 2), arrow category exists iff M non-branching. Three
  different constructions, three different obstruction *types* (cohomology class / nothing / Boolean
  arity), all container-native + computable. Grant Path-5 spine, deployable as prose. **Do NOT
  over-merge into one master obstruction** — the honest claim is three-modes-three-obstructions.
  → [[three-modes-of-composition]].
- **★★ Branching does DOUBLE duty.** The 07-27 entwining + 07-29 arrows are two faces of ONE entwined
  structure: **bialgebra face** `λ:TG⇒GT` exists for ALL M (= Plotkin–Turi YES, Neil's Q answered);
  **arrow face** `κ:GT⇒TG` exists iff M non-branching. Same monad, same two feeds — obstruction is
  *which direction* you commute effect past coeffect. That is the honest content of "arrows unify
  effects and coeffects for containers": unconditional as bialgebra, branching-obstructed as arrow.
- **★ Neil's arrow synthesis is genuinely OPEN** (07-29 browse): ingredients scattered — arrows=monoids
  (Heunen–Jacobs MFPS 2006), coeffects=indexed comonads (Petricek–Orchard–Mycroft ICALP 2013), graded
  eff+coeff DLs (Gaboardi et al. arXiv:2112.14966), Chu-space/Day alt-unification (Katsumata–Rivas–
  Uustalu arXiv:1912.13477), modern Plotkin–Turi (Goncharov et al. arXiv:2405.16708) — **nobody
  assembled them for containers/Poly, none as an arrow category.** I own the hard core (both faces +
  branching obstruction). **Route (b)** (Chu monoid object over (Endofunctors, Day)) reuses my
  Dirichlet Day-convolution machinery ⟹ likely the tractable next PROVE. Depth flags: 1912.13477
  abstract-only, 2405.16708/2112.14966 title-abstract, all read-in-full owed. Day: `dream-journal/2026-07-29.md`.

## 2026-07-29 (LEAN) — The (Set,×)-graded category of Workers, sorry-free
- **★★ `state/LEAN.md` target DONE — `Containers/Workers.lean`, full library builds, zero errors/warnings.**
  T3-core of `state-object-delta.json` promoted **proved → lean-verified** (registry child
  `lean-worker-composition`, `lean: Worker.comp`).
- `Worker S p q := ContainerMorphism (deltaS S ⊗ p) q`; `Worker.comp : Worker S p q → Worker T q r →
  Worker (S×T) p r` (**state multiplies**, direct coordinates, **axiom-free**); `Worker.id : Worker Unit p p`
  (grade 1); `Worker.reGrade` = state transport along a grade bijection (Δ on Core(Set)).
- Three graded-category laws, each `ext' rfl; intro; rfl` (**Quot.sound-only**): `unit_left` (1×T≅T),
  `unit_right` (S×1≅S), `assoc` ((S×T)×U≅S×(T×U)). **LEAN.md's "Lemma-3.1-is-rfl ⟹ defeq-shaped, no
  transport slog" prediction held — compiled first try.** `para-identification` stays computed (deep-read owed).
- Collaborator note `for-collaborator/2026-07-29-lean-worker-composition.md`. → [[workers-graded-category-proved]] [[lean-state-comonad-delta-done]].

## 2026-07-29 (PROVE) — Effect–coeffect arrows: compositor is the REVERSE entwining; category ⟺ M non-branching
- **★★ Neil's 07-29 PROVE target DONE — `proofs/2026-07-29-effect-coeffect-arrows.md` (registry `effect-coeffect-arrows.json`=proved).**
  Effect–coeffect **arrows** `p⇝q:=Cont(G_M p,T_M q)` form the **biKleisli category ⟺ M is NON-BRANCHING (arity≤1)**.
- **★ The key reversal (corrects PROVE.md):** the compositor is **NOT** the proved `λ:T_MG_M⇒G_MT_M` (07-27). To
  compose you commute `T` OUT of `G` — `G(Tq)→T(Gq)` is the arrow `GT⇒TG`, i.e. the **reverse** law
  `κ:G_MT_M⇒T_MG_M` (lax `∏M→M∏`), the branching-obstructed one. Theorem A: category ⟺ `G_M` lifts to `Kl(T_M)`
  ⟺ `κ` mixed-DL axioms ⟺ M non-branching. Unit laws=E1′/E3′, **associativity=E2′** (sole branching-obstructed axiom).
- **Direct arrow-level (bikleisli.py, composite as a real Cont-morphism):** Maybe & Writer/ℤ₂ = genuine categories
  (1536/1536, 4608/4608 assoc triples + unit laws); **Pf NON-ASSOCIATIVE**, explicit witness (unit laws still hold).
- **Dichotomy = the honest "unification":** arrow/Freyd face (`κ`, non-branching) vs **bialgebra/Turi–Plotkin face**
  (`λ`, ALL M — `G_M`↑`T_M`-alg + `T_M`↑`G_M`-coalg). **Answers Neil's Plotkin–Turi Q: YES for the `λ` direction.**
- Neighbour diff-engine: Katsumata–Rivas–Uustalu 1912.13477 (Chu/Day interaction laws = *pairing*, not compositor).
  GAPS: E2′ general-`j` (inherited, mechanical); full Arrow (`first`/costrength) unchecked = next; logic angle open.
  Collaborator note `for-collaborator/2026-07-29-effect-coeffect-arrows.md`. → [[two-feeds-entwine-one-direction]].

## 2026-07-29 (wake) — Workers-vs-A.4 CLOSED (orthogonal); Neil steers to effects⊗coeffects paper; two neighbours cleared; triggers reset
- **Morning daily to Neil SENT** (CC Robin): Workers proved+Lean'd; the A.4 opportunity; two-axes framing;
  Core(Set)/Para question. **Then a focused follow-up** (our mails crossed) answering Neil's three direct Qs.
- **★ Inbox: Neil's 07-29 reply — a rich steer that reshapes the cycle.** (1) approves the finer chapter map;
  (2) **★★ the entwining mixes a Kleisli arrow (effect) + a coKleisli arrow (coeffect); ARROWS/PROFUNCTORS are
  the FP solution to "monad on top, comonad on bottom" — "a genuine unification of effects and coeffects for
  containers, might be worth a paper"** (→ this cycle's PROVE); (3) he's worked on predicate liftings for
  fibrations; (5) asked for the Topos-PLTL blog URL (SENT: topos.institute/blog/2025-09-26-free-pltl-algebras-
  and-hyperdoctrines) + whether it relates to logic over `Cont(Set^→)→Set`; (6) is this **Plotkin–Turi
  bialgebraic semantics** (lift comonad→algebras, monad→coalgebras)? — YES lead, the entwining already gives
  both lifts; (7) Capucci was his PhD student, happy to cite as neighbour.
- **★★ CROWN OPEN Q CLOSED — Workers vs Contextads Thm A.4 = ORTHOGONAL** (research-agent close-read, verified
  quotes). Their grade is DEPENDENT `X→S` over a FIXED `S`, multiplying via one monad's `seq` (Def A.3(1),
  Eq A.2.2) — cannot make `S×T`; mine is EXTERNAL `S` over all `(Set,×)`, cartesian `Δ(S×T)=ΔS⊗ΔT`. **Workers
  settles NO fragment of A.4.** Clean positioning (my extension): by their **Example 3.24** (M-graded comonad
  = trivially-fibred contextad / colax action), Workers = the trivially-fibred corner, OPPOSITE A.2/A.4's
  dependency-essential corner. Cite A.4 as neighbour, self-identify via Ex 3.24. → [[workers-contextads-a4]].
- **★ Race-risk CLEARED — Spivak 2503.21974 "Categories by Kan extension" = NEIGHBOUR, not scoop.** It builds
  NEW base categories from "distributive laws of monads over comonads" via the density comonad (Lawvere,
  Δ^op); my entwining = mixed DL of two endofunctors ON Cont with a fibrewise base monad. Cite in Ch7
  entwining as neighbour. → [[spivak-2503-kan-extension-neighbour]].
- **Triggers RESET** (all 3 prior consumed by the 07-28 pipeline; dream ran 07-28 23:46):
  - **PROVE** = **effects ⊗ coeffects on Cont** — is the entwining `λ` the compositor of the effect–coeffect
    arrows `G_M p→T_M q` (⟹ they form a Freyd/arrow category, coherence = the E-axioms)? Neil-endorsed,
    extends the proved entwining, decides Freyd/arrow/bialgebra + Plotkin–Turi. Retreat = one assoc triangle
    in coords + `/expository` survey. Registry: new `effect-coeffect-arrows` (speculative→).
  - **LEAN** = **Worker graded-composition laws** (`Workers.lean`, extends `StateComonad.lean`): compose via
    `deltaS_tensor` (Lemma 3.1 `rfl`), unit/assoc up to `(Set,×)` coherence ⟹ promote `state-object-delta`
    T3 to lean-verified. Retired: free-monad `freeExtPos_mult` (5× resisted).
  - **WRITE** = **the category of Workers into the book** (Ch7) + both neighbour citations settled today
    (A.4 via Ex 3.24 colax corner; Spivak 2503 in entwining §) + two-axes paragraph + effects⊗coeffects
    forward-pointer.

## 💤 2026-07-28 (dream) — Workers pipeline consolidated; crown = the proof lands on an UNPROVEN published theorem
- Full Ch4 pipeline ran on Neil's Workers steer: PROVE (Workers = `(Set,×)`-graded category, banked below),
  LEAN (`StateComonad.lean` — `ΔS` D1–D5 rfl/axiom-free + Lemma 3.1 `ΔS⊗ΔT=Δ(S×T)` rfl), WRITE (entwining
  into book Ch7), BROWSE×2 (Contextads deep-read).
- **★★ CROWN — Workers vs the UNPROVEN Contextads Theorem A.4.** Capucci–Myers "Contextads as Wreaths"
  (arXiv:2410.21889 App. A.2), deep-read 07-28, has **Thm A.4 `Kl(T)≅Ctx(⊙)` LEFT UNPROVEN** — a polynomial
  monad transposing to a dependently graded comonad whose grade multiplies by `seq`, "close to verbatim" on
  the proved Workers shape. **Sharp open Q (next PROVE):** is `S↦ΔS⊗−` an instance of `⊙` (⟹ my coordinate
  proof settles a *case* of the open theorem) or orthogonal (external `S` vs dependent `X→S` grade)? Distinct
  from my own transfer `(S,P)↦(S,M∘P)` — three constructions, one neighbourhood. Workers *math* is proved;
  its *positioning* vs A.4 is open — Ch4 writeup must lead with 2410.21889. → [[workers-graded-and-contextads]].
- **★ Two axes of agent composition** (grant Path-5 duality): Workers = **state axis** (context multiplies
  `S×T`, `(Set,×)`-graded, NO obstruction — always composes, grade accumulates), dual to ZS **directed axis**
  (`[ω]∈H²`, may fail to exist). Unobstructed-but-accumulating vs obstructed-but-non-accumulating.
- **★ Breadcrumbs:** Ghani–Kurz CALCO 2007 Thm 3.2 (`X↦μY.X×FY` comonad = empty 4th quadrant of free/cofree
  table) — but higher-DIMENSIONAL not higher-ORDER; confirm w/ Neil before citing item-1. Race-risk: Spivak
  "Categories by Kan extension" CT2026 talk = comonads "from distributive laws of monads over comonads" —
  re-check arXiv:2503.21974 version. Para↔Poly↔graded-monad bridge genuinely unwritten (novelty upside).
  Day: `dream-journal/2026-07-28.md`; topic `topics/graded-workers-para.md`; leads in `questions/open-threads.md`.

## 2026-07-28 (prove) — Category of WORKERS PROVED (ΔS store comonad → (Set,×)-graded category → Para)
- **★★ Neil's Ch4 Workers target PROVED** — `proofs/2026-07-28-delta-state-object-and-workers.md`,
  `registry/state-object-delta.json` root=**proved** (trustcheck OK). Code `scratch/state-object-delta/` all green.
  - **T1:** `ΔS=(S,s↦S)` = **codiscrete category** on `S` (DCont≅Cat; `o_s=s, s↓p=p, p⊕p'=π₂`, D1–D5 ✓);
    `⟦ΔS⟧=S×(−)^S` = **store/costate comonad** (Uustalu–Vene). **T2:** `⟦ΔS⟧=S×Reader_S`; reader `X^S` = fibre.
  - **T3 (target):** Worker `p→q`/state `S` = container map `ΔS⊗p→q` (Dirichlet ⊗). **`ΔS⊗ΔT=Δ(S×T)` strict**
    ⟹ composition **multiplies context to S×T** = exactly Neil's prediction. **Workers = (Set,×)-graded category**
    = coKleisli of graded comonad `S↦ΔS⊗−`. Assoc/unit exhaustively verified (512+1369 triples). **⊗ forced**:
    product tensor gives fibres |S|+|T|≠|S×T| (negcontrol). S-varying = **Gavranović Para** of action `S·p=ΔS⊗p`.
  - **Two GAPS (identifications only):** (1) Para exact only over `Core(Set)` (Δ functorial on bijections only) —
    graded **computed**, not proved; (2) FKM graded-comonad packaging unwritten. Core mathematics (T1–T3 graded
    category) is **proved**. → [[applications-are-directed-containers]], for-collaborator note 07-28.
  - **Next:** LEAN Lemma 3.1 (`ΔS⊗ΔT=Δ(S×T)`, defeq-shaped, mirror MonadComonadTransfer.lean); Neil Qs (graded
    vs Para statement; Core(Set) home?).

## 2026-07-28 (wake) — Neil's Workers/graded-monad steer; daily sent; triggers reshaped (entwining still owed in book)
- **Two unread from Neil (07-27, uids 79/80), now read + answered in the 07-28 daily (CC Robin).** He replied
  inline to the entwining + transfer dailies. Load-bearing steers → [[neil-workers-graded-steer-2026-07-27]]:
  - **★★ Category of WORKERS (Kodamai name) = the next direction.** Objects `ΔS⊗p→q`; composition multiplies
    context `DS*p→q ; DT*q→r ↦ D(S×T):p→r`; "not really monads but **graded monads**", graded by `(Set,×)`,
    `S:Set` not Monoid; "S changes" = Gavranović **Para** construction. Reader-monad basic defs first.
  - **Item 1 (Ghani–Kurz higher-order trees):** easy — "decode the free-monad formula"; do as a worked example.
  - **Predicate liftings:** `P′:MA→Set` = predicate liftings; my ∏-cointerp = the *universal* one; ADOPT that
    language over "weak Mendler algebra". Mendler↔Kan-extensions FLAGGED for later (push known material first).
  - **Chapter numbering:** Neil's 4 blocks vs my 10 fine chapters (his "Ch4 Monads&Comonads" = my Ch6+Ch7;
    transfer+entwining live in my Ch7 §sec:moncomon-transfer ~L2279). Asked him whether to consolidate; did NOT
    renumber unilaterally.
  - Answered his explicit questions in the daily: λ:MP→PI^op type; entwining gives an *entwined structure*
    (not a single (co)monad; G_M lifts to T_M-alg); position-op "two faces"; Capucci Contextads = ZS-wreath,
    cite-as-neighbour; wants 2-sentence lit-relations added as we go (no retro-sweep).
- **Entwining is proved (07-27, `monad-comonad-entwining.json` root=proved) but STILL not in the book** — this
  remains the WRITE target. Book = 10 chapters, 54pp; transfer in Ch7, ZS/distributive-laws in Ch8.
- **Triggers reshaped (NOT yet consumed — browse/prove/lean/write still to run this heartbeat):**
  - **PROVE** = the **category of Workers** (ΔS characterization → reader/store → graded composition `D(S×T)`
    → Para). Retreat = ΔS as codiscrete/store comonad. `state/PROVE.md` rewritten to Neil's framing.
  - **LEAN** = free-monad MULT-backward (5th pass, do-NOT-bash) → else fresh **ΔS state comonad** (now strongly
    endorsed; pairs with PROVE). `state/LEAN.md` unchanged.
  - **WRITE** = fold **entwining** into Ch7 + Neil's 5 additions (lit sentences Topos-PLTL/Hinze/Ahman–Bauer;
    item-1 Ghani–Kurz trees example; position-op paragraph; predicate-lifting language; Workers forward-pointer).
    `state/WRITE.md` extended.

*Pruned 2026-07-14 (dream 6): ~155 lines of superseded 06-11/06-12/06-13 pipeline chronology
removed; all citations retained. Where this file and `proofs/registry/` disagree, the registry wins.*

## 2026-07-26 (wake) — entwining audited PROVED; daily sent; triggers reset to Neil Ch4 items 3+4 (state object ΔS)
- **Audited last cycle vs disk (grades, not prose).** Entwining PROVED: `proofs/2026-07-27-monad-comonad-entwining.md`
  + `registry/monad-comonad-entwining.json` root=**proved**, trustcheck OK. Children: `TM-is-a-monad`=published
  (Ahman–Bauer), `GM-is-a-comonad`/`str-canonical-direction`/`axioms-E1-E3-E4`/`axiom-E2-mult-T`(computed child)/
  `reverse-orientation-fails`=proved; **`general-mendler-algebra`=dead-end** (honest — general-`j` case open).
  LEAN `DualTransfer.lean` = genuinely **sorry-free** (the lone "sorry" hit is inside a comment) ⟹ transfer
  Lean-verified BOTH directions. Book ~54pp/2785 lines; Ch7 has Ahman–Bauer nearest-neighbour discussion + the
  two-feeds pedagogy (no literal "Novelty" heading — content is there as prose). **Gap: the entwining is proved
  but NOT yet in the book** ⟹ this cycle's WRITE.
- **Inbox EMPTY** (latest = Neil's already-read 07-24 reply; no new steer, no registry events).
- **Morning daily to Neil SENT** (CC Robin): entwining proved (two feeds interact via canonical mixed
  distributive law `λ:T_M G_M⇒G_M T_M`, standard `TG⇒GT` only; obstruction=**branching** not commutativity;
  `Pf` witness); DualTransfer Lean'd; Ch7 novelty firmed. Asked (1) which remaining Ch4 item next — 1
  (Ghani–Kurz trees) / 3 (reader `ΔS⊸−`) / 4 (Kleisli/stateful morphisms) / 5 (continuation/oracle); (2) does
  the entwining belong IN Ch7 or as a standalone note.
- **Triggers RESET (a Monads-on-Cont continuation around the state object `ΔS=(S,s↦S)`, shared by items 3+4):**
  - **PROVE** = characterize `ΔS` (conjecture: codiscrete category on `S` via `DCont≅Cat`; D1–D5 check) + the
    reader/store construction `ΔS⊸(−)` (pin `⊸` from [[closed-structures-are-spivaks]]; identify the Set-level
    (co)monad — expect store/costate `S×(−)^S`) + Kleisli = **stateful container morphisms** (item 4). Retreat =
    just the `ΔS`-comonoid characterization. ⚠ store/costate comonad is folklore — grade the identification, not it.
  - **LEAN** = free-monad **MULT-backward** (5th pass — time-box ONE, do NOT bash) → else **fresh** `ΔS` state
    comonad in core Lean (D1–D5 + 3 comonad laws, mirrors `DirichletComonoid.lean`), pairs with PROVE.
  - **WRITE** = fold the **entwining** into Ch7 as the Monads-on-Cont capstone (statement + forced orientation +
    branching obstruction + Beck–Chevalley reading + honest open general-Mendler scope); verdict on standalone note.

## 2026-07-27 (prove) — ★★ THE TWO FEEDS ENTWINE — in exactly one direction
- **PROVE trigger DISCHARGED.** Do `T_M` (shapes→monad, A–B Thm 6.3) and `G_M` (positions→comonad, transfer)
  of one Set-monad `M` interact via a mixed distributive law? **YES — canonically, standard orientation only.**
- **Main theorem (proved):** for every `M` with the **∏-cointerpretation** weak Mendler algebra (A–B's class:
  `Pf`, `Maybe`/exception, `Id`, …), the **oplax product-comparison** `str : M(∏_b Z_b)→∏_b M Z_b` (every
  functor has it, by the universal property of `∏`) is the backward map of a **mixed distributive law**
  `λ : T_M G_M ⇒ G_M T_M` (the *standard* `TG⇒GT` orientation) satisfying all four entwining axioms. Proof:
  E3 = naturality of `η`; E1 = Mendler `i`=id on singleton products; E4 = naturality of `μ`; E2 = naturality
  of `str` w.r.t. the product-reindexing (= A–B Def 6.2 `j`-naturality), machine-verified for the class incl.
  branching commutative `Pf`. `(T_M,G_M,λ)` = entwining structure; `G_M` lifts to `T_M`-alg, `T_M` to `G_M`-coalg.
- **★ The orientation PROVE.md GUESSED (`GT⇒TG`) FAILS** once `M` branches: the lax map `∏M→M∏` breaks the
  T-multiplication axiom. **Obstruction = BRANCHING, not commutativity** — `Pf` is commutative and fails,
  via *union-of-products ≠ product-of-unions* (explicit witness `X=({a,b},a:2,b:1)`). Arity ≤1 (`Maybe`,`Writer`):
  both orientations coincide (`str`=lax=iso). **Meaning:** `λ` = "`M` oplax-preserves products, on positions";
  fibrationally a Beck–Chevalley 2-cell (`G_M` vertical `(M^op)_*`, `T_M` covers base monad `M`).
- Proof `proofs/2026-07-27-monad-comonad-entwining.md`; harness `scratch/monad-comonad-transfer/entwine.py`
  (forward 12/12 PASS); registry `monad-comonad-entwining.json` (**proved**, trustcheck OK). Deep-read A–B
  §6 (Def 6.2 + Thm 6.3) from PDF → sources upgraded to `deep-read`. → [[two-feeds-entwine-one-direction]].
  Gaps: general-`j` chase (mechanical), non-∏ Mendler algebras (open), named Set-level descent (open).

## 2026-07-25 (wake) — item-2 NOVELTY RESOLVED (narrowed, not scooped); Ahman–Bauer is the mirror; triggers reset
- **Morning daily to Neil SENT** (CC Robin): transfer **proved + Lean-verified + written** (Ch6/Ch7, 54pp);
  flagged the Ch7 novelty gap honestly; asked which Ch4 item (1 higher-order trees / 3 reader / 4 Kleisli /
  5 continuation) he wants next. **Inbox EMPTY** (no unread).
- **★★ NOVELTY of the monad→comonad transfer RESOLVED — the three unengaged neighbours engaged (2 research
  agents; durable reading note `reading/2026-07-25-transfer-novelty-three-neighbours.md`):**
  - **Topos-PLTL blog** (2025-09-26 hyperdoctrines post) — **ADJACENT, no scoop**: their `λ:MP→PI^op` links a
    PLTL-algebra monad on *predicates* to a cofree-comonad interface; never applies `M` to positions; the
    "branching (degree≥2) obstruction" slogan is a **coincidence**. (Confirm byline before citing.)
  - **Hinze WG2.8 pearl** — **UNRELATED**: (co)monad transport across an adjunction `L⊣R`, no containers.
  - **★ Ahman–Bauer 2409.17664** — the **MANDATORY nearest-neighbour cite, NOT a scoop**. Same `Cont`, same
    cointerpretation `∏_a(Pa×X)` (AU prior art). BUT Prop 4.1/4.2 = trivial `C↔C^op`; and Thm 6.3
    `T(A◁P)=MA◁P⋆` applies `M` to **SHAPES → monad** = the **MIRROR** of the transfer (positions → comonad).
  - **★★ Verdict:** contribution is NOT "monads & comonads on containers" (A–B own that) — it is specifically
    **positions→comonad `(S,M∘P)` = ◁-left-coclosure `Lan_{(S,P)}M`**, absent in both papers. Ch7's Novelty
    Remark must **lead with Ahman–Bauer 2409.17664**. New pedagogy: **two ways to feed a Set-monad into a
    container — shapes→monad / positions→comonad**, locked by the fibrewise op.
    → [[position-op-turns-monads-into-comonads]] (novelty block updated).
- **Triggers RESET (all three prior were consumed by the last pipeline):**
  - **PROVE** = do the **shapes-monad `T_M` and positions-comonad `G_M` ENTWINE?** (a mixed distributive law
    for the two feeds; grant-relevant — distributive laws are the seed's core tool). Honest retreat = the
    **dual transfer** `H(S,P)=(S,W∘P)` monad + its `Ran`/◁-right-coclosure characterisation (near-certain).
  - **LEAN** = free-monad **MULT-backward** (ONE time-boxed pass — 4th attempt, do NOT bash) → else the
    **dual transfer comonad→monad** (clean mirror of the done `MonadComonadTransfer.lean`).
    → **✅ DONE 2026-07-25 (LEAN):** pivoted to fallback (MULT-backward still resisting, honoured do-NOT-bash).
    `DualTransfer.lean` sorry-free, `[Quot.sound]`-only, full `lake build` green (38 jobs). `SetComonad` →
    monad `H(S,P)=(S,W∘P)`; 3 monad laws each = one comonad-law field via `ext' rfl` (transport-free):
    `unit_left`=left-counit, `unit_right`=right-counit, `mult_assoc`=coassoc. **Transfer now Lean-verified BOTH
    directions.** Registry child `lean-dual-transfer` (lean-verified). Note:
    `for-collaborator/2026-07-25-lean-dual-transfer.md`. MULT-backward node step + backward-uniqueness STILL OPEN.
  - **WRITE** = rewrite Ch7's **Novelty Remark to lead with Ahman–Bauer** + add the two-feeds paragraph.

## 💤 2026-07-26 (dream) — transfer pipeline consolidated; crown jewel = ONE op, two faces; novelty NOT yet cleared
- Consolidates the pipeline after the 07-25 dream: browse (`reading/2026-07-25.md`) → PROVE
  (monad→comonad transfer promoted computed→**proved**) → LEAN (transfer comonad **machine-checked**) →
  WRITE (book Ch6/Ch7 refactor, 54pp). PROVE+LEAN already banked in the 07-27 wake block below; dream
  folded in the browse + WRITE and extracted the connection.
- **★★ CROWN JEWEL — the transfer `(S,P)↦(S,M∘P)` and the free/cofree UPs are TWO FACES OF ONE OP.**
  Cont's position-contravariance (`Cont=∫(cod)^op`) is a single fibrewise `(−)^op`, and every
  monad→comonad passage on Cont factors through it: the **transfer** applies the op to the fibre-object
  (`M↦M^op`, so `G=(M^op)_*`); the **cofree UP** applies the same op to the recursion scheme
  (initiality→finality, `W`→`M`, μ→ν). Not special cases of each other — two uses of the one op. New
  connection [[position-op-turns-monads-into-comonads]], bridging [[contravariance-is-the-fibrewise-op]]
  and [[free-cofree-up-reduces-to-given-laws]]. ⚠ `G` is a comonad yet a *left* Kan extension /
  left-coclosure ⟹ the "comonads-from-the-right" slogan is FALSE here; the invariant is the op, not an
  adjoint side (flagged so future-me doesn't "tidy" it into a wrong duality).
- **★ HONESTY — item-2 novelty is NOT fully cleared** (registry `monad-comonad-transfer` = **proved**,
  unchanged; the *theorem* is solid — this is only about the novelty claim). The PROVE gate ran against
  AU / Purdy–Damato / Niu–Spivak; the same-day browse surfaced **three unengaged neighbours**:
  (1) Topos "Free PLTL algebras & hyperdoctrines" blog (2025-09-26) `λ:MP→PI^op` — a live group's
  **same open question** (does the monad→comonad linking upgrade past degree 1?); (2) Hinze WG2.8 pearl
  "Monads from Comonads…"; (3) Ahman–Bauer "Comodule Representations" 2409.17664 (its Prop 4.1/4.2 =
  trivial `𝒞`↔`𝒞ᵒᵖ` duality, CLEAR, but closest territory). **Ch7's Novelty Remark currently only names
  AU/Purdy–Damato — engage all three before it firms up.** Do NOT read this as "novelty cleared."
- **★ Browse also: H²-sibling hunt 5-for-5 CLOSED** (Aguiar–Andruskiewitsch math/0402118 cleared via
  download-then-Read-tool PDF trick — reusable fallback for garbled PDFs; next target 2111.10968). Stand
  down as a recurring browse target. → [[zs-h2-sibling-hunt-closed-5-for-5]].
- Day: `dream-journal/2026-07-26.md`; leads in `questions/open-threads.md` (2026-07-26 block).

## 2026-07-27 (wake) — Neil's Ch4 "Monads on Cont" steer; monad→comonad transfer VERIFIED [computed]; triggers reset to a monads-on-Cont cycle
- **This wake follows the pipeline that consumed the 07-26 triggers.** Audited disk (grades not prose):
  **PROVE done** — `groupoid-zs-obstruction` = **computed**, validates, .pdf compiled (7pp). Seed
  "connected groupoid ⟹ [ω]=0" **REFUTED** (a connected groupoid is a K(Γ,1), H²=group cohomology;
  witnesses ℤ/4⊇ℤ/2, Q8⊇centre obstruct); correct positive theorem [proved] **cd(Sk_C)≤1 (freeness) ⟹
  merges** (Stallings–Swan). Dividing line = freeness, NOT invertibility. Stages Neil's social-networks
  turn (mutual-tie = free groupoid ⟹ always merges; follows/torsion can obstruct). **LEAN partial** —
  `FreeUniversal.lean` gained the two position-side M-law INPUTS (`mult_left_unit_pos`,`mult_assoc_pos`)
  + MULT-forward shape; `freeExtPos_mult` node step + backward-uniqueness STILL remain (3rd session on the
  position half — time-box it next time). **WRITE never fired** (book still pre-refactor: DCont already
  absorbed into a "Comonoids in Cont" chapter, but NOT yet reframed to Neil's "Monoids AND Comonoids" with
  the free-monoid STATED there).
- **★ Inbox: Neil's 2026-07-24 "Ch4 tasks" email — a rich 6-item Monads-on-Cont steer.** (1) Ghani–Kurz
  higher-order trees as the initial-algebra example (foreshadow opetopes); **(2) the monad→comonad transfer
  `(S,P)↦(S,M∘P)`** — he thinks it's a left Kan extension from the ◁-**left**-coclosure, "slots in nicely";
  (3) reader `ΔS⊸(−)` via `ΔS=(S,λs↦S)`; (4) Kleisli `ΔS⊗p→q`, coalgebras `S→Y([p,q])S` = stateful
  container morphisms; (5) continuation `X↦(X→1)→1` / oracle transformer (oracle for (S,P) = `Πs:S. P s`);
  (6) "anything else about monads on Cont?".
- **★ Item 2 already VERIFIED [computed] this wake.** `scratch/monad-comonad-transfer/check.py`: `G(S,P)=
  (S,M∘P)` with **counit backward = monad unit η**, **comult backward = monad mult μ**, is a comonad on
  Cont — all 3 laws PASS for M=Maybe and Writer/ℤ₂; the **dual** (comonad W → monad H(S,P)=(S,W∘P)) PASSes;
  **negative controls fire exactly** (non-assoc μ → only coassoc fails; wrong η → only counit laws fail).
  It's the **position-contravariance reversing arrows** — same mechanism as [[free-cofree-up-reduces-to-given-laws]]
  but at the FIBRE level. Registry `monad-comonad-transfer.json` = **computed** (validates). NOVELTY NOT
  cleared — Ahman–Uustalu update-monads / Purdy–Damato monadic containers are the neighbourhood to check.
- **★★ PROVE SESSION 2026-07-25 — item 2 PROMOTED computed→PROVED** (`proofs/2026-07-25-monad-comonad-transfer.md`,
  registry validates at `proved`). Three legs: **(1) coordinate proof** — each comonad law, localised at
  fibre A=Ps, IS the correspondingly-named monad law (counit-left⟺right-unit, counit-right⟺left-unit,
  coassoc⟺assoc); biconditional via the single-shape container (1,A); self-contained, no external premise.
  **(2) fibred mechanism** — G = pushforward (M^op)_* of the comonad M^op along Cont→Set (fibre (Set^op)^S);
  "positions contravariant" = the (−)^op that turns monad into comonad. **(3) Neil's why, PROVED** —
  G(S,P)={M/(S,P)}=Σ_s y^{M(Ps)} is Meyers' ◁-**left-coclosure** (Niu–Spivak Prop 6.57, formula 6.59) with
  the monad in the NUMERATOR; universal property Poly(Gp,r)≅[Set,Set](⟦p⟧,r◁M) proved by Yoneda
  (counting-verified); =Lan_{(S,P)} M (Trimble Ex 6.63) — **exactly** Neil's "left Kan extension from the
  ◁-left-coclosure." Poly descent ⟦G(S,P)⟧(A)=Σ_s(MPs→A). **NOVELTY CLEARED**: absent from Ahman–Uustalu
  (opposite direction — cointerpretation Cont^op→[Set,Set]), Purdy–Damato (horizontal distributive laws),
  Niu–Spivak (nearest named object = the coclosure the proof USES); construction = fibred-category folklore,
  contribution = coordinate proof + fibred mechanism + coclosure identity + Ch4 exposition. Collaborator
  note in `for-robin/`. **Next: LEAN the transfer comonad; WRITE it into Ch4.**
- **★★ LEAN SESSION 2026-07-25 — item 2 transfer comonad MACHINE-CHECKED** (`lean/Containers/Containers/MonadComonadTransfer.lean`,
  wired into root, full `lake build` green, Lean v4.30.0). Abstract `SetMonad` structure (functor + η + μ +
  naturality + 3 monad laws as fields, no Mathlib); transfer functor `SetMonad.G` on objects + `onMor` on
  morphisms with functor laws (`onMor_id`/`onMor_comp`); `counit` (bwd=η) + `comult` (bwd=μ) as
  `ContainerMorphism`s; naturality (`counit_natural`/`comult_natural`); the **three comonad laws**
  `counit_left`/`counit_right`/`coassoc` EACH reduce via `ContainerMorphism.ext' rfl` (no transport) to ONE
  monad-law field — `right_unit`/`left_unit`/`assoc` respectively, precisely as predicted. Sorry-free; all
  seven results `#print axioms = [Quot.sound]` only (mirrors `DirichletComonoid.lean`). Registry child
  `lean-coordinate-proof` = **lean-verified** (`monad-comonad-transfer.json` validates). Formalises the
  coordinate proof (sec 1) ONLY; the coclosure/left-Kan identity (sec 3) + Poly descent (sec 4) stay
  paper-only. First machine-checked monad→comonad transfer on `Cont` in the corpus — a Ch4 flagship.
- **★ Morning daily to Neil SENT** (CC Robin): reported groupoid [computed] + LEAN state + the item-2
  computed verification (with the η/μ mechanism spelled out) + a plan for items 1,3–5. Combined daily +
  reply to his steer (one-email/day honoured).
- **Triggers RESET to a monads-on-Cont cycle:**
  - **PROVE** = the **monad→comonad transfer** theorem (item 2): promote computed→proved (coordinate
    proof), verify Neil's left-Kan/◁-left-coclosure characterisation, dual, Poly descent, + the novelty gate.
  - **LEAN** = **carry-over** free-monad MULT-backward node step + backward-uniqueness (time-boxed); **fresh
    fallback** = Lean the transfer comonad (elementary, core, no Mathlib — mirrors `DirichletComonoid.lean`)
    once PROVE lands.
  - **WRITE** = reframe the Comonoids chapter to **"Monoids and Comonoids"** (state the free-monoid
    construction there) + open the **"Monads on Cont"** §7 section (transfer Prop [grade = whatever PROVE
    reached]; Ghani–Kurz higher-order-trees example slot; reader/Kleisli/continuation forward-pointer
    teachbox `[to be developed]`) + carry-over Abbott-cite / S′P′-order fixes.

## 2026-07-26 (wake) — Neil's Ch3/Ch4 STRUCTURE steer + Mathlib GREEN LIGHT; all 3 triggers were consumed, reset fresh
- **Morning daily to Neil SENT** (CC Robin): cofree-comonad UP proved (Ch6 mirror complete on paper),
  MULT-forward Lean'd, Ch3 coequaliser now cited, book 52pp; asked the cofree-Mathlib blocker.
- **Our mails crossed — Neil had already answered.** His reply (2026-07-24 "Re: Daily update — Ch4
  answers") carries TWO load-bearing steers:
  1. **★ BOOK STRUCTURE:** NO standalone directed-containers chapter. **Ch3 = "Monoids and Comonoids"**
     (directed containers live here AS comonoids-in-Cont; the **free-monoid construction is STATED in
     Ch3**); **Ch4 = "Monads and Comonads"** (reuses the Ch3 free monoid as the free-monad presenter;
     the DCont≅Cat category-generating role sits in Ch4). ⟹ the 52pp book needs a **refactor** (this
     cycle's WRITE).
  2. **★ MATHLIB GREEN-LIT:** "Yes" — Robin may add Mathlib (`PFunctor.M`+`bisim`) to `lean/Containers`.
     Unblocks the **cofree** Lean (M-type carrier). But the add is Robin's infra action — **cofree Lean
     waits until Mathlib is actually present**; this cycle's LEAN stays in **core** (free-side MULT-backward).
  3. Abbott coequaliser: **just cite the thesis, drop the section number, remove from further-work.**
  4. `S′`/`P′`: the `1+Σ` presentation is fine but `P′`-well-definedness leans on indexed containers not
     yet defined — **book dependency-order caveat** to fix.
- **Sent Neil a short acknowledgement** (CC Robin) closing the crossed-wires loop: green-light noted +
  Robin please add Mathlib; adopting Ch3/Ch4 structure; Abbott + S′/P′ handled.
- **All 3 prior triggers were CONSUMED by the last pipeline** (PROVE cofree-UP proved; LEAN MULT-fwd
  shape landed; WRITE Ch3 coequaliser + Ch6 cofree done). **Triggers RESET:**
  - **WRITE** = the **Ch3/Ch4 refactor** per Neil (absorb the standalone DCont chapter; free-monoid
    stated in Ch3, reused in Ch4; + Abbott-simplify + S′/P′ dependency fix). The substantive item.
  - **LEAN** = **free-side MULT-backward + backward-uniqueness in CORE** (unblocked; do NOT wait on
    Mathlib; cofree Lean is a FUTURE cycle once Robin adds Mathlib).
  - **PROVE** = **the GROUPOID case of the ZS-merge obstruction** — does invertibility force `[ω]∈H²`
    to vanish (`Sk_C` contractible ⟹ merge always exists)? Diversifies the obstruction theory beyond
    the acyclic instances (all prior `[ω]` were over posets/DAGs) AND stages Neil's next-week
    social-networks-as-DCont (mutual-tie=groupoid merges free; follows-graph can obstruct). Computed
    clone of the supply-chain/orchestration template; general theorems cited not re-graded.

## 💤 2026-07-25 (dream) — cofree-UP pipeline consolidated; the two Ch6 UPs are one proof in a mirror
- Full pipeline ran since the 07-24 dream (browse → PROVE cofree-UP → LEAN MULT-fwd → WRITE Ch3/Ch6).
  Crown jewels banked live below (cofree UP proved; MULT-forward Lean'd). Dream job = fold in browse +
  LEAN + WRITE and extract the connection.
- **★★ CROWN JEWEL — free-monad UP (07-24) and cofree-comonad UP (07-25) are the SAME proof mirrored.**
  Both reduce **entirely to the (co)monoid laws of the object at the *given* end**: free's `ĝ` is a
  monoid hom because the **target** `M` is unital/assoc (base=unit, step=assoc); cofree's `ĝ` is a
  comonoid morphism because the **source** `D` satisfies D1–D5 (fwd←D1+D4, bwd←D2+D5, triangle←D3). The
  free/cofree object only supplies its (co)recursion principle; no law of it is re-proved. Coinduction is
  confined to **shapes** (M-type); positions are **vertices** ⟹ finitely inductive on BOTH sides, so the
  backward layer is identical. New connection [[free-cofree-up-reduces-to-given-laws]]; this is Ch6's
  syntax↔behaviour (μ↔ν, W↔M, induction↔coinduction) duality made into a single structural moral.
- **★ Browse: the H²-obstruction SIBLING-HUNT thread is FULLY CLOSED** (ran since 07-22, 4+ candidates).
  Mundey–Sims 2311.09600 full-text read: matched pair postulated **by fiat** (Def 3.1), ZS product exists
  **unconditionally** (Lemma 3.5) — completeness axis, NOT my existence axis. All four candidates
  (2405.10207 retracted, 2511.07906, 2503.08630, 2311.09600) cleared via direct reads. The operator-algebra
  ZS tradition assumes globally-compatible data; my (G)⟺[ω]=0 obstructs *local* data gluing — a genuine,
  now well-evidenced structural difference (sharpens the grant novelty claim). → [[cohomological-obstruction-family]].
- **★ Prior-dream source-depth flag DISCHARGED:** Spivak 2202.00534 v14 full-PDF re-read confirms BOTH
  adjunctions (eqs 244–264) as prior art — two anchors (GK 4.5 + Spivak), NOT a scoop. Mathlib `PFunctor.M`
  = Spivak's `𝔠p=lim p_k` inverse-limit tower, independently (no comonad structure on it yet = the Lean gap).
- **★ LEAN (this cycle):** `FreeUniversal.lean` MULT-**forward** (shape half) + `mult_assoc_shape` landed,
  `[Quot.sound]`-only, transport-free. MULT-**backward** + backward-uniqueness (position side) REMAIN.
  Registry child `mult-fwd-shape-lean`; `free-monad-universal-property` stays **proved** (paper complete,
  Lean partial). → [[lean-free-monad-unit-laws-done]].
- **★ LEAN session 3 (07-24):** both M-law **BACKWARD** extractions landed in `FreeUniversal.lean`,
  `[Quot.sound]`-only: `mult_left_unit_pos` + `mult_assoc_pos` (duals of `mult_left_unit`/`mult_assoc_shape`,
  via `onPos_congr`; `mult_assoc_pos` = one-liner, transport = literally `mult_assoc_shape`). These are the
  two inputs the MULT-backward law (§4.3) consumes; its **base case verified**, node step remains. File
  sorry-free (incomplete `freeExtPos_mult` NOT shipped). Registry child `mult-bwd-mlaw-inputs-lean` =
  **lean-verified**. Handoff `for-collaborator/free-monad-mult-backward-lean.md`.
- **★ WRITE (this cycle):** book **52pp** (was 40). Ch3 coequaliser hedge → cited **Proposition** (AAG
  2005 Prop 4.3 + Ex 4.4 swap-quotient witness) — **last Ch3 TODO closed**. Cofree couniversal property
  added to Ch6 as a Theorem (prior art tagged; cofree-Lean-blocked footnote). Free Lemma got Spivak
  2202.00534 as second anchor + Neil's `1+Σ` dictionary. → [[book-ch6-monads-comonads-drafted]].
- **The one blocker on Ch4/Ch6 M2 = infra:** add Mathlib to `lean/Containers` for `PFunctor.M`+`bisim`
  (cofree carrier). Robin/Neil call; do NOT re-attempt cofree in core Lean. Day: `dream-journal/2026-07-25.md`.

## 2026-07-25 (prove) — COFREE comonad couniversal property proved (dual of free-monad UP; Ch4 cofree milestone)
- **Deliverable:** `proofs/2026-07-25-cofree-comonad-universal-property.md`. `U:Comon(Cont)→Cont` has
  **right adjoint** `𝔠:p↦𝔠_p`; counit `ε_p`=read-root; induced comonoid morphism `ĝ:D⇒𝔠_p` by
  M-corecursion (`ĝ₁`=anamorphism), `ĝ♯` by finite path recursion using `⊕`.
- **Structural moral:** the couniversal property reduces to the SOURCE comonoid `D`'s five
  directed-container laws — fwd(shape) ← D1+D4 (Lemma U), bwd(position) ← D2+D5 (Lemma S),
  triangle ← D3; uniqueness-fwd=**coinduction** (finality of `tree_p`), uniqueness-bwd=path
  induction. Free↔cofree = W-type/M-type on shapes, **leaves/vertices on positions**; coinduction is
  confined to shapes, positions stay finitely inductive on BOTH sides (why positions=vertices matters).
- **Cor:** `⟦𝔠_p⟧(A)=Σ_t(vtx t→A)≅νZ.(A×⟦p⟧Z)` = cofree comonad on `⟦p⟧` (direct vertex count +
  `⟦−⟧` preserves the ω^op connected cofree tower, Ch3).
- **Prior art (cited, direct-read this session):** construction+theorem = Niu–Spivak Prop
  8.18/8.33/Thm 8.45 + Spivak 2202.00534 Eq.(244)–(249); contribution = the coordinate proof.
- **Verified** `scratch/cofree_up_verify.py` (walking-arrow `D`, nontrivial `g`; corecursion+triangle+
  Lemma U(20)+Lemma S(70)+comonoid law reassembled INDEPENDENTLY via ◁-on-morphisms(22+70)+uniqueness
  determinacy(20) to path len 4; 3 neg controls fire). Registry `cofree-comonad.json`=**proved** (validates).
- **Collaborator note** `for-collaborator/2026-07-25-cofree-comonad-universal-property.md`. **Next = LEAN**
  (portable backward/position layer now; shape layer awaits M-types — Mathlib `PFunctor.M` matches the tower).

## 2026-07-24 (wake-2) — daily answers Neil's 3 Ch4 Qs; Abbott coequaliser citation FOUND; triggers reset to a Ch4 cycle
- **Second wake since the 07-24 dream.** Inbox: 3 unread from Neil (UID 74/75/76), all marked read.
  UID 75 = the Ch4 "Monads and Comonads" 3-milestone spec (M1 initial-alg/final-coalg → Preliminaries;
  M2 W-types + connected-limit dual; M3 free-monad Lemma `Mon(Cont)→Cont` left adjoint `X↦m_X` with his
  explicit `(S′,P′)` formula). UID 76 = three direct questions, all answered in today's daily.
- **★ Morning daily SENT** (CC Robin), folding in answers to Neil's UID-76 questions:
  1. **S′ construction** — mine (`Free.lean` `PTree`/`leaves`) = his `1+Σ(s:S).(Ps→S′)` / `P′` **on the
     nose** (`lf=inl*`, `nd s κ=inr(s,f)` with `κ=f`, `P′=leaves`); fresh-read confirmed. Offered to adopt
     his explicit `1+Σ` presentation in the book prose.
  2. **Abbott coequaliser "further work"** — answered honestly: I hedged only because I couldn't verify the
     source, not the maths. **Then FOUND the reference myself** (seed direct-read): **AAG *Categories of
     Containers* FoSSaCS 2003, Prop 4.3 + Example 4.4** (swap-quotient counterexample: coeq in `Cont` =
     `(1,∅)`→const `1`, vs unordered pairs `(X×X)/∼` in `[Set,Set]`). Neil was right; VERIFIED QUOTE, not
     agent-summary → restore as cited theorem in Ch3, drop the hedge. → [[abbott-coequaliser-citation-found]].
  3. **"Patterns run on Matter"** = Libkind–Spivak **arXiv:2404.16321** (EPTCS 2025; 2410.08373 withdrawn).
- **★ Asked Neil the ONE blocker:** cofree comonad LEAN is infra-blocked (core `lean/Containers` has no
  coinduction) — is he happy for Robin to add Mathlib (`PFunctor.M`+`bisim`) so the cofree half of Ch4 M2
  can be formalised? The free side is the tractable side in core Lean; cofree is gated on this decision.
- **All 3 prior triggers were done/blocked** (free-monad UP proved; cofree LEAN blocked; Ch6 drafted).
  **Triggers RESET to a Ch4 cycle:** PROVE = **cofree comonad universal property** in container coords
  (coinductive dual of the free-monad UP; paper-advances the cofree half while its LEAN is blocked; hazard
  memory `cofree-comonoid-scooped-and-wrong` flagged — positions=vertices; 2202.00534 direct-read owed
  first). LEAN = **free-monad-UP MULT-homomorphism law + backward-uniqueness** in `FreeUniversal.lean`
  (unblocked; `onPos_congr` + `split`-bijectivity the keys). WRITE = **restore the Abbott coequaliser
  citation** in Ch3 + fold the proved free-monad-UP coordinate proof into Ch4/Ch6 + adopt Neil's `1+Σ`
  S′ presentation.

## 💤 2026-07-24 (dream) — Ch4 pipeline consolidated; free/cofree = one duality, literature hands us both halves
- Full pipeline ran since the 07-23 morning dream (browse2 → PROVE → LEAN → WRITE). Crown jewels banked
  live below (free-monad UP proved; Ch6 drafted). Dream job = fold in LEAN + WRITE + browse2 and extract
  the connection.
- **★ The Ch4/Ch6 duality is now half-proved, half-cited, and the asymmetry is real.** Free monad
  (syntax / W-type / μ) got **proved + partially Lean-verified** this cycle; cofree comonad
  (behaviour / M-type / ν) got a **citable recipe** (Spivak `2202.00534` limit tower `𝔠p=lim p_k`,
  `p_{k+1}=(p◁p_k)×y`) but is **Lean-BLOCKED**: core `lean/Containers` has no coinduction; needs
  Mathlib `PFunctor.M`+`bisim` (Robin infra call — the one blocker on Ch4 M2). No cofree Lean claim
  exists in the corpus. → [[lean-free-monad-up-partial-and-cofree-blocked]], [[browse-2026-07-23-browse2-key-finds]].
- **★ `2202.00534` reinforces (does NOT threaten) the free-monad-UP grade.** It presents `𝔪⊣U` as an
  *established* adjunction (ordinal colimit), consistent with GK 0906.4931 Thm 4.5. Theorem stays prior
  art; my contribution stays the **coordinate W-type proof**. WRITE should cite BOTH GK 4.5 AND
  `2202.00534` — two anchors, not a scoop. ⚠ **Source-depth flag:** `2202.00534` lines 3899–3995
  (free/cofree recipes) are an **arXiv-agent extraction, NOT a verified quote** (sources.json
  `verified-quote` only for ~10 Day-conv equations pp.3–4) → direct read of `~/papers/2202.00534.txt`
  owed before either recipe is load-bearing in the book.
- **★ LEAN (this cycle):** `FreeUniversal.lean` — full triangle + unit + object-uniqueness
  machine-checked (`[Quot.sound]`-only); MULT-homomorphism law + backward-uniqueness REMAIN. Registry
  `free-monad-universal-property` stays **proved** (added `lean_status`, NOT lean-verified). Reusable
  `ContainerMorphism.onPos_congr` (projection dual of `ext'`) = likely key to MULT-backward.
- **★ WRITE (this cycle):** §7.1 seed promoted to full **Ch6 "Monads and Comonads"** (48pp, compiles,
  placed after Ch5 DCont≅Cat). **Stripped the bogus `[MacBeth]` tag** off cofree theorem
  (= Niu–Spivak `2312.00990` Prop 8.18/8.33/Thm 8.45 prior art). Folds in the 07-24 free-monad-UP
  result tagged `[Cited: GK 4.5]`. → [[book-ch6-monads-comonads-drafted]].
- **Obstruction-family watch-list shrank:** sighting #5 (Mundey–Kwaśniewski `2511.07906`) + k-graphs
  `2503.08630` both CLEARED orthogonal via **direct full-text reads** — completeness axis (classify
  twists on a fixed ZS category), NOT my existence axis ((G)⟺[ω]=0). Do NOT re-flag. Only live sibling
  left = Mundey–Sims 2025a matched-pair cohomology (unread). → [[mundey-kwasniewski-cleared-orthogonal]].
- Day: `dream-journal/2026-07-24.md`; browse follow-ups in `questions/open-threads.md`.

## 2026-07-24 (prove) — Free-monad UNIVERSAL PROPERTY proved (Neil's Ch4 milestone-3 gap CLOSED)
- **★★ The one open gap of Ch4 milestone 3 is closed.** `U:Mon(Cont)→Cont` has a **left adjoint**
  `F:X↦m_X` (free-monad container), unit `α_X:X⇒U(m_X)` = insertion of generators. Container-coordinate
  proof by W-type induction: `α₁ s=nd s(λp.lf)`; induced `ĝ:m_X⇒M` by recursion (`ĝ₁ lf=e_M`,
  `ĝ₁(nd s κ)=μ_M(g₁ s, λq.ĝ₁(κ(g♯_s q)))`, `ĝ♯` mirrored via `μ_M♯`); proved (a) ĝ a monoid morphism,
  (b) triangle `α;ĝ=g`, (c) uniqueness. Artifact `proofs/2026-07-24-free-monad-universal-property.md`;
  registry node `free-monad-universal-property`=**proved** (validates). → [[lean-free-monad-universal-property]].
- **★ The structural moral:** the UP of the *free* monoid reduces, by induction on the tree, to the monoid
  laws of the *target* `M` — **base = M's unit law, step = M's associativity**, each in BOTH components. No
  law of M re-proved (M is given). Exact mirror of the grafting note (free monoid's own laws ↔ graft-assoc).
  Two fallouts: **triangle uses M's RIGHT-unit** (α = root generator + leaf children = right-unit config; the
  compute check independently reported this); **uniqueness of the backward map is FORCED by bijectivity of
  `split`** (Lemma A does double duty — multiplication AND uniqueness).
- **Part 2:** `⟦−⟧` strong-monoidal (Lean `⟦G◁F⟧=⟦G⟧∘⟦F⟧`) + AAG full-faithful ⟹ preserves free monoid;
  GK 4.5 (deep-read) completes "against all monads": `⟦m_X⟧(A)=μY.(A+⟦X⟧Y)`, free monad on `⟦X⟧`.
- **Honesty:** theorem = Gambino–Kock 4.5 (prior art); contribution = the coordinate PROOF (the piece the
  grafting note's §6 gap #3 left open). Part 1 self-contained on Lean-verified carrier+laws+induction; Part 2
  rests on AAG+GK (flagged §9). Verified `scratch/free_monad_up_verify.py`: Writer(ℤ/3), Reader (nontrivial
  backward), free `m_Y`; triangle+both MULT comps+uniqueness; 306 exhaustive `(t,u)`; negative controls fire.
- **Collaborator note** `for-collaborator/2026-07-24-free-monad-universal-property.md`. **Next = LEAN** (ĝ as
  PTree recursor ⟹ first end-to-end machine-checked free-monad adjunction incl. UP).

## 2026-07-23 (wake-2) — Neil pivots to Ch4 "Monads and Comonads"; arXiv:2511.07906 VERIFIED orthogonal; triggers reset to a Ch4 prove→lean→write pipeline
- **Second wake since the 07-23 dream.** Inbox: two unread from Neil. **Ch1–3 signed off "done for now"**
  (Abbott TODO already reworded). **★ NEIL'S NEW DIRECTIVE: next chapter = "Monads and Comonads"**, with a
  detailed 3-milestone spec (M1 initial algebras/final coalgebras + accessible functors → Preliminaries;
  M2 W-types `W S P=μY.(S,P)`, dual via connected-limit preservation; M3 free-monad Lemma: `Mon(Cont)→Cont`
  has left adjoint `X↦m_X`, `⟦m_X⟧`=free monad on `⟦X⟧`, explicit `m_(S,P)=(S′,P′)`). Also: social-networks-
  as-DCont (he explores next week), supply chains present categories, KGs→Spivak ologs. → [[neil-ch4-monads-comonads-steer]].
- **★ Milestone-3 is ALREADY proved + Lean-verified in my corpus.** A reconciliation agent confirmed Neil's
  `m_(S,P)=(S′,P′)` formula is `Free.lean`'s `PTree`/`leaves` construction ON THE NOSE (dictionary:
  `inl*↦lf`, `inr(s,f)↦nd s κ`, `P′↦leaves`). So Ch4's central Lemma ships with a Lean citation. The ONE open
  gap = the *universal property* (left-adjointness of `X↦m_X`; grafting note §6 gap #3). Cofree comonad is
  paper+Python only — NOT Lean-verified anywhere (highest-value missing artifact). Book already has a §7.1
  seed (l.1810–1892) to promote; ⚠ its `[MacBeth]` tag on `thm:cofree-dircont` must be STRIPPED (cofree =
  Niu–Spivak 8.18/8.33/8.45 prior art).
- **★ Consolidated reply sent to Neil** (CC Robin) — acknowledged the steer, flagged milestone-3 as done+Lean,
  laid out the chapter plan, asked whether applications-outlook advances now or waits behind the book.
- **★ arXiv:2511.07906 (Mundey–Kwaśniewski) direct-read DONE → VERIFIED ORTHOGONAL, not a sibling/scoop.**
  Both say "H² of a ZS product category" but they *classify T-valued twists on an EXISTING* ZS category
  (completeness), whereas mine is an *obstruction to EXISTENCE* ((G)⟺[ω]=0). Real follow-up = **Mundey–Sims
  2025a matched-pair cohomology** (the actual potential sibling); stop re-flagging the C*-paper. →
  [[mundey-kwasniewski-cleared-orthogonal]]. Direct-read gate held (prior lookalike 2405.10207 was a hallucination).
- **Triggers RESET to a Ch4 pipeline:** PROVE = free-monad universal property (left adjoint `X↦m_X`, the one
  open piece; GK 0906.4931 Thm 4.5 anchor); LEAN = **cofree comonad as ◁-comonoid** (dual of `Free.lean`;
  Mathlib `PFunctor.M` carrier + `bisim`; honest fallback ladder to finite-depth if the project is Mathlib-free);
  WRITE = draft the "Monads and Comonads" chapter (promote §7.1, add M1/M2, fold in PROVE, strip the cofree tag).

## 💤 2026-07-23 (dream) — 07-23 pipeline consolidated; applications spine = one H² theorem, three instances; a possibly-genuine ZS/H² sibling (UNVERIFIED)
- Full pipeline ran since the 07-22 dream (wake/prove/write + browse; lean no-op). Crown jewels banked
  live below (supply-chain ZS computed / Z/n; Ch1–3 closed; applications staged). Dream job =
  consolidate the PROVE + browse and correct one stale citation.
- **★★ The applications spine is now ONE theorem with three instances, PROVED not analogized.** Hinge
  `DCont≃Cat` (lean-verified `DContCat.lean`) ⟹ anything presenting a small category is a directed
  container; composing any two = ZS product `C⋈D`, obstructed by the *same* class `[ω]∈H²(Sk_C;𝒟)` as
  orchestration re-entrancy (`Reentrancy.lean`). Supply-chain composability / ontology-merge / agent
  re-entrancy = one degree-two obstruction; 07-23 PROVE refined the token Z/2 bit → Z/n unit-count
  (`n=2` = the proved orchestration bit, cite don't re-grade). → [[applications-are-directed-containers]],
  [[supply-chain-zs-computed]].
- **★ Browse's real event — a CANDIDATE 5th sibling to `(G)⟺[ω]∈H²`, from operator algebras:**
  Mundey–Kwaśniewski **arXiv:2511.07906** claims T-valued twists "exhaust the second cohomology of the
  associated Zappa–Szép product category" — at abstract level almost exactly my framing, from the
  self-similar-groupoid / C\*-algebra tradition (NOT Baues–Wirsching). Closest literal match in ~10
  sessions. **agent-summary ONLY; hard direct-read gate** (the last identical-looking claim, 2405.10207,
  was a WebFetch hallucination). Added as sighting #5 to `connections/cohomological-obstruction-family.md`
  with the gate; k-graphs 2503.08630 added as a recurring adjacent skim. Direct read = tomorrow's top item.
- **Negative controls held:** applications novelty sweep (4 angles) CLEAN — no prior art on
  ologs/KGs/supply-chains-as-DCont; Path-5 orchestration territory filling (Waites Plumbing/traces #4th
  effort, Myers/Capucci "contextads," Banu) but **none use ZS/Poly/H²** — differentiator holds.
- **Infra:** Google Groups "categories" now blocked (3rd forum lost after MO/nForum); research-MCP
  `arxiv_*` still dead (WebFetch fallback works). Both flagged to Robin. Day: `dream-journal/2026-07-23.md`.

## ★ 2026-07-23 (PROVE) — supply-chain composition = Zappa–Szép product, COMPUTED; obstruction generalized Z/2 → Z/n

Staging for Neil's applications turn (does NOT touch the book). Cloned the proved orchestration
template (`orchestration-zs.json`) into the supply-chain / olog domain and **generalized the token
from Z/2 to Z/n** — supply-chain bookkeeping is a cyclic *lot-cursor*, so the obstruction lands in
Z/n and measures the discrepancy *in units*, not merely a parity bit. Three deliverables, all
machine-checked in `scratch/supply_chain_zs.py`, written up in
`proofs/2026-07-23-supply-chain-zs.tex` (compiles, 5pp):
- **(A) Object level.** `procure→manufacture→ship` as a poset category `C₀`, written out as an
  explicit directed container `(S,P,o,↓,⊕)` via the lean-verified DCont≃Cat hinge; **D1–D5
  machine-checked** exhaustively. (Orchestration stayed category-level; this is the new object-level
  content — greenfield in the corpus.)
- **(B) Composition = ZS.** Warehouse family `W_{n,ε}` (`s·p=q`, `s₂·p=q·τ^ε`), right factor
  `D=Z/n` internal relabelings. Verified (L),(H); `Sk_C = Wh→Pr⇉De` (ε-independent); presheaf
  restrictions 0; `C³=0 ⟹ H²(Sk_C;Z/n)=(Z/n)²/diag ≅ Z/n`; defect `ω_T=(0,ε) ⟹ [ω]=ε`. So
  **`C⋈D` exists ⟺ ε=0 ⟺ both routes to the same delivered good agree on lot-provenance.**
  Independent cross-check: `#SFS = n` (ε=0, a Z/n-torsor of canonical labelings) / `0` (ε≠0).
  **n=2 reproduces the PROVED orchestration re-entrancy bit** — cite, don't re-grade.
- **(C) Olog sibling.** `Book→Author→Name` olog as directed container (D-laws checked); merge along
  shared `Author` = ZS composition; naming-convention clash (Z/2) = nonzero `[ω]` = merge conflict.

**Grade discipline:** general theorems (DCont≃Cat lean-verified; pairwise-ZS, (G)=H², orchestration
all proved) CITED as shared stubs, never re-graded. The domain instantiation is **computed**.
Object-level "a real supply chain *is* this category" stays **open** (SEED Q4) — faithful
abstraction, not a fidelity claim. Registry `supply-chain-zs.json` (status computed, validates clean
`--root .`). The grant line: supply-chain composability, ontology-merge consistency, and agent
re-entrancy are the **same degree-two obstruction**, refined here from a bit to a Z/n unit-count.
Handoff: `memory/for-collaborator/2026-07-23-supply-chain-zs.md`.

## 2026-07-23 (wake) — ★ Ch1–3 CLOSED (Neil's week-goal met); registry "rot" was a FALSE alarm; applications staged for Robin
- **Morning email to Neil SENT** (CC Robin, one/day): reported the classification folded into the book +
  today's plan to close Ch1–3; asked whether he considers Ch1–3 done after the last edit. **Inbox:** one
  unread from Neil (Re: Away today) — no reply owed; steers: **close Ch1–3 this week**; **ologs** = the
  knowledge-graph pointer; **directed-containers / supply-chain-as-category on deck NEXT week**. No registry events.
- **★ Ch1–3 are now CLOSED.** Audit agent: book compiles clean at **40pp**, zero undefined refs, **exactly
  ONE live gap** — a Ch3 `\prov` TODO (l.620) deferring an *unverified* "Abbott's thesis" coequaliser
  reference. Per Neil's no-moonshot discipline I **reworded it to clean further-work** (the mechanism —
  quotients add position automorphisms ⟹ analytic/species functors outside ⟦–⟧ — is already argued in the
  prose; dropped the promised theorem-number + unverified source). Recompiled: clean, 40pp, 0 undefined.
  Pending only Neil's confirmation that no extra Ch1–3 content is wanted.
- **★ Registry "128 dangling reading-log refs" (flagged 07-23 as hygiene debt) was a FALSE ALARM — do NOT
  prune.** Diagnose-first agent: the sources are **live**; the failure was an **invocation bug** in my own
  canonical command — `--root memory` double-prepends `memory/`, misresolving the repo-root-relative `read`
  paths (the lone `proofs/…` read ref is decisive). With **`--root .`**, `closed-tensor-classification.json`
  AND `equivalence-chain.json` validate **0 problems**. Fixed the command in `PROGRESSIVE_DISCLOSURE.md`.
  Averted deleting live references. → [[registry-root-flag-false-alarm]].
- **★★ Applications staging (grant Path-5 spine) — greenfield, sent to Robin (who starts applications today).**
  Survey confirmed: NO existing note connects ologs / knowledge graphs / supply chains to DCont beyond
  analogy; the hinge **DCont ≃ SmallCat is lean-verified** (`DContCat.lean`; `equivalence-chain` legs). So
  *anything presenting a small category is a directed container*: ologs (Spivak schema; KG instance = functor
  to Set) are DCont definitionally; supply chains are DCont iff they present a category (SEED Q4, object-level
  OPEN; morphism level ours = cofunctor/lens). **The payoff is ours and proved:** composing them = Zappa–Szép
  `C⋈D`, exists ⟺ `(L)∧(G)`, fails ⟺ `[ω]∈H²` — the **SAME obstruction class as orchestration re-entrancy**
  (`Reentrancy.lean`). Supply-chain composability / ontology-merge consistency / agent re-entrancy = one H²
  theorem, three instances. Staging map `for-robin/2026-07-23-ologs-supply-chains-as-directed-containers.md`
  (honest-status table) emailed to Robin. → [[applications-are-directed-containers]].
- **Triggers reset for the applications turn (staging; Ch1–3 banked):** **PROVE** = minimal supply-chain
  ZS instance (`procure→make→ship`; two chains sharing a node → `C⋈D`; `[ω]` obstruction table), computed,
  cloning `orchestration_zs*.py` — SEED-Q4→computed. **WRITE** = polish the staging note into a standalone
  `papers/applications-outlook.tex` (NOT into the book; flag for Neil); fold in PROVE's instance if it lands.
  **LEAN** = trigger file DELETED (no in-scope proved-but-unformalised target; lean no-ops this cycle).

## 2026-07-24 (PROVE) — arity gap NOT closed, but sharply characterized as genuine open problem
- **Deliverable:** `proofs/2026-07-24-arity-gap-further-work.md` (honest Further Work, per Neil's
  "no moonshots" steer). Registry `closed-tensor-classification`: `gap-infinite-arities` stays
  **speculative**; added 3 proved child nodes (Lemma A / Prop B / Prop C). Validates clean.
- **★ Main finding — counting is provably blind to the gap.** (Prop C) the associativity arity
  recursion `A_{C⋆B,(b,φ)}=Σ A_{C,φ(i)}` is a FIXED POINT at infinite seed: `R_2=y+y^λ` →
  `R_{2⋆2}=y+2^λ·y^λ`, associator `(X⋆2)⋆2≅X⋆(2⋆2)` genuine natural-in-X iso. So cardinality /
  arity-recursion / one-variable-naturality CANNOT obstruct — explains the multi-session stuckness.
  Finite seed n≥2 grows n→n²→… (re-derives Key Lemma). `scratch/arity-gap/recursion_selfconsistency.py`.
- **★ Reframing.** (Lemma A) affine = preserves connected COLIMITS; (Prop B) closure ⟺ preserves
  connected LIMITS only (via `Cont≅Fam(Set^op)`), and these are INDEPENDENT — no categorical
  shortcut, bounded case worked only by `κ²>κ`. §6 of the 2026-07-23 classification updated to point here.
- **Now believe the conjecture may be FALSE** (an infinite-arity closed convolutional tensor could
  exist). Precise remaining target: does `R_2=y+y^λ` admit an all-variable-natural associator
  satisfying pentagon? Element-level coherence, NOT counting. Collaborator note written.
- Search agent (scratch/arity-gap/) reconfirmed: NO finite/bounded arity-≥2 tensor (only `×`,`∨_S`);
  no unbounded construction survived {unit,symmetry,assoc}, none proven impossible.

## 2026-07-23 (wake) — daily sent; ALL 3 prior triggers audited DONE; Neil sets chapters-1–3 as the week's goal
- **Morning email to Neil SENT** (CC Robin, one/day): reported the closed-tensor CLASSIFICATION
  (bounded arity: closed convolutional tensors on Cont = exactly `⊗` and the `▷_S` family; ⚠ unbounded
  arity is the one open gap), the `×/+` Lean cell, and the collapse tensor folded into book Ch3.
- **★ NEIL'S STEER (uid "Away today", offline today; back tomorrow): the week's strategic goal is to
  CLOSE OUT chapters 1–3. Anything incomplete → write as "Further work," do NOT chase moonshots.**
  Acknowledged in the daily. Robin: starting tomorrow he moves to supply-chain + knowledge-graph
  applications of container theory. Inbox otherwise empty.
- **Audited all 3 prior triggers vs disk (grades not prose) — ALL DONE.** PROVE = the closed-tensor
  classification (`2026-07-23-…-classification.md`, 13KB; registry `closed-tensor-classification` root
  `in-progress`, `main-theorem-bounded`=proved, `gap-infinite-arities`=speculative — honest). LEAN =
  `TimesCoprodDistrib.lean` sorry-free + imported + `cell-x-plus`=lean-verified. WRITE = collapse tensor
  live in book `sec:closed` (`def:collapse`/`prop:collapse`/teachbox), vacuity conjecture retired.
- **⚠ Registry hygiene flag:** `trustcheck` on `closed-tensor-classification.json` FAILS with 128
  problems — ALL of one class: `sources[...] read file missing: memory/reading/*.md` (dangling
  reading-log references in `sources.json`; likely pruned). ZERO problems touch any proof node. Flagged
  to Robin in the daily; offered to prune dangling source entries in a dream cycle. Not blocking.
- **Triggers RESET, all pointed at closing chapters 1–3 (sequenced prove→lean→write):**
  PROVE = BOUNDED attempt at the arity gap (exclude κ≥2 via associator-naturality / taut+★'), deliver
  the unconditional theorem OR a crisp "Further work" statement that WRITE folds in — no moonshot.
  LEAN = the ×-monoid CONVERSE (mirror `DirichletMonoidConverse.lean`) → full iso, closes the ×
  column of the Ch3 (co)monoid table both sides. WRITE = fold the CLASSIFICATION into book Ch3
  `sec:closed` (biconditional → collapse witness → classification payoff), unbounded arity as Further
  work per Neil.

## 💤 2026-07-22 (dream) — day's pipeline consolidated; collapse tensor refutes yesterday's crown jewel
- Full pipeline ran since the 07-21 dream (wake/prove/lean/write + browse). Crown jewels banked live
  below (vacuity FALSE / collapse tensor; `×/+` Lean cell; collapse folded into book Ch3). Dream job =
  consolidate the PROVE + browse and update the notes that yesterday's *conjecture* had made stale.
- **★★ Yesterday's "closure is free inside the Day family" is REFUTED.** Updated
  `topics/monoidal-structures-on-cont.md` (vacuity subsection rewritten: RESOLVED FALSE, collapse tensor +
  η-cartesian locator), and `connections/polynomiality-is-provenance-is-coherence.md` already carried the
  refutation banner. The slogan survives as intuition; the "free closure" reading is dead.
  → [[vacuity-false-collapse-tensor]]. **Discipline note:** a conjecture consolidated as a crown jewel one
  night can be a *witness* the next — being wrong here produced a cleaner book result (concrete counterexample
  for where the side-condition bites) than the hedge would have.
- **★ Browse crown find — ⚠️ RETRACTED (07-22 browse2): this was a WebFetch hallucination.** The "Sec-4
  cohomological obstruction" below does NOT exist in the paper (direct-text grep: zero H²/cohomology hits;
  Remark 4.16 leaves the categorified question OPEN). Downgraded out of the obstruction-family cluster;
  NOT a sibling, NOT a scoop. Kept here only as the cautionary precedent for the 07-23 #5 candidate.
  arXiv:2405.10207 (Müller–Peña Pollastri–Plavnik) — bicrossed products of **fusion categories**, exact
  factorization `E=C·D ⟺ C⋈D` with a Sec-4 **cohomological obstruction**. Same characterization shape as my
  pairwise-ZS, one categorical level up; if H²-valued, same *axis* as `(G)⟺[ω]∈H²` (existence of a
  factorization), unlike the H⁰/H¹ agent-sheaf cousins. Added as sighting #4 to
  `connections/cohomological-obstruction-family.md`. **⚠️ agent-summary/PDF-extraction only — HIGH-PRIORITY
  verified re-read owed before any cite** (HTML 404'd, theorem numbers unconfirmed).
- **★ Book-write blocker surfaced:** n-Café 2009 "Deviant Relatives" (Baez–Stay; Theo/Cisinski currying-
  vacuously examples) is a 17-yr precedent for the collapse-tensor genus. **Cite-or-distinguish before the
  Ch3 vacuity example ships** — do their examples share collapse's `η_B` non-injectivity? Cheap check owed.
- **Refined PROVE target (Neil-gated):** characterize which convolutional `⋆` ARE left-closed (candidate =
  taut/η-injective + ★'). Details in `questions/open-threads.md` (07-22 block); day in `dream-journal/2026-07-22.md`.

## 2026-07-22 (wake) — daily sent; all 3 prior triggers confirmed DONE; triggers reset; bib fixed
- **Morning email to Neil SENT** (CC Robin, one/day): reported the 07-22 crown jewels — vacuity FALSE
  (collapse tensor), `[ω]=ε` now in Lean, orchestration note compiles — and asked his steer on the
  refined PROVE target (characterize left-closed convolutional = taut monoidal ⋆). **Inbox EMPTY**
  (Neil UID-71 already answered 07-21; no reply owed).
- **Audited the 3 prior triggers against disk (grades not prose): ALL DONE.** LEAN `[ω]=ε` =
  `Reentrancy.lean` sorry-free, wired in, registry `lean-omega-equals-epsilon` = lean-verified.
  WRITE `containers-for-orchestration.tex` compiles (639 lines, PDF) — already had a 17-item
  `thebibliography`; a verify-agent CAUGHT + FIXED real attribution bugs: **Banu cite pointed to the
  WRONG paper** (2607.04240 → correct **2605.12239 "Harness Engineering as Categorical Architecture"**)
  + author-name typos + truncated Aberlé title; recompiled clean. PROVE = collapse-tensor result
  (already banked below).
- **Shared collapse-tensor proof with Rick** (CC Robin, attachment) — bears on the census he endorsed
  (convolutional ⊋ left-closed; ⋉/⋊ = same moral from outside the Day family).
- **★ INFRA BUG flagged to Robin** (`for-robin/2026-07-22-research-mcp-arxiv-broken.md`): the research
  MCP `arxiv_*` tools are DEAD (http→https 301 redirect the client won't follow) — degrades browse.
  Workaround = WebFetch `https://export.arxiv.org/api/query`. One-line server fix (follow_redirects).
- **Triggers reset:** PROVE = KEPT (characterize left-closed convolutional tensors; sub-goal taut+★'⟹
  wide-pullback; Neil-gated, I asked). LEAN = FRESH `×/+` Hedges cell `(P+P')×Q≅(P×Q)+(P'×Q)` (clean
  sibling of `⊗/+`; stretch = ⋊ left-closed adjunction). WRITE = FRESH — fold the collapse tensor into
  book Ch3 closed-structures as THE example the side-condition bites (do NOT ship vacuity as conjecture).

## ★★ 2026-07-22 (PROVE) — closure-vacuity RESOLVED: it is FALSE (the collapse tensor)
- The 07-21 "Vacuity Conjecture" (below) was **WRONG**. Deep-work PROVE session found a genuine
  monoidal counterexample: the **COLLAPSE TENSOR** `A⋆B := B if A=∅ / A if B=∅ / 1 if A,B≠∅`
  (unit ∅, symmetric). It is truly monoidal (natural associator + pentagon + triangle + unitors +
  braiding; emptiness-pattern proof + exhaustive size≤3 — hostile-refereed vs the support-tensor
  precedent). `R_2=(−)⋆2` **non-polynomial** (`R_2(∅)=2 > 1=R_2(1)`; poly ⟹ `|F(∅)|≤|F(1)|`).
  So `⊙_collapse` on Cont is **convolutional but NOT left-closed**: **convolutional ⊋ left-closed**.
  Answers Neil's "lucky with ⊗,×" = YES. `proofs/2026-07-22-vacuity-resolved-collapse-tensor.md`;
  registry `closed-day-structures.condition-vacuity` now **proved (NO)** & validates.
- Mechanism = **unit insertion `η_B` non-injective ("×1 shrinks")** — a mechanism the 07-21
  three-candidate search never considered (it only hunted support's phantom-extra). Built an
  **η-cartesian framework** that LOCATES all counterexamples: **Lemma D** (assoc input, proved) +
  **★'** (structural: balanced⟹independent ⟺ η cartesian, CAN fail). Monoidal counterexample ⟺
  Lemma D holds ∧ ★' fails; collapse realises it, support is the mirror. Global memory
  [[vacuity-false-collapse-tensor]]; collaborator note asks Neil the refined target (characterize
  left-closed convolutional = monoidal ⋆ preserving connected limits per variable; necessary =
  taut/η injective + ★'). The `polynomiality=provenance=coherence` slogan survives as intuition
  but the "closure is free" reading is dead.
- **Book Ch3 impact:** state the biconditional, then give the collapse tensor as THE example the
  side-condition bites — do NOT ship "vacuity" as a conjecture (it's false).

## ⚠️ 2026-07-21 (wake-2) — LNV novelty debt CLEARED (no ⋉/⋊ scoop); triggers reset fresh
- Second wake after the 07-21 full pipeline. Morning email to Neil SENT (CC Robin, one/day): reported
  the closure-vacuity crown jewel + Π-form Lean iso + book closed-structure section + Path-5 browse;
  asked whether to ship the Ch3 vacuity result as a stated conjecture or hold for the open half.
  **Inbox EMPTY** (Neil's UID-71 already answered in wake-1) — no reply owed.
- **★ LNV 2405.07724 read IN FULL (v4) → novelty debt CLEARED, ORTHOGONAL, no ⋉/⋊ scoop.** Their
  tensor = product-in-base + fibre-tensor + pullback reindexing; **the Dialectica twist is in the HOM,
  not the tensor** — my ⋉/⋊ put the twist in the tensor (Π-pushforward `p[s]^{S_q}`) ⟹ non-convolutional,
  outside the Shulman–LNV template. **CORRECTION: their closure theorem is 9.19, NOT 9.17** (9.17 = a
  Lax-comma example) — fix any cite. No duoidal/LDC content ⟹ my (Poly,⋉,⋊,y) result absent there.
  Reading note `reading/2026-07-21-lnv-2405.07724.md` (has the cite-and-distinguish one-liner); global
  memory `lnv-2405-cleared-thm-919.md`. Debt list now: SS 2407.01849, Niu 2022 Zulip remark.
- **Triggers RESET (prior LEAN/WRITE were STALE — both done 07-21; audited on disk):**
  - **PROVE** (KEPT + sharpened) = closure-vacuity OPEN CORE (surjective half of two-point-pullback
    preservation). Sharpest lead added: *lift the `support`-tensor refutation (already an
    associator-naturality argument) to an arbitrary monoidal ⋆*.
  - **LEAN** (fresh) = the orchestration obstruction `[ω]=ε` as finite 𝔽₂ linear algebra (`ZMod 2`
    quotient `C2/diag`, or membership form `omega ε ∈ range d1 ↔ ε=0`) — grant-Impact, tractable,
    transcribe the complex from `proofs/2026-07-20-orchestration-reentrancy-obstruction-analytic.tex`.
  - **WRITE** (fresh) = finish `papers/containers-for-orchestration.tex` (Path-5 crowding: cite
    Aberlé/ArchAgents/Waites as the mechanism/orthogonal efforts, none use ZS/Poly/H² — the delta is
    `C⋈D` + `[ω]∈H²`; cite the Lean `[ω]=ε` if LEAN lands).

## 💤 2026-07-21 (dream) — day's pipeline consolidated; crown jewel = provenance=polynomiality=coherence
- Full pipeline ran since the 07-20 dream (wake/prove/lean/write + browse). Crown jewels banked live
  below (Π-form Lean iso; Neil UID-71 answered; closed-structures book section). Dream job = consolidate
  the PROVE session + browse, and extract the connection.
- **★ CROWN JEWEL — `polynomiality = provenance-tracking = coherence`** (new connection
  [[polynomiality-is-provenance-is-coherence]], from `proofs/2026-07-21-closure-condition-vacuity.md`).
  A polynomial functor records per-output which inputs it uses (fibre exponent = provenance); monoidal
  **coherence forces exactly that**. So the closure side-condition looks **vacuous**: a non-left-closed
  convolutional tensor would have to lose provenance, and every way to do so breaks a *different* axiom
  (`max`→interchange; support tensor→associator naturality; `Sym²`→associativity-by-growth). Bridges
  Path 3 (closure) ↔ Path 1 (poly = connected-limit preservation, GK 0906.4931) ↔ coherence theory.
  Banked reusable **retraction lemma** (proved; injective half of two-point-pullback preservation).
  **Vacuity Conjecture stays a conjecture**; open core = the surjective half ("agreement ⟹ first-slot
  independence"). Unit-terminal ⟹ `⋆=×` modulo one Fox-theorem step. Registry
  `closed-day-structures.condition-vacuity` = open (children proved/refuted) — summary & registry agree.
- **★ DICHOTOMY for the book:** inside the Day family closure is (conjecturally) free; the only non-closed
  tensors on `Cont` are the non-convolutional `⋉/⋊` (Dialectica line). Two results, one sentence.
- **Browse:** Path-5 territory filling in — Waites n-Café (Mar 2026) plumbing-language + traced-monoidal
  inner/outer-trace, 3rd categorical-orchestration effort, **none use ZS/Poly** (mechanism stays
  differentiated; finish `containers-for-orchestration.tex` sooner). Novelty debts still unread: LNV
  2405.07724 Thm 9.17 (⋉/⋊-non-closure neighbour, agent-summary), SS 2407.01849 overlap. No ACT-2026 scoop
  (Neil's "Snoc Trees", Braithwaite–Hedges–Mihejevs "Polylang" among 44 accepted). Details:
  `dream-journal/2026-07-21.md`; leads in `questions/open-threads.md` (07-21 block).

## ★ 2026-07-21 (lean) — Π-form=morphism-form gap CLOSED in Lean (sorry-free, axiom-free)
- **`Container.ihomPiIso : ihom q r ≅ Πᵢ (r ◁ q[i]·y)`** — `DirichletHomPi.lean`, wired into root,
  `lake build` clean (0 err/warn), **no axiom dependency** (`#print axioms`). Closes the exact gap the
  wake session flagged below ("only ⊗ Lean-verified via morphism form; Π-form unformalised"). The Π-form
  is now machine-verified to be the *same container* as the morphism form; the closed structure on
  `(Cont,⊗,y)` may be read off the uniform formula.
- **Predicted transport DIDN'T materialise:** LEAN.md budgeted `heq_sigma_mk`/`SeqProdDistrib` template for
  a "propositionally-invertible choice"; instead both round trips are `rfl`, definitional under
  structure/`Sigma`/`Unit`-eta. New reusable defs: `Container.monomialY (A·y)`, `Container.piCont`
  (arbitrary-index container product, no Fintype — binary `prod` = `Bool` case).
- **Scope:** container identity only; the adjunction stays `Container.dirichlet_closure`. Only `⋆=×`
  formalised; general Day-tensor closure + vacuity still paper/open. Registry: added `lean-verified` child
  `pi-form-equals-morphism-form` under `uniform-closure-formula`. → note in `for-collaborator/2026-07-21-lean-dirichlet-hom-pi-form.md`.

## ★ 2026-07-21 (wake) — Neil UID-71 answered in full; closed-structure scepticism RESOLVED; triggers reset fresh
- **Both prior triggers were STALE (already done):** ×-monoid converse = full Lean iso
  (`TimesMonoidConverse.lean`, sorry-free), orchestration-zs = `proved` (analytic obstruction). Audited
  against registry (grades, not prose). Today genuinely open; Neil's UID-71 set the agenda.
- **★ Sent ONE consolidated substantive reply to Neil (CC Robin)** answering every question in UID 71:
  - **Closed structure spelled out — Neil was right to be sceptical, and it resolved cleanly.** His
    correction (internal hom = MORPHISM form `[q,r]=(Cont(q,r), f↦Σ_t r[f(t)])` = NS Eq 4.79) is the
    honest presentation and = what `DirichletClosed.lean` verifies. **My Π-form is the SAME container**
    (`ΠΣ≅ΣΠ`; numerically CONFIRMED 9/9, `scratch/dirichlet_hom_verify.py`). His right-Kan objection
    answered EXACTLY: `(Cont,⊙_⋆)` left-closed ⟺ `(−)⋆B` polynomial ∀B — the "when is the right Kan a
    container" condition. Honest caveats given: only ⊗ Lean-verified (via morphism form; Π-form
    unformalised); 3 concrete closures are prior art; **vacuity of the condition is OPEN**. →
    [[closed-structures-are-spivaks]] (07-21 update).
  - **⋉/⋊ = Dialectica, detailed for Neil to check** (gates the Nelson Niu email — HELD pending his OK):
    formulas, Hmg(2)≃Dial(Set) dictionary, ⋉=de Paiva symmetric ⊗ / ⋊=directed variant, the
    additive-vs-multiplicative conjunction split, non-convolutional ⟹ outside Day family. Framing rule
    + neighbours (LNV 2405.07724, Capucci MFPS24) restated. → [[ltimes-rtimes-are-dialectica]].
  - **Ch1–3 lit-sweep = CLOSED** (concluded, Neil agreed). **Editorial:** orchestration OUT of the book
    (his hard instruction; he writes the standalone note); (co)monoid table → END of Ch3. →
    [[neil-steers-2026-07-21]].
- **Triggers RESET fresh:** PROVE = closure-condition VACUITY (is there a monoidal `(Set,⋆)` with
  `(−)⋆B` non-polynomial? — resolves `closed-day-structures.condition-vacuity` either way, answers
  Neil's "lucky with ⊗/×"); LEAN = `ihom q r ≅ Π_i r◁(q[i]·y)` (formalise the Π-form=morphism-form
  `ΠΣ≅ΣΠ` iso — closes the unformalised-Π-formula gap); WRITE = Ch3 closed-structure section for the
  BOOK (morphism form → Π repackaging → biconditional/representability condition → honest prior-art).

## ★ 2026-07-20 (prove) — re-entrancy obstruction PROVED analytically; orchestration-zs computed→PROVED
- **`[ω(K_ε)] = ε·(generator)` in `H²(Sk_C;D) ≅ ℤ/2`** — the degree-two obstruction class *equals* the
  token-mutation bit. Parametrized the supervisor–worker category by `ε∈ℤ/2` (`s₂∘p = q·τ^ε`);
  **Corollary:** `K_ε = C⋈D` (distributive law / serializable joint agent) exists **iff `ε=0`, iff the
  worker fixes the supervisor turn token**; `ε=1` ⇒ obstruction = nonzero generator = unprotected re-entrancy.
- **Analytic, not enumerated:** killed the machine-verified `K_bug≅rigid-twist` iso and the brute `#SFS`
  counts. Verify (L)+(H) for `K_ε` by hand, apply the *general* (T3) `(G)⟺[ω]=0` classification (rigid
  twist was only its *example* — no circularity), compute `Sk_C`/presheaf/complex(`C³=0⇒H²=(ℤ/2)²/diag`)/defect
  `ω_T=(0,ε)` directly, chain (T2)+(T3). Iso-to-rigid-twist now a corollary/remark.
- Artifact `proofs/2026-07-20-orchestration-reentrancy-obstruction-analytic.tex` (6pp, compiles); cross-check
  `scratch/orchestration_zs_parametrized.py`; registry `orchestration-zs.json` **status `proved`** (validates);
  collab note `for-collaborator/2026-07-20-orchestration-reentrancy-obstruction-analytic.md`. This is the
  **surviving-novelty ZS/H² layer** (Aberlé has the mechanism, not the obstruction) — grant-Impact anchor.
  Illustrative regimes (indep→C×D, coherent→S₃) stay *computed context*; no new cohomology; minimal faithful
  abstractions (no "framework IS K_ε"). **Next:** Lean the `[ω]=ε` computation (finite 𝔽₂ linear algebra).

## ⚠️ 2026-07-21 (wake) — Aberlé read: orchestration MECHANISM is prior art; ZS/H² layer survives; triggers reset
- Second wake in the 07-20/21 window after a full pipeline ran. Inbox EMPTY; today's daily to Neil was
  already sent this morning (wake-2) — respected one-email/day (Aberlé finding folds into tomorrow's).
- **★ Aberlé arXiv:2604.01303 READ IN FULL** (cheap-win, before the orchestration write went load-bearing).
  Verdict: the poly-interface / free-monad-on-Poly-implementation / dependent-poly-spec / wiring-diagram
  MECHANISM is **prior art (Thms 3.1, 5.3, Def 7.1)** — "theorem-proving-as-container" and
  "orchestration-as-workflow" are a domain REINTERPRETATION, not a new mechanism (cite prominently). But
  Aberlé has NO Zappa–Szép / distributive law / interaction obstruction / cohomology (his only two-system
  construct is the UNOBSTRUCTED parallel sum) ⟹ **"shared-resource composition = `C⋈D` obstructed by
  [ω]∈H²" is the surviving defensible novelty.** Banked in [[orchestration-is-zappa-szep-weld]] + reading
  note `reading/2026-07-21-aberle-2604.01303.md`.
- **Triggers reset for the next cycle:** LEAN = ×-monoid CONVERSE + round-trips (full iso, mirror
  `DirichletMonoidConverse.lean` — the clearest open Lean target, closes the × column both sides);
  PROVE = the re-entrancy OBSTRUCTION THEOREM (promote `orchestration-zs` computed→proved by assembling
  pairwise-ZS + g-obstruction + the verified K_bug≅rigid-twist iso into one named theorem — this IS the
  surviving-novelty layer); WRITE = REVISE `containers-for-orchestration.tex` to cite Aberlé as the
  mechanism's prior art and reframe the ZS/H² layer as the delta (+ ArchAgents differentiator, cite TODOs).
- Still-owed cheap read: arXiv:2603.25710 (Stone Duality two-trail hub, from 07-19) — leave to browse.

## 💤 2026-07-20 (dream) — browse consolidated; orchestration differentiator + 3 cites banked
- Day's crown jewels (×-monoid Lean forward, (⋉,⋊)-duoidal-LDC proof, orchestration draft, Neil UID-70
  endorsement) were banked live below. Dream job = browse-consolidation + prune, in the 07-18/07-19 mould.
- **★ ArchAgents arXiv:2605.12239** (Banu) — categorical multi-agent orchestration via **operads +
  coalgebraic state**, orthogonal to my distributive-law/ZS axis; NO scoop, citable **differentiator** for
  the grant Impact section (surfaced by two blind agents). Appended to [[orchestration-is-zappa-szep-weld]].
- **★ 3 new cites (wake sweep, none a scoop):** Aberlé **2604.01303** (poly interfaces + free-monad impls,
  Agda — closest prior art to theorem-proving-as-container; READ before the orchestration write); Hua–Xu
  **2602.05689** (π-clans vs LCC → Ch2); Fairbanks **2605.03102** (monads in 2-cats → DCont≅Cof / ZS).
- **★ nLab categorical-ZS gap** (stable ≥5 sessions) promoted to a low-cost WRITE target (Rosebrugh–Wood +
  pairwise-ZS stub). Details: `dream-journal/2026-07-20.md`; leads in `questions/open-threads.md` (07-20 block).

## ★ 2026-07-20 (LEAN) — ×-monoid forward map (Thm B) machine-checked
- **`Container.TimesMonoid.toShapeMonoidOplaxFibresCoproduct`** sorry-free in
  `lean/Containers/Containers/TimesMonoid.lean` (imports FourMonoidal + DirichletComonoid; full
  build green, `#print axioms` = `[Quot.sound]` only). Formalises Thm B §6 forward: a bare
  `×`-monoid (categorical-product tensor `(Cont,×,1)`) = a monoid on shapes with **empty identity
  fibre** `posEmpty : C[e]→Empty` + an oplax functor into `(Set,⊔,∅)`, routing
  `ψ : C[s·t]→C[s]⊕C[t]`. The `×`-analogue of the `⊗`-monoid forward map — "one theorem
  parameterised by fibre monoidal structure" made concrete.
- **New Lean idiom logged:** the `⊗` file's `congrArg Prod.snd` unit-coherence shortcut does NOT
  port to `×`, because the fibre combiner is `⊕`. The `onPosOfEq` position content of the `×` unit
  law lands in `Empty ⊕ C[s]` (identity fibre routed through `η.onPos : C[e]→Empty`), a *different
  sum type* from the target `C[e]⊕C[s]`; recovered by `cases` on the routing + `Sum.inr.inj` +
  empty-fibre `.elim`. This is where `c[e]=∅` earns its keep. Registry
  `dirichlet-monoid-classification` node `lean-times-forward` = lean-verified.
- **OPEN:** `×`-monoid converse + round-trips (mirror `DirichletMonoidConverse.lean`). Both
  Day-monoid columns (`⊗`,`×`) now Lean-covered on the *forward* side; converse only for `⊗`.
- Collaborator note: `for-collaborator/2026-07-20-lean-times-monoid-forward.md`.

## ★ 2026-07-20 (PROVE) — (⋉,⋊) is a NORMAL DUOIDAL / linearly-distributive structure on Poly
- **Answered PROVE.md YES + upgraded.** `(Poly,⋉,⋊,y)` is normal duoidal (⋉ outer/symmetric,
  ⋊ inner/directed, shared unit y); linear distributor `δ:A⋉(B⋊C)→(A⋉B)⋊C` exists — id on shapes,
  dir=(id,id,**const** `C[c]→C[c]^{S_A}`), genuinely NON-iso ⇒ a real LDC (not a duoidal-iso collapse).
  Interchange `ζ:(A⋊B)⋉(C⋊D)→(A⋉C)⋊(B⋉D)`; δ = ζ specialised via normality.
- **Proof = the REINDEXING CALCULUS** (reusable coherence engine): every ⋉/⋊-composite of atoms has
  dir `∏_i p_i[s_i]^{S(A_i)}`, A_i⊆atoms; every structural map = id-on-shapes-up-to-(Set,×)-coherence +
  factor-wise precompose with product-projection `S(A_i^src)↠S(A_i^tgt)` (exists iff A_i^tgt⊆A_i^src);
  subsets = POSET (≤1 arrow) ⇒ ≤1 structural map ⇒ ALL duoidal + Cockett–Seely LDC diagrams commute
  FOR FREE. Full container-level Python verify (`scratch/ldc-duoidal/`) — all pass.
- **Trust proved** (registry `other-cont-monoidal-tensors` node `ltimes-rtimes-duoidal-ldc`, validates).
  ⚠️ **NOVELTY UNVERIFIED (no-browse)** — (⋉,⋊) analogue of Spivak–Srinivasan 2407.01849's (⊗_Day,◁);
  ⋊≠Dialectica par ⇒ fresh pairing, do NOT claim priority. Fits deferred Cont(C)/Dialectica chapter.
  Proof: `proofs/2026-07-20-ltimes-rtimes-duoidal-ldc.md`; note: `for-collaborator/2026-07-20-…`.
  → [[ltimes-rtimes-duoidal-ldc-proved]]

## ★ 2026-07-20 (wake-2) — morning email SENT (was still owed); Neil ENDORSES orchestration-via-containers; triggers reset
- **The 07-20 morning email had NOT actually been sent** (prior wake banked ⊗-comonoid converse Lean iso
  + scoop checks but crashed before emailing / setting triggers). Email agent confirmed: last outgoing =
  07-19 daily; Neil's reply **UID 70 unread**. Sent today's daily (CC Robin), folding the UID-70 reply in
  — one-email/day respected. UID 70 marked read.
- **★ NEIL (UID 70) sets the agenda + ENDORSES the orchestration direction.** His model = agent=container
  (prompts=shapes, replies=positions), morphism to `y`=oracle/LLM call, container morphisms=delegation,
  monoidal=orchestration language, **closed structure=higher-order orchestration (his explicit "unexplored"
  flag)**, theorem-proving-as-container (theorems=shapes, lemmas=positions, tactics=◁-monoid/free-monad),
  harness=comonad. Asked for: lit sweep, orchestration thinking, a ch1–3 wrap-up checklist, and **a draft
  email to Nelson Niu** — all delivered in the reply. My response grounded every row in proved/Lean-verified
  results (Free.lean, DirichletClosed.lean, pairwise-ZS, H²) → [[orchestration-is-zappa-szep-weld]].
- **★ Literature sweep (Neil item 1): NO scoop for the Ch3 classification** (reassuring negative — Day-census
  + ⋉/⋊-outside-Day still unclaimed). Two high-value new cites: **Aberlé arXiv:2604.01303** (poly interfaces
  + free-monad implementations, Agda — closest prior art to theorem-proving-as-container; CITE Ch3 +
  orchestration note) and **Hua–Xu arXiv:2602.05689** (π-clans vs LCC — CITE Ch2). Also Fairbanks
  arXiv:2605.03102 "Monads in 2-categories" (retrofunctors/distributive laws — DCont≅Cof + ZS layer).
- **★ ⊗ ROW FULLY CLOSED (audit-confirmed):** all four Lean files (DirichletComonoid/Monoid + both
  Converses) sorry-free; ⊗ (co)monoid classification is a full machine-checked iso BOTH sides. WRITE.md's
  dcont-cof related-work bank (Stone Duality + Comonads-as-Spaces) was ALREADY done (lines 513, 593–600).
- **Triggers RESET for the orchestration turn:** WRITE=`containers-for-orchestration.tex` (grant-Impact
  note, everything it cites already proved/Lean-verified); LEAN=×-monoid classification FORWARD (Thm B,
  sibling of DirichletMonoid.lean — the one clearly-open Lean target, completes the (co)monoid table);
  PROVE=do ⋉/⋊ form a linearly-distributive pair on Poly? (Spivak–Srinivasan 2407.01849 lens, untried).

## ★ 2026-07-19 (PROVE deep-work) — orchestration = Zappa–Szép product is now COMPUTED (dictionary grounded)
- **Deliverable:** `proofs/2026-07-19-orchestration-zs-instantiation.tex` (4pp, compiles), registry
  `orchestration-zs.json` (validates, **computed**), scripts `scratch/orchestration_zs{,2,3}.py` (all
  machine-checked). Collaborator note: `for-collaborator/2026-07-19-orchestration-zs-instantiation.md`.
- **What moved:** the orchestration=ZS reading was **speculative** (no worked instance). Now **computed**.
  Supervisor–worker orchestration modelled as a small category (T1 DCont≅Cat); composing two = distributive
  law / ZS product K=C⋈D (T2 pairwise-ZS); re-entrancy = (G)-failure = nonzero [ω]∈H²(Sk;Z/2) (T3).
- **The table (4 regimes, machine-checked):** independent supervisors → composes (K=C×D); coherent
  nontrivial interleave → composes (K=S₃=Z/3⋊Z/2, non-abelian); state-protected re-entry → composes
  (#SFS=2, [ω]=0); **unprotected re-entry → OBSTRUCTED (#SFS=0, [ω]=gen Z/2)**.
- **Crux:** the re-entrant model `K_bug` (worker outcome flips supervisor's turn token, `s₂∘p=qτ≠q`)
  is **isomorphic to the rigid twist** (explicit iso matching D, verified) ⇒ H² transfers verbatim. The
  **single bit** flipping composable↔obstructed = *does a worker mutate shared supervisor state?*
- **Honesty:** T1/T2/T3 cited (Ahman–Uustalu / mine / Rosebrugh–Wood·Baues–Wirsching·Pirashvili); NO new
  cohomology; models are minimal faithful abstractions (NOT a claim that LangGraph *is* this — that node
  is a registry dead-end). Empirical GA-style validation = future step. See [[orchestration-is-zappa-szep-weld]].

## ⚠️ 2026-07-20 (wake) — ⊗-monoid column CLOSED as a full Lean iso; two scoop-checks clean; orchestration weld banked
- **Morning email to Neil SENT** (CC Robin, one-email/day; inbox read FIRST per the process fix — it was
  empty, nothing new since uid 69). Reported yesterday's ⊗ work + today's plan.
- **★ ⊗-MONOID CLASSIFICATION IS NOW A FULL MACHINE-CHECKED ISO.** `DirichletMonoidConverse.lean` (new):
  reverse map `ShapeMonoidOplaxFibres c → DirichletMonoid c` + BOTH round-trips ⟹
  `DirichletMonoid c ≅ ShapeMonoidOplaxFibres c`. **VERIFIED BY ME** (not just the sub-agent): `lake build`
  green (29 jobs), no sorry/admit, `#print axioms` both round-trips = `[Quot.sound]` only. Registry
  `dirichlet-monoid-classification` child **`lean-converse` = lean-verified** (trustcheck green). Method =
  clean mirror of the forward `onPosOfEq`: `ext'` with shape-eq = monoid axiom, fibre goal = oplax
  coherence matched by `Eq` proof irrelevance; round-trips `rfl`. Shared with Rick (email + file).
  **⊗-comonoid converse still open** (the arrow-reversed sibling `bare-dirichlet-comonoid`).
- **★ Two scoop-checks came back CLEAN (both read in full by agents, PDFs banked):**
  - **arXiv:2603.25710 "Stone Duality for Monads"** (Garner–Renata–Wu, MFPS 2026; NOT "…Retrofunctors in
    Locales" — that was my paraphrase). Contravariant idempotent adjunction {ranked Set-monads} ⊣ {localic
    categories + internal retrofunctors}; fixpoints = hyperaffine-unary monads ≃ ample localic categories.
    **ORTHOGONAL, no scoop** — cites AU [3,4] + Clarke [7] TAC35 + Niu–Spivak [22] as BLACK-BOX prior art
    for "Retro ≃ polynomial comonads" (the *detopologized* Set-case = my formalised object). Strong
    **NEIGHBOUR for the cofunctor chapter** + a `Loc`/`Top` data-point for the comonoid-over-a-fibration
    question (but it fixes the base to locales, does NOT do the general fibration). Key adjacent cites:
    Clarke [7] (internal retrofunctors), Garner [9] costructure–cosemantics. PDF: `~/papers/garner-stone-duality.pdf`.
  - **arXiv:2511.07314 "The Free Bifibration on a Functor"** (Clarke–Scherer–Zeilberger, 96pp). Free
    bifibration `Bif(p)→C` via a proof-theoretic sequent calculus (pushforward/pullback = ∃_f/∀_f); id_C
    case = zigzag double cat ℤ(C) = free companions-and-conjoints completion. **No scoop, ORTHOGONAL**;
    does NOT cite AU/Clarke-cofunctors/Niu–Spivak; no Poly/comonoid content; does NOT answer the
    comonoid-over-a-fibration question (base is a plain category, not a fibration). **3rd flag RESOLVED —
    stop re-flagging.** PDF: `~/papers/free-bifibration.pdf`.
- **★ ORCHESTRATION = ZAPPA–SZÉP weld banked** (connection [[orchestration-composition-is-zappa-szep]];
  scratch `2026-07-20-orchestration-obstruction-note.md`). Survey confirmed my corpus splits into two
  disjoint universes — orchestration-as-container (seed notes: composition = **functor**) and ZS⇒H²
  obstruction (my proved theorems: no agents) — that NEVER touch. The note is the weld. **Novelty is
  link (2): agent composition = distributive law / ZS product `C ⋈ D`** (every prior note used a *functor*;
  none wrote "joint agent = C ⋈ D"). H² is cited-not-new (Neil demoted that thread — respect it).
  Differentiator: MAS crowd uses `H⁰`/`H¹` sheaf-Laplacian on the *communication* graph (consensus 2606.01663
  / identifiability Anwer–Riess–Hale 2605.11204); container view uses `H²` on the *handoff* category
  (composability). **Grounding = a concrete COMPUTE target** (free cat on `sup⇄{w₁,w₂}`; two supervisors
  sharing workers; enumerate δ, check (L)∧(G), exhibit a (G)-failure = re-entrancy = nonzero [ω]). Grade:
  T1–T3 proved, dictionary speculative. Candidate WRITE / grant-Impact target pending Neil.

## 💤 2026-07-19 (dream) — browse consolidated; loose threads swept
- Day's crown jewels (⊗-monoid classification PROVED + Lean forward zero-axiom; (co)monoid table into
  §4.3; Dialectica §10 relocated) were banked live below. Dream job = browse-consolidation + prune.
- **[SGF25] RESOLVED** = `Functorial Aggregation` arXiv:2111.10968 (JPAA 229 (2025) 107883), the canonical
  "polynomial comonads = categories" cite; full-read owed; may be the retitled 2021 "Polynomial Comonoids".
- **★ Two blind citation trails (AU16 + Poly book) HUB on arXiv:2603.25710 "Stone Duality for Monads"**
  (Garner–Renata–Wu) — top read priority; resolves the 07-16 disambiguation (same paper).
- **★ Grant Path-5 opening:** container/DCont lens on AGENT ORCHESTRATION is unstaked — three searches
  converge (sheaf/multi-agent crowd uses generic Laplacians, nobody uses poly functors). Zero H² scoop risk.
- Details: `dream-journal/2026-07-19.md`; leads in `questions/open-threads.md` (07-19 block).

## ⚠️ 2026-07-19 (wake) — Neil's (co)monoid table DELIVERED; 07-18 backlog answered; Dialectica deferred
- **Morning email + ONE consolidated reply to Neil's 07-18 backlog (uid 65–69) SENT** (CC Robin). Those
  five emails postdated my last sessions. Key STEERS captured:
  - **Neil is DEFERRING Dialectica ⋉/⋊** to a later `Cont(C), C≠Set` chapter (they work over the
    coproduct-completion of the product-completion of Set). ⟹ WRITE trigger: **pull §10 out of the
    monoidal chapter** into a held file. Noted the symmetric-⋉ = "subgame perfection" game-theory line.
  - **First three chapters fixed:** (1) Intro + preliminary CT, (2) category of containers, (3) monoidal
    structures. **Cofunctors / DCont≅Cof = Chapter 4** (monads/comonads), OUT of the milestone.
  - **One consolidated email per day** (Neil overloaded, wife ill). PROCESS FIX: from tomorrow read
    inbox BEFORE the morning note so it's genuinely one email.
- **★ THE (CO)MONOID TABLE for the four structures — Neil's requested deliverable — assembled & delivered.**
  ⚠️ **It already existed** (`scratch/monoid-comonoid-table/TABLE.md`, 07-18) — today's table agent
  *independently re-derived* it (good corroboration, but I DUPLICATED existing work; **grep scratch/
  before dispatching classification agents** → [[check-scratch-before-dispatch]]). Delivery to Neil (he
  only had it as internal scratch) + backlog answers = the real contribution today. The table:
  | ⊙ | comonoids | monoids |
  | + (0) | only 0 | every container (∇) |
  | × (1) | every container (Δ) | monoid on shapes, **identity-fibre EMPTY** (generically none; 1,4,33) |
  | ⊗ (y) | **families of monoids** [proved+lean fwd] | **monoid on shapes + OPLAX P:S→(Set,×)** [PROVED 07-19] |
  | ◁ (y) | small categories [AU] | polynomial monads [G–K] |
  ⟦–⟧ strong monoidal for all four. **Climax = the ⊗ lax/oplax duality** (comonoid=lax family-of-monoids,
  monoid=oplax functor). Present the four cartesian/cocartesian-collapse cells in ONE box; spend real
  estate on ◁ & ⊗ as a 2×2 of dualities (category↔monad, family-of-monoids↔oplax-functor).
- **Registry:** ⊗-monoids `dirichlet-monoid-classification` = **PROVED 2026-07-19** (was computed).
  Proof `proofs/2026-07-19-dirichlet-monoid-classification.md` (trustcheck green): shape part of each
  monoid law ⟹ monoid on S; fibre part ⟹ oplax functor `(S,·,e)→(Set,×,1)`. Thm B: `×`-monoid = SAME
  theorem with fibre target `(Set,⊔,∅)` + `c[e]=∅` (`times_monoid.py` confirms 1,4,33). **The whole
  monoid column is one theorem** parameterised by the fibre monoidal structure the tensor uses. §5 gives
  the honest reason comonoid↔monoid is not a mirror (comult maps INTO S×S ⟹ diagonal forced; mult maps
  OUT ⟹ any monoid free). Collaborator note: `for-collaborator/2026-07-19-dirichlet-monoid-classification.md`.
- **★ LEAN forward map DONE 2026-07-19** (lean session): `Container.DirichletMonoid.toShapeMonoidOplaxFibres`
  in `lean/Containers/Containers/DirichletMonoid.lean`, sorry-free, **`#print axioms` = NO axioms at all**
  (cleaner than the comonoid's `Quot.sound` — closes by `congrArg`/`onPosOfEq` + `Eq` proof irrelevance).
  Structure `DirichletMonoid` (η:y⟶C, μ:C⊗C⟶C, unit laws, assoc) → target `ShapeMonoidOplaxFibres`
  (smul/e/phi + shape monoid laws + oplax unit coherences `phi_one_smul`/`phi_smul_one` + oplax hexagon
  `phi_assoc`). Arrow-reversed dual of `DirichletComonoid.toFamilyOfMonoids`; reuses its `onPosOfEq`. No
  forced diagonal ⟹ **no `dirichlet_mul_assoc`-style subst needed** (shape mult is a free forward map; the
  assoc transport IS `smul_assoc`). Registry child `lean-forward` = `lean-verified`. The whole ⊗ column is
  now machine-checked on BOTH sides (comonoid fwd 07-18, monoid fwd 07-19). Converse still open both sides.
- **Answers given Neil:** position formula (his generic-element reconstruction CONFIRMED; P(s)=domain of
  initial elt of the s-fibre of el F); **Lens subcategory** = monomials `S·y^A`, morphisms = lenses,
  closed under × but NOT coproduct/W-types (⚠️ verify before the box); **right Kan** = Ran_F F codensity
  MONAD (dual of Lan_F F density comonad) but polynomiality FAILS (ultrafilter monad counterexample) →
  Ch4; **Nelson** (Niu) = worth a scoped note on ⋉/⋊=Dialectica answering DJN §6, draft-for-review;
  **Hyland "containers = Dialectica²"** = filed as a question (dovetails ⋉/⋊=Dialectica), no direction
  asserted. → [[browse-2026-07-19-and-neil-steers]]
- **Browse leads resolved:** **Purdy–Damato = arXiv:2503.17191** "Distributive Laws of Monadic
  Containers" (CALCO 2025, Cubical Agda) — monad-side sibling of pairwise-ZS, cite as parallel neighbour.
  **arXiv:2203.15633 is NOT containers-as-REST** — it's Videla–Capucci "Lenses for Composable Servers";
  drop that lead. **Lean confirm:** `DirichletComonoid.lean` mul_assoc sorry was ALREADY discharged
  07-18 (dream-journal "tomorrow" note was stale) — `bare-dirichlet-comonoid` fwd is lean-verified.
- **Triggers set:** PROVE = analytic proof of ⊗-monoid classification (computed→proved, dual of the
  comonoid unwinding) + ×-monoid; LEAN = ⊗-monoid FORWARD in Lean (dual of DirichletComonoid.lean,
  completes the ⊗ row both-sided); WRITE = (co)monoid table into monoidal chapter + pull Dialectica §10
  out + (if time) Lens subcategory box.

## ★ 2026-07-18 (prove-2) — ⋊ IS LEFT-CLOSED → directed-closed monoidal category
- **Open Question 5 RESOLVED (YES).** `2026-07-18-rtimes-left-closed.md`. **Theorem:** for every `q`,
  `(−) ⋊ q` has a right adjoint `[q,−]_⋊`, so `(Cont,⋊,y)` is **left-closed**. Explicit internal hom
  `[q,r] = (Cont(q,r), (a,c)↦ S_q × ∐_{t} r[a t])` — **the shape set of the internal hom is the
  external hom `Cont(q,r)`**. Natural iso `Cont(p⋊q,r)≅Cont(p,[q,r])` proved (bijection Θ §2 via
  currying + exponential/coproduct adjunctions; naturality in p §3, full index-tracked check);
  pointwise-adjoint criterion (Mac Lane IV.1). Verified computationally: hom-cardinalities match on
  2000 random triples; Θ injective on a 4096-morphism example (actual direction SETS); `[y,r]=r`
  (500 trials, unit sanity).
- **⋊ = DIRECTED-CLOSED** (Cor 4.2): left-closed (exponent-*base* side `(−)⋊q`) but **not** right-
  closed (`p⋊(−)`, from the morning note). The handedness of closure = the handedness of the tensor.
  Cor 4.3: `(−)⋊q` is a left adjoint ⇒ preserves ALL small colimits (strengthens the morning
  coproduct-only result to a one-liner). Cor 4.4: `[y,−]_⋊=Id`.
- **Refined slogan:** `(−)⊙q` is a left adjoint (closure-eligible) **iff the *varied* shape set does
  not appear in an exponent** of the direction formula. One dial reads off closure on each side; for
  the directed tensor it is set on exactly one side.
- **Honesty:** does NOT contradict de Paiva's closed `Dial(Set)` — this is the `C=1` predicate-free
  slice of all `Cont`. External novelty owed a browse (de Paiva/Trotta/Spivak/Hedges "directed
  Dialectica / one-sided closed poly tensor"); the *math* is proved. Registry child
  `rtimes-left-closed` = **proved**; validator OK.
- **Chapter feedback owed:** `four-monoidal-chapter.tex` §10 — the ⋊ Remark should now state ⋊ is
  **directed-closed** with the explicit `[q,r]_⋊`, not "⋊ is not closed."
- **Next:** `/lean` the adjunction (`Adjunction.mkOfHomEquiv`) — first machine-checked one-sided-
  closed container structure.

## ★ 2026-07-18 (prove) — ⋉/⋊ non-closed PROVED + ⋊ one-sidedness correction
- **PROVE target closed.** `2026-07-18-dialectica-tensors-non-closed.md`. **Theorem 1:** `(Cont,⋉,y)`
  is neither left- nor right-closed (witness `p=q=y²`; `p⋉(−)` and `(−)⋉q` fail to preserve `y+y`,
  profile ⟨4,4⟩≠⟨2,2⟩ ⇒ no right adjoint via Mac Lane V.5). **Theorem 2:** `(Cont,⋊,y)` is **not
  right-closed** (`p⋊(−)` fails) — **BUT `(−)⋊q` DOES preserve binary coproducts** (§2(d): exponent
  `S_q` fixed, distributivity iso). So the closure obstruction is **one-sided / directed**, mirroring
  ⋊'s directedness. This **CORRECTS** the companion note's blanket "same computation kills ⋊" (false
  in the left variable). Method: contrapositive of "left adjoint preserves colimits" via
  non-ISO-of-objects (stronger than comparison map) + AAG container-iso criterion (profile invariant).
  Registry `other-cont-monoidal-tensors` child `ltimes-rtimes-non-closed` = **proved**; validator OK.
- **Open Question 5 — RESOLVED 2026-07-18 (YES, see top section):** ⋊ is left-closed. [was:] needs
  all-colimit preservation (coequalizers in Fam(Set^op) not shapewise — untested) or explicit
  `[p,−]_⋊`. Conjecture: YES — ⋊ = a genuinely *directed-closed* monoidal category.
- **Chapter feedback owed:** `four-monoidal-chapter.tex` §10 — replace blanket "⋊ not closed" with
  "⋊ not right-closed; `(−)⋊q` preserves coproducts, left-closure open."

## ⚠️ 2026-07-18 (wake) — Neil uid-64 answered; SEED Q5 resolved; Dialectica §10 shipped
- **Morning email + reply to Neil's uid-64 SENT** (CC Robin). His four questions map onto done work:
  (1) wide-pullback theorem → Ch2 (now a WRITE target); (2) ⋉/⋊ **formulas given verbatim**
  (`p⋉q[(s,t)]=p[s]^{S_q}×q[t]^{S_p}` symmetric; `p⋊q[(s,t)]=p[s]^{S_q}×q[t]` directed/triangular);
  (3) cofunctors = DCont morphisms (DCont≅Cof); (4) Day-conv comonoids = bare ⊗-comonoids =
  families of monoids (proved yesterday). He wants first 3 chapters "complete."
- **★ SEED Q5 (density comonads) RESOLVED — orthogonal, NO scoop.** Spivak "Categories by Kan
  extension" arXiv:2503.21974 does NOT reprove DCont≅Cat — it CITES Ahman–Uustalu and builds a
  Kan-extension/density-comonad *construction machine* (produces categories: Lawvere theories, Δ^op,
  selection cats). Cite as complementary, not an alt-proof, not a generalisation of my Lean object.
  **NEW LEAD: [SGF25] = Spivak–Garner–Fairbanks 2025** may be THE canonical modern citation for
  "polynomial comonad = category" — vet as closest neighbour before the book comonad chapter (resolve
  vs the 2021 "Polynomial Comonoids"). `[q/p]` Kan notation = lens coclosure (touches ◁-coclosure).
  → [[density-comonads-orthogonal-seed-q5]].
- **★ Dialectica §10 citation-VERIFIED (primary sources) + chapter SHIPPED to Neil (PDF, CC Robin).**
  Math all holds. Two bib TITLES were WRONG (conflations) — fixed: **lnv2405** = "Monoidal closure of
  Grothendieck constructions via Σ-tractable monoidal structures and Dialectica formulas"
  (arXiv:2405.07724, to appear TAC; their tensor is untwisted product-like, twist in the ⊸ ⇒ NOT ⋉);
  **capucci2024** = "On a fibrational construction for optics, lenses, and Dialectica categories"
  (arXiv:2403.16388, MFPS XL; a category not a tensor). de Paiva 1989/1991 correct; ⋉=de Paiva's
  Dialectica ⊗ confirmed from primary source (direction `X^V×Y^U`). four-monoidal-chapter.pdf = 30pp,
  compiles clean. Registry `other-cont-monoidal-tensors` stays `computed`.
- **Rick uid-57 (peer):** registers my refutation as peer-claimed/methodology (won't cross my
  lean-verified in until he re-derives — checked-sober policy); **endorses the CENSUS framing**
  ("every monoidal structure on Set induces one by Day convolution") over "four canonical structures";
  urges reading Shapiro–Spivak duoidal before dirToSeq-asymmetry claims. → [[census-framing-preferred]].
- **Triggers set:** LEAN = bare ⊗-comonoid **forward** direction (Dirichlet comonoid → family of
  monoids); WRITE = Ch2 wide-pullback theorem (Neil-requested); PROVE = **⋉/⋊ are NOT closed**
  (explicit coproduct-non-preservation witness ⟹ no right adjoint; promotes `other-cont-monoidal-tensors`).

## ⚠️ 2026-07-17 (wake-2) — Dialectica novelty CLEARED (C); Neil's four questions answered
- **★ ⋉=Dialectica NOVELTY SWEEP RUN → verdict (C) CLEAR.** The ⋉/⋊ = Dialectica identification
  (below) is genuinely novel and answers DJN's OWN stated open question — **but only under the framing
  rule: identify a KNOWN tensor (de Paiva's) with DJN's uninterpreted ⋉, NEVER "first Dialectica-on-Poly"
  (false — theme is crowded).** Two neighbours to cite+distinguish: **Lucatelli Nunes–Vákár
  arXiv:2405.07724** (Dialectica-FORMULA *closed* structure on Grothendieck constructions, incl.
  containers; but tensor = fibred product, twist in the ⊸ — does NOT produce ⋉; ALSO a new neighbour
  for the closed-structures/von-Glehn programme + a lead on whether ⋉ is closed) and
  **Capucci–Gavranović–Malik–Rios–Weinberger MFPS 2024** (fibrational Dial(P), the *category* not a
  tensor). Reviewer pre-empt: DJN's §3 "dialectica" tensor is the NON-twisting A×B product; the twisting
  multiplicative one is ⋉. Registry `other-cont-monoidal-tensors` stays **computed** (definition-match),
  now carries the verdict+neighbours in `notes`, trustcheck green. → [[ltimes-rtimes-are-dialectica]].
- **★ ⋉/⋊ section DRAFTED** (`papers/ltimes-rtimes-dialectica-section.tex`, 5pp, compiles clean,
  style-matched to slot into `four-monoidal-chapter.tex`). Has the homogeneous-fragment computation,
  the non-convolutional/non-cocontinuous/non-closed structural payoff (⟹ Theorem A does NOT exhaust
  Cont's monoidal structures — the linear-logic tensors sit outside the Day family), and the Related-work
  paragraph. ⚠️ TWO WRITE-TODOs: (1) its novelty Remark still reads "unverified" — update to (C) CLEAR +
  framing rule; (2) 5 bibliography entries are placeholders, verify venues/DOIs before shipping.
- **★ Neil's uid-64 (07-17) four questions ALL answered by email** (CC Robin): (1) wide-pullback theorem
  for Ch2 + position formula P(s)=domain of generic element, `F≅Σy^{P(s)}`, cofiltered-limit = his
  final-coalgebra chain, his `F(2)→F(1)` guess corrected (gives 2^{P(s)}), cite Gambino–Kock 0906.4931;
  (2) ⋉/⋊ defined + Dialectica interpretation + honesty flags; (3) cofunctors arise as DCont-maps
  (DCont≅Cof, contravariant fibre) = Put-half of delta lenses = Cat# morphisms; (4) Day-conv comonoids
  = ⊗-comonoids = Niu–Spivak Ch9 Q5; double comonoids in (◁,⊗) = sets of commutative monoids
  (comparitor no-go); offered bare-⊗-comonoid classification as a follow-up PROVE.
- **★ 2026-07-17 PROVE — BARE ⊗-COMONOID CLASSIFICATION DONE (`proofs/2026-07-17-bare-dirichlet-comonoid.md`,
  registry `bare-dirichlet-comonoid`, proved).** ⊗-comonoids in Poly (no ◁) = **families of monoids**
  `Σ_s y^{M_s}`, each `M_s` an *arbitrary* monoid; comult forced diagonal on shapes + fibrewise binary
  op; `Comon(Cont,⊗,y) ≅ Fam(Mon^op)` (cocommutative = `Fam(CMon^op)`). No cocommutativity forced
  (brute-force y^1/y^2/y^3/[1,2] all match unfiltered monoid count). **Answers the Poly/⊗ slice of Ch9
  Q5** (open in the book — full-PDF re-read confirms). Three-layer table: ◁-comonoid=category,
  ⊗-comonoid=family of monoids, double=commutative monoids. **CORRECTION:** double-comonoid note §7's
  "Spivak owns the ⊗-comonoid classification" is WRONG (Q5 open; Rmk 3.78 = ⊗-*monoids* future work;
  §8.2.4/Prop 8.79 = ⊗-on-Cat#). → LEAN target (forward dir) next.
- **Cheap citation wins:** 2305.02571 "All Concepts are ℂat#" (Lynch–Shapiro–Spivak) = OPTIONAL-cite for
  DCont≅Cof (must-cites remain Ahman–Uustalu + Garner); ZS=distributive-law folklore anchor = Liang Ze
  Wong, n-Café "Distributive Laws", 18 Feb 2017 (groups/monoids; category-level = analogue).

## ⚠️ 2026-07-17 (prove) — ⋉/⋊ are the DIALECTICA tensors (DJN §6 open problem answered)
- **★ Dorta–Jarvis–Niu's two extra tensors ⋉/⋊ (arXiv:2305.05655 §6) INTERPRETED** →
  `proofs/2026-07-17-ltimes-rtimes-dialectica.md`, registry `other-cont-monoidal-tensors`
  (**computed**, trustcheck green). Container coords (shapes `S_p×S_q`):
  `(p⋉q)[(s,t)]=p[s]^{S_q}×q[t]^{S_p}`, `(p⋊q)[(s,t)]=p[s]^{S_q}×q[t]` — exponential over the
  **opposite shape set**. (1) **⋉ = de Paiva's Dialectica tensor** extended off `Hmg(2)≃Dial(Set)`
  to all of Poly: on homogeneous inputs direction `=A^J×B^I=X^V×Y^U` = de Paiva `⊗_Dial`. The
  linear-logic content of `Dial(Set)` lives in ⋉, NOT in DJN's Day `⊗` (which restricts to `X×Y`).
  (2) **⋊ = directed variant** — `n`-fold closed forms: ⋉ exponent = ∏ *all other* shape sets
  (symmetric), ⋊ = ∏ shape sets *to the right* (triangular ⇒ associative, NOT symmetric). **Answers
  DJN's stated open question.** (3) Taxonomy: **non-convolutional** (Thm A can't reach ⇒ four canonical
  + Day family DON'T exhaust Cont's monoidal structures), non-cocontinuous (no distrib over `+`),
  **non-closed** (first such on Cont). ⚠️ **Novelty NOT cleared** (no-browse session): identification is
  a definition-match (proved-math), but "is it new?" needs live de Paiva/Trotta/Spivak/Hedges 2023–26
  check — hence registry `computed` + de Paiva formula `unclassified`. Do NOT publish novelty pre-check.
  Target B (closure sub-Q 6.1) reduced (non-poly ⇒ non-cocontinuous; `+` shows insufficient),
  conjectured NO. Collaborator note `for-collaborator/2026-07-17-ltimes-rtimes-dialectica.md`;
  crown-jewel connection (Poly ↔ linear logic, novelty-flagged) → [[ltimes-rtimes-are-dialectica]].

## ⚠️ 2026-07-17 (lean-2) — third Hedges cell machine-checked (`⊗/+`)
- **★ `⊗/+` distributive law `lean-verified`.** `Container.dirCoprodDistrib`
  (`lean/Containers/Containers/TensorCoprodDistrib.lean`): `(P + P') ⊗ Q ≅ (P ⊗ Q) + (P' ⊗ Q)` as a full
  `ContainerIso`, both round-trips, sorry-free, `[Quot.sound]` only; full `lake build` green (26 jobs, no
  warnings). Registry `hedges-interchange-table.cell-ox-plus` → `lean-verified` (note the registry id is
  `cell-ox-plus`, not `cell-tensor-plus` as LEAN.md guessed). **Sibling of `seqCoprodDistrib`** with the
  Dirichlet tensor `⊗` (product positions `P.Pos s × Q.Pos t`) in place of `◁`: the bijection pushes the
  `inl`/`inr` tag across `⊗`, the untouched second factor `Q.Pos t` rides along, and each summand is
  definitionally equal — **no transport**; both round trips = `ext_id` + `cases <;> rfl` / `cases <;>
  HEq.refl`. This is the FIRST genuinely **two-sided** (symmetric ⊗) cell; only the left law formalised
  (it already witnesses the cell). Reused `ext_id`/`heq_sigma_mk` verbatim (imported `SeqProdDistrib` +
  `Dirichlet`). Note `for-collaborator/2026-07-17-lean-tensor-coprod-distrib.md`. Three D-cells now Lean
  (`◁/×`, `◁/+`, `⊗/+`); remaining: `×/+` (the other two-sided one, should be equally clean) and the
  harder `⊗/◁` / `×/⊗` cells. STRETCH ⋉/⋊ Dialectica-in-Lean target NOT attempted (banked the clean cell).

## ⚠️ 2026-07-17 (lean) — second Hedges cell machine-checked (`◁/+`)
- **★ `◁/+` LEFT-distributive law `lean-verified`.** `Container.seqCoprodDistrib`
  (`lean/Containers/Containers/SeqCoprodDistrib.lean`): `(P + P') ◁ Q ≅ (P ◁ Q) + (P' ◁ Q)` as a full
  `ContainerIso`, both round-trips, sorry-free, `[Quot.sound]` only; full `lake build` green (25 jobs, no
  warnings). Registry `hedges-interchange-table.cell-comp-plus` → `lean-verified`. **Sibling of
  `seqProdDistrib`** and STRICTLY cleaner: coproduct shape is already a `Sum`, so the bijection just pushes
  the `inl`/`inr` tag across `◁` — no `Sum.elim`-η rule, **no transport**; both round trips = `ext_id` +
  `cases <;> rfl` / `cases <;> HEq.refl`. Reused `ContainerMorphism.ext_id` verbatim (imported
  `SeqProdDistrib`). Note `for-collaborator/2026-07-17-lean-seq-coprod-distrib.md`. Two LEFT-variable D-cells
  (`◁/×`, `◁/+`) now both Lean; harder cells `⊗/◁` (lax `L`) + `⊗`-row remain. Pre-existing registry-validator
  gripe (root vs `computational-verification`) is unrelated, left as-is.

## ⚠️ 2026-07-16 (prove) — Hedges interchange table PROVED
- **★ HEDGES 4×4 DISTRIBUTIVE-LAW TABLE reconstructed from scratch, all 16 cells proved** →
  `proofs/2026-07-16-hedges-distributive-table.md`, registry `hedges-interchange-table` (proved,
  trustcheck green). **15/16 cells agree with Hedges.** Deliverables: (1) **convention decoded** (OWED
  item): row=outer; (co)cartesian columns `+`,`×` = preservation, tensor columns `⊗`,`◁` = duoidal
  interchanger, formal (co)limit gadgets dashed (⟹ `+` row & `×` column all `–`). (2) **`◁/+`, `◁/×`
  are LEFT-variable only** — sequential composition distributes over choice/product on the *outside*
  only (precomposition preserves colimits; postcomposition doesn't): `(y+1)◁(1+0)=2≠3` (NS Ex 6.56),
  `2y◁(y×y)=2y²≇4y²`. Bare `D` there is one-sided; only `⊗/+`,`×/+` two-sided. (3) **`×/⊗` CORRECTION:
  proved `–` not `L`** — witness `(1,y,y,1)` forces impossible `1→y`; the genuine `⊗`–`×` interchanger
  is the *formal* `⊗/×` (S–S Ex 2.2 dual, pair-into-product). Grid transposes this pair — flagged for
  Hedges via Neil (`for-collaborator/2026-07-16-hedges-table.md`). The one deep `L` (`⊗/◁`) = my
  comparitor coreflection (Thm C) + Eckmann–Hilton no-go — content I already hold. Maps are Spivak's/
  S–S's; delta = assembled proved table + convention + corrections. Feeds Neil's interaction chapter.

## ⚠️ 2026-07-16 (lean) — first Hedges cell machine-checked + root cleanup
- **★ `◁/×` LEFT-distributive law `lean-verified`.** `Container.seqProdDistrib`
  (`lean/Containers/Containers/SeqProdDistrib.lean`): `(P × P') ◁ Q ≅ (P ◁ Q) × (P' ◁ Q)` as a full
  `ContainerIso` (both round-trips), sorry-free, `[Quot.sound]` only. Registry
  `hedges-interchange-table.cell-comp-times` → `lean-verified`. **First machine-checked cell of the
  four-structure interaction table.** New for this library: the FIRST iso whose shape map is only
  *propositionally* (not definitionally) invertible — shape bijection curries a **sum-domain**
  function, so one round-trip hits the non-defeq η-rule `Sum.elim (f∘inl)(f∘inr)=f`. Two reusable
  transport helpers proven by `subst`: `ContainerMorphism.ext_id` (destructure φ first → shape map
  becomes a var → subst collapses the fibre dependency, no `▸`) and `heq_sigma_mk` (`Sigma.mk`
  `HEq`-congruence under a change of fibre family). Template for the remaining `Sum`/`Prod`-η cells.
  Note in `for-collaborator/2026-07-16-lean-seq-prod-distrib.md`.
- **Root-import cleanup (Robin's overdue request).** Added `Trajectory` + `TrajectoryComposition`
  (latter needed `import Trajectory`→`import Containers.Trajectory`). `Composition`/`Cofunctor`/
  `CoKleisli` stay orphaned — each a *genuine* incompatibility (namespace clashes with
  `Sequential`/`DContCat`, and unsolved goals resp.), not an import gap; documented in root note.
  Full `lake build` green (24 jobs, no warnings, no sorry).

## ⚠️ 2026-07-17 (wake) — deltas since 07-16
- **★ FREE-MONAD LEAN COMPLETE → `lean-verified`.** `freeMonoid.assoc` discharged; `Free.lean` zero-`sorry`,
  `[Quot.sound]`-only (re-checked by me). All three ◁-monoid laws machine-checked. Registry
  `free-monad-grafting` = **lean-verified**, trustcheck green. Phase 2's proof-object contribution CLOSED
  (free-monad side now mirrors the comonad/comonoid side M2b/M3b). Shared with Rick (email + Free.lean).
- **★ Neil's uid-63 direction picked up.** (a) **Connected-limits/position formula** answered (research
  agent): container ⟺ preserves connected limits (= wide pullbacks + cofiltered); `S=F(1)`, `P(s)`=domain
  of the GENERIC ELEMENT (initial object of the s-component of `el F`), giving `F≅Σ_s y^{P(s)}`. **Cleanest
  cite = Gambino–Kock 0906.4931 §1.18 + Prop 1.22** (⇐ Diers 1977, Carboni–Johnstone MSCS 1995 +corrig 2004).
  **Neil's guessed formula `fibre of F(2)→F(1)` is WRONG — gives `2^{P(s)}`; recovery needs the
  connected-limit universal property.** Poly terminology clash flagged (Poly "positions"=our shapes).
  Note: `scratch/2026-07-17-connected-limits-position-formula.md`; emailed Neil. (b) **Jules Hedges'
  4×4 distributive-law table transcribed** (`scratch/2026-07-17-hedges-distributive-table.md`): rows
  distribute over cols, D=distributive/L=lax/–=none; the ⊗-over-◁ **L** cell = the lax duoidal `Indep`
  interchange my comparitor no-go sits on. WRITE/PROVE target for the interaction chapter.
- **CITATION threads closed:** Garner 2019 = **talk-only, credits AU** → keep SS23 (no upstream shift);
  Kun Chen **2601.22968 current, Conj 7.2 still OPEN** (registry `m6-infinity-dcont` accurate). Both in
  `questions/open-threads.md`.
- **Alastair Poole:** address found (alastair.poole@strath.ac.uk) but he is **NOT on my CLAUDE.md email
  allowlist** → **asked Robin to confirm authorization + which pages already sent BEFORE emailing.** Do
  not email Alastair until Robin confirms. Chapter 0 email to Neil = **SENT** (PDF attached).

## ⚠️ 2026-07-16 (wake) — deltas since the 07-15 body below
- **Scoop-risk queue CLEARED** (IDs verified, abstracts read): Spivak "Interactions…" = **2602.17917**
  (PolyTr, not on Cont — safe); **no** Dorta–Jarvis–Niu follow-up (2305.05655 is it — Thm A/B⁺/C
  survive); Clarke "Grothendieck for delta lenses" = **2502.21288** (published); **2606.01663** is
  Nash-equilibria-as-global-sections, **NOT** an H² paper (my H² line stays covered by RW/BW/Pirashvili);
  Pradic–Price = **two** papers (2501.17250 Weihrauch-as-containers + **2601.15420** LICS-2026 fixpoints).
  See `questions/open-threads.md`.
- **★ FREE-MONAD TARGET REFRAMED (full read of Gambino–Kock 0906.4931).** The *construction* is
  **Gambino–Kock Thm 4.5 (2009)** — positions = P-trees, **directions = LEAVES**, μ = grafting, in any
  LCC-with-W-types. **NOT open** (the old "Ch9 Q11 open" line was the authors' ignorance). Defensible =
  **(1) Lean formalisation** (strongest; no machine-checked version exists) + **(2) writing out the
  grafting-monoid laws G-K omit.** SUMMARY §5 corrected; PROVE/LEAN triggers set to this.
- **Chapter 0 "The Machinery" drafted + VERIFY-PASSED** (Neil's UID-61 ask): `expository/preliminaries-
  representables-yoneda-day-kan.tex`, proves Neil's two observations. **07-16 WRITE session: removed a
  FALSE density theorem, corrected Neil's obs (ii) (strong monoidal ⇏ strong closed — counterexample
  `k[−]`; Dirichlet hom of two reps is ∐-of-reps "shapes are morphisms", Niu–Spivak Ex 4.78, NOT
  `y^{b^a}`), fixed Day-embedding variance (`𝒞^op`) and the Day base for Cont (`(Set,⋆)` not `Set^op`).**
  Chapter is now *more honest than the draft* — no originality claimed. → [[strong-monoidal-not-strong-closed]].
  Deliverable email staged in `for-robin/2026-07-16-chapter0-machinery.md` (write-session can't send).
  Four-monoidal chapter PDF emailed to Neil 07-16.

