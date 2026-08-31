# For Neil / Robin — ⋉ and ⋊ are the Dialectica tensors (DJN §6 open problem answered)

**2026-07-17 (prove).** Proof file: `proofs/2026-07-17-ltimes-rtimes-dialectica.md`.
Registry: `other-cont-monoidal-tensors` (status **computed**, trustcheck green).

## The headline
Dorta–Jarvis–Niu (arXiv:2305.05655) §6 exhibit two extra monoidal structures **⋉/⋊** on `ΣΠC` and
**explicitly leave open** what they mean ("we would like to know if there are interpretations"). At
`C=1` (= Poly = Cont) they are, in container coordinates (shapes `S_p×S_q` both):
```
  (p ⋉ q)[(s,t)] = p[s]^{S_q} × q[t]^{S_p}      (p ⋊ q)[(s,t)] = p[s]^{S_q} × q[t]
```
An exponential indexed by the **opposite shape set**. That is the Dialectica hallmark, and it lands:

- **⋉ is de Paiva's Dialectica tensor.** On the homogeneous subcategory `Hmg(2) ≃ Dial(Set)` (DJN Prop
  2.13), `(p⋉q)` has direction `A^J × B^I = X^V × Y^U` — *exactly* de Paiva's tensor
  `(U,X,α)⊗(V,Y,β) = (U×V, X^V×Y^U, …)`. So **⋉ = de Paiva's multiplicative-conjunction tensor extended
  off the homogeneous slice to all of Poly.** The linear-logic content of `Dial(Set)` lives in ⋉, *not*
  in DJN's Day `⊗` (which restricts to the Gödel conjunction, challenge `X×Y`).
- **⋊ is its directed variant.** The `n`-fold closed forms make it visible: `⋉` exponentiates each
  factor by the product of *all other* shape sets (symmetric); `⋊` exponentiates each factor only by
  the shape sets **to its right** (triangular ⇒ associative but **not** symmetric). Game reading: ⋉ =
  both players respond adaptively; ⋊ = one-way dependency (one problem answered in response to the
  other, which is played blind).

**This answers DJN's own open question.** A candidate **Poly ↔ Dialectica cross-domain identification**.

## Taxonomy payoff
⋉/⋊ are **non-convolutional** (direction depends on the global opposite shape set, not the fibres — so
**Theorem A cannot reach them**: the four canonical + Day family do **not** exhaust the monoidal
structures on Cont), **non-cocontinuous** (don't distribute over `+`), and **non-closed** — the *first*
non-closed monoidal structures on Cont. Full derivation + computational checks in the proof file.

## Two honesty flags (please note)
1. **Novelty of the ⋉=Dialectica identification is NOT cleared.** This was a no-browse deep session. The
   *math* is a definition-match (proved-level); whether it's *new* needs a live arXiv check of de Paiva /
   Trotta / Spivak / Hedges / Capucci 2023–2026 and the Niu–Spivak *Poly* book Ch 3–4. DJN pose it as
   open despite knowing `Dial≃Hmg(2)`, which is encouraging, but **do not publish the novelty claim
   before the check.** (Owed next browse.)
2. **Registry graded `computed`, not `proved`**, on purpose: the identification cites de Paiva's tensor
   formula from prior study, not a source deep-read this session — the trust meet caps it there until I
   re-read de Paiva. The self-contained structural results (coordinates, symmetry/directedness,
   non-convolutional/non-closed) are `proved`.

## Loose ends (for a future session)
- Interaction table: the new ⋉/⋊ rows vs `⊗`/`◁` are only partial (a candidate **lax duoidal ⋉-over-⊗**
  law identified, coherence unchecked; ⋉-vs-◁ untouched).
- **Closure residue (Target B / `closed-day-structures` sub-Q 6.1):** reduced — "monoidal `⋆` on Set with
  `(−)⋆B` non-polynomial" *requires* `⋆` non-cocontinuous (cocontinuous Set-endofunctor = monomial), but
  `+` shows non-cocontinuous ⇏ non-polynomial. Standard `×,+,∨` all polynomial. **Conjecture: NO**
  witness exists ⇒ every convolutional tensor on Cont is left-closed. Not settled offline.

**Grant angle:** ⋊'s directedness is a natural home for *sequential/causal* compositional bounds
(cf. DJN's dynamical-systems motivation for `◁`); ⋉/⋊ are candidate new Lean-verifiable tensors.
Suggest a `/lean` target: `(Cont, ⋉, y)` symmetric monoidal (unit + associativity via the exponential
laws) — would be the first machine-checked Dialectica tensor on containers.
