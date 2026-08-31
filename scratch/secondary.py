"""
Secondary check.
Enumerate ALL associative binary operations f on {0,1,2,3} that have a two-sided
identity element e in {0,1}.  For each such op and each b, test whether
   g_b : n |-> f(n,b)   (n in {0,1,2,3})
is 'cardinality-polynomial', i.e. equals  n |-> sum_i n^{k_i}  for some multiset
of exponents k_i (equivalently g_b(n)=sum_j c_j n^j with c_j in N).
Report the ops for which SOME b fails (candidate non-closed tensors).
"""
import itertools
S = range(4)

def is_assoc(f):
    for a in S:
        for b in S:
            for c in S:
                if f[(f[(a,b)],c)] != f[(a,f[(b,c)])]:
                    return False
    return True

def card_poly(vals):
    # vals = (g(0),g(1),g(2),g(3)); is there c0..c3>=0 int with g(n)=sum c_j n^j ?
    # values<=3 => exponents>=2 impossible, but we search c0..c3 to be safe/explicit.
    for c0 in range(4):
        for c1 in range(4):
            for c2 in range(4):
                for c3 in range(4):
                    ok=True
                    for n in S:
                        if c0 + c1*n + c2*n*n + c3*n**3 != vals[n]:
                            ok=False; break
                    if ok:
                        return (c0,c1,c2,c3)
    return None

def enumerate_ops():
    ops=[]
    for e in (0,1):
        others=[x for x in S if x!=e]
        # free entries: f(a,b) for a,b in others  (9 entries)
        cells=[(a,b) for a in others for b in others]
        for assignment in itertools.product(S, repeat=len(cells)):
            f={}
            for x in S:
                f[(e,x)]=x; f[(x,e)]=x
            for (cell,val) in zip(cells, assignment):
                f[cell]=val
            if is_assoc(f):
                ops.append((e,f))
    return ops

ops=enumerate_ops()
print("total associative ops with identity in {0,1}:", len(ops))
# dedupe by table (an op could appear once per its identity; identity is unique so fine)
seen=set(); uniq=[]
for e,f in ops:
    key=tuple(f[(a,b)] for a in S for b in S)
    if key not in seen:
        seen.add(key); uniq.append((e,f,key))
print("unique operation tables:", len(uniq))

noncard=[]
for e,f,key in uniq:
    failing=[]
    for b in S:
        vals=tuple(f[(n,b)] for n in S)
        if card_poly(vals) is None:
            failing.append((b,vals))
    if failing:
        noncard.append((e,key,failing))

print("\n# ops that are NOT cardinality-polynomial (some column g_b not a power-sum):",
      len(noncard))
def show(key):
    # print 4x4 table
    rows=[]
    for a in S:
        rows.append(" ".join(str(key[a*4+b]) for b in S))
    return " | ".join(rows)

for e,key,failing in noncard:
    print(f"\n unit e={e}   table[rows a=0..3][cols b=0..3]: {show(key)}")
    for b,vals in failing:
        print(f"    b={b}: n->f(n,{b}) = {vals}   NOT of form sum n^k")

# sanity anchor: is 'max' among them?
maxkey=tuple(max(a,b) for a in S for b in S)
print("\n--- anchor: max operation ---")
print(" max table:", show(maxkey), " assoc/unital(e=0):", is_assoc({(a,b):max(a,b) for a in S for b in S}))
for b in S:
    vals=tuple(max(n,b) for n in S)
    print(f"   b={b}: max(n,{b}) over n=0..3 = {vals}  cardinality-poly? {card_poly(vals)}")
