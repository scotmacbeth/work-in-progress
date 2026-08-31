# Workers closure column completed — × CLOSED (conjecture flipped), ◁ obstructed

**For:** Neil, Robin. **Date:** 2026-08-21 PROVE. **Proof:** `proofs/2026-08-21-workers-x-closed-lhd-obstructed.md`.

Neil — you asked us to put more effort into Workers closedness (applied-half, toward Spivak's
double monoidal cat). Here's the resolution of the two open cells, and the × answer is the
**opposite** of what we'd conjectured.

`Workers_S(a,q) := Cont(ΔS⊗a, q)`, ΔS = codiscrete category `(S, s↦S)`, ⊗ = Dirichlet.

## 1. Workers IS ×-closed (we had conjectured NOT).
Internal hom:
  **`[p⇒q]_× = ∏_{s_p} q ◁ (y ⊕ c_{S×P_p(s_p)})`,   `⟦[p⇒q]_×⟧Y = ∏_{s_p} ⟦q⟧(Y + S×P_p(s_p))`.**
Reduction (Yoneda): `Workers_S(a×p,q) ≅ Cont(a, ([ΔS,q]_⊗)^p)` via ⊗-closure then Cont's CCC;
`Workers_S(a,E) ≅ Cont(a,[ΔS,E]_⊗)`; so closed iff `([ΔS,q]_⊗)^p ∈ image[ΔS,−]_⊗`. It is —
key lemma `⟦[ΔS,r]_⊗⟧X = ⟦r⟧(S×X)^S` plus `(∏B_i)^S=∏B_i^S` make E work.

**The point:** the "state entangles the curried argument" intuition was *right* — the hom is
Cont's cartesian exponential with each argument fibre inflated `P_p ↦ S×P_p` — but that
entanglement is **representable**, so it does not obstruct closure. Prior naive test (1296≠256)
just used the wrong candidate `q^p`; the true hom is bigger.

**Uniform reason (nice for the write-up):** for any Day-convolution tensor `⊙_⋆` with Cont
`⊙_⋆`-closed, Workers is `⊙_⋆`-closed iff `S×(A⋆K)` is a functor of `S×A`. Holds for `⋆=+`
(→ `×`, since × distributes over +) and `⋆=×` (→ `⊗`, since × associates). So **both** native
tensors close — one structural mechanism. This is the "closed" row of the type-hierarchy table.

## 2. Workers is NOT ◁-closed — and it's inherited from Cont, not a state effect.
For p with ≥2 shapes the would-be `(−)◁p` internal hom is forced to be
  `⟦H⟧(A) = ∏_{γ:A→S_p} ⟦R⟧(Σ_{i}P_p(γ i))`  (R=[ΔS,q]_⊗),
which is **non-polynomial**: `|⟦H⟧([n])|` grows double-exponentially (`≥2^{2^n}`), while every
container has `|⟦H⟧(n)| ≤ (#shapes)·n^K`. Sharpest witness with no state (R=Id, p=(2,1)):
`|H([n])| = n^{2^n} = 0,1,16,6561,…` — `|H(1)|=1` forces a single arity-4 shape, predicting
`|H(3)|=81 ≠ 6561`. So **Cont itself has no right adjoint to `−◁p`** — it carries only a
◁-*co*closure (left adjoint, Niu–Spivak §6), never a ◁-closure. Workers inherits the obstruction;
single-shape p is the only escape (then `T_R = R◁(|P_p|·y)`, polynomial).

## Grant framing
Closure column of the Workers table now reads: **⊗ closed · × closed · ◁ obstructed.** The
`separate-vs-merge` fault line survives but is *re-drawn*: it's not "merge ⟹ not closed" (⊗
merges yet closes) — it's "Day-convolutional (⊗,×) ⟹ closed; genuine composition ◁ ⟹ not even
closed in Cont." Workers as a graded *reader* monad `R⊸−` is ×- and ⊗-closed; the internal homs
are explicit and finite-verified. Ready for the applied-half section toward Spivak's double
monoidal category.

Verified: `scratch/workers-type-hierarchy/{xclosed_resolve,lhd_cardinality,lhd_probe}.py`.
Registry: `workers-type-hierarchy.json`, nodes `C2-product-CLOSED-resolved` (proved),
`C3-substitution-NOT-closed-resolved` (proved). Validates.
