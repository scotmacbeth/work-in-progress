# The comonoid layer over a fibration: is "directed container = internal category" about Π, or about composition?

**MacBeth — 2026-07-14 — deep-work (prove) session.**

**Verdict up front.** The conjecture `DirCont(q) ≃ Cat(B)` (no Π) is **TRUE** — with one correction —
and it is **NOT NOVEL**: the equivalence, at objects *and* morphisms, and the precise observation that
Π is needed only for the `◁`-monoidal *packaging* and not for the equivalence, are all in
**Shapiro–Spivak, arXiv:2305.00167 (2023)**, resting on **Ahman–Chapman–Uustalu (LMCS 2014) §7**,
**Ahman–Uustalu (2016) §3.2**, **Clarke (TAC 2020) Def. 2.10 / (EPTCS 2019) Def. 12**, and
**Spivak, arXiv:1908.02202 Ex. 3.5**. This document records the honest attribution, the clean
diagram-level derivation (my one genuine contribution, expository), the computational confirmation, and
the crisp answer to Neil's question. This is the **seventh** reproof my full-PDF METHOD has caught; the
kill line is SS23 Remark 3.16.

---

## 1. The question (Neil, task C)

Over `Set`, a directed container `(S,P,o,↓,⊕)` is three equivalent things:

- a **comonad** `⟦S,P⟧X = Σ_{s:S} X^{P s}` on `Set` — needs the extension functor `⟦–⟧` (an
  exponential: **Π**);
- a **comonoid** in `(Cont, ◁, y)` — needs the composition product `◁` (an exponential: **Π**);
- an equational gadget satisfying **D1–D5** — needs *no exponential of any kind*.

> **Is the equivalence "directed container = internal category" a theorem about Π, or about
> composition?**

If it is about composition, then `◁` is a red herring we reach for only because we live in Set, and
the theorem should survive over any base with pullbacks.

## 2. The Ahman–Uustalu dictionary, in the open

Write `A := Σ_{s:S} P s`, `dom := π_P : A → S` the display projection. The dictionary is:

| container gadget | category gadget | type |
|---|---|---|
| family `P` | `dom : A → S` | display projection |
| `↓` | `cod : A → S` | any map |
| `o` | `id : S → A` | **section of `dom`** |
| `⊕` | `∘ : A ×_S A → A` | composition of composable pairs |

with `D1 = (cod∘id = id)`, `D2 = (cod of a composite = cod of the second factor)`, `D3,D4` unit laws,
`D5` associativity. **A directed container is an internal category written in family notation.** The
whole of Ahman–Uustalu is the equivalence `Fam(S) ≃ Set/S` — a *comprehension* fact, not a Π-fact.

## 3. The general definition (Π-free) and the diagram chase

Let `q : E → B` be a **full comprehension category** over `cod` (Jacobs): a cloven fibration with a
fully faithful `{–} : E → B^→` sending cartesian arrows to pullbacks. For `P ∈ E_S` write
`{P} = (π_P : S.P → S)`, a **display map**; `D` := the class of display maps (pullback-stable, contains
isos, closed under composition). Assume `B` has **no limits** beyond what comprehension supplies.

**Definition.** A *directed container over `q`* is `(S, P, o, ↓, ⊕)` with `(S,P) ∈ Cont(q)`,
`A := S.P`, `dom := π_P`, and

    o : S → A,   dom∘o = id_S           ↓ : A → S           ⊕ : A₂ → A over S,

where `A₂ := A.(↓*P)` and comprehension (CP) makes the square

        A.(↓*P) ─α─▶ A                    A₂ ≅ A ×_{↓,S,dom} A  =  composable pairs
           │π         │dom                (this pullback IS the comprehension square —
           ▼          ▼                     not an extra hypothesis)
           A ───↓───▶ S     PULLBACK

subject to D1–D5 phrased as `B`-equations. **No exponential, no `◁`, no `⟦–⟧`.**

### The chase (my clean contribution — expository)

Set `A₃ := A₂.((↓∘α)*P)` (triple composables, again a comprehension square). The internal-category
axioms are **seven** equations; D1–D5 supply exactly five, and the missing two are *free*, absorbed
into the dependent typing:

| internal category axiom | directed container | provenance |
|---|---|---|
| `dom∘i = id` | (typing of `o : Π_s P s`) | **free** — the section condition |
| `cod∘i = id` | **D1** | |
| `dom∘c = dom∘pr₁` | (typing of `⊕ : … → P s`) | **free** — codomain of `⊕` |
| `cod∘c = cod∘pr₂` | **D2** | |
| left unit | **D4** | |
| right unit | **D3** | |
| associativity | **D5** | |

**`5 + 2 = 7`.** The two "free" laws are why Ahman–Uustalu list five, not seven: externalise the type
theory and they reappear.

**The dependent casts become pullback-compatibility conditions** — the payoff of the external view.
A map *into* the pullback `A₂` exists only when its two legs agree. Checking each mediating map:

- The right-unit map `ρ = ⟨id_A, o∘↓⟩` exists ⟺ `dom∘o = id` — the section condition. ✓
- The left-unit map `λ = ⟨o∘dom, id_A⟩` exists ⟺ `↓∘o = id`, i.e. **D1**. *So D4 cannot even be
  stated until D1 is known* — precisely the silent coercion `p : P(s↓o_s) = P s` in the type theory.
- The associativity source map `u = ⟨⊕∘π₃, β⟩` exists ⟺ `↓∘⊕ = ↓∘α`, i.e. **D2**. *So D5's LHS cannot
  be stated until D2 is known* — the coercion `p'' : P(s↓(p⊕p')) = P((s↓p)↓p')`.

Every dependent transport that made the Lean formalisation painful ([[dcont-laws-need-dependent-casts]])
is, externally, just a pullback-mediation obligation discharged by an earlier law. This is the one thing
I have *not* found stated in SS23/ACU/AU; it is expository, useful for the book, not a theorem.

## 4. The correction: it is `Cat_D(B)`, not `Cat(B)`

`A = S.P`, so `dom : A → S` is a **display map**. An arbitrary internal category has an arbitrary
`dom`. Hence:

> **`DirCont(q) ≃ Cat_D(B)`** — internal categories whose *source* map is a display map — and
> `= Cat(B)` **iff** every map is display, iff `q ≃ cod_B` (Set is this case).

The asymmetry is the content: **`dom` is display, `cod` is arbitrary.** Outgoing arrows form a
family indexed by objects; incoming ones do not. Morphisms are therefore **cofunctors, not functors**
([[dcont-morphisms-are-cofunctors]]) — the same contravariance.

## 5. Computational confirmation of the dictionary

`projects/scratch/dircont_vs_cat.py`. Two **independently coded** sides — directed containers
(diagrammatic D1–D5) and internal categories in Set (classical order, classical axioms) — enumerated
over all shape-sets with a fixed out-degree profile `m`:

| profile m | (1,) | (2,) | (3,) | (1,1) | (2,1) | (1,2) | (2,2) | (3,1) | (1,3) | (3,2) |
|---|---|---|---|---|---|---|---|---|---|---|
| #DirCont | 1 | 4 | 33 | 1 | 6 | 6 | 36 | 48 | 48 | 288 |
| #Cat | 1 | 4 | 33 | 1 | 6 | 6 | 36 | 48 | 48 | 288 |

Triangulated a third way: one-object profiles `(1,),(2,),(3,)` = **labelled monoids** of order 1,2,3 =
1, 4, 33 (independent associativity+identity brute force). Dictionary solid.

## 6. Where Π actually enters — and that this is exactly SS23's own account

This is the answer to Neil's question, and it is **already published**.

**SS23, Definition 3.1:** *a polynomial in `E` is an **exponentiable** morphism.* So exponentiability is
baked into the **objects** of `Poly_E`.

**SS23, Theorem 5.6:** for a polynomial (= exponentiable `c`) in a finite-limit category `E`, ⊳-comonoid
structures on `c` ↔ internal categories with `c` as source. **Corollary 5.12:** `Comon(Poly_E) ≅`
{internal categories with **exponentiable** source, internal cofunctors}.

**SS23, Remark 3.16 — the kill line:**

> "The category `Poly_E` is isomorphic to a full subcategory of the category of **dependent lenses**
> in `E` [Spivak 1908.02202, Ex. 3.5], **whose objects are all morphisms in `E`** … While allowing
> such additional objects does not interfere with the formation of a **category**, the **monoidal
> structure** … required the objects to be **exponentiable** morphisms."

That *is* the answer: the underlying category of directed containers — hence the equivalence with
internal categories — needs only pullbacks; **only `◁` needs exponentiability (Π).** Shapiro and
Spivak wrote it in 2023.

So the complete, correctly-attributed answer:

| presentation | needs Π? | citation |
|---|---|---|
| DirCont = internal category (D1–D5, objects **and** cofunctor morphisms) | **NO** — pullbacks only | ACU §7 (def), AU §3.2 (Set obs.), Clarke Def. 12 (cofunctors), **SS23 Rmk 3.16 + Thm 5.6 + Cor 5.12** |
| `◁`-comonoid in `Poly_E` | **YES** | SS23 Def. 3.1, §4 (monoidal structure) |
| `⟦–⟧`-comonad on `B` | **YES** | classical (extension = Π) |

**The equivalence is a theorem about composition. `◁` is Π-laden packaging.** *This is settled, not
open.* Every generalisation past Set (ACU §7, von Glehn's `Poly_F`, Gambino–Kock 1.17, Hua–Xu π-clans)
carries an exponentiability/Π hypothesis for exactly one reason: to *form the monoidal structure*, never
to *express the internal category*. ACU §7 is the smoking gun — they stipulate `s` exponentiable in the
data and use it in **none** of the five laws.

## 7. The `◁`-packaging is strictly lossy off LCC (a known phenomenon; a fresh witness)

Because `Comon(Poly_E)` sees only **exponentiable-source** internal categories, it *strictly* misses
some when `E` is not locally cartesian closed. SS23 already flag this:

**SS23, Example 5.10:** in `Poly_Cat`, comonoids are exactly the double categories with **Conduché**
source functor — and "**not every double category has this property**."

I add a second, cleaner witness in a different base, and the tidy iff:

> **Observation (instance of SS23's phenomenon, base = Top).** `(ℚ, +)` as a one-object topological
> category (internal monoid in `Top`) is an internal category — hence a directed container over the
> display structure of `Top` — whose source `s : ℚ → 1` is **not exponentiable**: exponentiable objects
> in `Top` are exactly the **core-compact** spaces (Day–Kelly 1970; Escardó–Heckmann 2001), and `ℚ` is
> not locally compact, hence not core-compact. So `(ℚ,+)` is a directed container that is **not** a
> `◁`-comonoid in `Poly_Top` and lies outside SS23 Cor. 5.12.
>
> **The iff.** For a finite-limit `E`: `Cat(E) = Cat_exp(E) = Comon(Poly_E)` **iff every map of `E` is
> exponentiable, iff `E` is locally cartesian closed.** Off LCC (Top, Cat, …) the internal-category
> picture is strictly larger than the comonoid picture — witnessed by `(ℚ,+)` and by non-Conduché
> doubles.

The phenomenon is SS23's; the Top witness and the iff-LCC packaging are mine, minor.

## 8. Verification (hostile-referee pass)

- **§3 chase** vs **§5 computation**: every mediating-map obligation (`ρ,λ,u,v,w`) was walked on the
  Set data; counts match to 288. GREEN.
- **§4 correction** vs computation: profile `(3,)` supports 33 directed containers; the monoid `ℤ/3`
  is one of them; under a display class `D` = fibres of size ≤2, `ℤ/3` is an internal category *not*
  over `q` — so `DirCont(q) ⊊ Cat(Set)` for that `q`. GREEN.
- **§6 attribution**: read against the SS23 PDF at full depth (Def. 3.1 L557, Thm 5.6 L2881, Cor 5.12
  L3283, Rmk 3.16 L965, Rmk 5.7 L3129, Ex. 5.10 L3160). GREEN — the equivalence and the Π-locus are
  both theirs.
- **§7 witness**: rests on standard topology (core-compact ⟺ exponentiable object in Top; ℚ not
  core-compact). Not reproved here; cited. YELLOW→cited.
- **Negative control** (per [[associativity-is-not-coherence]]): the story is **not** symmetric —
  `cod` is not forced display — and that asymmetry is corroborated independently by
  `DCont ≅ Cof` (cofunctors, not functors). The naive symmetric `DirCont ≃ Cat(B)` with functors is
  false on both counts, with explicit counterexamples. Control fires clean. GREEN.

## 9. Gaps / honest residue

- **No new theorem.** The equivalence and its Π-locus are prior art (SS23 + ACU + AU + Clarke). Per
  Value 2 I do not claim them.
- **Genuinely mine, and only expository:** (i) the `5+2=7` law accounting and the "dependent cast =
  pullback-mediation obligation" reading of §3; (ii) the `(ℚ,+)∈Top` witness and the iff-LCC statement
  of §7. All correct, none publishable as a theorem.
- **The one live target in the vicinity** (a *different* problem, not pursued this session per the
  no-new-problems rule): the **∞-categorical** version — Kun Chen, arXiv:2601.22968, **Conjecture 7.2**,
  explicitly open; he has one direction of a nerve toward complete Segal spaces and has "not studied
  ∞-cofunctors yet." That is registry node `m6-infinity-dcont`, and it is where novelty actually lives.
