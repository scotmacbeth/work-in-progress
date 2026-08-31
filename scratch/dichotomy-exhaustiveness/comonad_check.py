"""
Certify the 'auxiliary-monoid Pi' family: A(Q)=Q(e0)^M is a monad lifting of R_E via
   ev_{e0}: R_E => Id  (monad morphism)   pulled back over   C_M(S,P)=(S,P^M)  (comonad lifting of Id).
Two checks:
 (1) ev_{e0}: R_E => Id is a monad morphism (eta, mu compatibility).
 (2) Q |-> Q^M is a comonad on Set  <=>  M a monoid:  counit=eval@unit, comult via mult; check laws.
"""
import itertools

# ---- (1) ev_{e0} monad morphism  R_E => Id ----
def check_ev_monad_morphism(nE, e0, Xsize=3):
    X=list(range(Xsize))
    ok=True
    # eta: X->X^E const ; ev(eta x)= x   (matches Id.eta = id)
    for x in X:
        if (tuple([x]*nE))[e0]!=x: ok=False
    # mu: (X^E)^E -> X^E, mu(g)(e)=g[e][e].  need ev(mu g) = ev( R_E(ev)(g) ) with Id.mu=id
    #   ev(mu g)=mu(g)[e0]=g[e0][e0]
    #   R_E(ev)(g): E->X, e|-> ev(g[e])=g[e][e0]; then ev at e0: g[e0][e0]
    for g in itertools.product(itertools.product(X,repeat=nE), repeat=nE):
        lhs=g[e0][e0]
        rhs=g[e0][e0]
        if lhs!=rhs: ok=False
    return ok

# ---- (2) Q^M comonad laws for a monoid M (given as Cayley table) ----
def check_exp_comonad(mult, unit, Qsize=3):
    Mel=list(range(len(mult)))
    Q=list(range(Qsize))
    QM=list(itertools.product(Q, repeat=len(Mel)))  # f: M->Q
    ok=True
    # counit eps: Q^M->Q, f|->f(unit)
    eps=lambda f: f[unit]
    # comult del: Q^M -> (Q^M)^M,  f |-> (m |-> (m'|-> f(m*m')))
    def dl(f):
        return tuple(tuple(f[mult[m][mp]] for mp in Mel) for m in Mel)
    # counit laws: (eps o at each) ... left: (eps applied to outer) then id; check (id): apply del, then eps on OUTER m-index -> should recover f
    for f in QM:
        d=dl(f)                      # d[m] in Q^M
        # left counit: eps on outer: pick m=unit component then that's a Q^M: d[unit] should = f
        if d[unit]!=f: ok=False
        # right counit: eps inside each: m|-> eps(d[m]) = d[m][unit]=f[m*unit]=f[m] -> = f
        if tuple(d[m][unit] for m in Mel)!=f: ok=False
        # coassoc: (del o del) two ways equal
        # (del x id) o del : f|-> m|->m'|-> del(f)(m*... ) ; compare (id x del) o del
        left = tuple(tuple(tuple(f[mult[mult[m][mp]][mpp]] for mpp in Mel) for mp in Mel) for m in Mel)
        right= tuple(tuple(tuple(f[mult[m][mult[mp][mpp]]] for mpp in Mel) for mp in Mel) for m in Mel)
        if left!=right: ok=False   # holds iff M associative
    return ok

# monoids on 2 elements: Z/2, and the AND-monoid (unit=1), the OR-monoid (unit=0)
Z2   = ([[0,1],[1,0]], 0)     # add mod 2, unit 0
AND  = ([[0,0],[0,1]], 1)     # mult, unit 1
# a NON-monoid (non-associative) to confirm the check discriminates:
BAD  = ([[0,1],[1,1]], 0)     # unit 0? check: 0 is unit? 0*x=[0,1][x]=x yes; x*0: [x][0]; 1*0=1 !=? need x. 1*0 should=1 -> table[1][0]=1 ok. assoc? (1*1)*1=1*1=1 ; 1*(1*1)=1 ok... try to find noncomm/nonassoc
NONASSOC = ([[0,0],[1,1]],0)  # 0 unit? 0*x=table[0][x]=0 !=x for x=1 -> not unit. so not a monoid.

for name,(mt,un) in [("Z/2",Z2),("AND(unit1)",AND),("nonunital",NONASSOC)]:
    print(f"Q^M comonad laws  M={name:12s}: {check_exp_comonad(mt,un)}")

print("ev_{e0} monad morphism R_E=>Id (E=2,e0=0):", check_ev_monad_morphism(2,0))
print("ev_{e0} monad morphism R_E=>Id (E=3,e0=1):", check_ev_monad_morphism(3,1))
