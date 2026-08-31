# Fibrational containers: what already exists

**Date:** 2026-07-14
**Task (from Neil):** `Cont ≅ Fam(Set^op)` is the free coproduct completion of `Set^op`. Generalize: given a fibration `p : E → B`, what is `Cont(p)`?

---

## HEADLINE — READ THIS FIRST

**The fibrational generalization is ALREADY DONE, completely, and the author calls the answer "the category of containers" in so many words.**

It is **Tamara von Glehn**, *Polynomials and models of type theory*, PhD thesis, University of Cambridge, 2015 (advisors Johnstone & Hyland), DOI 10.17863/CAM.16245; published as **"Polynomials, fibrations and distributive laws", Theory and Applications of Categories 33 (2018), no. 36, 1111–1144.**

From her abstract (verbatim):

> "Polynomial functors make sense in a category when there exist **pseudomonads freely adding indexed sums and products to fibrations** over the category, and **a category of polynomials is obtained by adding sums to the opposite of the codomain fibration**."

And from §4.1 (verbatim):

> "The base category of the new type theory `Poly_F` is also known as **the category of containers** and studied in the case when `B` is locally cartesian closed in [Abb03, AAG03]."

`[Abb03, AAG03]` = Abbott's thesis and **Abbott–Altenkirch–Ghani**. So Neil's own work is explicitly cited *as the special case*. This strongly suggests Neil is pointing at von Glehn (or at least will recognise her the moment he sees it). **Do not re-derive this.**

### The answer, stated

For a fibration `p : E → B` (with the relevant structure):

> **`Cont(p) := Σ_p ( p^op )`** — apply the *fibrewise opposite* (dual) to `p`, then freely add indexed sums.
> Concretely, `Cont(p)` is the **total category of the fibrewise-opposite fibration**, i.e. `∫(p^op)`:
> - objects: pairs `(I ∈ B, X ∈ E_I)`;
> - morphisms `(I,X) → (J,Y)`: a map `u : I → J` in `B` **plus a vertical map `u*(Y) → X` in the fibre `E_I`**.

That vertical-map-backwards is *exactly* the container morphism `q[u s] → p[s]`. Setting `p =` the codomain/family fibration of `Set` recovers `Cont = Fam(Set^op)` on the nose.

Equivalently, von Glehn presents it as the fibre over `1` of the two-sided fibration `Σ_F Π_F F ⇉ B`, built in her §1.9.

### The machinery she uses (all in her Chapter 1)

- `Σ_B` — a **lax-idempotent pseudomonad on `Fib(E)`** freely adding indexed sums (this is "Fam for fibrations").
- `Π_B := (Σ_B)^op` — **colax-idempotent** pseudomonad freely adding products. *The fibrewise-op duality is built into the machinery.*
- A **pseudo-distributive law of `Π` over `Σ`** (Prop. 1.30 for `E = Set`; Prop. 1.33 in general) makes `ΣΠ` a pseudomonad — **this is what composition of polynomials/containers IS**. Local cartesian closedness of the base ⟺ existence of this distributive law.
- **Prop. 1.33** is the key structural theorem: for a class `F` of display maps, TFAE — (1) `Ψ_F` lifts to a lax-idempotent pseudomonad `Σ_F` in `Fib`; (2) a pseudo-distributive law `λ : Φ_B Ψ_F → Ψ_F Φ_B` exists; (3) **the codomain functor `c : F → B` is a fibration**; (4) `F` is stable under pullback.
- **Def. 1.34**: a fibration `p : M → B` *has `F`-sums* iff it is a left module for `Σ_F`.

Her §1.9 is literally titled **"Polynomials in non-lcc categories"** — precisely Neil's question.

---

## THE TRAP (Neil's crux — report on this specifically)

Yes: the contravariance of positions means you need the **fibrewise opposite**, and **naively dualizing is WRONG.**

**Streicher, *Fibered Categories à la Jean Bénabou*, arXiv:1801.02927, Chapter 5, "The Opposite of a Fibration"** — opens with exactly our motivation and exactly the warning:

> "If `P : X → B` is a fibration thought of *'as of the form `Fam(C)`'* then one may want to construct the fibration `P^op` thought of *'of the form `Fam(C^op)`'*. **It might be tempting at first sight to apply `(−)^op` to the functor `P` giving rise to the functor `X^op → B^op` which, however, has the wrong base** — even if it were a fibration (which in general it will not be)."

So `(-)^op` on the total category is **not** the construction. The correct one:

- **Split/indexed case (easy):** if `P = ∫H` for `H : B^op → Cat`, then `P^op := ∫(H^op)` where `H^op(I) = H(I)^op` — apply `(−)^op` **fibrewise**, to fibres and to reindexing functors. Spivak calls this the **pointwise opposite** `F^p`.
- **General (cleavage-free) case:** objects of `P^op` are those of `P`; a morphism `Y → X` over `u : J → I` (with `Y ∈ P(J)`, `X ∈ P(I)`) is an **equivalence class of spans `(α, φ)`** with `α : Z → Y` **vertical** and `φ : Z → X` **cartesian over `u`**, modulo vertical iso.

Unwind that span with `Z = u*(X)`: it is a vertical map `u*(X) → Y`. **That is the container morphism, verbatim.** So Streicher's Chapter 5 is, without knowing it, the definition of the container category over a general fibration.

**Consequence / gotcha:** the fibrewise opposite is *not* functorial on arbitrary fibred functors — it is functorial on **cartesian** functors only, and the span-quotient means `P^op` is generally only a *cloven*, not split, fibration unless `P` was split. Spivak's **Remark 3.4** makes the same point from the other side ("we chose `Lens_F` to be the fiberwise opposite of `Gr(F)` rather than replacing `F` with `F^p` at the outset").

---

## Does `Fam(−)` applied to a fibration have a standard name? YES — three of them.

1. **Streicher, op. cit., Chapter 6, Definition 6.2: the "fibred family fibration" `Fam(P)`.** Defined by the comma/pullback `P ↓ B → B²`, fibred over `B` by `∂₁`. Footnote 5: **`(Fam, η, μ)` is a monad on `Fib(B)`.**
   - **Theorem 6.1**: `P` **has internal sums iff `η_P : P → Fam(P)` has a fibred left adjoint `∐_P ⊣ η_P`** (cartesian, with cartesian unit/counit). This *is* "Fam = free coproduct completion", at the level of fibrations.
2. **von Glehn's `Σ` pseudomonad on `Fib(E)`** (above) — same thing, done 2-categorically, and lax-idempotent (= "free cocompletion under Σ" in the KZ sense, so the algebras are *property-like*: having sums is a property, not structure). This is the cleanest formulation.
3. **"Σ-completion" / "existential completion"** in the categorical-logic literature (Trotta; Maietti–Trotta; see also *Skolem, Gödel and Hilbert fibrations*, arXiv:2407.15765, which discusses the Σ-completion and explicitly relates it to "the family construction on the level of fibrations"). Same construction, logician's name.

So: **`Fam` on fibrations = Streicher's fibred family monad = von Glehn's `Σ` = the Σ-/existential completion.** Use von Glehn's, it's the sharpest.

---

## Ranked reading list

1. **von Glehn, T.** *Polynomials, fibrations and distributive laws.* TAC **33** (2018), no. 36, 1111–1144. (= thesis *Polynomials and models of type theory*, Cambridge 2015, DOI 10.17863/CAM.16245; free PDF at Cambridge Apollo.)
   → **THE answer.** Defines polynomials/containers over an arbitrary fibration as `Σ` applied to the fibrewise-opposite codomain fibration; §1.9 "Polynomials in non-lcc categories"; §4.1 identifies the base category as *the category of containers* and cites AAG as the LCC special case. Composition of containers = a pseudo-distributive law `ΠΣ → ΣΠ`.

2. **Streicher, T.** *Fibered Categories à la Jean Bénabou.* arXiv:**1801.02927**.
   → Ch. 5 **"The Opposite of a Fibration"** (the fibrewise dual, with the exact `Fam(C) ↦ Fam(C^op)` motivation and the "wrong base" warning); Ch. 6 **`Fam(P)`, Def. 6.2 + Thm 6.1** (the family monad on `Fib(B)`, internal sums via a fibred left adjoint). The two ingredients of `Cont(p)`, in one document.

3. **Spivak, D. I.** *Generalized Lens Categories via functors `C^op → Cat`.* arXiv:**1908.02202**.
   → **Def. 3.3 (`F`-lenses)**: `Lens_F := Gr_o(F^p)`, the Grothendieck construction of the **pointwise opposite**; morphism `(c,x) → (d,y)` is `f : c → d` plus `f♯ : F(f)(y) → x`. **Prop. 3.2** = the three isomorphic presentations. **Example 3.5 (dependent lenses)**: `F = Slice`, giving exactly `Cont` when `C = Set`. **Crucially answers "what survives":** the get-functor `π_F : Lens_Slice → C` is a **fibration** always, a **bifibration** when `C` has pullbacks (`Σ_f`), and a **trifibration** when `C` is **locally cartesian closed** (`Π_f`). That is the precise structure ladder for `Cont(p)`.

4. **Abbott, M.; Altenkirch, T.; Ghani, N.** *Containers: constructing strictly positive types.* TCS **342** (2005) 3–27. (+ *Categories of Containers*, FoSSaCS 2003, LNCS 2620; + Abbott's Leicester PhD thesis, 2003.)
   → **Neil's own work, and it is already the fibrational special case.** Works throughout in an ambient **locally cartesian closed category with disjoint coproducts** ("Martin-Löf category"), and explicitly uses fibred functors / fibred natural transformations over `C` (TCS §2: "We will need to make some explicit use of the machinery of fibrations"). This is `Cont(p)` for `p =` the codomain fibration of an LCCC. **The gap von Glehn fills is exactly: drop LCC.**

5. **Gambino, N.; Kock, J.** *Polynomial functors and polynomial monads.* Math. Proc. Camb. Phil. Soc. **154** (2013) 153–192; arXiv:0906.4931.
   → Polynomial functors over an **LCCC** `E`; framed bicategory `PolyFun_E`. Note **§1.17**: they explicitly flag that LCC is *not* necessary — one can work with **exponentiable (Conduché) maps** in a category with pullbacks. That remark is the doorway to the fibrational version, which they do not walk through.

6. **Weber, M.** *Polynomials in categories with pullbacks.* TAC **30** (2015), no. 16, 533–598; arXiv:**1106.1983**.
   → Drops LCC to **pullbacks only**, requiring the middle map of the polynomial to be **exponentiable**; relates to Street's fibrations *internal to* a 2-category. The other main "non-LCC" generalization; von Glehn (§1.9) says she "generalizes in a slightly different direction" from Weber. **Read these two together — they are the two competing answers, and von Glehn's is the one that matches the `Fam ∘ (−)^op` shape.**

7. **Altenkirch, T.; Ghani, N.; Hancock, P.; McBride, C.; Morris, P.** *Indexed containers.* JFP **25** (2015), e5.
   → **NOT the fibrational generalization** — worth knowing precisely why. `ICont I J` is containers over the *slices* `Set/I`, i.e. the codomain fibration of `Set`; and **footnote 3 explicitly disclaims the reading you'd want**: "This should not be confused with the usual notion of the category of families over a given base category, i.e. **the families fibration**." So it is an *instance* (one particular `p`), not a generalization over `p`. Good news for MacBeth: the JFP paper leaves the door open on purpose.

8. **Vertechi, P.** *Dependent Optics.* arXiv:**2204.09547** (ACT 2022).
   → Builds optics from **two indexed categories** (forward and backward), via "the Grothendieck construction on the **pointwise opposite**". **Dependent lenses = containers** are a special case; gives conditions for coproducts. The natural *two-fibration* generalization of `Cont(p)` — i.e. the answer if Neil later asks "why should forward and backward live over the same fibration?" See also **Capucci, *Seeing double through dependent optics*, arXiv:2204.10708**.

### Also worth knowing (recent, and close to us)
- **Hua, J.; Xu, Y.** *Polynomial functors in π-clans for the semantics of type theory.* arXiv:**2602.05689** (Feb 2026). Polynomial functors where the context category is **not LCC** but is a π-clan. The current live front of exactly this question.
- **Chen, K.** *On polynomial functors and polynomial comonads over infinity groupoids.* arXiv:**2601.22968** (Jan 2026). `Poly_S` for `S` = ∞-groupoids; defines polynomial **comonads** there and **"partially generalizes"** the Ahman–Uustalu theorem (directed container = small category). **This is the closest anyone has come to the directed/comonoid layer over a base other than `Set` — and they say themselves it is only partial.**
- **Hazratpour, S.** `sinhp/Poly` — Lean 4 formalization of polynomial functors (`UvPoly`) in an LCCC, underpinning Awodey's natural models / HoTTLean. If MacBeth wants a Lean target, this is the existing API to build on rather than duplicate.
- **Jacobs, B.** *Categorical Logic and Type Theory* (1999) — the standard reference for the family fibration, comprehension categories, and `Σ`/`Π` in fibrations. Background, not a competitor.

---

## Honest verdict on novelty (the fifth-burn check)

- **`Cont ≅ Fam(Set^op)` is prior art.** It's on the nLab (*free coproduct completion*), in Spivak's *summary of categorical structures in Poly* (arXiv:2202.00534), and the **1Lab literally defines `Poly` as `∫ (Family (Sets ^op))`** in `Cat.Instances.Poly`. MacBeth's own memory already flagged this ("the map itself = prior art, 6 cites"). Fine as an *observation*; not publishable as a result.
- **`Cont(p)` for a general fibration is prior art too** — von Glehn 2015/2018, and independently reachable as Spivak's `Lens_F` / Vertechi's dependent optics. **Claiming the definition would be the fifth burn. Don't.**

### What is genuinely NOT done (the gap to own)

The **directed / comonoid layer over a general fibration**:

- von Glehn builds `(Cont(p), ◁)` (via the `ΣΠ` pseudo-distributive law) but her interest is *models of type theory*; she never asks about **comonoids in `(Cont(p), ◁)`**.
- Ahman–Uustalu's theorem — **directed container = small category**, and `DCont ≅ Cof` — is stated only over `Set`.
- Chen (arXiv:2601.22968, Jan 2026) generalizes it to ∞-groupoids and explicitly calls his result **"partially generalizing"** Ahman–Uustalu. **Nobody has done it over a general fibration.**
- Likewise the **four monoidal structures** (`+`, `×`, Dirichlet `⊗`, `◁`) and the duoidal/`Cat#` story over a general `p`: unexamined. MacBeth's `DCont ≅ Cof` and Zappa–Szép results are all `Set`-based.

**Recommended framing for Neil:** cite von Glehn for the definition (`Cont(p) = Σ_p(p^op)`), cite Streicher for the fibrewise dual, and push the *directed* theory — "what is a small category internal to a fibration, seen as a `◁`-comonoid in `Cont(p)`?" — which is open and is squarely MacBeth's existing territory. Chen's paper is both the evidence that the question is live and the clock that says move.

---

## Traps summary

1. **Do not dualize the total category.** `X^op → B^op` has the wrong base and generally isn't a fibration (Streicher Ch. 5, first paragraph).
2. **Fibrewise op is only functorial in *cartesian* functors**, and preserves splitness only if you started split. Expect a span/zigzag quotient in the general (cloven) case.
3. **`Π` is where LCC hides.** Positions being *sets* is what gives `Π`. Over a general fibration you get: fibration (always) → bifibration (pullbacks; gives `Σ`, hence coproducts of containers) → trifibration (LCC/exponentiable; gives `Π`, hence **the extension functor `⟦−⟧` and the composition `◁`**). Spivak Ex. 3.5 spells out exactly this ladder. So "which container theory survives" has a crisp answer: **`+` and `×` survive with pullbacks; `◁` and `⟦−⟧` need `Π`.**
4. `Fam` is **lax-idempotent (KZ)** — so "having sums" is *property-like*, not extra structure. That's why the theory is as rigid as it is, and it's the right way to say "free coproduct completion" 2-categorically.
