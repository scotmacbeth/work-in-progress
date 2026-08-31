"""
dcont_check.py
==============
Deliverable 1: the groupoid bases are genuine DIRECTED CONTAINERS (D1-D5),
via the DCont ~= Cat recipe (lean-verified DContCat.lean; Ahman-Uustalu):

    S        = objects of the category
    Pos(s)   = arrows OUT of s          (morphisms with domain s)
    root(s)  = id_s
    sub(s,p) = codomain of p
    shift(s,p,q) = q . p  (p: s->b, q: b->(sub b q))    [p in Pos s, q in Pos(sub s p)]

D-laws:
  D1 sub(s,root s)=s
  D2 shift(s,root s,p)=p
  D3 shift(s,p,root(sub s p))=p
  D4 sub(s,shift(s,p,q))=sub(sub(s,p),q)
  D5 shift(s,shift(s,p,q),r)=shift(s,p,shift(sub(s,p),q,r))

For a GROUPOID these all hold (a groupoid is a category); we machine-check on
  * B(Z/2), B(Z/4)  (one-object groupoids = groups),
  * the codiscrete groupoid on 2 objects.
"""
import sys
sys.path.insert(0, "/home/agent/projects/scratch")
from groupoid_zs import Zn, ZmxZn, Q8, codiscrete2

def cat_to_dcont_check(C):
    S = C.objs
    def Pos(s):   return [m for m in C.arrows if C.src[m] == s]
    def root(s):  return C.ident[s]
    def sub(s, p): return C.dst[p]
    def shift(s, p, q):   # q . p
        assert C.src[q] == C.dst[p]
        return C.compose(q, p)
    for s in S:
        assert sub(s, root(s)) == s, ("D1", s)
        for p in Pos(s):
            assert shift(s, root(s), p) == p, ("D2", s, p)     # id then p = p
            b = sub(s, p)
            assert shift(s, p, root(b)) == p, ("D3", s, p)     # p then id = p
            for q in Pos(b):
                assert sub(s, shift(s, p, q)) == sub(b, q), ("D4", s, p, q)
                c = sub(b, q)
                for r in Pos(c):
                    lhs = shift(s, shift(s, p, q), r)
                    rhs = shift(s, p, shift(b, q, r))
                    assert lhs == rhs, ("D5", s, p, q, r)
    return True

if __name__ == "__main__":
    for C in [Zn(2), Zn(4), ZmxZn(2, 2), Q8(), codiscrete2()[0]]:
        ok = cat_to_dcont_check(C)
        print(f"  {C.name:16s}: directed-container D1-D5 all hold: {ok}")
    print("\nAll groupoid bases are genuine directed containers (DCont ~= Cat).")
