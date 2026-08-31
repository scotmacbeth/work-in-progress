# Cont(q) over an arbitrary fibration — MacBeth's own derivation
**2026-07-14. Written BEFORE the literature agent reported. Novelty NOT yet audited.**
*(Standing rule after today: nothing here is "new" until grepped against full-text PDFs.)*

## The question (Neil, 2026-07-14)
I have `Cont ≅ Fam(Set^op)`. Neil asks: given an arbitrary fibration `q : E → B`, what is `Cont(q)`?

## The crux, identified up front
Positions are **contravariant**. That is the whole reason it is `Set^op` and not `Set`. So the
generalisation cannot be "`Fam` of the fibration" — the `op` has to go *somewhere*, and the only
place it can go is **fibrewise**.

## Step 1: rewrite Fam(Set^op) as a Grothendieck construction
`Fam(C) = ∫_{S ∈ Set} C^S` (S discrete). So

    Cont = Fam(Set^op) = ∫_{S ∈ Set} (Set^op)^S = ∫_{S ∈ Set} (Set^S)^op

and `Set^S ≅ Set/S`. A position family `p[-] : S → Set` **is** an object of `Set/S`, namely its
total space `Σ_s p[s] → S`. Hence

    **Cont ≅ ∫_{S ∈ Set} (Set/S)^op**

But `S ↦ Set/S` is exactly the **codomain fibration** `cod : Set^→ → Set`. So:

    **Cont is the total category of the FIBREWISE OPPOSITE of the codomain fibration of Set.**

## Step 2: the generalisation writes itself
For any fibration `q : E → B`, let `q^op : E^op_B → B` be its **fibrewise opposite** (dual fibration:
same base, each fibre `E_b` replaced by `(E_b)^op`; reindexing `u^*` is unchanged on objects). Define

    ┌──────────────────────────────────────────┐
    │   Cont(q)  :=  ∫_B q^op                  │
    └──────────────────────────────────────────┘

**Unfolded.** Objects: pairs `(b, X)` with `b ∈ B`, `X ∈ E_b`.  ["shape" = b, "positions" = X]
Morphisms `(b, X) → (b', X')`:
  - a map `u : b → b'` in `B`  — the **shape map, covariant**;
  - a map `u^*(X') → X` in `E_b`  — the **position map, CONTRAVARIANT**.

## Step 3: sanity check — does it give back containers?
Take `B = Set`, `q = cod : Set^→ → Set`, so `E_S = Set/S`.
- Object `(S, p)` with `p ∈ Set/S`: a shape set and a family of position sets. ✓
- Morphism `(S,p) → (T,r)`: `u : S → T`, plus a map `u^*(r) → p` in `Set/S`.
  Now `u^*(r)` is the pullback of `r` along `u`; its fibre over `s` is `r[u s]`. A map `u^*(r) → p`
  **over S** is precisely a family `∀ s. r[u s] → p[s]`. ✓✓

**That is the container morphism, on the nose, backward position map and all.** The contravariance is
not a quirk of containers — it is the fibrewise `op`, and it was hiding in plain sight.

## What this buys
1. **It explains the `op`.** "Why `Set^op`?" has never had a satisfying answer in the container
   literature. Answer: because `Cont` is the dual of the codomain fibration, and *duals of fibrations
   are the natural home of backward maps*. (Cf. the fact that DCont morphisms are **cofunctors**, not
   functors — same contravariance, one level up. Suspect these are the same phenomenon.)
2. **It predicts what survives.** The extension functor is the polynomial-functor construction, which
   needs `B` locally cartesian closed. So: `Cont(cod_C)` for `C` an LCCC should be **exactly polynomial
   functors in C** — i.e. **Gambino–Kock**. If so, GK is the special case `q = cod_C`, and my `Fam(Set^op)`
   is the special case `C = Set`. ⚠️ CHECK THIS — if true, half the generalisation is already done and
   I need to say so.
3. **The genuinely open direction:** fibrations that are NOT codomain fibrations. That is where nobody
   has been, because nobody had a reason to look. `Cont(q)` for `q` a general fibration is a category of
   "containers whose positions live in an arbitrary indexed universe."

## Two things I must check before claiming anything (TODAY'S LESSON)
- [ ] Is `∫_B q^op` (Grothendieck of the dual fibration) a *named* construction? (Jacobs, *Categorical
      Logic and Type Theory*, has the dual/opposite fibration. Bénabou.) It almost certainly is.
- [ ] Is `Cont(cod_C) = ` polynomial functors in `C` literally Gambino–Kock? Their PDF is in my seed
      (`pdf/related/`). **GREP IT.** Do not derive it. Do not summarise it. Grep it.
- [ ] Does Neil's own *Indexed Containers* (JFP 2015) already do the fibrational version? He may be
      pointing at his own paper too politely for me to notice.

## The honest prior
Given today (five reproofs of results in my own seed), my prior that Step 2 is new is **low**. The
*definition* is forced — any competent fibred category theorist writes it down in one line. What might
be new is nothing about the definition and everything about **which container theorems survive it**:
the four monoidal structures, the Day classification, the comonoid=small-category theorem. THAT is the
paper, if there is one. The definition is a lemma, not a result.
