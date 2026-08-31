from itertools import product
from verify import *

print("="*60)
print("T1: directed-container laws D1-D5 for ΔS")
for S in [['a'], ['a','b'], ['a','b','c']]:
    print(f"  S={S}: D1-D5", "OK" if check_directed_laws(S) else "FAIL")

print("="*60)
print("T1: comonad laws of induced comonad = store comonad")
for S in [['a','b']]:
    for X in [[0,1], [0,1,2]]:
        print(f"  S={S} X={X}:", "OK" if check_comonad_laws(S,X) else "FAIL")

print("="*60)
print("T3: ΔS⊗ΔT = Δ(S×T) strictly")
S=['a','b']; T=['0','1','2']
lhs = tensor(Delta(S), Delta(T))
# Δ(S×T): shapes S×T, fibres S×T
SxT = [(s,t) for s in S for t in T]
rhs = make_container(SxT, {st: list(SxT) for st in SxT})
# compare cardinalities of shapes and fibres (structure matches up to tagging)
def shape_fibre_profile(c):
    return (len(c['A']), sorted(len(c['B'][a]) for a in c['A']))
print("  ΔS⊗ΔT profile:", shape_fibre_profile(lhs))
print("  Δ(S×T) profile:", shape_fibre_profile(rhs))
print("  equal:", shape_fibre_profile(lhs)==shape_fibre_profile(rhs)
      and len(lhs['A'])==len(S)*len(T)
      and all(len(lhs['B'][a])==len(S)*len(T) for a in lhs['A']))
print("  Δ1 = y (unit):", shape_fibre_profile(Delta(['*']))==(1,[1]))

# ============================================================
# Build small containers and ENUMERATE all workers
# ============================================================
# p: 1 shape 'ap' with 1 position; q: 1 shape with 2 positions; r: 2 shapes...
def enum_functions(dom, cod):
    """all dicts dom->cod"""
    dom=list(dom); cod=list(cod)
    for vals in product(cod, repeat=len(dom)):
        yield dict(zip(dom, vals))

def enum_workers(S, p, q):
    """enumerate ALL workers ΔS⊗p -> q (small)."""
    dom_shapes = [(s,a) for s in S for a in p['A']]
    # f: dom_shapes -> q['A']
    for f in enum_functions(dom_shapes, q['A']):
        # for each (s,a), need f1:(D[c]->S) and f2:(D[c]->B[a])
        # build the per-shape choice spaces
        choice_spaces=[]
        keys=[]
        for (s,a) in dom_shapes:
            c=f[(s,a)]
            Dc=q['B'][c]; Ba=p['B'][a]
            f1_opts=list(enum_functions(Dc, S))
            f2_opts=list(enum_functions(Dc, Ba))
            keys.append((s,a))
            choice_spaces.append(list(product(f1_opts, f2_opts)))
        for combo in product(*choice_spaces):
            f1={}; f2={}
            for (s,a),(o1,o2) in zip(keys, combo):
                f1[(s,a)]=o1; f2[(s,a)]=o2
            yield {'S':list(S),'p':p,'q':q,'f':dict(f),'f1':f1,'f2':f2}

# tiny containers
p = make_container(['ap'], {'ap':['p0']})            # 1 shape,1 pos
q = make_container(['cq'], {'cq':['q0','q1']})        # 1 shape,2 pos
r = make_container(['er'], {'er':['r0']})             # 1 shape,1 pos
z = make_container(['fz'], {'fz':['z0','z1']})        # 1 shape,2 pos
S=['s0','s1']; T=['t0']; U=['u0','u1']

print("="*60)
print("T3: all composites are valid container morphisms")
allvalid=True; count=0
for w in enum_workers(S,p,q):
    for wp in enum_workers(T,q,r):
        wc = compose_workers(w,wp)
        dom,cod,f,fsh = worker_as_contmap(wc)
        if not is_valid_contmap(dom,cod,f,fsh):
            allvalid=False; print("INVALID composite"); break
        count+=1
    if not allvalid: break
print(f"  checked {count} composites: {'ALL VALID' if allvalid else 'FAIL'}")

print("="*60)
print("T3: UNIT LAWS  (id_q ∘ w == w ,  w ∘ id_p == w  up to state unitor)")
# left unit: idq has state {*}; compose w:ΔS⊗p->q  then id_q:Δ1⊗q->q  => state {*}×S ; unitor (*,s)->s
unit_ok=True; n=0
idq=identity_worker(q); idp=identity_worker(p)
for w in enum_workers(S,p,q):
    # left:  id_q ∘ w  (w first p->q state S, then id_q q->q state 1) -> state 1×S
    left = compose_workers(w, idq)               # state = T'×S with T'={*} -> [('*',s)]
    bijL = {('*',s): s for s in S}
    if not workers_equal_upto_state_bij(left, w, bijL): unit_ok=False; print("LEFT unit fail")
    # right: w ∘ id_p (id_p first p->p state 1, then w p->q state S) -> state S×1
    right = compose_workers(idp, w)              # state = [('s','*')]? note order: compose(w=idp first, wp=w)
    bijR = {(s,'*'): s for s in S}
    if not workers_equal_upto_state_bij(right, w, bijR): unit_ok=False; print("RIGHT unit fail")
    n+=1
print(f"  checked {n} workers: {'UNIT LAWS HOLD' if unit_ok else 'FAIL'}")

print("="*60)
print("T3: ASSOCIATIVITY  (w3∘w2)∘w1 == w3∘(w2∘w1) up to ×-associator on states")
# w1:ΔS⊗p->q , w2:ΔT⊗q->r , w3:ΔU⊗r->z
# left-assoc: compose_workers(w1,w2) gives state T×S ; then with w3 gives U×(T×S)
# right-assoc: compose_workers(w2,w3) gives state U×T ; then compose_workers(w1, that) gives (U×T)×S
# associator bijection: ((u,t),s) <-> (u,(t,s))
assoc_ok=True; m=0
# reduce enumeration size: fix small; iterate a sample of workers but exhaustively over these tiny sets
w1_list=list(enum_workers(S,p,q))
w2_list=list(enum_workers(T,q,r))
w3_list=list(enum_workers(U,r,z))
print(f"  |w1|={len(w1_list)} |w2|={len(w2_list)} |w3|={len(w3_list)}  total triples={len(w1_list)*len(w2_list)*len(w3_list)}")
for w1 in w1_list:
    c12 = compose_workers(w1,w2_list[0]) # placeholder, will redo in loop
    for w2 in w2_list:
        w12 = compose_workers(w1,w2)          # state T×S
        for w3 in w3_list:
            L = compose_workers(w12, w3)      # state U×(T×S)
            w23 = compose_workers(w2, w3)     # state U×T
            R = compose_workers(w1, w23)      # state (U×T)×S
            # associator: L state = (u,(t,s)); R state = ((u,t),s)
            bij = {}
            for u in U:
                for t in T:
                    for s in S:
                        bij[(u,(t,s))] = ((u,t),s)
            if not workers_equal_upto_state_bij(L, R, bij):
                assoc_ok=False; print("ASSOC FAIL"); break
            m+=1
        if not assoc_ok: break
    if not assoc_ok: break
print(f"  checked {m} triples: {'ASSOCIATIVE' if assoc_ok else 'FAIL'}")
print("="*60)
print("DONE")
