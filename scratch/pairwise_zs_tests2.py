"""Richer two-object exhaustive tests: loops + cross arrows in both factors."""
from pairwise_zs_check import FinCat, build_zs_product, check_zs_axioms
from pairwise_zs_tests import all_type_correct_lambdas, equivalence_test


def D_loop_up():
    """D on {0,1}: End(0)=Z/2={id0,n} (n^2=id0), d:0->1, dn:=d o n:0->1, End(1)={id1}."""
    objs = [0, 1]
    arrows = {"id0": (0, 0), "n": (0, 0), "id1": (1, 1),
              "d": (0, 1), "dn": (0, 1)}
    comp = {}
    # End(0) = Z/2
    e0 = {("id0", "id0"): "id0", ("id0", "n"): "n", ("n", "id0"): "n", ("n", "n"): "id0"}
    comp.update(e0)
    comp[("id1", "id1")] = "id1"
    # d, dn : 0->1 ; right action of End(0): d o id0 = d, d o n = dn, dn o id0 = dn, dn o n = d
    comp[("d", "id0")] = "d"; comp[("d", "n")] = "dn"
    comp[("dn", "id0")] = "dn"; comp[("dn", "n")] = "d"
    # left id1: id1 o d = d, id1 o dn = dn
    comp[("id1", "d")] = "d"; comp[("id1", "dn")] = "dn"
    ident = {0: "id0", 1: "id1"}
    return FinCat(objs, arrows, comp, ident)


def C_down():
    """C on {0,1}: thin, c:1->0, trivial ends."""
    objs = [0, 1]
    arrows = {"id0": (0, 0), "id1": (1, 1), "c": (1, 0)}
    comp = {("id0", "id0"): "id0", ("id1", "id1"): "id1",
            ("c", "id1"): "c", ("id0", "c"): "c"}
    ident = {0: "id0", 1: "id1"}
    return FinCat(objs, arrows, comp, ident)


def C_loopdown():
    """C on {0,1}: End(1)=Z/2={id1,h}, c:1->0, ch:=c o h. End(0) trivial."""
    objs = [0, 1]
    arrows = {"id0": (0, 0), "id1": (1, 1), "h": (1, 1),
              "c": (1, 0), "ch": (1, 0)}
    comp = {("id0", "id0"): "id0"}
    e1 = {("id1", "id1"): "id1", ("id1", "h"): "h", ("h", "id1"): "h", ("h", "h"): "id1"}
    comp.update(e1)
    comp[("c", "id1")] = "c"; comp[("c", "h")] = "ch"
    comp[("ch", "id1")] = "ch"; comp[("ch", "h")] = "c"
    comp[("id0", "c")] = "c"; comp[("id0", "ch")] = "ch"
    ident = {0: "id0", 1: "id1"}
    return FinCat(objs, arrows, comp, ident)


for Cf, Df, lab in [(C_down(), D_loop_up(), "Cdown x D(Z2-loop,up)"),
                    (C_loopdown(), D_loop_up(), "C(Z2-loop,down) x D(Z2-loop,up)")]:
    assert Cf.check_category(verbose=True), "C not a category"
    assert Df.check_category(verbose=True), "D not a category"
    equivalence_test(Cf, Df, lab)
