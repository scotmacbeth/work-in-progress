## What I'm trying to show
Grade-independence: for a polynomial fibred monad lifting of State (|S|=2), the object family
J_t^s (source-s objects at grade t) is independent of grade t: J_t^s ≅ J_id^s matching
out-position sets. Concretely: sh_t and pr_t (both = δ_out of specific factorizations) are
inverse bijections J_t^s ↔ J_id^s.

## What's going wrong
Unit laws give sh_t: J_t^s → J_id^s (LU) and pr_t: J_id^s → J_t^s (a σ=id factorization),
verified inverse on all 𝕊×C. But I can't force them inverse abstractly: LU makes
δ_{(id,(t))} split-mono but that doesn't make δ_out=sh_t injective (two j,j' can share a
shadow with different inner f). Injectivity/surjectivity must come from ASSOCIATIVITY, and I
can't cleanly identify the associativity instance. Free-δ enumeration is walled (10^12).

## Every Assumption I Am Making

### About the objects
1. J_t is finite (polynomial hypothesis). — TRUE (polynomial).
2. Each object reads exactly one source state (purity). — PROVED.
3. The counit gives a marked position per A_id object. — PROVED (Reader Step A).
4. Objects at grade t≠id have NO marked position. — TRUE (counit only at id). ← suspicious?
5. J_t^s and J_id^s are a priori different sets that need a bijection. — assumption.

### About the maps
6. δ_out(j) is a well-defined function J_σ^s → J_T^s. — TRUE (δ is a function of domain obj).
7. sh_t = δ_out of (id,(t,...)); pr_t = δ_out of (t,(t'_s)) with σ=id. — DEFINITION.
8. pr_t is independent of the CHOICE of (t'_s) with σ=id. — UNTESTED! multiple t'_s give σ=id.
9. sh_t injective. — UNTESTED (the blocker).
10. The transport ψ_φ=δ_out "composes" under associativity (functorial). — UNTESTED, the hoped tool.
11. β (backward on positions) is essentially trivial in the unit factorizations. — from RU2/LU2.

### About definitions / prior results
12. Reader classification applies to the (id,id)-restricted sub-structure with E:=S. — PROVED (P1).
13. "polynomial comonad ≅ small category" (ACU) — cited, TRUE.
14. The routing constraint (point-matching) is exactly naturality of δ. — PROVED.
15. Associativity of the State monad = the honest engine's assoc check. — TRUE.

### About the problem
16. Completeness (State liftings ≅ Cat) is TRUE. — CONJECTURE (could be false: grade-dep survivor).
17. Grade-independence is the right first target. — assumption (PROVE.md flags it as crux).
18. The proof must go through sh/pr bijection. — assumption; maybe a different invariant.
19. δ_out is the right thing to track (vs the whole δ with f, β). — assumption.

### Too obvious
20. A_t for different t are "the same kind of object". — the whole question.
21. The grade t enters δ_out(j) only through T (the outer), not through the inner t_s. — CHECK.
22. Purity's "target state t(ρ(j))" is intrinsic to j. — but t is the grade; target depends on grade.
23. There's a single global category, not per-source. — that's source-independence, SEPARATE from grade-indep.

## Challenging the suspects

### Assumption 8 (pr_t independent of choice of t'_s): TEST
If pr_t depends on the choice, then "pr_t" isn't canonical and my inverse claim is ill-posed.
NATURALITY might force independence. TEST computationally on 𝕊×C with different t'_s choices.

### Assumption 21 (grade enters δ_out only via T): 
For sh_t: factorization (id,(t)), T=id always. So sh_t's OUTER grade is id regardless of t;
the grade t enters only through the INNER t_s=t. So δ_out lands in J_T^s=J_id^s. The grade-t
info is in the inner. So sh_t "reads off" the shadow WITHOUT the outer knowing t. Interesting.

### Assumption 9 + 10: the real blocker. 
Maybe the right tool is NOT associativity of δ_out but the FULL δ including β, via the
comonad structure at fixed source. Reconsider.

### Assumption 4/22: MOST SUSPICIOUS.
"Objects at grade t≠id have no marked position, and their target depends on grade t."
Re-examine: is the object j∈J_t^s REALLY grade-dependent data, or is it the SAME underlying
object as some c∈Ob C̃_s (an A_id object) that merely SITS at grade t? The bijection sh_t
says: yes, j corresponds to sh(j)∈J_id^s. If I could show sh_t is a bijection NATURALLY (via
a universal property of A_id objects), grade-independence follows. The universal property:
A_id objects = the ones with identities. Maybe EVERY object, at every grade, must have an
"identity witness" forced by... the RIGHT UNIT applied cleverly.
