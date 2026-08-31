# Day 1 — The shape/position trick

*(Draft one-pager for Alastair Poole. Pilot reader for the book. Send once Robin/Neil
supply his email address — requested in the 13 Jun daily.)*

---

Subject: **Containers, day 1 — the shape/position trick**

A container is a deceptively small idea with a long reach. Here it is.

Take any data structure — a list, a binary tree, a pair, a fixed-size-7 array. Strip
away what it *contains* and ask only about its *form*. Two questions capture the form
completely:

1. What are the possible **shapes**? (For lists: one shape per length — the empty
   shape, the one-element shape, …. For binary trees: one shape per tree silhouette.)
2. Given a shape, where can data **sit**? Call these the **positions** of that shape.
   (A length-3 list has 3 positions; a particular tree shape has one position per node.)

That is a container: a set of shapes `S`, and for each shape `s` a set of positions
`P(s)`. We write it `S ◁ P`. Lists are `ℕ ◁ (n ↦ {0,…,n−1})`. Pairs are
`1 ◁ {left, right}`. A "structure of this form holding elements of type `X`" is then
just: *pick a shape, then label every position with an element of `X`* — i.e. a shape
`s` together with a function `P(s) → X`.

The slogan: **a container separates the branching structure (shapes and positions)
from the payload (what fills the positions).** Everything else follows from taking that
separation seriously.

Why does it matter? Because that one function `P(s) → X` is enough to recover the
*whole* data structure as a **functor**. To map `f : X → Y` over your data, just
post-compose: `(P(s) → X) ⤳ (P(s) → Y)`. No special-casing lists versus trees versus
arrays — they are all "shape + labelling." The functor you get,

  `⟦S ◁ P⟧ X = Σ_{s ∈ S} (P(s) → X)`,

is the **extension** of the container. It is the bridge between the combinatorial
picture (shapes, positions) and the type you actually program with. The remarkable
theorem behind all of this — that *every* map between two such functors comes from a
map of shapes-and-positions, nothing is lost — is what makes the bridge two-way. (More
on that another day.)

The punchline I will build toward over the coming days: an astonishing amount of
structure — how data structures **compose**, how you **differentiate** them (one-hole
contexts, genuinely the derivative from calculus), and the difference between a plain
data structure and a *navigable* one (a small category wearing a disguise) — is already
visible in this tiny shape/position split, once you know where to look.

Tomorrow: how containers *compose*, and why composition is where it gets interesting.

— MacBeth
