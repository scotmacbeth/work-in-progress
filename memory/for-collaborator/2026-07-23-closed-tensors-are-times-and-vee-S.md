# Closed convolutional tensors on Cont = ⊗ and the ▷_S family (modulo one gap)

MacBeth, 2026-07-23. For Neil / Robin. Full write-up:
`proofs/2026-07-23-closed-convolutional-tensors-classification.md`.

## The claim
Following yesterday's non-vacuity (the collapse tensor is convolutional but not left-closed),
I classified the **left-closed** convolutional tensors. For symmetric monoidal `(Set,⋆,I)` with
`R_B=(−)⋆B` polynomial for all `B`:

> **modulo excluding infinite arities, the only ones are `⋆=×` (→ `⊗`) and `⋆=∨_S` (→ `▷_S`).**
> `∨_S B = A + A×S×B + B`; `∨_∅ = +` gives the product `×` on Cont.

So the three closures you already knew (`⊗`, `×`, `▷_S`) are (conjecturally) the **complete list** —
not luck. The census of Theorem A becomes effective on the closed locus.

## How the proof goes (four clean moves)
1. **Unit is small, `|I|≤1`.** `R_1(I)=I⋆1=1` + polynomial normal form forces it; else a one-line
   contradiction with the unit. (Corroborated: no unit-≥2 assoc/comm/unital polynomial op on ℕ.)
2. **Degrees multiply.** `R_B∘R_C≅R_{C⋆B}` ⟹ `d(C⋆B)=d(C)·d(B)`, `d`=max arity.
3. **Key Lemma: no high arities.** If the global sup of arities `κ` is finite and `≥2`, then
   `d(B⋆B)=κ²>κ` contradicts `κ` being the sup. So (bounded case) every `R_B` is **affine**,
   `X⋆B=C_B+D_B×X`.
4. **Reconstruction.** Affine + unit + symmetry + associativity force `X⋆B=B×X` (`I=1`) or
   `X⋆B=X+B+S×X×B=∨_S` (`I=∅`), `S` unique.

## The one gap (honest)
Move 3 only handles **bounded** arities: `κ²=κ` for infinite cardinals, so the growth argument
can't exclude an infinite (or finite-but-unbounded) arity. All counting arguments I tried are
tautological — the real obstruction lives in **associator naturality** (exactly what killed the
`support` and `Sym²` candidates on 2026-07-21), but I don't have a general argument for an arbitrary
infinite arity. I did **not** paper over it. Both conclusion families have `κ=1`, so the families are
complete; only exhaustiveness against hypothetical unbounded pathologies is conditional.

**Question for you:** is excluding infinite-arity monoidal `⋆` worth a focused push (it would make the
theorem unconditional and, I think, publishable as "the closed convolutional tensors on Poly"), or do
you prefer the bounded-arity statement as-is? The bounded statement already covers every container
application (finite/bounded positions). Also: the **non-symmetric / one-sided** case (left-closed but
not right-closed) is genuinely open — my proof uses symmetry throughout.

Grade: bounded-case theorem = `proved`; unconditional = `conjecture` (gap = infinite arities).
Verifications in `scratch/cardinality-classification.py`, `scratch/verify_reconstruction.py`.
