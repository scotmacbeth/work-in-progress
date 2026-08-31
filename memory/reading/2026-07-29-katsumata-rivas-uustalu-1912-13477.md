# Deep-read: Katsumata–Rivas–Uustalu, "Interaction Laws of Monads and Comonads" (arXiv:1912.13477)

**Read:** 2026-07-29 (full text, PDF via pdftotext -layout, ~2370 lines).
**Prior depth:** abstract-only (SUMMARY.md line 56: "Chu/Day interaction laws = *pairing*, not compositor"; connections/three-modes-of-composition.md; sources.json entry). This note EXTENDS that — the abstract-level guess was correct and is now confirmed at definition level, plus new detail on the degeneracy/branching theorems and the exact Day-vs-composition monoidal subtlety.

## Metadata
- **Authors:** Shin-ya Katsumata (NII Tokyo), Exequiel Rivas (Inria Paris), Tarmo Uustalu (Reykjavik / Tallinn). Title verified verbatim.
- **Venue:** FoSSaCS 2020 (this is the arXiv v1, 31 Dec 2019). 22pp + appendix.
- **Base category:** ONE fixed base category `C`, assumed **extensive with finite products**; **Cartesian closed** additionally for the dual construction (§ intro, lines 81–84). Set is the running example. NOT restricted to any subcategory of functors except pragmatically (finitary functors) to make Day convolution/exponential total.

---

## Q1 — What exactly is an interaction law?

**Functor-functor interaction law** (§2.1): two endofunctors `F, G` on `C` and a family
> `φ_{X,Y} : F X × G Y → X × Y` natural in X, Y.
No further laws. Category `IL(C)`; a map `(F,G,φ)→(F',G',φ')` is `(f:F→F', g:G'→G)` with `φ ∘ (id_F × g) = φ' ∘ (f × id_{G'})` (note the **contravariance in G** — g goes backwards).

**Monad-comonad interaction law** (§3.1, Def + Eq (1)): a monad `T=(T,η,μ)`, a comonad `D=(D,ε,δ)`, and a natural family
> `ψ_{X,Y} : T X × D Y → X × Y`
that is a functor-functor interaction law AND satisfies the four (co)unit/(co)mult compatibilities (Eq (1)):
- **unit/counit:** `ψ ∘ (η_X × id) = ` project after `id×ε`, i.e. `ψ_{X,Y}(η x, d) = (x, ε d)` — returning a value interacts trivially, reading off the initial state via ε.
- **mult/comult:** `ψ ∘ (μ_X × id) = ψ ∘ (id × ε-chain) ...` precisely: `ψ_{X,Y} ∘ (μ_X × id_{DY}) = ψ_{X,Y} ∘ (id × δ_Y)`-routed double interaction `ψ_{TX,DY}` then `ψ_{X,Y}` — sequencing two computations = two successive interactions threading the comonad's comultiplication.

**Type-summary: `ψ` takes a computation `TX` and a machine-behavior-from-initial-state `DY`, returns a value `X` and a final state `Y`.** Explicitly (line 46): "a natural transformation ψ : T X × DY → X × Y compatible with the (co)unit and (co)multiplication."

Examples: reader/writer/update monad paired with its evident comonad (Ex 6/7/8). Update monad `TX=A⇒(B×X)` vs `DY=A×(B⇒Y)`.

---

## Q2 — Chu spaces / Day convolution / monoid object

**Two-step story (§6). The Day-convolution tensor and the composition tensor are DIFFERENT, and this distinction is the whole point.**

**(a) Chu over Day (§6.1).** Day convolution on `[C,C]`:
`(F ? G) Z = ∫^{X,Y} C(X×Y, Z) • (F X × G Y)`.
Coend/end calculus gives `∫_{X,Y} C(FX×GY, X×Y) ≅ ∫_Z C((F?G)Z, Z)`, so:
> "a functor-functor interaction law is a triple `(F, G, φ : F ? G → Id_C)`, i.e., a **Chu space over the monoid object `Id_C` w.r.t. the Day convolution monoidal structure** on `[C,C]`. … `IL(C) ≅ Chu([C,C], Id_C)`." (lines 1714–1716)

BUT the authors immediately warn: the *canonical* Chu monoidal structure (built from Day via pullbacks) is **NOT** the one they want. "we are interested in a different monoidal structure on IL(C) that is based on **composition** and gives us monads and comonads as monoids resp. comonoids." (lines 1718–1721)

**(b) Hasegawa glueing (§6.2) — this is where monad-comonad interaction laws = monoid objects.** Take `[C,C]` as a **duoidal category** `(F, I, ⊗, J, ?)` with `⊗ = functor composition` (the tensor for the monoid structure) and `? = Day convolution` (the closed structure). Define `(−)◦ : F^op → F` by `G◦ = G −? Id` (the Day-convolution internal hom into Id — this IS the "dual"). Then the comma category `F ↓ (−)◦` is monoidal (glueing), and:
> "An object of `F ↓ (−)◦` is a functor-functor interaction law while a **monad-comonad interaction law is a monoid object of this category**." (lines 1761–1762); `MCIL(C) ≅ Mon(IL(C))` (line 632).

**So the precise statement: monad-comonad interaction laws are monoid objects in `IL(C)` where `IL(C)`'s monoidal structure comes from Hasegawa glueing of the COMPOSITION tensor on `[C,C]`, and Day convolution enters only as the closed structure `−?` used to define the dual `(−)◦`.** The tensor of interaction laws is `(F,G,φ)⊗(J,K,ψ) = (F·J, G·K, ψ∘φ·(J×K))` — composition of functors, NOT Day (lines ~127). Day is the *ambient closed structure*, not the monoid tensor.

Dual `(−)◦` and Sweedler dual: greatest functor interacting with `G` = its dual `G◦ = ∫_Y GY ⇒ (X×Y)` (§2.3); greatest comonad interacting with monad `T` = its **Sweedler dual** `T•` (§3.4, §6.2), the equalizer in `Comon(F)` (line 1858). Interaction laws of `T` with `D` ⟺ comonad morphisms `D → T•` (line 1137).

---

## Q3 — PAIRING or COMPOSITOR? **PAIRING. Decisively.** (critical for MacBeth)

`ψ : T X × D Y → X × Y` is a **pairing / running map**: run an effect `TX` against a coeffect/behavior `DY`, extract value×state. It is **NOT** a distributive law `TD⇒DT` or `DT⇒TD`. Confirming evidence:

1. The type itself: `× → ×` at the object level, not `TD ⇒ DT`.
2. Equivalent forms (all pairings): comonad map `D → T•` (Sweedler dual); runner = monad map `T → St_Y` where `St_Y X = Y⇒(X×Y)` (§4.1, line ~1218); "stateful runners" of Uustalu.
3. **Distributive laws are INPUTS, not outputs.** The only place `TD⇒DT`-type structure appears is §"Interaction laws of a composite monad" (lines 925–980): to build an interaction law on a *composite* monad `T0·T1` you must be *handed* a **monad-monad distributive law `λ` of T1 over T0** (and, for composite comonads, a comonad-comonad distributive law `κ`). The framework *consumes* distributive laws to glue pairings; it never *produces* a distributive law as a byproduct.

**Verdict: their "interaction law" is a Chu-space pairing, orthogonal in kind to MacBeth's mixed distributive law `λ:T_M G_M ⇒ G_M T_M`.** MacBeth's earlier one-line gloss ("pairing, not compositor") is exactly right.

---

## Q4 — Polynomial / container restriction? **NO.**

General endofunctors on an extensive, finite-product (Cartesian-closed for duals) category. **Zero occurrences of "polynomial" or "container" in the entire text.** No restriction to Poly/Cont at any point. Guiding examples are Set-monads (reader, writer, update, Maybe, nonempty list, free monads). The only closure assumption is pragmatic (restrict to finitary functors so `?` and `−?` are total — line ~1764). Their Day convolution is the *general* `[C,C]` Day convolution, not MacBeth's Dirichlet-on-Cont specialisation — but the two coincide when `C=Set` and functors are containers (the Dirichlet tensor IS Day convolution of `+`; see MacBeth's dirichlet-is-day-convolution note).

---

## Q5 — Branching / arity condition? **YES — three degeneracy theorems, strongly parallel to MacBeth's non-branching criterion.**

The paper has a systematic "structural operation on the effect functor ⟹ interaction degenerates" family (§2.2, §3.2):

- **Theorem 1** (nullary op = partiality): if `F` has a family `c_X : 1 → F X` natural (a nullary operation, e.g. `Maybe`'s `nothing`), then any interacting functor `G ≅ 0`. Proof: strictness of initial object in an extensive category.
- **Theorem 2** (commutative binary op): if `F` has commutative `c_X : X×X → F X` (`c = c∘sym`), then any interacting `G ≅ 0`. Uses coproduct-disjointness in an extensive category.
- **Theorem 3** (MONAD-comonad, **associative** binary op): if a monad `T` has an *associative* binary operation `c_X : X×X → T X` (compatible with μ), then for any comonad `D` and interaction law `ψ`, the two "extract-a-branch" composites collapse. **Example 9:** the nonempty-list / free-semigroup monad `T X = X⁺` with `dblt(x0,x1)=[x0,x1]` — "**no monad-comonad interaction law can extract a middle element `x_i` (0<i<n+1) from a list [x0,…,x_{n+1}]**" (lines 895–898). Note the contrast: *functor-functor* laws CAN do this; the *monad* laws are what forbid it.

**This is a genuine sibling of MacBeth's result.** MacBeth: arrows `Cont(G_M p, T_M q)` form a category ⟺ `M` non-branching; the compositor `κ:GT⇒TG` exists iff non-branching. KRU: a *non-degenerate* monad-comonad interaction law is obstructed exactly when the monad carries an associative (branching ≥2) binary operation. **Both say "branching / arity ≥ 2 obstructs the effect–coeffect interaction," reached by completely different mechanisms** (KRU: extensive-category coproduct disjointness + strictness; MacBeth: failure of arrow-composition associativity E2′, and separately the H² obstruction). The *direction/object* differs (KRU obstructs a pairing; MacBeth obstructs an arrow-category built from a compositor), but the branching-is-the-enemy phenomenon is the same. **Worth citing as an independent confirmation of the branching dichotomy.**

KRU's escape hatch: **residual** interaction laws (§2.4, §5) — replace codomain `X×Y` by `R(X×Y)` for a monad `R` (Maybe / finite multiset), so partial/branching interaction becomes possible with a residual effect. MacBeth analogue: this is like allowing the arrow composite to land in a larger effect — a possible route past the non-branching wall worth a look.

---

## RELEVANCE TO MACBETH'S ENTWINING — verdict on route (b)

**Route (b) as literally stated — "reframe the `T_M`/`G_M` entwining `λ:T_M G_M ⇒ G_M T_M` as a Chu/Day monoid object" — is a CATEGORY MISMATCH and is NOT a free win.** KRU's monoid objects are **pairings** `ψ:TX×DY→X×Y` (running an effect against a coeffect), whereas MacBeth's entwining is a **mixed distributive law / compositor** (a natural transformation between composite endofunctors on `Cont`). These are different kinds of object: KRU even *takes distributive laws as inputs* and never manufactures one. So there is no ready-made "monoid object over Day convolution" that equals MacBeth's `λ`. Converting `λ` into a KRU pairing would require first collapsing the compositor to a running map `T_M X × G_M Y → X × Y`, which discards the compositor content — not a reframing but a lossy projection.

**What KRU DOES give MacBeth (real, but different from route (b)):**
1. **The dual/Sweedler-dual toolkit is directly reusable.** KRU build everything (dual `G◦=G−?Id`, Sweedler dual `T•` as an equalizer in `Comon`) using exactly the **Day-convolution closed structure `−?` on `[C,C]`** — and MacBeth already owns Day convolution on `Cont` (Dirichlet tensor). So if MacBeth wants "the greatest comonad on `Cont` interacting (in the pairing sense) with `T_M`," the machinery transfers verbatim; he'd compute a *Sweedler dual of `T_M` in `Cont`*. That is a **new, well-posed question** and a plausible PROVE target — but it answers "which comonad *pairs* with `T_M`," not "does `G_M` *entwine* with `T_M`."
2. **An independent branching-obstruction theorem** (Thm 3 / Ex 9) confirming MacBeth's non-branching dichotomy via extensive-category arguments rather than H² — a strong neighbour to cite in the three-modes-of-composition connection and the effect-coeffect-arrows proof.
3. **The residual-interaction escape hatch** as a candidate for weakening MacBeth's non-branching requirement.

**Honest bottom line:** KRU is a **neighbour, not a repackaging.** It supplies (i) a Day/Sweedler-dual apparatus MacBeth can lift onto `Cont` for the *pairing* story, and (ii) a parallel branching no-go theorem. It does **not** offer a tractable monoid-object encoding of the mixed distributive law `λ` — that remains MacBeth's own (Plotkin–Turi/bialgebra) territory. Recommend: cite KRU as the Chu/Day *pairing* framework and the extensive-category branching no-go; do **not** pursue route (b) as an equivalent packaging of the entwining. If anything, the tractable spin-off is a *separate* result: "the Sweedler dual of `T_M` in `Cont`."
