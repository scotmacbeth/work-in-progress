"""Verify (★): Ext^n_{kG}(k[G/A],k[G/B]) =? sum over A\G/B of H^n(A ∩ gBg^{-1}; k)."""
from groups import Group, compose
from modules import Module, resolve_and_ext

def perm(cycle_list, n):
    """Build permutation on {0..n-1} from list of cycles (1-indexed cycles for readability)."""
    p = list(range(n))
    for cyc in cycle_list:
        c = [x - 1 for x in cyc]
        for i in range(len(c)):
            p[c[i]] = c[(i + 1) % len(c)]
    return tuple(p)

def group_cohomology(G, Hidx, p, maxdeg):
    """H^n(H;k) for n=0..maxdeg, H given as element-index subset of G. Build H as its own group."""
    if len(Hidx) == 1:
        return [1] + [0] * maxdeg  # trivial group
    Hperms = [G.elts[i] for i in Hidx]
    Hg = Group(Hperms, G.n, name="H")
    triv = Module.trivial(Hg, p)
    dims, betti = resolve_and_ext(Hg, triv, triv, p, maxdeg)
    return dims

def ext_LHS(G, Aidx, Bidx, p, maxdeg):
    M = Module.permutation_GmodH(G, Aidx, p)
    N = Module.permutation_GmodH(G, Bidx, p)
    dims, betti = resolve_and_ext(G, M, N, p, maxdeg)
    return dims, betti

def ext_RHS(G, Aidx, Bidx, p, maxdeg):
    dcs = G.double_cosets(Aidx, Bidx)
    total = [0] * (maxdeg + 1)
    detail = []
    for (gi, dc) in dcs:
        gBg = G.conjugate_subgroup(Bidx, gi)
        Hg = G.intersect_subgroups(Aidx, gBg)
        coh = group_cohomology(G, Hg, p, maxdeg)
        detail.append((gi, len(Hg), coh))
        for n in range(maxdeg + 1):
            total[n] += coh[n]
    return total, detail, len(dcs)

def run_case(name, gens, n, Agens, Bgens, p, maxdeg):
    G = Group(gens, n, name)
    Aidx = G.subgroup_indices(Agens) if Agens else [G.index[G.e]]
    Bidx = G.subgroup_indices(Bgens) if Bgens else [G.index[G.e]]
    lhs, betti = ext_LHS(G, Aidx, Bidx, p, maxdeg)
    rhs, detail, ndc = ext_RHS(G, Aidx, Bidx, p, maxdeg)
    ok = lhs == rhs
    print(f"=== {name}  |G|={G.order} p={p}  |A|={len(Aidx)} |B|={len(Bidx)} ===")
    print(f"  #(A\\G/B) = {ndc};   intersection orders/cohom: {[(o,c) for (_,o,c) in detail]}")
    print(f"  LHS Ext (direct kG resolution): {lhs}   [betti {betti}]")
    print(f"  RHS Mackey sum H^*(A∩gBg^-1):   {rhs}")
    print(f"  Ext^0 = {lhs[0]}   (should be #double cosets = {ndc})")
    print(f"  MATCH: {ok}\n")
    return ok

if __name__ == "__main__":
    MD = 4
    results = []

    # Case 1: V4, A=<a>, B=<b>  transverse
    a = perm([[1, 2]], 4); b = perm([[3, 4]], 4)  # on 4 points: a=(12), b=(34): V4
    results.append(run_case("V4 A=<(12)> B=<(34)> p2 (transverse)",
                            [a, b], 4, [a], [b], 2, MD))

    # Case 2: V4, A=B=<a>
    results.append(run_case("V4 A=B=<(12)> p2",
                            [a, b], 4, [a], [a], 2, MD))

    # Case 3: S3, A=B=<(12)>  (Sylow-2)
    s12 = perm([[1, 2]], 3); s123 = perm([[1, 2, 3]], 3)
    results.append(run_case("S3 A=B=<(12)> p2",
                            [s12, s123], 3, [s12], [s12], 2, MD))

    # Case 4: S3 regular rep A=B={e} p2
    results.append(run_case("S3 A=B={e} p2 (regular)",
                            [s12, s123], 3, None, None, 2, MD))

    # Case 5: S3 A=<(12)>, B=<(13)>  transverse-ish (distinct order2)
    s13 = perm([[1, 3]], 3)
    results.append(run_case("S3 A=<(12)> B=<(13)> p2",
                            [s12, s123], 3, [s12], [s13], 2, MD))

    # Case 6: Z/3 p=3, A=B=G
    c3 = perm([[1, 2, 3]], 3)
    results.append(run_case("Z3 A=B=G p3",
                            [c3], 3, [c3], [c3], 3, MD))

    # Case 7: Z/3 p=3 regular A=B={e}
    results.append(run_case("Z3 A=B={e} p3 (regular)",
                            [c3], 3, None, None, 3, MD))

    # Case 8: A4 p2, A=B=V4 (normal Sylow-2)
    # A4 on 4 points
    a4_3 = perm([[1, 2, 3]], 4); a4_2 = perm([[1, 2], [3, 4]], 4)
    results.append(run_case("A4 A=B=V4 p2",
                            [a4_3, a4_2], 4, [a4_2, perm([[1,3],[2,4]],4)], [a4_2, perm([[1,3],[2,4]],4)], 2, 3))

    # Case 9: A4 p2, A=B=<(12)(34)> order2
    results.append(run_case("A4 A=B=<(12)(34)> p2",
                            [a4_3, a4_2], 4, [a4_2], [a4_2], 2, 3))

    print("ALL MATCH:", all(results))
