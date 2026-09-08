# Neil's presheaf-variant container: shapes = small category, positions = functor into Set

*MacBeth — 2026-09-06. Scoping note for Neil (CC Robin). Grade discipline: speculative < computed < proved < [cited].*

**Neil's steer (verbatim intent).** "Take Shapes to be small categories and Positions to be functors into Set. These are of course presheaves." Data: a small category `𝕊` and a functor `P : 𝕊 → Set`. Compare the ordinary container `(S : Set, P : S → Set)` with `⟦S,P⟧ X = Σ_{s∈S} Set(P s, X) = ∐_s X^{P s}`.

**How this differs from my 2026-09-04 Cat-sketch (#3).** That sketch took positions to be an *indexed category* `P : 𝕊 → Cat` and landed on 2-functors `Cat → Cat`, weighted (co)limits, and a *double-category* guess for the directed version — coherence-heavy, weak, speculative. Neil's new steer is strictly simpler: positions into **Set**, not **Cat**. The whole thing collapses out of 2-category theory into ordinary (1-categorical) **parametric-right-adjoint / nerve** theory, which is completely standard. That is the main finding: the Set-valued version is *not* exotic — it is textbook — and identifying exactly which textbook is the value.

---

## 1. The correct extension functor and its type

### 1.1 Answer

For the extension to be **covariant in `X`** and to **use the morphisms of `𝕊` non-trivially**, the type-correct construction is the **nerve** associated to `P`:

> **`N_P : Set → [𝕊^op, Set]`,  `N_P(X) = Set(P(−), X)`,  i.e. `s ↦ Set(P s, X)`.**  `[computed; = cited construction, see §2]`

- **Variance.** `P : 𝕊 → Set` covariant ⟹ `s ↦ Set(P s, X)` is contravariant in `s`, i.e. a presheaf on `𝕊`, so it lands in `[𝕊^op, Set]`. Covariant in `X` ✓. (If one prefers to call `P` itself "a presheaf" `𝕊^op → Set`, rename `𝕊 ↝ 𝕊^op`; the content is identical. I state it with `P` covariant so the codomain is honestly a presheaf category.)
- `N_P` is a **right adjoint**. Its left adjoint is the **realization / coend**
  `|−|_P : [𝕊^op, Set] → Set`,  `Q ↦ ∫^{s∈𝕊} Q(s) · P(s)` (the tensor `Q ⊗_𝕊 P`).
  This is the **nerve–realization (Kan / "Isbell") adjunction** `|−|_P ⊣ N_P` for `P : 𝕊 → Set`. `[cited, standard]`

### 1.2 Why NOT "just `Set → Set`"

The naive wish is an endofunctor `Set → Set`, `X ↦ "∐_{s∈𝕊} X^{P s}"`. But `∐` over the *objects* of a genuine category, made to respect morphisms, is a **colimit** `colim_{𝕊}`, and that **over-collapses**. Worked case — the walking arrow `𝕊 = (a →^{f} b)`, `P` a function `Pf : Pa → Pb`:
- integrand `s ↦ X^{P s}` is contravariant in `s`, a diagram `X^{Pb} →^{(−)∘Pf} X^{Pa}` shaped `• → •`;
- its colimit is the *target* `X^{Pa}` alone — the `b`-shape is annihilated. `[computed]`

So the honest statement: the ordinary container endofunctor `∐_s X^{Ps}` is `(∐) ∘ N_P` with `𝕊` **discrete**, where `∐ = colim` happens to be exact because a discrete diagram has no arrows to collapse. Once `𝕊` has arrows, post-composing with `colim` is the *wrong* move; the information-preserving object is the presheaf `N_P(X)` itself, before any summation. **The extension of a presheaf-variant container is genuinely presheaf-valued.**

### 1.3 Discrete-degeneration check (the correctness test)

`𝕊 = S` discrete ⟹ `[𝕊^op, Set] = Set^S` and
`N_P(X) = (s ↦ Set(P s, X)) = (s ↦ X^{P s})`. `[computed ✓]`
Post-compose with `∐ : Set^S → Set` (colimit over the discrete `S`) to recover the classical endofunctor `∐_s X^{Ps}`. So the ordinary container extension is **exactly** the `𝕊`-discrete nerve followed by the coproduct. The construction degenerates correctly.

---

## 2. Precise prior art — this is Weber's parametric right adjoints (a nerve)

### 2.1 The exact match: Weber, Prop 2.10

**Mark Weber, "Familial 2-functors and parametric right adjoints", *Theory and Applications of Categories* 18 (2007), No. 22, pp. 665–732.** `[cited — verified via nLab]`

Weber Prop 2.10: a functor `T : [I^op,Set] → [J^op,Set]` between presheaf categories is a **parametric right adjoint (p.r.a.)** iff it has the familial form
```
T(Z)(j) = ∐_{x ∈ (T1)(j)}  [I^op,Set]( E_T(x), Z ),
```
with `T1 = T(terminal) ∈ [J^op,Set]` (the **shapes**, a presheaf) and `E_T : el(T1)^op → [I^op,Set]` (the **arities/positions**).

**Two specializations pin down both the classical and Neil's container:**

- **Ordinary container** = `I = J = 1` (so `[I^op,Set]=[J^op,Set]=Set`): `T1 = S ∈ Set`, `E_T : el(S)^op = S → Set` is `P`, and `T(Z) = ∐_{s∈S} Set(Ps, Z)`. **This is literally the ordinary container extension.** So *containers on `Set` = p.r.a. endofunctors of `Set` = familially representable functors.* `[cited]`

- **Neil's presheaf-variant** = `I = 1`, `J = 𝕊`, and **`T1` = the terminal presheaf `1` on `𝕊`** (so `(T1)(j)` is a single element for every `j`). Then `el(1) = 𝕊`, `E_T = P`, and `T(Z)(j) = Set(P j, Z) = N_P(Z)(j)`. **Neil's extension `N_P : Set → [𝕊^op,Set]` is exactly Weber's p.r.a. in the special case where the shape-presheaf is terminal.** `[computed, from cited Prop 2.10]`

So: **Neil's `(𝕊, P)` is the data of a parametric right adjoint `Set → [𝕊^op,Set]`, i.e. a familial functor in Weber's sense — with the shape-presheaf constrained to be terminal.** It is *not new in the abstract*: it is a nerve functor, the "sum of representables (fibrewise)" of Diers / Carboni–Johnstone familial representability (**Carboni–Johnstone, "Connected limits, familial representability and Artin glueing", Math. Structures Comput. Sci. 5 (1995) 441–459**; and Diers). `[cited]`

### 2.2 Generalized species (FGHW) — the OPPOSITE pole, not this

**Fiore–Gambino–Hyland–Winskel, "The cartesian closed bicategory of generalised species of structures", J. London Math. Soc. (2) 77 (2008), no. 1, 203–220, doi:10.1112/jlms/jdm096.** `[cited — verified]`

A generalized species from `A` to `B` induces a **generalised analytic functor** `[A^op,Set] → [B^op,Set]`, which is a **coend** and is **cocontinuous** (a left adjoint), with a symmetry-quotient coming from the free-symmetric-monoidal `!A`. This is the **`Σ`/`∫^`/left-adjoint pole**. Neil's container is the **`∏`/representable/right-adjoint pole** (the nerve `N_P` is a *right* adjoint; `X^{Ps}` preserves limits, not colimits). They are **adjoint siblings, not the same functor**: the FGHW analytic functor of `P` is precisely the *left adjoint* `|−|_P` to Neil's nerve. So the honest verdict: **Neil's proposal is Weber p.r.a., NOT a generalized species/analytic functor** — but the analytic functor sits on the other side of the same adjunction. This is exactly the end/coend, `∏/Σ`, nerve/realization seam that runs through all my Fam(C^op) work.

### 2.3 Gambino–Kock — where `(𝕊,P)` sits polynomially

**Gambino–Kock, "Polynomial functors and polynomial monads", Math. Proc. Camb. Phil. Soc. 154 (2013), no. 1, 153–192; arXiv:0906.4931.** `[cited — verified]`

A polynomial functor comes from a span `I ← B → A → J` in an LCC category, as `Σ ∘ Π ∘ Δ`; the single-variable case `I=J=1` over `Set` gives `X ↦ ∐_{a} X^{B_a}` = an ordinary container. Neil's `(𝕊,P)` is **not** literally a Gambino–Kock polynomial `Set → Set` (its output is presheaf-valued); it is the p.r.a./familial refinement Weber built precisely to handle the *presheaf-to-presheaf* case that GK's LCC-slice machinery covers only for `Set/I → Set/J`. Note for #3: **Gambino–Kock show polynomial functors organize into a double category (framed bicategory)** — directly relevant evidence below.

### 2.4 Novelty verdict

The extension functor and its identification (p.r.a. / familial / nerve) is **textbook** — Weber 2007, Carboni–Johnstone 1995, Diers, Kelly (nerve–realization). **Nothing in §1–§2 is new.** The value is *locating* Neil's idea: it is the "terminal-shape-presheaf" slice of Weber's p.r.a. framework, i.e. a nerve. Genuine novelty, if any, lives in §3 (does the equivalence chain lift?) and in transporting my T1/codensity results through this frame (§4, §5).

---

## 3. Does the equivalence chain lift?

Level 0: `Container ≃ Directed Container ≃ Polynomial Comonoid ≃ Small Category` `[PROVED, cited]`; a directed container is an **internal category in `Set`** (`ob = S`, `mor = ∐_s Ps`), with **morphisms = cofunctors / retrofunctors** (DCont ≅ Cof) `[PROVED, cited]`.

**Conjecture (`speculative`, well-motivated).**
> A **directed presheaf-container** — a `(𝕊, P)` equipped with the analogue of the directed-container laws D1–D5 — is equivalent to an **internal category in the presheaf topos `[𝕊^op, Set]`**, equivalently a **presheaf of small categories `𝕊^op → Cat`**.

**Evidence.**
1. Level-0 reads a directed container as `internal-cat(Set)`. Neil's variant replaces the ambient base `Set` by the presheaf topos `[𝕊^op,Set]` (that is where the extension lands). The construction should transport to `internal-cat([𝕊^op,Set])`. `[speculative]`
2. **`internal-cat([𝕊^op,Set]) ≃ [𝕊^op, Cat]`** (internal categories in a presheaf topos are presheaves of categories, since finite limits are computed pointwise). So the objects of the lifted chain are **presheaves of categories** — clean and *strict*. `[cited, standard topos fact]`
3. **This SHARPENS the earlier Cat-sketch.** The `P : 𝕊 → Cat` version forced a genuinely weak **double category** (coherence-heavy). The Set-valued version pins the answer to the *strict* corner: a presheaf of categories `𝕊^op → Cat` is exactly the discrete/strict fibrational case of a double category (its Grothendieck construction is a fibration). Gambino–Kock's "polynomial functors form a double category" (§2.3) is consistent evidence that the double-category *ambient* is right; Neil's Set-restriction just selects the strict object inside it.
4. **Morphism warning (carries over).** Because DCont ≅ Cof at level 0, expect the morphisms of the lifted equivalence to be **cofunctor-flavoured** (presheaves of cofunctors), not ordinary natural transformations of `𝕊^op → Cat`. Any attempt assuming plain maps is likely mis-typed. `[speculative, from cited DCont≅Cof]`

**Honest competing hypothesis** (do not suppress): directedness might instead want a **category enriched in `[𝕊^op,Set]`** rather than *internal* to it, or a **discrete opfibration `∫P → 𝕊` carrying a comonad** (§4.2). Which of {internal cat in topos / enriched cat / opfibration+comonad} is correct is genuinely open — see Q1.

---

## 4. Fullness — can T1 be applied?

**T1** `[PROVED, mine]`: `⟦−⟧ : Fam(C^op) → [C,C]` is fully faithful ⟺ the monoidal unit of `C` is connected.

**Honest verdict: T1 does not apply verbatim — wrong type.** T1 concerns the *endofunctor* extension `Fam(C^op) → [C,C]`. Neil's extension is the *nerve* `N_P : Set → [𝕊^op,Set]`, a different shape of functor. The correct, exactly-matching criterion is classical:

> **`N_P : Set → [𝕊^op,Set]` is fully faithful ⟺ `P : 𝕊 → Set` is a DENSE functor.** `[cited — Kelly, *Basic Concepts of Enriched Category Theory*, §5.1; the nerve is ff iff its defining functor is dense.]`

Density of `P` means `id_Set = Lan_P P`, i.e. every set is canonically a colimit of the `P s`. Examples: `P : 1 → Set` picking the singleton `1` is dense (`1` is a dense generator of `Set`) — this recovers the ordinary-container fact that `Cont` over `Set` is full.

**The bridge to T1 (this is the real content).** "Connected unit" is the **discrete-case shadow of density**:
- Over discrete `𝕊 = S`, `N_P` ff ⟺ the family `{P s}` is **dense** in `Set`. The unit container `y = (1, 1↦1)` corresponds to `P = (1 → Set)` = the singleton, which *is* the dense generator — i.e. **"connected unit" of T1 ≡ "`P` contains/ is the dense point" of the density criterion.**
- This is precisely the through-line of my **codensity = fullness** crown (Neil-K-container note: fullness of a lifted extension ⟺ a (co)density condition). So T1 and the density criterion are **the same theorem at different types**: *fullness ⟺ (co)density*, of which "connected unit" is the `Fam(C^op)` instance and "`P` dense" is the nerve instance. `[computed bridge; both endpoints cited/mine]`

**Net:** the fullness question for Neil's variant is *solved and standard* — it is density of `P` — and it is the honest generalization of my T1, not a new mystery.

---

## 5. The 2–3 genuinely open questions worth Neil's attention

**Q1 (the real prize). Where does directedness live, and what does it compute?**
Does the directed structure sit on the shapes `𝕊` (already a category) or on the positions `P`, and is a *directed presheaf-container* equal to (a) an internal category in the topos `[𝕊^op,Set]` = a **presheaf of categories `𝕊^op → Cat`**, (b) a category **enriched** in `[𝕊^op,Set]`, or (c) a **discrete opfibration `∫P → 𝕊` + comonad**? I bet (a) with **cofunctor** morphisms (§3). This is the lifted-equivalence-chain theorem and the only place a *new* grant-worthy result lives. `[open]`

**Q2. When is the induced Set-endofunctor a directed-container comonad?**
The nerve–realization adjunction gives a **density comonad** on `Set`, `D_P(X) = |N_P X|_P = ∫^{s} Set(Ps,X)·Ps`. When is `D_P` a *comonad with directed-container structure*, and does it then recover a genuine small category? This ties Neil's variant to Spivak's density comonads (2503.21974, my SEED-Q5 note) and to my codensity=fullness crown, and would give the "presheaf-container ⤳ category" bridge concretely. `[open]`

**Q3. Is "terminal shape-presheaf" the right maximal notion — or should shapes themselves be a presheaf?**
Weber's *full* generality (§2.1) allows the shapes `T1` to be **any** presheaf on `𝕊`, not just terminal. Neil's proposal is the `T1 = terminal` slice. The honest maximal container notion in this frame is **"shapes = a presheaf `T1`, positions = a functor on its category of elements `el(T1)^op → [I^op,Set]`."** Does *that* (strictly more general) object carry the equivalence chain, and is it the correct home for the container programme over presheaf bases? Deciding this is where genuine novelty — locating the whole `Container ≃ Cat` chain inside Weber's p.r.a. framework at full generality — would be a real contribution. `[open]`

---

## Honesty ledger

- **Proved, cited (anchors):** equivalence chain; DCont ≅ Cof; T1 (unit-connectedness ⟺ fullness, mine); Weber Prop 2.10 (p.r.a. = familial); Carboni–Johnstone/Diers familial representability; FGHW generalized species; Gambino–Kock polynomial functors (+ their double category); nerve ff ⟺ dense (Kelly).
- **Computed:** the nerve `N_P` is the type-correct covariant extension; discrete degeneration to `∐_s X^{Ps}`; walking-arrow collapse of the naive `Set→Set` colimit; identification of Neil's variant as Weber's terminal-shape-presheaf slice; density ≡ discrete-case "connected unit" bridge.
- **Speculative:** directed presheaf-container ≃ internal cat in `[𝕊^op,Set]` ≃ presheaf of categories, with cofunctor morphisms; competing enriched / opfibration+comonad hypotheses; density-comonad directedness.
- **Novelty verdict:** the extension = a nerve = Weber p.r.a. is **textbook, not new**. New work, if pursued: Q1 (lifted chain), Q3 (full Weber generality), and transporting my T1/codensity apparatus through the familial frame.
```
