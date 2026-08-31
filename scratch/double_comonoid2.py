import itertools

def is_assoc(op, els):
    return all(op[(op[(a,b)],c)] == op[(a,op[(b,c)])] for a in els for b in els for c in els)
def is_comm(op, els):
    return all(op[(a,b)]==op[(b,a)] for a in els for b in els)

def cyclic(n):
    els=list(range(n)); mu={(a,b):(a+b)%n for a in els for b in els}; return els,mu,0
def klein():
    els=list(range(4)); mu={(a,b):a^b for a in els for b in els}; return els,mu,0
def meet():
    els=[0,1]; mu={(a,b):min(a,b) for a in els for b in els}; return els,mu,1
def S3():
    perms=list(itertools.permutations(range(3))); idx={p:i for i,p in enumerate(perms)}
    els=list(range(6)); comp=lambda p,q:tuple(p[q[i]] for i in range(3))
    mu={(i,j):idx[comp(perms[i],perms[j])] for i in els for j in els}; return els,mu,idx[(0,1,2)]
def T2():
    funcs=list(itertools.product([0,1],repeat=2)); idx={f:i for i,f in enumerate(funcs)}
    els=list(range(4)); comp=lambda f,g:tuple(f[g[x]] for x in range(2))
    mu={(i,j):idx[comp(funcs[i],funcs[j])] for i in els for j in els}; return els,mu,idx[(0,1)]

# Two versions of the interchange constraint:
# USER  C2u: m(a*b, a'*b') = m(a,b) * m(a',b')   [pairs (a,b),(a',b')]
# CORRECT EH C2c: m(a*c, b*d) = m(a,b) * m(c,d)   [regroup: 2x2 grid rows/cols]
def c2_user(m, mu, els):
    for a in els:
        for b in els:
            for ap in els:
                for bp in els:
                    if m[(mu[(a,b)],mu[(ap,bp)])] != mu[(m[(a,b)],m[(ap,bp)])]:
                        return False
    return True
def c2_correct(m, mu, els):
    for a in els:
        for b in els:
            for c in els:
                for d in els:
                    if m[(mu[(a,c)],mu[(b,d)])] != mu[(m[(a,b)],m[(c,d)])]:
                        return False
    return True

def solve(els, mu, e, c2fn, require_C3=True):
    pairs=[(a,b) for a in els for b in els]
    fixed={}
    for a in els:
        fixed[(a,e)]=a; fixed[(e,a)]=a
    free=[p for p in pairs if p not in fixed]
    sols=[]; m=dict(fixed)
    # partial C2 check: only enforce constraints whose all referenced cells are assigned
    def c2_partial_ok(m):
        # use whichever fn but guarded
        for a in els:
            for b in els:
                for c in els:
                    for d in els:
                        pass
        return True
    def full_ok(m):
        if not c2fn(m,mu,els): return False
        if require_C3 and not is_assoc(m,els): return False
        return True
    def bt(i):
        if i==len(free):
            if full_ok(m): sols.append(dict(m))
            return
        cell=free[i]
        for v in els:
            m[cell]=v
            bt(i+1)
        del m[cell]
    bt(0)
    return sols

lib=[('Z/2',*cyclic(2)),('Z/3',*cyclic(3)),('Z/4',*cyclic(4)),('V4',*klein()),
     ('Meet(min,1)',*meet()),('T2',*T2()),('S3',*S3())]

# S3 full enumeration = 6^25 too big; restrict: for n>=5 rely on m=mu test + smart.
# For correct law we still brute force where feasible. n=4 -> 4^9=262144 ok. n=6 -> 6^25 infeasible.
# So for S3 we test only: does m=mu satisfy? and do a targeted search? We'll brute n<=4, and for S3 test m=mu only.

print(f"{'monoid':14}{'comm':6}| USER-law: exists #sol all=mu | CORRECT-EH-law: exists #sol all=mu")
for name,els,mu,e in lib:
    comm=is_comm(mu,els); n=len(els)
    if n<=4:
        su=solve(els,mu,e,c2_user); sc=solve(els,mu,e,c2_correct)
        su_s=f"{len(su)>0!s:5} {len(su):<4} {all(s==mu for s in su) if su else None}"
        sc_s=f"{len(sc)>0!s:5} {len(sc):<4} {all(s==mu for s in sc) if sc else None}"
    else:
        # S3: test m=mu under each law only (full search infeasible)
        mmu=dict(mu)
        u_mu = c2_user(mmu,mu,els) and is_assoc(mmu,els)
        c_mu = c2_correct(mmu,mu,els) and is_assoc(mmu,els)
        su_s=f"[m=mu:{u_mu}] (full search skipped n=6)"
        sc_s=f"[m=mu:{c_mu}] (full search skipped n=6)"
    print(f"{name:14}{comm!s:6}| {su_s:28} | {sc_s}")

print("\nNote: for S3 (n=6) full 6^25 search infeasible; only m=mu tested.")
