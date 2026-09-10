#!/usr/bin/env python3
"""
O_{2,C3} HYBRID operad model (Rick's Problem 5.23 test).

Generators of the free symmetric operad O = O_{2,C3}:
  (1) mu  : BINARY,  slot-symmetry S_2  => mu(x,y)=mu(y,x)  (COMMUTATIVE).
  (2) omega: TERNARY, slot-symmetry C_3 = <(0 1 2)>  (cyclic, NOT S_3).
  (3) e   : absorbed nullary unit.  Absorption deletes e-slots:
              mu(x,e)=x, mu(e,e)=e,
              omega(x,y,e)=mu(x,y), omega(x,e,e)=x, omega(e,e,e)=e.
    NOTE: omega with ONE unit slot reduces to the COMMUTATIVE mu (this is forced /
    consistent with C_3 symmetry of omega + absorption, and is the decisive structural
    difference from the pure-C_3 residual where the binary composite was non-commutative).

M = free-algebra monad, M(X)=normal-form O-trees with X-leaves.  a_0=|M(empty)|=1 (only e).

Tree data model (single O-tree):
  ('L', k)                leaf carrying label k
  ('U',)                  absorbable nullary unit e
  ('P',)                  RIGID filler leaf E' (a peg: NOT absorbed, carries no label,
                          invariant under relabeling).  Used as inner-unit-as-outer-leaf.
  ('M', (c0,c1))          binary mu node   (children canonicalised: SORTED => S_2 commutative)
  ('W', (c0,c1,c2))       ternary omega node (children canonicalised up to C_3 rotation)

Two-level (M o M) model:
  ('OL', inner_tree)      outer leaf carrying an inner O-tree; peg = ('OL',('U',))
  ('OU',)                 outer absorbable unit
  ('OM',(c0,c1))          outer mu node
  ('OW',(c0,c1,c2))       outer omega node
"""
import itertools
from collections import Counter

# ----------------------------------------------------------------------
# inner single-O-tree canonicalisation
# ----------------------------------------------------------------------
def C3_rots(triple):
    a,b,c=triple
    return [(a,b,c),(c,a,b),(b,c,a)]   # the 3 cyclic rotations

def canon(t):
    tag=t[0]
    if tag in ('L','U','P'): return t
    if tag=='M':
        kids=[canon(k) for k in t[1]]
        return reduce_mu(kids)
    if tag=='W':
        kids=[canon(k) for k in t[1]]
        return reduce_omega(kids)
    raise ValueError(t)

def is_unit(k): return k==('U',)

def reduce_mu(kids):
    real=[k for k in kids if not is_unit(k)]   # peg P counts as REAL
    if len(real)==0: return ('U',)
    if len(real)==1: return real[0]
    # 2 real children: commutative -> sort
    return ('M', tuple(sorted(real)))

def reduce_omega(kids):
    real=[k for k in kids if not is_unit(k)]
    if len(real)==0: return ('U',)
    if len(real)==1: return real[0]
    if len(real)==2:
        # omega(x,y,e) = mu(x,y)  (COMMUTATIVE binary composite)
        return reduce_mu(real)
    # 3 real children: canonicalise up to C_3 rotation
    best=min(C3_rots(tuple(real)))
    return ('W', best)

def relabel(t,perm):
    tag=t[0]
    if tag=='L': return ('L',perm[t[1]])
    if tag in ('U','P'): return t
    if tag=='M': return ('M',tuple(relabel(k,perm) for k in t[1]))
    if tag=='W': return ('W',tuple(relabel(k,perm) for k in t[1]))
    raise ValueError(t)

def labels_of(t):
    tag=t[0]
    if tag=='L': return {t[1]}
    if tag in ('U','P'): return set()
    s=set()
    for k in t[1]: s|=labels_of(k)
    return s

def aut(t,n):
    """Aut(t) <= S_n by brute force over all permutations of range(n)."""
    base=canon(t); G=[]
    for p in itertools.permutations(range(n)):
        if canon(relabel(t,list(p)))==base: G.append(tuple(p))
    return G

# ----------------------------------------------------------------------
# outer (M o M) canonicalisation
# ----------------------------------------------------------------------
def ocanon(t):
    tag=t[0]
    if tag=='OL': return ('OL',canon(t[1]))
    if tag=='OU': return t
    if tag=='OM':
        kids=[ocanon(k) for k in t[1]]
        return oreduce_mu(kids)
    if tag=='OW':
        kids=[ocanon(k) for k in t[1]]
        return oreduce_omega(kids)
    raise ValueError(t)

def ois_unit(k): return k==('OU',)

def oreduce_mu(kids):
    real=[k for k in kids if not ois_unit(k)]
    if len(real)==0: return ('OU',)
    if len(real)==1: return real[0]
    return ('OM',tuple(sorted(real)))

def oreduce_omega(kids):
    real=[k for k in kids if not ois_unit(k)]
    if len(real)==0: return ('OU',)
    if len(real)==1: return real[0]
    if len(real)==2: return oreduce_mu(real)
    best=min(C3_rots(tuple(real)))
    return ('OW',best)

def orelabel(t,perm):
    tag=t[0]
    if tag=='OL': return ('OL',relabel(t[1],perm))
    if tag=='OU': return t
    if tag=='OM': return ('OM',tuple(orelabel(k,perm) for k in t[1]))
    if tag=='OW': return ('OW',tuple(orelabel(k,perm) for k in t[1]))
    raise ValueError(t)

def oaut(t,n):
    base=ocanon(t); G=[]
    for p in itertools.permutations(range(n)):
        if ocanon(orelabel(t,list(p)))==base: G.append(tuple(p))
    return G

# ----------------------------------------------------------------------
# pretty printing
# ----------------------------------------------------------------------
def cyc(perm):
    n=len(perm); seen=[False]*n; out=[]
    for i in range(n):
        if seen[i] or perm[i]==i: seen[i]=True; continue
        c=[]; j=i
        while not seen[j]: seen[j]=True; c.append(j); j=perm[j]
        if len(c)>1: out.append(tuple(c))
    return "id" if not out else "".join("("+" ".join(map(str,c))+")" for c in out)
def show(G): return sorted(cyc(list(g)) for g in G)

def conj_key(G,n):
    """S_n-conjugacy invariant of the group G: (order, sorted cycle-type multiset)."""
    def ctype(p):
        seen=[False]*n;t=[]
        for i in range(n):
            if seen[i]:continue
            c=0;j=i
            while not seen[j]: seen[j]=True;c+=1;j=p[j]
            t.append(c)
        return tuple(sorted(t))
    return (len(G),tuple(sorted(Counter(ctype(list(g)) for g in G).items())))

# node constructors
L=lambda k:('L',k); U=('U',); P=('P',)
Mu=lambda a,b:('M',(a,b)); Om=lambda a,b,c:('W',(a,b,c))
OL=lambda t:('OL',t); OU=('OU',); OMu=lambda a,b:('OM',(a,b)); OOm=lambda a,b,c:('OW',(a,b,c))

# ----------------------------------------------------------------------
# SANITY
# ----------------------------------------------------------------------
if __name__=='__main__':
    print("=== SANITY: O_{2,C3} generators ===")
    print("mu(0,1) canon:", canon(Mu(L(0),L(1))))
    print("mu(1,0) canon:", canon(Mu(L(1),L(0))))
    print("  mu commutative? mu(0,1)==mu(1,0):", canon(Mu(L(0),L(1)))==canon(Mu(L(1),L(0))))
    print("  Aut(mu(0,1)) =", show(aut(Mu(L(0),L(1)),2)), " (expect (0 1): S_2)")
    print("mu(0,e) canon:", canon(Mu(L(0),U)), " (expect leaf 0)")
    print("  mu(0,e)==leaf0?", canon(Mu(L(0),U))==L(0))
    print("mu(e,e) canon:", canon(Mu(U,U)), " (expect e)")
    print()
    print("omega(0,1,2) canon:", canon(Om(L(0),L(1),L(2))))
    print("  Aut(omega(0,1,2)) =", show(aut(Om(L(0),L(1),L(2)),3)), " (expect a 3-cycle: C_3)")
    print("  omega(0,1,2)==omega(1,2,0) (cyclic)?",
          canon(Om(L(0),L(1),L(2)))==canon(Om(L(1),L(2),L(0))))
    print("  omega(0,1,2)==omega(1,0,2) (transposition, should FAIL for C_3)?",
          canon(Om(L(0),L(1),L(2)))==canon(Om(L(1),L(0),L(2))))
    print("omega(0,1,e) canon:", canon(Om(L(0),L(1),U)), " (expect mu(0,1))")
    print("  omega(0,1,e)==mu(0,1)?", canon(Om(L(0),L(1),U))==canon(Mu(L(0),L(1))))
    print("  omega(0,1,e)==omega(1,0,e) (=> mu commutative via C_3+absorption)?",
          canon(Om(L(0),L(1),U))==canon(Om(L(1),L(0),U)))
    print("omega(0,e,e) canon:", canon(Om(L(0),U,U)), " (expect leaf 0)")
    print("omega(e,e,e) canon:", canon(Om(U,U,U)), " (expect e)")
    print()
    print("peg P: relabel-invariant, not absorbed. mu(2,P) canon:", canon(Mu(L(2),P)))
    print("  Aut(mu(2,P)) on 1 label =", show(aut(Mu(L(2),P),3)), " (peg pins nothing but leaf 2 fixed)")
