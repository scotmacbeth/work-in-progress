import itertools
from engine import all_morphisms, ident, comp, generators
from search import enumerate_actions, bifunctors, poly_test, fcompose
from driver import size_tables, assoc_exists

N=2
# the flagged table: sizes[[0,1,2],[1,1,1],[2,1,1]], unit 0
target=[[0,1,2],[1,1,1],[2,1,1]]
for (u,s) in size_tables(N):
    grid=[[s[a][b] for b in range(N+1)] for a in range(N+1)]
    if grid==target and u==0:
        print("size table:",grid,"unit",u)
        for Lact,Ract in bifunctors(s,u,N):
            pt=poly_test(s,Lact,Ract,N)
            if not all(v[0] for v in pt.values()):
                print("  --- non-poly bifunctor ---")
                print("  Lact (left action, per fixed right-object b):")
                for b in range(N+1):
                    print(f"    b={b}:")
                    for m in generators(N):
                        if m in Lact[b]:
                            print(f"       {m} -> {Lact[b][m]}")
                print("  Ract (right action, per fixed left-object a):")
                for a in range(N+1):
                    print(f"    a={a}:")
                    for m in generators(N):
                        if m in Ract[a]:
                            print(f"       {m} -> {Ract[a][m]}")
                ae=assoc_exists(s,Lact,Ract,u,N)
                print("  assoc_exists:",ae)
                print("  poly_test:",{b:(v[0],v[1]) for b,v in pt.items()})
                break
        break
