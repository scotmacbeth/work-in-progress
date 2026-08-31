"""
Finite container library for the Workers type-hierarchy investigation.

A container p = (A, B): shape set A (list of hashable labels), position family
B: dict a -> list of position labels.  Extension |p| X = Sum_{a in A} X^{B a}.

A morphism p->q = (fwd, bwd): fwd: A -> C (dict), bwd: for each a, a dict
D(fwd a) -> B a  (backward on positions).  Composition: forward on shapes,
backward on positions.

We represent objects concretely with small finite sets so we can test whether a
*candidate formula* for a natural transformation is a valid container morphism,
whether it is iso, and whether coherence squares commute on concrete instances.
"""

from itertools import product

class Cont:
    def __init__(self, shapes, fib):
        # shapes: list ; fib: dict shape -> list of positions
        self.shapes = list(shapes)
        self.fib = {a: list(fib[a]) for a in self.shapes}
    def __repr__(self):
        return f"Cont(shapes={self.shapes}, fib={self.fib})"
    def num_positions(self):
        return {a: len(self.fib[a]) for a in self.shapes}

# ---- constructors ----
def deltaS(S):
    # S: list.  ΔS = (S, s -> S)  every fibre = S
    return Cont(list(S), {s: list(S) for s in S})

def y():
    return Cont(['*'], {'*': ['0']})   # unit for ⊗ ; note fibre singleton

# ---- Dirichlet tensor ⊗ : (A×C, (a,c)->Ba×Dc) ----
def tensor(p, q):
    shapes = [(a,c) for a in p.shapes for c in q.shapes]
    fib = {(a,c): [(b,d) for b in p.fib[a] for d in q.fib[c]] for (a,c) in shapes}
    return Cont(shapes, fib)

# ---- product × : (A×C, (a,c)->Ba + Dc) ----
def prod(p, q):
    shapes = [(a,c) for a in p.shapes for c in q.shapes]
    fib = {(a,c): [('l',b) for b in p.fib[a]] + [('r',d) for d in q.fib[c]]
           for (a,c) in shapes}
    return Cont(shapes, fib)

# ---- coproduct + : (A + C, inherited fibres) ----
def coprod(p, q):
    shapes = [('l',a) for a in p.shapes] + [('r',c) for c in q.shapes]
    fib = {}
    for a in p.shapes: fib[('l',a)] = list(p.fib[a])
    for c in q.shapes: fib[('r',c)] = list(q.fib[c])
    return Cont(shapes, fib)

# ---- substitution ◁ : ⟦p◁q⟧ = ⟦p⟧∘⟦q⟧ ----
# shape: (a, gamma) with gamma: Ba -> C  (a choice function)
# position at (a,gamma): (b, d) with b in Ba, d in D(gamma b)
def lhd(p, q):
    shapes = []
    fib = {}
    for a in p.shapes:
        Ba = p.fib[a]
        # all functions gamma: Ba -> q.shapes
        for vals in product(q.shapes, repeat=len(Ba)):
            gamma = tuple(vals)  # gamma[i] = C-shape for i-th position of Ba
            sh = (a, gamma)
            shapes.append(sh)
            positions = []
            for i,b in enumerate(Ba):
                c = gamma[i]
                for d in q.fib[c]:
                    positions.append((b,d))
            fib[sh] = positions
    return Cont(shapes, fib)

# ---- morphism validation ----
class Mor:
    def __init__(self, src, tgt, fwd, bwd):
        self.src=src; self.tgt=tgt; self.fwd=fwd; self.bwd=bwd
    def validate(self):
        # fwd: src.shapes -> tgt.shapes ; bwd[a]: dict pos of tgt.fib[fwd a] -> src.fib[a]
        for a in self.src.shapes:
            if a not in self.fwd: return (False, f"fwd undefined at {a}")
            c = self.fwd[a]
            if c not in self.tgt.shapes: return (False, f"fwd({a})={c} not a target shape")
            need = set(self.tgt.fib[c])
            have = self.bwd[a]
            for d in need:
                if d not in have: return (False, f"bwd[{a}] undefined at target-pos {d}")
                if have[d] not in self.src.fib[a]:
                    return (False, f"bwd[{a}][{d}]={have[d]} not a src position of {a}")
        return (True, "ok")
    def is_iso(self):
        ok,msg = self.validate()
        if not ok: return False
        # bijective on shapes and each bwd bijective
        if sorted(map(str,self.fwd.values())) != sorted(map(str,self.tgt.shapes)):
            return False
        if len(set(map(str,self.fwd.values()))) != len(self.src.shapes): return False
        for a in self.src.shapes:
            c=self.fwd[a]
            vals=[self.bwd[a][d] for d in self.tgt.fib[c]]
            if sorted(map(str,vals)) != sorted(map(str,self.src.fib[a])): return False
        return True

def compose(m1, m2):
    # m1: p->q, m2: q->r  ==> p->r
    p,q = m1.src, m1.tgt
    q2,r = m2.src, m2.tgt
    fwd = {a: m2.fwd[m1.fwd[a]] for a in p.shapes}
    bwd = {}
    for a in p.shapes:
        c = m1.fwd[a]; e = m2.fwd[c]
        bwd[a] = {}
        for d in r.fib[e]:
            # m2.bwd[c][d] in q.fib[c]; then m1.bwd[a][that] in p.fib[a]
            qpos = m2.bwd[c][d]
            bwd[a][d] = m1.bwd[a][qpos]
    return Mor(p, r, fwd, bwd)

def eq_mor(m1, m2):
    if m1.fwd != m2.fwd:
        # compare as strings for structural equality
        if {k:str(v) for k,v in m1.fwd.items()} != {k:str(v) for k,v in m2.fwd.items()}:
            return False
    for a in m1.src.shapes:
        if {str(k):str(v) for k,v in m1.bwd[a].items()} != {str(k):str(v) for k,v in m2.bwd[a].items()}:
            return False
    return True
