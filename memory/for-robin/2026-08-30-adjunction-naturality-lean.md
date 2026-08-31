# LEAN 2026-08-30 (second pass) — naturality completes `F_q ⊣ (−)◁q`

**File:** `lean/Containers/Containers/CompLeftAdjoint.lean` (extended, not new).
`lake build` green, sorry-free, zero warnings. Seven new declarations, all on the first build.

## What was missing

This morning's session proved both triangle identities and both hom-set round trips. But
`adjUnit` and `adjCounit` were only *families* of container morphisms — their **naturality was
never stated**. Without it, `F_q ⊣ L_q` is a pointwise bijection, not an adjunction of functors.
That was a real gap in the certification, and it is now closed:

| declaration | axioms |
|---|---|
| `Container.whiskerRight_id` (`L_q` preserves id) | none |
| `Container.whiskerRight_comp` (`L_q` preserves ∘) | none |
| `Container.adjUnit_naturality` | `[Quot.sound]` |
| `Container.adjCounit_naturality` | `[Quot.sound]` |
| `Container.adjTranspose_naturality_right` (in `p`) | `[Quot.sound]` |
| `Container.adjTranspose_naturality_left` (in `r`, contravariant) | `[Quot.sound]` |
| `Container.adjCounitPerturbed_naturality` (control) | `[Quot.sound]` |

With `leftAdjMap_id`/`leftAdjMap_comp` and the two triangles, that is now the complete
definition of an adjunction.

## The finding: naturality and the triangles are independent probes

Everything again proved by `ext' rfl (fun _ _ => rfl)`, so I ran controls.

**Control 1 (compiles — kept as a theorem).** Take `qBool` = one shape, two positions, and
perturb the counit to flip the injected position, `ε'_p a = ⟨c a, fun z => ⟨a, !z⟩⟩`. This is the
*same perturbation that broke `triangle_seq`* last cycle. It still satisfies the naturality
square **on the nose**. So naturality does not detect it, and the triangles are not implied by
naturality — the two conditions are independent probes of the same counit. Certifying one leaves
the other free to be wrong.

**Control 2 (a failure, so it lives in the module docstring).** Post-compose the unit square with
the automorphism `⟨w,z⟩ ↦ ⟨w,!z⟩` of `F_q r ◁ qBool`: `adjUnit_naturality` then FAILS — on the
**position** leg, while the shape leg still discharges by `rfl`. The squares have content, and
that content is in the positions.

That last point is now the *second* independent confirmation of the same warning: a shape-level
argument certifies wrong data just as happily. It is the precise sense in which the two-line
Yoneda proof in §4.3 of `2026-08-30-pra-vs-probe-method.md` is under-determined, and it is what
to watch for in any `Fam(C^op)` version.

## Registry

`proofs/registry/pra-vs-probe-method.json`, new child `lean-adjunction-naturality`,
role `attempt`, trust `lean-verified`. `trustcheck` reports OK. `registry_validate` still flags
the pre-existing root-vs-`small-case-sweeps` advisory, deliberately left — `computed` is the
correct trust for a script sweep.

## Not done

Naturality of `F_q` in the parameter `q` (contravariant, since positions run backwards); the
`Fam(Vec^op)` version (open PROVE target); the right adjoint (does not exist for `|T| ≥ 2`).
