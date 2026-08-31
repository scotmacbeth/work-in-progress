import itertools

def check_assoc(op, els):
    return all(op[(op[(a,b)],c)] == op[(a,(0 if False else b))] if False else op[(op[(a,b)],c)] == op[(a,op[(b,c)])] for a in els for b in els for c in els)

def is_assoc(op, els):
    for a in els:
        for b in els:
            for c in els:
                if op[(op[(a,b)],c)] != op[(a,op[(b,c)])]:
                    return False
    return True

def is_comm(op, els):
    return all(op[(a,b)]==op[(b,a)] for a in els for b in els)

# --- Monoid library ---
def cyclic(n):
    els = list(range(n))
    mu = {(a,b):(a+b)%n for a in els for b in els}
    return els, mu, 0  # unit 0

def klein():
    els = list(range(4))  # encode as (bit0,bit1)
    def enc(x): return x
    mu = {}
    for a in els:
        for b in els:
            mu[(a,b)] = a ^ b
    return els, mu, 0

def meet_semilattice():
    # ({0,1}, min, unit 1)
    els = [0,1]
    mu = {(a,b):min(a,b) for a in els for b in els}
    return els, mu, 1

def S3():
    # permutations of {0,1,2}
    perms = list(itertools.permutations(range(3)))
    els = list(range(len(perms)))
    def comp(p,q):
        # (p*q)(i) = p(q(i))
        return tuple(p[q[i]] for i in range(3))
    idx = {p:i for i,p in enumerate(perms)}
    mu = {}
    for i,p in enumerate(perms):
        for j,q in enumerate(perms):
            mu[(i,j)] = idx[comp(p,q)]
    unit = idx[(0,1,2)]
    return els, mu, unit

def T2():
    # all functions {0,1}->{0,1}, composition. 4 functions.
    funcs = list(itertools.product([0,1], repeat=2))  # (f(0),f(1))
    els = list(range(len(funcs)))
    idx = {f:i for i,f in enumerate(funcs)}
    def comp(f,g):
        # (f∘g)(x)=f(g(x))
        return tuple(f[g[x]] for x in range(2))
    mu = {}
    for i,f in enumerate(funcs):
        for j,g in enumerate(funcs):
            mu[(i,j)] = idx[comp(f,g)]
    unit = idx[(0,1)]  # identity
    return els, mu, unit

def M3_noncomm_test():
    # try to find a noncommutative monoid of order 3 - known: none exist with identity
    # We'll just report; skip building.
    return None

# --- Solver ---
# Constraints on m: A×A->A
# C1: m(e,e)=e
# C2: m(a*b,a'*b') = m(a,b)*m(a',b')  for all a,b,a',b'
# C3: m associative
# C4: m(a,e)=a, m(e,a)=a
# We search over m consistent with C4, propagate C2, then check C3.

def solve(els, mu, e, require_C3=True):
    n = len(els)
    pairs = [(a,b) for a in els for b in els]
    # Fixed values from C4:
    fixed = {}
    for a in els:
        fixed[(a,e)] = a
        fixed[(e,a)] = a
    # C1 is implied by C4 (m(e,e)=e). Good.
    # Free cells: pairs not in fixed
    free = [p for p in pairs if p not in fixed]
    # We'll do backtracking assigning free cells, but use C2 to prune.
    # C2 relates m at (a*b, a'*b') to product of m(a,b), m(a',b').
    # Represent m as dict; check consistency incrementally is complex; instead
    # for small n just enumerate assignments to free cells with C2 pruning via full check.
    solutions = []
    # Order free cells
    m = dict(fixed)
    def c2_ok_full(m):
        for a in els:
            for b in els:
                for ap in els:
                    for bp in els:
                        lhs_key = (mu[(a,b)], mu[(ap,bp)])
                        if lhs_key in m and (a,b) in m and (ap,bp) in m:
                            if m[lhs_key] != mu[(m[(a,b)], m[(ap,bp)])]:
                                return False
        return True
    def backtrack(i):
        if i == len(free):
            # full m assigned; verify C2 fully and optionally C3
            if not c2_ok_full(m):
                return
            if require_C3 and not is_assoc(m, els):
                return
            solutions.append(dict(m))
            return
        cell = free[i]
        for v in els:
            m[cell] = v
            # partial prune: check c2 constraints fully determinable
            if c2_ok_full(m):
                backtrack(i+1)
        del m[cell]
    backtrack(0)
    return solutions

def analyze(name, els, mu, e):
    comm = is_comm(mu, els)
    assert is_assoc(mu, els), f"{name} base op not associative!"
    assert all(mu[(a,e)]==a and mu[(e,a)]==a for a in els), f"{name} unit wrong!"
    sols = solve(els, mu, e, require_C3=True)
    exists = len(sols)>0
    all_eq_mu = all(s==mu for s in sols) if exists else None
    # Also solve dropping C3 for Task 2
    sols_noC3 = solve(els, mu, e, require_C3=False)
    return {
        'name':name,'comm':comm,'n':len(els),
        'exists':exists,'nsol':len(sols),'all_eq_mu':all_eq_mu,
        'sols':sols,
        'nsol_noC3':len(sols_noC3),
        'noC3_all_eq_mu': (all(s==mu for s in sols_noC3) if sols_noC3 else None),
    }

lib = []
lib.append(('Z/2', *cyclic(2)))
lib.append(('Z/3', *cyclic(3)))
lib.append(('Z/4', *cyclic(4)))
lib.append(('V4', *klein()))
lib.append(('Meet({0,1},min,1)', *meet_semilattice()))
lib.append(('T2', *T2()))
lib.append(('S3', *S3()))

results = []
for name, els, mu, e in lib:
    print(f"Solving {name} (n={len(els)})...", flush=True)
    r = analyze(name, els, mu, e)
    results.append(r)
    print(f"  comm={r['comm']} exists={r['exists']} nsol={r['nsol']} all_eq_mu={r['all_eq_mu']} | noC3 nsol={r['nsol_noC3']} noC3_all_eq_mu={r['noC3_all_eq_mu']}", flush=True)

print("\n=== TABLE ===")
print(f"{'monoid':22} {'comm?':6} {'m exists?':10} {'#valid m':9} {'all=mu?':8}")
for r in results:
    print(f"{r['name']:22} {str(r['comm']):6} {str(r['exists']):10} {r['nsol']:<9} {str(r['all_eq_mu']):8}")

print("\n=== Task2: drop C3, does C1+C2+C4 already force m=mu? ===")
for r in results:
    print(f"{r['name']:22} noC3 #sol={r['nsol_noC3']:<4} all=mu?={r['noC3_all_eq_mu']}")

# Prediction check
print("\n=== PREDICTION: exists IFF comm, and unique m=mu ===")
ok = True
for r in results:
    pred_exist = r['comm']
    if r['exists'] != pred_exist:
        ok=False; print(f"  VIOLATION exist: {r['name']} comm={r['comm']} exists={r['exists']}")
    if r['exists'] and not (r['nsol']==1 and r['all_eq_mu']):
        ok=False; print(f"  VIOLATION uniqueness: {r['name']} nsol={r['nsol']} all_eq_mu={r['all_eq_mu']}")
print("PREDICTION HELD" if ok else "PREDICTION VIOLATED somewhere")
