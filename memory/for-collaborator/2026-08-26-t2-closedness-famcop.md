# T2 done: closedness of the Dirichlet tensor `⊗` on `Fam(C^op)` — and the pre-registered prediction was wrong (in an interesting way)

**MacBeth → Neil/Robin, 2026-08-26 (PROVE session).** Answers UID 124 "try and do T2 generally."
Full proof: `proofs/2026-08-26-t2-day-closedness-famcop.md`. Registry (valid, `proved`):
`proofs/registry/t2-day-closedness-famcop.json`.

## The one-paragraph version

Closedness of the parallel/Dirichlet tensor `(S,P)⊗(T,Q)=(S×T,(P_s⊗Q_t))` on `Fam(C^op)` is
**exactly a familial-representability condition** (Diers), which splits into two *independent*
conjuncts:
- **(A)** each `Z ↦ C(A, Z⊗Q)` is familially representable (a sum of corepresentables);
- **(B)** the product `∏_{t∈T}` of the resulting corepresentables is representable, i.e. the
  coproduct `∐_{t∈T} N_t` exists in `C`.

Cartesian bases (`Set`, toposes, `Set×Set`) satisfy both **for free** — the diagonal splits
`C(A,Z×Q)=C(A,Z)×C(A,Q)` and coproducts do the rest — so `⊗` is closed there, with the explicit
`Set`/`Poly` Dirichlet internal hom (Niu–Spivak Ex 4.78) recovered as the instance. Over a
**linear** base the two conjuncts **fight**: (A) over `Vec` holds *iff the position `Q` is
finite-dimensional* (Lemma 3.1 — dualizability is forced), while (B) for infinite index needs a
coproduct that *leaves* `Vec_fd`.

## The headline (and the honest correction)

**`⊗` is closed on `Fam_fin(Vec_fd^op)` (finite shapes, fd positions) — and on NEITHER
`Fam(Vec_fd^op)` NOR `Fam(Vec^op)`.**

The PROVE brief predicted "closedness HOLDS over full `Vec`, FAILS over `Vec_fd`." That is **wrong**,
and the way it's wrong is the content: it fails over *both*, by **dual** mechanisms —
- over `Fam(Vec_fd^op)`: **conjunct (B)** breaks. Witness `T=ℕ`, `Q_t=k`, `R=M=k`:
  `Φ(Z)=∏_ℕ|Z|=|Z|^ℕ=Vec(k^{(ℕ)},Z)`, whose only representative `k^{(ℕ)}` is infinite-dimensional.
- over `Fam(Vec^op)`: **conjunct (A)** breaks. Witness `Q=k^{(ℕ)}` (infinite-dim position):
  `Z↦|Z⊗Q|` fails to preserve an infinite product, so it isn't familially representable.

The brief saw (B) and missed that full `Vec` re-introduces failure through (A). The **load-bearing
conjunct**, named: the internal-hom position `∐_{t}M_{ρ(t)}⊗Q_t^*` must *simultaneously* make sense
(each `Q_t` dualizable ⟹ fd) and *exist* (the coproduct present) — jointly true over `Vec` only on
the finite/fd corner.

## What I'd flag for you, Neil

1. **T2 and T1 are independent axes.** `Set×Set` *closes* `⊗` (cartesian) yet its extension `⟦−⟧`
   is *not* full (T1, disconnected unit). Closedness of the tensor ≠ fullness of the extension.
2. **It is NOT the `∐⊊⊕` extensivity seam in disguise** (I checked, §4). T1-fullness is "the unit
   `C(I,−)` doesn't preserve `⊕`"; T2 is "the *category* isn't cocomplete (over Vec_fd)" *or* "the
   *monoidal* structure lacks duals (over Vec)". Same origin (external shapes / internal positions),
   two different structural resources (duals, coproducts).
3. **Day LNM 137 Thm 3.3 is the right tool but does not apply off-the-shelf** — the enriched domain
   `A=C` is *large*, so Day's small-`A` branch fails and the internal hom is an end that needn't
   land back in `Fam(C^op)`. The *representability refinement* (does it land?) is precisely the T2
   delta, and it is exactly what Dorta–Jarvis–Niu `2305.05655` omit. I did the reduction elementarily
   (def of adjunction + Set-distributivity `∏∐=∐∏` + connectedness of corepresentables), so nothing
   leans on Day as a black box; Day is cited for placement only.

## Status / where it's soft

**Proved:** the reduction (Thm 1.1), both sufficient regimes with explicit internal homs (Thm
2.1/2.3), the Vec single-factor dualizability iff (Lemma 3.1), the linear dichotomy (Thm 3.2).
Verified 2000/2000 random small families over `Vec_fd` and over `Set`.

**Gaps (honest):** (i) I have the exact *iff* (Thm 1.1) but haven't *characterized* the general
class of non-cartesian, non-rigid closed `C` that satisfy it — candidate: "`-⊗Q` a
parametric-right-adjoint for every `Q`." (ii) Lemma 3.1's dualizability-necessity is proved over
`Vec` (field-flatness); whether it's general to additive closed bases is open. (iii) `◁`-coclosure
(the secondary target) untouched — largely known from position-op/`Lan`, fragile survival criterion
still conjectured.

**Question back to you:** the practitioner reading of Thm 3.2 is *"higher-order (curried) parallel
composition of resource-graded processes exists exactly when the resource base is cartesian, or
finite-dimensional-linear with finitely many branches"* — i.e. **linear (quantum/probabilistic)
resource types resist internal-hom unless finite**. Is that the framing you want for the grant's
applications section, or do you want me to push gap (i) to a full classification first?
