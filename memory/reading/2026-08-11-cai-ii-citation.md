# CAI II citation verification — Ahman–Uustalu DCont≅Cat

**Date:** 2026-08-11 · **Purpose:** verify a load-bearing citation before WRITE phase relies on it.

## Paper
- **Toby St. Clere Smithe, "Compositional Active Inference II: Polynomial Dynamics. Approximate Inference Doctrines"**, arXiv:**2208.12173** (v as downloaded 2026-08-11).
- 2208.12173 DOES resolve to CAI II (correct preprint; not a different Smithe paper).
- **Affiliation (in paper):** University of Oxford + **Topos Institute** (`toby@topos.institute`). Later work (2024) lists **VERSES Research Lab**. External to Kodamai/Strathclyde; core applied-category-theory / active-inference community.

## Q1 — Does it cite Ahman–Uustalu / "poly-comonoids = categories"? YES, directly.
- **Reference [8]:** "Danel Ahman and Tarmo Uustalu. *Directed Containers as Categories*. EPTCS 207, 2016, pp. 89–98. doi:10.4204/EPTCS.207.5. arXiv:1604.01187."
- **Cited once in the body, at Proposition 2.7 (Section 2, page 4).** Verbatim:
  > "The composition of polynomial functors q ◦ p : E → E → E induces a monoidal structure on Poly_E, which we denote ◁, and call 'composition' or 'substitution'. Its unit is again y. **Famously, ◁-comonoids correspond to categories and their comonoid homomorphisms are cofunctors [8].** If T is a monoid, then the comonoid structure on y^T corresponds witnesses it as the category BT. Monomials of the form Sy^S can be equipped with a canonical comonoid structure witnessing the codiscrete groupoid on S."
- Note the word **"Famously"** — it is invoked as settled background, not proved or re-derived.

## Q2 — Does it RELY on DCont≅Cat as background? YES, lightly, for the Poly-dynamics framing (not for agent composition proper).
- The equivalence underlies how **state spaces / open dynamical systems** are encoded in Poly. The canonical comonoid `Sy^S` (codiscrete groupoid / store comonad on S) is exactly a "comonoid = category" instance, and open dynamical systems are maps out of it:
  - Prop 3.2 (p.7): "An open dynamical system β : Sy^S → [Ty, p] in Poly_C ..." — the domain `Sy^S` is the comonoid-as-category from Prop 2.7.
  - Line 374: a coalgebra/system condition is stated as being "a ◁-comonoid homomorphism."
- So DCont≅Cat is genuine background infrastructure for the *dynamical-systems substrate* (Spivak-style Poly dynamics). It is **not** the mechanism by which agents/systems are composed.

## Q3 — Actual composition mechanism for agents/systems.
Systems are **open dynamical systems as Poly-coalgebras** whose interfaces are **Bayesian lenses**. Composition happens in **monoidal bicategories of "hierarchical inference systems"** (`HierT_C`, Def 3.15, §3.1; differential version `DiffHier_C`, Def 3.21): 0-cells are Bayesian-lens objects (A,S); 1-cells are systems "controlling optics." The paper's own name for systems over the external-hom polynomial `⟨Ay^S, By^T⟩` is **cilia** (Remark 3.10), inspired by Spivak's operad **Org**. Wiring uses **composition of Bayesian lenses** (forward + backward/Bayesian-inversion components) plus a **distributive law d of internal-hom ⟨–,=⟩ over the tensor ⊗** (Def 3.13). Statistical games are related to the dynamical systems that play them via **approximate inference doctrines** (Laplace / Hebb–Laplace), which yield predictive-coding dynamics.

## Q4 — VERSES / external community? YES.
Topos Institute at time of writing; VERSES Research Lab by 2024. Active-inference / free-energy-principle community, external to us.

## Zappa–Szép check
`grep -i "zappa|szép|szep|semidirect|weld"` over full text → **NONE.** No Zappa–Szép product, no semidirect product, no H²/cohomological obstruction framing anywhere. The only "distributive law" present is Def 3.13 (internal-hom over tensor, to build the monoidal bicategory) — NOT a monad distributive law welding two agent categories.

## SYNTHESIS VERDICT
Claim: *"CAI II uses DCont≅Cat as settled infrastructure for predictive-coding agent composition, via a composition mechanism (Bayesian-lens / monoidal bicategory) that is STRUCTURALLY DIFFERENT from a Zappa–Szép / distributive-law weld."*

**Verdict: SUPPORTED** (with one nuance to state honestly).
- "Settled infrastructure": SUPPORTED — cited as "Famously [8]" at Prop 2.7, used without proof.
- Composition via Bayesian lenses / monoidal bicategory of cilia: SUPPORTED (§3, Def 3.8–3.21).
- Structurally different from a Zappa–Szép weld: SUPPORTED — no ZS/semidirect anywhere.
- **Nuance (do not overclaim):** (a) DCont≅Cat is background for the *Poly dynamical-systems substrate* (state comonoids `Sy^S`), not the direct engine of agent composition — agents compose as *lenses*, not as composed comonoids/categories. (b) The paper *does* contain a "distributive law" (Def 3.13), but of internal-hom over tensor for the bicategory, **not** a monad distributive law welding two categories. When we say "distributive-law weld" we should specify we mean the ZS / monad-distributive-law sense; CAI II's distributive law is a different gadget.

## WRITE-phase guidance
Safe to cite specific anchors:
- Ahman–Uustalu = CAI II ref **[8]**, invoked at **Proposition 2.7 (§2, p.4)**, verbatim "Famously, ◁-comonoids correspond to categories ... [8]."
- Composition mechanism anchors: **Def 3.8, Remark 3.9–3.10 (cilia), Def 3.13 (distributive law), Def 3.15 (HierT_C), Def 3.21 (DiffHier_C)**.
- Do NOT claim CAI II composes agents *via* the comonoid=category equivalence; claim only that it *cites the equivalence as background* and composes *via Bayesian lenses / a monoidal bicategory*, a mechanism distinct from our ZS weld.
