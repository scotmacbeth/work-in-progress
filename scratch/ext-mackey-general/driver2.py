"""Second battery: D4, asymmetric A!=B, mixed towers, and the emergent-holonomy witness."""
from groups import Group
from driver import perm, run_case
from modules import Module, resolve_and_ext

MD = 4
res = []

# D4 = dihedral order 8 on 4 points: r=(1234), s=(13)
r = perm([[1, 2, 3, 4]], 4); s = perm([[1, 3]], 4)
D4 = [r, s]

# reflection subgroup <s>=<(13)> order2, and <r^2>=<(13)(24)> center
r2 = perm([[1, 3], [2, 4]], 4)
res.append(run_case("D4 A=B=<(13)> p2", D4, 4, [s], [s], 2, MD))
res.append(run_case("D4 A=B=<r^2>=center p2", D4, 4, [r2], [r2], 2, MD))
res.append(run_case("D4 A=<(13)> B=<(24)> p2 (non-conj refl in same class? )", D4, 4, [s], [perm([[2,4]],4)], 2, MD))
# asymmetric: A=<r> (cyclic order4), B=<s> order2  -> different indices
res.append(run_case("D4 A=<r> (C4) B=<s> p2 asymmetric", D4, 4, [r], [s], 2, MD))
res.append(run_case("D4 A={e} B=<s> p2 (Ext0 = index)", D4, 4, None, [s], 2, MD))

# S4 p2 : A=B=<(12)> ; heavier but n small
s4_12 = perm([[1,2]],4); s4_1234 = perm([[1,2,3,4]],4)
res.append(run_case("S4 A=B=<(12)> p2", [s4_12, s4_1234], 4, [s4_12], [s4_12], 2, 3))

# --- Emergent-holonomy witness: apply (star) with G:=U=Stab, A=Stab_P(s),B=Stab_{P'}(s).
# S3 = A3 . <(12)>, s=1 (index 0). U=Stab_{S3}(1)=<(23)>. A=Stab_{A3}(1)={e}, B=Stab_{<(12)>}(1)={e}.
# Then (star) over U: Ext^0_{kU}(k[U/A],k[U/B]) = |A\U/B| = h(s).
s23 = perm([[2,3]],3)
U = Group([s23], 3, "U=<(23)>")
# A=B={e} in U
print("--- Emergent-holonomy witness (S3=A3.<(12)>, s=1, U=<(23)>) ---")
res.append(run_case("holonomy: over U=<(23)>, A=B={e}  Ext0 should = h=2", [s23], 3, None, None, 2, MD))

# A larger emergent case: S4 = A4 . <(12)> ? not exact factorization dims: |A4|*2=24=|S4|, A4∩<(12)>={e}: YES exact.
# Take action of S4 on {1,2,3,4}, s=1. U=Stab_{S4}(1)=S3 on {2,3,4} (order6).
# A=Stab_{A4}(1)= even perms fixing 1 = A3 on {2,3,4} (order3). B=Stab_{<(12)>}(1): (12) moves 1 -> {e}.
# h(1)=|A\U/B| = |U|/(|A||B|) = 6/(3*1)=2.  Check Ext^0_{kU}=2 and full (star).
print("--- Emergent-holonomy witness 2 (S4=A4.<(12)>, s=1, U=S3, A=A3, B={e}) ---")
A3_on234 = perm([[2,3,4]],4)
s23_4 = perm([[2,3]],4)
# U = S3 on {2,3,4}
res.append(run_case("holonomy2: U=S3{2,3,4}, A=<(234)>=A3, B={e}  h=2", [A3_on234, s23_4], 4, [A3_on234], None, 2, MD))

print("BATTERY 2 ALL MATCH:", all(res))
