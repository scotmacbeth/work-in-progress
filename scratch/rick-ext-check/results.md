# Rick's Emergent-Holonomy / Ext Conjecture — Computational Check

Trust grade: **computed** (explicit permutation + finite-field linear algebra, two
independent cohomology methods agreeing). No GAP/Sage available; done in
Python/SymPy over Q, F2, F3.

Scripts (all runnable, `python3 <file>`):
- `witnesses.py`     — verifies group data (U,A,B,h) by explicit permutations
- `cohomology.py`    — H^1(C_n;k) via the periodic free resolution of k over kC_n
- `crossed_homs.py`  — H^1(C_n;k) via brute crossed-homomorphism linear system (independent)

---

## 1. Verified group data (both witnesses)

Computed by explicit permutation enumeration (0-indexed points internally).

### S₃ witness — G=S₃ on {1,2,3}, P=A₃=⟨(123)⟩, P'=⟨(12)⟩, s=1
- |P|=3, |P'|=2, |G|=6. **Exact factorization confirmed**: P∩P'={e}, |P||P'|=|G|, P·P'=G.
- A = Stab_P(1) = {e}, size 1
- B = Stab_{P'}(1) = {e}, size 1
- U = Stab_G(1) = ⟨(23)⟩ ≅ C₂, size 2
- **h(s) = |A\U/B| = 2 = |U|.** ✓ (matches MacBeth's proved h=|U| when A=B={e})

### A₄ witness — G=A₄ on {1,2,3,4}, P=V₄, P'=C₃=⟨(123)⟩, s=1
- |P|=4, |P'|=3, |G|=12. **Exact factorization confirmed**: V₄∩C₃={e}, 4·3=12, V₄·C₃=A₄.
- A = Stab_{V₄}(1) = {e}, size 1 (V₄ acts freely/regularly)
- B = Stab_{C₃}(1) = {e}, size 1
- U = Stab_{A₄}(1) = ⟨(234)⟩ ≅ C₃, size 3
- **h(s) = |A\U/B| = 3 = |U|.** ✓

---

## 2. H¹ / Ext¹ dimension table

dim_k Ext¹_{kU}(k,k) = dim_k H¹(U;k), trivial coefficients.
Two independent computations (periodic resolution; brute crossed-homs) **agree**.

| U        | char 0 | char 2 | char 3 |
|----------|:------:|:------:|:------:|
| C₂ (S₃)  |   0    | **1**  |   0    |
| C₃ (A₄)  |   0    |   0    | **1**  |

Matches the theory dim H¹(C_n;k) = [char(k) | n]. The augmentation-scalar
cross-check (aug of the norm element N = n mod char; H¹ = ker(mult-by-n) on k)
reproduces the same table.

**Which characteristic does Ψ live in?**
- S₃: Ψ lives in **char 2** (= the prime dividing |U|=2).
- A₄: Ψ lives in **char 3** (= the prime dividing |U|=3).
In both, "the char where Ext¹ is nonzero" = "the char dividing |U|". Rick's claim holds
here.

---

## 3. Verdict on pattern (b): h(s) = |U|·dim_k Ext¹_{kU}(k,k) in char | |U|

- S₃, char 2:  |U|·dim = 2·1 = 2 = h.  **holds**
- A₄, char 3:  |U|·dim = 3·1 = 3 = h.  **holds**

**BUT — adversarial caveat (important):** this is very likely a **TAUTOLOGY on these
two data points**, not a validated prediction.
- Because A=B={e} in both witnesses, MacBeth's theorem already forces h=|A\U/B|=|U|.
- Because U is cyclic, dim Ext¹_{kU}(k,k)=1 in the char dividing |U| — automatically.
- So |U|·dim = |U|·1 = |U| = h holds by construction, independent of any real
  content of Rick's pairing Ψ.
Two points, both degenerate (A=B trivial, U cyclic) ⇒ the identity is forced.
**A genuine test requires a witness with A and/or B NON-trivial** (so h=|A\U/B| < |U|),
and/or U non-cyclic (so dim Ext¹ can differ from 1). Only then does
h = |U|·dim Ext¹ have falsifiable content. As stated it is not yet a real prediction.

---

## 4. Permutation-module Ext caveat (c)

Rick's fuller formula is Ext¹_{k[U]}(k[P/A], k[P'/B]).
- **Module structure is NOT canonically specified** in Rick's email: how U acts on the
  coset spaces P/A and P'/B is left open (P/A carries a P-action, not a priori a
  U-action; the identification needs pinning). **We do not guess it silently.**
- In BOTH witnesses A=B={e}, so P/A = P and P'/B = P' as sets. The cleanest honest
  interpretation, where these reduce to the trivial U-module k, is exactly part (a)
  above (computed).
- Regular-module sanity: Ext¹_{kU}(kU, kU) = 0 in every characteristic, since kU is
  free hence projective and Ext^{≥1}(projective, −)=0. So if the coset modules were
  read as free/regular U-modules, the Ext would vanish — a useful boundary check
  showing the answer is sensitive to which module structure is meant.
- **FLAG:** the module structure in Rick's formula must be pinned down before the
  permutation-module Ext can be asserted. We report only what the two clean
  interpretations give (trivial → table §2; regular → 0).

---

## 5. Explicit S₃ 2-cocycle deliverable → it is honestly a 1-cocycle

At s=1 with A=Stab_P(s)={e} trivial, the extension 1→A→E→B→1 is degenerate (A=B={e}),
so there is **no nondegenerate 2-cocycle** here — manufacturing one would be dishonest.
The relevant class governs whether U=C₂ splits, and it lives in **H¹(U;k)**.

Because A is trivial, Rick's "2-cocycle" framing collapses to a **1-cocycle**.

**Generator of H¹(C₂;F₂), explicitly (verified in `crossed_homs.py`):**

Let U = {e, r} with r = (23), r²=e. Coefficients k=F₂, trivial U-action.
Define the 1-cochain (crossed homomorphism)
```
    f : U → F₂,   f(e) = 0,   f(r) = 1        i.e.  f(u) = [u ≠ e].
```
- 1-cocycle identity (trivial action): f(xy) = f(x) + f(y) for all x,y ∈ U —
  checked exhaustively over F₂, holds.
- Not a coboundary: B¹ = 0 for trivial action (a principal crossed hom u↦u·a−a = 0),
  so f ≠ 0 in cohomology.
- Therefore **H¹(C₂;F₂) = F₂**, generated by `u ↦ (u ≠ e)`, the nontrivial
  homomorphism C₂ → F₂.

This is "the unpolished page": the emergent holonomy of the S₃ witness sits in
H¹(C₂;F₂) (1-dimensional), generated by the identity crossed homomorphism r↦1. The
char-2 location is exactly the prime dividing |U|=2.
