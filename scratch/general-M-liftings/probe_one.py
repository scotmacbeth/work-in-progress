"""One minimal grade-dependent-support profile, cap raised, single-profile exhaustive."""
import grade_independence as gi, honest
gi.args_cap = 20_000_000
SS=honest.SS; ID=honest.ID; NM=honest.NM; GN=gi.GN
# base 1 everywhere; sw source0 -> 2 objects. total=9. grade-dependent (J_sw^0=2, J_id^0=1)
n={(g,s):1 for g in SS for s in honest.S}
SW=GN['sw']
n[(SW,0)]=2
print("profile:", gi.profile_sig_M(n), "grade-dep:", gi.grade_dependent_M(n))
A,obj_at=gi.build_M(n)
# count delta product size
import itertools
cnt=0; found=False; big=False
for delta in gi.enum_delta_M(A,obj_at):
    if delta is None: continue
    if isinstance(delta,tuple) and delta[0]=='TOOBIG':
        big=True; print("TOOBIG total=",delta[1]); break
    for eps in gi.enum_eps_M(A,obj_at):
        cnt+=1
        if honest.check_laws_fast(A,eps,delta):
            found=True; print("VALID FOUND", eps); break
    if found: break
print("checked (delta,eps) pairs:", cnt, "found:", found, "big:", big)
