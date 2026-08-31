import itertools, random

# A container: (S, dims) where S = list of shape labels, dims: dict shape-> int (|direction set|).
# We only need cardinalities to check hom-set sizes.

def hom_size(p, q):
    # |Cont(p,q)| = sum over f0: S_p->S_q of prod_{s} |p[s]|^{|q[f0 s]|}
    Sp, dp = p
    Sq, dq = q
    total = 0
    for f0 in itertools.product(Sq, repeat=len(Sp)):
        prod = 1
        for i,s in enumerate(Sp):
            prod *= dp[s] ** dq[f0[i]]
        total += prod
    return total

def rtimes(p, q):
    # (p rtimes q): shapes S_p x S_q ; dir at (s,t) = |p[s]|^{|S_q|} * |q[t]|
    Sp, dp = p; Sq, dq = q
    nq = len(Sq)
    S = [(s,t) for s in Sp for t in Sq]
    d = {(s,t): (dp[s]**nq) * dq[t] for s in Sp for t in Sq}
    return (S, d)

def internal_hom(q, r):
    # [q,r]: shapes = { (a, c) : a: S_q->S_r, c_t: r[a t]->q[t] }
    #   count as sum over a of prod_t |q[t]|^{|r[a t]|}, but we need the actual container (shapes+dims)
    # dir at (a,c) = |S_q| * sum_{t} |r[a t]|
    Sq, dq = q; Sr, dr = r
    nq = len(Sq)
    S = []
    d = {}
    for a in itertools.product(Sr, repeat=len(Sq)):
        # a maps position i (shape Sq[i]) to a[i] in Sr
        # number of choices of c = prod_t |q[t]|^{|r[a t]|}
        num_c = 1
        for i,t in enumerate(Sq):
            num_c *= dq[t] ** dr[a[i]]
        dir_card = nq * sum(dr[a[i]] for i in range(len(Sq)))
        for c_idx in range(num_c):
            lbl = (a, c_idx)
            S.append(lbl)
            d[lbl] = dir_card
    return (S, d)

def rand_container(maxshapes=3, maxdir=3):
    n = random.randint(1, maxshapes)
    S = list(range(n))
    d = {s: random.randint(1, maxdir) for s in S}
    return (S, d)

random.seed(0)
ok = True
for trial in range(2000):
    p = rand_container(2,3)
    q = rand_container(2,3)
    r = rand_container(2,3)
    lhs = hom_size(rtimes(p,q), r)          # Cont(p rtimes q, r)
    rhs = hom_size(p, internal_hom(q,r))    # Cont(p, [q,r])
    if lhs != rhs:
        ok = False
        print("MISMATCH", p, q, r, lhs, rhs)
        if trial > 20: break
print("all matched" if ok else "FOUND MISMATCH")

# Consistency: [y, r] should equal r  (since (-) rtimes y = Id, its right adjoint is Id)
def container_eq_upto_profile(a,b):
    Sa,da=a; Sb,db=b
    return sorted(da[s] for s in Sa)==sorted(db[s] for s in Sb) and len(Sa)==len(Sb)
y=([0],{0:1})
import random
random.seed(1)
allok=True
for _ in range(500):
    r=rand_container(3,4)
    if not container_eq_upto_profile(internal_hom(y,r), r):
        allok=False; print("[y,r]!=r", r)
print("[y,r] == r for all trials?", allok)
