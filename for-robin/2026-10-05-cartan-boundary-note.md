# Shipped: "The container derivative has no fiberwise negation" (8pp) — 2026-10-05

**What it is.** The Cartan-boundary note, typeset from the 10-05 PROVE result. The
sequel to the uniqueness note. Existence and uniqueness of ∂ are banked; this one
*delimits* the program: containers have a first-order tangent calculus but **not** a full
Cartan calculus.

**Main theorem (negative).** The additive bundle of $T=(-)\lhd D$ on finite-support
polynomial functors is a bundle of commutative monoids with **no fiberwise additive
inverses** (fibers are free ℕ-modules on holes). Hence $(\SPoly,\partial)$ is not Rosický,
carries **no scalar ring object** in the Aintablian–Blohmann sense, and the full Cartan
calculus (d, ι, L, Chevalley–Eilenberg; cubical CDGA) does **not** descend. Only the
subtraction-free ℕ-scalar fragment survives. The rig ℕ is the knife — same one as the
uniqueness converse.

**Where.** `github.com/scotmacbeth/work-in-progress`
- paper: `papers/container-cartan-boundary.tex` / `.pdf`
- content commit **5a33e34** (stamped on page 1; stamp commit 7cbb523, pushed to `main`)
- proof: `proofs/2026-10-05-spoly-negation-obstruction.md`; registry
  `proofs/registry/cartan-scalar-object-spoly.json` (root = **proved**)
- Lean core: `lean/2026-10-05-spoly-negation-obstruction.lean` (`[propext, Quot.sound]`)

**Two independent witnesses (both in the paper).**
1. §4 — counting-functor transport: any negation would push through $N:\SPoly\to\PolyN$ to
   a negation of $\PolyN$, but $v+g(x,v)=0$ has no ℕ-polynomial solution. Airtight; uses
   only that $N$ *preserves* the ops in the axiom, not faithfulness.
2. §5 — explicit fibers: $p=y$ (fiber ℕ, unit 1 no inverse), $p=y^2$ (fiber ℕ², (1,0) no
   inverse). The Cartan-facing presentation.

**What I'm least sure about (referee here, please).**
- **Lemma A** (scalar ring object ⟹ Rosický negation) and **N-functoriality** are
  pen-and-paper — Lean certifies only the *arithmetic* obstruction (no-negation-over-ℕ,
  free-ℕ-module fibers). Stated as such in §6. Lemma A is AB Prop 4.4 reproved from the
  module axioms; I believe it but it's not formalised.
- **Cockett 2012** ("Can you Differentiate a Polynomial?") is cited **secondhand** — via
  the community relay of the unpublished FMCS slides, with Cruttwell's species=tangent-
  *bicategory* caveat. Labelled as such in the bibliography and conclusion. If you or Neil
  have the actual slides, I'd like to upgrade this.

**Candidate status:** `publishable-result` (your call to queue; I don't submit). Fits the
Strathclyde mini-course (Oct 13–16, Cruttwell + Neil) as the slide right after uniqueness.

**Deferred to the next comms phase (this was a no-email write session):** email the PDF to
Rick with a short covering note (he's the sequel's natural reader), CC you; and the daily
update to Neil.

**Sequel / open question the theorem exposes:** fiberwise group completion ℕ→ℤ. Does
group-completing the tangent fibers land in a category of virtual/ℤ-containers that *is*
Rosický, so the full Cartan calculus descends there? That's the honest route to forms, and
this cycle's PROVE target (`proofs/2026-10-06-virtual-container-cartan.md` + Lean
`2026-10-06-virtual-container-negation-exists.lean` already exploring it).
