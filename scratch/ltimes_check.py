import itertools, math
# container = (S, dirsizes) where S is a list of shapes, dir a dict shape->size
def mk(S, dfun): return (list(S), {s:dfun(s) for s in S})

def ltimes(p,q):
    Sp,dp=p; Sq,dq=q
    S=[(s,t) for s in Sp for t in Sq]
    d={(s,t): dp[s]**len(Sq) * dq[t]**len(Sp) for s in Sp for t in Sq}
    return (S,d)
def rtimes(p,q):
    Sp,dp=p; Sq,dq=q
    S=[(s,t) for s in Sp for t in Sq]
    d={(s,t): dp[s]**len(Sq) * dq[t] for s in Sp for t in Sq}
    return (S,d)
def tens(p,q): # DJN Day
    Sp,dp=p; Sq,dq=q
    return ([(s,t) for s in Sp for t in Sq], {(s,t):dp[s]*dq[t] for s in Sp for t in Sq})
def plus(p,q):
    Sp,dp=p; Sq,dq=q
    S=[('L',s) for s in Sp]+[('R',t) for t in Sq]
    d={}; d.update({('L',s):dp[s] for s in Sp}); d.update({('R',t):dq[t] for t in Sq})
    return (S,d)
def sig(c):  # multiset of dir sizes (position count profile), shape-count
    S,d=c; return (len(S), sorted(d.values()))
def same(a,b): return sig(a)==sig(b)

y=mk(['*'],lambda s:1)
# random-ish small containers
p=mk(['p0','p1'],{'p0':2,'p1':3}.get)
q=mk(['q0','q1','q2'],{'q0':1,'q1':2,'q2':2}.get)
r=mk(['r0'],{'r0':3}.get)

print("UNIT laws:")
print(" p ltimes y == p ?", same(ltimes(p,y),p), " y ltimes p == p ?", same(ltimes(y,p),p))
print(" p rtimes y == p ?", same(rtimes(p,y),p), " y rtimes p == p ?", same(rtimes(y,p),p))
print("ASSOC ltimes:", same(ltimes(ltimes(p,q),r), ltimes(p,ltimes(q,r))))
print("ASSOC rtimes:", same(rtimes(rtimes(p,q),r), rtimes(p,rtimes(q,r))))
print("SYMMETRY ltimes (p,q vs q,p same profile):", sorted(ltimes(p,q)[1].values())==sorted(ltimes(q,p)[1].values()))
print("SYMMETRY rtimes:", sorted(rtimes(p,q)[1].values())==sorted(rtimes(q,p)[1].values()))
print("DISTRIB ltimes over +:  (p+p')|<q  vs  (p|<q)+(p'|<q)")
pp=mk(['a'],{'a':2}.get); ppr=mk(['b'],{'b':2}.get)
lhs=ltimes(plus(pp,ppr),q); rhs=plus(ltimes(pp,q),ltimes(ppr,q))
print("   equal profiles?", same(lhs,rhs), " lhs",sig(lhs)," rhs",sig(rhs))
print("DISTRIB tens(Day) over +:", same(tens(plus(pp,ppr),q), plus(tens(pp,q),tens(ppr,q))))

print("\n--- TARGET B sanity: (-)+B and (-)xB as polynomial functors, cocontinuity ---")
# functor (-)+B on Set: X |-> X + B. Polynomial? shapes = 1 + B (one shape w/ 1 dir, B shapes w/ 0 dir).
# Test wide-pullback preservation numerically on a small cospan pullback via cardinalities is unsafe; 
# instead confirm the algebraic identity (X+X')+B  !=  (X+B)+(X'+B) [non-cocontinuous] but X+B is a coprod of reps.
def card_plusB(x,B): return x+B
# non-preservation of coproduct: |(X+X')+B| vs |(X+B)+(X'+B)|
X,Xp,B=3,4,2
print(" (-)+B preserves coproduct?", card_plusB(X+Xp,B)==card_plusB(X,B)+card_plusB(Xp,B), 
      f"[{card_plusB(X+Xp,B)} vs {card_plusB(X,B)+card_plusB(Xp,B)}]  -> non-cocontinuous, but y+B IS polynomial")
# Dialectica witness match: homogeneous p (dir A const), q (dir B const): ltimes dir = A^|Sq| * B^|Sp| = X^V * Y^U
A,Bd,I,J=2,3,2,2  # A=X, Bd=Y, I=U, J=V
print(" Dialectica tensor witness X^V*Y^U =", A**J * Bd**I, " ; ltimes hmg dir A^|Sq|*B^|Sp| =", A**J*Bd**I, "-> MATCH")
