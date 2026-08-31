from itertools import product
from monad import Cont, Lifting, check_monad

# ---- test containers ----
def make_tests():
    t=[]
    # small containers: shapes with various position-set sizes
    t.append(Cont(['a'], {'a':[0,1]}))                 # 1 shape, 2 positions
    t.append(Cont(['a','b'], {'a':[0],'b':[0,1]}))     # 2 shapes, sizes 1,2
    t.append(Cont(['a','b'], {'a':[0,1],'b':[0,1,2]})) # sizes 2,3
    return t

# =============== candidate: Sigma_U ===============
def sigma_U(e, U):
    U=list(U)
    def L_eval(Bs): return [(v,x) for v in U for x in Bs[v]]
    def L_act(elt,maps):
        v,x=elt; return (v, maps[v][x])
    def eps(elt): return elt[1]
    def delta(mm,S,P,elt):
        v,x=elt                      # v in U, x in P[diag[v]]=P[mm[v][v]]
        return (v,(v,x))             # (v, element (v,x) of pos_T[m^v])
    return Lifting(e,L_eval,L_act,eps,delta)

# =============== candidate: full product PI (no delta; existence tested elsewhere) ===============

# =============== candidate: weighted sum  L(B)=Sum_v W_v x B_v ===============
def weighted(e, W):   # W: dict v-> list of weight-tokens
    def L_eval(Bs): return [(v,w,x) for v in range(e) for w in W.get(v,[]) for x in Bs[v]]
    def L_act(elt,maps):
        v,w,x=elt; return (v,w,maps[v][x])
    def eps(elt): return elt[2]
    def delta(mm,S,P,elt):
        v,w,x=elt
        return (v,w,(v,w,x))
    return Lifting(e,L_eval,L_act,eps,delta)

# =============== candidate: B_0^2 (read leaf0 twice), two delta variants ===============
def leaf0sq(e, variant):
    def L_eval(Bs): return [(x0,x1) for x0 in Bs[0] for x1 in Bs[0]]
    def L_act(elt,maps):
        x0,x1=elt; return (maps[0][x0], maps[0][x1])
    def eps(elt): return elt[0]           # pick first copy
    def delta(mm,S,P,elt):
        x0,x1=elt                          # x0,x1 in P[mm[0][0]]
        # codomain: pos_TT[mm]=L over [pos_T[m^0]] = pos_T[m^0]^2
        # pos_T[m^0] = L over [P[m^0[0]]] = P[mm[0][0]]^2 ; element (z0,z1)
        if variant=='diag':      # ((x0,x1),(x0,x1))
            return ((x0,x1),(x0,x1))
        if variant=='split':     # ((x0,x0),(x1,x1))
            return ((x0,x0),(x1,x1))
        if variant=='cross':     # ((x0,x1),(x1,x0))
            return ((x0,x1),(x1,x0))
    return Lifting(e,L_eval,L_act,eps,delta)

if __name__=="__main__":
    # assoc builds T^3 (shapes |S|^(e^3)); keep containers TINY.
    tests=[Cont(['a'],{'a':[0,1]}),           # |S|=1, 2 pos  (cheap, full assoc)
           Cont(['a','b'],{'a':[0],'b':[0,1]})]  # |S|=2 sizes 1,2 (e=2: 2^8=256 shapes)
    print("=== e=2 ===")
    for U in [[0],[1],[0,1]]:
        r=check_monad(sigma_U(2,set(U)), tests)
        print(f"Sigma_U U={U}: {r}")
    print("--- e=3 (|S|=1 only, cheap) ---")
    tests3=[Cont(['a'],{'a':[0,1]}), Cont(['a'],{'a':[0,1,2]})]
    for U in [[0],[1,2],[0,1,2]]:
        r=check_monad(sigma_U(3,set(U)), tests3)
        print(f"Sigma_U(e=3) U={U}: {r}")
    print("--- weighted sums e=2 ---")
    for W in [ {0:['*'],1:['*']}, {0:['p','q'],1:['*']}, {0:['p','q']} ]:
        r=check_monad(weighted(2,W), tests)
        print(f"weighted W={W}: {r}")
    print("--- B_0^2 e=2 (3 delta variants) ---")
    for var in ['diag','split','cross']:
        r=check_monad(leaf0sq(2,var), tests)
        print(f"leaf0^2 {var}: {r}")
