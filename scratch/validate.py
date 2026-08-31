"""Validation: the enumerator must FIND bifunctors for object maps that are
known to admit functors, and must handle 'min' (unit=2). This checks the
solver is not vacuously returning 0 due to a bug."""
import importlib, itertools
import max_tensor as MT

# monkeypatch star_obj to different object maps and re-run core solver
def run_with(objmap, name):
    MT.star_obj = objmap
    # rebuild candidates closure uses MT.star_obj dynamically? candidates uses star_obj global.
    res = MT.solve_bifunctors(limit=5)
    print(f"object map {name}: found {len(res)} bifunctor(s) (capped at 5)")
    return res

# projection: A*B := A  (a genuine functor, the left projection)
run_with(lambda a,b: a, "proj_left |A*B|=|A|")
# min : closed on {0,1,2}
run_with(lambda a,b: min(a,b), "min")
# constant to 1? object map =1 always is NOT a functor-friendly? test
run_with(lambda a,b: 1, "const-1")
# back to max
run_with(lambda a,b: max(a,b), "max")
