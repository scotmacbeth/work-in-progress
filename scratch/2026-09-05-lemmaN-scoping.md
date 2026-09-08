# Scoping note — Lemma N (necessity for M-container composition)

**Date:** 2026-09-05
**Task:** scope, do NOT prove. Seed an attack plan for the OPEN converse of THM 3.
**Grading tags:** [verified from PDF] = read the exact statement in the seed PDF; [from abstract only] = only saw abstract/attribution; [my assessment] = my reasoning, not a cited fact.

Sources read:
- Gambino–Kock, *Polynomial Functors and Polynomial Monads* (2009 preprint of the 2013 MSCS paper), `/home/agent/git/ghani-containers/pdf/related/`. §1.16, §1.18, §1.22.
- Niu–Spivak, *Polynomial Functors — A Math. Theory of Interaction* (2023), `/home/agent/git/ghani-containers/pdf/spivak-poly/`. Def 6.71, Thm 6.80, Prop 8.106 (Garner), Def 8.107.
- Carboni–Johnstone, *Connected limits, familial representability and Artin glueing*, MSCS 5 (1995) 441–459, **with Corrigenda MSCS 14 (2004) 185–187** [from abstract only — DOIs 10.1017/S0960129500001183 and .../S0960129503004080; note the corrigenda exists and should be consulted before relying on fine print].
- Weber, *Familial 2-functors and parametric right adjoints*, TAC 18 (2007) [from abstract only].

---

## §1. The familial-representability characterization (exact statements + citations)

### 1.1 The master equivalence (this is the workhorse)
[verified from PDF — Gambino–Kock §1.18]
For a functor `P : Set/I → Set/J`, TFAE:
- (i) `P` is **polynomial** (represented by a diagram `I ← B → A → J`, `P = Σ_A ∘ Π_f ∘ Δ_s`);
- (ii) `P` **preserves connected limits** (equivalently: pullbacks **and** cofiltered limits; equivalently: **wide pullbacks**);
- (iii) `P` is **familially representable** (a sum/coproduct of representables);
- (iv) the comma category `(Set/J)↓P` is a presheaf topos;
- (v) `P` is a **local right adjoint** = **parametric right adjoint** (every slice of `P` is a right adjoint);
- (vi) `P` admits strict generic factorisations (Weber);
- (vii) every slice of `el(P)` has an initial object (Girard's normal-form property).

Attribution [verified from PDF, GK §1.18 prose]:
- **(ii)⇔(iii)** is due to **Diers**; clarified by **Carboni–Johnstone**, who also got **(ii)⇔(iv)** (Artin glueing). **(i)⇔(iii)** implicit in C–J, one-variable case explicit.
- **(ii)⇔(v)⇔(vi)** go back to **Lamarche** and **Taylor** (after Girard).
- **(i)⇔(v)** observed by **Weber**. **Crucial caveat** [verified from PDF, GK §1.18]: over **general presheaf toposes**, local right adjoints need **not** be polynomial (counterexample: the free-category monad on directed graphs is a pra but not polynomial). The "(v)⇒(i)" / "(iv)⇒polynomial" collapse is **special to `Set`** (uses `Set/I ≃ Set^I`).

The single fact I will use downstream, over `Set`:
> **[GK §1.18 (i)⇔(ii)]** `M : Set → Set` is polynomial **iff** `M` preserves connected limits.

### 1.2 Supporting facts
- [verified — GK §1.16] Polynomial functors **preserve connected limits** (hence are cartesian, i.e. preserve pullbacks). Proof: `Δ_s`, `Π_f` are right adjoints (preserve all limits); `Σ_t` preserves connected limits.
- [verified — GK §1.22] A `P : Set → Set` is polynomial iff every slice of `el(P)` has an initial object (direct, Girard).
- [verified — Niu–Spivak Def 6.71] A connected limit = limit over a nonempty connected `J`; examples: equalizers, pullbacks, cofiltered (directed) limits. **Products and terminal objects are NOT connected.** This is the reason polynomials preserve pullbacks but not products-on-the-right.
- [verified — Niu–Spivak Prop 8.106 (Garner) + Def 8.107] For `C,D` categories, a functor `Set^C → Set^D` is a **prafunctor** iff it is a **parametric right adjoint** iff it **preserves connected limits** iff it is a `(C,D)`-bicomodule. (The `C=D=1` case is exactly `M:Set→Set` polynomial ⇔ connected-limit-preserving.)

### 1.3 Weber (parametric right adjoints)
[from abstract only — Weber TAC 18 (2007)] Develops familial 2-functors / parametric right adjoints and **strict generic (generic/free) factorisations**; the pra ⇔ familial characterization is his (v)/(vi). **No cancellation/composition-reflection result** ("if `G∘M` is a pra and `G` is a nice pra then `M` is a pra") appears in the abstract, and I found none cited in GK or NS. **[my assessment]** pra's are closed under composition; I have not located any statement that pra-ness of a composite *reflects* down onto a right factor. Treat "cancel the trailing M" as **unsupported by the literature** until shown otherwise.

---

## §2. The trailing-M obstruction, stated precisely

Setup. An `M`-container `(S,P)` has extension `⟦S,P⟧_M := ⟦S,P⟧ ∘ M`, where `⟦S,P⟧ = Σ_{s∈S} y^{P s}` is the underlying polynomial. The unit container `y` has `⟦y⟧_M = M`.

Composition of extensions is functor composition:
```
⟦p⟧_M ∘ ⟦q⟧_M  =  ⟦p⟧ ∘ M ∘ ⟦q⟧ ∘ M .
```
"`M`-containers **compose**" means: for all polynomial `p,q` there is a polynomial `r` with
```
(H)      ⟦p⟧ ∘ M ∘ ⟦q⟧ ∘ M   ≅   ⟦r⟧ ∘ M          (an M-container, NOT a bare polynomial).
```

**Correction to the prompt's phrasing [my assessment — this is the crux, flag hard].**
The prompt states the hypothesis two ways: (a) "`M`-containers compose" and (b) "`⟦p⟧∘M∘⟦q⟧` is polynomial `⟦r⟧` for all `p,q`." **These are NOT literally equivalent, and the gap between them IS Lemma N.**
- Under reading (b), take `p=q=Id` (`⟦Id⟧=y`): then `⟦p⟧∘M∘⟦q⟧ = M` is polynomial — **Lemma N is trivial**. So (b) cannot be the real open hypothesis.
- The real hypothesis is (H): the composite is `⟦r⟧∘M`, i.e. it carries a **trailing `M`**. Passing from (H) to (b) requires cancelling one trailing `M`:
  ```
  (TMC)   ⟦p⟧∘M∘⟦q⟧ ∘ M ≅ ⟦r⟧ ∘ M   ⟹?   ⟦p⟧∘M∘⟦q⟧ ≅ ⟦r⟧  (polynomial).
  ```
  **(TMC) is exactly the open content of Lemma N**, and it is false in the naive form because `(−)∘M : [Set,Set] → [Set,Set]` is **not conservative**: a natural iso `F∘M ≅ G∘M` only pins `F` and `G` down on the (essential) image of `M`, saying nothing off `im(M)`.

So: **Lemma N ⟺ a trailing-`M` cancellation.** The cleanest instance (`p=q=Id`) is
```
(★)   M ∘ M ≅ ⟦r⟧ ∘ M  with r polynomial   ⟹   M polynomial.
```
Every `p,q` instance is `⟦p⟧∘M∘⟦q⟧∘M ≅ ⟦r_{p,q}⟧∘M`; the `p=q=Id` instance (★) is the minimal one and, I argue in §4, essentially the whole problem for a **monad** `M`.

**Why `(−)∘M` isn't conservative — the precise defect.** A natural transformation `α : F ⇒ G` with `α∘M` iso means `α_{MX}` iso for all `X`. To conclude `α_X` iso for all `X` we need every set `X` to be (a retract of / built from) values `MY` — i.e. `M` "eso/dense" — which a general effect monad is not. `⟦r⟧∘M ≅ M∘M` constrains `M` and `⟦r⟧` to agree only on `im(M)`.

---

## §3. The three candidate strategies, assessed

Throughout use [GK §1.18 (i)⇔(ii)]: "polynomial" ⇔ "preserves connected limits" over `Set`.

### Strategy (a) — strip the LEADING polynomial by reflection. **PARTIAL; stalls at trailing M.**
Key sub-fact [my assessment, clean and I believe correct]:
> A polynomial functor `⟦p⟧` that is **conservative** (reflects isos) **reflects connected limits**. Reason: `⟦p⟧` preserves connected limits (GK §1.16), `Set` is complete, and a **conservative limit-preserving functor into/over a complete category reflects those limits** (compare the true limit with the image; the comparison becomes iso after `⟦p⟧`, hence was iso). Concretely `⟦p⟧(X)=X^A` (`A≠∅`, a right adjoint, conservative) works.

Consequence: if `⟦p⟧∘G` **preserves** connected limits and `⟦p⟧` **reflects** them, then `G` preserves connected limits. This **strips a leading polynomial factor**.

Where it breaks: to apply it to (H) we need `⟦p⟧∘(M∘⟦q⟧∘M)` to *preserve connected limits*. But (H) only says this composite `≅ ⟦r⟧∘M`, and `⟦r⟧∘M` preserves connected limits **iff `M` does** — the very conclusion. **Circular.** Strategy (a) can strip a leading polynomial *only once we already know the composite preserves connected limits*, which we don't. **Verdict: (a) is a valid technique with no fuel; it does not by itself touch the trailing `M`.**

### Strategy (b) — a polynomial that REFLECTS connected limits "on the right." **MISDIRECTED.**
The reflection in (a) is about the **left** (outer) factor. The trailing `M` is a **pre**-composition `F ↦ F∘M`. Reflecting connected limits is a property of the outer functor and cannot cancel an inner/right factor. To cancel a trailing `M` one needs `M` itself to be "co-conservative"/**dense** (`im(M)` generating), not a property of some polynomial `p`. **Verdict: (b) as stated attacks the wrong side; no nonconstant polynomial helps cancel a trailing `M`.** (Diagonal/`X↪X²` monomorphism tricks change the outer functor, not the trailing `M`.)

### Strategy (c) — direct, exploiting extra structure. **MOST PROMISING — and the prompt undersold it: `M` is a MONAD.**
Two observations.

1. **The trivial-cancellation illusion.** `M∘Id = M`, but the composite is `⟦r⟧∘M`, not `M`; §2 shows why the extra `M` cannot be dropped. So the naive (c) fails exactly as the prompt says.

2. **[my assessment — the unused lever] Use the monad unit/multiplication.** An **effect monad** `M` has `η:Id⇒M`, `μ:M∘M⇒M` with `μ∘η_M = id_M`. Hence **`M` is a split retract of `M∘M`** in `[Set,Set]`:
   ```
   η_M : M ⇒ M∘M ,   μ : M∘M ⇒ M ,   μ∘η_M = id_M .
   ```
   **Split idempotents are absolute** (preserved by every functor; limits commute with them). Therefore:
   > **[my assessment]** For a monad `M`, `M∘M` preserves connected limits **iff** `M` preserves connected limits. (⇐ composite of preservers; ⇒ `M` is an absolute retract of `M∘M`, and retracts of connected-limit-preservers preserve connected limits.)

   This **dissolves the `(−)∘M` non-conservativity worry for the specific self-composite**: we do **not** need to cancel `M` off `M∘M ≅ ⟦r⟧∘M`; we need only show `M∘M` (equivalently `M`) **preserves connected limits**.

   Residual gap after (c.2): the hypothesis (★) gives `M∘M ≅ ⟦r⟧∘M`. We must show this forces `M∘M` to preserve connected limits. `⟦r⟧` preserves connected limits, but `⟦r⟧∘M` inherits preservation only if `M` does — still circular **unless** we get independent leverage. Two live sub-ideas:
     - **(c.2a)** If the specific `⟦r⟧` (at `p=q=Id`) is **conservative**, then `⟦r⟧∘M` preserves connected limits ⇒ (`⟦r⟧` reflects) `M` preserves them. But we don't control whether `r` is conservative (it could be constant). Need: rule out `M∘M ≅` (constant/non-conservative)`∘M` for a monad — plausibly the unit `η` forces `⟦r⟧` to be "inhabited/nonconstant," but this is unproven.
     - **(c.2b)** Bring in the **full** family of hypotheses `M∘⟦q⟧∘M ≅ ⟦r_q⟧∘M` (all polynomial `q`) plus monad strength, to manufacture a connected-limit diagram on which `M∘M` visibly preserves the limit. Unexplored.

**Verdict on strategies:** (a) and (b) are essentially neutralized by the trailing `M`. (c), **upgraded with the monad structure**, is the only route with traction: it reduces Lemma N to showing `M∘M` preserves connected limits, and the retract-absoluteness fact means proving it for `M∘M` is the same as proving it for `M`.

---

## §4. Verdict + first sub-statement to attack

### Verdict
[my assessment] **Lemma N is NOT provable by an off-the-shelf familial-representability argument alone.** GK §1.18 cleanly converts the goal to "`M` preserves connected limits," and conservativity lets you strip *leading* polynomial factors — but the **trailing `M`** is a genuine gap: `(−)∘M` is not conservative, and neither Carboni–Johnstone, Weber, nor Diers provide a cancellation/right-factor-reflection theorem (indeed Weber's own counterexample warns that composite-level niceness need not descend — pra ≠ polynomial off `Set`).

**However**, the problem is *more reachable than the prompt frames it*, because the prompt omits that `M` is a **monad**. The unit/multiplication make `M` an **absolute (split) retract of `M∘M`**, which (i) collapses the "cancel `M` off `M∘M`" worry into "show `M∘M` preserves connected limits," and (ii) makes `M∘M`-preservation and `M`-preservation **equivalent**. This is the single most valuable new observation from this scoping pass and it is not among strategies (a)/(b)/(c) as originally posed.

**Grade of reachability:** genuine gap, but **plausibly closable** via the monad-retract route if one can show `M∘M ≅ ⟦r⟧∘M` forces connected-limit preservation. **Honest risk:** it may be FALSE — a non-polynomial monad `M` agreeing with a polynomial only on `im(M)` (thus satisfying (H) and the known cardinality law, which already kills `P⁺,P,D`) is not yet excluded. If such `M` exists, Lemma N fails and the correct theorem is a weaker "polynomial-on-`im(M)`" statement.

### First sub-statement to attack (the minimal, self-contained crux)
> **(★)** Let `M : Set → Set` be a monad. Suppose there is a polynomial functor `⟦r⟧` and a natural iso `M ∘ M ≅ ⟦r⟧ ∘ M`. Then `M` preserves connected limits (equivalently, `M` is polynomial).

Attack plan for (★), in order:
1. **Reduce to preservation of `M∘M`.** Record `M` = absolute retract of `M∘M` (via `η_M`, `μ`); conclude `M` polynomial ⟺ `M∘M` preserves connected limits. *(This is the clean, do-first lemma — should formalise cleanly, candidate for Lean.)*
2. **Attack "`M∘M ≅ ⟦r⟧∘M` ⇒ `M∘M` preserves connected limits."** Sub-tasks:
   - (c.2a) Show the unit `η` forces `⟦r⟧` **nonconstant/conservative** enough that `⟦r⟧` **reflects** connected limits; then `⟦r⟧∘M` preserves ⇒ `M` preserves.
   - If (c.2a) resists, run `/assumptions` on "the trailing `M` cannot be cancelled" — the broken belief is likely "the iso only constrains `M` on `im(M)`": with a **monad**, `η_X : X → MX` embeds every `X` into `im(M)`-data, so `im(M)` may be **dense** after all. Testing density of `im(M)` (does `M` preserve enough colimits/does `η` exhibit `X` as a canonical (co)limit of `M`-values?) is the concrete next computation.
3. **In parallel, hunt a counterexample:** a non-polynomial monad on `Set` satisfying the cardinality law `|M(Mn)| = R(|Mn|)` with `M∘M ≅ ⟦r⟧∘M`. A refutation here would redirect the whole THM 3 converse to a "polynomial-on-image" statement. (Free/cofree, filter, or ultrafilter-flavored monads are the natural test cases — ultrafilter monad `β` is a prime suspect: not polynomial, but check whether `β∘β` is `⟦r⟧∘β`.)

**Cleanest single thing to prove first:** step 1 (monad ⇒ `M` is an absolute retract of `M∘M`, hence `M` polynomial ⟺ `M∘M` preserves connected limits). It is short, almost certainly true, isolates the real difficulty, and is Lean-formalisable.
