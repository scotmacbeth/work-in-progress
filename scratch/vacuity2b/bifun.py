"""
Finite unital bifunctors on Set and the four vacuity tasks.

Conventions (matching support_no_assoc_full.py / day-family/core.py):
  * finite sets  = python frozensets of hashable elements
  * base sets    = frozenset(range(n))          (elements are ints)
  * functions    = python dicts {domain_elt: codomain_elt}
  * A * B        = frozenset of TAGGED tuples, so the functorial action is
                   unambiguous.  Tags: ('l',a) A-part, ('r',b) B-part,
                   ('m',...) middle part, ('dot',) the support point.
  * bifunctor    = object with  star(A,B) -> frozenset,
                                 smap(f,g,A,B) -> dict on star(A,B),
                                 unit  (the unit set),
                                 lam_inv(C) -> dict c -> element of star(unit,C)
                   (inverse left unitor; only meaningful when unit = EMPTY).
"""
import itertools, random

EMPTY = frozenset()
def nset(n): return frozenset(range(n))
ONE = nset(1)          # {0}
TWO = nset(2)          # {0,1}
THREE = nset(3)

def idmap(S): return {s: s for s in S}
def bang(C):  return {c: 0 for c in C}          # C -> ONE, everything -> 0
EMPTYMAP = {}                                    # the map EMPTY -> anything
# points of a J-set as maps ONE -> J
def point(j): return {0: j}

# ---------------------------------------------------------------- bifunctors
class Bifun:
    unit = EMPTY
    def lam_inv(self, C):
        # for all EMPTY-unit examples below, star(EMPTY,C) = {('r',c)}
        return {c: ('r', c) for c in C}

class COPROD(Bifun):
    name = "COPROD  A+B"
    def star(self, A, B):
        return frozenset([('l', a) for a in A] + [('r', b) for b in B])
    def smap(self, f, g, A, B):
        d = {}
        for x in self.star(A, B):
            d[x] = ('l', f[x[1]]) if x[0] == 'l' else ('r', g[x[1]])
        return d

class JOIN(Bifun):
    name = "JOIN    A+B+AxB"
    def star(self, A, B):
        return frozenset([('l', a) for a in A] + [('r', b) for b in B]
                         + [('m', (a, b)) for a in A for b in B])
    def smap(self, f, g, A, B):
        d = {}
        for x in self.star(A, B):
            if x[0] == 'l':  d[x] = ('l', f[x[1]])
            elif x[0] == 'r': d[x] = ('r', g[x[1]])
            else:
                a, b = x[1]; d[x] = ('m', (f[a], g[b]))
        return d

class VEE(Bifun):
    def __init__(self, S):
        self.S = S
        self.name = f"VEE_S   A+AxSxB+B  |S|={len(S)}"
    def star(self, A, B):
        return frozenset([('l', a) for a in A] + [('r', b) for b in B]
                         + [('m', (a, s, b)) for a in A for s in self.S for b in B])
    def smap(self, f, g, A, B):
        d = {}
        for x in self.star(A, B):
            if x[0] == 'l':  d[x] = ('l', f[x[1]])
            elif x[0] == 'r': d[x] = ('r', g[x[1]])
            else:
                a, s, b = x[1]; d[x] = ('m', (f[a], s, g[b]))
        return d

class SUPPORT(Bifun):
    name = "SUPPORT A+B+{dot iff both nonempty}   (NON-ASSOC)"
    def star(self, A, B):
        e = [('l', a) for a in A] + [('r', b) for b in B]
        if A and B: e.append(('dot',))
        return frozenset(e)
    def smap(self, f, g, A, B):
        d = {}
        for x in self.star(A, B):
            if x == ('dot',): d[x] = ('dot',)
            elif x[0] == 'l':  d[x] = ('l', f[x[1]])
            else:              d[x] = ('r', g[x[1]])
        return d

class DIRICHLET(Bifun):
    name = "DIRICHLET  AxB   (unit = 1, NOT empty)"
    unit = ONE
    def star(self, A, B):
        return frozenset((a, b) for a in A for b in B)
    def smap(self, f, g, A, B):
        return {(a, b): (f[a], g[b]) for a in A for b in B}
    def lam_inv(self, C):
        raise NotImplementedError("Dirichlet unit is 1, EMPTY-formulas N/A")

# ------------------------------------------------------------ shared helpers
def eta(bif, C):
    """eta_C : C -> unit*C  =  (! * C) o lambda^{-1},  unit = EMPTY."""
    li = bif.lam_inv(C)
    m = bif.smap(EMPTYMAP, idmap(C), EMPTY, C)   # star(EMPTY,C) -> star(ONE,C)
    return {c: m[li[c]] for c in C}

def is_bijection_onto(dom_map, target):
    """dom_map : dict (its keys=domain).  True iff injective and image == target."""
    vals = list(dom_map.values())
    inj = len(vals) == len(set(vals))
    onto = set(vals) == set(target)
    return inj and onto, inj, onto

# ==========================================================================
# TASK 1  --  Lemma D
# ==========================================================================
def task1(bif):
    rows = []
    for Bn, B in [("1", ONE), ("2", TWO)]:
        SB = bif.star(ONE, B)                       # 1*B
        i0B = bif.smap({0: 0}, idmap(B), ONE, B)    # (i0 * B): 1*B -> 2*B
        i1B = bif.smap({0: 1}, idmap(B), ONE, B)
        balanced = [u for u in SB if i0B[u] == i1B[u]]
        K = SB                                       # the set 1*B
        etaK = eta(bif, K)                           # eta_{1*B}: K -> 1*K
        etaB = eta(bif, B)                           # eta_B : B -> 1*B
        oneEtaB = bif.smap(idmap(ONE), etaB, ONE, B) # (1 * eta_B): 1*B -> 1*(1*B)
        results = []
        for u in balanced:
            lhs = etaK[u]
            rhs = oneEtaB[u]
            results.append((u, lhs == rhs))
        rows.append((Bn, balanced, results))
    return rows

# ==========================================================================
# TASK 2  --  star'  (pullback preservation)
# ==========================================================================
def task2(bif, Cs=("0","1","2","3")):
    out = {}
    # p_L = eta_1(*) in 1*1
    pL = eta(bif, ONE)[0]
    Cmap = {"0": EMPTY, "1": ONE, "2": TWO, "3": THREE}
    for Cn in Cs:
        C = Cmap[Cn]
        bangC = bang(C)                                    # C -> ONE
        starEC = bif.star(EMPTY, C)                        # EMPTY * C
        starOC = bif.star(ONE, C)                          # 1 * C
        starE1 = bif.star(EMPTY, ONE)                      # EMPTY * 1
        bangE_C = bif.smap(EMPTYMAP, idmap(C), EMPTY, C)   # !*C : E*C -> 1*C
        E_bangC = bif.smap(EMPTYMAP, bangC, EMPTY, C)      # E*!_C : E*C -> E*1
        one_bangC = bif.smap(idmap(ONE), bangC, ONE, C)    # 1*!_C : 1*C -> 1*1
        bang_1 = bif.smap(EMPTYMAP, idmap(ONE), EMPTY, ONE)# !*1  : E*1 -> 1*1
        # PB = {(x,y) in (1*C)x(E*1) : (1*!_C)(x) = (!*1)(y)}
        PB = set()
        for x in starOC:
            for y in starE1:
                if one_bangC[x] == bang_1[y]:
                    PB.add((x, y))
        # phi_C : E*C -> PB
        phi = {w: (bangE_C[w], E_bangC[w]) for w in starEC}
        img = set(phi.values())
        inj = len(set(phi.values())) == len(phi)
        onto = img == PB
        # simpler equivalent: eta_C injective and im(eta_C)=(1*!_C)^{-1}(p_L)
        etaC = eta(bif, C)
        fiber = {x for x in starOC if one_bangC[x] == pL}
        etainj = len(set(etaC.values())) == len(etaC)
        equiv = etainj and set(etaC.values()) == fiber
        out[Cn] = dict(phi_bij=(inj and onto), phi_inj=inj, phi_onto=onto,
                       equiv=equiv, fiber_size=len(fiber), imC_size=len(set(etaC.values())),
                       pL=pL, agree=((inj and onto) == equiv))
    return out

# ==========================================================================
# TASK 3  --  WIDE star'
# ==========================================================================
def task3(bif, Js=(2,3), Cs=("1","2")):
    out = {}
    Cmap = {"1": ONE, "2": TWO}
    for jn in Js:
        J = nset(jn)
        pts = [point(j) for j in J]                    # points 1 -> J
        for Cn in Cs:
            C = Cmap[Cn]
            starOC = bif.star(ONE, C)
            starEC = bif.star(EMPTY, C)
            # (a*C): 1*C -> J*C  for each point a
            actions = [bif.smap(a, idmap(C), ONE, C) for a in pts]
            WPB = [u for u in starOC
                   if all(actions[i][u] == actions[0][u] for i in range(len(actions)))]
            WPB = set(WPB)
            # canonical map  E*C -> 1*C   (! * C)
            canon = bif.smap(EMPTYMAP, idmap(C), EMPTY, C)
            img = set(canon.values())
            inj = len(set(canon.values())) == len(canon)
            onto_wpb = img == WPB
            out[(jn, Cn)] = dict(passes=(inj and onto_wpb and img <= WPB),
                                 wpb_size=len(WPB), img_size=len(img),
                                 img_subset=img <= WPB, onto=onto_wpb)
    return out

# ==========================================================================
# TASK 4  --  eta_C mono & split
# ==========================================================================
def task4(bif, Cs=("1","2","3")):
    out = {}
    Cmap = {"1": ONE, "2": TWO, "3": THREE}
    for Cn in Cs:
        C = Cmap[Cn]
        etaC = eta(bif, C)
        inj = len(set(etaC.values())) == len(etaC)
        # retraction r: 1*C -> C with r o eta = id ; exists iff eta injective and C nonempty
        starOC = bif.star(ONE, C)
        retr = None
        if inj and C:
            c0 = next(iter(C))
            inv = {etaC[c]: c for c in C}
            retr = {x: inv.get(x, c0) for x in starOC}
            ok = all(retr[etaC[c]] == c for c in C)
            retr = ok
        out[Cn] = dict(inj=inj, has_retraction=retr)
    return out

# ==========================================================================
# TASK 2 crux -- exhaustive search over VALID functors G=F(1,-) + natural eta
#   G(EMPTY)={*} (right unit),  data (V,W,v0,p,q,r,sigma), functor axioms,
#   eta natural determined by p_L in V.  star'_2 tested directly.
# ==========================================================================
def all_funcs(dom, cod):
    dom = list(dom)
    for vals in itertools.product(cod, repeat=len(dom)):
        yield dict(zip(dom, vals))

def compose(g2, g1):
    return {x: g2[g1[x]] for x in g1}

def functor_valid(V, W, v0, p, q, r, sigma):
    # build G on every skel morphism, verify functoriality on all composites
    idV = idmap(V); idW = idmap(W)
    c0 = compose(p, r)   # i0 o !_2
    c1 = compose(q, r)   # i1 o !_2
    rho = {'*': v0}      # G(!_{E->1}): {*} -> V
    rho2 = {'*': p[v0]}  # G(!_{E->2})
    # F4: p o rho == q o rho  (since !_{E2}=i0 o !_{E1}=i1 o !_{E1})
    if p[v0] != q[v0]: return None
    # morphisms:  key -> (src,tgt,map)
    E, O, T = frozenset({'*'}), V, W    # sets G(EMPTY),G(1),G(2)   note G(EMPTY)={*}
    Gm = {}
    Gm[('idE',)] = ('E','E', {'*':'*'})
    Gm[('id1',)] = ('1','1', idV)
    Gm[('id2',)] = ('2','2', idW)
    Gm[('i0',)]  = ('1','2', p)
    Gm[('i1',)]  = ('1','2', q)
    Gm[('bang2',)]=('2','1', r)
    Gm[('swap',)]= ('2','2', sigma)
    Gm[('c0',)]  = ('2','2', c0)
    Gm[('c1',)]  = ('2','2', c1)
    Gm[('e1',)]  = ('E','1', rho)
    Gm[('e2',)]  = ('E','2', rho2)
    sets = {'E': {'*'}, '1': set(V), '2': set(W)}
    # underlying morphisms in skel (as label -> (src,tgt,dict on base sets))
    # BASE-category (skel) morphisms: EMPTY is initial, so maps out of it are {}.
    base = {
      'idE':('E','E',{}), 'id1':('1','1',idmap(nset(1))), 'id2':('2','2',idmap(nset(2))),
      'i0':('1','2',{0:0}), 'i1':('1','2',{0:1}), 'bang2':('2','1',{0:0,1:0}),
      'swap':('2','2',{0:1,1:0}), 'c0':('2','2',{0:0,1:0}), 'c1':('2','2',{0:1,1:1}),
      'e1':('E','1',{}), 'e2':('E','2',{}),
    }
    # verify functoriality: for composable base maps g1:X->Y, g2:Y->Z, G(g2 o g1)=G(g2)oG(g1)
    def base_map(lbl): return base[lbl][2]
    def find_label(src, tgt, m):
        for lbl,(s,t,mm) in base.items():
            if s==src and t==tgt and mm==m: return lbl
        return None
    for l1 in base:
        s1,t1,m1 = base[l1]
        for l2 in base:
            s2,t2,m2 = base[l2]
            if t1 != s2: continue
            comp = {x: m2[m1[x]] for x in m1}
            lbl = find_label(s1,t2,comp)
            if lbl is None: return None   # composite not represented -> skip (shouldn't happen)
            G1 = Gm[(l1,)][2]; G2 = Gm[(l2,)][2]
            Gcomp = {x: G2[G1[x]] for x in G1}
            if Gcomp != Gm[(lbl,)][2]:
                return None
    return dict(p=p,q=q,r=r,sigma=sigma,v0=v0,V=V,W=W)

def search_star_prime(maxsize=3):
    found_fail = []
    tested = 0
    for nV in range(1, maxsize+1):
        for nW in range(1, maxsize+1):
            V, W = nset(nV), nset(nW)
            for p in all_funcs(V, W):
                for q in all_funcs(V, W):
                    for r in all_funcs(W, V):
                        # cheap axiom prefilter
                        if any(r[p[v]] != v for v in V): continue
                        if any(r[q[v]] != v for v in V): continue
                        for sigma in all_funcs(W, W):
                            if any(sigma[p[v]] != q[v] for v in V): continue
                            if any(sigma[q[v]] != p[v] for v in V): continue
                            if any(sigma[sigma[w]] != w for w in W): continue
                            for v0 in V:
                                G = functor_valid(V, W, v0, p, q, r, sigma)
                                if G is None: continue
                                tested += 1
                                # natural eta for each basepoint p_L in V:
                                for pL in V:
                                    # eta_2 = {0:p(pL),1:q(pL)}
                                    im2 = {p[pL], q[pL]}
                                    einj = p[pL] != q[pL]
                                    fiber = {w for w in W if r[w] == pL}
                                    ok = einj and (im2 == fiber)
                                    if not ok:
                                        found_fail.append(dict(
                                            nV=nV,nW=nW,V=sorted(V),W=sorted(W),
                                            p=p,q=q,r=r,sigma=sigma,v0=v0,pL=pL,
                                            im_eta2=sorted(im2), fiber=sorted(fiber),
                                            eta_inj=einj))
    return tested, found_fail

if __name__ == "__main__":
    print("="*74)
    print("SANITY: unit laws  star(EMPTY,C) ~ C  and  star(C,EMPTY) ~ C")
    for bif in [COPROD(), JOIN(), VEE(nset(1)), VEE(nset(2)), SUPPORT()]:
        okL = all(len(bif.star(EMPTY, nset(n))) == n for n in range(4))
        okR = all(len(bif.star(nset(n), EMPTY)) == n for n in range(4))
        print(f"  {bif.name:40s} left-unit={okL} right-unit={okR}")
