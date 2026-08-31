# Novelty gate — "F_q ⊣ (−) ◁ q" on Cont(Set)

Date: 2026-08-30. Checked by literature-check agent for MacBeth.

## The claim under test

For every container `q = (T,Q)`, the endofunctor `(−) ◁ q` on `Cont(Set) = Fam(Set^op)` has a
LEFT adjoint

    F_q (R, U) = (R, ρ ↦ ⟦q⟧(U_ρ)),   i.e.  F_q = Fam(⟦q⟧^op),

with `⟦q⟧(X) = Σ_t X^{Q_t}`. Unconditional in `q`.

## VERDICT: **KNOWN**. Exact prior statement, three independent write-ups plus a generalisation.

---

## Source 1 — Niu–Spivak, *Polynomial Functors: A Mathematical Theory of Interaction* (arXiv:2312.00990)

Extracted with `pdftotext -layout` to
`/home/agent/projects/scratch/txtcache/Niu-Spivak_Polynomial-Functors-Mathematical-Theory-of-Interaction_2023.txt`
(source PDF `/home/agent/git/ghani-containers/pdf/spivak-poly/Niu-Spivak_Polynomial-Functors-Mathematical-Theory-of-Interaction_2023.pdf`).

Grepped: `left adjoint`, `adjoint`, `coclosure`, `composition product`, `6.5[0-9]`, `6.57`, `Meyers`.

**HIT — Proposition 6.57 (Meyers), §6.3.2 "Interaction with limits on the left", p. 204. VERBATIM:**

> **Proposition 6.57 (Meyers).** The composition product is left co-closed. That is, there exists a
> left coclosure operation, which we denote `⌜−/−⌝ : Poly^op × Poly → Poly`, such that there is a
> natural isomorphism
>
>     Poly(p, r ⊳ q)  ≅  Poly(⌜q/p⌝, r).                     (6.58)
>
> In particular, the left coclosure operation sends `q, p ∈ Poly` to
>
>     ⌜q/p⌝ ≔ Σ_{i ∈ p(1)} y^{q(p[i])}.                       (6.59)

Formula (6.59) **is** `F_q`: same shape set `p(1)`, position set at `i` replaced by `q(p[i]) = ⟦q⟧(p[i])`.
(6.58) **is** the adjunction `F_q ⊣ (− ⊳ q)`, unconditional in `q`. Exact match, including the direction.

Corroborating in the same book:
- **Prop. 6.68 / proof, p. ~207:** "By Proposition 6.57, the functor `(− ⊳ q) : Poly → Poly` is the right
  adjoint of the functor `⌜q/−⌝ : Poly → Poly`, and right adjoints preserve limits." — states the
  adjoint side explicitly.
- **§6.4 Summary, p. 213:** "we showed that `− ⊳ q` has a left adjoint `⌜q/−⌝` and that `q ⊳ −` has a
  left multi-adjoint `− ⌢ q`."
- **§6.4 further reading, p. 214:** "We learned of the left coclosure (see Proposition 6.57) from
  **Josh Meyers**, though **it may have already been known in the containers community**."
- **Exercise 6.60**: asks for exactly MacBeth's Σ/Π proof: `Poly(p, r ◁ q) ≅ Π_{i∈p(1)} r(q(p[i])) ≅ Poly(Σ_i y^{q(p[i])}, r)`.
- **Exercise 6.63 (Trimble, personal communication)**: the left coclosure is a **left Kan extension**
  `Lan_q p`. This is the same observation as "`F_q = Fam(⟦q⟧^op)`".

Answer to (a): **YES, it is in the book.**

## Source 2 — Spivak–Garner–Fairbanks, *Functorial Aggregation* (2021)

`/home/agent/git/ghani-containers/pdf/spivak-poly/Spivak-Garner-Fairbanks_Functorial-Aggregation_2021.pdf`

> **Proposition 2.16 (Coclosure for ⊳).** The composition operation `⊳` has a (right) co-closure. That
> is, for every `p, q ∈ Poly` we can define a polynomial `[q/p] ∈ Poly` and bijections, natural in `p′`,
> of the form `Poly([q/p], p′) ≅ Poly(p, p′ ⊳ q)`. (17)
> Explicitly, `[q/p] := Σ_{i∈p(1)} y^{q(p[i])}`. (18)

Preceded by "We learned the following from Josh Meyers (personal communication); it will be
generalized in Proposition 6.7." And **Remark 2.17** says it in the words of the claim:
> "Left Kan extension along `q` refers to a left adjoint of `(–) ∘ q`; **coclosure at `q` refers to a
> left adjoint of `(–) ⊳ q`**."

NOTE THE TERMINOLOGY CLASH: the book calls this the **left** coclosure; SGF and Lynch–Shapiro–Spivak
call the identical thing the **right** coclosure. Same proposition, same formula.

## Source 3 — Spivak, *Reference: Categorical Structures on Poly* (2022, arXiv 2202.00534)

§5 "Coclosures for substitution and Dirichlet product", Eqs. 68–69: same statement; footnote 9:
"I learned the right-coclosure from Josh Meyers."

## Source 4 (generalisation) — Lynch–Shapiro–Spivak, *All Concepts are Cat♯* (2023)

§2.4 "Right coclosure and left Kan extension", **Definition 2.12** (citing Spivak 2021a Prop 2.4.6):
for a `(d,e)`-bicomodule `q`, the functor `− ⊳_d q` has a **left adjoint** `[q/−]` with carrier
`Σ_{C∈c(1)} Σ_{I∈p_C(1)} y^{q ⊳_e p[I]}`. This is the bicomodule-level generalisation of the claim;
at `c = d = e = y` it reduces to (6.59). **Lemma 2.13**: `[p/(p⊳c)]` is again a comonoid.

## Source 5 — Gambino–Kock, *Polynomial Functors and Polynomial Monads* (2009)

Grepped `left adjoint`, `adjunction`, `coclosure`. All hits are about `Σ_f ⊣ Δ_f ⊣ Π_f` in slices and
about free monads (`U : P-alg → C` having a left adjoint). **NO** statement of a left adjoint to
substitution `(−) ⊳ q`. Answer to (b): **NOT THERE** (though the Poly book cites [GK12] for
substitution generally).

## Source 6 — Ahman–Uustalu / Abbott–Altenkirch–Ghani / Purdy–Damato

Grepped all 6 directed-container PDFs + 4 Nottingham container PDFs for
`left adjoint`, `coclosure`, `left-adjoint`. **Zero hits** in the Ahman–Uustalu papers; the two hits in
the Ghani line (`Categories of Containers` p.~3, `Indexed Containers` §) are about `Σ_f ⊣ Δ_f ⊣ Π_f`
reindexing, unrelated. Answer to (c): **NOT THERE** — but note the book's own hedge that it "may have
already been known in the containers community", i.e. folklore risk is on the containers side.

## Source 7 — Pradic–Price arXiv:2601.15420

`/home/agent/papers/pradic-price_2601.15420.txt`: only 4 occurrences of "adjoint", the relevant one
being `− ∘ f = Σ_f : C/I → C/J` left adjoint to pullback. **No** coclosure, no `(−) ⊳ q` adjoint.
Answer to (d): **NOT THERE**.

## Source 8 — MacBeth's own seed and notes

Already logged, repeatedly and correctly:
- `/home/agent/projects/memory/reading/poly-book-index/ch6-end.md:25,46,496` — full verbatim index entry
  for Prop 6.57 incl. the synonym list "the left adjoint of `− ◁ q`" and the Meyers attribution.
- `/home/agent/projects/memory/SUMMARY.md:76` — "◁ right-coclosure = DCont (Prop 6.57)".
- `/home/agent/projects/memory/for-robin/2026-07-25-monad-comonad-transfer-proved.md:25` — "Meyers' left
  coclosure of ◁ (Niu–Spivak Prop 6.57, formula 6.59) is `{q/p} = Σ_{i∈p(1)} y^{q(p[i])}`."
- `/home/agent/projects/memory/connections/position-op-turns-monads-into-comonads.md:32` — MacBeth's
  `G(S,P) = Σ_s y^{M(P_s)}` transfer result is *already identified* as this coclosure with `M` in the
  numerator. **That is `F_M` — the same functor.**
- `/home/agent/projects/memory/questions/open-threads.md:1040` — "Cite, don't claim."

Answer to (e): **YES — MacBeth already had it, in at least five places.**

## What is NOT the same (distinguish carefully)

- **MacBeth's T4-left theorem** (right adjoint / closure of `◁`, exists over `Set` iff `|T| = 1`) is the
  OPPOSITE adjoint side. Not a match, and its `|T|=1` condition does not contradict anything here:
  `(−)◁q` has a left adjoint always, a right adjoint essentially never.
- **`q ⊳ (−)`** (the other variable) has only a *left multi-adjoint* `− ⌢ q` (book §6.4) — different variable.
- **Cat♯ / directed containers** enters via LSS Lemma 2.13 (the coclosure of a comonoid is a comonoid),
  which is a consequence, not the adjunction itself.

## OVERALL VERDICT: **KNOWN**

Cite: **Niu–Spivak, *Polynomial Functors: A Mathematical Theory of Interaction*, arXiv:2312.00990,
Proposition 6.57 + Eq. (6.59), p. 204, credited to Josh Meyers**; equivalently
**Spivak–Garner–Fairbanks, *Functorial Aggregation*, Proposition 2.16 + Eq. (18)**; equivalently
**Spivak, arXiv:2202.00534, §5, Eqs. 68–69**.

Residual genuinely-open bits (not the adjunction itself): (i) the *identification* `F_q = Fam(⟦q⟧^op)`,
i.e. that the coclosure is literally the functor `Fam(−)` applied to `⟦q⟧^op` — the Kan-extension form
is Exercise 6.63 (Trimble), the `Fam` packaging is a presentation choice, not a new theorem;
(ii) the folklore question the book itself raises — whether the containers community had it first.
