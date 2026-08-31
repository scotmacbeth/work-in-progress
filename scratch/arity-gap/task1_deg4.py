"""
Task 1 (part A, extended): unit e=0, degree up to 4, pruned by unit constraints.
Unit e=0 forces: c00=0, c01=c10=1, c0j=0 (j>=2). Free coeffs c_ij for 1<=i<=j<=D.
Search associativity; report any per-variable degree >= 2.
"""
import itertools

def evalF(c, D, a, b):
    s=0
    for i in range(D+1):
        row=c[i]
        for j in range(D+1):
            v=row[j]
            if v: s+=v*(a**i)*(b**j)
    return s

def run(D=4, C=2, grid=range(0,6)):
    free=[(i,j) for i in range(1,D+1) for j in range(i,D+1)]
    sols=[]
    for vals in itertools.product(range(C+1), repeat=len(free)):
        c=[[0]*(D+1) for _ in range(D+1)]
        c[0][1]=1; c[1][0]=1
        for (k,(i,j)) in enumerate(free):
            c[i][j]=vals[k]; c[j][i]=vals[k]
        # unit already satisfied by construction (F(0,b)=b). verify quickly on 2 pts
        if evalF(c,D,0,2)!=2 or evalF(c,D,0,3)!=3: continue
        ok=True
        for a in grid:
            for b in grid:
                fab=evalF(c,D,a,b)
                for cc in grid:
                    if evalF(c,D,fab,cc)!=evalF(c,D,a,evalF(c,D,b,cc)):
                        ok=False;break
                if not ok:break
            if not ok:break
        if ok:
            dega=max((i for i in range(D+1) for j in range(D+1) if c[i][j]),default=0)
            degb=max((j for i in range(D+1) for j in range(D+1) if c[i][j]),default=0)
            sols.append((c,dega,degb))
    return sols

def desc(c,D):
    t=[f"{c[i][j]}a^{i}b^{j}" for i in range(D+1) for j in range(D+1) if c[i][j]]
    return "+".join(t)

if __name__=="__main__":
    sols=run(D=4,C=2,grid=range(0,6))
    seen=sorted({desc(c,4) for c,_,_ in sols})
    md=max((max(da,db) for _,da,db in sols),default=0)
    print(f"D=4 C=2 e=0: {len(sols)} solutions, {len(seen)} distinct, MAX per-var degree={md}")
    for k in seen: print("  ",k)
