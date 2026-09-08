# Lemma S IS sufficient for ◁-admissibility; extensive pole fully characterized

**MacBeth → Neil / Robin — 2026-09-02 (PROVE session).**
File: `proofs/2026-09-02-lemmaS-sufficiency.md` (`proved`). Verification `scratch/verify_distributive.py`
(FinSet, 0 failures). Registry node `lemmaS-sufficiency-extensive-pole` (validates).

## The headline

The `PROVE.md` primary target — **is Lemma S sufficient for admissibility?** — is answered **YES**
on the rigid/extensive pole, and it upgrades to a *complete characterization*:

> **For `C` an infinitary-extensive cartesian closed category (e.g. any Grothendieck topos),
> `Fam(C^op)` is `◁`-admissible ⟺ `π₀` preserves finite products.**

Both directions now proved: `⟹` is Lemma S necessity (your extensive-pole result, `2026-08-30`);
`⟸` is this session (Theorems 1–2).

## The one idea that makes it work (and why it isn't trivial)

`Gl((−)²)` is a **topos** (extensive CCC) and yet **inadmissible** — we proved that last session. So
whatever "distributivity" admissibility requires, it is NOT the internal (Gambino–Kock) distributive
law, because that holds in *every* topos. The resolution:

- **Internal** law (always holds in a topos): shape is the internal exponential `[P,T·1_C]`,
  positions are an internal dependent product.
- **External** law (D) (what admissibility needs): shape is the hom-**set** `C(P,T·1_C)`, positions
  are an **external** coproduct decomposition `P ≅ ∐_t P^c_t`.

**External = internal exactly when `[P,T·1_C]` is a copower of `1_C`** — i.e. a *discrete* object,
i.e. **Lemma S (weak form)**. In `Gl`, `[K,2·1_C] = 2·1_C ⊔ K` has a stray bald edge (a component
with no point), so the internal shape object is *not* discrete, external ⊋ internal, and admissibility
dies. This is the whole story, and it is where the sufficiency proof lives — precisely the gap the
target predicted.

## The two theorems

- **Theorem 1** (sufficiency, needs only extensive + closed monoidal): if the external law (D) holds,
  substitute `Y_t = [Q_t,X]`, apply tensor–hom and hom-out-of-coproduct, and get
  `[P,⟦q⟧X] ≅ ∐_{c∈C(P,T·1_C)} [∐_t P^c_t⊗Q_t, X]` — a natural extension. So every object is
  absorptive (Prop 6.1), hence admissible. It even *constructs* `p◁q = ∐_s r_s` explicitly.
- **Theorem 2** (needs cartesian closure): on an extensive CCC, (D) ⟺ Lemma S (weak). The `⟸` is a
  Yoneda computation; its one load-bearing step is turning "a map `X→[P,T·1_C]`" into "an external
  partition of `X`", which is exactly what Lemma S licenses. Universality of coproducts (U) is the
  extensivity input, and it *fails* in additive categories — which is precisely why `Vec_fd` (the
  flexible pole) is out of scope and admissible by a different mechanism (copower-tiny).

## Two corrections/unifications worth flagging

1. **The two "mechanisms" were one.** Our census listed `Set×Set` (obstruction: "disconnected unit")
   and `Gl` (obstruction: "`π₀` non-multiplicative") as *different* failure modes. Corollary 3.2:
   on the extensive pole there is a **single** criterion, `π₀`-multiplicativity. For `Set×Set`,
   `π₀ = ` coproduct and `π₀(X×Y) = X₁Y₁ ⊔ X₂Y₂ ≠ (X₁⊔X₂)×(Y₁⊔Y₂)`. The "disconnected unit"
   obstruction *is* `π₀`-non-multiplicativity.
2. **A prose overreach corrected.** The `2026-08-31` Cor 5.1 wrote (parenthetically) that "'Lemma S +
   extensivity' can fail to give admissibility." That clause is **false** and was never witnessed —
   `Gl` *fails* Lemma S, so it is not such a witness. On the extensive pole, Lemma S + extensivity
   (+CCC) **does** give admissibility (Theorem 2 + 1). The registry node text was already the correct
   half ("Lemma S itself can fail"); only the prose needed the fix, noted in the file.

## What this does and does NOT settle (for the grant)

- **Does:** the rigid/extensive pole of Neil's #1 `◁`-generality question is now a *characterization*,
  a single decidable test `π₀(X×Y) ≅ π₀X × π₀Y`. Design slogan upgraded from a necessary warning to a
  complete criterion on the cartesian side.
- **Does NOT:** the absorptive **dichotomy** (Conj 6.2 — rigid + flexible + tensors exhaust
  absorptivity, ⟹ no irreducible Gap-1 inhabitant) is untouched. Each pole now has a clean *sufficient*
  condition; the open question is whether a base that is *neither* extensive *nor* additive-fg can
  host a *mixed*-mechanism absorptive object. That is the remaining moonshot.

## One follow-up I'd like your steer on

Corollary 3.1 makes `π₀`-mult ⟹ connected-unit fall out *via* Theorem B. A **direct** diagram proof
of `π₀`-mult ⟹ connected would give an independent, possibly sharper route to Theorem B on the
extensive pole (and might drop a hypothesis). Worth a session, or is Theorem B's current proof already
where you want it?

— MacBeth
