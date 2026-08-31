# Hedges' distributive-law table for the four monoidal structures on `Cont`

**MacBeth — 2026-07-16 (PROVE deep-work session).**

> **Headline.** I reconstruct Jules Hedges' 4×4 table of relationships between the four monoidal
> structures `{⊗, ×, +, ◁}` on `Cont ≅ Poly` **from first principles, with an explicit map and a
> proof (or negative control) for every one of the sixteen cells.** The reconstruction agrees with
> Hedges' transcribed grid in **fifteen of sixteen cells** and yields three deliverables:
>
> 1. **The convention, decoded** (this was the OWED item). "Row `R` distributes over column `C`",
>    with `R` the *outer/distributing* operation. The verdict `D`/`L`/`–` means: **`D`** = a genuine
>    two-sided distributive law (the canonical comparison is invertible); **`L`** = a genuine, *non-
>    formal* lax interchanger exists but is not invertible; **`–`** = no canonical comparison beyond
>    the *formal* `(co)limit` gadgets (which are dashed throughout). This single reading generates the
>    whole grid.
>
> 2. **A sharpening.** The two composition-row entries `◁/+` and `◁/×` marked `D` are **left-variable
>    only**: `◁` distributes strictly over `+` and `×` in its *outer* argument (an isomorphism) and
>    **fails in the inner argument** (Niu–Spivak Ex. 6.56; and `2y²≇4y²`). They are one-sided
>    distributive laws, not two-sided; only `⊗/+` and `×/+` are genuinely two-sided.
>
> 3. **One correction.** The lone disagreement is the cell `×/⊗`. I **prove** that the `×`-outer /
>    `⊗`-inner interchanger *does not exist* (explicit witness `(1,y,y,1)` would demand an impossible
>    morphism `1→y`). The genuine lax interchanger of the `⊗`–`×` pair is `⊗/×` (⊗ outer, × inner —
>    Shapiro–Spivak Ex. 2.2 dual, *pair-into-the-product*), which is *formal* and never invertible.
>    So the `⊗`–`×` cell that Hedges records at `×/⊗=L` is a transposition: the map lives at `⊗/×`,
>    and is of the same *formal* character as the gadgets dashed everywhere else.
>
> The individual maps are Spivak's and Shapiro–Spivak's; the **delta is the assembled, proved table
> with `L`-vs-`D` settled and the one anomalous cell resolved**, plus the convention decode and the
> one-sidedness of the `◁`-row.

---

## 0. The four structures, and the reading of the table

A **container / polynomial** is `p = Σ_{s∈S_p} y^{p[s]}`: a shape set `S_p` and a position set `p[s]`
for each shape. A morphism `p→q` is a forward map `S_p→S_q` on shapes and a *backward* map on
positions. Extension `⟦p⟧X = Σ_s X^{p[s]}` is fully faithful (`Cont ≅ Poly`). The four monoidal
structures (all standard; see my `2026-07-14-day-family-classification.md` §0):

| `⊙` | shapes of `p ⊙ q` | positions at that shape | unit |
|---|---|---|---|
| **⊗** Dirichlet | `S_p × S_q` | `p[s] × q[t]` | `y` |
| **×** product | `S_p × S_q` | `p[s] + q[t]` | `1 = y^∅` |
| **+** coproduct | `S_p + S_q` | inherited | `0` |
| **◁** (`;`) composition | `Σ_{s}(p[s]→S_q)` | `Σ_{i∈p[s]} q[f i]` | `y` |

and `⟦p◁q⟧=⟦p⟧∘⟦q⟧`, `⟦p×q⟧=⟦p⟧×⟦q⟧`, `⟦p+q⟧=⟦p⟧+⟦q⟧` pointwise; `⊗` has **no** pointwise form.

### 0.1 The table

Hedges' grid (Neil's email uid 63; transcribed `scratch/2026-07-17-hedges-distributive-table.md`),
**ROW distributes over COLUMN**:

|       | ⊗ | × | + | ; |
|-------|---|---|---|---|
| **⊗** | – | – | **D** | **L** |
| **×** | **L** | – | **D** | – |
| **+** | – | – | – | – |
| **;** | – | **D** | **D** | – |

### 0.2 Decoding the convention (the OWED item)

The grid mixes two genuinely different notions, and *which* notion a cell uses is forced by whether
the column `C` is `(co)cartesian` or a genuine tensor. This is not a defect — it is the honest content
of "distributes," and Shapiro–Spivak's *Duoidal Structures for Compositional Dependence*
(**arXiv:2210.01962**, §2) supplies both notions as the two families of duoidal structures on `Poly`.
*(Not to be confused with Spivak's separate* Reference for Categorical Structures on Poly*,
arXiv:2202.00534, which carries the interchanger/`Indep` equations (29),(32),(33).)*

Throughout, **the row `R` is the *outer* operation** — the one that starts on the outside and is
pushed in. This is forced by the cell `⊗/;=L`, whose map is Spivak's interchanger
`(a◁b)⊗(c◁d) → (a⊗c)◁(b⊗d)` with `⊗` outermost (Reference eq. (29); Prop. 2.1.14). *(N.B. my own
prior scratch notes had this map written backwards — the authoritative direction is `⊗` outer,
confirmed against the PDF.)*

**(i) Column `C ∈ {+, ×}` — the `(co)cartesian` reading.** "`R` distributes over `C`" means **`R`
preserves the `(co)product` `C`**: the canonical comparison
`(a C b) R c ⇄ (a R c) C (b R c)` (and the right version) coming from the universal property of `C`.
Verdict **`D`** iff it is an isomorphism, **`–`** iff not. (No `L` appears in these columns: the
`(co)limit` comparison always exists as a bare map, so "lax but not iso" is the same as "not a
distributive law," i.e. `–`.)

**(ii) Column `C ∈ {⊗, ◁}` — the *duoidal* reading.** "`R` distributes over `C`" means there is a
**duoidal interchanger** `ζ : (a C b) R (c C d) → (a R c) C (b R d)` (Aguiar–Mahajan; S–S Def. 2.1),
`R` outer. Verdict **`D`** iff `ζ` is iso, **`L`** iff a canonical *non-formal* `ζ` exists but is not
iso, **`–`** iff none.

**(iii) The formal-gadget exclusion.** Two families of interchangers exist for purely formal reasons
(S–S Example 2.2): *copairing out of a coproduct source* (available whenever `R = +`), and *pairing
into a product target* (available whenever `C = ×`). These carry no information about the partner
structure — they exist for *any* partner — and Hedges records them as **`–`**. This is exactly why
**the entire `+` row is dashed** and **the `×` column is dashed except where a genuine `(co)limit`
preservation lives** (`◁/×`). It is the load-bearing convention; §D makes it precise.

Under (i)–(iii) the grid is generated cell-by-cell below. The reconstruction matches Hedges except at
`×/⊗` (§C.3).

---

## A. The coproduct column `+` — preservation of colimits

Here `R` ranges over the rows and `C = +`. The relationship is "`R` preserves coproducts."

### A.1 `⊗/+ = D` and `×/+ = D` (two-sided)

**Claim.** `⊗` and `×` each preserve coproducts in *each* variable: the canonical maps
`(a+b)⊗c → a⊗c + b⊗c`, `a⊗(b+c) → a⊗b+a⊗c` (and same for `×`) are isomorphisms.

*Proof.* For `⊗`: shapes of `(a+b)⊗c` are `(S_a+S_b)×S_c ≅ S_a×S_c + S_b×S_c`, and positions are
unchanged (`(a+b)[s]×c[t]`), so the shape bijection is a container isomorphism. Symmetrically in the
right variable and for `×` (positions `(a+b)[s]+c[t]`). Equivalently: `⟦⊗⟧` and `⟦×⟧` are Day
convolutions (`⊗=Day(×,1)`, `×=Day(+,∅)`), and every Day tensor preserves coproducts in each variable
(Niu–Spivak Prop. 3.79; "`⊙` distributes over coproducts", arXiv:2312.00990 p. 70). ∎

Two-sided by symmetry of `⊗`, `×`. *(Computational spot-check: `⊗/+` and `×/+` both `left=right=True`,
`witnesses.py`.)*

### A.2 `◁/+ = D` — but **left variable only** (the sharpening)

**Claim.** `(a+b)◁c ≅ (a◁c)+(b◁c)` naturally (left/outer variable: **iso**). But
`a◁(b+c) → (a◁b)+(a◁c)` is **not** an iso (right/inner variable **fails**).

*Proof (left, iso).* `⟦(a+b)◁c⟧ = ⟦a+b⟧∘⟦c⟧`, and `⟦a+b⟧ = ⟦a⟧+⟦b⟧` pointwise, so
`(⟦a⟧+⟦b⟧)∘⟦c⟧ = ⟦a⟧∘⟦c⟧ + ⟦b⟧∘⟦c⟧` (precomposition is computed pointwise and preserves the
coproduct). At container level: shapes of `(a+b)◁c` are `Σ_{s∈S_a+S_b}(·[s]→S_c) ≅
Σ_{S_a}(a[s]→S_c) + Σ_{S_b}(b[s]→S_c)`, positions unchanged. Isomorphism. ∎

*Proof (right, fails).* `⟦a◁(−)⟧ = ⟦a⟧∘(−)` is *post*composition by `⟦a⟧ = Σ_s(−)^{a[s]}`, which does
**not** preserve coproducts (a sum of representables is not connected-colimit-preserving). Concrete
witness — **Niu–Spivak Exercise 6.56**, reproduced in `witnesses.py`: with `a = y+1`, `b = 1`, `c = 0`,
```
        (y+1) ◁ (1+0)  ≅  2·y⁰ = 2,     but     ((y+1)◁1) + ((y+1)◁0)  ≅  3·y⁰ = 3.
```
So the canonical map is `2 → 3`, not an iso. ∎

> **Reading.** `◁/+ = D` is a genuine distributive law, but a **one-sided** one: sequential
> composition distributes over choice only when the choice is *outer* (the two branches share the
> continuation `c`), because `(−)◁c` is precomposition and precomposition preserves every colimit;
> `a◁(−)` is postcomposition by a non-cocontinuous functor. Hedges' bare `D` hides this.

### A.3 `+/+ = –`

`+` does not preserve coproducts: `(a+b)+c ≇ (a+c)+(b+c)` (three summands vs. four). Diagonal
self-relation; see §D. ∎

---

## B. The product column `×` — preservation of limits

`C = ×`; relationship "`R` preserves products."

### B.1 `◁/× = D` — again **left variable only**

**Claim.** `(a×b)◁c ≅ (a◁c)×(b◁c)` naturally (left: **iso**); `a◁(b×c) → (a◁b)×(a◁c)` **fails** (right).

*Proof (left, iso).* `(−)◁c` is precomposition by `⟦c⟧`, hence preserves products. Shapes:
`(a×b)◁c` has shapes `Σ_{(s,s')∈S_a×S_b}((a[s]+b[s'])→S_c)`; using `(a[s]+b[s']→S_c) ≅
(a[s]→S_c)×(b[s']→S_c)` (a map out of a coproduct is a pair) this is
`Σ_{(s,s')}(a[s]→S_c)×(b[s']→S_c) =` shapes of `(a◁c)×(b◁c)`; and positions
`Σ_{i∈a[s]+b[s']}c[fi] = Σ_{a[s]}c[fi] + Σ_{b[s']}c[fi]` split identically. Isomorphism. ∎

*Proof (right, fails).* `a◁(−)` is postcomposition by `⟦a⟧`, which does not preserve products.
Witness (`witnesses.py`): `a = 2y`, `b = c = y`,
```
        2y ◁ (y×y)  =  2y ◁ y²  =  2·y²,     but     (2y◁y)×(2y◁y)  =  2y × 2y  =  4·y².
```
`2y² ≇ 4y²`. The diagonal `S_a`-shape on the left (one `s` used for both factors) collapses the
independent product on the right. ∎

### B.2 `⊗/× = –`, `×/× = –`, `+/× = –`

- `⊗/× = –`: `⊗` does **not** preserve products. Witness `a=2y, b=c=y`:
  `(2y×2y')⊗… ` — the shape count multiplies while positions add, giving `2y² ≇ 4y²`
  (`3-ary` table: `⊗` over `×`, `L0.50/R0.51`, never iso). The *formal* pair-into-product interchanger
  `(a×b)⊗(c×d)→(a⊗c)×(b⊗d)` does exist (§D), but it is not a preservation iso and is a formal gadget.
- `×/× = –`: diagonal (§D); `(a×b)×c ≇ (a×c)×(b×c)`.
- `+/× = –`: `+` does not preserve products (`+`-row, §D).

---

## C. The tensor columns `⊗` and `◁` — duoidal interchangers

`C ∈ {⊗, ◁}`; relationship = a duoidal interchanger `ζ:(aCb)R(cCd)→(aRc)C(bRd)`, `R` outer.

### C.1 `⊗/◁ = L` (the one genuine, non-formal lax cell)

**Map.** Spivak's interchanger (Reference [arXiv:2202.00534] eq. (29), Prop. 2.1.14; S–S [2210.01962]
Ex. 2.9):
```
   ζ : (a◁b) ⊗ (c◁d)  ⟶  (a⊗c) ◁ (b⊗d).
```
Its `b=d=y` restriction is the **comparitor** `o:a⊗c→a◁c` (S–S [2210.01962] eq. (5)). `(Poly, ⊗, ◁)`
is a **normal, in fact physical, duoidal category** (units agree at `y`, `⊗` symmetric — S–S Ex. 2.9).

**`L`, not `D`.** `ζ` is *not* invertible. This is the content of my two prior results:

- **Iso-locus.** `o_{p,q}` (hence `ζ`) is an isomorphism iff `q` is representable, or `p` is linear
  (`2312.00990` Ex. 6.84; my `2026-07-14` Prop. 6.2 gives the exhaustive trichotomy). Generically
  neither holds, so `ζ` is strictly lax.
- **Why the lax direction is forced.** My *Theorem C* (`2026-07-14`) identifies
  `p⊗− = Lan_J((p◁−)∘J)` — the Dirichlet tensor is the terminal coproduct-preserving approximation to
  `◁`, and the comparitor is the **counit of a coreflection**. A counit of a coreflection points
  `⊗→◁` and is invertible exactly on the (representable) image of `J`. So the one-directionality and
  the iso-locus are not accidents: they are the coreflection.
- **What the failure *is*.** My comparitor no-go (`2026-07-15`, registry `comparitor-comonoid-nogo`,
  `proved`): the double-`(⊗,◁)`-comonoids are precisely the *sets of commutative monoids*, via a
  fibrewise Eckmann–Hilton collapse — the exact obstruction to `ζ` being invertible on comonoid data.

So `⊗/◁ = L`, and its `L` is the deepest cell in the table: it is the entire `(⊗,◁)`-duoidal /
comparitor story. ∎

### C.2 `◁/⊗ = –` (the reverse: **no natural interchanger**)

**Claim.** There is **no** natural transformation `(a⊗b)◁(c⊗d) ⟶ (a◁c)⊗(b◁d)`.

*Proof (factorization obstruction).* A shape of the source is `((i,j), g)` with
`g : a[i]×b[j] → S_c×S_d` an *arbitrary* function on the **product** `a[i]×b[j]`. A shape of the
target is `((i,h),(j,k))` with `h:a[i]→S_c` and `k:b[j]→S_d` **independent**. A natural forward shape
map would have to produce `(h,k)` from `g` naturally in `a,b,c,d`; but `h(p)` can only be
`π₁ g(p,q)` for some `q∈b[j]`, and `k(q)` only `π₂ g(p,q)` for some `p∈a[i]` — there is no natural
choice of basepoints (and none at all if `a[i]` or `b[j]` is empty). Only the `g` that already
*factor* as `g(p,q)=(h(p),k(q))` lie in the image; the general `g` has nowhere to go. Concretely, with
`a=b=y²` and `c=d=2y`, the source has `(mn)^{|a[i]×b[j]|}=4^4=256` shapes over the single `(i,j)`, the
target only `m²n²=16`, and the missing `240` shapes are exactly the non-factoring `g`. Hence no total
natural forward shape map, so no interchanger. ∎

This is the *same* one-directionality as C.1 seen from the other side: the comparitor is a coreflection
counit `⊗→◁`, and there is no natural section `◁→⊗` (my Theorem C). `◁` carries genuine dependency (a
joint function on a product of positions) that `⊗` cannot express. `◁/⊗ = –`. ∎

*(Note: a bare container morphism `source→target` exists at every finite test point — `focus.py` finds
no pointwise obstruction — so this cell is dashed by a **naturality** obstruction, not a pointwise one.
Contrast `×/⊗` below, which fails already pointwise.)*

### C.3 `×/⊗` — the correction: **`–`, not `L`**

Hedges records `×/⊗ = L`. I claim this is untenable and the `⊗`–`×` lax interchanger lives at `⊗/×`.

**(a) `×/⊗` does not exist.** The `×`-outer / `⊗`-inner interchanger
`ζ:(a⊗b)×(c⊗d) → (a×c)⊗(b×d)` has forced shape bijection (both sides are the four-fold shape product,
reshuffled), so it reduces to a *backward* position map
`(a[i]⊔c[k])×(b[j]⊔d[l]) → (a[i]×b[j]) ⊔ (c[k]×d[l])`.
Distributing the source, `= a[i]b[j] ⊔ a[i]d[l] ⊔ c[k]b[j] ⊔ c[k]d[l]`; the **cross terms**
`a[i]d[l]`, `c[k]b[j]` have no natural target (mapping `a[i]d[l]` into `a[i]b[j]` needs `d[l]→b[j]`;
into `c[k]d[l]` needs `a[i]→c[k]` — neither is natural). **Explicit witness** (`witnesses.py`),
`(a,b,c,d) = (1,y,y,1)`:
```
   src (a⊗b)×(c⊗d) = (1⊗y)×(y⊗1) = 1×1 = 1 = y⁰   (has an empty shape)
   tgt (a×c)⊗(b×d) = (1×y)⊗(y×1) = y⊗y = y = y¹   (has no empty shape)
```
A container morphism `X→Y` exists iff `X` has no empty shape **or** `Y` has one; here `src=1` has an
empty shape and `tgt=y` has none, so **no morphism `1→y` exists at all**. A natural `ζ` would restrict
to one. Hence `×/⊗` admits no natural transformation. ∎

**(b) The genuine `⊗`–`×` interchanger is `⊗/×`, and it is *formal*.** The `⊗`-outer / `×`-inner
interchanger
```
   ⊗/× :  (a×b) ⊗ (c×d)  ⟶  (a⊗c) × (b⊗d)
```
**does** exist: pair the two composites `(a×b)⊗(c×d) --π⊗π--> a⊗c` and `--π⊗π--> b⊗d` into the product
target. This is **Shapiro–Spivak Example 2.2 (dual)**: `(y_⊗,⊗)` and `(1,×)` form a duoidal structure
for *any* monoidal `⊗`, via the universal property of the product. It is **lax, never iso** (witness
`a=2y,b=y,c=y,d=2y`: `src=4y⁴ ≇ tgt=4y²`, `witnesses.py`), and — crucially — it is *formal*: a
pair-into-product gadget that exists for any outer tensor and carries no information about `⊗`
specifically. By the exclusion (iii) it is dashed, exactly as Hedges dashes it (`⊗/× = –`).

**Conclusion.** Under any consistent reading, `×/⊗ ≠ L`:
- If formal gadgets are excluded (as the `+`-row and `×`-column show they are): the `⊗`–`×` pair is
  `– / –`, and `×/⊗=L` is spurious.
- If formal gadgets are admitted as `L`: then the map lives at `⊗/×` (not `×/⊗`), *and* consistency
  forces the whole `+` row and `×` column to become `L` too — a far denser table than Hedges'.

Either way the `L` belongs, if anywhere, at `⊗/×`, and `×/⊗` is provably empty. I read Hedges' grid as
transposing this pair (an easy slip between adjacent cells in a photographed grid). **My corrected
cell: `×/⊗ = –`.** ∎

### C.4 The composition column `◁` off `⊗`: `×/◁ = –`, `+/◁ = –`, `◁/◁ = –`

- **`×/◁ = –`.** The `×`-outer / `◁`-inner interchanger `(a◁b)×(c◁d)→(a×c)◁(b×d)` fails pointwise:
  witness `(1,y,y,1)` gives `src = (1◁y)×(y◁1) = 1×1 = 1` (empty shape) and
  `tgt = (1×y)◁(y×1) = y◁y = y` (no empty shape) — no morphism `1→y` (`focus.py`). ∎
- **`+/◁ = –`.** The `+`-outer interchanger `(a◁b)+(c◁d)→(a+c)◁(b+d)` exists (copair out of the
  coproduct source — S–S Example 2.2 with inner `⊳ := ◁`) but is the *formal* coproduct gadget, dashed
  by (iii). ∎
- **`◁/◁ = –`.** Diagonal; `◁` is not symmetric, so even the braiding self-interchange is absent (§D). ∎

---

## D. The `+` row, the `×` column, and the diagonal — the formal-gadget wall

The remaining `–` cells are all *formal*. Two dual families (S–S Example 2.2):

- **`+` outer (the whole `+` row).** For *any* inner monoidal `C`, `(∅,+)` and `(y_C,C)` form a duoidal
  category with interchanger `(aCb)+(cCd)→(a+c)C(b+d)` from the universal property of the coproduct
  *source* (copairing). So `+/⊗`, `+/×`, `+/◁` all carry a lax interchanger — but it is content-free
  (it exists for every `C`). Dashed. And `+` preserves neither `+`, `×`, nor `◁` as `(co)limits`
  (`3-ary` table: `+`-row is `≈0` everywhere). Hence **the `+` row is entirely `–`**. ∎
- **`×` inner (the whole `×` column, modulo preservation).** For any outer `R`, `(y_R,R)` and `(1,×)`
  form a duoidal category with interchanger `(a×b)R(c×d)→(aRc)×(bRd)` from the universal property of
  the product *target* (pairing). Formal, dashed — this dashes `⊗/×`, `×/×`, `+/×`. The only surviving
  non-dash in the `×` column is `◁/×`, which is a genuine `(co)limit` **preservation** iso (§B.1), not
  a gadget. Hence **the `×` column is `– – – D`**. ∎

**Diagonals `R/R = –`.** A structure does not "distribute over itself": for symmetric `⊗`, `×`, `+`
the self-interchanger `(aRb)R(cRd)→(aRc)R(bRd)` is just the **braiding** middle-swap (S–S Example 2.3),
present and invertible but not a relationship between *distinct* structures — excluded by convention.
For `◁` (not symmetric) there is no braiding, so `◁/◁` is genuinely absent. All four diagonals: `–`. ∎

---

## E. The reconstructed table

Assembling §§A–D:

|       | ⊗ | × | + | ; |
|-------|---|---|---|---|
| **⊗** | –<sup>diag</sup> | –<sup>formal</sup> | **D**<sup>2-sided</sup> | **L**<sup>Spivak (29)</sup> |
| **×** | **–**<sup>†no map</sup> | –<sup>diag</sup> | **D**<sup>2-sided</sup> | –<sup>no map</sup> |
| **+** | –<sup>formal</sup> | –<sup>formal</sup> | –<sup>diag</sup> | –<sup>formal</sup> |
| **;** | –<sup>no map</sup> | **D**<sup>‡left only</sup> | **D**<sup>‡left only</sup> | –<sup>diag</sup> |

Legend: **2-sided** = iso in both variables; **‡left only** = iso in the outer variable, fails in the
inner (§A.2, §B.1); **formal** = a `(co)limit` gadget, dashed by convention (iii); **no map** = no
natural transformation exists; **†** = the cell where I differ from Hedges (`×/⊗`: I prove `–`, the
genuine `⊗`–`×` interchanger being the formal `⊗/×`).

**Agreement with Hedges: 15/16 cells**, exact. The differences from the transcribed grid:
1. `×/⊗`: **`–`** (proved) vs. Hedges' `L` — a transposition of the `⊗`–`×` pair (§C.3).
2. Annotation, not disagreement: `◁/+` and `◁/×` are **one-sided** (`D` in the outer variable only),
   where Hedges' bare `D` reads as two-sided (§A.2, §B.1). Only `⊗/+`, `×/+` are two-sided.

---

## F. Verification (computational)

Scripts in `scratch/hedges/` (`cont.py`, `exist.py`, `focus.py`, `witnesses.py`). Containers as lists
of position-cardinalities; iso-type = sorted multiset; all four ops implemented exactly.

| Check | Result |
|---|---|
| `3-ary` distributivity table, all 16 pairs, left & right iso-fractions | matches §§A–B: `⊗/+`,`×/+` `L1.00/R1.00`; `◁/+` `L1.00/R0.25`; `◁/×` `L1.00/R0.49`; `+`-row `≈0` |
| `◁/+` right-failure = Niu–Spivak Ex. 6.56 | `(y+1)◁(1+0)=2` vs `3` ✓ |
| `◁/×` right-failure | `2y²` vs `4y²` ✓ |
| `⊗/+`, `×/+` two-sided | `left=right=True` ✓ |
| `×/⊗` non-existence witness `(1,y,y,1)` | `src=1` (empty shape), `tgt=y` (none) ⟹ no morphism `1→y` ✓ |
| `×/◁` non-existence witness `(1,y,y,1)` | same obstruction ✓ |
| `⊗/×` formal interchanger exists, lax≠iso | `4y⁴→4y²`, morphism exists, not iso ✓ |
| `4-ary` interchanger existence sweep (`exist.py`) | only `×`-outer cells fail pointwise; `◁/⊗` fails by naturality (§C.2), confirmed structurally |

---

## G. Honesty ledger — sources, novelty, gaps

**Cited, not mine.**
- The Dirichlet interchanger `(a◁b)⊗(c◁d)→(a⊗c)◁(b⊗d)` and `Indep`: **Spivak, *A Reference for
  Categorical Structures on Poly* (arXiv:2202.00534) eqs. (29),(32),(33), Prop. 2.1.14**. The comparitor
  eq. (5) and `(Poly,⊗,◁)` normal/physical duoidal: **Shapiro–Spivak, *Duoidal Structures for
  Compositional Dependence* (arXiv:2210.01962), eq. (5), Ex. 2.9**.
- The two formal duoidal families (coproduct-outer, product-inner): **S–S (2210.01962) Example 2.2**
  and its dual.
- `⊗=Day(×)`, `×=Day(+)`, Day tensors preserve coproducts: **Niu–Spivak arXiv:2312.00990 Prop. 3.79**.
- `◁` not cocontinuous in the right variable: **Niu–Spivak Ex. 6.56**.

**Mine (the delta).**
- **The assembled, proved table** with `D`/`L`/`–` settled and *proved* per cell, including the
  negative controls on every `–` (naturality obstruction for `◁/⊗`; pointwise witness for `×/⊗`,
  `×/◁`; formal-gadget classification for the `+` row, `×` column, diagonals).
- **The convention decode** (§0.2): row = outer; `(co)cartesian` columns = preservation, tensor
  columns = duoidal interchanger, with the formal-gadget exclusion. This was the OWED item and it
  generates the grid.
- **The one-sidedness of `◁/+`, `◁/×`** (§A.2, §B.1): they are *left-variable* distributive laws, a
  strict sharpening of Hedges' bare `D`.
- **The `×/⊗` correction** (§C.3): a proof that the cell is empty and the genuine `⊗`–`×` interchanger
  is the formal `⊗/×`.
- Reuse of my `2026-07-14` Theorem C (comparitor = coreflection counit) and `2026-07-15` comparitor
  no-go to *explain* the `⊗/◁=L` cell — the one deep `L` — as the coreflection/Eckmann–Hilton story.

**Gaps / caveats.**
- `×/⊗` correction: I am confident in the mathematics (the non-existence is proved), but the
  *attribution* — whether Hedges intends a different notion at that cell, or the transcription
  transposed it — should be confirmed with Hedges via Neil. This is the one place the reconstruction
  departs from the source, so it is flagged loudly rather than smoothed over.
- Coherence of the two `L` interchangers (`⊗/◁` and, if admitted, `⊗/×`) as *duoidal* structures
  (pentagon/unit axioms) is cited from Spivak/S–S, not re-verified here; the `⊗/◁` coherence I did
  check by hand for the associators in `2026-07-14` Prop. 6.1.1.
- "Formal-gadget exclusion" (iii) is my *reconstruction* of Hedges' intent from the pattern of dashes;
  it is the unique reading consistent with the `+`-row and `×`-column being dashed while `⊗/◁` is `L`.
  If Hedges instead admits formal gadgets, the table densifies uniformly (noted in §C.3).

**For the book / grant.** This is the interaction chapter's backbone: a single decoded convention
turns Hedges' grid into a theorem, the one deep `L` (`⊗` over `◁`) *is* the comparitor/duoidal spine
already proved, and the sharpening ("sequential composition distributes over choice and product only
on the outside") is a clean, quotable slogan about dependency.
