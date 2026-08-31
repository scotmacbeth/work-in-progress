# LEAN 2026-08-11 — `DirectedContainer.prod` and the store category `𝕊 × C`

**File:** `lean/Containers/Containers/StateProductLifting.lean` (wired into root
`Containers.lean`, full `lake build` green, zero warnings, zero `sorry`).

## What this certifies

The **SOUND half** of the State-liftings classification
(`proofs/2026-08-10-state-liftings-holonomy-free.md`, §SOUND;
`proofs/2026-08-11-state-liftings-holonomy-triviality.md`): *every small category
`C` yields a State proof-relevant monad lifting, via `C ↦ 𝕊 × C`*, where `𝕊` is
the store/costate category `ΔS = deltaDC S`. The Python "count = #monoids" check
now has a Lean certificate of the embedding object.

## The deliverables

1. **`DirectedContainer.prod C D`** — a *reusable* product of directed containers
   (does NOT bake in `Bool`/`Z2`). Under DCont ≅ Cat this is the **product
   category**: `Shape = C.Shape × D.Shape`, and the position fibre is the
   **product** `C.Pos s × D.Pos t` (a morphism out of `(s,t)` = a *pair* of
   morphisms). Note this is NOT `Containers.Cont`'s `Container.prod`, whose fibre
   is a *coproduct* `P s ⊕ Q t` (that is the categorical product in Poly, a
   different universal property). `root/sub/shift` act componentwise; D1–D5 hold.
   **Axiom-free** (`#print axioms DirectedContainer.prod` → none).

2. **`transport_prod`** — the one genuinely dependent lemma: a transport over a
   product of shapes `fun w => F w.1 × G w.2` factors as the pair of componentwise
   transports. Proof is `cases h; rfl`. **Axiom-free.** This is what discharges the
   transports in D2 (along D1) and D5 (along D4) for the product.

3. **`stateProduct := (deltaDC Bool).prod readerGroupoidLifting`** — the concrete
   `𝕊 × C = ΔBool × ℤ/2`. Comonad laws inherited from `Containers.Directed`
   (`stateProduct_left_counit`/`_right_counit`/`_coassoc`).

4. **Distinguishing invariant (State vs Reader).** `deltaDC_connected`: `ΔS` is
   codiscrete — for any `s,s'` a morphism `s→s'` exists (`p := s'`), i.e. a single
   shape-orbit `π₀(𝕊)=1`. Contrast Reader's `π₀=|E|` (shape-preserving `sub s p=s`).
   `stateProduct_state_connected`: from `(b,o)` reach `(b',o)` for any `b'`.

5. **`stateProduct_is_sound_state_lifting`** — packaged: three comonad laws + the
   single-orbit witness. Depends only on `Quot.sound` (from `funext` in the
   inherited laws); no `Classical.choice`, no `sorryAx`.

## Lean gotcha worth remembering (for future product/transport work)

Do **not** hand-write `h ▸ (x, y)` when `h : (a,b) = (a',b')` and the target type
is `F a' × G b'`: the `▸` elaborator abstracts the equation's endpoints out of the
*expected type*, and `F a' × G b'` does not contain the pair `(a',b')` as a
subterm, so motive inference fails ("does not contain the expected result type").
Two fixes, both used here:
- state `transport_prod` over **whole-pair variables** `ab a'b' : A × B` with the
  type written via projections `F ab.1 × G ab.2` / `F a'b'.1 × G a'b'.2`, so the
  motive `fun w => F w.1 × G w.2` *is* discoverable; prove by `cases h; rfl`;
- in the field proofs never write `▸` yourself — route the transport through
  `rw [transport_prod]` (the compiled lemma carries its motive), then reduce the
  concrete `shift`/`root` pair with a `show`/`exact prodEq …`.

## Not done (honestly)

- No registry JSON node covers the state-liftings classification yet (the
  `state-holonomy-triviality` node is proof-memory only), so nothing was set to
  `lean-verified`. **Suggest** creating `proofs/registry/state-liftings-cat.json`
  with a `sound-embedding` child pointing at `DirectedContainer.prod` +
  `stateProduct_is_sound_state_lifting`. Completeness (the ONTO direction) is a
  PROVE result, deliberately NOT formalised here.
- The comonad laws for `stateProduct` are *inherited*, so their axiom footprint is
  `Quot.sound` (funext), same as every other DCont in the library. `prod` and
  `transport_prod` themselves are fully axiom-free.
