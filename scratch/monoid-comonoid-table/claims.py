from table import *

def diagonal(c):
    """Delta: c -> c x c (for Prod)."""
    cc = Prod.tensor_obj(c, c)
    F = {}; B = {}
    for s in c['S']:
        F[s] = (s, s)
        b = {}
        for p in c['P'][s]:
            b[('l', p)] = p
            b[('r', p)] = p
        B[s] = b
    return F and {'f': F, 'b': B}

def terminal_map(c):
    """eps: c -> 1 (Prod.unit)."""
    return {'f': {s: '*' for s in c['S']}, 'b': {s: {} for s in c['S']}}

print("="*70)
print("SANITY: known x-diagonal comonoid must pass")
for name in ['1sh,2pos', '2sh,[2,1]', 'y (1sh,1pos)']:
    c = samples[name]
    d = diagonal(c); e = terminal_map(c)
    assert is_morphism(d, c, Prod.tensor_obj(c, c)), (name, 'delta not morph')
    assert is_morphism(e, c, Prod.unit), (name, 'eps not morph')
    print(f"  {name}: is_comonoid(x, diag, term) = {is_comonoid(Prod, c, d, e)}  laws={comonoid_laws(Prod,c,d,e)}")

print()
print("="*70)
print("C1: x-comonoids -- every container has exactly ONE, the diagonal+terminal")
for name in ['y (1sh,1pos)', '1sh,2pos', '1sh,3pos', '2sh,[1,1]', '2sh,[2,1]', '2sh,[0,1]']:
    c = samples[name]
    res, nd, ne = count_comonoids(Prod, c)
    dg = diagonal(c); tm = terminal_map(c)
    is_diag = any(eq(d, dg) and eq(e, tm) for d, e in res)
    print(f"  {name}: #comonoids={len(res)} (of {nd} deltas x {ne} eps); diagonal present={is_diag}")

print()
print("="*70)
print("C2: +-monoids -- every container has exactly ONE, the codiagonal+initial")
for name in ['y (1sh,1pos)', '1sh,2pos', '2sh,[1,1]', '2sh,[2,1]', '1sh,0pos(=1)']:
    c = samples[name]
    res, nm, ne = count_monoids(Coprod, c)
    print(f"  {name}: #monoids={len(res)} (of {nm} mu x {ne} eta)")

print()
print("="*70)
print("C3: +-comonoids collapse -- morphisms c -> 0 exist only if c=0")
for name in ['y (1sh,1pos)', '1sh,2pos', '2sh,[1,1]', '1sh,0pos(=1)']:
    c = samples[name]
    ms = enum_morphisms(c, Coprod.unit)   # c -> 0
    res, nd, ne = count_comonoids(Coprod, c)
    print(f"  {name}: #morphisms(c->0)={len(ms)}; #+-comonoids={len(res)}")
# the empty container 0 itself:
zero = Coprod.unit
res0, _, _ = count_comonoids(Coprod, zero)
print(f"  0 (empty): #+-comonoids={len(res0)}")

print()
print("="*70)
print("C4: x-monoids -- genuine extra structure (count varies / not always 1)")
for name in ['y (1sh,1pos)', '1sh,0pos(=1)', '1sh,2pos', '2sh,[0,1]', '2sh,[1,1]', '2sh,[0,0]' if '2sh,[0,0]' in samples else '1sh,0pos(=1)']:
    c = samples[name]
    cc = Prod.tensor_obj(c, c)
    etas = enum_morphisms(Prod.unit, c)   # 1 -> c
    res, nm, ne = count_monoids(Prod, c)
    print(f"  {name}: #x-monoids={len(res)} (of {nm} mu x {ne} eta); #units(1->c)={len(etas)}")
# extra: container all-empty positions
for cards in ([0], [0, 0], [0, 0, 0]):
    c = cont(cards)
    res, nm, ne = count_monoids(Prod, c)
    print(f"  all-empty {cards}: #x-monoids={len(res)} (mu {nm} x eta {ne})")

print()
print("="*70)
print("C5: (x)-comonoids = families of monoids on position sets")
# monoid structures on a labelled set of size n
def count_set_monoids(n):
    elems = list(range(n))
    cnt = 0
    mats = list(itertools.product(elems, repeat=n*n))  # multiplication tables
    for flat in mats:
        m = {(i, j): flat[i*n+j] for i in elems for j in elems}
        # associativity
        if not all(m[(m[(i,j)],k)] == m[(i,m[(j,k)])] for i in elems for j in elems for k in elems):
            continue
        # has identity?
        ident = [e for e in elems if all(m[(e,x)]==x and m[(x,e)]==x for x in elems)]
        if ident:
            cnt += 1
    return cnt

for n in [1, 2, 3]:
    print(f"  monoid structures on labelled {n}-elt set = {count_set_monoids(n)}")
for name in ['y (1sh,1pos)', '1sh,2pos', '1sh,3pos']:
    c = samples[name]
    res, nd, ne = count_comonoids(Dir, c)
    npos = len(c['P'][c['S'][0]])
    print(f"  {name}: #(x)-comonoids={len(res)}; monoids on {npos}-set={count_set_monoids(npos)}")
# two-shape: should be product of per-shape monoid counts
for name in ['2sh,[2,1]', '2sh,[1,1]']:
    c = samples[name]
    res, nd, ne = count_comonoids(Dir, c)
    prod = 1
    for s in c['S']:
        prod *= count_set_monoids(len(c['P'][s]))
    print(f"  {name}: #(x)-comonoids={len(res)}; product of per-shape monoid counts={prod}")

print()
print("="*70)
print("C6: (x)-monoids -- the open cell")
def analyze_dir_monoids(name):
    c = samples[name] if name in samples else name
    res, nm, ne = count_monoids(Dir, c)
    print(f"  {name if isinstance(name,str) else 'custom'}: #(x)-monoids={len(res)} (of {nm} mu x {ne} eta)")
    # analyze shape-part m: is it always a monoid on S?
    S = c['S']
    always_shape_monoid = True
    shape_ops = set()
    for mu, eta in res:
        # mu shape map: S x S -> S
        m = {(s, t): mu['f'][(s, t)] for s in S for t in S}
        # eta shape: unit '*' -> some shape
        e = eta['f']['*']
        # check associative + unit e
        assoc = all(m[(m[(a,b)],cc)] == m[(a,m[(b,cc)])] for a in S for b in S for cc in S)
        unit = all(m[(e,x)]==x and m[(x,e)]==x for x in S)
        if not (assoc and unit):
            always_shape_monoid = False
        shape_ops.add(tuple(sorted(m.items())))
    print(f"     shape-part always a monoid on S? {always_shape_monoid}; #distinct shape-ops among monoids={len(shape_ops)}")
    return res

for name in ['2sh,[1,1]', '1sh,2pos', 'y (1sh,1pos)', '2sh,[2,1]']:
    analyze_dir_monoids(name)
