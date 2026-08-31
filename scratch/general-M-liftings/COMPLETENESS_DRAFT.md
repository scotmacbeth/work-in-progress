# Completeness draft — State liftings ≅ Cat

## The reduction data (recalled, proved)

Polynomial fibred monad lifting of State `M=(S^S, S)` ↔ family `(A_t)_{t∈S^S}`,
`A_t : Set^S → Set`, with:
- **counit** `ε : A_id(⟨V⟩) → V` natural in V  (ONLY on grade id);
- **comult** `δ_{T,(t_s)} : A_σ(s↦D(s,T(s))) → A_T(s↦A_{t_s}(D(s,−)))`,
  `σ(s)=t_s(T(s))`, natural in `D∈Set^{S×S}`;
- three monad laws (RU, LU, A).

**Purity (proved):** `A_t(Q)=∐_{j∈J_t} Q_{ρ(j)}^{Out(j)}`, `ρ(j)∈S` source, `Out(j)` a
finite set of out-positions. Write `s*=ρ(j)`. "Target state" of grade t at j is `t(s*)`.

## The routing constraint (naturality of δ, point-matching) — CLEAN DERIVATION

Nat transf between covariant poly functors of `D∈Set^{S×S}`:
`Nat(∐_a D^{U_a}, ∐_b D^{V_b}) ≅ ∏_a (∐_b ∏_{v∈V_b} U_{a}(pt(v)))`  — i.e. per Dom-shape `a`,
choose a Cod-shape `b` and match EACH output position `v` (reading point `pt(v)∈S×S`) BACKWARD
to an input position of `a` reading the SAME point.

- **Dom** `A_σ(s↦D(s,T(s)))`: shape `j∈J_σ`, source `s*=ρ(j)`, reads point `(s*, T(s*))`,
  multiplicity `Out(j)`. Only ONE point.
- **Cod** `A_T(s↦A_{t_s}(D(s,−)))`: shape `(i,f)`, `i∈J_T`, `f:Out(i)→J_{t_{ρ(i)}}`; reads
  points `(ρ(i), ρ(f(o)))` for `o∈Out(i)`, mult `Out(f(o))`.

**Routing (forced):** for `δ(j)=(i,f,β)`, whenever `(i,f)` has any output position:
- `ρ(i)=s*` (outer object shares j's source);
- `ρ(f(o))=T(s*)` for all `o∈Out(i)` (every inner object sits at the threaded state T(s*));
- `β: Σ_{o∈Out(i)} Out(f(o)) → Out(j)` backward on out-positions.

This is EXACTLY source-routed composition: outer reads s*, inner reads T(s*).

## Reading δ as a partial "composition"

Given the routing, δ at (T,(t_s)) and object j∈J_σ (source s*) produces:
- outer object `i = δ_out(j) ∈ J_T` with ρ=s*,
- for each o∈Out(i): inner object `f(o) ∈ J_{t_{s*}}` with ρ=T(s*),
- β assembling out-positions.

Think of j's out-positions as "morphisms out of j". The datum says: composite morphism p∈Out(j)
factors as (outer o∈Out(i)) then (inner o'∈Out(f(o))), via β.

## UNIT LAWS — pin identities and the "shadow"

**RU** factorization `(T=t, t_s=id ∀s)`, so σ=t. For j∈J_t (source s*):
δ_out(j)=i∈J_t (source s*); inner f(o)∈J_id (source t(s*)). Then A_t(ε) applies ε to inners,
selecting marked positions. RU=id forces:
  (RU1)  i = j  (outer object is j itself),
  (RU2)  the map o ↦ β(o, e_{f(o)}) : Out(j)→Out(j) is the identity,
where e_k∈Out(k) is the ε-marked position of k∈J_id.
⟹ each o∈Out(j) has a **target** object `tgt(o):=f(o)∈J_id`, source t(s*), and post-composing
   with its identity is trivial. Define `T_grade(o) = t(s*)` (state), `col(o)` = its J_id-object.

**LU** factorization `(T=id, t_s=t ∀s)`, so σ=t. For j∈J_t (source s*):
δ_out(j)=i∈J_id (source s*); inner f(o)∈J_t (source id(s*)=s*). ε on OUTER A_id selects marked
position e_i∈Out(i); reads inner f(e_i)∈J_t. LU=id forces:
  (LU1) f(e_i) = j,
  (LU2) β(e_i, −): Out(f(e_i))=Out(j) → Out(j) is the identity.
⟹ each j∈J_t has a **shadow** `sh(j):=i∈J_id`, source s*, with a marked out-position e whose
   inner regenerates j. Pre-composing j by sh(j)'s identity is trivial.

## The category at grade id (C̃), and grade-independence target

At grade id: objects J_id, out-positions Out(j), tgt:Out(j)→J_id (RU with t=id: tgt stays in
J_id, source id(s*)=s*), marked positions e_j (identities). Restricting δ to the SUB-family of
factorizations that keep everything at id... BUT NOTE: σ=id has factorizations with T≠id
(e.g. T=sw, t_s=sw). So grade id is NOT closed. The grades genuinely interact.

### KEY QUESTION for the crux (grade-independence):
Is J_t ≅ J_id (matching ρ and Out) for every t? Equivalent formulations:
(a) sh: J_t → J_id is a bijection respecting ρ, Out.
(b) Every object of J_id "extends" to a unique object of J_t over the 𝕊-arrow [t]_{s*}.

## Plan
- P2 (grade-indep): use A + sh/tgt to transport.
- P3 (holonomy): 𝕊 connected ⟹ single category; nontrivial transport breaks A (computed).
