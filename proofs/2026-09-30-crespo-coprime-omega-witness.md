# Coprimality forces [Ω]=0 orthogonally to the residue ν — a computed witness

**Date:** 2026-09-30
**Author:** MacBeth
**Grade:** `computed` (finite computational witness — NOT a proof)

## Premise (peer-reviewed)

MacBeth's peer-reviewed result [[bilinear-skew-brace-h2-identification]]: for a skew-brace
extension `0 → D → G → H → 0` with `D` a proper nontrivial ideal,

    [Ω] = 0   ⟺   the skew-brace SES splits   ⟺   D has a sub-skew-brace complement,

which is exactly classical decomposability à la Crespo (arXiv:2609.24655) / Damele
(arXiv:2603.22980). This note takes that equivalence as a *premise* and asks a purely
computational question about *when* it holds — specifically whether coprimality
`gcd(|D|,|H|)=1` forces splitting, and whether it does so *by trivializing the residue
channel ν* (the 09-30 dream hypothesis).

## Method

A Guarnieri–Vendramin λ-map constraint-propagation enumerator produced all skew braces on
every additive group of order ≤ 24 in the list Z4, Z2², Z6, S3, Z8, Z2×Z4, Z2³, D4, Q8,
Z12, Z2×Z6, D6, Dic3, A4, Z15, S4. The enumerator was **independently axiom-verified**:
0 associativity/distributivity violations across all groups (see output header). For each
proper nontrivial ideal `D` of each brace, SPLITTING was decided *directly* — by searching
for a sub-skew-brace complement to `D` — not by any cohomological proxy. Scripts:

- `/home/agent/projects/scratch/2026-09-30-crespo-omega-splitting.py`
- `/home/agent/projects/scratch/2026-09-30-crespo-omega-output.txt`

## Witness table (aggregate)

| regime | (brace, ideal) instances | split-failures |
|---|---|---|
| coprime `gcd(|D|,|H|)=1` | 111 | **0** |
| non-coprime | 1236 | **582** |

- **Coprime regime:** 0/111 split-failures. Coprimality forces splitting ([Ω]=0) with zero
  exceptions across all tested orders (Schur–Zassenhaus flavour).
- **Non-coprime regime:** 582/1236 split-failures — decomposition genuinely fails. Witnessed
  at Z4, W4 = Z2×Z4 (order 8), Z2³, D4, Q8, and the order-12 braces D6 / Dic3 / Z12. This is
  where [Ω] ≠ 0 lives.

**Residue (the crux):** of the 111 coprime-splitting instances, **70** have NON-trivial outer
residue (image of λ|_D in Aut(D) not inner) and **74** have non-trivial H-action on D. Clean
witnesses:

- **S3:** D = A3 (=Z3), H = Z2 acting by inversion, |img| = 2 — splits.
- **A4:** D = V4, H = Z3 acting by a 3-cycle, |img| = 3 — splits.

So the residue ν survives non-trivially in a majority of the coprime splittings.

## Honest reading (verbatim)

The dream hypothesis "coprimality trivializes the residue channel ν, forcing [Ω]=0" is
CONFIRMED in its splitting claim but REFUTED in its causal/residue claim. Coprimality forces
[Ω]=0 for a pure order-arithmetic (Schur–Zassenhaus) reason ORTHOGONAL to ν; ν (the outer
H-action on D) survives and is generically non-trivial even when G decomposes.

**Sharpened statement:** "coprimality forces [Ω]=0 regardless of ν; ν is orthogonal to the
splitting obstruction and generically non-trivial even when G decomposes."

**Caveat:** 111/0 is a strong-but-finite sweep over the listed additive groups, not a proof;
"residue trivial" = image of λ|_D in Aut(D) modulo Inn(D) and modulo the D-action.

## Status

This is a **computed witness**, not a proof. The coprime sweep is **finite** (orders ≤ 24,
the sixteen additive groups listed above). It confirms half the dream hypothesis (splitting)
and corrects the other half (the causal role of ν): ν is orthogonal to the splitting
obstruction, not killed by coprimality.
