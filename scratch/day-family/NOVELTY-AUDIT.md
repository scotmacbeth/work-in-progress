# Novelty audit — Day family on Poly (2026-07-14)

Searched: the seed only (no web). Verdicts:

## PRIOR ART — cite, do not claim

| Item | Where |
|---|---|
| Day convolution on Poly; **for any** monoidal (I,★) on Set there **is** one on Poly; "⊙ distributes over coproducts" | **Niu–Spivak Prop 3.79** (2312.00990), pp. 69–71 |
| Explicit formula `p ⊙ q ≅ Σ_{(i,j)} y^(p[i] ★ q[j])` | Niu–Spivak **eq. (3.81)**, p. 71 (via coend (3.80) + co-Yoneda) |
| `× = Day(+,0)` and `⊗ = Day(×,1)` — **verbatim** | Niu–Spivak Prop 3.79 ¶2; Spivak *Reference* (2022) p. 6 under eq. (34) |
| `A ∨_S B := A + A×S×B + B`, monoidal with unit 0; `∨_0 ≅ +` | **Spivak *Reference* p. 3, eq. (9)** + fn. 2 (learned from R. Garner; = Haskell `These`; ∨_S for S≥2 from MathOverflow). Asserted monoidal, **no proof given**. S=1 case = N–S **Exercise 3.82** (solution p. 82) |
| The induced Poly family `p ▷_S q := Σ y^(p[i] ∨_S q[j])` | Spivak *Reference* **eq. (12)**, p. 4. **So my "proper class of Day tensors" IS his ▷_S family.** |
| **dirToSeq / the map ⊗ → ◁** — six independent statements | *comparitor* Shapiro–Spivak **eq. (5)**; *Indep* Spivak *Reference* **eq. (32)**; `o_{p,q}` Niu–Spivak **Ex. 6.85**; Spivak–Garner–Fairbanks **Prop 7.10**; Spivak 2020 eq. (15); Spivak 2026 fn. 5 |
| dirToSeq is **lax monoidal** (Poly,y,⊗) → (Poly,y,⊳), commutes with associators/unitors | **Niu–Spivak Ex. 6.85** — so my "Id is oplax monoidal" observation is THEIRS |
| dirToSeq **iso when p linear or q representable**: `Ay ⊗ q ≅ Ay ⊳ q`, `p ⊗ y^A ≅ p ⊳ y^A` | Spivak *Reference* **eq. (33)**; N–S **Ex. 6.84**(2)(7) — matches my computation exactly |
| ◁ not cocontinuous in the RIGHT variable | Niu–Spivak **Ex. 6.56**: `(y+1) ⊳ (1+0) ≅ 2` but `((y+1)⊳1) + ((y+1)⊳0) ≅ 3` |
| Duoidal (⊗ outer, ⊳ inner), shared unit y, "physical"/normal; interchanger `(p⊳p')⊗(q⊳q') → (p⊗q)⊳(p'⊗q')` | Shapiro–Spivak Ex. 2.5, 2.9; N–S Prop 6.87 |
| `Poly ≃ Fam(Set^op)` (free coproduct completion) | Spivak–Garner–Fairbanks **Prop 3.6** (generalized: `Set[c] ≃ Fam((c-Set)^op)`); Kondyrev–Spivak **eq. (5)**: `Poly ≃ Set[{y}]`. Not stated in the bare form. |

## NOT FOUND — the opening

- **No classification.** Every source says "for any (I,★) on Set there IS a ⊙ on Poly." Nobody
  states a converse, an essential image, or fullness/faithfulness for
  (Set-monoidal) → (Poly-monoidal). Spivak *Reference* p. 18 is openly non-exhaustive
  ("We know of two more monoidal products (y,†) and (y,‡) from Nelson Niu…").
- **No uniqueness of the pointwise member.** Nothing of the form "× is the only Day tensor
  whose extension is the pointwise product."
- **No universal property for the comparitor.** It is always *derived from* the duoidal
  interchanger by plugging y into `(p⊳p')⊗(q⊳q')→(p⊗q)⊳(p'⊗q')`. Nobody says what it IS.

## Embarrassing but useful
My OWN `lean/Containers/Containers/Dirichlet.lean` (~lines 220–246) already contains the
four-structure Day table AND an informal criterion ("whether the representable splits the
domain tensor: `y^(A+B) ≅ y^A × y^B`"). Unproved, in a doc-comment. **Theorem B is the
theorem that doc-comment was reaching for.** Check own Lean before claiming, always.

## Correction to my draft
`+` does NOT satisfy (D1): every Day tensor annihilates 0 (`S × ∅ = ∅`), but `p + 0 = p`.
So `+` fails (D1) *and* (D2). It is `◁` that is the near-miss: (D2) exactly, (D1) in the
left variable only. Hence ⊗ = the Day-ification of ◁, and the comparitor is its counit.
