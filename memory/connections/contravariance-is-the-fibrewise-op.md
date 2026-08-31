# The contravariance of positions IS the fibrewise op

**2026-07-14. Status: the identification is `proved` (it is a computation); the claim that it EXPLAINS
`DCont ≅ Cof` is `speculative`. Grade accordingly.**

## The three sightings

Container theory has a recurring oddity that everybody notices and nobody explains. **Position maps go
backwards.**

1. **Objects.** A container morphism `(S,p) → (T,q)` is `u : S → T` *forwards* on shapes, but
   `q[u s] → p[s]` *backwards* on positions. Hence `Cont = Fam(Set^op)` — and the `op` is always
   introduced as a *bookkeeping* device, never as a *phenomenon*.
2. **Morphisms of directed containers.** `DCont ≅ Cof` — **cofunctors**, not functors. The roadmap said
   "morphisms ↔ functors" and it was **wrong**: `f♯_s : P'(f s) → P(s)` is contravariant, so a DCont-map
   is *ill-typed* as a functor. → [[dcont-morphisms-are-cofunctors]]
3. **Lenses.** A delta lens = **functor (Get)** + **cofunctor (Put)** on the same object map. The Put
   half — the backward one — is where the content is. → [[cofunctors-are-update-lenses]]

Three backward maps. Three separate explanations. That is two explanations too many.

## The identification

    Cont = Fam(Set^op) = ∫_{S ∈ Set} (Set^S)^op = ∫_{S ∈ Set} (Set/S)^op

and `S ↦ Set/S` **is the codomain fibration**. So:

> **`Cont` is the total category of the FIBREWISE OPPOSITE of the codomain fibration of `Set`.**

Generalised (von Glehn): `Cont(q) := ∫_B q^op` for any fibration `q : E → B`. Objects `(b, X ∈ E_b)`;
morphisms `(b,X) → (b',X')` = a map `u : b → b'` in the base, plus a **vertical** map `u*(X') → X` in
`E_b`. Unfold at `q = cod_Set`: the vertical map `u*(r) → p` over `S` is exactly `∀s. r[u s] → p[s]`.

**The backward position map, on the nose. It is not bookkeeping. It is the fibrewise op, and it has been
hiding in plain sight since 2003.**

⚠️ **The trap** (Streicher arXiv:1801.02927 **Ch. 5**): the naive dual `X^op → B^op` has the **wrong base**
and is generally **not a fibration**. You need the genuine fibrewise dual (spans `(α vertical, φ cartesian)`
mod vertical iso). Getting this wrong is the standard way to fumble this construction.

## The conjecture this generates (the reason the note exists)

If sighting (1) is the fibrewise op, then **sightings (2) and (3) should be the same fibrewise op one
level up** — and `DCont ≅ Cof` should not need a separate proof at all. It should be a *corollary of
where the theory lives*.

> **CONJECTURE.** Cofunctors are what functors become when you take the fibrewise opposite. `DCont ≅ Cof`
> is not a theorem about directed containers; it is a theorem about `∫ q^op`, and it will hold over any
> fibration.

This is testable and it is the **PROVE target** (`state/PROVE.md`): does *"directed container = internal
category"*, with **cofunctors** as morphisms, survive over a general fibration `q : E → B`?

**The sharp obstruction, stated honestly:** the comonoid presentation needs `◁`, and **`◁` needs Π**
(local cartesian closure). Over a fibration with pullbacks but no Π there may be no `◁` to be a comonoid
in. **But D1–D5 are equational and elementwise and mention no exponentials.** So the real question is:

> **Is "directed container = small category" a theorem about Π, or a theorem about composition?**

If composition: the theorem generalises far past the machinery that currently states it, and `◁` is a
**red herring we reach for only because we happen to live in Set.**
If Π: the failure **locates exactly which container theorems are secretly exponential.** Either way it
pays. → [[lean-comonoid-forward-done]] (M3 was already stated *internally to `Cont`*, never mentioning
`Set` — so it is **already in a language a general fibration can speak**. That was an accident; it now
looks like foresight.)

**⏰ CLOCK:** **Kun Chen, arXiv:2601.22968** (Jan 2026) does this for ∞-groupoids and concedes he only
*"partially generalizes"* Ahman–Uustalu. Someone is circling. Also Hua–Xu arXiv:2602.05689 (π-clans).

## Prior art — and the reproof I DIDN'T commit

**`Cont(q) = ∫_B q^op` is Tamara von Glehn**, *Polynomials, fibrations and distributive laws*,
**TAC 33 (2018) no. 36** (= Cambridge thesis 2015). Her §4.1 **calls it "the category of containers"** and
cites **Abbott–Altenkirch–Ghani as her LCCC special case**. Neil was almost certainly pointing at her.

I derived it independently — and then **checked before claiming.** That is the sixth reproof *avoided*,
and the first time the method has actually fired in time. The lesson holds:
**derive if you like; but grep before you say "new."** → [[read-poly-before-claiming]]

## Why this is the crown jewel and not just a tidy remark

The container literature treats the `op` as a wart — an artifact of writing `S ◁ P` rather than a fact
about the world. If the conjecture holds, the `op` is the **load-bearing wall**: it is what makes
positions contravariant, what makes DCont-morphisms cofunctors, what makes lenses have a Put, and what
makes supply-chain updates flow backwards while state flows forwards. **One `op`, four phenomena.**

And the grant reading writes itself: **Get is the fibration, Put is its fibrewise dual.** Forward state
propagation and consistent backward update are not two mechanisms bolted together — they are one
structure and its opposite. → [[cofunctors-are-update-lenses]]
