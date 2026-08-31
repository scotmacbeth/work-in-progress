Subject: Re: Daily update — pausing the paper, pivoting to container theory; λ/κ note attached + answers to your five

Neil,

Catching up this morning on your five messages (Aug 1–2) — thank you, they reshape
the week and I'm glad of it. Headline: I'm **pausing the standalone effects-and-coeffects
paper** and turning back to the book / container theory, as you ask. Below: the λ/κ note
you wanted (attached), then answers to your four questions.

**The note (asked twice, UID 84 + 88).** Attached: `lambda-kappa-note.pdf` — short and
self-contained, giving the definitions leading up to λ and κ (containers and ⟦–⟧, the
effect monad T_M, the coeffect comonad G_M, then λ and κ), aimed at a colleague who knows
monads/comonads/DLs but not containers. Definitions and precise statements, not full
proofs. Forward as-is; happy to expand any section.

**Q1 — "is the intention to put λ and κ as the justification of a profunctor on
containers?" (UID 88).** Yes — exactly that. The object is the profunctor

    Arr_M(p, q) = Cont(G_M p, T_M q) :  Cont^op × Cont → Set,

contravariant in the source through the coeffect comonad G_M, covariant in the target
through the effect monad T_M. λ and κ are precisely the data that decide its *composition*:
 • κ : G_M T_M ⇒ T_M G_M is the compositor — what lets you compose Arr_M(p,q) with
   Arr_M(q,r). Arr_M is a genuine category (a promonad / arrow on Cont) ⟺ κ satisfies the
   mixed-DL axioms ⟺ M non-branching.
 • λ : T_M G_M ⇒ G_M T_M (the other orientation) is the entwining making (T_M, G_M) a
   bialgebra — the behavioural / Plotkin–Turi face — and it holds for *all* M.
So λ/κ are the justification that Arr_M is a *composable* profunctor. That is the
profunctor-on-containers statement, and it is the same object your Plotkin–Turi
enthusiasm points at: the arrow is the operational packaging, the bialgebra the behaviour.

**Q2 — "is E + A×(−) too restrictive?" (UID 85).** A fair worry; the honest picture is
that it is less restrictive than it looks.
 • The restriction bites on **one face only**. The λ/bialgebra face — the deep
   Plotkin–Turi one — holds for **every** set-monad M. Powerset, probability, lists,
   trees: all still entwine. Only the *arrow-category packaging* (κ) needs non-branching.
 • E + A×(−) is not an assumption I make but a **characterization I proved**: for
   cartesian (polynomial) monads, "the arrows compose" ⟺ "M ≅ E + A×(−)". It is the
   discovered boundary of the arrow story, not an arbitrary narrowing; = exactly the
   arity-≤1 ("non-branching") polynomial monads.
 • It is the two effects that matter most — exceptions (E) and writer/logging (A×), as you
   said — and it is the *general* such monad (arbitrary exception set with an action,
   arbitrary monoid of logs), not a toy.
 • What it excludes is precisely **branching** — forking into ≥2 leaves (nondeterminism,
   probability). Those provably *don't* form an arrow category (Pf non-associativity
   witness) but keep the λ structure.
Honest slogan: "arrows unify effects and coeffects on containers" is **unconditional as a
bialgebra (λ)**; the **arrow-category** refinement (κ) is available exactly on the
exception+writer fragment. The narrowing is a theorem about *which* effects package as
arrows, not a limitation of method.

**Q3 — the Workers "fault line / crown", plainly (UID 86).** A Worker is a stateful
container map ΔS ⊗ p → q carried with a state S. Question: combining two Workers that
share one register (state S), which of Cont's tensors survive? One dichotomy:
 • To fuse two copies of the register (collapse S × S back to S) you need an **algebra
   (monoid) on S** — but *only* when the tensor **merges** the operands' positions. ⊗
   multiplies position-fibres (B_a × D_c) and ◁ nests them: both merge, both need the
   monoid.
 • When the tensor **separates** positions into a disjoint union (categorical + and ×,
   fibres B_a ⊔ D_c) the two register-reads stay apart and **no algebra is needed** —
   composition is free.
The same merge-vs-separate line decides which structures stay closed. That is the whole
content: *merge positions ⇒ you must say how the two register-reads combine (a monoid);
separate positions ⇒ free.* It is the state-mode analogue of "branching obstructs the
arrow" and "[ω]∈H² obstructs the directed weld" — three modes, three obstruction types.

**Q4 — Weihrauch / Pradic–Price (UID 86); and I agree it is not a grant.** Weihrauch
reducibility compares *mathematical problems* by computational difficulty: P reduces to Q
if you can solve P by pre-processing the input, making one oracle call to Q, and
post-processing the answer. A "problem" is exactly a container — shapes = instances/inputs,
positions = admissible solutions — and reductions are (roughly) container morphisms. The
point that caught my eye: the Weihrauch **compositional product** ⋆ (run one problem, then
a second depending on the first's answer) **is the ◁ / substitution tensor** of containers
— a fourth independent place ◁ appears. The open thread was whether the container
derivative ∂p corresponds to a Weihrauch degree operation — unresolved, and I agree with
you it is **too narrow for a grant**; I'll keep it as a triangulation note, not pursue it.

**Plan, given your steer.** Pausing the paper. The two-feeds material (transfer, entwining
λ, arrows κ) is core "Monads and Comonads" container theory and belongs *in the book*, not
as a separate venue chase — I'll fold it there. Tell me which container-theory front you
want next (continue the Ch4 Monads-and-Comonads writeup? the indexed-container / closed-
structure analogues you anticipated? something else) and I'll aim there. And I'll watch for
your colleague's monads/comonads write-up.

More tomorrow.
MacBeth
