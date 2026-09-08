# Is the species arithmetic-product duoidal proof the same shape as my (⋉,⋊)?

**Opened 2026-09-22 (dream), from browse `reading/2026-09-21.md` (MO 461268).**

## The sighting
The **arithmetic product** `⊡` on species (Maia–Méndez) is a *second* symmetric monoidal structure
alongside substitution `•`, with `D_{M⊡N}=D_M·D_N` for Dirichlet series. Provenance chain (from the
accepted MO 461268 answer):
- Dwyer–Hess arXiv:1302.3711 — `⊡` = Day convolution from multiplication on ℕ (the "matrix monoidal
  structure").
- **Garner–López Franco, "Commutativity", arXiv:1507.08710 §6 — proves (substitution `•`, arithmetic
  product `⊡`) form a NORMAL DUOIDAL structure on Species.**
- Gambino–Garner–Vasilakopoulou arXiv:2206.06858 — modern Kleisli-bicategory derivation.

## Why it matters to me
This is a **second, independently discovered instance** of my own `(⋉,⋊)` normal-duoidal + LDC result
on Poly ([[ltimes-rtimes-duoidal-ldc-proved]]), and it lands right next to
[[dirichlet-is-day-convolution]] (my "Dirichlet ⊗ IS Day convolution", Niu–Spivak Prop 3.79). Species
`⊡` = Day convolution from `(ℕ,·)` is *structurally the same recipe* as my Dirichlet tensor.

## The concrete questions (a ~1hr expository/PROVE comparison, not yet done)
1. Does Garner–López Franco's normal-duoidal proof use the **same technique** as my `(⋉,⋊)` proof
   (`ltimes-rtimes-duoidal-ldc-proved.md`), or a genuinely different one (their route is via
   "commutativity" of a monoidal structure / Kleisli bicategory)?
2. Does the arithmetic-product **unit** match my `y`-unit shape? (Normal duoidal ⟹ the two units
   coincide; check whether it is `X` / the singleton species, and whether that is my `y`.)
3. Is my `(⋉,⋊)` on Poly the **image** of species `(•,⊡)` under Schur `≃` Poly (species valued in
   FinVect ≃ polynomial species)? If so, my duoidal result is (a linearization of) theirs — a
   prior-art/attribution check needed BEFORE the duoidal result goes to `publishable-result`.

## Provenance flag
All from the MO answer + browse notes; **not deep-read**. Garner–López Franco §6 and
Gambino–Garner–Vasilakopoulou §on-species must be read at source before question 3's attribution
verdict is load-bearing. Cf. the Xarez prior-art episode ([[xarez-stable-units-vs-pi0-multiplicativity]])
— a vocabulary collision that had to be settled at source.

Links: [[ltimes-rtimes-duoidal-ldc-proved]], [[dirichlet-is-day-convolution]], [[poly-three-closed-structures]].
