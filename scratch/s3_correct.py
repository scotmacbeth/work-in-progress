import itertools
perms=list(itertools.permutations(range(3))); idx={p:i for i,p in enumerate(perms)}
els=list(range(6)); comp=lambda p,q:tuple(p[q[i]] for i in range(3))
mu={(i,j):idx[comp(perms[i],perms[j])] for i in els for j in els}; e=idx[(0,1,2)]

# Correct EH interchange: m(a*c,b*d)=m(a,b)*m(c,d)
# Incremental backtracking with full-constraint pruning after each assignment.
fixed={}
for a in els:
    fixed[(a,e)]=a; fixed[(e,a)]=a
free=[(a,b) for a in els for b in els if (a,b) not in fixed]

def partial_c2_ok(m):
    for a in els:
        for b in els:
            for c in els:
                for d in els:
                    L=(mu[(a,c)],mu[(b,d)])
                    if L in m and (a,b) in m and (c,d) in m:
                        if m[L]!=mu[(m[(a,b)],m[(c,d)])]:
                            return False
    return True

sols=[]; m=dict(fixed)
import sys
sys.setrecursionlimit(10000)
def bt(i):
    if i==len(free):
        sols.append(dict(m)); return
    cell=free[i]
    for v in els:
        m[cell]=v
        if partial_c2_ok(m):
            bt(i+1)
    del m[cell]
bt(0)
print("S3 correct-EH-law: #solutions =", len(sols))
# sanity: also confirm this search finds m=mu for a commutative one (Z/3) 
