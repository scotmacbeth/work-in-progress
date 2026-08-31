"""
Task 1 (part A): Search FIXED bivariate symmetric polynomials F(a,b) = sum c_ij a^i b^j
(i,j in 0..D, c_ij >= 0 integers, c_ij = c_ji) that are:
  - unital: F(e,b) = b for all b, with e in {0,1}
  - associative on cardinalities: F(F(a,b),c) = F(a,F(b,c))
and detect whether ANY has per-variable degree >= 2 (=> arity >= 2 for some R_b).

A jointly-polynomial F corresponds to R_b polynomial with bounded arity.
"""
import itertools, sys

def evalF(c, D, a, b):
    s = 0
    for i in range(D+1):
        for j in range(D+1):
            if c[i][j]:
                s += c[i][j] * (a**i) * (b**j)
    return s

def per_var_degree(c, D):
    dega = 0; degb = 0
    for i in range(D+1):
        for j in range(D+1):
            if c[i][j]:
                dega = max(dega, i); degb = max(degb, j)
    return dega, degb

def search(D=3, C=3, e=0, grid=range(0,6)):
    # independent symmetric coeffs c_ij, i<=j
    idx = [(i,j) for i in range(D+1) for j in range(i,D+1)]
    # Apply unit constraints to prune which coeffs are free / forced
    # e=0: F(0,b)=sum_j c_0j b^j = b  => c00=0, c01=1, c0j=0 (j>=2)
    # e=1: F(1,b)=sum_j (sum_i c_ij) b^j = b => only column j=1 nonzero and sum_i c_i1 =1
    solutions = []
    # brute force over free coeffs
    ranges = []
    for (i,j) in idx:
        ranges.append(range(0, C+1))
    total = 1
    for r in ranges: total *= len(r)
    count = 0
    for vals in itertools.product(*ranges):
        c = [[0]*(D+1) for _ in range(D+1)]
        for (k,(i,j)) in enumerate(idx):
            c[i][j] = vals[k]; c[j][i] = vals[k]
        # unit check
        ok = all(evalF(c,D,e,b)==b for b in grid)
        if not ok: continue
        # associativity on grid
        assoc = True
        for a in grid:
            for b in grid:
                for cc in grid:
                    if evalF(c,D, evalF(c,D,a,b), cc) != evalF(c,D,a, evalF(c,D,b,cc)):
                        assoc=False; break
                if not assoc: break
            if not assoc: break
        if not assoc: continue
        dega, degb = per_var_degree(c,D)
        solutions.append((c, dega, degb))
    return solutions

def describe(c, D):
    terms=[]
    for i in range(D+1):
        for j in range(D+1):
            if c[i][j]:
                terms.append(f"{c[i][j]}*a^{i}*b^{j}")
    return " + ".join(terms) if terms else "0"

if __name__=="__main__":
    for e in (0,1):
        sols = search(D=3, C=3, e=e, grid=range(0,6))
        print(f"\n===== unit e={e}: {len(sols)} associative unital fixed-poly solutions (D=3,C=3) =====")
        maxdeg = 0
        deg2 = []
        # dedupe by formula
        seen=set()
        for c,da,db in sols:
            key = describe(c,3)
            if key in seen: continue
            seen.add(key)
            maxdeg=max(maxdeg, da, db)
            if max(da,db)>=2: deg2.append((key,da,db))
        # print families compactly
        for c,da,db in sols:
            pass
        print(f"  distinct formulas: {len(seen)}")
        # show sample of low-degree family
        shown=0
        for key in sorted(seen):
            print("   F =", key)
            shown+=1
            if shown>=12:
                print("   ... (%d more)"%(len(seen)-shown)); break
        print(f"  MAX per-variable degree among solutions: {maxdeg}")
        print(f"  degree>=2 solutions: {len(deg2)}")
        for k in deg2[:10]:
            print("     DEG>=2:", k)
