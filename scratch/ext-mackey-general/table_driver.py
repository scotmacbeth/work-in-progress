"""Table driver: sweep (G,A,B), report h, Ext^0,1,2, (Ext0-Ext1), #transverse double cosets.
Uses the verified engine (groups.py, modules.py). Every row cross-checks LHS==RHS."""
from itertools import combinations
from groups import Group, closure, identity
from modules import Module, resolve_and_ext
from driver import perm, ext_LHS, ext_RHS

def all_subgroups(G):
    """All subgroups of G as frozensets of element-indices (via closure of element subsets)."""
    idx_elts = list(range(G.order))
    subs = set()
    # generate by closure of small generating subsets (up to 2 generators suffices for these groups)
    subs.add(frozenset([G.index[G.e]]))
    for i in idx_elts:
        Hi = frozenset(G.subgroup_indices([G.elts[i]]))
        subs.add(Hi)
    for i, j in combinations(idx_elts, 2):
        Hij = frozenset(G.subgroup_indices([G.elts[i], G.elts[j]]))
        subs.add(Hij)
    return sorted(subs, key=lambda s: (len(s), sorted(s)))

def sub_label(G, Hidx):
    """Human label: order + generating reflection/rotation description via cycle form of a nontrivial gen."""
    Hidx = sorted(Hidx)
    if len(Hidx) == 1:
        return "{e}"
    if len(Hidx) == G.order:
        return "G"
    # list nontrivial elements' cycle notation
    def cyc(gi):
        p = G.elts[gi]; seen=[False]*G.n; parts=[]
        for st in range(G.n):
            if seen[st] or p[st]==st:
                seen[st]=True; continue
            c=[]; x=st
            while not seen[x]:
                seen[x]=True; c.append(x+1); x=p[x]
            if len(c)>1: parts.append("("+"".join(str(z) for z in c)+")")
        return "".join(parts) if parts else "e"
    nontriv=[gi for gi in Hidx if G.elts[gi]!=G.e]
    return f"<{','.join(cyc(gi) for gi in nontriv[:2])}>(ord{len(Hidx)})"

def analyze(G, Aidx, Bidx, p, maxdeg):
    lhs, betti = ext_LHS(G, Aidx, Bidx, p, maxdeg)
    rhs, detail, ndc = ext_RHS(G, Aidx, Bidx, p, maxdeg)
    transverse = sum(1 for (_, o, _) in detail if o == 1)
    return {
        "h": ndc, "ext": lhs, "rhs": rhs, "match": lhs == rhs,
        "diff": lhs[0] - lhs[1], "transverse": transverse,
        "detail": [(o, c[:maxdeg+1]) for (_, o, c) in detail], "betti": betti,
    }

def sweep(name, gens, n, p, maxdeg=2):
    G = Group(gens, n, name)
    subs = all_subgroups(G)
    print(f"\n########## SWEEP {name}  |G|={G.order}  p={p}  (#subgroups={len(subs)}) ##########")
    print(f"{'A':<26}{'B':<26}{'h':>3}{'Ext0':>6}{'Ext1':>6}{'Ext2':>6}{'d0-d1':>7}{'#trans':>8}  match")
    rows=[]
    for Aidx in subs:
        for Bidx in subs:
            if sorted(Bidx) < sorted(Aidx):  # unordered pairs only (A<=B canonical)
                continue
            r = analyze(G, list(Aidx), list(Bidx), p, maxdeg)
            la, lb = sub_label(G, Aidx), sub_label(G, Bidx)
            e = r["ext"]
            print(f"{la:<26}{lb:<26}{r['h']:>3}{e[0]:>6}{e[1]:>6}{e[2]:>6}{r['diff']:>7}{r['transverse']:>8}  {r['match']}")
            rows.append((name, la, lb, r))
    return rows

def spotlight(name, gens, n, Agens, Bgens, p, maxdeg=4):
    G = Group(gens, n, name)
    Aidx = G.subgroup_indices(Agens) if Agens else [G.index[G.e]]
    Bidx = G.subgroup_indices(Bgens) if Bgens else [G.index[G.e]]
    r = analyze(G, Aidx, Bidx, p, maxdeg)
    print(f"\n--- SPOTLIGHT {name} ---")
    print(f"  A={sub_label(G,Aidx)}  B={sub_label(G,Bidx)}")
    print(f"  h=|A\\G/B|={r['h']}   Ext tower (LHS)={r['ext']}   RHS={r['rhs']}   MATCH={r['match']}")
    print(f"  intersection (order, H^*): {r['detail']}")
    print(f"  Ext0={r['ext'][0]}  Ext1={r['ext'][1]}  (Ext0-Ext1)={r['diff']}  #transverse={r['transverse']}")
    return r

if __name__ == "__main__":
    # ============ D8 = D4 dihedral order 8 on 4 points ============
    r = perm([[1,2,3,4]],4); s = perm([[1,3]],4)
    D8 = [r,s]; nD=4

    # ============ V4 = (Z/2)^2 on 4 points ============
    a = perm([[1,2]],4); b = perm([[3,4]],4)
    V4 = [a,b]; nV=4

    # ============ V8 = (Z/2)^3 on 6 points ============
    x = perm([[1,2]],6); y = perm([[3,4]],6); z = perm([[5,6]],6)
    V8 = [x,y,z]; nV8=6

    # ---- Required spotlights (deep towers, maxdeg=4, tower sanity) ----
    print("="*70); print("REQUIRED SPOTLIGHT CASES (maxdeg=4, LHS vs RHS cross-check)"); print("="*70)
    spotlight("D8 A=B=<s>=<(13)> (non-normal reflection)", D8, nD, [s], [s], 2)
    spotlight("D8 A=B=G (diagonal control)", D8, nD, [r,s], [r,s], 2)
    spotlight("V4 A=B=G (diagonal control)", V4, nV, [a,b], [a,b], 2)
    spotlight("V4 A=B=<a> self", V4, nV, [a], [a], 2)
    spotlight("V4 A=<a> B=<b> transverse", V4, nV, [a], [b], 2)

    # ---- Full sweeps (maxdeg=2 table) ----
    print("\n"+"="*70); print("FULL SUBGROUP-PAIR SWEEPS (unordered pairs, maxdeg=2)"); print("="*70)
    sweep("D8", D8, nD, 2)
    sweep("V4", V4, nV, 2)
    sweep("V8", V8, nV8, 2)
