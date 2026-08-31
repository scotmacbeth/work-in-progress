import itertools, math

# Represent a container as (shape_list, pos_func) where pos_func(s) returns a frozenset (position set)
# Monomial: pos_func constant.

def is_monomial(shapes, posf):
    if not shapes: return True  # zero monomial (vacuously constant)
    sizes = {len(posf(s)) for s in shapes}
    return len(sizes) == 1

def prod(c1, c2):
    S,P = c1; T,Q = c2
    shapes = list(itertools.product(S,T))
    def posf(st):
        s,t = st
        # coproduct (disjoint union) of P(s) and Q(t)
        return [('L',a) for a in P(s)] + [('R',b) for b in Q(t)]
    return shapes, posf

def coprod(c1, c2):
    S,P = c1; T,Q = c2
    shapes = [('L',s) for s in S] + [('R',t) for t in T]
    def posf(x):
        tag,v = x
        return list(P(v)) if tag=='L' else list(Q(v))
    return shapes, posf

# Build monomial S*y^A
def mono(S, A):
    return (list(S), (lambda s, A=A: list(A)))

# extension count |[C](X)| = sum_s |X|^|pos(s)|
def ext_count(c, xsize):
    shapes,posf = c
    return sum(xsize**len(posf(s)) for s in shapes)

# --- product test ---
print("=== PRODUCT of monomials ===")
passes=0; tot=0
for sS in range(1,4):
 for sA in range(0,3):
  for sT in range(1,4):
   for sB in range(0,3):
    c1=mono(range(sS),range(sA)); c2=mono(range(sT),range(sB))
    p=prod(c1,c2)
    tot+=1
    mono_flag = is_monomial(*p)
    # expected monomial (S*T)*y^(A+B)
    expected = mono(range(sS*sT), range(sA+sB))
    # check extension counts match expected for several X
    okcount = all(ext_count(p,x)==ext_count(expected,x) for x in range(0,5))
    if mono_flag and okcount: passes+=1
    else: print("FAIL",sS,sA,sT,sB,mono_flag,okcount)
print(f"product: {passes}/{tot} are monomial & match (S*T)y^(A+B)")

# --- coproduct test ---
print("=== COPRODUCT of monomials ===")
mono_count=0; nonmono_count=0; tot=0
for sS in range(1,4):
 for sA in range(0,3):
  for sT in range(1,4):
   for sB in range(0,3):
    c1=mono(range(sS),range(sA)); c2=mono(range(sT),range(sB))
    p=coprod(c1,c2); tot+=1
    if is_monomial(*p): mono_count+=1
    else: nonmono_count+=1
# theory: monomial iff A==B (or one shape empty, but shapes>=1 here)
print(f"coproduct: {mono_count} monomial, {nonmono_count} non-monomial of {tot}")
# check: is it monomial exactly when sA==sB?
predok=True
for sS in range(1,4):
 for sA in range(0,3):
  for sT in range(1,4):
   for sB in range(0,3):
    c1=mono(range(sS),range(sA)); c2=mono(range(sT),range(sB))
    p=coprod(c1,c2)
    pred=(sA==sB)
    if is_monomial(*p)!=pred: predok=False; print("predict-mismatch",sS,sA,sT,sB)
print("coproduct monomial <=> |A|=|B| :", predok)

# --- terminal & initial ---
print("=== TERMINAL / INITIAL ===")
term = mono([0],[])   # 1 shape, empty positions = 1*y^0
init = ([],(lambda s:[]))  # empty shapes
print("terminal 1=(1,emptyset) monomial:", is_monomial(*term))
print("initial 0=(emptyset,!) monomial:", is_monomial(*init))

# --- W-type / free monad of a monomial ---
# Free monad on p=S*y^A: shapes = finite S-labelled A-branching trees, positions = LEAVES.
# Enumerate trees up to depth d, record number of leaves. If leaf-count varies -> not monomial.
def free_monad_leafcounts(S, A, maxdepth):
    # tree = ('leaf',) or ('node', s, tuple of A subtrees)
    # generate all trees of depth <= maxdepth
    def gen(depth):
        trees=[('leaf',)]
        if depth==0: return trees
        subs=gen(depth-1)
        for s in S:
            for children in itertools.product(subs, repeat=len(A)):
                trees.append(('node',s,children))
        return trees
    def leaves(t):
        if t[0]=='leaf': return 1
        return sum(leaves(c) for c in t[2])
    ts=gen(maxdepth)
    return sorted({leaves(t) for t in ts})
print("=== W-TYPE / FREE MONAD ===")
lc=free_monad_leafcounts(range(1),range(2),3)  # |S|=1,|A|=2 binary
print("free monad on 1*y^2: distinct leaf-counts among trees depth<=3:", lc)
print("positions constant? ->", len(lc)==1, "(monomial iff True)")
