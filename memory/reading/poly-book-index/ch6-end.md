# Niu–Spivak, *Polynomial Functors: A Mathematical Theory of Interaction* — THEOREM INDEX, Ch. 6 to end

**Source:** arXiv:2312.00990 (last updated 20 Aug 2024). PDF in seed at
`/home/agent/git/ghani-containers/pdf/spivak-poly/Niu-Spivak_Polynomial-Functors-Mathematical-Theory-of-Interaction_2023.pdf`

**Pages covered:** printed pp. **177–351** (PDF pages 189–363; printed page = PDF page − 12).
- Ch. 6 "The composition product" — pp. 177–224 (§6.1–6.4 text pp. 177–213; §6.5 solutions pp. 214–224)
- Ch. 7 "Polynomial comonoids and retrofunctors" — pp. 225–288 (§7.5 solutions pp. 276–288)
- Ch. 8 "Categorical properties of polynomial comonoids" — pp. 289–348 (§8.5 solutions pp. 339–348)
- Ch. 9 "New horizons" — pp. 349–350
- Bibliography — p. 351 ff.

**Items indexed: 313 numbered items** (Ch. 6: 6.1–6.91; Ch. 7: 7.1–7.110; Ch. 8: 8.1–8.112). Chapter 9 has no numbered environments (14 unnumbered open questions).

> **CRITICAL NOTE ON NUMBERING.** This book uses **ONE shared counter** for environments *and* displayed equations. So `6.57` is a Proposition but `6.58` and `6.59` are equations. **A gap in the environment numbering is an equation, not a missing item.** Any novelty grep must search equation numbers too.

> **TERMINOLOGY WARNING.** The book says **"retrofunctor"**, NOT "cofunctor". It explicitly states these are the same thing (footnote 6, p. 253; §7.4, p. 276) and that Aguiar's term was "cofunctor". **Grepping this book for "cofunctor" finds almost nothing.** Likewise the book writes `⊳` for what MacBeth writes `◁`. Throughout this index `◁` = the book's `⊳`.

---

## AT A GLANCE — the 10 most citation-dangerous results in this range

| # | Result | What a container theorist would independently rediscover it AS |
|---|---|---|
| 1 | **Prop. 6.57 (Meyers) + Eq. (6.58), (6.59)**, p. 204 — `Poly(p, r ◁ q) ≅ Poly(⌜q/p⌝, r)` with `⌜q/p⌝ := Σ_{i∈p(1)} y^{q(p[i])}` | "the ◁ **co**closure", "the right-coclosure of the substitution product", "the home of directed-container morphisms", "the left adjoint of `− ◁ q`". **This is the one MacBeth's memory already logs as `◁ right-coclosure = home of DCont morphisms`.** Credited to **Josh Meyers**, and the book itself hedges: "it may have already been known in the containers community." |
| 2 | **Exercise 6.63 (Trimble)**, p. 206 — the left coclosure IS a left Kan extension, `⌜q/p⌝ ≅ Lan_q p` | "the coclosure is a Lan" / "DCont morphisms live in a Kan extension". Credited to **Todd Trimble (personal communication)**. An *exercise* — exactly the kind of item a summary-reader misses. |
| 3 | **Thm. 7.28 (Ahman–Uustalu)**, p. 240 — polynomial comonoids in `(Poly, y, ◁)` ↔ small categories, one-to-one and isomorphism-preserving | "directed containers are comonoids", "comonoids in ◁ are categories". Book cites **[AU16] = Ahman–Uustalu, "Directed Containers as Categories", EPTCS 207** — i.e. the *directed container* paper by name. |
| 4 | **Def. 7.55 + Eqs. (7.56)–(7.58) + `Cat♯ ≅ Comon(Poly)`**, p. 255 — comonoid morphisms ARE retrofunctors (= Aguiar's cofunctors) | "**DCont ≅ Cof**". MacBeth's own logged result. The book derives it *by construction* (no separate numbered theorem) and credits **Aguiar [Agu97]** for cofunctors and **Paré [Par23]** for the name. |
| 5 | **Prop. 8.18** (p. 297) + **Prop. 8.33** (p. 306) + **Thm. 8.45** (p. 314) — cofree comonoid carrier `𝔱_p := Σ_{T ∈ tree_p} y^{vtx(T)}`; `U : Cat♯ → Poly` has right adjoint `T_(−)` | "**C^∞ = M-tree ◁ paths**" — MacBeth's logged "free/cofree containers proved … C^∞ IS a directed container (o=root, ↓=subtree, ⊕=concat)". The book states *exactly* this: objects = p-trees, morphisms = finite rooted paths, codomain = subtree at the path's end, identity = empty path (= root), composition = concatenation (Prop. 8.33). **Direct scoop.** |
| 6 | **Thm. 8.102**, p. 333 — an **eight-fold** equivalence: functors `C → Set` ≃ discrete opfibrations ≅ cartesian retrofunctors ≅ C-coalgebras ≅ constant left C-comodules ≅ (C,0)-bicomodules ≅ linear left C-comodules ≅ representable right C-comodules | "the equivalence chain". Any "I proved X ≅ Y" where X, Y are on this list is already here. |
| 7 | **Prop. 8.106 (Garner)**, p. 336 — `(C,D)`-bicomodules ≅ parametric right adjoints `Set^D → Set^C` ≅ connected-limit-preserving functors `Set^D → Set^C` | "bicomodules are prafunctors / familial functors". Credited to **Richard Garner**, and the book says it is **currently unpublished** (video only). The book explicitly attributes "the foundational theory of Cat♯ to **Ahman-Uustalu-Garner**" (p. 335). |
| 8 | **Example 6.85 + Eq. (6.86) + Prop. 6.87**, pp. 211–212 — the cartesian comparison lens `o_{p,q} : p ⊗ q → p ◁ q` is a **lax monoidal functor** `(Poly, y, ⊗) → (Poly, y, ◁)`; and `(y,⊗), (y,◁)` are **duoidal**, with interchange `(p ◁ p′) ⊗ (q ◁ q′) → (p ⊗ q) ◁ (p′ ⊗ q′)` | MacBeth's "**comparitor**" and his "`(⊗,◁)` duoidal frame for coherence". **Both are prior art, right here.** Note the comparitor is an *Example*, not a theorem — easy to miss. |
| 9 | **Prop. 6.73 + Eqs. (6.74), (6.75), (6.78)**, pp. 208–209 — `q ◁ −` has a **left MULTI-adjoint**: `Poly(p, q ◁ r) ≅ Σ_{f : p(1)→q(1)} Poly(p ⌢^f q, r)`, `p ⌢^f q := Σ_{i∈p(1)} q[f(i)]·y^{p[i]}` | "the *other* adjoint of ◁", "the indexed coclosure". Less famous than the coclosure, fully numbered, and easy to think you invented. |
| 10 | **Thm. 6.80** (p. 210) + **Eq. (6.82)** — `◁` preserves **connected limits on BOTH sides**; consequently `p ◁ (qr) ≅ (p ◁ q) ×_{(p◁1)} (p ◁ r)` | "◁ preserves pullbacks", "the repaired right-distributivity of ◁". Alternative proof credited to **[GK12, Prop. 1.16] = Gambino–Kock**. |

**Honourable mentions (also dangerous):** Prop. 6.47 + (6.48)–(6.51) (left distributivity of ◁ over Σ and Π); Prop. 7.79 (`Mon^op ↪ Cat♯` fully faithful, image = representable carriers); Prop. 7.85 (retrofunctors between state categories = **very well-behaved lenses**, get-put/put-get/put-put); Prop. 8.73 (**Porst**: `U : Cat♯ → Poly` is comonadic); Prop. 8.90 (left C-comodules ≃ functors `C → Poly`); Thm. 8.61 (arrow fields functor `Cat♯ → Mon^op` is right adjoint to the inclusion).

**What is NOT in Ch. 6–9:** the **derivative / chain rule**. The derivative `ṗ` appears only at Example 3.22 (p. 52, out of range), and the book says "We will not use derivatives very much in the rest of this text." There is **no** chain rule for `◁` anywhere in Ch. 6–9. MacBeth's `∂(G ◁ F) ≅ (∂G ◁ F) × ∂F` is not scooped by this book. (The book does cite Abbott–Altenkirch–Ghani–McBride, "Derivatives of containers", TLCA 2003 [Abb+03], and McBride [McB01], for p. 51.)

---

## THE FOUR SPECIFIC QUESTIONS — ANSWERED

### Q1. The ◁ coclosure naming conflict — CONFIRMED, and the book says **LEFT**.

**The book (arXiv:2312.00990), Proposition 6.57, p. 204, verbatim:**

> **Proposition 6.57 (Meyers).** The composition product is **left co-closed**. That is, there exists a **left coclosure** operation, which we denote `⌜−/−⌝ : Poly^op × Poly → Poly`, such that there is a natural isomorphism
>
>     Poly(p, r ⊳ q)  ≅  Poly( ⌜q/p⌝ , r )                     (6.58)
>
> In particular, the left coclosure operation sends `q, p ∈ Poly` to
>
>     ⌜q/p⌝  ≔  Σ_{i ∈ p(1)}  y^{ q(p[i]) }                    (6.59)

(The `⌜q/p⌝` is printed as a *fraction*, `q` over `p`. The section lead-in on p. 204 also says "by appealing to the **left coclosure** of ⊳".)

**Direction of the isomorphism:** the coclosure sits in the **domain** on the right-hand side. So it is
`Poly(p, r ◁ q) ≅ Poly(⌜q/p⌝, r)` — i.e. **`⌜q/−⌝ ⊣ (− ◁ q)`**, the coclosure is LEFT adjoint to composing-with-`q`-on-the-right. (This is what makes `− ◁ q` a right adjoint, hence limit-preserving: Prop. 6.68.)

**Spivak's reference paper (arXiv:2202.00534, "Reference: categorical structures on Poly"), §5, calls the SAME thing the RIGHT-coclosure:**

> "The left Kan extension of a polynomial functor `p` along another polynomial functor `q` is again a polynomial functor, which we denote
>     `⌜q/p⌝ ≔ Σ_{I : p(1)} y^{q ⊳ (p[I])}`                     (68)
> This satisfies the following universal property of a Kan extension, i.e. a **right-coclosure**:⁹
>     `Poly(⌜q/p⌝, p′) ≅ Poly(p, p′ ⊳ q)`                       (69)"
>
> **Footnote 9:** "I learned the **right-coclosure** from Josh Meyers. I learned the in-retrospect-obvious fact that it is the same as a left Kan extension from Todd Trimble."

**Verdict:** same isomorphism, same formula, same Meyers attribution, **opposite left/right naming**. The book renamed it. The disambiguator is the **formula** `Σ_{i∈p(1)} y^{q(p[i])}` and the **Meyers** credit, never the word "left"/"right".

**Extra trap:** arXiv:2202.00534 *also* has a genuinely different **"indexed left ⊳-coclosure"** (Eqs. 99–101): `p ⌢^f q := Σ_{I:p(1)} q[fI]·y^{p[I]}` with `Poly(p, q ⊳ r) ≅ Σ_{f : p(1)→q(1)} Poly(p ⌢^f q, r)`. **The book has this too** — it is Prop. 6.73 / Eqs. (6.74), (6.75), (6.78), and the book's §6.4 summary calls it the **left multi-adjoint** of `q ◁ −`. So the two papers have BOTH structures; only the names for the first one clash.

**Trimble's Kan-extension observation is Exercise 6.63 (p. 206) in the book** — "In personal communication, Todd Trimble noted (the in-retrospect-obvious fact) that the left coclosure can be thought of as a left Kan extension." (And it is footnote 9 of arXiv:2202.00534.)

**§6.4 "Summary and further reading", p. 213/214, verbatim:**
> "We learned of the left coclosure (see Proposition 6.57) from **Josh Meyers**, though **it may have already been known in the containers community**."

That hedge is the book conceding it does not claim priority — but it is still the citable numbered statement.

### Q2. Comonoids — YES, Theorem 7.28, credited to Ahman–Uustalu, and BOTH directions are given (but not as a formal 2-part proof).

**Theorem 7.28 (Ahman-Uustalu), p. 240, verbatim:**
> "There is a one-to-one isomorphism-preserving correspondence between polynomial comonoids and (small) categories."

- **Credit:** in the theorem's title, and in prose on p. 225 ("In 2018, researchers Daniel Ahman and Tarmo Uustalu presented a characterization of comonoids in (Poly, y, ⊳)…") and p. 240 ("What Ahman and Uustalu showed…"). §7.4 (p. 276) cites **[AU16] = Ahman & Uustalu, "Directed Containers as Categories", EPTCS 207 (2016), arXiv:1604.01187** — cited on p. 276 **only**.
- **Strength:** a **one-to-one correspondence**, i.e. a bijection on objects, *not* an equivalence of categories. **Remark 7.32** (p. 241) explicitly defends this wording: (7.29) and (7.30) "really can be just strict equalities. This is why we are comfortable naming a 'one-to-one correspondence' … rather than just, say, some form of equivalence."
- **Both directions?** **Yes, both** — but there is **no `Proof.` environment**. The proof is the running text of §7.2.1 (pp. 240–246), which ends: "We've seen that the data and equations of polynomial comonoids correspond exactly to the data and equations of categories. **This proves Theorem 7.28.**"
  - *category ⟹ comonoid*: **Definition 7.31** (p. 241), the polynomial carrier `Σ_{i ∈ Ob C} y^{C[i]}` where `C[i] := Σ_{j} C(i,j)`.
  - *comonoid ⟹ category*: **Eq. (7.29)** `𝔠(1) = Ob C`, **Eq. (7.30)** `𝔠[i] = Σ_{j∈Ob C} C(i,j)`, then the unnumbered subsections mapping each comonoid law to each category law.
  - The load-bearing summary is an **unnumbered table on p. 242**.
- **Law-by-law dictionary** (this is the part worth grepping):

| comonoid law | becomes |
|---|---|
| right erasure `δ # (𝔠 ◁ ε) = id`, on positions | the bottom arrow of `δ` is `id_{𝔠(1)}` |
| left erasure `δ # (ε ◁ 𝔠) = id`, on positions | `cod(id_i) = i` |
| erasure laws, on **directions** | `id_i # f = f = f # id_{cod f}` |
| coassociativity, on **positions** | `cod(f # g) = cod g` |
| coassociativity, on **directions** | `(f # g) # h = f # (g # h)` |

- **Formulas:** carrier `𝔠 = Σ_{i∈Ob C} y^{C[i]}`; `ε : 𝔠 → y` on directions is `ε♯_i(∗) = id_i`; `δ : 𝔠 → 𝔠 ◁ 𝔠` on positions is `i ↦ (i, cod)` with `cod : C[i] → Ob C`, and on directions is `δ♯_i(f, g) = f # g`.

### Q3. Cofunctors — the book calls them **retrofunctors**, defines them at **Def. 7.55 (p. 255)**, and declares **`Cat♯ ≅ Comon(Poly)` in that same definition**. It does NOT connect them to *directed container* morphisms.

**Definition 7.55 (Retrofunctor), p. 255, verbatim:**
> "Let C and C′ be (small) categories. A **retrofunctor** `F : C ⇸ C′` consists of
> • a function `F : Ob C → Ob C′` **forward on objects**, and
> • a function `F♯_c : C′[Fc] → C[c]` **backward on morphisms** for each `c ∈ Ob C`,
> satisfying the following conditions, collectively known as the **retrofunctor laws**:
> i. `F` preserves identities: `F♯_c id_{Fc} = id_c`  **(7.56)**
> ii. `F` preserves codomains: `F(cod F♯_c g) = cod g`  **(7.57)**
> iii. `F` preserves composites: `F♯_c g # F♯_{cod F♯_c g} h = F♯_c(g # h)`  **(7.58)**
> We let **`Cat♯ ≅ Comon(Poly)`** denote the category of (small) categories and retrofunctors."

- **`Cat♯ = Comod(Poly)`? NO — the book says `Cat♯ ≅ Comon(Poly)`, comon*oids*, not comod*ules*.** That identification is stated (a) inside Def. 7.55, p. 255; (b) p. 256, "Henceforth we will identify the category Cat♯ with the isomorphic category Comon(Poly)"; (c) p. 324, inside the proof of Prop. 8.73. Comod*ules* are a *different* Ch. 8 topic (§8.3): left/right comodules and bicomodules over comonoids, which assemble into `Mod`.
- **There is NO separate numbered theorem "comonoid morphisms = retrofunctors."** §7.3 is *titled* "Morphisms of polynomial comonoids are retrofunctors", and the identification is made **by construction**: Def. 7.49 (comonoid morphism, general monoidal category) is specialised to `(Poly, y, ◁)` via polyboxes (7.53)/(7.54), and Def. 7.55 falls out. "(Here (7.56) is equivalent to (7.53), while (7.57) and (7.58) are together equivalent to (7.54))" (p. 255).
- **"cofunctor" — YES, the book says they are the same thing**, twice:
  - **Footnote 6, p. 253:** "Many authors have referred to these as **cofunctors**, including ourselves in other work and in early versions of this book. However, the prefix *co* in category theory is very special—having to do with taking opposites—and we will see in Remark 7.59 that comonoid homomorphisms are not just opposite-functors. Thus to keep the prefix *co* more pristine, and in solidarity with other researchers, we have decided to use the term **retrofunctor**, which is an appropriate usage of the term defined by **Bob Paré [Par23]**."
  - **§7.4, p. 276:** "Retrofunctors were first defined by **Marcelo Aguiar [Agu97]**, though **his definition was opposite to ours; he referred to these as cofunctors**."
  - Also p. 261: retrofunctors `C ⇸ y^ℕ` "have been called **admissible sections** [Agu97]"; the book renames them **arrow fields**.
- **Directed containers — NO.** The phrases "directed container", "container", "morphism of directed containers" appear **nowhere** in Ch. 6–9 body text. `[AU16]` ("Directed Containers as Categories") is cited exactly once, on p. 276, and only for the *objects* half (comonoids = categories). **The book never says "directed-container morphisms are retrofunctors."** It leaves that to the reader. (So MacBeth's `DCont ≅ Cof` is not *literally* in the book — but it is one composition step away from Thm. 7.28 + Def. 7.55 + [AU16], and Cat♯ is already known as `Comon(Poly)`.)
- **Remark 7.59 (p. 256)** explains "retro": viewing categories as monads in `Span`, a functor is a monad map one way and a **retrofunctor is the monad map the other way** — citing **Paré [Par23, Def. 6.1]** ("retromorphism of monads").
- **Cat♯ as a double category is NOT defined here.** Footnote 9 (p. 256) refers to "the (yet-undefined) double category Cat♯" and defers it. Ch. 8 §8.3 builds comodules/bicomodules (the 1-cells) but never says "double category".

### Q4. Free monad / cofree comonad — the **cofree comonoid is Theorem 8.45** and its carrier is **Prop. 8.18**. The **free monad is NOT constructed.**

**Proposition 8.18, p. 297, verbatim:**
> "For `p ∈ Poly`, let
>     `𝔱_p ≔ Σ_{T ∈ tree_p} y^{vtx(T)}`
> be the polynomial whose **positions are p-trees** and whose **directions at each p-tree are the rooted paths**. Then `𝔱_p` is the limit of the diagram (8.1), with projections `ε_p^{(n)} : 𝔱_p → p^{◁n}` for every `n ∈ ℕ` …"

**Eq. (8.1), p. 290** — the tower whose limit is `𝔱_p`:
`y ← p ← p^{◁2} ← p^{◁3} ← ⋯` over `1 ←! p◁1 ← p^{◁2}◁1 ← p^{◁3}◁1 ← ⋯`

**IMPORTANT — what "paths" means.** The directions at `T` are **ALL finite rooted paths** of `T`, equivalently **all vertices**: `𝔱_p[T] = vtx(T) = Σ_{n∈ℕ} p^{◁n}[π^{(n)}T]` (p. 296). They are **NOT** root-to-leaf (maximal) paths. Maximal rooted paths appear only once, in Example 8.50 (p. 317), where they encode the accepted words of a halting automaton. (An *infinite* "path" is called a **ray**, not a path.)

**Theorem 8.45 (Cofree comonoid), p. 314, verbatim:**
> "The forgetful functor `U : Cat♯ → Poly` has a **right adjoint** `T_(−) : Poly → Cat♯`, giving rise to an adjunction `Cat♯ ⇄ Poly`, such that for each `p ∈ Poly`, the carrier `𝔱_p ≔ U T_p` of the category `T_p` is given by the limit of the diagram (8.1) … That is, for any category `C ∈ Cat♯` with carrier `𝔠 ≔ U C`, there is a natural isomorphism
>     `Poly(𝔠, p) ≅ Cat♯(C, T_p)`."

**The cofree comonoid AS A CATEGORY — Proposition 8.33, p. 306, verbatim:**
> "`(𝔱_p, ε_p, δ_p)` is a polynomial comonoid corresponding to a category `T_p` characterized as follows.
> • An **object** in `T_p` is a p-tree `T ∈ tree_p`.
> • A **morphism** emanating from `T` is a **rooted path** in `T`; its **codomain is the p-subtree rooted at the end of the path**.
> • The **identity** morphism on `T` is its **empty rooted path**.
> • **Composition** is given by **concatenating rooted paths**…"

Restated in §8.4 (p. 338): "the category corresponding to `T_p` has p-trees as its objects; the morphisms emanating from such a p-tree are the finite rooted paths up the tree, and the codomain of such a path is the tree rooted at its endpoint."

Duplicator (**Eq. 8.32**, p. 305): `δ_p` is the **unique** lens with `δ_p # (ε_p^{(ℓ)} ◁ ε_p^{(m)}) = ε_p^{(ℓ+m)}` for all `ℓ, m ∈ ℕ`; in elements, `cod v := T(v)` (subtree at `v`) and `v # w := v ⇝ w` (path concatenation).

**Also: Prop. 8.57 (p. 319) — every cofree category `T_p` is FREE ON A GRAPH** `G_p` (vertices `tree_p`, arrows `Σ_{t} p[π_1(t)]`), and **Cor. 8.58** — every morphism in `T_p` is both **monic and epic**.

**⇒ This is precisely MacBeth's `C^∞ = M-tree ◁ paths` with `o = root`, `↓ = subtree`, `⊕ = concat`. It is Prop. 8.18 + Thm. 8.45 + §8.4. SCOOPED.**

Closed forms the book computes (Solution to Ex. 8.17, pp. 340–341):
`𝔱_1 ≅ y`, `𝔱_2 ≅ 2y`, `𝔱_y ≅ y^ℕ`, `𝔱_{y²} ≅ y^{List(2)}`, `𝔱_{2y} ≅ 2^ℕ·y^ℕ`, `𝔱_{y+1} ≅ {∞}·y^ℕ + Σ_{n∈ℕ} y^{n+1}`, **`𝔱_{B y^A} ≅ B^{List(A)} · y^{List(A)}`** where `List(A) = Σ_{n∈ℕ} A^n`.

Fixed-point form: **the book never displays `C_p ≅ y × (p ◁ C_p)` or any fixed-point equation.** The closest it comes is **Exercise 8.16** (p. 295), which asks the reader to show `tree_p → p(tree_p)` is a bijection — i.e. `tree_p` is the **terminal `p`-coalgebra** (Lambek). The text says (p. 295): "it is the terminal coalgebra for the functor `p`". **No attribution** (this is classically Adámek/Barr; the book cites nobody).

**Free monad:** the book does **not** construct it. There is no free-monad / initial-algebra / `W`-type section in Ch. 6–9. Monads in Poly are an **open question** — Chapter 9, Question 11: "Characterize the monads in poly. They're generalizations of one-object operads (which are the Cartesian ones), but how can we think about them?" **Cofree comonad:** the book identifies polynomial comonoids with **comonads** (Remark 7.18, p. 236: "comonoids in a functor category with respect to the composition product are exactly comonads; so 'polynomial comonoid' = 'polynomial comonad'"), so Thm. 8.45 *is* the cofree-comonad-on-a-polynomial theorem — but the book credits no one for it.

---

## CHAPTER 9 "NEW HORIZONS" (pp. 349–350) — the book's own open problems

Framing (p. 349): *"we lay out some questions that whose answers may or may not be known, but which were **not known to us** at the time of writing."* — **Chapter 9 cites NO ONE.** Zero names, zero references. An item appearing here is NOT evidence of an open problem in the literature, only that Niu–Spivak had not resolved it.

1. Comonoids in `[Set, Set]` that aren't polynomial.
2. Internal logic of the topos `[T_p, Set]` in terms of `p`.
3. How that logic helps study dynamical systems.
4. Morphisms `p → q` in Poly give left adjoints `T_p → T_q` preserving connected limits (not geometric morphisms — they fail to preserve the terminal object but preserve *all* connected limits). How do they translate internal-language statements?
5. **`×`-(co)monoids and `⊗`-(co)monoids in `Poly`, `Cat♯`, and `Mod`** — "Find examples … perhaps characterize them or create a theory of them." *(Directly = MacBeth's four-monoidal-structures census programme. The authors flag it as OPEN.)*
6. Is there a functor from the bicategory of spans in Poly to `Mod` sending `p ↦ T_p`?
7. Databases ↔ dynamical systems interaction.
8. Dynamic database aggregation.
9. Replace `Set` with homotopy types.
10. Non-polynomial functors `Set → Set` admitting a `(y, ◁)`-comonoid structure.
11. **Characterize the monads in Poly** (the Cartesian ones = one-object operads).
12. **Describe the limits in `Cat♯` combinatorially.** *(So an explicit combinatorial limit computation in Cat♯ is, by the authors' own admission, NOT in this book.)*
13. `U : Cat♯ → Poly` is faithful so reflects monos; are ALL monomorphisms in `Cat♯` of that form?
14. Gödel-numbering propositions of `[tree_p, Set]` into a language `p`-dynamical systems can work with.

---

## ATTRIBUTION LEDGER (every external credit in Ch. 6–9)

| Credited to | For what | Where |
|---|---|---|
| **Josh Meyers** | the **left coclosure** of `◁` (Prop. 6.57) | Prop. 6.57 title, p. 204; §6.4, p. 213/214 ("may have already been known in the containers community") |
| **Todd Trimble** | the coclosure is a **left Kan extension** (personal communication) | Exercise 6.63, p. 206 |
| **Gambino–Kock [GK12]** | polynomial substitution generally; an alternative proof that `◁` preserves connected limits [GK12, Prop. 1.16] | p. 208; §6.4, p. 213/214; also p. 37 |
| **Bart Jacobs [Jac17]** | coalgebras as models of dynamical systems | Example 6.67, p. 206 |
| **nLab [nLa19]** | connected limits, Thm. 4.3 (used in proof of Thm. 6.80) | p. 210 |
| **Ahman–Uustalu [AU16]** | **comonoids in Poly = categories** (Thm. 7.28). Paper title: *"Directed Containers as Categories"*, EPTCS 207 (2016), arXiv:1604.01187 | Thm. 7.28 title, p. 240; prose p. 225, p. 240; §7.4, p. 276 (**only citation of [AU16] in the book**) |
| **Marcelo Aguiar [Agu97]** | **retrofunctors — he called them COFUNCTORS**, with the opposite convention; also "admissible sections" for `C ⇸ y^ℕ` | §7.4, p. 276; Example 7.71, p. 261 |
| **Bob Paré [Par23]** | the *term* "retrofunctor"; retromorphisms of monads in double categories like Span [Par23, Def. 6.1] | footnote 6, p. 253; Remark 7.59, p. 256 |
| **David Spivak [Spi12]** | copresheaves as categorical databases | p. 274 |
| **nLab [nLa22]** | lenses (in computer science) | §7.4, p. 276 |
| **H.-E. Porst [Por19]** | **Prop. 8.73**: `U : Cat♯ → Poly` is **comonadic** [Por19, Fact 3.1]; and Cat♯ has all small limits [Por19, Fact 3.4] | Prop. 8.73, p. 324; Cor. 8.78, p. 326 |
| **Robert Paré [Par69]** | "Absolute coequalizers" — the argument generalised in Prop. 8.73 | p. 324 |
| **Max Kelly [Kel74]** | **doctrinal adjunction** — used to prove the cofree functor `T` is **lax monoidal** for `⊗` (Prop. 8.81) | p. 327 |
| **Richard Garner** | **Prop. 8.106**: `(C,D)`-bicomodules ≅ **parametric right adjoints** `Set^D → Set^C`. **"currently unpublished"** — video only: https://www.youtube.com/watch?v=tW6HYnqn6eI | Prop. 8.106, p. 336; §8.3.4 preamble, p. 335; §8.4, p. 338 |
| **Ahman-Uustalu-Garner** (jointly) | *"Thus we attribute the **foundational theory of Cat♯** to Ahman-Uustalu-Garner."* | p. 335, verbatim |
| **Spivak–Wisnesky [SW15]** | parametric right adjoints model data migration between categorical databases | p. 336 |
| **Weber [Web07], Garner–Hirschowitz [GH18], Shapiro [Sha21]** | prafunctors are elsewhere called **familial functors** between (co)presheaf categories | §8.4, p. 338 |
| *(unattributed, "functional programming community")* | **very well-behaved lenses** (get-put / put-get / put-put) = retrofunctors between state categories | Example 7.85, pp. 265–267; §7.4, p. 276 |
| *(no attribution — presented as the book's own)* | the comparison lens `o_{p,q} : p ⊗ q → p ◁ q` and the `(⊗, ◁)` **duoidal** structure | Example 6.85, Prop. 6.87, pp. 211–212 |
| *(no attribution)* | the **cofree comonoid** `𝔱_p = Σ_{T∈tree_p} y^{vtx(T)}` and the adjunction `U ⊣ T_(−)` | Prop. 8.18, Thm. 8.45 |


---
---

# CHAPTER 6 — The composition product (pp. 177–224)

*Chapter theme: `◁` (printed `⊳`), its formula, its action on lenses, its distributivity, its coclosure, its limit preservation, its duoidal interaction with `⊗`.*

### 6.1 Definition — Composition product   [p. 178]
**Statement:** For polynomial functors `p, q`, the composition product `p ∘ q : Set → Set` sends `X ↦ p(q(X))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 6.1, p. 178
**Keywords:** composition product, substitution product, p ◁ q, composite functor

### 6.2 Proposition — Poly is closed under composition   [p. 178]
**Statement:** If `p, q ∈ Poly` then `p ∘ q ∈ Poly`; proof rewrites the ΣΠΣΠ form (6.3) via distributivity (1.30) into the single-Σ normal form (6.4).
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 6.2, p. 178
**Keywords:** Poly closed under composition, ΣΠΣΠ, distributivity

### 6.3 Equation — ΣΠΣΠ formula   [p. 178]
**Statement:** `p ◁ q ≅ Σ_{i∈p(1)} Π_{a∈p[i]} Σ_{j∈q(1)} Π_{b∈q[j]} y`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.3), p. 178
**Keywords:** ΣΠΣΠ, nested formula, composite polynomial

### 6.4 Equation — Single-sum normal form   [p. 178]
**Statement:** `p ◁ q ≅ Σ_{i∈p(1)} Σ_{j : p[i]→q(1)} y^{Σ_{a∈p[i]} q[j(a)]}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.4), p. 178
**Keywords:** normal form, j : p[i] → q(1), Σ_{a∈p[i]} q[j(a)]

### 6.5 Corollary — (Poly, y, ◁) is monoidal   [p. 178]
**Statement:** Poly has a monoidal structure `(y, ◁)` with unit the identity functor `y`; introduces `p^{◁n}`, with `p^{◁0} = y`, `p^{◁1} = p`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Corollary 6.5, p. 178
**Keywords:** monoidal structure, unit y, p^{◁n}, n-fold composite

### 6.6 Equation — ΣΠΣΠ formula in ◁ notation   [p. 179]
**Statement:** `p ◁ q ≅ Σ_{i∈p(1)} Π_{a∈p[i]} Σ_{j∈q(1)} Π_{b∈q[j]} y`. (The workhorse formula, cited throughout.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.6), p. 179
**Keywords:** ΣΠΣΠ, workhorse formula

### 6.7 Equation — Normal form in ◁ notation   [p. 179]
**Statement:** `p ◁ q ≅ Σ_{i∈p(1)} Σ_{j : p[i]→q(1)} y^{Σ_{a∈p[i]} q[j(a)]}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.7), p. 179
**Keywords:** normal form, positions as functions

### 6.8 Exercise — Compute (y²+y) ◁ (y³+1)   [p. 179]
**Statement:** With `p := y²+y`, `q := y³+1`: compute `y² ◁ q ≅ q×q ≅ y⁶+2y³+1`, `y ◁ q ≅ q`, so `p ◁ q ≅ y⁶+3y³+2`; count functions `j : p[i] → q(1)` and the exponents `Σ_{a∈p[i]} q[j(a)]`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.8, p. 179 (solution p. 214)
**Keywords:** worked example, y⁶+3y³+2

### 6.9 Exercise — ◁ preserves representable / linear / constant   [p. 179]
**Statement:** `y^A ◁ y^B ≅ y^{A×B}`; `(Ay) ◁ (By) ≅ ABy`; `A ◁ B ≅ A` (constants).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.9, p. 179 (solution p. 214)
**Keywords:** representable, linear, constant, closure under ◁

### 6.10 Exercise — Representable ◁ IS the ⊗-internal-hom   [p. 179]
**Statement:** For all `A ∈ Set`, `q ∈ Poly`: `y^A ◁ q ≅ [Ay, q]`, where `[−,−]` is the closure for `⊗` from (4.75). Explicitly `y^A ◁ q ≅ Σ_{j : A→q(1)} y^{Σ_{a∈A} q[j(a)]}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.10, p. 179 (solution p. 215)
**Keywords:** y^A ◁ q ≅ [Ay, q], parallel product closure, internal hom, Dirichlet hom

### 6.11 Definition — Horizontal composition of natural transformations   [p. 180]
**Statement:** For `f : p → p'`, `g : q → q'`, the horizontal composite `f ◁ g : p ◁ q → p' ◁ q'` has X-component `p(q(X)) --f_{q(X)}--> p'(q(X)) --p'(g_X)--> p'(q'(X))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 6.11, p. 180
**Keywords:** horizontal composition, f ◁ g, action of ◁ on morphisms

### 6.12 Equation — The horizontal composite's X-component   [p. 180]
**Statement:** `(f ◁ g)_X = f_{q(X)} # p'(g_X)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.12), p. 180
**Keywords:** f_{q(X)}, p'(g_X), X-component

### 6.13 Exercise — Interchange: the other order agrees   [p. 180]
**Statement:** Show `f_{q(X)} # p'(g_X) = p(g_X) # f_{q'(X)}` (naturality of `f`), so (6.14) may replace (6.12) in Def. 6.11.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.13, p. 180 (solution p. 215)
**Keywords:** interchange law, naturality square, well-definedness

### 6.14 Equation — Alternative composite   [p. 180]
**Statement:** `(f ◁ g)_X = p(g_X) # f_{q'(X)}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.14), p. 180
**Keywords:** alternative order

### 6.15 Remark — "Composite lens" vs "composition product of lenses"   [p. 180]
**Statement:** Terminology: *composite lens* `h # j` (vertical composition in Poly, written `#`) vs *composition product* `f ◁ g` (the monoidal product on lenses = horizontal composition). `∘` is avoided.
**Cite as:** Niu–Spivak arXiv:2312.00990, Remark 6.15, p. 180
**Keywords:** vertical vs horizontal composition, # notation, terminology

### 6.16 Equation — Positions of a composite   [p. 181]
**Statement:** `(p ◁ q)(1) ≅ Σ_{i∈p(1)} Set(p[i], q(1))` — a position is a `p`-position `i` plus a function `j : p[i] → q(1)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.16), p. 181
**Keywords:** (p ◁ q)(1), Set(p[i], q(1)), composite positions

### 6.17 Equation — Directions of a composite   [p. 181]
**Statement:** `(p ◁ q)[(i,j)] ≅ Σ_{a∈p[i]} q[j(a)]`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.17), p. 181
**Keywords:** (p ◁ q)[(i,j)], composite directions

### 6.18 Exercise — Instructions for p^{◁3} and p ◁ p ◁ 1   [p. 182]
**Statement:** Write out the uncollapsed "instructions" (choose position; for each direction choose next position; …) for `p^{◁3}` and for `p ◁ p ◁ 1` ("choose an element of 1" = "done").
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.18, p. 182
**Keywords:** instructions, nesting, n-fold composite, strategy

### 6.19 Exercise — The composition product of lenses, explicitly   [p. 183]
**Statement:** Derive that `f ◁ g` has on-positions `(i, j_i) ↦ (f_1(i), f♯_i # j_i # g_1)` (6.20) and on-directions `(a', b') ↦ (f♯_i(a'), g♯_{j_i(f♯_i(a'))}(b'))` (6.21).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.19, p. 183 (solution pp. 215–216)
**Keywords:** composition product of lenses, on-positions, on-directions

### 6.20 Equation — On-positions of f ◁ g   [p. 183]
**Statement:** `(f ◁ g)_1 : (i, j_i) ↦ (f_1(i), f♯_i # j_i # g_1)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.20), p. 183
**Keywords:** (f ◁ g)_1, f♯_i # j_i # g_1

### 6.21 Equation — On-directions of f ◁ g   [p. 183]
**Statement:** `(f ◁ g)♯_{(i,j_i)} : (a', b') ↦ (f♯_i(a'), g♯_{j_i(f♯_i(a'))}(b'))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.21), p. 183
**Keywords:** (f ◁ g)♯, backward pass

### 6.22 Equation — Running-example corolla forests   [p. 183]
**Statement:** The corolla forests of `p := y²+y` and `q := y³+1`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.22), p. 183
**Keywords:** corolla forest, running example

### 6.23 Equation — Positions of p ◁ q by grafting roots   [p. 184]
**Statement:** `(p ◁ q)(1)` drawn as the six trees obtained by grafting a `q`-root onto every leaf of a `p`-corolla in all ways (`2² = 4` from `y²`, `2` from `y`).
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.23), p. 184
**Keywords:** grafting, roots onto leaves

### 6.24 Equation — p ◁ q as a forest of height-2 trees   [p. 184]
**Statement:** `p ◁ q` with full `q`-corollas grafted on; directions = rooted paths of length 2 (height-2 leaves). Reads off `p ◁ q ≅ y⁶ + 3y³ + 2`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.24), p. 184
**Keywords:** height-2 leaves, rooted path, tree picture of ◁

### 6.25 Equation — The "pedantic" corolla forest of p ◁ q   [p. 184]
**Statement:** The literal corolla forest of `p ◁ q` with levels smashed: six corollas with 6, 3, 3, 0, 3, 0 leaves.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.25), p. 184
**Keywords:** smashed levels, pedantic corolla forest

### 6.26 Exercise — Draw composites as trees   [p. 185]
**Statement:** With `p := y²+y`, `q := y³+1`, `r := 2y+1`, draw `q ◁ p`, `p ◁ p`, `p ◁ p ◁ 1`, `r ◁ r`, `r ◁ r ◁ r` as forests.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.26, p. 185
**Keywords:** draw trees, non-commutativity of ◁

### 6.27 Example — Composing with constants   [p. 185]
**Statement:** `p(X) ≅ p ◁ X`. With `p := y³+y+1`, `X := 2`: `p ◁ 2 ≅ 11` while `2 ◁ p ≅ 2`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.27, p. 185
**Keywords:** p ◁ X ≅ p(X), constant polynomial, X ◁ p ≅ X

### 6.28 Exercise — X ◁ p ≅ X and p ◁ X ≅ p(X)   [p. 185]
**Statement:** For a set `X` as a constant polynomial and any `p`: `X ◁ p ≅ X` and `p ◁ X ≅ p(X)`. Hence `p(1)` and `p ◁ 1` are interchangeable notations for the position set.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.28, p. 185 (solution p. 217)
**Keywords:** X ◁ p ≅ X, p ◁ X ≅ p(X), p ◁ 1, position-set

### 6.29 Exercise — φ ◁ X is the X-component of φ   [p. 186]
**Statement:** For `φ : p → q` and a set `X`, the lens `φ ◁ X : p(X) → q(X)` is exactly the X-component `φ_X` of `φ` as a natural transformation.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.29, p. 186 (solution p. 217)
**Keywords:** φ ◁ X, X-component, lens as natural transformation

### 6.30 Exercise — y is the ◁-unit   [p. 186]
**Statement:** `p ◁ y ≅ p ≅ y ◁ p`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.30, p. 186 (solution pp. 217–218)
**Keywords:** unitors, monoidal unit

### 6.31 Example — φ ◁ ψ drawn on trees   [p. 186]
**Statement:** For `φ : p → p'`, `ψ : q → q'`, `φ ◁ ψ` is computed on trees by (6.20)/(6.21): `φ_1` pushes the bottom corolla forward, `φ♯_i` pulls leaves back, `ψ_1` pushes the grafted corolla forward, `ψ♯_j` pulls height-2 leaves back.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.31, p. 186
**Keywords:** φ ◁ ψ, tree picture, zig-zag, forward-backward

### 6.32 Exercise — Draw ψ ◁ φ   [p. 188]
**Statement:** Draw `ψ ◁ φ : q ◁ p → q' ◁ p'` in terms of trees (order matters).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.32, p. 188
**Keywords:** ψ ◁ φ, order matters

### 6.33 Exercise — Does the interchange square commute? (NO)   [p. 188]
**Statement:** Given `φ : q → p ◁ q` and `ψ : q → q ◁ r`, must `φ # (p ◁ ψ) = ψ # (φ ◁ r)`? **No.** Counterexample: `p := y`, `q := 2`, so both are functions `2 → 2`; take `φ ≡ 1`, `ψ ≡ 2`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.33, p. 188 (solution p. 218)
**Keywords:** interchange fails, counterexample, coalgebra compatibility

### 6.34 Equation — On-positions of φ ◁ φ for a dynamical system   [p. 189]
**Statement:** `(φ ◁ φ)_1(s_0, e^{-1}) = (φ_1(s_0), φ♯_{s_0} # e^{-1} # φ_1)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.34), p. 189
**Keywords:** φ ◁ φ, two-step dynamics

### 6.35 Equation — The next-position function   [p. 189]
**Statement:** `p[o_0] --φ♯_{s_0}--> q[s_0] = S' --e^{-1}--> S = q(1) --φ_1--> p(1)`: given direction `i_1` at the returned position `o_0`, this composite gives the next position `o_1`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.35), p. 189
**Keywords:** update then return, next position, dynamical system step

### 6.36 Example — Substitution products of dynamical systems as trees   [p. 189]
**Statement:** For the halting DFA `φ : Sy^S → p` with `p := y^A + 1`, `φ ◁ φ` sends the two-level state tree (6.37) to a decision tree giving the two-step dynamics.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.36, p. 189
**Keywords:** halting automaton, y^A + 1, decision tree, two steps

### 6.37 Equation — A position of Sy^S ◁ Sy^S   [p. 190]
**Statement:** The two-level tree whose root is a state and whose height-1 vertices are the states the root's directions point to — the "correct" grafting.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.37), p. 190
**Keywords:** correct grafting, state tree

### 6.38 Example — Composition products of dynamical systems can be misleading   [p. 191]
**Statement:** A *different* valid position of `Sy^S ◁ Sy^S` (wrong corollas grafted) makes `φ ◁ φ` report nonsense dynamics. This extraneous data motivates the transition lens `δ`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.38, p. 191
**Keywords:** wrong grafting, extraneous data, motivation for comonoid

### 6.39 Equation — Polyboxes for a lens p → q₁ ◁ q₂   [p. 193]
**Statement:** `Poly(p, q₁ ◁ q₂) ≅ Π_{i∈p(1)} Σ_{j₁∈q₁(1)} Π_{b₁∈q₁[j₁]} Σ_{j₂∈q₂(1)} Π_{b₂∈q₂[j₂]} p[i]`. Generalises to n-fold composites.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.39), p. 193
**Keywords:** polyboxes, lens to composite, multi-step policy, stacked boxes

### 6.40 Example — Lenses p → q ◁ r as a triple (φ^q, φ^r, φ♯)   [p. 194]
**Statement:** A lens `φ : p → q ◁ r` splits into `φ^q : p(1) → q(1)`, plus for each `i` a function `φ^r_i : q[φ^q(i)] → r(1)`, plus `φ♯_i : (q ◁ r)[φ_1(i)] → p[i]`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.40, p. 194
**Keywords:** φ^q, φ^r, φ♯, triple, empty direction set

### 6.41 Example — Dynamical systems with composite interfaces   [p. 195]
**Statement:** `φ : Sy^S → q ◁ r` uses two interfaces in succession: state ↦ `q`-position `j`; on receiving `b ∈ q[j]`, returns an `r`-position `k`; on receiving `c ∈ r[k]`, updates the state. Metaphor: cascading menus.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.41, p. 195
**Keywords:** composite interface, cascading menus, successive interaction

### 6.42 Equation — Polyboxes for φ ◁ φ'   [p. 196]
**Statement:** `φ ◁ φ' : p ◁ p' → q ◁ q'` is drawn by stacking polyboxes, identifying the lower `p'`-position box with the upper `p`-direction box (likewise `q'`/`q`), filling bottom-up.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.42), p. 196
**Keywords:** stacked polyboxes, monoidal product of lenses

### 6.43 Example — Dynamical systems and ◁, revisited   [p. 197]
**Statement:** `φ^{◁3} : (Sy^S)^{◁3} → p^{◁3}` as three stacked return/update polybox pairs. Resolves the notation problem but not the "blue boxes should fill automatically" problem.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.43, p. 197
**Keywords:** φ^{◁n}, three-step polyboxes, blue box problem

### 6.44 Example — The transition lens δ of a state system   [p. 198]
**Statement:** `δ : Sy^S → Sy^S ◁ Sy^S` with `δ_0 = id_S`; `δ_1 = tgt : (s_0, s_1) ↦ s_1` (target function); `δ_2 = run : (s_0, s_1, s_2) ↦ s_2`. Then `δ # (φ ◁ φ)` correctly simulates two steps. Foreshadows the comonoid.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.44, p. 198
**Keywords:** transition lens δ, target function tgt, run function, comonoid foreshadowing

### 6.45 Exercise — Counter dynamical system   [p. 201]
**Statement:** `S := ℕ`, `p := ℝy`, `φ_1(k) := k`, `φ♯_k(1) := k+1`. Draw polyboxes and `δ # (φ ◁ φ) : Sy^S → p ◁ p`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.45, p. 201 (solution p. 219)
**Keywords:** counter, δ # (φ ◁ φ), two runs

### 6.46 Exercise — δ as a standalone dynamical system   [p. 202]
**Statement:** `δ : Sy^S → Sy^S ◁ Sy^S` is itself a dynamical system with interface `Sy^S ◁ Sy^S`; describe its dynamics. Solution: `Sy^S ◁ Sy^S ≅ (S × S^S)·y^{S×S}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.46, p. 202 (solution p. 219)
**Keywords:** δ as dynamical system, Sy^S ◁ Sy^S ≅ (S × S^S) y^{S×S}

### 6.47 Proposition — LEFT distributivity of ◁ over + and ×   [p. 202]
**Statement:** `(− ◁ r)` commutes with coproducts and products: `(p+q) ◁ r ≅ (p ◁ r) + (q ◁ r)`, `pq ◁ r ≅ (p ◁ r)(q ◁ r)`, and generally `(Σ_{a∈A} q_a) ◁ r ≅ Σ_{a∈A}(q_a ◁ r)`, `(Π_{a∈A} q_a) ◁ r ≅ Π_{a∈A}(q_a ◁ r)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 6.47, p. 202
**Keywords:** left distributivity, (p+q) ◁ r, pq ◁ r, Σ and Π distribute on the left

### 6.48 Equation — `(p + q) ◁ r ≅ (p ◁ r) + (q ◁ r)`   [p. 202]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.48), p. 202
**Keywords:** coproduct distributes on the left

### 6.49 Equation — `pq ◁ r ≅ (p ◁ r)(q ◁ r)`   [p. 202]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.49), p. 202
**Keywords:** product distributes on the left

### 6.50 Equation — `(Σ_{a∈A} q_a) ◁ r ≅ Σ_{a∈A} (q_a ◁ r)`   [p. 202]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.50), p. 202
**Keywords:** arbitrary coproduct

### 6.51 Equation — `(Π_{a∈A} q_a) ◁ r ≅ Π_{a∈A} (q_a ◁ r)`   [p. 202]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.51), p. 202
**Keywords:** arbitrary product

### 6.52 Exercise — Prove 6.47 by Σ/Π manipulation   [p. 203]
**Statement:** Prove Prop. 6.47 from (6.6) by manipulating sums and products (the Π case uses (1.32), distributivity of Π over Σ).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.52, p. 203 (solution p. 219)
**Keywords:** explicit proof, Σ/Π manipulation

### 6.53 Example — Picturing left distributivity over ×   [p. 203]
**Statement:** `p := y`, `q := y+1`, `r := y²+1`: grafting-then-gluing = gluing-then-grafting, so `pq ◁ r ≅ (p ◁ r)(q ◁ r)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.53, p. 203
**Keywords:** picture proof, gluing roots, grafting leaves

### 6.54 Exercise — Picture left distributivity over +   [p. 204]
**Statement:** Give a pictorial understanding of `(p + q) ◁ r ≅ (p ◁ r) + (q ◁ r)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.54, p. 204
**Keywords:** coproduct picture, forests

### 6.55 Exercise — `A(p ◁ q) ≅ (Ap) ◁ q`   [p. 204]
**Statement:** For any set `A`: `(A·p) ◁ q ≅ A·(p ◁ q)` (via (6.51) plus `A ◁ q ≅ A`).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.55, p. 204 (solution p. 220)
**Keywords:** copower, scalar multiple pulls out on the left

### 6.56 Exercise — RIGHT distributivity FAILS   [p. 204]
**Statement:** Find `p,q,r` with `p ◁ (qr) ≇ (p ◁ q)(p ◁ r)` and with `p ◁ (q+r) ≇ (p ◁ q) + (p ◁ r)`. Counterexample: `p := y+1`, `q := 1`, `r := 0` gives `1 ≇ 2` and `2 ≇ 3`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.56, p. 204 (solution p. 220)
**Keywords:** counterexample, right distributivity fails

### 6.57 Proposition (MEYERS) — ◁ is LEFT COCLOSED   [p. 204]
**Statement:** There is a left coclosure `⌜−/−⌝ : Poly^op × Poly → Poly` with natural iso `Poly(p, r ◁ q) ≅ Poly(⌜q/p⌝, r)`, where `⌜q/p⌝ := Σ_{i∈p(1)} y^{q(p[i])}`. Equivalently `⌜q/−⌝ ⊣ (− ◁ q)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 6.57, p. 204
**Keywords:** left coclosure, coclosed, Poly(p, r ◁ q) ≅ Poly(⌜q/p⌝, r), Σ_{i∈p(1)} y^{q(p[i])}, adjunction, Meyers, RIGHT-coclosure (in arXiv:2202.00534)
**Attribution:** **Josh Meyers** (named in the statement). §6.4: "though it may have already been known in the containers community." NOTE: arXiv:2202.00534 Eq. (68)–(69) calls this same iso the **RIGHT**-coclosure.

### 6.58 Equation — The coclosure adjunction   [p. 204]
**Statement:** `Poly(p, r ◁ q) ≅ Poly(⌜q/p⌝, r)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.58), p. 204
**Keywords:** coclosure adjunction, hom-iso
**Attribution:** Meyers (via Prop. 6.57).

### 6.59 Equation — Formula for the left coclosure   [p. 204]
**Statement:** `⌜q/p⌝ := Σ_{i∈p(1)} y^{q(p[i])}` — positions are `p`-positions `i`; directions at `i` are elements of `q(p[i])`, i.e. pairs `(j, φ♯ : q[j] → p[i])`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.59), p. 204
**Keywords:** ⌜q/p⌝, coclosure formula, q(p[i])
**Attribution:** Meyers (via Prop. 6.57).

### 6.60 Exercise — Rewrite the coclosure proof in Σ/Π notation   [p. 205]
**Statement:** Translate the polybox proof of Prop. 6.57 into Σ/Π notation: `Poly(p, r ◁ q) ≅ Π_{i∈p(1)} r(q(p[i])) ≅ Poly(Σ_{i∈p(1)} y^{q(p[i])}, r)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.60, p. 205 (solution p. 220)
**Keywords:** coclosure proof, Σ/Π notation

### 6.61 Remark — Why the polybox proof   [p. 205]
**Statement:** The Σ/Π proof is more obviously rigorous; polyboxes show *what the adjunction does* — data on the codomain side of `p → r ◁ q` is repackaged onto the domain side of `⌜q/p⌝ → r`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Remark 6.61, p. 205
**Keywords:** polyboxes, adjunction intuition

### 6.62 Exercise — Functoriality of the coclosure   [p. 205]
**Statement:** `⌜−/−⌝` is functorial: for `φ : p → p'`, `⌜q/φ⌝` has on-positions `φ_1` and on-directions `q(φ♯_i) : q(p'[φ_1(i)]) → q(p[i])` (apply the FUNCTOR `q`). For `ψ : q' → q`, `⌜ψ/p⌝` has on-positions `id` and on-directions `ψ_{p[i]} : q'(p[i]) → q(p[i])` (the `p[i]`-component of `ψ`).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.62, p. 205 (solution pp. 220–221)
**Keywords:** functoriality, covariant in p, contravariant in q, q(φ♯_i), ψ_{p[i]}

### 6.63 Exercise (TRIMBLE) — The coclosure IS a left Kan extension   [p. 206]
**Statement:** Verify that the left coclosure is a left Kan extension: `⌜q/p⌝ ≅ Lan_q p` (the Lan of `p : Set → Set` along `q : Set → Set`).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.63, p. 206 (solution p. 221)
**Keywords:** left Kan extension, Lan_q p, coclosure, Trimble
**Attribution:** **Todd Trimble**, personal communication: "noted (the in-retrospect-obvious fact) that the left coclosure can be thought of as a left Kan extension." (Same credit appears as footnote 9 of arXiv:2202.00534.)

### 6.64 Exercise — Two monomial hom-isomorphisms   [p. 206]
**Statement:** Prove `Poly(Ay^B, p) ≅ Set(A, p(B))` (6.65) and `Poly(Ay ◁ p ◁ y^B, q) ≅ Poly(p, y^A ◁ q ◁ By)` (6.66). Solution also yields `⌜B/A⌝ ≅ A·y^B` and `⌜By/p⌝ ≅ p ◁ y^B`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.64, p. 206 (solution p. 221)
**Keywords:** Poly(Ay^B, p), monomial adjunctions

### 6.65 Equation — Monomial hom-formula   [p. 206]
**Statement:** `Poly(Ay^B, p) ≅ Set(A, p(B))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.65), p. 206
**Keywords:** Poly(Ay^B, p) ≅ Set(A, p(B)), coalgebra

### 6.66 Equation — Conjugation adjunction   [p. 206]
**Statement:** `Poly(Ay ◁ p ◁ y^B, q) ≅ Poly(p, y^A ◁ q ◁ By)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.66), p. 206
**Keywords:** Ay ◁ p ◁ y^B, y^A ◁ q ◁ By, linear/representable conjugation

### 6.67 Example — Dynamical systems ARE coalgebras   [p. 206]
**Statement:** Taking `A = B = S` in (6.65): `Poly(Sy^S, p) ≅ Set(S, p(S))` — dynamical systems `Sy^S → p` are exactly `p`-coalgebras `S → p(S)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.67, p. 206
**Keywords:** coalgebra, S → p(S), Sy^S → p, coalgebra for a functor vs comonad
**Attribution:** "Coalgebras as models of dynamical systems have been studied extensively in the context of computer science, most notably by **Jacobs** in **[Jac17]**."

### 6.68 Proposition — Left preservation of limits   [p. 207]
**Statement:** `◁` preserves **all** limits on the left: `(lim_{j∈J} p_j) ◁ q ≅ lim_{j∈J}(p_j ◁ q)`. Proof: by 6.57, `(− ◁ q)` is a right adjoint.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 6.68, p. 207
**Keywords:** limits on the left, right adjoint preserves limits

### 6.69 Equation — `(lim_{j∈J} p_j) ◁ q ≅ lim_{j∈J} (p_j ◁ q)`   [p. 207]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.69), p. 207
**Keywords:** limit preservation on the left

### 6.70 Exercise — Consequences of (6.69)   [p. 207]
**Statement:** (1) Use (6.69) + (6.50) to get `X ◁ p ≅ X`; (2) deduce (6.51) from (6.69) by taking `J` discrete.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.70, p. 207 (solution p. 221)
**Keywords:** deduce (6.51), limit argument

### 6.71 Definition — Connected limit   [p. 207]
**Statement:** A **connected limit** is a limit whose indexing category `J` is nonempty and connected (any two objects joined by a finite zigzag).
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 6.71, p. 207
**Keywords:** connected limit, connected category, zigzag

### 6.72 Example — Which categories are connected   [p. 207]
**Statement:** Connected: `•`, `•⇉•`, `•→•←•`, `•←•←•←⋯` — so **equalizers, pullbacks, inverse limits are connected**. NOT connected: `∅`, `• •` — so **terminal objects and products are NOT connected limits**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.72, p. 207
**Keywords:** equalizer, pullback, directed limit, products not connected

### 6.73 Proposition — Slice adjunction: the LEFT MULTI-ADJOINT of (q ◁ −)   [p. 208]
**Statement:** For `f : p → q ◁ 1`, `Poly_{/(q ◁ 1)}(p, q ◁ r) ≅ Poly(p ⌢^f q, r)` where `p ⌢^f q := Σ_{i∈p(1)} q[f(i)] · y^{p[i]}` (positions `(i,b)` with `b ∈ q[f(i)]`; directions at `(i,b)` are `p[i]`).
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 6.73, p. 208
**Keywords:** slice category Poly/(q ◁ 1), p ⌢ q, left multiadjoint, indexed coclosure

### 6.74 Equation — The slice hom-isomorphism   [p. 208]
**Statement:** `Poly_{/(q ◁ 1)}(p, q ◁ r) ≅ Poly(p ⌢^f q, r)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.74), p. 208
**Keywords:** slice hom, p ⌢^f q

### 6.75 Equation — Formula for `p ⌢^f q`   [p. 208]
**Statement:** `p ⌢^f q := Σ_{i∈p(1)} q[f(i)] · y^{p[i]}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.75), p. 208
**Keywords:** p ⌢^f q, Σ_{i∈p(1)} q[f(i)] y^{p[i]}
**Attribution:** Same construction as the "indexed left ⊳-coclosure", arXiv:2202.00534 Eq. (99).

### 6.76 Remark — Notation for ⌢   [p. 209]
**Statement:** A lens `p → q ◁ 1` is identified with its on-positions function `p(1) → q(1)`; `p ⌢^f q` is used for both.
**Cite as:** Niu–Spivak arXiv:2312.00990, Remark 6.76, p. 209
**Keywords:** notation, on-positions function

### 6.77 Exercise — The multi-adjoint formula   [p. 209]
**Statement:** Prove `Poly(p, q ◁ r) ≅ Σ_{f : p(1)→q(1)} Poly(p ⌢^f q, r)` — so `(q ◁ −)` has a **left multi-adjoint**. Also `Poly(p, q ◁ 1) ≅ Set(p(1), q(1))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.77, p. 209 (solution p. 222)
**Keywords:** left multiadjoint, Σ over f : p(1)→q(1)

### 6.78 Equation — Hom into a composite as a sum over on-positions maps   [p. 209]
**Statement:** `Poly(p, q ◁ r) ≅ Σ_{f : p(1)→q(1)} Poly(p ⌢^f q, r)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.78), p. 209
**Keywords:** multiadjoint formula
**Attribution:** = arXiv:2202.00534 Eq. (100).

### 6.79 Exercise — Functoriality of ⌢   [p. 209]
**Statement:** `p ⌢^f q` is covariant in `p` and contravariant in `q`; construct `p' ⌢^{g#f} q → p ⌢^f q` for `g : p' → p` and `p ⌢^{f#(h◁1)} q' → p ⌢^f q` for `h : q → q'`, and prove functoriality.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.79, p. 209 (solution p. 222)
**Keywords:** functoriality of ⌢

### 6.80 Theorem — Preservation of CONNECTED LIMITS on BOTH sides   [p. 210]
**Statement:** For `J` connected: `(lim_{j∈J} p_j) ◁ q ≅ lim_{j∈J}(p_j ◁ q)` AND `q ◁ (lim_{j∈J} p_j) ≅ lim_{j∈J}(q ◁ p_j)`. Proof: left = Prop. 6.68; right — Poly is complete (Thm. 5.33), so by [nLa19, Thm. 4.3] it suffices that `(q ◁ −)` preserve **wide pullbacks**, which follows from Prop. 6.73.
**Cite as:** Niu–Spivak arXiv:2312.00990, Theorem 6.80, p. 210
**Keywords:** connected limits, both sides, wide pullbacks, ◁ preserves pullbacks
**Attribution:** proof cites **[nLa19, Thm. 4.3]** (nLab); an **alternative proof** of this fact is credited on p. 208 to **[GK12, Proposition 1.16] = Gambino–Kock**.

### 6.81 Exercise — Applications of Theorem 6.80   [p. 210]
**Statement:** (1) Every polynomial `p : Set → Set` preserves connected limits of sets. (2) Prove `p ◁ (qr) ≅ (p ◁ q) ×_{(p ◁ 1)} (p ◁ r)` (6.82) — since `qr ≅ q ×_1 r` and pullbacks ARE connected limits. (3) Check against the Ex. 6.56 counterexample.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.81, p. 210 (solution p. 222)
**Keywords:** p preserves connected limits, fibre product over p ◁ 1

### 6.82 Equation — The right-hand "distributivity" that DOES hold   [p. 210]
**Statement:** `p ◁ (qr) ≅ (p ◁ q) ×_{(p ◁ 1)} (p ◁ r)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.82), p. 210
**Keywords:** repaired right distributivity, pullback over p ◁ 1

### 6.83 Proposition — ⊗ preserves connected limits   [p. 211]
**Statement:** For `J` connected: `(lim_{j∈J} p_j) ⊗ q ≅ lim_{j∈J}(p_j ⊗ q)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 6.83, p. 211
**Keywords:** parallel product ⊗, connected limits

### 6.84 Exercise — ⊗ vs ◁ on monomials   [p. 211]
**Statement:** Decide which of `(Ay)⊗(By) ≟ (Ay)◁(By)`, `y^A ⊗ y^B ≟ y^A ◁ y^B`, `A ⊗ B ≟ A ◁ B`, `By ⊗ p ≟ By ◁ p`, `y^A ⊗ p ≟ y^A ◁ p`, `p ⊗ By ≟ p ◁ By`, `p ⊗ y^A ≟ p ◁ y^A` hold. (1,2,4,7 hold; 3,5,6 fail but have canonical lenses.) **All lenses found are CARTESIAN.**
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.84, p. 211 (solution p. 223)
**Keywords:** ⊗ vs ◁, monomials, canonical lens, cartesian

### 6.85 Example — THE COMPARITOR `o_{p,q} : p ⊗ q → p ◁ q`   [p. 211]
**Statement:** For all `p, q` there is a **cartesian** lens `o_{p,q} : p ⊗ q → p ◁ q` that "orders" the symmetric `⊗` into the asymmetric `◁`: on positions `(i,j) ↦ (i, const_j)`; on directions `(a,b) ↦ (a,b)`. Its image is the positions of `p ◁ q` whose upper-level corollas are all the same. **"The lenses `o_{p,q}` constitute a LAX MONOIDAL FUNCTOR `(Poly, y, ⊗) → (Poly, y, ◁)`. In particular, `o_{p,q}` commutes with associators and unitors."** By symmetry there is also `p ⊗ q → q ◁ p`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 6.85, p. 211
**Keywords:** comparitor, o_{p,q}, p ⊗ q → p ◁ q, lax monoidal functor, cartesian lens, order-independent positions
**Attribution:** none — presented as the book's own.

### 6.86 Equation — The DUOIDAL interchange lens   [p. 212]
**Statement:** `(p ◁ p') ⊗ (q ◁ q') → (p ⊗ q) ◁ (p' ⊗ q')`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.86), p. 212
**Keywords:** duoidal, interchange lens

### 6.87 Proposition — `(y, ⊗)` and `(y, ◁)` are DUOIDAL on Poly   [p. 212]
**Statement:** The monoidal structures `(y, ⊗)` and `(y, ◁)` together comprise a **duoidal structure** on Poly, the key condition being the natural lens (6.86). On positions `((i,i'),(j,j')) ↦ ((i,j), (a,b) ↦ (i'(a), j'(b)))`; on directions `(a',b') ↦ ((a,a'),(b,b'))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 6.87, p. 212
**Keywords:** duoidal structure, ⊗ and ◁, interchange
**Attribution:** none — presented as the book's own.

### 6.88 Proposition — ◁ preserves CARTESIAN lenses   [p. 213]
**Statement:** If `φ : p → p'` and `ψ : q → q'` are cartesian, so is `φ ◁ ψ`. Proof: cartesian = naturality squares are pullbacks (Prop. 5.59); paste, using that `◁` preserves pullbacks (Thm. 6.80).
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 6.88, p. 213
**Keywords:** cartesian lens, φ ◁ ψ cartesian, pullback pasting

### 6.89 Exercise — ◁ does NOT preserve vertical lenses   [p. 213]
**Statement:** (1) If `φ` is an iso and `ψ` is vertical then `φ ◁ ψ` is vertical. (2) Counterexample without the iso hypothesis: `φ : y → 1` is vertical but `φ ◁ 0 : 0 → 1` is not.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 6.89, p. 213 (solution p. 223)
**Keywords:** vertical lens, φ ◁ ψ not vertical, counterexample, OFS

### 6.90 Equation — Adjunction `(Ay ◁ −) ⊣ (y^A ◁ −)`   [p. 221]
**Statement:** `Poly(Ay ◁ p, q) ≅ Poly(p, y^A ◁ q)` — from `Ay ◁ p ≅ A·p`, `y^A ◁ q ≅ q^A`, and the copower/power adjunction (5.9).
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.90), p. 221
**Keywords:** composition product adjunction, Ay ◁ p, y^A ◁ q, copower power

### 6.91 Equation — Adjunction `(− ◁ y^B) ⊣ (− ◁ By)`   [p. 221]
**Statement:** `Poly(p ◁ y^B, q) ≅ Poly(p, q ◁ By)` — via the coclosure formula `⌜By/p⌝ = Σ_{i∈p(1)} y^{B·p[i]} ≅ p ◁ y^B` and (6.58). Combined: `Poly(Ay ◁ p ◁ y^B, q) ≅ Poly(p, y^A ◁ q ◁ By)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (6.91), p. 221
**Keywords:** composition product adjunction, p ◁ y^B, q ◁ By, coclosure

## §6.5 Exercise solutions (pp. 214–224) — additional citable content

- **Sol. 6.19** (pp. 215–216): full on-positions/on-directions formula for `f ◁ g`, plus its natural-transformation X-component.
- **Sol. 6.46** (p. 219): `Sy^S ◁ Sy^S ≅ S·(Sy^S)^S ≅ (S × S^S)·y^{S×S}`.
- **Sol. 6.62** (pp. 220–221): the coclosure's functorial action — `⌜q/φ⌝♯_i = q(φ♯_i)` (apply the functor `q`); `⌜ψ/p⌝♯_i = ψ_{p[i]}` (the component of `ψ`).
- **Sol. 6.63** (p. 221, printed as "Solution to Exercise 6.3.2" — a numbering glitch): the unit `p → ⌜q/p⌝ ◁ q` of (6.58) is universal, which is exactly the Lan property.
- **Sol. 6.77** (p. 222): `Poly(p, q ◁ 1) ≅ Set(p(1), q(1))`; the multi-adjunction derivation.
- **Sol. 6.81** (p. 222): products are not connected limits but **pullbacks are**, which is what makes (6.82) work; Example 5.38 (pullbacks in Poly: positions pull back, directions push out).
- **Sol. 6.84** (p. 223): full `⊗`-vs-`◁` table; "every lens we found in this exercise is **cartesian**".

---
---

# CHAPTER 7 — Polynomial comonoids and retrofunctors (pp. 225–288)

*Chapter theme: comonoids in `(Poly, y, ◁)` ARE small categories (Ahman–Uustalu); their morphisms are retrofunctors (= Aguiar's cofunctors); `Cat♯ ≅ Comon(Poly)`.*

### 7.1 Equation — Polyboxes for the do-nothing section ε : 𝔰 → y   [p. 226]
**Statement:** `ε : 𝔰 → y` is the dependent function `(s ∈ 𝔰(1)) → 𝔰[s]`, `s ↦ id_s`, choosing at each state a distinguished "stay put" direction.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.1), p. 226
**Keywords:** do-nothing section, eraser, counit, ε : 𝔰 → y, id_s

### 7.2 Exercise — What does ε : 𝔰 → y tell you about 𝔰?   [p. 226]
**Statement:** A lens `𝔰 → y` is a section `(s ∈ 𝔰(1)) → 𝔰[s]`, so every direction-set `𝔰[s]` is nonempty; equivalently `𝔰` is a product of `y` with some other polynomial.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.2, p. 226 (solution p. 276)
**Keywords:** lens to y, section, nonempty directions

### 7.3 Example — The do-nothing section in tree pictures   [p. 226]
**Statement:** For `𝔰 ≅ 3y³`, `ε` marks at each of the three roots the leaf "of the same colour" as the root.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.3, p. 226
**Keywords:** tree pictures, corolla, 3y³

### 7.4 Equation — Polyboxes for the transition lens δ : 𝔰 → 𝔰 ◁ 𝔰   [p. 227]
**Statement:** `δ` has three arrows: on positions `id : s_0 ↦ s_0`; **tgt** `(s_0, a_1) ↦ s_1`; **run** `(s_0, a_1, a_2) ↦` a composite direction at `s_0`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.4), p. 227
**Keywords:** transition lens, δ : 𝔰 → 𝔰 ◁ 𝔰, tgt, run

### 7.5 Equation — Target of a run   [p. 227]
**Statement:** `tgt(s_0, run(s_0, s_0→s_1, s_1→s_2)) = s_2 = tgt(tgt(s_0, s_0→s_1), s_1→s_2)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.5), p. 227
**Keywords:** tgt/run compatibility, cod(f # g) = cod g

### 7.6 Example — The transition lens in tree pictures; "bending the arrows"   [p. 228]
**Statement:** For `𝔰 ≅ 3y³`, bending each leaf-arrow to point at its target turns the corolla forest into the **complete graph** on its 3 roots; `run` collapses each 2-arrow path to a single arrow with the same source and target.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.6, p. 228
**Keywords:** grafting, complete graph, bending the arrows

### 7.7 Equation — The two erasure (counit) triangles   [p. 231]
**Statement:** `δ # (ε ◁ 𝔰) = id_𝔰 = δ # (𝔰 ◁ ε)`. In elements: `tgt(s, id_s) = s`, `run(s, id_s, s→t) = s→t`, `run(s, s→t, id_t) = s→t`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.7), p. 231
**Keywords:** erasure law, counit law, y ◁ 𝔰 ≅ 𝔰

### 7.8 Equation — Polybox proof that δ # (δ ◁ 𝔰) = δ # (𝔰 ◁ δ)   [p. 231]
**Statement:** The two composites `𝔰 → 𝔰^{◁3}` agree; in elements this is associativity of `run`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.8), p. 231
**Keywords:** coassociativity, polyboxes, 𝔰^{◁3}

### 7.9 Exercise — The associativity equation for `run`   [p. 231]
**Statement:** `run(s_0, run(s_0, s_0→s_1, s_1→s_2), s_2→s_3) = run(s_0, s_0→s_1, run(s_1, s_1→s_2, s_2→s_3))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.9, p. 231 (solution pp. 276–277)
**Keywords:** run associativity

### 7.10 Equation — Coassociativity square; the canonical δ^{(n)}   [p. 232]
**Statement:** `δ # (δ ◁ 𝔰) = δ # (𝔰 ◁ δ)`, hence a canonical `δ^{(n)} : 𝔰 → 𝔰^{◁n}` for every `n ≥ 2`, with `δ^{(n)} = δ # (δ^{(ℓ)} ◁ δ^{(m)})` for `ℓ + m = n`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.10), p. 232
**Keywords:** coassociative law, δ^{(n)}, 𝔰^{◁n}

### 7.11 Exercise — All lenses 𝔰 → 𝔰^{◁4} built from δ agree   [p. 232]
**Statement:** List every lens `𝔰 → 𝔰^{◁4}` formed from `δ`, `id`, `◁`, `#`, and show all are equal given (7.10). Hint: the interchange law `(f # g) ◁ (h # k) = (f ◁ h) # (g ◁ k)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.11, p. 232
**Keywords:** interchange law, coassociativity, canonicity

### 7.12 Exercise — Run₀ and Run₁   [p. 234]
**Statement:** With `Run_n(φ) := δ^{(n)} # φ^{◁n}`, setting `δ^{(0)} := ε` and `δ^{(1)} := id_𝔰` gives `Run_0(φ) = ε` and `Run_1(φ) = φ`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.12, p. 234
**Keywords:** Run_n(φ) = δ^{(n)} # φ^{◁n}, nullary composite

### 7.13 Example — Returning every other position (digits of 1/7)   [p. 234]
**Statement:** `Run_2(φ) : Sy^S → ℕy ◁ ℕy ≅ ℕ²y` emits pairs; post-composing with `π₂` gives the system emitting only the digits of 1/7.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.13, p. 234
**Keywords:** Run₂, ℕ²y, π₂, sped-up system

### 7.14 Definition — COMONOID   [p. 235]
**Statement:** In a monoidal category `(C, y, ◁)`, a comonoid `𝒞 := (𝔠, ε, δ)` is a carrier `𝔠`, an **eraser** (counit) `ε : 𝔠 → y`, and a **duplicator** (comultiplication) `δ : 𝔠 → 𝔠 ◁ 𝔠`, satisfying the **erasure laws** (7.15) `δ # (ε ◁ 𝔠) = id_𝔠 = δ # (𝔠 ◁ ε)` and the **coassociative law** (7.16) `δ # (δ ◁ 𝔠) = δ # (𝔠 ◁ δ)`. A comonoid in `(Poly, y, ◁)` is a **polynomial comonoid**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 7.14, p. 235
**Keywords:** comonoid, carrier, eraser, duplicator, counit, comultiplication, polynomial comonoid

### 7.15 Equation — The erasure (counit) laws   [p. 235]
**Statement:** `δ # (ε ◁ 𝔠) = id_𝔠` (left) and `δ # (𝔠 ◁ ε) = id_𝔠` (right).
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.15), p. 235
**Keywords:** left/right erasure law, counit law

### 7.16 Equation — The coassociative law   [p. 236]
**Statement:** `δ # (δ ◁ 𝔠) = δ # (𝔠 ◁ δ) : 𝔠 → 𝔠 ◁ 𝔠 ◁ 𝔠`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.16), p. 236
**Keywords:** coassociative law

### 7.17 Remark — Terminology: "eraser" and "duplicator"   [p. 236]
**Statement:** Comonoids are dual to monoids. The book prefers "eraser" for the counit (to avoid clashing with an adjunction's counit) and "duplicator" for the comultiplication.
**Cite as:** Niu–Spivak arXiv:2312.00990, Remark 7.17, p. 236
**Keywords:** eraser, duplicator, terminology

### 7.18 Remark — Polynomial comonoids ARE polynomial COMONADS   [p. 236]
**Statement:** "Comonoids in a functor category with respect to the composition product are exactly **comonads**; so 'polynomial comonoid' = 'polynomial comonad'." The book prefers "comonoid" because it thinks in positions/directions.
**Cite as:** Niu–Spivak arXiv:2312.00990, Remark 7.18, p. 236
**Keywords:** comonad, polynomial comonad, composition product

### 7.19 Example — State systems are polynomial comonoids   [p. 236]
**Statement:** Every state system `𝔰 ≅ Sy^S` is a comonoid with eraser the do-nothing section and duplicator the transition lens; giving `δ^{(n)}` and `Run_n(φ) := δ^{(n)} # φ^{◁n}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.19, p. 236
**Keywords:** state system, do-nothing section, transition lens, Run_n

### 7.20 Proposition — Defining δ^{(n)}   [p. 237]
**Statement:** With `δ^{(0)} := ε`, `δ^{(n+1)} := δ # (δ^{(n)} ◁ 𝔠)`: (a) `δ^{(n)} : 𝔠 → 𝔠^{◁n}`; (b) `δ^{(1)} = id_𝔠`; (c) `δ^{(2)} = δ`; (d) **`δ^{(n)} = δ # (δ^{(k)} ◁ δ^{(n−k)})` for `k ≤ n`** — so the choice is canonical. (d) "amounts to coassociativity."
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 7.20, p. 237
**Keywords:** δ^{(n)}, generalized duplicator, unbiased composition, canonical

### 7.21 Exercise — Prove parts (a), (b), (c) of Prop. 7.20   [p. 237]
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.21, p. 237
**Keywords:** δ^{(1)} = id, δ^{(2)} = δ, induction

### 7.22 Example — Not all comonoids are state systems   [p. 237]
**Statement:** State systems are exactly the comonoids for which the target/codomain function `𝔠[s] → 𝔠(1)` is a **bijection** for each `s`. Nothing in the comonoid laws forces bijectivity.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.22, p. 237
**Keywords:** bijection 𝔰[s] ≅ 𝔰(1), generalized state system

### 7.23 Example — A comonoid that is not a state system: 𝔞 ≅ y² + y   [p. 238]
**Statement:** `𝔞 := {s}y^{{id_s, a}} + {t}y^{{id_t}} ≅ y² + y`; `ε` picks `id_s`, `id_t`; `δ` gives `cod(a) = t` and forces the composites `id_s # a = a`, `a # id_t = a`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.23, p. 238
**Keywords:** y² + y, walking arrow, non-state-system comonoid

### 7.24 Equation — δ on positions for 𝔞: "bending the arrows"   [p. 239]
**Statement:** Bending the leaf-arrows of `𝔞`'s corollas to point at their targets yields the graph `s --a--> t` plus identity loops.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.24), p. 239
**Keywords:** bending arrows, δ on positions, codomain assignment

### 7.25 Equation — δ on directions for 𝔞   [p. 239]
**Statement:** Whenever one of the two directions run together is an eraser-selected identity, `δ` returns the other: `id_s # a = a`, `a # id_t = a`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.25), p. 239
**Keywords:** δ on directions, run, erasure laws force identities

### 7.26 Exercise — Verify (𝔞, ε, δ) is a comonoid   [p. 240]
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.26, p. 240
**Keywords:** verify comonoid laws, y² + y

### 7.27 Exercise — Unique comonoid structure on a linear polynomial By   [p. 240]
**Statement:** For any set `B` there is a **unique** comonoid structure on `By` (each direction-set is a singleton, so `ε` and `δ` are forced). It is the discrete category on `B` (Ex. 7.36).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.27, p. 240
**Keywords:** linear polynomial, By, unique comonoid structure, discrete category

### 7.28 Theorem (AHMAN–UUSTALU) — POLYNOMIAL COMONOIDS ARE CATEGORIES   [p. 240]
**Statement:** VERBATIM: "There is a **one-to-one isomorphism-preserving correspondence between polynomial comonoids and (small) categories**." Explicitly: `Ob C = 𝔠(1)` (7.29); `𝔠[i] = Σ_{j∈Ob C} C(i,j)` = morphisms out of `i` (7.30); `ε♯_i(∗) = id_i`; `δ` on positions gives `cod : C[i] → Ob C`; `δ♯_i(f, g) = f # g`. Law dictionary: right erasure/positions ⟹ `δ`'s bottom arrow is `id_{𝔠(1)}`; left erasure/positions ⟹ `cod(id_i) = i`; erasure/directions ⟹ `id_i # f = f = f # id_{cod f}`; coassoc/positions ⟹ `cod(f # g) = cod g`; coassoc/directions ⟹ `(f # g) # h = f # (g # h)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Theorem 7.28, p. 240
**Keywords:** Ahman-Uustalu, comonoids are categories, Cat♯, one-to-one correspondence, cod, composition, identity
**Attribution:** **Ahman–Uustalu** (in the title). Prose p. 225: "In 2018, researchers Daniel Ahman and Tarmo Uustalu presented a characterization of comonoids in (Poly, y, ⊳)…". §7.4 p. 276 cites **[AU16] = "Directed Containers as Categories", EPTCS 207, arXiv:1604.01187**. NB: **no `Proof.` environment** — the proof is the running text of §7.2.1 (pp. 240–246), ending "This proves Theorem 7.28." The load-bearing table (p. 242) is **unnumbered**.

### 7.29 Equation — Positions are objects   [p. 240]
**Statement:** `𝔠(1) = Ob C`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.29), p. 240
**Keywords:** positions are objects

### 7.30 Equation — Directions at i are the morphisms OUT OF i   [p. 241]
**Statement:** `𝔠[i] = Σ_{j ∈ Ob C} C(i, j)`. The polynomial perspective is **domain-centric**; codomains live in `δ`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.30), p. 241
**Keywords:** directions are morphisms, 𝔠[i] = Σ_j C(i,j), domain-centric

### 7.31 Definition — Polynomial carrier of a category   [p. 241]
**Statement:** With `C[i] := Σ_{j ∈ Ob C} C(i, j)`, the **polynomial carrier** of `C` is `Σ_{i ∈ Ob C} y^{C[i]}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 7.31, p. 241
**Keywords:** polynomial carrier, Σ_{i∈Ob C} y^{C[i]}, f : i → _

### 7.32 Remark — Why "one-to-one correspondence", not "equivalence"; smallness   [p. 241]
**Statement:** (7.29)/(7.30) are **strict equalities**, hence "one-to-one correspondence" rather than an equivalence. Positions/directions are sets, so the categories are necessarily **small**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Remark 7.32, p. 241
**Keywords:** strict equality, small categories, size issues

### 7.33 Exercise — Carriers of six categories   [p. 242]
**Statement:** `A→B` ↦ `y²+y`; `B→A←C` ↦ `2y²+y`; empty ↦ `0`; free monoid on one endomorphism ↦ `y^ℕ`; `(ℕ, ≤)` ↦ `ℕy^ℕ`; `(ℕ, ≥)` ↦ `Σ_{n∈ℕ} y^{n+1}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.33, p. 242
**Keywords:** carrier of a category, y²+y, y^ℕ, ℕy^ℕ

### 7.34 Example — 𝔞 ≅ y² + y is the walking arrow   [p. 247]
**Statement:** The comonoid `y²+y` corresponds to the **walking arrow** `s --a--> t`, a preorder.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.34, p. 247
**Keywords:** walking arrow, preorder, thin category, y² + y

### 7.35 Exercise — The comonoid of the span preorder B ← A → C   [p. 248]
**Statement:** Carrier `y³ + 2y`; `ε` picks the identities; `δ` sets `cod f = B`, `cod g = C`; composition forced by thinness.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.35, p. 248
**Keywords:** preorder, span, y³ + 2y

### 7.36 Exercise — Which category is By?   [p. 248]
**Statement:** The **discrete category** on `B` (each object's only outgoing morphism is its identity).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.36, p. 248
**Keywords:** By, linear polynomial, discrete category

### 7.37 Exercise — A star-shaped preorder on `p := y^{n+1} + ny`   [p. 248]
**Statement:** Find a comonoid structure on `y^{n+1} + ny` whose category is a preorder: one centre object with `n+1` outgoing morphisms (its identity plus one arrow to each of `n` others), and `n` objects with only identities.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.37, p. 248
**Keywords:** y^{n+1} + ny, star-shaped, preorder

### 7.38 Example — State systems as categories: the STATE CATEGORY on S   [p. 248]
**Statement:** `𝔰 ≅ Sy^S` is exactly the comonoid whose `cod : 𝔰[s] → 𝔰(1)` are **bijections** — the **codiscrete/indiscrete preorder** on `S` (also a contractible groupoid). Underlying graph = complete graph on `S`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.38, p. 248
**Keywords:** state category, codiscrete preorder, contractible groupoid, Sy^S, complete graph

### 7.39 Exercise — Is the state category the only comonoid on Sy^S?   [p. 249]
**Statement:** No in general — e.g. monoid actions `α : S × M → S` with `|S| = |M|` give other comonoids on `Sy^M` (Ex. 7.43).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.39, p. 249
**Keywords:** Sy^S, uniqueness, monoid action

### 7.40 Example — MONOIDS are REPRESENTABLE comonoids y^M   [p. 250]
**Statement:** A monoid `(M, e, ∗)` ≅ a 1-object category ≅ a comonoid with **representable** carrier `y^M`: `ε : y^M → y` picks `e ∈ M` on directions; `δ : y^M → y^M ◁ y^M ≅ y^{M×M}` is `∗ : M × M → M` on directions. The construction inverts.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.40, p. 250
**Keywords:** representable comonoid, y^M, monoid, y^M ◁ y^M ≅ y^{M×M}

### 7.41 Exercise — Monoid laws ⟺ comonoid laws for y^M   [p. 251]
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.41, p. 251
**Keywords:** monoid axioms iff comonoid axioms, y^M

### 7.42 Example — Cyclic lists: y^{ℤ/nℤ}   [p. 251]
**Statement:** `y^{ℤ/nℤ}` sends `X ↦ X^{ℤ/nℤ}` (length-n tuples); the comonoid structure makes these **cyclic lists**. Since comonoids are closed under coproducts, `Σ_{n∈ℕ} y^{ℤ/nℤ}` is also a comonoid.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.42, p. 251
**Keywords:** cyclic list, y^{Z/nZ}, coproduct of comonoids

### 7.43 Example — MONOID ACTIONS give comonoids Sy^M   [p. 251]
**Statement:** A right action `α : S × M → S` with `α(s,e) = s`, `α(s, m∗n) = α(α(s,m), n)` gives a category with `Ob = S` and a morphism `s --m--> α(s,m)`; carrier **`Sy^M`**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.43, p. 251
**Keywords:** monoid action, α : S × M → S, Sy^M, action category

### 7.44 Exercise — The comonoid structure on Sy^M from an action   [p. 252]
**Statement:** `ε(s) = e`; `δ`: `cod(s,m) = α(s,m)`, `(m,n) ↦ m ∗ n`; verify the laws; hom-sets `MA(s,s') = {m ∈ M : α(s,m) = s'}`; compare `My^M` (regular action) with the state category of Ex. 7.38.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.44, p. 252
**Keywords:** Sy^M, monoid action comonoid, My^M, regular action

### 7.45 Example — The category of B-STREAMS: carrier B^ℕ y^ℕ   [p. 252]
**Statement:** The shift `τ : B^ℕ × ℕ → B^ℕ`, `τ(b,n) := (b_n → b_{n+1} → ⋯)`, is an action of `(ℕ, 0, +)`. Carrier **`B^ℕ y^ℕ`**: positions = B-streams, directions at `b` = `ℕ`, `cod(b,n) = τ(b,n)`. Morphisms `n : b → b'` iff `b'` is the `n`-shifted substream; identity `0`; composition = addition. (Reappears as Example 8.38.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.45, p. 252
**Keywords:** B-streams, shift action, B^ℕ y^ℕ, substream, composition is addition

### 7.46 Exercise — A comonoid structure on (ℝ/ℤ)y^ℝ   [p. 253]
**Statement:** Via the translation action of `(ℝ, 0, +)` on `ℝ/ℤ`. Is the resulting category a **groupoid**?
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.46, p. 253
**Keywords:** (ℝ/ℤ)y^ℝ, circle, translation action, groupoid

### 7.47 Definition — Degree of an object; linear objects   [p. 253]
**Statement:** `deg(c)` := the set of arrows emanating from `c` (= `C[c]`, the direction-set at the corresponding position). If `deg(c) ≅ 1`, `c` is **linear**; if `deg(c) ≅ n`, `c` has **degree n**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 7.47, p. 253
**Keywords:** degree of an object, deg(c), linear object

### 7.48 Exercise — Degrees: consequences and counts   [p. 253]
**Statement:** (1) If every object is linear, `C` is **discrete**. (2) **No object can have degree 0** (every object has its identity). (3) Find a category with an object of degree `ℕ`. (4) Count categories with one linear and one quadratic object. (5) Is (4) the same as counting comonoid structures on `y² + y`?
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.48, p. 253
**Keywords:** degree 0 impossible, y² + y, counting comonoid structures

### 7.49 Definition — Comonoid morphism   [p. 254]
**Statement:** For comonoids `C = (𝔠, ε, δ)`, `C' = (𝔠', ε', δ')` in `(C, y, ◁)`, a comonoid morphism is `F : 𝔠 → 𝔠'` with **(7.50)** `F # ε' = ε` and **(7.51)** `F # δ' = δ # (F ◁ F)`. `Comon(C)` := the subcategory of comonoids and comonoid morphisms.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 7.49, p. 254
**Keywords:** comonoid morphism, eraser preservation, duplicator preservation, Comon(Poly)

### 7.50 Equation — Eraser preservation law   [p. 254]
**Statement:** `F # ε' = ε`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.50), p. 254
**Keywords:** eraser preservation, F # ε' = ε

### 7.51 Equation — Duplicator preservation law   [p. 254]
**Statement:** `F # δ' = δ # (F ◁ F)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.51), p. 254
**Keywords:** duplicator preservation, F # δ' = δ # (F ◁ F)

### 7.52 Exercise — Comon(C) is a category   [p. 254]
**Statement:** `id_𝔠` is a comonoid morphism, and comonoid morphisms compose, using `(F # G) ◁ (F # G) = (F ◁ F) # (G ◁ G)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.52, p. 254 (solution p. 282)
**Keywords:** Comon(C) subcategory, interchange

### 7.53 Equation — Eraser law in polyboxes   [p. 255]
**Statement:** Reads off as `F♯_c(id_{Fc}) = id_c` — i.e. exactly (7.56).
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.53), p. 255
**Keywords:** polybox eraser law

### 7.54 Equation — Duplicator law in polyboxes   [p. 255]
**Statement:** Reads off as BOTH (7.57) `F(cod F♯_c g) = cod g` and (7.58) `F♯_c(g # h) = F♯_c g # F♯_{cod F♯_c g}(h)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.54), p. 255
**Keywords:** polybox duplicator law, equivalent to (7.57)+(7.58)

### 7.55 Definition — RETROFUNCTOR (= COFUNCTOR); Cat♯ ≅ Comon(Poly)   [p. 255]
**Statement:** VERBATIM: a **retrofunctor** `F : C ⇸ C'` consists of a function `F : Ob C → Ob C'` **forward on objects** and a function `F♯_c : C'[Fc] → C[c]` **backward on morphisms** for each `c`, satisfying: **(7.56)** `F♯_c(id_{Fc}) = id_c`; **(7.57)** `F(cod F♯_c g) = cod g`; **(7.58)** `F♯_c(g) # F♯_{cod F♯_c g}(h) = F♯_c(g # h)`. "We let **`Cat♯ ≅ Comon(Poly)`** denote the category of (small) categories and retrofunctors."
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 7.55, p. 255
**Keywords:** retrofunctor, cofunctor, F♯, forward on objects backward on morphisms, retrofunctor laws, Cat♯, Cat sharp, Comon(Poly), DCont ≅ Cof
**Attribution:** **Aguiar [Agu97]** first defined these (opposite convention) and **called them COFUNCTORS** (§7.4, p. 276). The *term* "retrofunctor" is from **Bob Paré [Par23]** (footnote 6, p. 253). **There is NO separate numbered theorem "comonoid morphisms = retrofunctors"** — the identification is by construction from Def. 7.49 via (7.53)/(7.54).

### 7.56 Equation — Retrofunctor law i (identities)   [p. 255]
**Statement:** `F♯_c(id_{Fc}) = id_c`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.56), p. 255
**Keywords:** preserves identities

### 7.57 Equation — Retrofunctor law ii (codomains)   [p. 255]
**Statement:** `F(cod F♯_c g) = cod g`. (Codomains are objects, so preserved *forward*.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.57), p. 255
**Keywords:** preserves codomains

### 7.58 Equation — Retrofunctor law iii (composites)   [p. 255]
**Statement:** `F♯_c(g) # F♯_{cod F♯_c g}(h) = F♯_c(g # h)`. Footnote 8: the equality of the two sides' codomains is **not** implied by the other laws and is part of the assertion.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.58), p. 255
**Keywords:** preserves composites, backward composition law

### 7.59 Remark — Why "retro": monads in Span   [p. 256]
**Statement:** Viewing `C`, `C'` as monads in `Span`, a functor is a monad map `Mor(C) ⇒ F̌ # Mor(C') # F̂`; a **retrofunctor is the monad map in the other direction**: `F̌ # Mor(C') # F̂ ⇒ Mor(C)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Remark 7.59, p. 256
**Keywords:** retromorphism of monads, Span, equipment, companion, conjoint
**Attribution:** **Paré [Par23, Definition 6.1]**. Footnote 9 mentions "the (yet-undefined) **double category** Cat♯" — deferred, never defined in the book.

### 7.60 Exercise — Identity and composite retrofunctors   [p. 256]
**Statement:** `(F # G)(c) = G(Fc)` and `(F # G)♯_c = G♯_{Fc} # F♯_c : E[G(Fc)] → D[Fc] → C[c]`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.60, p. 256 (solution p. 282)
**Keywords:** composite retrofunctor, (F#G)♯_c = G♯_{Fc} # F♯_c

### 7.61 Proposition — Retrofunctors preserve isomorphisms   [p. 257]
**Statement:** If `g : Fc → _` is an iso in `D`, then `F♯_c(g)` is an iso in `C`, with inverse `F♯_{c'}(g^{-1})` where `c' := cod F♯_c g`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 7.61, p. 257
**Keywords:** retrofunctors preserve isomorphisms

### 7.62 Exercise — C ≅ D in Cat iff C ≅ D in Cat♯   [p. 257]
**Statement:** Two categories are isomorphic in `Cat` iff isomorphic in `Cat♯` (this is what "isomorphism-preserving" in Thm. 7.28 means).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.62, p. 257 (solution pp. 282–283)
**Keywords:** isomorphism-preserving, Cat vs Cat♯

### 7.63 Example — Retrofunctors to discrete categories   [p. 258]
**Statement:** `Cat♯(C, Sy) ≅ Set(Ob C, S)` — a labelling of objects with no transition information.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.63, p. 258
**Keywords:** discrete category, carrier Sy, labelling of objects

### 7.64 Exercise — y is TERMINAL in Cat♯   [p. 259]
**Statement:** `y` has a unique comonoid structure and is terminal in `Cat♯`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.64, p. 259 (solution p. 283)
**Keywords:** terminal object of Cat♯, y terminal

### 7.65 Example — Retrofunctors to the walking arrow A   [p. 259]
**Statement:** `F : C ⇸ A` is a partition `Ob C = C_s ⊔ C_t` plus, for each `c ∈ C_s`, a chosen morphism `F♯_c(a) : c → _` with codomain in `C_t`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.65, p. 259
**Keywords:** walking arrow, chosen outgoing morphism

### 7.66 Exercise — Retrofunctor to A constant at s forces C = 0   [p. 259]
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.66, p. 259 (solution p. 283)
**Keywords:** empty category, walking arrow obstruction

### 7.67 Exercise — Retrofunctors to star-shaped, (ℕ,≤), (ℕ,≥)   [p. 260]
**Statement:** Into `(ℕ,≤)`: a labelling `Ob C → ℕ` plus a chosen morphism from each `n`-labelled object to some `(n+1)`-labelled object. Into `(ℕ,≥)`: dually.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.67, p. 260 (solution p. 283)
**Keywords:** poset (ℕ,≤), grading with successor arrows

### 7.68 Example — Retrofunctors to the walking commutative square   [p. 260]
**Statement:** Composite-preservation forces a genuine **commutative square** in `C` with a common codomain.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.68, p. 260
**Keywords:** walking commutative square, lifted commutative square

### 7.69 Exercise — Count retrofunctors CS ⇸ A (=6) and A ⇸ CS (=3)   [p. 260]
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.69, p. 260 (solution p. 284)
**Keywords:** counting retrofunctors, 6, 3

### 7.70 Exercise — y ⇸ P picks a MAXIMAL element; [m] ⇸ [n] count = 2^m   [p. 261]
**Statement:** A retrofunctor `y ⇸ P` (P a poset) is a **maximal element** of `P`. For chain posets `[n] ≅ Σ_{i=0}^{n} y^{i+1}`, there are **`2^m`** retrofunctors `[m] ⇸ [n]` (`m ≤ n`).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.70, p. 261 (solution p. 284)
**Keywords:** maximal element, chain poset, 2^m retrofunctors

### 7.71 Example — ARROW FIELDS: retrofunctors C ⇸ y^ℕ   [p. 261]
**Statement:** A retrofunctor `A : C ⇸ y^ℕ` is determined by `A♯_c(1)` = one chosen morphism out of each object, since `A♯_c(0) = id_c` and `A♯_c(m+n) = A♯_c(m) # A♯_{cod A♯_c(m)}(n)`. The book calls these **arrow fields**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.71, p. 261
**Keywords:** arrow field, admissible section, y^ℕ, vector field analogy, policy
**Attribution:** **Aguiar [Agu97]** — these have been called **"admissible sections"**. "We prefer to call them arrow fields."

### 7.72 Equation — Decomposition of an arrow field   [p. 261]
**Statement:** `c = c_0 --A♯_{c_0}(1)--> c_1 --A♯_{c_1}(1)--> ⋯ --> c_n`, with `c_{j+1} := cod A♯_{c_j}(1)`; these compose to `A♯_c(n)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.72), p. 261
**Keywords:** arrow field iteration, orbit of a state

### 7.73 Exercise — How many arrow fields on • → • ? (2)   [p. 262]
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.73, p. 262 (solution p. 284)
**Keywords:** count arrow fields

### 7.74 Exercise — C ⇸ y^ℤ and the canonical y^ℤ ⇸ y^ℕ   [p. 262]
**Statement:** `C ⇸ y^ℤ` is an *invertible* arrow field (for every `c'` there is a **unique** `c` with `cod(c.1) = c'`). The inclusion `ℕ ↪ ℤ` gives the canonical retrofunctor `y^ℤ ⇸ y^ℕ`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.74, p. 262 (solution p. 284)
**Keywords:** y^ℤ, invertible arrow field

### 7.75 Exercise — Retrofunctors between monoids; op-duality FAILS   [p. 262]
**Statement:** (1) Retrofunctors `y^M ⇸ y^N` are exactly **monoid homomorphisms `N → M`** (backwards). (2) **NO** — "the weirdest thing about retrofunctors": there is a unique retrofunctor `y ⇸ y²+y`, but reversing arrows kills it. **`Cat♯` is NOT self-dual.**
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.75, p. 262 (solution p. 284)
**Keywords:** monoid homomorphism reversed, no op-duality, Cat♯ not self-dual

### 7.76 Exercise — The projection Sy^M → y^M is a retrofunctor   [p. 263]
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.76, p. 263 (solution pp. 284–285)
**Keywords:** monoid action, Sy^M ⇸ y^M

### 7.77 Example — Retrofunctor Gy^G ⇸ y^G for a group G   [p. 263]
**Statement:** On directions `(g_1, g_2) ↦ g_1 ∗ g_2`. Laws: `g_1 ∗ e = g_1`; associativity.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.77, p. 263
**Keywords:** group, Gy^G, left translation

### 7.78 Exercise — Does 7.77 work for a mere monoid? (YES)   [p. 263]
**Statement:** "This works!" — only unitality and associativity were used.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.78, p. 263 (solution p. 285)
**Keywords:** My^M ⇸ y^M, no inverses needed

### 7.79 Proposition — Mon^op ↪ Cat♯ FULLY FAITHFUL; image = representable carriers   [p. 263]
**Statement:** "There is a fully faithful functor **`Mon^op → Cat♯`**, whose image consists of all categories whose carriers are **representable**." (Retrofunctors `y^M ⇸ y^N` = monoid homomorphisms `N → M`.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 7.79, p. 263
**Keywords:** Mon^op → Cat♯ fully faithful, representable carrier y^M

### 7.80 Proposition — `Cat♯(C, Ay) ≅ Set(Ob C, A)`   [p. 263]
**Statement:** So `Ob : Cat♯ → Set` is **left adjoint** to `A ↦ Ay` (discrete category).
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 7.80, p. 263
**Keywords:** Cat♯(C, Ay) ≅ Set(Ob C, A), discrete category right adjoint

### 7.81 Exercise — Continuous arrow fields C ⇸ y^ℝ   [p. 264]
**Statement:** An assignment `c, r ↦ c.r` with `c.0 = id_c` and `(c.r).r' = c.(r+r')`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.81, p. 264 (solution p. 285)
**Keywords:** continuous arrow field, y^ℝ, flow

### 7.82 Example — Systems of ODEs ARE retrofunctors ℝ^n y^{ℝ^n} ⇸ y^T   [p. 264]
**Statement:** A vector field integrated to flows `x ↦ x^{+t}` is a retrofunctor `F : ℝ^n y^{ℝ^n} ⇸ y^T` with `F♯(x, t) = x^{+t} − x`, so `cod F♯(x,t) = x^{+t}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.82, p. 264
**Keywords:** ODE, vector field, integral curve, flow, differentiable dynamical system

### 7.83 Equation — Flow axioms   [p. 264]
**Statement:** `x^{+0} = x` and `x^{+t_1+t_2} = (x^{+t_1})^{+t_2}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.83), p. 264
**Keywords:** flow axioms, group action of time

### 7.84 Example — Retrofunctors Sy^S ⇸ C are C-coalgebras   [p. 265]
**Statement:** By (6.65), lenses `Sy^S → 𝔠` ↔ functions `S → 𝔠(S)`; a retrofunctor is a **C-coalgebra** (Def. 7.96, Prop. 7.98).
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.84, p. 265
**Keywords:** coalgebra, S → 𝔠(S), Sy^S ⇸ C

### 7.85 Example — Retrofunctors Sy^S ⇸ Ty^T ARE VERY WELL-BEHAVED LENSES   [p. 265]
**Statement:** With `get : S → T` (positions) and `put : S × T → S` (directions), the retrofunctor laws are exactly **get-put** `put(s, get(s)) = s` (=7.56), **put-get** `get(put(s,t)) = t` (=7.57), **put-put** `put(put(s,t), t') = put(s, t')` (=7.58). These hold **iff `get` is a product projection**: `S ≅ T × U` with `get = π_1`. Corollary: if `|T| ∤ |S|` (finite) there are **no** such retrofunctors.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.85, pp. 265–267
**Keywords:** very well-behaved lens, get-put, put-get, put-put, lens laws, S ≅ T × U, product projection
**Attribution:** "what are known in the **functional programming community** as very well-behaved lenses"; §7.4 cites **[nLa22]**. No individual named.

### 7.86 Exercise — Converse: S ≅ T × U gives a UNIQUE retrofunctor   [p. 267]
**Statement:** `put((t,u), t') = (t', u)` is forced.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.86, p. 267 (solution p. 285)
**Keywords:** converse of 7.85, unique lens from a product decomposition

### 7.87 Exercise — Counting retrofunctors between state categories   [p. 267]
**Statement:** `|S| = 3`: 6 retrofunctors `Sy^S ⇸ Sy^S`. `|S| = 4, |T| = 2`: 6.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.87, p. 267 (solution p. 285)
**Keywords:** counting very well-behaved lenses, product projections

### 7.88 Example — The canonical retrofunctor 𝔠(1)y^{𝔠(1)} ⇸ C   [p. 267]
**Statement:** On positions `i ↦ i`; on directions each `f : i → _` ↦ **`cod f`**. This is a retrofunctor.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.88, p. 267
**Keywords:** contractible groupoid on Ob C, canonical coalgebra, cod on directions

### 7.89 Exercise — Is 𝔠[i]y^{𝔠[i]} → 𝔠 (post-composition) a retrofunctor? (YES)   [p. 268]
**Statement:** On positions `f ↦ cod f`; on directions `g ↦ f # g`. Yes.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.89, p. 268 (solution p. 285)
**Keywords:** 𝔠[i]y^{𝔠[i]} ⇸ C, post-composition, representable copresheaf

### 7.90 Example — OBJECTS ARE NOT REPRESENTABLE in Cat♯   [p. 268]
**Statement:** Unlike `Cat` (where `Ob C ≅ Cat(T, C)`), there is **no** fixed `U` with `Cat♯(U, C) ≅ Ob C` naturally. Retrofunctors `T ⇸ C` correspond only to objects `c` such that **every** morphism out of `c` has codomain `c`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.90, p. 268
**Keywords:** objects not representable in Cat♯, fixed-point objects

### 7.91 Exercise — Proof that objects are not representable   [p. 269]
**Statement:** `Cat♯(U, 2y) ≅ 2^{Ob U}` forces `|Ob U| = 1`; the walking arrow then gives a contradiction. Also **no `V` with `Cat♯(E, V) ≅ Ob E`** (the empty category has one retrofunctor out but no objects).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.91, p. 269 (solution p. 285)
**Keywords:** Cat♯(U,2y) ≅ 2^{Ob U}, no representing object

### 7.92 Example — Retrofunctors into ℝy^ℝ (graded categories)   [p. 269]
**Statement:** `|·| : C ⇸ ℝy^ℝ` assigns each object `|c| ∈ ℝ` and each `r` a morphism `c → c^r` with **`|c| + r = |c^r|`**, `c^0 = c`, `(c^r)^s = c^{r+s}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 7.92, p. 269
**Keywords:** ℝy^ℝ, real-valued grading, |c| + r = |c^r|

### 7.93 Exercise — Count retrofunctors A ⇸ PA (=2)   [p. 269]
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.93, p. 269 (solution p. 286)
**Keywords:** walking parallel arrows, count = 2

### 7.94 Exercise — The "new identity" MONAD 𝔠 ↦ 𝔠y on Cat♯   [p. 269]
**Statement:** `𝔠y` is the carrier of `C` with a **new arrow `i_c : c → c` at each object, which becomes the identity** (the old identity is no longer one). The construction is functorial and is a **monad** on `Cat♯` (unit `𝔠 → 𝔠y`, multiplication `𝔠yy → 𝔠y`).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.94, p. 269 (solution p. 286)
**Keywords:** 𝔠y, adjoin a new identity, monad on Cat♯

### 7.95 Exercise — Retrofunctor 2-out-of-3 FAILS both ways   [p. 270]
**Statement:** If `f` and `f#g` are retrofunctors, `g` need not be (take `𝔠 = 0`); if `g` and `f#g` are, `f` need not be (take `𝔢 = y`; `f` need only be **copointed**).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.95, p. 270 (solution p. 286)
**Keywords:** two-out-of-three fails, copointed lens

### 7.96 Definition — Coalgebra for a polynomial comonoid   [p. 270]
**Statement:** A **C-coalgebra** `(S, α)` is a set `S` with `α : S → 𝔠 ◁ S` such that **(7.97)** `α # (ε ◁ S) = id_S` and `α # (δ ◁ S) = α # (𝔠 ◁ α)`. Morphisms `h : S → T` satisfy `α # (𝔠 ◁ h) = h # β`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 7.96, p. 270
**Keywords:** C-coalgebra, α : S → 𝔠 ◁ S, coalgebra laws, comonad coalgebra

### 7.97 Equation — The coalgebra laws   [p. 270]
**Statement:** `α # (ε ◁ S) = id_S`; `α # (δ ◁ S) = α # (𝔠 ◁ α)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.97), p. 270
**Keywords:** coalgebra counit law, coalgebra coassociativity

### 7.98 Proposition — Retrofunctors Sy^S ⇸ C ARE C-coalgebras on S   [p. 271]
**Statement:** "Retrofunctors `Sy^S ⇸ C` can be identified (up to isomorphism) with **C-coalgebras carried by `S`**." Proof via (6.65) and polyboxes: (7.53) ⟺ the counit law, (7.54) ⟺ coassociativity.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 7.98, p. 271
**Keywords:** Sy^S ⇸ C ≅ C-coalgebra, comonad coalgebra

### 7.99 Definition — Discrete opfibration   [p. 273]
**Statement:** `π : S → C` is a **discrete opfibration** if for every `s ∈ S` and every `f : π(s) → c'` there is a **unique** `s'` and `f̄ : s → s'` with `π(f̄) = f`. `dopf(C)` := the category of these (morphisms = functors over `C`, triangle (7.100)).
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 7.99, p. 273
**Keywords:** discrete opfibration, unique lift, dopf(C)

### 7.100 Equation — Triangle for morphisms of discrete opfibrations   [p. 273]
**Statement:** `F # π' = π`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (7.100), p. 273
**Keywords:** dopf morphism triangle

### 7.101 Exercise — A morphism of discrete opfibrations is one   [p. 273]
**Statement:** **Citable criterion (solution, p. 286):** `F : C → D` is a discrete opfibration **iff** for every `c`, the induced `F[c] : C[c] → D[Fc]` is a **bijection**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.101, p. 273 (solution p. 286)
**Keywords:** discrete opfibration iff C[c] → D[Fc] bijection, cartesian lens

### 7.102 Exercise — Lifts preserve identities/composites; π as a retrofunctor   [p. 273]
**Statement:** `id̄_{π(i)} = id_i`; `f̄ # ḡ = ‾(f#g)`. Hence `π` becomes a retrofunctor with `π♯_s(f) := f̄` (the lift).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.102, p. 273 (solution p. 286)
**Keywords:** π♯_s(f) = f̄, dopf ⟹ retrofunctor

### 7.103 Proposition — C-coalgebras ≅ dopf(C)   [p. 273]
**Statement:** "The category of C-coalgebras is **isomorphic** to the category `dopf(C)` of discrete opfibrations over `C`."
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 7.103, p. 273
**Keywords:** C-coalgebra ≅ discrete opfibration

### 7.104 Definition — Category of elements ∫^C I   [p. 274]
**Statement:** For `I : C → Set`, `Ob ∫^C I := {(c, x) | c ∈ C, x ∈ Ic}`, with a morphism `f : (c,x) → (c',x')` for each `f : c → c'` satisfying **`(I f)(x) = x'`**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 7.104, p. 274
**Keywords:** category of elements, ∫^C I, Grothendieck construction, copresheaf
**Attribution:** copresheaves as categorical databases — **Spivak [Spi12]** (p. 274).

### 7.105 Exercise — π : ∫^C I → C is a discrete opfibration   [p. 274]
**Statement:** The unique lift of `f : c → c'` at `(c,x)` is `f̄ := f` with target `(c', I(f)(x))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.105, p. 274 (solution p. 286)
**Keywords:** projection from category of elements, x' = I(f)(x)
**NB:** In `pdftotext` output the word "Exercise" is overlapped by the `∫` glyph. It IS an Exercise.

### 7.106 Exercise — ∫^C is a functor Set^C → dopf(C)   [p. 274]
**Statement:** For `α : I → J`, `∫^C α` sends `(c,x) ↦ (c, α_c x)` and `f ↦ f`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.106, p. 274 (solution pp. 286–287)
**Keywords:** ∫^C : Set^C → dopf(C), functoriality of Grothendieck construction

### 7.107 Exercise — ∫ of a copresheaf on a FREE category is free   [p. 274]
**Statement:** For a graph `G` with free category `𝒢` and `S : 𝒢 → Set`, `∫^𝒢 S` is free on the graph with vertices `Σ_{v∈V} S(v)` and arrows `Σ_{a∈A} S(src a)`, where `(a, s) : (v, s) → (v', S(a)(s))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.107, p. 274 (solution p. 287)
**Keywords:** free category, ∫^𝒢 S free, Σ_{a∈A} S(src a) ⇉ Σ_{v∈V} S(v)

### 7.108 Proposition — Set^C ≃ dopf(C)   [p. 275]
**Statement:** `Set^C` is **equivalent** to `dopf(C)`. Inverse: `(∂π)(c) := π^{-1}(c)` and `(∂π)(f)(s) := cod f̄`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 7.108, p. 275
**Keywords:** Set^C ≃ dopf(C), (∂π)(c) = π^{-1}(c), Grothendieck equivalence

### 7.109 Proposition — Discrete opfibrations = dynamical systems on C   [p. 275]
**Statement:** "Up to isomorphism, discrete opfibrations into `C` can be identified with **dynamical systems on `C`**." (Caveat printed: "this association is only functorial on the groupoid of objects and isomorphisms.") Proof uses the **vertical–cartesian factorization** `Sy → 𝔰 --ψ--> 𝔠`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 7.109, p. 275
**Keywords:** dynamical system on C, vertical-cartesian factorization, lift as on-directions

### 7.110 Exercise — Complete the proof of Prop. 7.109   [p. 275]
**Statement:** Give the comonoid structure on `𝔰` making `ψ : 𝔰 → 𝔠` a retrofunctor, and show the two directions are mutually inverse. *(No solution printed in §7.5.)*
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 7.110, p. 275
**Keywords:** vertical/cartesian factorization, comonoid structure on 𝔰

## §7.3.3 summary box (p. 276) — the FOUR-fold equivalence

For a fixed category `C` with carrier `𝔠`, the following are the same data:
(1) retrofunctors `F : Sy^S ⇸ C`; (2) `C`-coalgebras `(S, α)`, `α : S → 𝔠 ◁ S`; (3) discrete opfibrations `π : S → C` with `Ob S = S`; (4) copresheaves `I : C → Set` with `Ob ∫^C I = S`. Moreover (2), (3), (4) form **equivalent categories**. *(Extended to EIGHT in Theorem 8.102.)*

---
---

# CHAPTER 8 — Categorical properties of polynomial comonoids (pp. 289–348)

*Chapter theme: the COFREE comonoid (`U ⊣ T_−`), more properties of `Cat♯`, and comodules/bicomodules (Garner).*

## §8.1 Cofree comonoids (pp. 289–320)

### 8.1 Equation — The defining LIMIT TOWER for the cofree carrier   [p. 290]
**Statement:** `𝔱_p := U T_p` is the limit in Poly of the diagram with top row `y, p, p^{◁2}, p^{◁3}, …`, vertical lenses `! , p◁!, p^{◁2}◁!, …` into the bottom row `1 ← p◁1 ← p^{◁2}◁1 ← p^{◁3}◁1 ← ⋯`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.1), p. 290
**Keywords:** cofree comonoid carrier, limit diagram, 𝔱_p, tower of truncations

### 8.2 Definition — TREE on a polynomial (p-tree)   [p. 290]
**Statement:** A **p-tree** is a rooted tree whose every vertex `v` is assigned a `p`-position `i` and a **bijection from the children of `v` to `p[i]`**. The set of p-trees is `tree_p`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 8.2, p. 290
**Keywords:** p-tree, tree_p, corolla, rooted tree

### 8.3 Example — Example p-pretrees   [p. 291]
**Statement:** For `p := {red,blue}y² + {green}y + {yellow}`, four partially-built trees; only the lone yellow dot is an actual element of `tree_p`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.3, p. 291
**Keywords:** pretree example, unfilled leaves

### 8.4 Equation — The four drawn partial p-trees   [p. 291]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.4), p. 291
**Keywords:** displayed p-trees

### 8.5 Exercise — Finite trees on q = y² + 3y   [p. 292]
**Statement:** Every `q`-position has a nonempty direction-set, so no branch terminates: there are no finite `q`-trees and every vertex has infinitely many descendants.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.5, p. 292 (solution p. 339)
**Keywords:** finite q-trees, no empty direction set

### 8.6 Definition — Stage-n pretree; height-n leaves   [p. 292]
**Statement:** A **stage-n pretree** is an element of `p^{◁n}(1)`. The **height-n leaves** of `i ∈ p^{◁n}(1)` is the set `p^{◁n}[i]`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 8.6, p. 292
**Keywords:** stage-n pretree, p^{◁n}(1), height-n leaves

### 8.7 Remark — "stage" not "height"; unique stage-0 pretree   [p. 292]
**Statement:** A `p^{◁n}`-pretree need not reach height `n` (branches may terminate early). There is exactly one stage-0 pretree since `p^{◁0}(1) = y(1) = 1`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Remark 8.7, p. 292
**Keywords:** stage vs height, p^{◁0}(1) = 1

### 8.8 Example — Trimming pretrees   [p. 292]
**Statement:** `p^{◁n}(!) : p^{◁(n+1)}(1) → p^{◁n}(1)` sends each stage-(n+1) pretree to its stage-n pretree (trims one level).
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.8, p. 292
**Keywords:** trimming function, p^{◁n}(!)

### 8.9 Equation — The trimming chain   [p. 293]
**Statement:** `p^{◁n}(1) ← p^{◁(n+1)}(1) ← ⋯ ← p^{◁(n+k)}(1)`, the composite trimming off the top `k` levels.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.9), p. 293
**Keywords:** composite trimming, inverse system

### 8.10 Example — More actual p-trees; uncountability   [p. 293]
**Statement:** There are **uncountably many** trees in `tree_p` (already `tree_{2y} ≅ 2^ℕ`), so most p-trees are not describable in a finite language.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.10, p. 293
**Keywords:** uncountably many trees, tree_{2y} = 2^ℕ

### 8.11 Exercise — Characterize tree_p for basic p   [p. 294]
**Statement:** `tree_1 ≅ 1`; `tree_2 ≅ 2`; `tree_y ≅ 1` (the unique infinite ray); `tree_{y²} ≅ 1` (the infinite binary tree); `tree_{2y} ≅ 2^ℕ`; `tree_{y+1} ≅ ℕ ∪ {∞}`; **`tree_{B y^A} ≅ B^{List(A)}`** where `List(A) = Σ_{n∈ℕ} A^n`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.11, p. 294 (solution pp. 339–340)
**Keywords:** tree_{By^A} = B^{List(A)}, List(A)

### 8.12 Exercise — n-ary trees and L-labeled n-ary trees   [p. 294]
**Statement:** `tree_{y^n}` = n-ary trees; `tree_{L y^n}` = L-labeled n-ary trees.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.12, p. 294 (solution p. 340)
**Keywords:** n-ary trees, y^n, L y^n

### 8.13 Equation — The cone tree_p over the pretree tower   [p. 295]
**Statement:** Projections `π^{(n)} : tree_p → p^{◁n}(1)` (remove all vertices of height > n) satisfy `π^{(n+1)} # p^{◁n}(!) = π^{(n)}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.13), p. 295
**Keywords:** π^{(n)}, cone

### 8.14 Exercise — tree_p IS the limit of the pretree tower   [p. 295]
**Statement:** `tree_p ≅ lim( 1 ← p(1) ← p(p(1)) ← ⋯ )`. Unfolds to iterated dependent choices `i_1 ∈ p(1)`, `i_2 ∈ Π_{d_1∈p[i_1]} p(1)`, etc.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.14, p. 295 (solution pp. 339–340)
**Keywords:** limit of pretrees, inverse limit, tree_p = lim p^{◁n}(1)

### 8.15 Equation — The pretree tower in Set   [p. 295]
**Statement:** `1 ← p(1) ← p^{◁2}(1) ← p^{◁3}(1) ← ⋯` — its limit is `tree_p = 𝔱_p(1)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.15), p. 295
**Keywords:** pretree tower, ω^op limit

### 8.16 Exercise — tree_p is the TERMINAL p-COALGEBRA   [p. 295]
**Statement:** The map `tree_p → p(tree_p)` (root label + subtree along each branch) is the **terminal coalgebra** for the functor `p`, and it is a **bijection** (Lambek). Text (p. 295): "it is the terminal coalgebra for the functor `p`."
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.16, p. 295 (solution p. 340)
**Keywords:** terminal coalgebra, final coalgebra, tree_p ≅ p(tree_p), Lambek
**Attribution:** **NONE.** The book gives the classical Adámek/Barr terminal-sequence result as an exercise, uncredited.

### 8.17 Exercise — Characterize the polynomial 𝔱_p   [p. 297]
**Statement:** `𝔱_1 ≅ y`; `𝔱_2 ≅ 2y`; `𝔱_y ≅ y^ℕ`; `𝔱_{y²} ≅ y^{List(2)}`; `𝔱_{2y} ≅ 2^ℕ·y^ℕ`; `𝔱_{y+1} ≅ {∞}·y^ℕ + Σ_{n∈ℕ} y^{n+1}`; **`𝔱_{B y^A} ≅ B^{List(A)} · y^{List(A)}`**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.17, p. 297 (solution pp. 340–341)
**Keywords:** 𝔱_y = y^ℕ, 𝔱_{By^A} = B^{List(A)} y^{List(A)}, directions as rooted paths

### 8.18 Proposition — THE COFREE CARRIER: 𝔱_p = Σ_{T ∈ tree_p} y^{vtx(T)}   [p. 297]
**Statement:** VERBATIM: "let **`𝔱_p ≔ Σ_{T ∈ tree_p} y^{vtx(T)}`** be the polynomial whose **positions are p-trees** and whose **directions at each p-tree are the rooted paths**. Then `𝔱_p` is the limit of the diagram (8.1), with projections `ε_p^{(n)} : 𝔱_p → p^{◁n}`…" Directions: `𝔱_p[T] = vtx(T) = Σ_{n∈ℕ} p^{◁n}[π^{(n)}T]` — **ALL finite rooted paths ≅ all vertices**, NOT root-to-leaf paths. (An infinite "path" is called a **ray**.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.18, p. 297
**Keywords:** cofree comonoid carrier, Σ_{T∈tree_p} y^{vtx(T)}, vtx(T), rooted paths, ε_p^{(n)}, C^∞, M-tree ◁ paths
**Attribution:** **NONE.**

### 8.19 Equation — The universal cone with the ε_p^{(n)}   [p. 297]
**Statement:** `ε_p^{(0)} = ε_p : 𝔱_p → y`, `ε_p^{(1)} : 𝔱_p → p`, `ε_p^{(2)} : 𝔱_p → p^{◁2}`, … forming a cone over (8.1).
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.19), p. 297
**Keywords:** universal cone, projections from 𝔱_p

### 8.20 Example — Drawing ε_p^{(n)} in polyboxes   [p. 297]
**Statement:** Polybox depictions of `ε_p^{(n)}` (positions `T ↦ π^{(n)}T`; directions: height-n leaf ↦ corresponding vertex), including decompositions `p^{◁ℓ} ◁ p^{◁m}` (`n = ℓ+m`). Introduces `T(u)` = the p-subtree of `T` rooted at `u`, and `u ⇝ w` = **path concatenation** (associative).
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.20, pp. 297–301
**Keywords:** polyboxes, T(u), u ⇝ w, subtree, path concatenation

### 8.21 Equation — Polybox for ε_p^{(n)}   [p. 298]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.21), p. 298
**Keywords:** polybox ε^{(n)}, vtx_n

### 8.22 Equation — ε_p^{(4)} unpacked into four copies of p   [p. 298]
**Statement:** Position `i_0` = root label; `a_1 ∈ p[i_0]`; …; the returned `𝔱_p`-direction is the rooted path `a_1 ⇝ a_2 ⇝ a_3 ⇝ a_4`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.22), p. 298
**Keywords:** nested polyboxes, rooted path a_1⇝a_2⇝a_3⇝a_4

### 8.23 Equation — ε_p^{(4)} with codomain as p^{◁2} ◁ p^{◁2} (empty boxes)   [p. 299]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.23), p. 299
**Keywords:** p^{◁4} ≅ p^{◁2} ◁ p^{◁2}

### 8.24 Equation — The same boxes, lower half filled   [p. 299]
**Statement:** Lower `𝔱_p`-position `T`; `p^{◁2}`-position `π^{(2)}T`; direction `u` = the height-2 vertex at the end of `(a_1, a_2)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.24), p. 299
**Keywords:** π^{(2)}T, height-2 vertex

### 8.25 Equation — Full p^{◁2} ◁ p^{◁2} polyboxes with T(u) and u ⇝ w   [p. 300]
**Statement:** Upper position `π^{(2)}T(u)`; the composite direction returned is `u ⇝ w` = the **concatenation** of `u = (a_1,a_2)` and `w = (a_3,a_4)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.25), p. 300
**Keywords:** T(u), u ⇝ w, concatenation, subtree rooted at u

### 8.26 Equation — 𝔱_p ◁ 𝔱_p as a limit (left expansion)   [p. 303]
**Statement:** Apply `− ◁ 𝔱_p` to (8.1), using `◁` preserves all limits on the left (Prop. 6.68) and connected limits on the right (Thm. 6.80).
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.26), p. 303
**Keywords:** 𝔱_p ◁ 𝔱_p limit, Prop 6.68, Thm 6.80

### 8.27 Equation — Expansion of p^{◁ℓ} ◁ 𝔱_p   [p. 303]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.27), p. 303
**Keywords:** p^{◁ℓ} ◁ 𝔱_p, right expansion

### 8.28 Equation — The grid diagram whose limit is 𝔱_p ◁ 𝔱_p   [p. 304]
**Statement:** One copy of `p^{◁ℓ} ◁ p^{◁m}` and of `p^{◁ℓ} ◁ p^{◁m} ◁ 1` for every `ℓ, m ∈ ℕ`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.28), p. 304
**Keywords:** grid diagram, limit is 𝔱_p ◁ 𝔱_p

### 8.29 Equation — Vertical-into-1 arrows of (8.28)   [p. 304]
**Statement:** `p^{◁ℓ} ◁ p^{◁m} → p^{◁ℓ} ◁ p^{◁m} ◁ 1`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.29), p. 304

### 8.30 Equation — Column-trimming arrows of (8.28)   [p. 304]
**Statement:** `p^{◁ℓ} ◁ p^{◁(m+1)} ◁ 1 → p^{◁ℓ} ◁ p^{◁m} ◁ 1`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.30), p. 304

### 8.31 Equation — Bottom-row arrows of (8.28)   [p. 304]
**Statement:** `p^{◁(ℓ+1)} ◁ 1 → p^{◁ℓ} ◁ 1`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.31), p. 304

### 8.32 Equation — THE DUPLICATOR δ_p, defined by a universal property   [p. 305]
**Statement:** `δ_p : 𝔱_p → 𝔱_p ◁ 𝔱_p` is the **unique** lens with **`δ_p # (ε_p^{(ℓ)} ◁ ε_p^{(m)}) = ε_p^{(ℓ+m)}`** for all `ℓ, m ∈ ℕ`. In elements this forces `cod v := T(v)` (the subtree rooted at `v`) and `v # w := v ⇝ w` (path concatenation).
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.32), p. 305
**Keywords:** duplicator, δ_p, ε^{(ℓ)} ◁ ε^{(m)} = ε^{(ℓ+m)}, cod v = T(v), v # w = concat

### 8.33 Proposition — THE COFREE COMONOID IS THE CATEGORY OF p-TREES   [p. 306]
**Statement:** VERBATIM: "`(𝔱_p, ε_p, δ_p)` is a polynomial comonoid corresponding to a category `T_p`: • An **object** in `T_p` is a p-tree `T ∈ tree_p`. • A **morphism** emanating from `T` is a **rooted path** in `T`; its **codomain is the p-subtree rooted at the end of the path**. • The **identity** on `T` is its **empty rooted path**. • **Composition** is given by **concatenating rooted paths**."
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.33, p. 306
**Keywords:** category of p-trees, objects = trees, morphisms = rooted paths, codomain = subtree, identity = empty path, composition = concatenation, C^∞, o = root, ↓ = subtree, ⊕ = concat
**Attribution:** **NONE.**

### 8.34 Example — Why the limit: free refinement of states   [p. 308]
**Statement:** `p^{◁2}`-pretrees = all ways of assigning codomains to `p`'s directions; iterating forever, `𝔱_p` is the "ultimate free refinement": p-trees are states, rooted paths are freely-generated composable transitions.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.34, pp. 308–309
**Keywords:** free refinement of states, intuition for (8.1)

### 8.35 Example — The category of 1-trees   [p. 310]
**Statement:** `𝔱_1 ≅ y`; `T_1` = the terminal category.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.35, p. 310
**Keywords:** 𝔱_1 = y, terminal category

### 8.36 Exercise — The category of trees on a constant B   [p. 310]
**Statement:** `𝔱_B ≅ B·y`; `T_B` = the **discrete category on B**. (Cross-check: `List(0) ≅ 1`.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.36, p. 310 (solution p. 341)
**Keywords:** 𝔱_B = By, discrete category

### 8.37 Example — The category of y-trees IS the monoid (ℕ, 0, +)   [p. 310]
**Statement:** There is a unique `y`-tree (a single ray), so `𝔱_y ≅ y^ℕ`; morphisms = rooted paths ≅ `ℕ`; `id = 0`, `m # n = m + n`. So `T_y` = the monoid `(ℕ, 0, +)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.37, p. 310
**Keywords:** 𝔱_y = y^ℕ, T_y = (ℕ,0,+)

### 8.38 Example — By-trees are B-STREAMS   [p. 311]
**Statement:** `𝔱_{By} ≅ B^ℕ y^ℕ`; `T_{By}` = the category of B-streams (Example 7.45): objects `B^ℕ`, morphisms `ℕ`, `cod(b, n) = (b_n → b_{n+1} → ⋯)`, composition = addition.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.38, p. 311
**Keywords:** 𝔱_{By} = B^ℕ y^ℕ, B-streams, substream

### 8.39 Example — The category of ℕ-labeled binary trees   [p. 312]
**Statement:** For `p := ℕy²`: `𝔱_{ℕy²} ≅ ℕ^{List(2)} y^{List(2)}`; objects = ℕ-labeled infinite binary trees; morphisms = binary sequences (rooted paths); composition = concatenation.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.39, p. 312
**Keywords:** ℕ-labeled binary trees, ℕ^{List(2)}, List(2)

### 8.40 Exercise — The category of B-labeled A-ary trees   [p. 313]
**Statement:** `𝔱_{By^A} ≅ B^{List(A)} y^{List(A)}`: objects = B-labeled A-ary trees ≅ `B^{List(A)}`; morphisms out of an object = `List(A)`; codomain = the subtree at the path's end; identity = the empty path; **composition = concatenation of lists in A**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.40, p. 313 (solution p. 341)
**Keywords:** T_{By^A}, B^{List(A)} y^{List(A)}, concatenation

### 8.41 Exercise — The (y+1)-tree category   [p. 313]
**Statement:** Objects `ℕ ∪ {∞}` (rays that either terminate or run forever); morphisms out of `[n]` ≅ `{0,…,n}`; from `[∞]` ≅ `ℕ`, all with codomain `[∞]`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.41, p. 313 (solution p. 341)
**Keywords:** T_{y+1}, halting ray, ℕ ∪ {∞}

### 8.42 Exercise — The alphabet polynomial   [p. 313]
**Statement:** For `p := {a,…,z,␣}y + {•}`, objects of `T_p` = finite-or-infinite words over the 27-letter alphabet.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.42, p. 313 (solution p. 342)
**Keywords:** alphabet polynomial, words, halting

### 8.43 Exercise — Hands-on composition in T_p   [p. 313]
**Statement:** Identity = root; codomain = subtree; composite = concatenation — worked by hand.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.43, p. 313 (solution p. 342)
**Keywords:** identity is root, codomain is subtree, composite is concatenation

### 8.44 Exercise — Are retrofunctors T_p ⇸ y^Q constant?   [p. 313]
**Statement:** With `Q := {q ∈ ℚ | q ≥ 0}`: is every retrofunctor `T_p ⇸ y^Q` constant (factoring through `y`)? Solution (p. 342) exhibits a witness stream where every morphism from a given object has a different codomain.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.44, p. 313 (solution p. 342)
**Keywords:** retrofunctor to y^Q, arrow field, divisibility

### 8.45 Theorem — COFREE COMONOID (the forgetful–cofree adjunction)   [p. 314]
**Statement:** VERBATIM: "The forgetful functor **`U : Cat♯ → Poly` has a right adjoint `T_− : Poly → Cat♯`**, giving rise to an adjunction `Cat♯ ⇄ Poly`, such that for each `p ∈ Poly` the carrier `𝔱_p := U T_p` of the category `T_p` is given by the limit of the diagram (8.1)… That is, for any `C ∈ Cat♯` with carrier `𝔠 := U C`, there is a natural isomorphism **`Poly(𝔠, p) ≅ Cat♯(C, T_p)`**." Counit `ε_p^{(1)} : 𝔱_p → p`. The mate `F` has components `F # ε_p^{(n)} = δ^{(n+1)} # (ε ◁ φ^{◁n})`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Theorem 8.45, p. 314
**Keywords:** cofree comonoid, forgetful-cofree adjunction, U ⊣ T_−, Poly(𝔠,p) ≅ Cat♯(C,T_p), counit, cofree comonad
**Attribution:** **NONE.**
**Source-quality flag:** the **uniqueness half of the proof is truncated** in the source (ends with a literal `**` and a stray QED box).

### 8.46 Equation — The universal (counit) triangle   [p. 314]
**Statement:** For every lens `φ : 𝔠 → p` there is a **unique** retrofunctor `F : C ⇸ T_p` with `U F # ε_p^{(1)} = φ`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.46), p. 314
**Keywords:** universal property, counit triangle, mate

### 8.47 Equation — The base case of the induction   [p. 314]
**Statement:** `δ # (ε ◁ φ) = δ # (ε ◁ 𝔠) # φ = φ` (left erasure law).
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.47), p. 314
**Keywords:** left erasure law, base case

### 8.48 Equation — The cone from 𝔠 over the tower   [p. 315]
**Statement:** The induced `F : 𝔠 → 𝔱_p` satisfies `F # ε_p^{(n)} = δ^{(n+1)} # (ε ◁ φ^{◁n})`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.48), p. 315
**Keywords:** induction diagram, δ^{(n+1)}, ε ◁ φ^{◁n}

### 8.49 Proposition — THE MATE COMPUTES Run_n   [p. 316]
**Statement:** For `φ : 𝔠 → p` with mate `f = U F : 𝔠 → 𝔱_p`: **`f # ε_p^{(n)} = δ^{(n)} # φ^{◁n} = Run_n(φ)`** for all `n ∈ ℕ`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.49, p. 316
**Keywords:** Run_n(φ), f # ε^{(n)} = δ^{(n)} # φ^{◁n}, mate captures all runs

### 8.50 Example — A halting automaton as a retrofunctor into T_p   [p. 316]
**Statement:** For `φ : Sy^S → y^A + 1`, the tree `F(s_0)` encodes the **accepted language** in its **maximal** rooted paths.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.50, pp. 316–317
**Keywords:** halting automaton, y^A + 1, maximal rooted paths, accepted words

### 8.51 Example — Languages recognized by DFAs   [p. 317]
**Statement:** A DFA is `y → Sy^S` plus `φ : Sy^S → 2y^A`; its mate is `F : Sy^S ⇸ T_{2y^A}`, and `F(s_0) ∈ tree_{2y^A} ≅ 2^{List(A)}` is **exactly the set of accepted words**. `F♯_{s_0}` sends each word to the state reached.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.51, p. 317
**Keywords:** DFA, 2^{List(A)}, accepted language as a tree

### 8.52 Example — Moore machines: direction sequences ↦ position sequences   [p. 317]
**Statement:** For `φ : Sy^S → By^A`, the mate gives `F(s_0) ∈ B^{List(A)}`, a decision tree, and the output sequence is given **non-recursively** by **`b_i := F(s_0)(a_1, …, a_i)`**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.52, pp. 317–318
**Keywords:** Moore machine, b_i = F(s_0)(a_1..a_i), non-recursive, decision tree

### 8.53 Example — The mate as a copresheaf / database schema on T_p   [p. 318]
**Statement:** Since `T_p` is free on a graph (Prop. 8.57), the schema has one table per p-tree, one column per arrow out of the root.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.53, p. 318
**Keywords:** copresheaf on T_p, database schema, free on a graph

### 8.54 Equation — The automaton picture   [p. 318]
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.54), p. 318
**Keywords:** automaton diagram

### 8.55 Exercise — Compute T_φ on a tree   [p. 319]
**Statement:** The recursive rule: if the root of `t` is `i`, the root of `T_φ(t)` is `j := φ_1(i)`, and to each branch `b ∈ q[j]` we assign the tree situated at `φ♯_i(b)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.55, p. 319 (solution p. 343)
**Keywords:** T_φ on objects, root j = φ_1(i), branch b ↦ φ♯_i(b)

### 8.56 Exercise — The induced retrofunctor T_p ⇸ T_{p^{◁n}}   [p. 319]
**Statement:** Exists (via the cofree adjunction, from the lens `δ^{(n)} # r^{◁n} : 𝔱_p → p^{◁n}`); is **bijective on objects** but **NOT an isomorphism for `n ≥ 2`** — rooted paths in `tree_{p^{◁n}}` correspond only to paths in `tree_p` of length a **multiple of n**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.56, p. 319 (solution p. 343)
**Keywords:** T_p ⇸ T_{p^{◁n}}, bijective on objects not iso, height-n compression

### 8.57 Proposition — EVERY COFREE CATEGORY IS FREE ON A GRAPH   [p. 319]
**Statement:** For every `p`, `T_p` is **free on a graph** `G_p`: vertices `V_p := tree_p`; arrows `A_p := Σ_{t ∈ tree_p} p[π_1(t)]` (directions of `p` out of each tree's root corolla); source `(t,d) ↦ t`, target `(t,d) ↦ cod(π♯_t(d))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.57, p. 319
**Keywords:** free on a graph, G_p, path category, cofree category

### 8.58 Corollary — Every morphism in T_p is MONIC and EPIC   [p. 319]
**Statement:** Follows from Prop. 8.57 (free categories on graphs have this property).
**Cite as:** Niu–Spivak arXiv:2312.00990, Corollary 8.58, p. 319
**Keywords:** monic, epic, free category on a graph
**Source-quality flag:** the statement writes `C_p` where it means `T_p`.

### 8.59 Proposition — y^ℕ is a ×-MONOID in Cat♯   [p. 320]
**Statement:** The additive monoid `y^ℕ` has a **`×`-monoid structure in `Cat♯`**. Proof: `T_−` (right adjoint) preserves products, so `y^{List(n)} ≅ T_{y^n}` is the n-fold product of `y^ℕ` in `Cat♯`; `e : y → y^ℕ` = mate of `id_y`; `m : y^{List(2)} → y^ℕ` = mate of the lens given by the list `[1,2]`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.59, p. 320
**Keywords:** y^ℕ monoid object, Cat♯ product, T_{y^n} = y^{List(n)}, ×-monoid

### 8.60 Corollary — Arrow fields form a monoid, functorially   [p. 320]
**Statement:** `Cat♯(C, y^ℕ)` (the arrow fields / **policies** on `C`) is a monoid, and `Cat♯(−, y^ℕ) : Cat♯ → Mon^op` is a functor. Notation `C ↦ C⃗`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Corollary 8.60, p. 320
**Keywords:** arrow field, policy, Cat♯(C, y^ℕ), Mon^op

### 8.61 Theorem — The ARROW-FIELDS functor is right adjoint to Mon^op ↪ Cat♯   [p. 320]
**Statement:** "The arrow fields functor **`Cat♯ → Mon^op`** is **right adjoint** to the inclusion `Mon^op → Cat♯`" (Prop. 7.79). Proof: a retrofunctor `F : C ⇸ y^M` is exactly a monoid morphism `M → C⃗`, via `F♯_c(m # m') = F♯_c(m) # F♯_{c'}(m')`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Theorem 8.61, p. 320
**Keywords:** arrow fields functor, right adjoint, Mon^op → Cat♯, y^M

## §8.2 More categorical properties of Cat♯ (pp. 321–327)

### 8.62 Proposition — Commuting square of left adjoints   [p. 321]
**Statement:** `U ∘ y^{(−)} = y^{(−)} ∘ U` as left adjoints `Mon^op → Poly` (combining Prop. 5.12, Thm. 8.45, Thm. 8.61).
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.62, p. 321
**Keywords:** commutative square of left adjoints, Mon^op

### 8.63 Proposition — Cat♯_rep ≅ Mon^op   [p. 321]
**Statement:** The full subcategory of comonoids with **representable carrier `y^M`** is isomorphic to `Mon^op`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.63, p. 321
**Keywords:** Cat♯_rep ≅ Mon^op, one-object category, Yoneda fully faithful

### 8.64 Exercise — Cat♯_lin ≅ Set   [p. 322]
**Statement:** The full subcategory of comonoids with **linear carrier `Sy`** is isomorphic to `Set` (discrete categories; retrofunctors `Sy ⇸ Ty` = functions `S → T`).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.64, p. 322 (solution p. 343)
**Keywords:** Cat♯_lin ≅ Set, linear carrier Sy, discrete category

### 8.65 Proposition — Left adjoint to Cat♯_lin ↪ Cat♯ (discrete reflection)   [p. 322]
**Statement:** The inclusion has a **left adjoint** sending `(𝔠, ε, δ)` to the unique comonoid carried by **`(𝔠 ◁ 1)y`**; `Cat♯((𝔠 ◁ 1)y, Ay) ≅ Cat♯(𝔠, Ay)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.65, p. 322
**Keywords:** discrete category left adjoint, (𝔠 ◁ 1)y, object-set reflection

### 8.66 Proposition — VERTICAL–CARTESIAN factorization of retrofunctors   [p. 322]
**Statement:** Every retrofunctor `f : C ⇸ D` factors as `C --vert--> C' --cart--> D`. (**Cartesian** = the underlying lens is cartesian, i.e. `f♯_i : 𝔡[f_1(i)] → 𝔠[i]` is an iso for each `i`.) `C'` has `𝔠'(1) := 𝔠(1)`, `𝔠'[i] := 𝔡[f i]`, composition inherited from `D`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.66, p. 322
**Keywords:** vertical cartesian factorization, cartesian retrofunctor, 𝔠'[i] := 𝔡[f i]

### 8.67 Exercise — Completing the vert–cart factorization   [p. 323]
**Statement:** Show `𝔠'` is a category and both factors are retrofunctors (preserve codomains and composition).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.67, p. 323 (solution p. 343)
**Keywords:** retrofunctor laws, 𝔠' category

### 8.68 Proposition — CARTESIAN RETROFUNCTORS ≅ DISCRETE OPFIBRATIONS   [p. 323]
**Statement:** The wide subcategory of **cartesian retrofunctors** in `Cat♯` is **isomorphic** to the wide subcategory of **discrete opfibrations** in `Cat`. (A functor gives `f_♯ : C[c] → D[fc]`, a retrofunctor gives `f♯ : D[fc] → C[c]`; retrofunctor cartesian ⟺ `f♯` iso ⟺ functor is a discrete opfibration; pass between them by inverting.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.68, p. 323
**Keywords:** cartesian retrofunctor, discrete opfibration, wide subcategory, invert on morphisms

### 8.69 Proposition — Cat♯_vert ≅ (Cat_boo)^op   [p. 323]
**Statement:** The wide subcategory of **vertical** maps in `Cat♯` is isomorphic to the **opposite** of the wide subcategory of **bijective-on-objects** functors in `Cat`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.69, p. 323
**Keywords:** vertical retrofunctor, bijective-on-objects, Cat_boo, opposite category

### 8.70 Exercise — State category and object-set identification   [p. 323]
**Statement:** Categories `C` equipped with a **vertical** retrofunctor `S ⇸ C` (where `S = Sy^S`) = categories whose object set has been identified with `S`. (There is exactly one such vertical retrofunctor per category with object set `S` — it carries **no additional data**.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.70, p. 323 (solution p. 343)
**Keywords:** state category Sy^S, vertical retrofunctor, contractible groupoid

### 8.71 Exercise — boo functors between • ⇒ • and • → •   [p. 324]
**Statement:** With `𝔠 := y^{{id_1,s,t}} + y^{{id_2}}`, `𝔡 := y^{{id_1,f}} + y^{{id_2}}`: the functor `F : C → D` corresponds to a vertical retrofunctor `𝔡 ⇸ 𝔠` (**note the reversal**).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.71, p. 324 (solution p. 344)
**Keywords:** bijective-on-objects, opposite direction, walking parallel pair

### 8.72 Proposition — T sends cartesian lenses to cartesian retrofunctors   [p. 324]
**Statement:** If `φ : p → q` is cartesian then `T_φ : T_p ⇸ T_q` is cartesian: `(T_φ)♯_t : T_q[T_φ(t)] → T_p[t]` is a **bijection** (a cartesian `φ` preserves branching profiles, and rooted paths are determined by the branching profile).
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.72, p. 324
**Keywords:** cofree comonoid T_p, cartesian lens, branching profile, rooted paths

### 8.73 Proposition (PORST) — `U : Cat♯ → Poly` is COMONADIC   [p. 324]
**Statement:** The forgetful functor `Cat♯ ≅ Comon(Poly) → Poly` is **comonadic** (it has a right adjoint by Thm. 8.45; Beck's monadicity theorem).
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.73, p. 324
**Keywords:** comonadic, Comon(Poly), Beck monadicity
**Attribution:** **Porst** (in the statement name); proof cites **Paré [Par69, pp. 138–9]** and **Porst [Por19, Fact 3.1]**.

### 8.74 Corollary — Cat♯ has all small COLIMITS, created by U   [p. 325]
**Statement:** Colimits in `Cat♯` exist and are **created** by `U : Cat♯ → Poly` (a comonadic functor creates colimits; Poly is cocomplete by Thm. 5.43).
**Cite as:** Niu–Spivak arXiv:2312.00990, Corollary 8.74, p. 325
**Keywords:** colimits in Cat♯, created by forgetful functor
**Attribution:** proof cites **[nLa18]**.

### 8.75 Example — Coproducts in Cat♯ = disjoint unions   [p. 325]
**Statement:** `Σ_{i∈I} C_i` has carrier `Σ_{i∈I} 𝔠_i`; agrees with the coproduct in `Cat`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.75, p. 325
**Keywords:** coproduct in Cat♯, disjoint union of categories

### 8.76 Exercise — 0 is INITIAL in Cat♯   [p. 325]
**Statement:** `0` has a unique comonoid structure (the empty category) and is initial in `Cat♯` (also because `U` is a **left** adjoint and preserves the initial object).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.76, p. 325 (solution p. 344)
**Keywords:** initial object Cat♯, empty category

### 8.77 Exercise — Comonoid structure on 2𝔠   [p. 325]
**Statement:** `2𝔠 = 𝔠 + 𝔠` carries an induced comonoid structure (the disjoint union of `C` with itself), because `U` preserves colimits.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.77, p. 325 (solution p. 344)
**Keywords:** 2𝔠, induced comonoid

### 8.78 Corollary — Cat♯ has all small LIMITS   [p. 326]
**Statement:** `Cat♯` is complete. (But limits are **strange**: §8.4 notes the product in `Cat♯` of the walking arrow with itself has **infinitely many objects**. Describing them combinatorially is Chapter 9, Question 12 — OPEN.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Corollary 8.78, p. 326
**Keywords:** limits in Cat♯, connected limits, equalizers preserved by ◁
**Attribution:** proof cites **[Por19, Fact 3.4]**.

### 8.79 Proposition — (y, ⊗) is monoidal on Cat♯; ⊗ = PRODUCT in Cat   [p. 326]
**Statement:** The parallel product `(y, ⊗)` extends to `Cat♯`, with `U` **STRONG monoidal**, and the parallel product of two categories is their **product in `Cat`** (not the categorical product in `Cat♯`). `δ_{C⊗D} := (δ_𝔠 ⊗ δ_𝔡) # (duoidal (6.86))`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.79, p. 326
**Keywords:** parallel product comonoid, ⊗ on Cat♯, duoidal, strong monoidal forgetful, product of categories

### 8.80 Exercise — Completing Prop. 8.79   [p. 326]
**Statement:** `⊗ : (Poly, y, ◁)² → (Poly, y, ◁)` is **colax monoidal**, hence sends comonoids to comonoids; `𝔠 ⊗ 𝔡` corresponds to `C × D` in `Cat`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.80, p. 326 (solution p. 344)
**Keywords:** ⊗ colax monoidal for ◁, 𝔠 ⊗ 𝔡 = C × D

### 8.81 Proposition — The COFREE functor T is LAX MONOIDAL for ⊗   [p. 327]
**Statement:** There is a lens `y → 𝔱_y` and, naturally, **`𝔱_p ⊗ 𝔱_q → 𝔱_{p⊗q}`**, satisfying coherence. Proof: `U` is strong monoidal and a left adjoint; by **Kelly's doctrinal adjunction** the right adjoint of an oplax monoidal functor is lax monoidal.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.81, p. 327
**Keywords:** cofree lax monoidal, 𝔱_p ⊗ 𝔱_q → 𝔱_{p⊗q}, doctrinal adjunction
**Attribution:** **Kelly [Kel74]**.

### 8.82 Exercise — Computing 𝔱_y and the lax structure maps   [p. 327]
**Statement:** `𝔱_y ≅ y^ℕ`; `y → 𝔱_y` is the unique lens; the `(p⊗q)`-tree built from a p-tree and a q-tree has root the **pair** of root labels and children indexed by **pairs** of children.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.82, p. 327 (solution p. 344)
**Keywords:** 𝔱_y = y^ℕ, (p ⊗ q)-tree

## §8.3 Comodules over polynomial comonoids (pp. 327–338)

### 8.83 Definition — LEFT COMODULE   [p. 327]
**Statement:** For a comonoid `C = (𝔠, ε, δ)`, a **left C-comodule** is a carrier `m` with a **left coaction `λ : m → 𝔠 ◁ m`** satisfying **(8.84)**: `λ # (ε ◁ m) = id_m` and `λ # (δ ◁ m) = λ # (𝔠 ◁ λ) : m → 𝔠 ◁ 𝔠 ◁ m`. A morphism `α : m → n` satisfies `λ_m # (𝔠 ◁ α) = α # λ_n`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 8.83, p. 327
**Keywords:** left comodule, left coaction λ : m → 𝔠 ◁ m, counit law, coassociativity

### 8.84 Equation — The left comodule laws   [p. 328]
**Statement:** `λ # (ε ◁ m) = id_m`; `λ # (δ ◁ m) = λ # (𝔠 ◁ λ)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.84), p. 328
**Keywords:** left comodule laws

### 8.85 Exercise — C-coalgebras = CONSTANT left C-comodules   [p. 328]
**Statement:** The category of `C`-coalgebras (Def. 7.96) is **exactly** the full subcategory of left `C`-comodules whose carriers are **constant** polynomials.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.85, p. 328 (solution p. 344)
**Keywords:** C-coalgebra, constant left comodule

### 8.86 Definition — RIGHT COMODULE   [p. 328]
**Statement:** For a comonoid `D = (𝔡, ε, δ)`, a **right D-comodule** is a carrier `m` with **`ρ : m → m ◁ 𝔡`** satisfying **(8.87)**: `ρ # (m ◁ ε) = id_m` and `ρ # (m ◁ δ) = ρ # (ρ ◁ 𝔡)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 8.86, p. 328
**Keywords:** right comodule, right coaction ρ : m → m ◁ 𝔡

### 8.87 Equation — The right comodule laws   [p. 328]
**Statement:** `ρ # (m ◁ ε) = id_m`; `ρ # (m ◁ δ) = ρ # (ρ ◁ 𝔡)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.87), p. 328
**Keywords:** right comodule laws

### 8.88 Exercise — Polybox / ELEMENT forms of the comodule laws   [p. 329]
**Statement:** In elements: `a = a.id_{|a|}`; `cod(f) = |a.f|`; `a.(f # f') = (a.f).f'`; `λ♯_a(f # f', x) = λ♯_a(f, λ♯_{a.f}(f', x))`. (These are exactly the laws a container theorist would write for a two-sided module over categories-as-comonoids.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.88, p. 329 (solution pp. 344–346)
**Keywords:** bicomodule laws in elements, |−| : m(1) → 𝔠(1), a.f, λ♯, ρ♯

### 8.89 Exercise — y-comodules ARE just polynomials   [p. 329]
**Statement:** The category of left (resp. right) `y`-comodules is **isomorphic to Poly** — the coaction `λ` is forced to be `id_m`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.89, p. 329 (solution p. 346)
**Keywords:** y-comodule unique, y-Comod ≅ Poly, unit of Mod

### 8.90 Proposition — LEFT C-COMODULES ≃ FUNCTORS C → Poly   [p. 329]
**Statement:** For a category `C`, left `C`-comodules are **equivalent to functors `C → Poly`**, via `P^m_i := {a ∈ m(1) : |a| = i}` and **`p^m_i := Σ_{a ∈ P^m_i} y^{m[a]}`**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.90, p. 329
**Keywords:** left comodule = copresheaf valued in Poly, p^m_i = Σ_{a∈P_i} y^{m[a]}, C → Poly

### 8.91 Proposition — Right D-comodules ≃ functors D → Set^{m(1)}   [p. 329]
**Statement:** A right `D`-comodule is a functor `D × m(1) → Set`, `F(j, a) := {x ∈ m[a] : |a.f| = j}`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.91, p. 329
**Keywords:** right comodule as D-indexed family, F(j,a)

### 8.92 Proposition — y^G ◁ 𝔠 is a right C-comodule   [p. 330]
**Statement:** For any set `G`, `y^G ◁ 𝔠` carries a right `C`-comodule structure via `y^G ◁ δ`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.92, p. 330
**Keywords:** y^G ◁ 𝔠, right comodule from δ

### 8.93 Proposition — The FREE C-set on generators   [p. 330]
**Statement:** For `i' : G → 𝔠 ◁ 1`, `m := i^*(y^G ◁ 𝔠) ≅ y^{Σ_{g∈G} 𝔠[i'(g)]}` is a **representable right C-comodule**, i.e. (by Thm. 8.102) a **C-set**, whose elements are pairs `(g, f)` with `f : i'(g) → cod f`. This is the **free C-set** generated by `i'`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.93, p. 330
**Keywords:** free C-set, y^{Σ_g 𝔠[i'(g)]}, representable right comodule

### 8.94 Exercise — y^{𝔠[i]} as a right C-comodule via a PULLBACK   [p. 330]
**Statement:** The vertical–cartesian factorization of `i : y → 𝔠` is `y → y^{𝔠[i]} --φ--> 𝔠`; the square `(y^{𝔠[i]} --δ_i--> y^{𝔠[i]} ◁ 𝔠, φ, δ)` is a **pullback**, and `δ_i` makes `y^{𝔠[i]}` a right C-comodule.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.94, p. 330
**Keywords:** y^{𝔠[i]}, δ_i, pullback square, representable right comodule

### 8.95 Exercise — Functoriality of i ↦ y^{𝔠[i]}   [p. 331]
**Statement:** `y^{𝔠[f]} : y^{𝔠[i]} → y^{𝔠[i']}` is a morphism of right C-comodules, functorially — a functor `C → y Mod_C`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.95, p. 331
**Keywords:** y^{𝔠[f]}, functor C → y Mod_C, Yoneda-like embedding

### 8.96 Proposition — Coproducts of right comodules; representable decomposition   [p. 331]
**Statement:** `Σ_{i∈I} m_i` carries a right comodule structure (since `− ◁ 𝔠` commutes with coproducts, Prop. 6.47); moreover **each representable summand of a right comodule's carrier is itself a right comodule**, and `m` is their sum.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.96, p. 331
**Keywords:** coproduct of right comodules, (Σ m_i) ◁ 𝔠 ≅ Σ (m_i ◁ 𝔠), representable summand

### 8.97 Proposition — Combining right C- and right D-structures into (C × D)   [p. 331]
**Statement:** If `m` is both a right C- and a right D-comodule, it naturally carries a right `(C × D)`-comodule structure. (Key step: a right C-comodule with carrier `y^M` is the same as a **retrofunctor `My^M ⇸ C`**.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.97, p. 331
**Keywords:** product of comonoids, right comodule y^M ↔ retrofunctor My^M ⇸ C

### 8.98 Definition — BICOMODULE   [p. 331]
**Statement:** A **(C, D)-bicomodule** is `m ∈ Poly` that is both a left C-comodule (`λ : m → 𝔠 ◁ m`) and a right D-comodule (`ρ : m → m ◁ 𝔡`), satisfying the **coherence law (8.99)**: **`λ # (𝔠 ◁ ρ) = ρ # (λ ◁ 𝔡) : m → 𝔠 ◁ m ◁ 𝔡`**. Notation `𝔠 ◁(m)▷ 𝔡`. Footnote 4: the notation "also looks like an arrow going backward from `𝔡` to `𝔠`, which will turn out to have a semantic advantage."
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 8.98, p. 331
**Keywords:** bicomodule, coherence law, 𝔠 ◁(m)▷ 𝔡, C Mod_D

### 8.99 Equation — The bicomodule coherence law   [p. 331]
**Statement:** `λ # (𝔠 ◁ ρ) = ρ # (λ ◁ 𝔡)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.99), p. 331
**Keywords:** coherence law, left and right coactions commute

### 8.100 Equation — Polybox form of the coherence law   [p. 332]
**Statement:** The two polybox composites are equal, so one can unambiguously write a single combined polybox for `𝔠 ◁(m)▷ 𝔡`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.100), p. 332
**Keywords:** polyboxes, unambiguous combined polybox

### 8.101 Exercise — Degenerate bicomodules over y   [p. 332]
**Statement:** A left C-comodule = a `(C, y)`-bicomodule; a right C-comodule = a `(y, C)`-bicomodule; every `p ∈ Poly` has a **unique** `(y,y)`-bicomodule structure; **`Poly ≅ y Mod_y`** (so `y` is the unit of `Mod`).
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.101, p. 332 (solution p. 346)
**Keywords:** (C,y)-bicomodule, Poly ≅ y Mod_y, unit of Mod

### 8.102 Theorem — THE EIGHT-FOLD EQUIVALENCE   [p. 333]
**Statement:** VERBATIM: "Given a polynomial comonoid `C = (𝔠, ε, δ)`, the following comprise **equivalent categories**: 1. functors `C → Set`; 2. discrete opfibrations over `C`; 3. **cartesian retrofunctors to `C`**; 4. `C`-coalgebras; 5. **constant left C-comodules**; 6. **(C, 0)-bicomodules**; 7. **linear left C-comodules**; 8. **representable right C-comodules (opposite)**. In fact, **all but the first comprise ISOMORPHIC categories**; and up to isomorphism, any one of these can be identified with a **retrofunctor from a state category to `C`**." Key steps: 5≅7 via `Poly(Sy, 𝔠 ◁ Sy) ≅ Set(S, 𝔠 ◁ S)`; 7≅8 via (6.66): `Poly(Sy, 𝔠 ◁ Sy) ≅ Poly(y^S, y^S ◁ 𝔠)`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Theorem 8.102, p. 333
**Keywords:** eight equivalent categories, equivalence chain, copresheaf, discrete opfibration, cartesian retrofunctor, coalgebra, constant left comodule, (C,0)-bicomodule, linear left comodule, representable right comodule, state category
**Attribution:** none stated for the theorem as a whole.

### 8.103 Exercise — Completing Thm. 8.102 (3 ≅ 4)   [p. 335]
**Statement:** Show `𝔰 := α_1^* 𝔠` is a comonoid, `(α_1, id) : 𝔰 ⇸ 𝔠` a retrofunctor, and the roundtrips are identities and functorial.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.103, p. 335
**Keywords:** base change α_1^* 𝔠, roundtrip identity

### 8.104 Exercise — Where the representable copresheaf C(c, −) goes   [p. 335]
**Statement:** Trace `C(c, −)` through all eight descriptions. (Context: the **terminal** functor `C → Set` corresponds to the identity dopf, the identity retrofunctor, the **canonical left C-comodule with carrier `C(1)y`**, the **canonical (C,0)-bicomodule with carrier `C(1)`**, and the **canonical right C-comodule with carrier `y^{C(1)}`**.)
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.104, p. 335
**Keywords:** representable copresheaf C(c,−), canonical comodules, C(1)y, y^{C(1)}

### 8.105 Exercise — (0, C)-bicomodules and 0 Mod_C   [p. 335]
**Statement:** Given that `C Mod_0` is the **topos of copresheaves on `C`** (Thm. 8.102), what is a `(0, C)`-bicomodule, and what is `0 Mod_C`?
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.105, p. 335
**Keywords:** C Mod_0 topos of copresheaves, (0,C)-bicomodule

### 8.106 Proposition (GARNER) — BICOMODULES ARE PARAMETRIC RIGHT ADJOINTS   [p. 336]
**Statement:** VERBATIM: "Let `C` and `D` be categories. Then the following can be identified, up to isomorphism: 1. a **(C, D)-bicomodule**. 2. a **parametric right adjoint `Set^D → Set^C`**. 3. a **connected limit-preserving functor `Set^D → Set^C`**." Concretely, for `m = Σ_{i∈m(1)} y^{m[i]}` given a `(D, C)`-bicomodule structure: **`m(1) ∈ Set^D`** and **`m[i] ∈ Set^C`** — positions form a D-copresheaf, directions form a C-copresheaf. Note the **direction reversal**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Proposition 8.106, p. 336
**Keywords:** parametric right adjoint, prafunctor, connected limit preserving, Set^D → Set^C, bicomodule, familial functor
**Attribution:** **RICHARD GARNER** (named in the statement). p. 335: "There is an equivalent characterization of bicomodules … **due to Richard Garner. Thus we attribute the foundational theory of Cat♯ to Ahman-Uustalu-Garner.**" §8.4, p. 338: "This idea was due to Richard Garner; **it is currently unpublished**, but can be found in video form here: https://www.youtube.com/watch?v=tW6HYnqn6eI". **No proof is given in the book.** Also p. 336: "Parametric right adjoints model data migrations between categorical databases; see **[SW15]**."

### 8.107 Definition — PRAFUNCTOR   [p. 336]
**Statement:** A **prafunctor** (parametric right adjoint functor) `Set^C → Set^D` is one satisfying any of the conditions of Prop. 8.106.
**Cite as:** Niu–Spivak arXiv:2312.00990, Definition 8.107, p. 336
**Keywords:** prafunctor, parametric right adjoint functor, familial functor
**Attribution:** §8.4, p. 338: "What we call prafunctors are sometimes called **familial functors** between (co-)presheaf categories; see **[Web07], [GH18], [Sha21]**."

### 8.108 Example — CELLULAR AUTOMATA   [p. 336]
**Statement:** For a graph `src, tgt : A ⇒ V`, put `g := Σ_{v∈V} y^{src^{-1}(v)}`, a bicomodule `Vy ◁(g)▷ Vy`. A bicomodule `Vy ◁(T)▷ 0` is a functor `T : V → Set` (colour sets). A **cellular automaton** is a bicomodule map `α : (Vy ◁g▷ Vy) ◁_{Vy} (Vy ◁T▷ 0) ⇒ (Vy ◁T▷ 0)`; concretely an **update function** `α_v : Π_{src(a)=v} T(tgt(a)) → T(v)` for each `v`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.108, p. 336
**Keywords:** cellular automaton, g = Σ_v y^{src^{-1}(v)}, update function, colour set

### 8.109 Exercise — Structure lenses for the graph bicomodule   [p. 337]
**Statement:** `λ : g → Vy ◁ g` is the diagonal; `ρ : g → g ◁ Vy` is `v ↦ (v, a ↦ tgt(a), a)`. **"Most of this is forced on us, and the only interesting part is the function `A_v → V`, which … is exactly the choice of 'target map' that defines our graph."**
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.109, p. 337 (solution p. 346)
**Keywords:** λ : g → Vy ◁ g, ρ : g → g ◁ Vy, tgt, target map is the only data

### 8.110 Example — Running a cellular automaton   [p. 337]
**Statement:** An **initialization** is a bicomodule map `σ` (8.111): `(Vy ◁V▷ 0) ⇒ (Vy ◁T▷ 0)`. Since each `g_v = y^{src^{-1}(v)}` is representable, `g ◁_{Vy} V ≅ V`. Running for `k` steps = whiskering `k` copies of `g` with `σ` and then repeatedly with `α`.
**Cite as:** Niu–Spivak arXiv:2312.00990, Example 8.110, p. 337
**Keywords:** running a cellular automaton, initialization, g ◁_{Vy} V ≅ V, whiskering

### 8.111 Equation — Initialization of a cellular automaton   [p. 337]
**Statement:** `σ : (Vy ◁V▷ 0) ⇒ (Vy ◁T▷ 0)` — a choice of starting colour at each vertex.
**Cite as:** Niu–Spivak arXiv:2312.00990, Eq. (8.111), p. 337
**Keywords:** initialization σ, bicomodule 2-cell

### 8.112 Exercise — Why (8.111) is an initialization   [p. 338]
**Statement:** A `(Vy, 0)`-bicomodule `T` assigns each vertex a set of colours; `V` assigns each a singleton; so a map `V → T` **chooses one colour per vertex**.
**Cite as:** Niu–Spivak arXiv:2312.00990, Exercise 8.112, p. 338 (solution p. 347)
**Keywords:** (Vy,0)-bicomodule, colours, starting colour

## §8.5 Exercise solutions (pp. 339–348) — additional citable content

- **Sol. 8.11 / 8.17** (pp. 339–341): the closed forms for `tree_p` and `𝔱_p` (listed at 8.11, 8.17 above). Key step: the height-n vertices of a `B y^A`-tree biject with `A^n`, so the vertex set is `List(A)` and a tree is a labelling `List(A) → B`.
- **Sol. 8.16** (p. 340): `tree_p ≅ p ◁ tree_p` is the terminal coalgebra; the unique `u : S → tree_p` from a coalgebra `f : S → p ◁ S` is built as `(f'_n)_{n∈ℕ}` with `f_{n+1} = f_n ; (p^{◁n} ◁ f)`.
- **Sol. 8.56** (p. 343): the retrofunctor `T_p ⇸ T_{p^{◁n}}` comes from the lens `δ^{(n)} # r^{◁n} : 𝔱_p → p^{◁n}` (`r` = counit); bijective on objects, NOT on morphisms.
- **Sol. 8.67** (p. 343): the explicit vert–cart factorization: `𝔠'(1) := 𝔠(1)`, `𝔠'[i] := 𝔡[f i]`, composition inherited from `𝔡`.
- **Sol. 8.88** (pp. 344–346): the **element-level** bicomodule laws (see 8.88 above) — the exact laws a container theorist would independently write down.
- **Sol. 8.101** (p. 346): all four unitality checks for bicomodule composition reduce to (8.99) commuting vacuously when `𝔡 = y` — this is what makes `y` the unit of `Mod`.

---

# CROSS-REFERENCE: results OUTSIDE Ch. 6–9 that this range leans on

(Useful because a novelty check may land on one of these instead.)
`Prop. 1.37` (pointwise (co)limits of Set-functors) · `Eq. (1.30)/(1.32)` (distributivity) · `Example 3.22` (**the derivative `ṗ`**, p. 52 — the ONLY derivative material in the book) · `Eq. (3.7)` (`Poly(p,q) ≅ Π_{i∈p(1)} q(p[i])`) · `Prop. 3.44`/`Cor. 3.47` (lens ↔ natural transformation) · `Example 3.43` (lenses) · `Eq. (4.75)/(4.79)` (the `⊗`-closure `[−,−]`) · `Exercise 4.23` (the halting DFA) · `Eq. (5.9)` (copower/power adjunction) · `Prop. 5.12` (`y^{(−)} : Set^op → Poly` is a left adjoint) · `Prop. 5.18` · `Thm. 5.33` (Poly is complete) · `Example 5.38` (**pullbacks in Poly: positions pull back, directions push OUT**) · `Thm. 5.43` (Poly is cocomplete) · `Prop. 5.59` (cartesian ⟺ naturality squares are pullbacks).
