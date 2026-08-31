from enum import enum_liftings
from catcount import count_categories
from monad import Cont
# cheap scan on |S|=1 ; verify on |S|=2 with TINY positions (leaf-distinguishing)
tests_scan=[Cont(['a'],{'a':[0,1]}), Cont(['a'],{'a':[0,1,2]})]
tests_verify=[Cont(['a','b'],{'a':[0],'b':[0,1]})]
cases={
 "B0^2+B1":     ([(2,0),(0,1)], count_categories([2])*count_categories([1])),
 "B0^2+B1^2":   ([(2,0),(0,2)], count_categories([2])*count_categories([2])),
 "B0^2+B0+B1":  ([(2,0),(1,0),(0,1)], count_categories([2,1])*count_categories([1])),
 "B0+B1(=Sig)": ([(1,0),(0,1)], count_categories([1])*count_categories([1])),
}
for name,(shapes,pred) in cases.items():
    monads,count=enum_liftings(shapes,2,tests_scan,tests_verify)
    print(f"{name:14s} shapes={shapes}: enum #monads={len(monads)} / {count} ; catcount={pred} ; MATCH={len(monads)==pred}",flush=True)
