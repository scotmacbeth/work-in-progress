# Reader & State do NOT witness `cartesian ⊊ ∏-Mendler` — they fall *outside* ∏-Mendler (μ drops leaves)

**MacBeth — PROVE session, 2026-08-06.**
Target from `state/PROVE.md`: upgrade the *computed* claim "Reader and State are ∏-Mendler,
non-cartesian monads witnessing `cartesian ⊊ ∏-Mendler`" to *proved*. Companion to the crown
`2026-08-05-cartesian-preservation-nonbranching.md` / `-crown-gap-closure.md`.

## Headline (honest)

> **The PROVE.md theorem is FALSE.** Reader `E^(−)=(−)^E` and State `S⇒(S×−)` are **not**
> ∏-Mendler monads. Their `T_M(S,P)=(MS,P^⋆)` is a well-defined *endofunctor* on `Cont` and even
> carries a unit `η^T`, but it has **no multiplication `μ^T`**: the ∏-cointerpretation
> multiplication laxator `j` does not exist, because `μ` (the diagonal / state-threading) **drops
> leaves**, and the leaf-covering map `κ_μ` a natural `j` would reindex along is **not total**.
>
> The compute pass that produced PROVE.md identified a *single-valued diagonal* `δ:E→E×E` and
> called it "the ∏-Mendler `i_P`". That map is (i) about `μ`, not the unit; and (ii) **points the
> wrong way** — the required `j` runs `∏_{lv(μ mm)}→∏_{I(mm)}`, i.e. reindexing along
> `κ_μ : I(mm)→lv(μ mm)`, and `δ` is a section `lv(μ mm)→I(mm)` of the opposite variance. Its
> single-valuedness is irrelevant.
>
> **`cartesian ⊊ ∏-Mendler` is witnessed by `Pf` (powerset)** — already the crown's witness
> (`μ=∪` merges leaves, `κ_μ` total but non-injective). Reader/State are a *third*, distinct kind
> of non-cartesian monad — **leaf-dropping** — which lands them **outside** ∏-Mendler entirely,
> next to `Bag` (leaf-symmetric/analytic), not strictly between `cartesian` and the ∏-Mendler
> boundary.

The crown's *conclusion* ("Reader/State ∉ ∏-Mendler") was right all along. Its *stated reason*
(Lemma 1.3: "the unit `i_P` would have to be an iso, and Reader's is not") is imprecise — a natural
unit laxator `i_P` **does** exist for Reader. The decisive obstruction is the **multiplication**
`j`, corrected below.

---

## 0. Setup (all cited — see crown §5)

`p:Cont→Set`, `(S,P)↦S`. A morphism `(u,f):(S,P)→(T,Q)` is `u:S→T` **forward** and, backward,
a family `f_s:Q(us)→P(s)` (**target→source**). `M=(M,η,μ)` a Set-monad with support: each `m∈MX`
has a leaf set `lv(m)` with labels `x_b∈X` (`b∈lv(m)`). The ∏-cointerpretation lift (Ahman–Bauer
2409.17664 Thm 6.3):

- **Object.** `T_M(S,P)=(MS,P^⋆)`, `P^⋆(m)=∏_{b∈lv(m)}P(x_b)`.
- **Unit.** `η^T_{(S,P)}:(S,P)→(MS,P^⋆)`, forward `η^M_S`, backward
  `i_{P,s}:P^⋆(η^M s)=∏_{b∈lv(η s)}P(s)→P(s)`.
- **Mult.** `μ^T_{(S,P)}:T_MT_M(S,P)→T_M(S,P)`, forward `μ^M_S:MMS→MS`, backward
  `j_{mm}:P^⋆(μ^M mm)→(P^⋆)^⋆(mm)`, i.e.
  `∏_{L∈lv(μ mm)}P(\mathrm{lab}(L))\ \to\ ∏_{i∈I(mm)}P(\mathrm{lab}(i))`,
  where `I(mm):=⊔_{b∈lv(mm)}lv(\mathrm{inner}_b)` is the set of inner-leaf tokens `i=(b,c)`.

**Directions are forced by "`T_M` is a monad".** Both `i` and `j` are *backward* maps of container
morphisms, hence run **target→source**. So `j` runs `P^⋆(μ mm)→(P^⋆)^⋆(mm)` — from the (few) leaves
of `μ mm` to the (many) inner-leaf tokens. This is not a convention we may flip; it is what a monad
multiplication on `Cont` demands. (My 2026-07-27 entwining note line 114 wrote `ρ:lv(μ mm)→I(mm)`
for this map — a **direction slip**; harmless there since it did not affect the `Pf` conclusion, but
it is exactly the slip the compute pass amplified. Corrected here.)

---

## 1. The ∏-Mendler membership criterion (the exact statement, proved by Yoneda)

Write `S` for the (discrete) shape/label set, so a position family is `P∈[S,\mathbf{Set}]` and
`ev_a(P)=P(a)`. Both `P^⋆(μ mm)` and `(P^⋆)^⋆(mm)`, as functors of `P`, are **products of
evaluations**: `∏_{L}ev_{\mathrm{lab}(L)}` and `∏_{i}ev_{\mathrm{lab}(i)}`.

> **Lemma 1 (natural maps between products of evaluations are reindexings).**
> For finite index sets and labels `a_L,b_i∈S`,
> `\mathrm{Nat}_{P}\big(∏_{L}ev_{a_L},\ ∏_{i}ev_{b_i}\big)\ \cong\ ∏_{i}\{\,L : a_L=b_i\,\}.`
> In particular such a natural transformation **exists iff** for every output index `i` there is at
> least one input index `L` with `a_L=b_i`; and it is then a **reindexing** `(z_L)_L↦(z_{ρ(i)})_i`
> for a label-preserving `ρ:\{i\}→\{L\}`.

*Proof.* `∏_L ev_{a_L}=\mathrm{Hom}_{[S,\mathbf{Set}]}\!\big(⊔_L y_{a_L},-\big)` where `y_a=\mathrm{Hom}(a,-)`
is representable on the discrete `S` (so `y_a(x)=[a=x]`). By Yoneda, componentwise at output `i`,
`\mathrm{Nat}\big(\mathrm{Hom}(⊔_L y_{a_L},-),\ ev_{b_i}=\mathrm{Hom}(y_{b_i},-)\big)=\big(⊔_L y_{a_L}\big)(b_i)=⊔_{L}\,[a_L=b_i].`
So each output coordinate is a choice of an input coordinate with matching label — or, if none
matches, **there is no natural map to that coordinate at all** (the empty set), killing the whole
transformation. ∎

Applying Lemma 1 to `j` (`a_L=\mathrm{lab}(L)` over `L∈lv(μ mm)`, `b_i=\mathrm{lab}(i)` over
`i∈I(mm)`):

> **Criterion (∏-Mendler `j` exists).** A natural multiplication laxator `j_{mm}` exists **iff**
> there is a **total, label-preserving** function
> `κ_μ:I(mm)→lv(μ mm),\qquad \mathrm{lab}_{μ mm}(κ_μ(i))=\mathrm{lab}(i)\ \ \forall i∈I(mm).`
> `j` is then reindexing along `κ_μ`. Moreover:
> `κ_μ` **injective** ⟺ `μ^T` cartesian (no merge); `κ_μ` **non-total** ⟺ `μ` drops an inner leaf
> whose label is absent from `μ mm` ⟹ **no `j` at all**.

The same Lemma 1 applied to the **unit** `i_{P,s}:∏_{b∈lv(η s)}P(s)→P(s)` (all leaves of `η s`
labelled `s`) gives `\mathrm{Nat}(∏_{lv(η s)}ev_s,ev_s)=lv(η s)≠∅`: **a natural unit laxator always
exists** (project to any leaf), regardless of `|lv(η s)|`. So the unit is *not* where Reader is
excluded.

This is exactly the criterion the crown's `κ_μ` machinery (§0 of `-crown-gap-closure`) was reaching
for; Lemma 1 pins that it is **necessary and sufficient**, not merely sufficient, and that
**totality** — not just injectivity — is a real membership gate.

**Consistency check (the laxators are genuinely lax, not isos).** A–B's flagship ∏-Mendler example is
`Pf` (Ex 6.1), whose `κ_μ(i,x)=x` is **non-injective** (union merges). So `j` is *not* an iso for
`Pf`. Hence A–B's `i,j` cannot be required to be isomorphisms — were `j` an iso we would need `κ_μ`
bijective `=` cartesian, and `Pf` (non-cartesian) would be excluded, contradicting its being the
flagship. Dually the *unit* laxator `i_P` is lax too — so `|lv(η s)|=1` is **not** required by the unit.
This independently confirms the correction to crown Lemma 1.3 (§4.2): the exclusion of Reader is not a
unit-iso failure; it is the non-existence of the (lax) multiplication `j`.

---

## 2. `Pf` and `List` pass; `Reader`/`State` fail totality

**`Pf` (∏-Mendler, non-cartesian — the true witness of `cartesian ⊊ ∏-Mendler`).**
`mm=\{S_1,\dots,S_n\}∈\mathrm{Pf}\,\mathrm{Pf}\,X`, `μ mm=⋃_iS_i`. `I(mm)=⊔_iS_i` (tokens `(i,x)`,
`x∈S_i`), `lv(μ mm)=⋃S_i`. `κ_μ(i,x)=x` — **total** and label-preserving (`\mathrm{lab}(i,x)=x`),
hence `j` exists (`=` restriction/union laxator). It is **non-injective** whenever two sets share an
element (`(1,x),(2,x)↦x`), so `μ^T` is non-cartesian. *Computed:* `mm=\{\{0\},\{0,1\}\}` gives
`|I|=3>|lv(μ mm)|=2`, a forced merge (`kappa_test.py`). ✓

**`List` (cartesian).** `μ=` concat: `κ_μ` = "which position of the flattened list", total **and**
injective ⟹ `μ^T` cartesian. ✓

**`Reader_E=(−)^E`, `|E|=K≥2` (NOT ∏-Mendler).** `MX=X^E` (one shape, `E` leaves, labels = the
function's values). `mm=G∈(X^E)^E`; `μG(e)=G(e)(e)` (**diagonal**). `I(G)=E×E` (token `(e,e')`, label
`G(e)(e')`); `lv(μG)=E` (label of `e''` is `G(e'')(e'')`). A total label-preserving
`κ_μ:E×E→E` would need, for the **off-diagonal** token `(e,e')` (`e≠e'`), some `e''` with
`G(e'')(e'')=G(e)(e')`. But `G` is arbitrary, and there is a **uniform** witness that works for
**every `|E|≥2` at the minimum value-set size `|X|≥2`** (sharpening the earlier "large enough"):
take the **constant diagonal + one fresh off-diagonal**
`G(e)(e)=0\ (\forall e),\qquad G(0)(1)=1,\qquad G(e)(e')=0\ \text{otherwise}.`
Then `μG(e'')=G(e'')(e'')=0` for all `e''`, so **every** leaf of `μG` is labelled `0`; the label set
of `lv(μG)` is `\{0\}`. The inner token `(0,1)∈I(G)` has label `G(0)(1)=1∉\{0\}`. So no `e''` works
⟹ `κ_μ` is **not total** ⟹ (Lemma 1) **no natural `j`** ⟹ `T_{\mathrm{Reader}}` has no
multiplication ⟹ **Reader ∉ ∏-Mendler**, for all `|E|≥2` and `|X|≥2`. Only two ingredients are used —
an off-diagonal *position* (`|E|≥2`) and a *fresh label* for it (`|X|≥2`) — so the drop is genuinely
uniform in size, not a small-case artefact.

*Exhaustive witness (`general_drop.py`, `|X|=2`, `|E|∈\{2,\dots,8\}`):* for the `G` above, a
brute-force scan confirms **no** total label-preserving `κ_μ:E×E→E` exists (not merely that one fresh
label is unmatched). Earlier `|X|=3` witness `G(0)=(0,0),G(1)=(1,0)` (`kappa_test.py`) is the same
mechanism. ✓

**`State_S=S⇒(S×−)` (NOT ∏-Mendler) — reduced to the Reader diagonal.** `MX=(S×X)^S`; a leaf of
`m∈MX` is an input state `s∈S`, labelled by the value `\pi_X m(s)∈X`; the shape is `\pi_S m∈S^S`.
For `mm∈MMS`, write `mm(s_0)=(h(s_0),F(s_0))` — outer shape `h∈S^S`, inner computations `F(s_0)∈MS`.
The State multiplication **threads the state**: `μ(mm)(s_0)=F(s_0)(h(s_0))`, so `μ(mm)` reads each
inner computation **only at the threaded state** `s_1=h(s_0)`; the inner leaves at states `≠h(s_0)`
are **dropped**. Inner tokens are `I(mm)=S×S` (token `(s_0,s_1)`, label `\pi_XF(s_0)(s_1)`);
`lv(μ mm)=S` (leaf `s_0`, label `\pi_XF(s_0)(h(s_0))`).

**Take the outer shape `h=\mathrm{id}_S`.** Then `μ(mm)(s_0)=F(s_0)(s_0)` — the threaded labels are the
**diagonal** `\pi_XF(s_0)(s_0)`, *exactly* Reader's `μG(e)=G(e)(e)` transported onto the `X`-labels.
The uniform Reader witness ports verbatim: set the diagonal constant `\pi_XF(s)(s)=0\ (\forall s)` and
one fresh off-token `\pi_XF(0)(1)=1` (`S`-parts arbitrary). Then `lv(μ mm)` is all-`0`-labelled while
the token `(0,1)∈I(mm)` has label `1∉\{0\}` ⟹ `κ_μ` not total ⟹ no `j` ⟹ **State ∉ ∏-Mendler**, for
all `|S|≥2`, `|X|≥2`.

So State's extra `S^S`-many shapes (its *branching*) are **irrelevant** to the drop: the single
identity shape already breaks totality, and on that shape State's `μ` *is* Reader's diagonal `μ`.
Reader and State share **one** mechanism — the diagonal leaf-drop — and differ only in shape-
multiplicity. *Exhaustive witness:* `general_drop.py` (`h=\mathrm{id}`, `|X|=2`, `|S|∈\{2,\dots,8\}`)
confirms no total `κ_μ`; `kappa_test.py` reports NOT TOTAL for `State`, `S=3`. ✓

---

## 3. What is actually true about Reader/State (salvage)

Points **1** and **3** of PROVE.md survive; points **2** and **4** are refuted.

- **(P1, TRUE) Both are polynomial (container) functors.** Reader `=y^E` (monomial), State
  `≅∑_{h:S→S}y^S`; `M(u)` fixes the leaf set (`u_*` bijective, **cartFun**). *(counting in
  `state-monad-boundary/compute.py` Q1 still stands.)*
- **(P3, TRUE) Neither `μ` is cartesian.** In fact something *stronger* than "non-cartesian" holds:
  their `μ` **drops** leaves (`κ_μ` non-total), a strictly worse failure than merging (`Pf`,
  `κ_μ` non-injective-but-total). This is why they cannot even be given a container-monad `μ^T`.
- **(P2, FALSE)** "Both are ∏-Mendler monads" — refuted (§2). The single-valued `δ:E→E×E` the
  compute pass exhibited is the **wrong-variance** map (a section of `κ_μ`), not `j`.
- **(P4, FALSE)** "List ⊊ {Reader,State} (∏-Mendler) ⊊ boundary" — refuted. Reader/State are
  **outside** ∏-Mendler; they are not a rung of the ladder between cartesian and the boundary.

**The corrected census — a trichotomy of non-cartesian `μ` by how `κ_μ` fails:**

```
   κ_μ:              total   injective   in ∏-Mendler?   named monads
   ─────────────────────────────────────────────────────────────────────
   cartesian         yes     yes         YES             Id, Maybe, Writer, List
   MERGE (share)     yes     NO          YES             Pf   ← witnesses cartesian ⊊ ∏-Mendler
   DROP (diagonal)   NO      —           NO              Reader, State
   SYMMETRY (P^⋆ ill-defined, label-fixing leaf swap)   NO              Bag (multisets)
```

So the ∏-Mendler class is exactly the polynomial-functor monads whose `μ` **drops no leaf** (`κ_μ`
total) **and** has **rigid labels** (`P^⋆` well-defined; excludes `Bag`, crown §7). Merging is
*allowed* (that is the whole content of `cartesian ⊊ ∏-Mendler`, witnessed by `Pf`); dropping is
not. `Reader`/`State` are the canonical **leaf-dropping** monads and sit outside ∏-Mendler on the
polynomial side, symmetrically opposite `Bag` on the analytic side. This is a **richer** boundary
picture than PROVE.md conjectured — three named failure modes, not one extra rung.

---

## 4. Corrections to the prior notes (the honesty deliverable)

1. **Compute pass (`state-monad-boundary/compute.py`, PROVE.md §2):** "Reader `i_P=Δ:E→E×E`
   single-valued ⟹ ∏-Mendler" is **wrong twice**: (a) `i_P` names the *unit* laxator, but `Δ` is a
   map about `μ`; (b) the multiplication laxator `j` has the **opposite variance** to `Δ` — it
   reindexes along `κ_μ:I(mm)→lv(μ mm)`, which for Reader is **not total** (off-diagonal drop).
   Single-valuedness of the wrong-direction section is irrelevant to `j`'s existence.

2. **Crown Lemma 1.3 / `crown-boundary-table` node ("Reader excluded: no `i_P`"):** the *conclusion*
   (Reader/State ∉ ∏-Mendler) is **correct and unchanged**, but the *reason* should read: a natural
   **unit** laxator `i_P` *does* exist for Reader (Lemma 1, `\mathrm{Nat}(∏_{lv(η s)}ev_s,ev_s)≠∅`);
   the decisive obstruction is the **multiplication** laxator `j` (Reader's diagonal `μ` drops
   off-diagonal leaves ⟹ `κ_μ` non-total ⟹ no `j`). The phrase "no `i_P`" conflated "unit laxator
   fails to be an *iso*" (true, but not required) with "no ∏-Mendler structure" (true, but for the
   `j` reason). Recommend amending the node's `approach` text accordingly (no trust change).

3. **Entwining note (`2026-07-27` line 114):** `ρ_{mm}:lv(μ mm)→\{(b,c)\}` should be
   `κ_μ:I(mm)→lv(μ mm)` (reindexing runs opposite to the map). Direction slip; conclusion
   (E2 for `Pf`) unaffected because `Pf`'s `κ_μ` is total either way.

---

## 5. Verification (computational)

`scratch/pi-mendler-boundary/kappa_test.py` — for every `mm` over small data, tests existence of a
total label-preserving `κ_μ:I(mm)→lv(μ mm)`:

- **Reader** (`S=3`): NOT total — witness `G=((0,0),(1,0))`, `μG=(0,0)`, dropped label `1`.
- **State** (`S=3`): NOT total — state-threading drops the off-state inner leaf.
- **Pf**, **List**: total for all `mm` ⟹ `j` exists.
- Supplement 1: within the total cases, `Pf` forces a **non-injective** `κ_μ` (`|I|=3>|lv(μ)|=2`)
  = merge = non-cartesian; `List` admits injective `κ_μ` = cartesian.
- Supplement 2: Reader's off-diagonal drop persists for `|E|∈\{2,3,4,5\}` (general `K≥2`).
- **`general_drop.py` (2026-08-06):** the *uniform* `|X|=2` witness — constant diagonal + one fresh
  off-diagonal — gives an **exhaustive** no-total-`κ_μ` for Reader (`|E|∈\{2,\dots,8\}`) and for State
  under `h=\mathrm{id}` (`|S|∈\{2,\dots,8\}`), closing item (C) (§2, §6).

The underlying **Lemma 1** (Yoneda) makes these finite checks conclusive: `j` is natural iff `κ_μ`
is total, with no escape via non-reindexing maps. *Independently re-derived (2026-08-06):* the full
Yoneda chain is `∏_{L}ev_{a_L}=\mathrm{Hom}(⊔_L y_{a_L},-)`, then
`\mathrm{Nat}(\mathrm{Hom}(⊔_Ly_{a_L},-),\mathrm{Hom}(y_{b_i},-))\cong(⊔_Ly_{a_L})(b_i)=⊔_L[a_L=b_i]`,
so each output coordinate is a matching input coordinate or the whole hom-set is empty — the criterion
is necessary **and** sufficient, and the direction (`I(mm)→lv(μ mm)`, many→few) is forced by
"`μ^T` is a backward container map (target→source)". ✓

---

## 6. Scope / gaps

- **`State`/`Reader` general argument — CLOSED (2026-08-06 supplement, §2).** The drop is proved
  symbolically for **all** `|E|,|S|≥2` at the minimal value-set size `|X|≥2` via the uniform
  constant-diagonal + one-fresh-off-diagonal witness, and State is reduced to the Reader diagonal by
  taking outer shape `h=\mathrm{id}` (exhaustive no-total-`κ_μ` in `general_drop.py`, `|E|,|S|∈\{2..8\}`).
  This is exactly PROVE.md item (C): the non-totality is established by the Lemma-1 Yoneda criterion,
  not by small cases alone.
- **A–B Def 6.2 exact wording.** My deep-read (`sources.json` 2409.17664: "laxators `i_P` and
  `j_{Q,f}` + coherence diagrams", extraction = deep-read Sec 6) says the structure maps are
  *laxators* (one-directional), consistent with §1. The membership verdict here is derived directly
  from "`T_M` is a monad on `Cont`", which forces the laxator directions independently of A–B's
  packaging — so the conclusion does not rest on re-reading their coherence diagrams. Should a
  future pass want the A–B-internal statement, the target is: their `j_{Q,f}` laxator = my
  `κ_μ`-reindexing; their class = "`κ_μ` total, labels rigid".
- **`cartesian ⊊ ∏-Mendler` strictness** is unaffected and remains witnessed by `Pf` (crown §2),
  not Reader/State.

---

## 7. One line

Reader and State are **not** ∏-Mendler: `T_M` loses its multiplication because their `μ` **drops
leaves** (`κ_μ` non-total), a failure the ∏-cointerpretation cannot tolerate (unlike `Pf`'s
merging, which it can). PROVE.md's census rung is deleted; the true boundary is a **trichotomy**
— merge (`Pf`, inside) vs drop (`Reader/State`, outside) vs symmetry (`Bag`, outside) — and
`cartesian ⊊ ∏-Mendler` keeps its classical witness `Pf`.
