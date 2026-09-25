# Kernel triviality check for witnesses W1–W4 — 2026-09-25

**Question.** For each witness kernel ideal `D`, is `D` a *trivial brace*?
Trivial-brace(D)  ⇔  `(D,+)` abelian  **AND**  `a∘b = a+b` for all `a,b∈D`
⇔ `λ_a|_D = id` for all `a∈D` (i.e. `lam[a][b]==b`).
Decisive for Rathee–Yadav (arXiv:2601.12371), whose H²_Sb classification assumes the
kernel `I` is a **trivial** brace. Non-trivial-brace kernel = open general-kernel case.

Data model (from `2026-09-24-characterize-decomp.py`): a skew brace is a λ-map,
`mul(a,b)=add(a,lam[a][b])`; an ideal `D` = additive subgroup, mult-normal, λ-invariant.
Additive groups here are all abelian by construction, so the abelian clause is automatic
and the decisive test is `∘=+` on `D`.

## Representative witness kernels

| W | additive B | representative kernel D | \|D\| | (D,+) iso | ∘=+ on D? | trivial-brace | (mult,add,sb)-split |
|---|-----------|------------------------|------|-----------|-----------|---------------|---------------------|
| W1 | Z/8 | {0,2,4,6} | 4 | Z/4 | YES | **YES** | (T, F, F) |
| W2 | Z/4 (Klein-four mult) | {0,2} | 2 | Z/2 | YES | **YES** | (T, F, F) |
| W3 | Z2² (mult Z/4) | {(0,0),(0,1)} | 2 | Z/2 | YES | **YES** | (F, T, F) |
| W4 | Z2×Z4 | {0}×Z/4 = {(0,0),(0,1),(0,2),(0,3)} | 4 | Z/4 | YES | **YES** | (T, T, F) |

W4 confirmed as the crown: **mult-split = YES, add-split = YES, sb-split = NO** — both
group extensions split, no common sub-skew-brace complement (Q1 FALSE).

## Split-triple census (all proper ideals, all skew braces on each group)

| group | #skew braces | (F,F,F) | (F,T,F) | (T,F,F) | (T,T,F) | (T,T,T) |
|-------|-------------|---------|---------|---------|---------|---------|
| Z/4 | 2 | 1 | – | 1 | – | – |
| Z2² | 4 | – | 3 | – | – | 3 |
| Z/6 | 2 | – | – | – | – | 3 |
| Z/8 | 6 | 9 | – | 3 | – | – |
| Z/9 | 3 | 3 | – | – | – | – |
| Z2×Z4 | 28 | 22 | 14 | 26 | **10** | 20 |

`sb_split ⇔ (mult_split ∧ add_split)` fails on Z2×Z4: 10 ideals are both-split with no
sb-complement. Nowhere does `sb_split` hold while a component split fails (consistent).

## KEY FINDING — non-trivial-brace kernels DO occur (the open case is live)

Every kernel on Z/4, Z2², Z/8, Z/9 is a trivial brace. **On Z2×Z4 they are not.**
Cross-tabulating each proper ideal by (split-triple, trivial-brace):

| triple | trivial-brace = YES | trivial-brace = NO |
|--------|---------------------|--------------------|
| (F,F,F) | 20 | 2 |
| (F,T,F) | 10 | 4 |
| (T,F,F) | 20 | 6 |
| **(T,T,F)** | **6** | **4** |
| (T,T,T) | 12 | 8 |

So among the **W4-shaped obstruction instances** (T,T,F) on Z2×Z4: 6 have a trivial-brace
kernel, **4 have a NON-trivial-brace kernel**. Explicit non-trivial (T,T,F) witnesses:

- `sb#11`, `D={(0,0),(0,1),(0,2),(0,3)}` (add-iso Z/4): `λ_(0,1)=λ_(0,3)=` negation on D,
  so e.g. `(0,1)∘(0,1)=(0,1)+λ_(0,1)(0,1)=(0,1)+(0,3)=(0,0) ≠ (0,2)=(0,1)+(0,1)` ⇒ ∘≠+.
- `sb#11`, `D={(0,0),(0,2),(1,1),(1,3)}` (add-iso Z/4): `λ_(1,1)=λ_(1,3)` non-identity on D.
- `sb#15`, `D={(0,0),(0,1),(0,2),(0,3)}` (add-iso Z/4): same negation pattern as sb#11.

These kernels are additively Z/4 but internally a *non-trivial* brace (their own λ-action on
themselves is non-trivial) — exactly the **open general-kernel case** outside Rathee–Yadav.

## Verdict

- The **canonical representatives** of W1–W4 (as picked by the enumerator, first matching
  ideal) are **all trivial braces** ⇒ for those exact instances Rathee–Yadav applies
  directly and Option B is a clean target.
- **But the W4 obstruction class is not uniformly trivial**: the same (mult-split, add-split,
  sb-nonsplit) phenomenon on Z2×Z4 is realised by 4 skew braces whose kernel is a
  **non-trivial brace**. Those instances are the open general-kernel case; the general
  "does H²_Sb extend to non-trivial-brace kernels?" question is genuinely live on this group.

## Scripts
- New (no existing script modified): `2026-09-25-kernel-triviality-check.py` (per-witness
  representative check), `2026-09-25-kernel-scan-all.py` (full cross-tab; benign final
  TypeError — Z2³ exceeds the enumerator's 3M-assignment cap so `skew_braces` returns None),
  `2026-09-25-nontrivial-w4-extract.py` (explicit non-trivial (T,T,F) kernels).
- Reused unchanged: `2026-09-24-characterize-decomp.py` (autos, skew_braces).
