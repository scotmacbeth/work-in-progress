---
name: cofunctor-delta-lens-citeready
description: "Cite-ready precise statement of delta lens = functor + cofunctor (Clarke), with axioms, theorem numbers, arXiv ids, BibTeX, and the DCont ≅ Cof slot-in."
date: 2026-06-10
metadata:
  node_type: memory
  type: reading
---

# Delta lenses as functors + cofunctors — the precise, citable statement

Purpose: turn the slogan *"a delta lens is a functor (Get) plus a cofunctor (Put)
sharing an object map, with a section condition f∘φ = id"* into exact definitions,
exact theorem statements, and canonical citations. **Everything below labelled
[SOURCE] is verbatim-faithful to the primary papers; [MACBETH] is our own extension.**

Primary sources, both read in full (PDFs in `/home/agent/papers/`):
- **[C20]** B. Clarke, *Internal lenses as functors and cofunctors*, EPTCS 323 (2020) 183–195, arXiv:**2009.06835**. (ACT 2019 proceedings.)
- **[C22]** B. Clarke, *Delta lenses as coalgebras for a comonad*, arXiv:**2108.00390** (v2, 1 Mar 2022).
- **[AU17]** D. Ahman & T. Uustalu, *Taking Updates Seriously*, CEUR-WS 1827 (2017) 59–73. (= ref [4] in [C22], ref [2] in [C20].)
- **[JR13]** M. Johnson & R. Rosebrugh, *Delta Lenses and Opfibrations*, EASST 57 (2013) — origin of the delta-lens-as-semi-monad-algebra characterisation.

---

## 1. Exact definition of a delta lens (the three axioms) [SOURCE: C22, Def. 4 / unpacked p.4]

A **delta lens** `(f, φ): A ⇌ B` between (small) categories consists of:
- a **Get** functor `f : A → B`;
- a **Put** / **lifting operation** `φ` assigning to each pair `(a ∈ A, u : f a → b ∈ B)`
  a morphism `φ(a,u) : a → a'` in `A`,

satisfying the **three delta-lens axioms** ([C22] p.4, exactly):

1. **(PutGet)**  `f · φ(a,u) = u`;
2. **(PutId)**   `φ(a, 1_{f a}) = 1_a`;
3. **(PutPut)**  `φ(a, v∘u) = φ(a', v) ∘ φ(a,u)`, where `a' = cod(φ(a,u))`.

These are the morphism-level analogues of the classical PutGet / GetPut / PutPut
state-based lens laws.

> **DISCREPANCY FLAG.** The loose slogan said the section condition is "**f∘φ = id**".
> That is **wrong as stated**. The actual axiom is **(PutGet): f·φ(a,u) = u**, i.e.
> applying Get to a lifted update returns *the original update `u`*, **not** an identity.
> "f∘φ = id" would only be right read as "Get∘Put = id on the slice of anchored
> updates over each `a`" — a section-of-the-fibre statement — never as a plain identity.
> The clean diagrammatic version of this section condition is in §2 (diagram (11)/(12) of [C20]).

### Cofunctor, standalone [SOURCE: C22, Def. 3]

A **cofunctor** `φ : A ⇸ B` consists of an object map `φ₀ : A₀ → B₀` together with a
lifting operation `φ` sending `(a, u : φ₀a → b)` to `φ(a,u) : a → a'` in `A`, satisfying:
1. `φ₀ cod(φ(a,u)) = cod(u)`;
2. `φ(a, 1_{φ₀a}) = 1_a`;
3. `φ(a, v∘u) = φ(a',v) ∘ φ(a,u)`, `a' = cod(φ(a,u))`.

Equivalently ([C22] Def. 3, the **span form**): a cofunctor is a span of functors
`A ←φ— X —φ̄→ B` with `φ` **bijective-on-objects** and `φ̄` a **discrete opfibration**.
Note: a cofunctor is **NOT** a contravariant functor ([C20] p.188, explicit warning).

> So: **cofunctor = the Put data alone** (axioms 1–3 above), i.e. a delta lens
> *minus the information of how Get acts on morphisms*. ([C22] p.2.)

---

## 2. The decomposition theorem: delta lens = Get functor + Put cofunctor on a shared object map [SOURCE]

**[C20] Definition 19 + Corollary 20** (internal, in any category 𝓔 with pullbacks):

> An **internal lens** `(f, φ): A ⇌ B` is an internal **functor** `f : A → B` together
> with an internal **cofunctor** `φ : B ⇸ A`, **such that `φ₀ = f₀`** (shared object map)
> and the compatibility diagram (11) commutes; equivalently diagram (12): **`f₁ ∘ φ₁ = φ̄₁`**.
> **(Cor. 20)** Every internal lens is a commuting triangle of internal functors
> `A ←φ— Λ —φ̄→ B` with `f∘φ = φ̄`, where `φ̄ : Λ → B` is a discrete opfibration and
> `φ : Λ → A` is identity-on-objects.

The shared object map is the exact realisation of "same object map" in the slogan.
The exact compatibility/section condition is **`f₁∘φ₁ = φ̄₁`** ([C20] (12)) — equivalently,
in element form ([C20] Ex. 24 / [C22] PutGet): **`f·φ(a,u) = u`**.

**[C20] Example 24** (the landing in **Set**): `Lens(Set) = ` the category of **d-lenses**
(= delta lenses) of Johnson–Rosebrugh [JR13]. Get is the functor `f : A → B`, Put is the
cofunctor `φ : B ⇸ A`, and `φ₁(a, u: fa→b) = (φ(a,u): a → p(a,u))`. This is the precise
sentence that makes "a delta lens IS a functor-plus-cofunctor" a theorem, with the
section/compatibility being PutGet. **[C20] Def. 4 of the later paper restates this
diagrammatically: a delta lens is a commuting triangle `A←φ—X—φ̄→B` with `φ`
bijective-on-objects and `φ̄` a discrete opfibration ([C22] Def. 4 / [C20] Cor. 20).**

---

## 3. "DLens(B) is comonadic over Cof(B)" — exact form [SOURCE: C22]

[C22] fixes a base / view category `B` and forms:
- **Cof(B)** ([C22] Def. 5): objects = cofunctors `φ : A ⇸ B` *into* `B`; morphisms (3) =
  functors `h : A → C` between sources preserving the chosen lifts from `B`.
- **Lens(B)** ([C22] Def. 7): the **slice category** `Cof(B)/1_B`, where `1_B` is the
  trivial (identity) cofunctor on `B`. **Proposition 6**: a delta lens with view `B`
  is exactly a morphism in `Cof(B)` into the trivial cofunctor `1_B`.

There is a canonical **forgetful functor `L : Lens(B) → Cof(B)`** sending a delta lens
to its underlying Put cofunctor.

- **[C22] Lemma 8.** `L` has a right adjoint `R : Cof(B) → Lens(B)` — `R` builds the
  **cofree delta lens** on a cofunctor (the Ahman–Uustalu construction [AU17, §3.2 of ref [3]],
  via the pullback (6)–(7) against the codiscrete-category right adjoint `(̂-) : Set → Cat`).
- **[C22] Theorem 9.** **The forgetful functor `L : Lens(B) → Cof(B)` is comonadic.**
  I.e. `Lens(B) ≃ coAlg(LR)` for the comonad `G = LR` on `Cof(B)`. A coalgebra structure
  on a cofunctor `φ : A ⇸ B` (diagram (11)) is forced (by counit/comult compatibility) to be
  exactly the data of a **functor `f : A → B` with `f∘φ = φ̄`** — i.e. a delta lens
  `(f, φ): A ⇌ B`.

> So the precise statement is: **the comonad is `LR` on the category `Cof(B)` of cofunctors
> over the base `B`; the functor made comonadic is the Put-forgetting `L : Lens(B) → Cof(B)`;
> the cofree right adjoint `R` is the Ahman–Uustalu cofree-delta-lens construction.**
> The "coalgebra structure map = the section condition" intuition is correct, but the section
> condition is **PutGet (`f·φ = u`)**, realised as the coalgebra map, NOT a bare `f∘φ = id`.

This precise-form note **corrects** the earlier browse memo (browse-2026-06-09) which wrote
the result as `DLens(B) comonadic over Cof(B)` with "`f∘φ₁ = id`": the comonadicity is right,
the section condition wording was loose (see flag in §1).

---

## 4. Landing on directed containers / DCont ≅ Cof [MACBETH extension, anchored to SOURCE]

[SOURCE] [AU17] introduced **update–update lenses** as **morphisms of directed containers**,
and showed (same paper) these are equivalent to **cofunctors** between the induced categories;
they spell out how, in directed-container notation, **delta lenses are cofunctors with extra
structure**. [C22] (intro, p.1) cites exactly this: *"In 2017, Ahman and Uustalu introduced
update–update lenses as morphisms of directed containers, which are equivalent to cofunctors
between categories."*

[MACBETH] This is precisely the variance MacBeth proved on 2026-06-09:
**DCont ≅ Cof** as an isomorphism of categories, where a directed-container morphism `(f, f♯)`
has **position map `f♯_s : P'(fs) → P(s)` contravariant**, and conditions (M0)–(M2) are
*literally* the cofunctor laws (C0)–(C2). Reading off the dictionary:

- directed container ↔ category (object level, Ahman–Uustalu *Directed containers as categories*);
- **DCont-morphism = cofunctor = the Put (lifting) half of a delta lens.** [matches §1–§3]
- The covariant variant (position map `P(s) → P'(fs)`, conditions N0–N2) recovers **functors**
  — i.e. the Get half. So the functor/cofunctor split of a delta lens ([C20] Def. 19) is
  *exactly* the covariant/contravariant split on container position maps. The "shared object
  map" condition `φ₀ = f₀` ([C20] Def. 19) is the requirement that Get and Put share the same
  underlying shape/object assignment on the container.

**Slot-in sentence for the grant:** *A delta lens (Clarke, arXiv:2009.06835, Def. 19; arXiv:2108.00390,
Def. 4) is a Get functor together with a Put cofunctor on a shared object map, the two related by
the PutGet section condition `f·φ(a,u)=u`. Under MacBeth's `DCont ≅ Cof` isomorphism, the Put
cofunctor is exactly a directed-container morphism (contravariant on positions), and Clarke's
comonadicity `Lens(B) ≅ coAlg(LR)` over `Cof(B)` (arXiv:2108.00390, Thm. 9) thereby expresses
delta lenses internally to the directed-container world.*

---

## 5. BibTeX

```bibtex
@inproceedings{clarke2020internal,
  author    = {Bryce Clarke},
  title     = {Internal lenses as functors and cofunctors},
  booktitle = {Proceedings of the Third International Conference on
               Applied Category Theory (ACT 2019)},
  series    = {Electronic Proceedings in Theoretical Computer Science (EPTCS)},
  volume    = {323},
  pages     = {183--195},
  year      = {2020},
  doi       = {10.4204/EPTCS.323.13},
  eprint    = {2009.06835},
  archivePrefix = {arXiv},
  primaryClass  = {math.CT}
}

@misc{clarke2022deltalenses,
  author = {Bryce Clarke},
  title  = {Delta lenses as coalgebras for a comonad},
  year   = {2022},
  eprint = {2108.00390},
  archivePrefix = {arXiv},
  primaryClass  = {math.CT},
  note   = {arXiv:2108.00390}
}

@inproceedings{ahman2017updates,
  author    = {Danel Ahman and Tarmo Uustalu},
  title     = {Taking Updates Seriously},
  booktitle = {Proceedings of the 6th International Workshop on
               Bidirectional Transformations (Bx 2017)},
  series    = {CEUR Workshop Proceedings},
  volume    = {1827},
  pages     = {59--73},
  year      = {2017},
  url       = {http://ceur-ws.org/Vol-1827/paper11.pdf}
}

@article{johnson2013delta,
  author  = {Michael Johnson and Robert Rosebrugh},
  title   = {Delta Lenses and Opfibrations},
  journal = {Electronic Communications of the EASST},
  volume  = {57},
  year    = {2013},
  doi     = {10.14279/tuj.eceasst.57.875}
}

@phdthesis{clarke2018thesis,
  author = {Bryce Clarke},
  title  = {Characterising Asymmetric Lenses using Internal Categories},
  school = {Macquarie University},
  year   = {2018},
  note   = {http://hdl.handle.net/1959.14/1268984}
}
```
