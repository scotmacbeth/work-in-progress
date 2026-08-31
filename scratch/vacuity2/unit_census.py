"""
Unit-cardinality census: for skeleton {0..N}, over all size tables and units,
find which unit cardinalities admit a GENUINE monoidal structure (valid bifunctor
with a natural associator satisfying pentagon+triangle).  Also flag non-poly ones.
"""
import sys, time
from driver import size_tables, assoc_exists
from search import bifunctors, poly_test

def census(N, budget=1e9):
    t0=time.time()
    realized_units=set()
    nonpoly_units=set()
    per_unit={}
    examples=[]
    for (u,s) in size_tables(N):
        if time.time()-t0>budget:
            print("  [budget hit; partial]"); break
        found_here=False
        for Lact,Ract in bifunctors(s,u,N):
            if assoc_exists(s,Lact,Ract,u,N):
                realized_units.add(u)
                per_unit[u]=per_unit.get(u,0)+1
                found_here=True
                pt=poly_test(s,Lact,Ract,N)
                if pt and not all(v[0] for v in pt.values()):
                    nonpoly_units.add(u)
                    examples.append((u,[[s[a][b] for b in range(N+1)] for a in range(N+1)]))
    return dict(realized=sorted(realized_units), per_unit=per_unit,
                nonpoly_units=sorted(nonpoly_units), examples=examples,
                elapsed=time.time()-t0)

if __name__=="__main__":
    for N in [1,2]:
        r=census(N)
        print(f"N={N}: realized unit cardinalities={r['realized']}  "
              f"counts-by-unit={r['per_unit']}  elapsed={r['elapsed']:.1f}s")
        print(f"   unit cardinalities admitting a NON-POLYNOMIAL R_B: {r['nonpoly_units']}")
        seen=set()
        for u,grid in r['examples']:
            k=(u,tuple(map(tuple,grid)))
            if k in seen: continue
            seen.add(k)
            print(f"      unit={u} sizes={grid}")
