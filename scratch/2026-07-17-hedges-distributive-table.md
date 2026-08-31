# Jules Hedges' distributive-law table for the four monoidal structures on Cont
*Captured 2026-07-17 from Neil's email uid 63 attachment (PHOTO-2026-07-15-12-07-12.jpg). Neil (uid 53, 50) wants the "relationships / distributive laws between the four structures" section — duoidal categories, Hedges' "ten interesting relationships".*

## The table (ROW distributes over COLUMN; D = distributive law, L = lax, – = none)

|       | ⊗ | × | + | ; (=◁) |
|-------|---|---|---|--------|
| **⊗** | – | – | D | L      |
| **×** | L | – | D | –      |
| **+** | – | – | – | –      |
| **;** | – | D | D | –      |

Non-trivial entries (6):
- ⊗ over + : **D**
- ⊗ over ; : **L**
- × over ⊗ : **L**
- × over + : **D**
- ; over × : **D**
- ; over + : **D**

## First reading (TO VERIFY / CITE — do NOT claim novelty; grep Spivak first)
- **⊗ over + = D, × over + = D, ; over + = D:** every tensor distributes over the coproduct `+`.
  This is just "the tensor preserves coproducts in each variable" — for ⊗ and × it is (D1) of the Day
  story (Thm A); for ◁ it is `(∐_i p_i) ◁ q` / `p ◁ (∐_i q_i)` distributivity. All three are the
  standard "monoidal preserves coproducts" — CITE, not new. `+` distributes over NOTHING (its row is
  all –): coproduct is the additive unit, tensors distribute OVER it, it does not distribute over them.
- **⊗ over ; = L (lax):** this is the comparitor / duoidal interchange `(a⊗b)◁(c⊗d) → (a◁c)⊗(b◁d)`
  — Spivak's Eq. 29 duoidal interchange, `Indep` map (arXiv:2202.00534 Eq. 32). LAX, one-directional.
  → my [[comparitor-points-the-wrong-way]] and [[monoidal-coherence-four-structures]]. This is the
  `(◁,⊗)` DUOIDAL structure. The "L" is exactly the laxator.
- **× over ⊗ = L (lax):** interchange between the two "pointwise-ish" tensors. Needs identification —
  is this the `Indep`-type map with × outer, ⊗ inner? VERIFY direction and source.
- **; over × = D:** `(p×p') ◁ q` vs `(p◁q)×(p'◁q)`? Sequential distributes over product. CHECK: is it
  a genuine two-sided distributive law or lax? Hedges marks D (stronger than the ⊗;-entry's L).

## Connections to what I already hold
- The `(◁,⊗)` duoidal pair is the SPINE (comparitor no-go answers a piece of Niu–Spivak Ch9 Q5).
- Coherence of ◁ (pentagon/triangle) done: [[lean-monoidal-coherence-done]].
- The asymmetry L vs D is the CONTENT: which interchanges are invertible (D) vs merely lax (L) is a
  real classification. Hedges' "-" cells are also claims (no relationship) that need the negative control.

## Owed before writing (discipline)
1. Decode Hedges' EXACT convention: does "distributes over" mean row-outer or row-inner? L vs D
   precise meaning (lax duoidal vs bona-fide distributive law / two-sided). Ask Hedges via Neil, OR
   reconstruct from which interchange maps are invertible.
2. Grep Spivak (2202.00534 Eqs 29/32/33; Niu–Spivak duoidal §, Ex 6.85) + my own notes for EACH cell
   before calling any of it new. The reproof pattern has fired 6×.
3. This is a WRITE target (book interaction chapter) resting on mostly-cited interchange maps; the
   MacBeth delta is the SYSTEMATIC table with L-vs-D proved/refuted per cell + negative controls on –.
