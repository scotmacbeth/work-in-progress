import numpy as np
from gen_d8 import (build_D8, gen_subgroup, double_cosets, conj_intersection,
                    perm_module_GmodH, ext_tower, H_elemab_dims, mod2)

LEN = 6  # degrees 0..6

def verify_group(G):
    # closure + associativity spot check on all triples is 8^3=512, cheap
    for i in range(G.N):
        for j in range(G.N):
            for k in range(G.N):
                if G.mt[G.mt[i][j]][k] != G.mt[i][G.mt[j][k]]:
                    return False, (i,j,k)
    # identity
    for i in range(G.N):
        if G.mt[G.e][i] != i or G.mt[i][G.e] != i: return False, ('id', i)
    # inverses
    for i in range(G.N):
        if G.inv[i] is None: return False, ('inv', i)
    return True, None

def subgroup_type(G, H):
    """Identify elementary-abelian rank; return s such that H ~= (Z/2)^s (for the
    small 2-subgroups here). |H|=1->0, 2->1, 4 (Klein)->2."""
    n = len(H)
    # check exponent 2 & abelian
    ok = all(G.mt[h][h] == G.e for h in H)
    ab = all(G.mt[h][k] == G.mt[k][h] for h in H for k in H)
    if not (ok and ab):
        return None  # not elementary abelian (e.g. cyclic C4 or D8 itself)
    import math
    s = int(round(math.log2(n)))
    return s

def mackey_prediction(G, Aels, Bels, name):
    dcs = double_cosets(G, Aels, Bels)
    h = len(dcs)
    pred = np.zeros(LEN+1, dtype=int)
    print(f"  A\\G/B : {h} double coset(s)")
    for (g, cs) in dcs:
        inter = conj_intersection(G, Aels, Bels, g)
        s = subgroup_type(G, inter)
        gname = G.names[g]
        if s is None:
            # fall back: for D8 the only non-elem-abelian subgroups are C4 and D8
            # handle via direct name
            print(f"    g={gname:4s} |AgB|={len(cs)}  A∩gBg^-1 = {[G.names[x] for x in inter]} (NOT elem-ab, size {len(inter)})")
            if len(inter) == 8:
                dims = [1,2,3,4,5,6,7][:LEN+1]  # H*(D8)
            elif len(inter) == 4:  # C4
                # H*(Z/4;F2): dim 1 each degree
                dims = [1]*(LEN+1)
            else:
                raise RuntimeError("unexpected subgroup")
        else:
            dims = H_elemab_dims(s, LEN)
            print(f"    g={gname:4s} |AgB|={len(cs)}  A∩gBg^-1 = {[G.names[x] for x in inter]}  ~ (Z/2)^{s}  H*={dims}")
        pred += np.array(dims, dtype=int)
    print(f"  Mackey/Shapiro prediction  Ext^0..{LEN} = {list(pred)}")
    return list(pred), h

def direct_ext(G, Aels, Bels):
    modA = perm_module_GmodH(G, Aels)   # k[G/A]
    modB = perm_module_GmodH(G, Bels)   # k[G/B]
    ext, betti = ext_tower(G, modA, modB, LEN)
    return ext, betti, modA['d'], modB['d']

def run_case(G, els, Agen, Bgen, title):
    Aels = gen_subgroup(G, Agen); Bels = gen_subgroup(G, Bgen)
    print("="*70)
    print(f"CASE: {title}")
    print(f"  A = <{[G.names[x] for x in Agen]}> = {[G.names[x] for x in Aels]}")
    print(f"  B = <{[G.names[x] for x in Bgen]}> = {[G.names[x] for x in Bels]}")
    pred, h = mackey_prediction(G, Aels, Bels, title)
    ext, betti, dA, dB = direct_ext(G, Aels, Bels)
    print(f"  DIRECT resolution: dim k[G/A]={dA}, dim k[G/B]={dB}, betti={betti}")
    print(f"  DIRECT Ext^0..{LEN}          = {ext}")
    match = (ext == pred)
    print(f"  MATCH: {match}")
    return match

if __name__ == "__main__":
    G, els = build_D8()
    ok, info = verify_group(G)
    print(f"D8 group axioms verified: {ok}  {info if not ok else ''}")
    print(f"D8 elements: {G.names}")
    print()

    results = []
    # sanity: full group
    results.append(run_case(G, els, [els['r'], els['s']], [els['r'], els['s']],
                            "A=B=G=D8  (sanity: H*(D8;F2))"))
    print()
    # two Klein fours (the PROVE-file suggested case)
    results.append(run_case(G, els, [els['r2'], els['s']], [els['r2'], els['rs']],
                            "A=<r2,s>, B=<r2,rs>  (two Klein fours -- both NORMAL)"))
    print()
    # genuine non-collapse: A=B=<s>
    results.append(run_case(G, els, [els['s']], [els['s']],
                            "A=B=<s>  (order-2 reflection, NON-normal)"))
    print()
    # asymmetric reflections
    results.append(run_case(G, els, [els['s']], [els['rs']],
                            "A=<s>, B=<rs>  (two different reflections)"))
    print()
    # Klein four vs reflection
    results.append(run_case(G, els, [els['r2'], els['s']], [els['s']],
                            "A=<r2,s> (Klein), B=<s> (reflection)"))
    print()
    # cyclic C4 vs reflection
    results.append(run_case(G, els, [els['r']], [els['s']],
                            "A=<r>=C4, B=<s> (transverse: A∩B trivial, single coset)"))
    print()
    print("="*70)
    print(f"ALL CASES MATCH: {all(results)}   ({sum(results)}/{len(results)})")
