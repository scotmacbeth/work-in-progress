# Fibred-monad citations (Jacobs / Hermida) + skeptical match check — 2026-08-07

Task from Neil: cite Jacobs/Hermida for "fibred monad" instead of reinventing, and
**skeptically** check whether the standard defs actually match MacBeth's T_M / G_M / λ.
Primary PDFs pulled and grepped locally (Jacobs book from GitHub Mzk-Levi/texts; Hermida
thesis from era.ed.ac.uk). All numbers below are quoted from the actual text.

---

## 1. The canonical definitions (exact numbers)

### Bart Jacobs, *Categorical Logic and Type Theory*, Studies in Logic 141, North-Holland/Elsevier 1999 (ISBN 0-444-50170-3)

- **Cartesian morphism & fibration — Definition 1.1.3** (§1.1).
  "A morphism f:X→Y in E is Cartesian over u:I→J if pf=u and [terminal-lifting UP]."
  Fibration = every u:I→pY has a Cartesian lifting.
- **Cloven / split fibration — Definition 1.4.3** (§1.4). (i) cloven = chosen cleavage;
  (ii) split = induced substitution functors strictly functorial (id⇒id\* and u\*v\*⇒(vu)\* are identities).
- **Fibred functor — §1.7** ("Fibred functors and fibred natural transformations").
  A fibred functor = functor over B that **preserves Cartesianness** (preserves Cartesian morphisms).
  Explicit synonym note, p.62: *"Often the name 'Cartesian functor' is used for what is called a
  'fibred functor' here."* A **fibred (vertical) natural transformation** = one whose components are vertical.
- **FIBRED MONAD — Exercise 1.7.9** (§1.7), verbatim:
  > "Let p be a fibration. A **fibred monad on p is a monad on p in the 2-category Fib(B)**.
  > It is thus given by a **fibred functor** T:E→E together with **vertical** unit η:id⇒T and
  > **vertical** multiplication μ:T²⇒T, satisfying [monad laws]."
  Note appended: Kleisli / Eilenberg–Moore of a fibred monad are the Kleisli/EM **objects in Fib(B)**;
  cross-refs Street [314] (formal theory of monads) and Hermida [129].
  ⇒ **Jacobs' "fibred monad" is (a) VERTICAL (a monad on p, i.e. over id_B) and (b) requires T to
  preserve Cartesian morphisms.** This is the strict/vertical notion.
- **Beck–Chevalley — Definition 1.9.4** (§1.9 "Fibred products and coproducts"; simple version 1.9.1):
  p has products/coproducts iff each substitution u\* has a right adjoint ∏_u (resp. left ∐_u) AND
  **for every pullback square in the base B the canonical mate  u\*∏_v ⇒ ∏_w u\*  (resp. ∐ u\* ⇒ u\* ∐)
  is an ISOMORPHISM.** I.e. BC = quantification (Σ/Π adjoint to reindexing) commutes with substitution.
- Aside: **Exercise 2.6.x / 11659**: "split monads on the simple fibration ↔ strong monads on B" —
  a different fibrational-monad notion (simple fibration), not our setting.

### Claudio Hermida, *Fibrations, Logical Predicates and Indeterminates*, PhD thesis, Univ. Edinburgh 1993 (also DAIMI PB-462; ECS-LFCS-93-277)

Hermida is the **better-matched primary source for T_M**, because he works in the 2-category **Fib**
(fibred functors over *arbitrary* base functors), not only Fib(B). Chapter 5 "Comonads and Kleisli fibrations":
- **Definition 1.2.10** (fibred 1-cell / fibred functor): (K̄,K):p→q with K̄ **preserving Cartesian
  morphisms** ("if f is p-cartesian, K̄f is q-cartesian"). 2-category **Fib** (fibrations, fibred
  1-cells, fibred 2-cells) vs **Fib(B)** (fixed base).
- **Definition 5.3.1**: comonad in a 2-category K.
- **Definition 5.4.1 (FIBRED COMONAD)** — instantiate 5.3.1 in Fib. Verbatim gloss:
  > "a fibred comonad consists of a **pair of comonads**: the total one (G:E→E,ε,δ) and the **base
  > one** (Ĝ:B→B,ε,δ) such that the fibration p **is a morphism of (co)monads** (commutes with counits
  > and comultiplications) **and G is fibred over Ĝ**."  Written ((G,Ĝ):p→p,…).
  Dualise to get **fibred monad** = pair (total T on E, base M on B), p a morphism of monads, T a
  **fibred functor over M** (preserves Cartesian). This is EXACTLY MacBeth's T_M-covers-M shape —
  **and it demands T fibred over M (Cartesian-preserving).**
- **Vertical fibred (co)monad** (p.135, immediately after 5.4.1):
  > "A comonad in Fib(B) is a **vertical fibred comonad**, i.e. one where the **base comonad is the
  > identity**. It is therefore a B-fibred comonad."  = Jacobs' Ex 1.7.9 notion (dualised).
- **§5.4.1 / Prop 5.4.x**: Kleisli fibration for a *vertical* fibred comonad.
- **§5.4.2 / Theorem 5.4.11**: Kleisli fibration for a **comonad in Fib** — the fibred comonad
  "factors through a resolution for its **base comonad**". This is the genuine covering-a-base-comonad case.

### Cross-checks
- **Ross Street, "The formal theory of monads", JPAA 2 (1972) 149–168** — monads in a 2-category,
  monad functors/monad morphisms, Kleisli/EM objects. This is the citation for "p is a morphism of
  monads" / a monad covering a base monad *without* any fibredness. (Jacobs Ex 1.7.9 cites it as [314].)
- **Hermida & Jacobs, "Structural Induction and Coinduction in a Fibrational Setting", Inf. Comput.
  145(2) (1998) 107–152**, DOI 10.1006/inco.1998.2725 — uses Beck–Chevalley for lifting/comprehension;
  the standard cite for BC-in-a-fibration in the induction context.
- **Katsumata**, ⊤⊤-lifting / "Relating computational effects by ⊤⊤-lifting" (Inf. Comput. 2013) and
  CSL 2005 — *lifting a monad to the total category of a fibration* for logical predicates. This is the
  literature where "a monad on E covering M on B, not necessarily Cartesian" is called a **lifting of M**.

---

## 2. Skeptical match check — THREE VERDICTS

### Claim 1 — "T_M(S,P)=(MS,P⋆) is a fibred monad covering M."  →  **CAVEAT (cartesianness required)**
- T_M is a monad on Cont with p∘T_M = M∘p and p carrying η,μ to η^M,μ^M ⇒ **p is a morphism of monads
  / T_M is a lifting of M along p** (Street 1972; Katsumata-style lifting). That part is unconditional. ✓
- But **"fibred monad" in BOTH primary sources requires the total functor to be a FIBRED FUNCTOR
  (preserve Cartesian morphisms)**: Jacobs Ex 1.7.9 ("a fibred functor T"), Hermida Def 5.4.1 ("G
  fibred over Ĝ"). MacBeth's own crown result is **T_M preserves Cartesian ⟺ M is Cartesian**
  ([[crown-tfae-strict-chain]], [[lean-tm-cartesian-boundary-done]]). Therefore:
  **T_M is a fibred monad (Hermida Def 5.4.1, over base monad M) IFF M is a Cartesian monad.** For
  non-Cartesian M (e.g. Pf, List with merge) T_M is only a *lifting / monad-morphism*, NOT a fibred monad.
- Extra subtlety: **Jacobs Ex 1.7.9 is even stricter — it is VERTICAL (monad in Fib(B), base = id_B).**
  T_M is over M ≠ id, so Jacobs 1.7.9 does not apply to T_M at all; the right home is Hermida's Def 5.4.1
  (2-category **Fib**, nontrivial base). **Cite Hermida 5.4.1 for T_M, not Jacobs 1.7.9.**
- ⇒ **PHRASING FIX (flag for Neil):** do NOT write "T_M is a fibred monad." Write
  *"T_M is a lifting of the base monad M along p (p is a morphism of monads, Street 1972); it is a
  fibred monad in the sense of Hermida (Def. 5.4.1) — i.e. T_M is fibred over M — precisely when M is a
  Cartesian monad."* The Cartesian hypothesis is not decorative; it is exactly what "fibred" adds.

### Claim 2 — "G_M(S,P)=(S,M∘P) is a vertical fibred comonad."  →  **MATCH**
- G_M is identity on the base ⇒ **vertical** (base comonad = id) ⇒ candidate for a *comonad in Fib(B)*
  = Jacobs Ex 1.7.9 dualised = Hermida's **"vertical fibred comonad"** (p.135) — exactly the named notion.
- Comonad structure (counit from M's unit, comult from M's mult, via the fibrewise op on (Set^op)^S)
  is MacBeth's transfer theorem ([[monad-comonad-transfer-computed]]).
- Fibredness: a Cartesian morphism has a **bijection** on positions; G_M post-composes M, and M (a
  functor) sends bijections to bijections ⇒ **G_M preserves Cartesian morphisms for EVERY M**
  (consistent with the note "G_M-cartesian-∀M survives", [[neil-steer-2026-08-05-fibrational-orestis]]).
- ⇒ **G_M is a vertical fibred comonad (Hermida Def 5.4.1 vertical case / Jacobs Ex 1.7.9 dual),
  unconditionally in M.** Correct term, exact fit. This is the clean, quotable side.

### Claim 3 — "λ: T_M G_M ⇒ G_M T_M is a Beck–Chevalley square / mate."  →  **CAVEAT (wrong concept + not iso)**
- Beck–Chevalley (Jacobs **Def 1.9.4**) is a statement about **adjoints to reindexing** (Σ_u ⊣ u\* ⊣ Π_u):
  for every *pullback in the base*, the canonical **mate between substitution and quantification is an
  ISO**. It is not about a swap TG⇒GT of a monad past a comonad.
- λ:T_M G_M⇒G_M T_M is a **mixed distributive law / entwining** (Beck, "Distributive laws", LNM 80,
  1969), the object MacBeth already studies as `str` ([[two-feeds-entwine-one-direction]]). Calling it
  "Beck–Chevalley" conflates two different constructions.
- Worse for the word "square/mate": BC *demands the mate be invertible*. MacBeth's own finding is
  **TG⇒GT always holds but GT⇒TG FAILS on branching M** ([[two-feeds-entwine-one-direction]],
  [[effect-coeffect-arrows-first-strength]]). So λ is not an iso in general ⇒ it cannot be a
  Beck–Chevalley iso except in the non-branching case, and even then it is a distributive-law mate,
  not a Σ/Π-vs-reindexing mate.
- ⇒ **PHRASING FIX:** call λ a **mixed distributive law (entwining)** of the fibred monad T_M over the
  vertical fibred comonad G_M (Beck 1969; Street 1972 for the 2-categorical mate). Reserve
  "Beck–Chevalley" for a genuine Σ/Π-reindexing square, or state explicitly the restricted claim
  "λ is invertible ⟺ M is non-branching" as a BC-*style* coherence and prove the mate identity — do
  not assert BC as if it were the standard Def 1.9.4.

---

## 3. Nearest neighbour already known: arXiv:2408.16581 "Fibrations of algebras" (Ahman, Coraglia, Castelnovo, Loregian, Martins-Ferreira, Reimaa 2024)

Already cleared ([[fibrations-of-algebras-2408-cleared-neighbour]]). Their "fibred monad" is a
**parametrized monad** T:𝒜→Mnd(𝒳) (a family on a *fixed* carrier 𝒳), total category monadic over 𝒜×𝒳.
Wrong shape of "lying over": theirs is a family on a fixed fibre; MacBeth's T_M is a monad on the total
category covering a base monad (Hermida-Def-5.4.1 shape). **Does not help** pin the fibred-monad def and
does not supply the Cartesian-preservation subtlety. Cite as neighbour only.

---

## Bottom line for the write-up
1. **Cite Hermida 1993 Def 5.4.1** (2-cat **Fib**, base (co)monad + fibred-over-base) as the notion of
   fibred (co)monad covering a base; **cite Jacobs 1999 Ex 1.7.9** for the VERTICAL case (= vertical
   fibred (co)monad), plus Def 1.1.3 (Cartesian), 1.4.3 (split), 1.9.4 (Beck–Chevalley). Street 1972 for
   "morphism of monads / lifting". Hermida–Jacobs 1998 for BC-in-fibration usage.
2. **T_M**: CAVEAT — a *lifting* always; a *fibred monad (over M)* **iff M Cartesian**. FLAG loudly:
   the standard word "fibred" bakes in Cartesian-preservation, which is exactly MacBeth's crown boundary.
3. **G_M**: MATCH — vertical fibred comonad, for all M.
4. **λ**: CAVEAT — it is a mixed distributive law / entwining, not Beck–Chevalley (Def 1.9.4); and it is
   not even iso off the non-branching locus.
