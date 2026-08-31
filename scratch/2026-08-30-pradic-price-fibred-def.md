# Pradic–Price `arXiv:2601.15420` — the actual definition of *fibred (polynomial) functor*

**Status: PAPER OBTAINED AND READ.** Attribution debt CLOSED.

- PDF: `/home/agent/papers/pradic-price_2601.15420_fixpoints-poly-of-poly.pdf`
- Text: `/home/agent/papers/pradic-price_2601.15420.txt` (`pdftotext -layout`)
- Version: **v2 [cs.LO] 11 May 2026** (LICS-2026 accepted version), 45 pp incl. appendices.
- Title: *Problems with Fixpoints of Polynomials of Polynomials*, Cécilia Pradic & Ian Price (Swansea).
- Method: `curl -sL https://arxiv.org/pdf/2601.15420` then `pdftotext -layout` (the trick worked first time).

Page numbers below are the printed page numbers of the PDF.

---

## 0. What `sources.json` said, and how it held up

`memory/reading/sources.json:410` records `extraction: "deep-read"`, note:

> "Studies fixpoints (initial algebra/terminal coalgebra/zeta operator) of fibred endofunctors over
> the fibrewise-opposite-of-codomain-fibration framing (= Cont(C) in MacBeth's own vocabulary,
> matches contravariance-is-fibrewise-op almost verbatim)."

with a `locators` entry flagging as **STILL OPEN**: (a) whether their fibration IS my shape fibration,
and (b) their definition of *fibred endofunctor* — `(F,F_0)` or vertical `F_0=Id`.

**Verdict on the ledger: the recorded note was accurate, both open sub-questions now answered.**
(a) YES, over `C=Set` it is literally my `π`. (b) It is the `(F,F_0)` base-functor form — **and
strict**, not up to isomorphism. Details below.

---

## 1. Their fibration (§2.2, pp. 8–9) — VERBATIM

Containers are internal: "*Let `C` be a category with chosen pullbacks and `T` and `U` two objects
of `C`. A container from `T` to `U` is a triple of morphisms `(P,t,u)`*" fitting `T ← A →^P I → U`;
`I` = **shape**, `A` = **directions**. `Cont(C) := Cont(C)(1,1)`, i.e. containers of arity and
dimension 1, identified with plain morphisms `P : A → I` of `C`.

> "`shape` extends to a functor `Cont(C) → C` by considering the map `(φ,ψ) ↦ φ` on morphisms. In
> fact, **`shape` is a Grothendieck fibration, and it is straightforward to check that it is exactly
> the fibrewise opposite of the codomain fibration `cod : C^→ → C`** (see [60, §1 & §5] for details).
> So given a morphism `P → Q` in `Cont(C)` given by `(φ,ψ)`, we will call it **cartesian** or
> **horizontal** if `ψ` is an isomorphism and **vertical** if `φ = id`."
> — end of p. 8 / top of p. 9. ([60] = Streicher, *Fibered categories à la Jean Bénabou*, arXiv:1801.02927.)

Standing hypothesis (§2.1, p. 7): "**Henceforth, all categories in sight shall be lextensive.**"
Theorem 18 additionally needs `C` lextensive with dependent W- and M-types ("ΠWM-category").

## 2. Their definition of fibred — VERBATIM (Definition 13, §3.1, p. 14)

> "We now turn to introducing fixpoints of endofunctors over categories of containers `Cont(C)`.
> Here we focus on what we can achieve when we assume that `C` is a ΠWM-category on exploiting the
> fibration **`cod^op ≃ shape : Cont(C) → C`** (and more generally its `k`-fold products
> `shape^k : Cont(C)^k → C^k`)."
>
> "**▶ Definition 13.** Say that `F : Cont(C)^k → Cont(C)` is a **fibred polynomial functor** when
> 1. **`(F, F_0)` is a fibred functor `shape^k → shape` for some uniquely determined `F_0 : C^k → C`
>    (see [60, Definition 2.2])**
> 2. `F_0` is a polynomial functor
> 3. for every object `I = (I_1,…,I_k)` in `C^k`, the functors on the fibers
>    `F_I : C^{/(I_1+…+I_k)} → C^{/F_0(I)}` induced by the isomorphism `C^{/(I_1+…+I_k)} ≅ (C^{/I})^k`
>    and `F` are all polynomial functors.
>
> Say that `F : Cont(C)^k → Cont(C)^m` is a fibred polynomial functor if every component `π_i ∘ F`
> is a fibred polynomial functor."

**Reading of clause 1.** "Fibred functor" is imported from Streicher; his Def 2.3 (v20, 13 Sep 2023)
reads: "*A cartesian or fibered functor from `P` to `Q` is an ordinary functor `F : X → Y` such that
(1) `Q ∘ F = P` and (2) `F(ϕ)` is cartesian w.r.t. `Q` whenever `ϕ` is cartesian w.r.t. `P`*."
PP use the base-changing generalisation: `shape ∘ F = F_0 ∘ shape^k` plus preservation of cartesians.

- **Cartesian-preservation is definitely part of it.** p. 14: "Identities are fibred polynomial
  functors (as identity functors are polynomial functors [27, Ex. 1.6(i)] and **they trivially
  preserve cartesian morphisms**)". Lemma 15's proof (p. 31): "That the functor **is fibred**
  follows since if `ϕ:P→P'`, `ψ:Q→Q'` are cartesian, then so is `ψ⋆ϕ` [50, Prop. 6.88]".
- **It is STRICT, not up-to-iso.** "for some **uniquely determined** `F_0`", and the Theorem-22 proof
  (p. 33) verifies exactly: "To check that we have a morphism of fibrations, we define the base
  functor by `(µF)_0(I_0,…,I_{k-1}) := µF_0(I_0,…,I_{k-1},−)`. Then **`(µF)_0 ∘ shape = shape ∘ µF`
  holds by construction**."
- **NOT vertical.** `F_0` is a genuine base functor and is generally non-trivial (e.g. `⟦P⟧`, and the
  W-type functor `µF_0`). The vertical case is never singled out.

⚠ **Citation glitch (minor, mine to note not theirs):** in the 2023 v20 of Streicher on arXiv,
**Definition 2.2 is the definition of a *fibration***; the fibred/cartesian *functor* is **Definition
2.3**. PP's "[60, Definition 2.2]" is off by one against that version (or matches a different
numbering). The intent is unambiguous.

## 3. The fixpoint theorem, and what fibredness actually does (Theorem 18, pp. 14–16)

> "**▶ Theorem 18.** If `F : Cont(C) → Cont(C)` is a fibred polynomial functor and `C` is an
> lextensive category with dependent W and M-types, then
> - `F` has an initial algebra `(µF, a_{µF})`
> - `F` has a terminal coalgebra `(νF, c_{νF})`
> - `F` has a (co)algebra `(ζF, b_{ζF})` such that `(shape(ζF), shape(b_{ζF}))` is a final coalgebra
>   for `F_0` and it induces a final coalgebra for the endofunctor induced by `F` over `C^{/F_0(ζF)}`."
>
> "The basic idea behind the proof of Theorem 18 is that we may compute a fixpoint for a fibred
> polynomial endofunctor `F` by **first computing a fixpoint `γF_0` for the induced polynomial
> functor `F_0` in the base, and then take a fixpoint of `i^* ∘ F_{γF_0}`** where `i : γF_0 ≅ F_0(γF_0)`.
> In both steps, we have complete freedom over which fixpoint we want to compute" (Figure 5 matrix,
> p. 15: base-µ/total-µ → µ; base-µ/total-ν → µ; base-ν/total-µ → ν; base-ν/total-ν → **ζ**).

**Where fibredness is used, precisely (weak-initiality step, p. 16):**

> "The rearmost square is a pullback square, which can be viewed as a (representative of a)
> **cartesian morphism** between the containers `R : D → µ` and `P : A → I`. **Since `F` is a fibred
> functor, applying it to that square yields another pullback square**, and hence a unique arrow
> `γ : C → F(R)_dir` making the diagram below commute."

So: `F_0` (the base-functoriality half) is what lets you solve the fixpoint **in the base first**;
**cartesian-preservation** is what lets you transport the `fold α` pullback cube into the fibre to
get the mediating map. Both halves are load-bearing, in different places.

Authors' own scoping (§1.3 "Fixpoints of endofunctors over containers", p. 6):

> "While we do focus on those fibred polynomial endofunctors, we can note that **we only use the
> 'polynomial' aspect to be able to use the assumption that `C` has fixpoints of polynomial functors
> to begin with. Theorem 18 otherwise only requires the fibredness of the endofunctor
> `F : Cont(C) → Cont(C)`** and could be adapted to settings where fixpoints can be obtained by other
> means … **Lifting the restriction that `F` be fibred does break Theorem 18.** We only provide a
> single example of such a functor which does have a sensible initial algebra (Proposition 23)."
>
> "The definition of fibred polynomial functor that we adopt is useful insofar as it captures
> examples relevant to us and makes Theorem 18 go through, but **it is unclear to us whether it is a
> rather ad-hoc notion or if there is a more conceptual grounding to this notion**."

## 4. Statements about the composition product `◁` (their `⋆`) — the key section

**Notation alignment (Figure 4, p. 9, and Lemma 15's proof, p. 31).** Their "sequential product"
`Q ⋆ P`, for `P : A → I`, `Q : B → J`, `A_i := P^{-1}(i)`, `B_j := Q^{-1}(j)`, is the map

> `Σ_{i:I} Σ_{a:A_i} Σ_{f:A_i→J} B_{f(a)}  ⟶  Σ_{i:I} (A_i → J)`

so `shape(Q⋆P) = Σ_{i:I} J^{A_i}`. **Therefore `Q ⋆ P = P ◁ Q` in my notation: their LEFT argument
is my RIGHT argument.** (Checked against (SUB): `p◁q = (Σ_{s∈S} T^{P_s}, (s,τ)↦Σ_{d∈P_s}Q_{τ d})`.)

> "**▶ Lemma 14.** Constant functors and the bifunctors `×`, `+`, `⊗` over `Cont(C)` are all fibred
> polynomial." (p. 14; proof p. 31 uses extensivity, [19, Prop. 2.2].)
>
> "**▶ Lemma 15.** The following functor is fibred polynomial: `Cont(C) → Cont(C)`, `X ↦ X ⋆ P`."
> (p. 14; proof p. 31: "The base of the fibred polynomial functor `J ↦ Σ_{i:I} J^{A_i}` is clearly
> polynomial, as are the functors `(B_j)_{j:J} ↦ (Σ_{a:A_i} B_{f(a)})_{(i,f):Σ_{i:I}J^{A_i}}`. That the
> functor is fibred follows since if `ϕ:P→P'`, `ψ:Q→Q'` are cartesian, then so is `ψ⋆ϕ`.")
>
> "**▶ Remark 16.** On the other hand, `X ↦ P ⋆ X` is **not fibred**." (p. 14.)
>
> "**▶ Remark 17.** Unlike the usual polynomial endofunctors over a locally cartesian closed
> category, fibred polynomial functors do not necessarily have a canonical strength."
>
> §4.2 Iterations, p. 18: "As `⋆` is not commutative there are, a priori, two ways of defining
> functors whose fixpoints are iterations of some problem `P`. However, **one of these is not fibred
> (Remark 16) and the other is (Lemma 15)**." Prop 23 (p. 18): the non-fibred one,
> `X ↦ I + P ⋆ X`, still has initial algebra `Σ_{n:ℕ} P^{⋆n}`; the fibred one `X ↦ I + X ⋆ P` gives
> `P^⋄` (free monad, Thm 22 / Thm 25).

**★ Remark 16 is stated with NO proof and NO justification, anywhere in the paper or its 25 pages of
appendices** (grepped: the only occurrences of "Remark 16" are the statement on p. 14 and the
back-reference on p. 18; Appendix B.1 proves Lemmas 14, 15, 49 only). So Remark 16 is, in the
literature, exactly the same epistemic object as BHM's parenthetical: an unproved assertion.

---

## 5. VERDICT against my shape fibration `π : Fam(C^op) → Set`

### 5.1 Over `C = Set`: **SAME.** Exactly, not merely morally.

`Cont(Set) = Fam(Set^op) = Poly`, and their `shape : Cont(Set) → Set`, `(φ,ψ) ↦ φ`, **is** my
Definition 1.1 `π(S,P) = S`, `π(f,f^♯) = f`. Their "cartesian iff `ψ` iso" is my Lemma 1.2
("cartesian iff every `f^♯_s` is an isomorphism"); their "vertical iff `φ = id`" is my verticality.
Their identification with `cod^op` is my `Cont = ∫_{Set}(cod)^{op}` (`contravariance-is-fibrewise-op`).
The 2026-07-29-browse3 open question is **answered: same operation.**

### 5.2 The definition of *fibred functor*: **SAME SHAPE, THEIRS IS STRICTER.**

Mine (Def 1.3): `(F,F_0)` with a **natural isomorphism** `πF ≅ F_0π` + preserves cartesians.
Theirs (Def 13.1): `(F,F_0)` with **strict equality** `shape ∘ F = F_0 ∘ shape^k` + preserves cartesians.

`PP-fibred ⟹ my-(F)`, and the converse can fail on strictness alone. Their *fibred polynomial*
adds two polynomiality clauses (2 and 3) that I do not impose — those are orthogonal extra structure,
not a different fibredness. Neither of us uses the vertical form as *the* definition; my `(V)` is my
own extra rung.

**Consequence for my two proved results — both survive, in the safe direction:**

- **Theorem A** (`Set`): `(F) ⟹ |T| = 1` for `L_q = (−)◁q`. Since `PP-fibred ⟹ my-(F)`, my Theorem A
  is *stronger* than needed: it refutes PP-fibredness a fortiori. **My Theorem A is a PROOF of their
  unproved Remark 16** (their `X ↦ P ⋆ X` = my `(−)◁q` with `q=P`; alignment double-checked in §4
  above — the argument-order flip cancels against their `⋆` being my `◁` reversed, so the variable
  they call "left" and the variable BHM call "left" and the variable I call "left" all agree).
- **§2 "Bonus"** (`◁` is fibred in its RIGHT variable, base functor `⟦q⟧`): **this is their Lemma 15**,
  p. 14, proved p. 31, with *the same base functor* `J ↦ Σ_{i:I} J^{A_i} = ⟦P⟧`. **PRIOR ART — must be
  cited, not claimed.** What is genuinely mine there is the finer observation that cartesianness is
  preserved in *both* variables unconditionally, so the left-variable failure is *purely* failure of
  base-functoriality (they never isolate this; Remark 16 is bare).

### 5.3 Over `C = Vec_fd` (**Theorem B**): **DIFFERENT — their notion does not apply.**

Two independent mismatches, both fatal to any claim of alignment off `Set`:

1. **Different total category.** Their `Cont(C)` is *internal*: objects are morphisms `P : A → I` of
   `C`, and the base of the fibration is `C` itself. My `Fam(C^op)` has an **external** shape *set*
   `S` and a family of `C`-objects, base `Set`. These agree iff `C = Set`. `Fam(Vec_fd^op)` is not
   `Cont(Vec_fd)`.
2. **Their standing hypothesis fails.** "Henceforth, all categories in sight shall be lextensive"
   (p. 7), and Theorem 18 wants ΠWM. `Vec_fd` is **not extensive** (`∐ ⊊ ⊕`, cf.
   `vec-biproduct-collapse-proved`) and not LCC.

So Theorem B is **outside PP's scope**: no conflict, but also **no support** from them, and it must
not be presented as "fibred in Pradic–Price's sense". It is fibred in *my* `π`-sense, which is a
different (and off-`Set` genuinely distinct) notion. This is the one place the two notions come
apart and it is exactly where my strict-vs-iso and internal-vs-external caveats bite.

### 5.4 One-line answer

**SAME over `Set` (their `shape` = my `π`, their Def 13.1 = my Def 1.3 modulo strict-vs-iso, theirs
being the stricter);** **GENERALISATION in a different direction off `Set`** (they generalise the
*base* from `Set` to any lextensive `C` by internalising shapes; I generalise the *fibres* from `Set`
to any closed monoidal cocomplete `C` while keeping shapes external) — **so over `Vec_fd` the two are
DIFFERENT and theirs is undefined.**

---

## 6. Edits owed to `proofs/2026-08-30-fibredness-vs-left-closure.md`

1. Replace the Attribution note after Definition 1.3 with: paper obtained, `Definition 13` clause 1,
   `(F,F_0)` strict form, `[60, Def 2.2]` = Streicher; drop "not currently on disk".
2. §2 Bonus: **cite Pradic–Price Lemma 15 as prior art** for right-variable fibredness with base
   `⟦q⟧`. Keep only the unconditional-cartesianness refinement as mine.
3. §Theorem A: add "this proves Pradic–Price's Remark 16 (p. 14), which they state without proof",
   and note the corresponding BHM parenthetical is downstream of that Remark.
4. §Theorem B: add the scope caveat of §5.3 above — `Fam(Vec_fd^op) ≠ Cont(Vec_fd)` and `Vec_fd` is
   not lextensive, so "(F) holds always" is a statement about **my** `π`, not about PP-fibredness.
5. `sources.json`: bump `2601.15420` to a full read; record the locators of §§1–4 above; close the
   `locators` open item.

---

APPLIED to proofs/2026-08-30-fibredness-vs-left-closure.md on 2026-08-31. — Audit finding: §6 items
1–4 had **already** been applied to that file on 2026-08-30 (file mtime 00:54, this note 00:47), and
§6 item 5 (`sources.json`) had already been applied too (full-read locator + PRIOR-ART CORRECTION
entry both present under `/sources/2601.15420`). The 2026-08-31 pass verified all five line by line
and added three attribution-only refinements: the Lemma 2.1 and Proposition 2.2 headers now carry
their prior-art tags (Niu–Spivak Prop. 6.88; Pradic–Price Lemma 15) in the Definition-1.3 "stated as
mine" convention, so the attribution survives header-level skimming, and the §2 ⚠ Streicher
off-by-one citation glitch is now recorded in the attribution note after Definition 1.3.
NOT APPLIED: nothing from §6; but two *downstream* artefacts still carry the pre-correction text and
were left untouched as out of scope — `memory/for-collaborator/2026-08-30-fibredness-vs-left-closure.md`
(still frames right-variable fibredness as a bonus that "fell out" and still says PP "is not on
disk") and `proofs/registry/fibredness-vs-left-closure.json` (approach field still states the
attribution question as open).
