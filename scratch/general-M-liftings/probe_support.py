"""Targeted grade-dependent-SUPPORT hunt (FAMILY M, degree 1, beta trivial -> no blowup).
Base = Sigma (one object per (grade,source)=8). Add k extra degree-1 objects at chosen
(grade,source) slots (total up to 10). A grade-dependent-support survivor would have some
source s with different object-counts across grades. fast-valid superset of full-valid, so
NO fast survivor => NO survivor."""
from itertools import product, combinations_with_replacement
import honest, grade_independence as gi
SS=honest.SS; ID=honest.ID; NM=honest.NM
slots=[(g,s) for g in SS for s in honest.S]

def sweep(max_extra=2, only_grade_dep=True):
    valid=[]; checked=0; toobig=0; dead=0
    # base: 1 everywhere; add extras via multiset of slots
    extrasets=[()]
    for k in range(1,max_extra+1):
        extrasets_k=list(combinations_with_replacement(range(8),k))
        extrasets=extrasets+extrasets_k
    seen=set()
    for extras in extrasets:
        n={sl:1 for sl in slots}
        for e in extras: n[slots[e]]+=1
        key=tuple(n[sl] for sl in slots)
        if key in seen: continue
        seen.add(key)
        if only_grade_dep and not gi.grade_dependent_M(n): continue
        A,obj_at=gi.build_M(n)
        found=False; big=False
        for delta in gi.enum_delta_M(A,obj_at):
            if delta is None: continue
            if isinstance(delta,tuple) and delta[0]=='TOOBIG': big=True; break
            for eps in gi.enum_eps_M(A,obj_at):
                if honest.check_laws_fast(A,eps,delta): found=True; break
            if found: break
        if big: toobig+=1; continue
        checked+=1
        if found: valid.append(n)
    return valid, checked, toobig

if __name__=="__main__":
    import sys
    me=int(sys.argv[1]) if len(sys.argv)>1 else 2
    valid,checked,toobig=sweep(max_extra=me)
    print(f"[SUPPORT HUNT] max_extra={me}: grade-dep profiles checked={checked} toobig={toobig} VALID={len(valid)}")
    for n in valid:
        print("   VALID grade-dependent:", gi.profile_sig_M(n))
