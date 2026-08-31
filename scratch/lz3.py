import itertools
# {e=0, a=1, b=2}, e identity; {a,b} left-zero: x*y=x
els=[0,1,2]; e=0
def mul(x,y):
    if x==e: return y
    if y==e: return x
    return x  # left zero on {a,b}
mu={(x,y):mul(x,y) for x in els for y in els}
def is_assoc(op): return all(op[(op[(a,b)],c)]==op[(a,op[(b,c)])] for a in els for b in els for c in els)
def is_comm(op): return all(op[(a,b)]==op[(b,a)] for a in els for b in els)
print("order-3 left-zero+identity: associative?",is_assoc(mu),"commutative?",is_comm(mu))

def c2_user(m):
    return all(m[(mu[(a,b)],mu[(ap,bp)])]==mu[(m[(a,b)],m[(ap,bp)])] for a in els for b in els for ap in els for bp in els)
def c2_correct(m):
    return all(m[(mu[(a,c)],mu[(b,d)])]==mu[(m[(a,b)],m[(c,d)])] for a in els for b in els for c in els for d in els)

def solve(c2fn):
    fixed={}
    for a in els: fixed[(a,e)]=a; fixed[(e,a)]=a
    free=[(a,b) for a in els for b in els if (a,b) not in fixed]
    sols=[]; m=dict(fixed)
    def bt(i):
        if i==len(free):
            if c2fn(m) and is_assoc(m): sols.append(dict(m))
            return
        for v in els:
            m[free[i]]=v; bt(i+1)
        del m[free[i]]
    bt(0); return sols
su=solve(c2_user); sc=solve(c2_correct)
print("USER law: #sol",len(su),"all=mu?",all(s==mu for s in su) if su else None)
print("CORRECT EH law: #sol",len(sc))
