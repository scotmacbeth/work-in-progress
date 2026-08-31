# Topic — `◁`-ADMISSIBILITY of `Fam(C^op)`: when does substitution exist at all?
Opened 2026-08-30 (third PROVE). Proof `proofs/2026-08-30-admissibility-and-the-connectedness-converse.md`.
Registry `left-adjoint-over-vec` subtree `gap3-converse`. Predecessor topic `topics/left-adjoint-over-vec.md`.

## Definition
`C` is **`◁`-admissible** if for all `p,q ∈ Fam(C^op)` there is `p◁q` with `⟦p◁q⟧ ≅ ⟦p⟧∘⟦q⟧`.
Deliberately the weakest hypothesis: closure of the image of `⟦−⟧` under composition. No monoidal
structure, no canonicity. All negative results are proved against it, hence maximally strong.

## The necessary condition (Lemma S)
Admissible ⟹ for every `P ∈ C` and every small `T`, `[P, T·1_C]` is a **copower of `1_C`**.
*Reading:* the shape set of `p◁q` is an EXTERNAL set; the base must be able to see it inside itself.
- `Set`: `1_C = 1` and every set is a copower of it — vacuous; the copower count is `T^P`,
  exactly the decoration set.
- `Vec`: `1_C = 0`, so `E·1_C = 0` always — vacuous the other way, the shape data is INVISIBLE.
  (That invisibility is T1's failure of faithfulness and is why `◁` needs a convention there.)
- **Between the two degeneracies the criterion has teeth.**

## The trichotomy (replaces the refuted §9bis dichotomy)
| base | admissible | `I` connected | left adjoint to `L_q` |
|---|---|---|---|
| `Set`, infinitary-lextensive ccc toposes | yes ⟹ **connected forced** (Thm B) | ✓ | always (Thm 1) |
| `Vec`, `Vec_fd`, additive/tiny (collapse) | yes on the collapse locus | ✗ **forced** (Lem D) | iff `\|T\|=1` (Thm 2) |
| `Set×Set` (lextensive ccc, `1` decomposable) | **no** (Thm B) | ✗ | n/a |
| `Set_*` (zero object, neither pole) | **no** (Thm A) | ✗ | n/a |

## Key lemmas worth reusing
- **E1 (terminal rigidity).** Lextensive, `1 ≅ 1 ⊔ Z` ⟹ `Z ≅ 0`. `θι_1` is a map to the terminal
  hence `id_1`; disjointness makes the pullback of the legs `0`; the pullback of `id_1` along
  `θι_2 : Z → 1` is `Z`. **E2:** `1 ≇ 0` and `E·1 ≅ 1` ⟹ `|E| = 1`. *Possibly folklore (CLW).*
- **E0.** In an infinitary lextensive `C` with `1 ≇ 0`, `γ` at `I=1` is ALWAYS injective; so
  disconnectedness is exactly failure of SURJECTIVITY, which yields a nontrivial `1 ≅ A ⊔ B`.
- **Lemma D.** Every object copower-tiny ⟹ `I` disconnected. Chase, no cardinalities.
- **`κ_{B,Z} = γ^B`.** On the collapse locus the predecessor's comparison map is `γ` with the probe
  `I` replaced by `B`. Connectedness = probe `I`; **fatal probe = `0_C`**. Two-line Thm 2 necessity
  in any base. This is `one-representability-functional-two-probes` with the probe ranging over `C`.

## The punchline (Theorem D)
`I` connected ⟹ `⟦−⟧` full+faithful (T1) ⟹ injective on objects up to iso ⟹ `◁` determined ⟹ the
question is about `C`. `I` disconnected ⟹ `◁` is a CHOICE (`Vec_fd` witness: `({∗},k²)` and
`({1,2},k)` both present `X↦X⊕X`, non-isomorphic). **Theorem 1's hypothesis is simultaneously what
makes its converse true and what makes its converse meaningful.**

## Open
1. Middle region: admissible + non-collapse + non-cartesian. No example, no non-existence proof.
   Lead: `I ≅ I_1⊔I_2` ⟹ `X ≅ (X⊗I_1)⊔(X⊗I_2)` — idempotent-splitting shape; if `I_i⊗I_j ≅ 0`
   for `i≠j`, Thm B runs without cartesianness.
2. Is Lemma S SUFFICIENT (with extensivity)? Needs the INTERNAL form of the decomposition; only
   the external hom-set version checked.
3. **Novelty ungated** for Thms A, B, D and E1/E2. And: does DJN `2305.05655`'s INDEXED formulation
   dodge Thm B (one index set per component)? If so Thm B scopes to my external-shape convention.
