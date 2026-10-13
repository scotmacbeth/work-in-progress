# Covering note for Neil — the δ-commutator lemma as a butterfly (exposition)

**To:** Neil · **CC:** Robin (always) · **Re:** a crossed-module/butterfly section for the
Strathclyde capstone & the book · **Status:** EXPOSITION — no new theorem, grades unchanged.

**QUEUED FOR WAKE DELIVERY** (WRITE phase cannot email).

Neil — a short companion note that may be the cleanest way to present the coupled-$T^2$ result at
Strathclyde. It reproves nothing; it re-reads the δ-commutator lemma (the one from the capstone,
`inventory-gerbe-couples-on-torus`, content commit `e306ae5`) in the language of crossed modules
and butterflies, so the structure that the Schreier computation hides becomes visible.

- **PDF/TeX:** `papers/inventory-gerbe-butterfly.{pdf,tex}` (9pp, compiles clean, no warnings)
- **GitHub:** https://github.com/scotmacbeth/work-in-progress/blob/main/papers/inventory-gerbe-butterfly.pdf
  (content commit `0d73790`)
- **Source material (unchanged):** the capstone proof note and its Lean witnesses, commit `e306ae5`.

## The one idea

The whole Giraud tower of the inventory gerbe is a **single crossed module**
$\partial=\mathrm{conj}\colon K\to\mathrm{Aut}\,K$. Its three invariants are exactly the cast:
$$\pi_0=\mathrm{Out}\,K\ (\text{band target}),\quad \pi_1=Z(K)\ (\text{inventory coeff}),\quad
\mathrm{im}\,\partial=\mathrm{Inn}\,K\ (\text{the hinge}).$$
So the two extensions of the tower are **not two facts**: extension (I) $1\to\mathrm{Inn}K\to
\mathrm{Aut}K\to\mathrm{Out}K\to1$ is the *cokernel* extension of $\partial$, and (II) $1\to Z(K)\to
K\to\mathrm{Inn}K\to1$ is its *kernel* extension — the two edges of one map, necessarily welded at
$\mathrm{Inn}K=\mathrm{im}\,\partial$. The shared hinge is forced, not noticed. (The note draws this
as one five-term diagram; I think it is the right opening slide.)

## What the butterfly buys

A band $\rho\colon\mathbb Z^2\to\mathrm{Out}K$ is a map into $\pi_0$. It lifts *strictly* iff it
extends to a strict morphism of crossed modules — generically it does not. It always extends to a
**weak** morphism, presented (Aldrovandi–Noohi, `0808.3627`, deep-read) by a **butterfly**: a span
whose central *waist* is a group extension $1\to K\to E\to\mathbb Z^2\to1$ with $E\to\mathrm{Aut}K$
restricting to conjugation. Then:

1. The capstone's pullback extension $E_\rho$ **is** that waist, pushed past the centre:
   $E_\rho=E/\iota(Z(K))$, so $\delta(\rho)=[E_\rho]$ is the waist class (Prop. 5.2).
2. The commutator formula is literally a commutator **in the waist**: lift the generators to
   $\hat s,\hat t\in E$; since they commute downstairs, $[\hat s,\hat t]\in K$, and
   $[A,B]=q([\hat s,\hat t])=\partial([\hat s,\hat t])\in\mathrm{Inn}K$. The bar–Koszul comparison
   $\varphi_2(e_{st})=[s|t]-[t|s]$ is exactly "read the commutator off the waist".
3. The class-$\le2$ hypothesis is read off the crossed module: $\pi_1=Z(K)$ is abelian *for free*
   (Peiffer), and class $\le2$ is precisely $\mathrm{im}\,\partial=\mathrm{Inn}K$ abelian — the
   condition on the *cokernel* edge, not imposed by hand.

## Two honest open edges (flagged as open in §7, not claimed)

- **Composition of welds.** Butterflies compose = weak morphisms compose. Whether a composite weld's
  obstruction is the composite of waist classes is a clean question the language *poses*; I did not
  settle it. Candidate next PROVE node (ties to the ZS-overlay lane).
- **Beyond class $\le2$.** Dropping it makes $\mathrm{Inn}K$ nonabelian, so edge (I) leaves the
  abelian-kernel world and the waist class becomes a genuinely nonabelian (Breen bitorsor) datum —
  exactly what the Aldrovandi–Noohi formalism was built to carry. The right entry point for the
  long-standing nonabelian-gerbe extension of the inventory lane.

No action needed — this is for the capstone/book and the mini-course. If you'd like it folded in as
a section of the capstone rather than a standalone companion, say so and I'll merge it.

— MacBeth
