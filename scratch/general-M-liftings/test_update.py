"""
Probe update-monad degree-1 liftings for several (monoid, action) pairs on S={0,1}.
Mirrors targeted.py's T1/T2/T3 (which MacBeth trusts for State), now update-monad general.

Decisive comparison, DELIBERATELY separating |P| from pi0(action):
  reader_triv : P=1                 down(s,p)=s        pi0=2   (= Reader)
  Z2_swap     : P=Z/2 (nontrivial)  down(s,1)=1-s      pi0=1   (NEITHER Reader NOR State)
  Z2_triv     : P=Z/2 (nontrivial)  down(s,p)=s        pi0=2   (NEITHER Reader NOR State)
  overwrite   : P=1+S (State's mon.) down=overwrite     pi0=1   (= State)
If pi0 governs, Z2_swap behaves like State (1 orbit) and Z2_triv like Reader (2 orbits),
regardless of |P|.
"""
from itertools import product
import update_engine as U
S = U.S

# ---- acts ----
reader_triv = U.Act(elems=['o'], o='o', oplus=lambda a, b: 'o',
                    down=lambda s, p: s, name='reader_triv (P=1)')

Z2_swap = U.Act(elems=[0, 1], o=0, oplus=lambda a, b: (a + b) % 2,
                down=lambda s, p: (s if p == 0 else 1 - s), name='Z2_swap')

Z2_triv = U.Act(elems=[0, 1], o=0, oplus=lambda a, b: (a + b) % 2,
                down=lambda s, p: s, name='Z2_triv')

# overwrite (State) : free monoid on overwrite semigroup on S = {o,w0,w1}
OW = ['o', 'w0', 'w1']
def ow_plus(a, b):
    if a == 'o': return b
    if b == 'o': return a
    return b            # inr s (+) inr s' = inr s'  (overwrite)
def ow_down(s, p):
    return s if p == 'o' else int(p[1])
overwrite = U.Act(elems=OW, o='o', oplus=ow_plus, down=ow_down, name='overwrite (State)')

ACTS = [reader_triv, Z2_swap, Z2_triv, overwrite]
print("=== orbit counts pi0(down) ===")
for a in ACTS:
    print(f"  {a.name:22s}: |P|={len(a.elems)}  pi0={a.orbits()}")

# ---- Sigma sanity: single object per state, trivial transport ----
print("\n=== Sigma (1 obj/state, trivial transport) laws ===")
for a in ACTS:
    O = {0: ['*'], 1: ['*']}
    keys = [(f, g, s, c) for f in a.SHAPES for g in product(a.SHAPES, repeat=2)
            for s in S for c in O[s]]
    OUT = {k: '*' for k in keys}; INN = {k: '*' for k in keys}
    A, eps, delta = U.build_deg1(a, O, OUT, INN)
    print(f"  {a.name:22s}: laws={U.laws_ok(a, A, eps, delta)}")

# ---- targeted T1/T2/T3 with 2 objects/state ----
O2 = {0: ['A', 'B'], 1: ['A', 'B']}
SW = {'A': 'B', 'B': 'A'}
ID2 = {'A': 'A', 'B': 'B'}

def build_from_psi(a, psi):
    """psi: dict (s,m)->(dict O_s->O_m). endpoint-local INN, OUT=id."""
    keys = [(f, g, s, c) for f in a.SHAPES for g in product(a.SHAPES, repeat=2)
            for s in S for c in O2[s]]
    OUT = {(f, g, s, c): c for (f, g, s, c) in keys}
    INN = {}
    for (f, g, s, c) in keys:
        m = a.down(s, f[s])
        INN[(f, g, s, c)] = psi[(s, m)][c]
    return U.build_deg1(a, O2, OUT, INN)

def build_from_fn(a, tau):
    """tau(f,s,c) -> object at down(s,f[s]).  possibly NON endpoint-local (depends on full f)."""
    keys = [(f, g, s, c) for f in a.SHAPES for g in product(a.SHAPES, repeat=2)
            for s in S for c in O2[s]]
    OUT = {(f, g, s, c): c for (f, g, s, c) in keys}
    INN = {(f, g, s, c): tau(f, s, c) for (f, g, s, c) in keys}
    return U.build_deg1(a, O2, OUT, INN)

def reachable_pairs(a):
    return sorted({(s, a.down(s, p)) for s in S for p in a.elems})

print("\n=== targeted T1/T2/T3 (mirror of targeted.py) ===")
for a in [Z2_swap, Z2_triv, overwrite]:
    print(f"\n-- {a.name}  (pi0={a.orbits()}, reachable {reachable_pairs(a)}) --")
    RP = reachable_pairs(a)

    # T2a: psi=id everywhere reachable  => product  => PASS
    psi_id = {(s, m): dict(ID2) for (s, m) in RP}
    A, e, d = build_from_psi(a, psi_id)
    print(f"  T2a psi=id (product): units={U.check_units(a,A,e,d)} assoc={U.assoc_sample(a,A,e,d)[0]}")

    # T1: psi_{s->s}=swap (tau^o != id) but id elsewhere  => units should FAIL
    psi_T1 = {(s, m): (dict(SW) if s == m else dict(ID2)) for (s, m) in RP}
    A, e, d = build_from_psi(a, psi_T1)
    print(f"  T1  psi_(s->s)=swap (tau^o!=id): units={U.check_units(a,A,e,d)} (expect False)")

    # T2c: coherent within-orbit relabel: psi_(s->m)=swap for s!=m, id for s==m (only if cross pairs reachable)
    if any(s != m for (s, m) in RP):
        psi_rel = {(s, m): (dict(ID2) if s == m else dict(SW)) for (s, m) in RP}
        A, e, d = build_from_psi(a, psi_rel)
        print(f"  T2c coherent relabel (swap off-diag): units={U.check_units(a,A,e,d)} assoc={U.assoc_sample(a,A,e,d)[0]}")
    else:
        print("  T2c n/a (no cross-orbit reachable pair; orbits singletons)")

    # T3: NON endpoint-local functorial-ish: tau depends on full f, not just down(s,f[s])
    def tau_np(f, s, c, a=a):
        # map object by parity of the WHOLE outer update f[s] index in elems (not via endpoint)
        idx = a.elems.index(f[s])
        return SW[c] if (idx % 2 == 1) else c
    A, e, d = build_from_fn(a, tau_np)
    el = _ = None
    # endpoint-local iff tau_np depends on f[s] only through down(s,f[s]):
    isEL = all(
        (a.elems.index(p) % 2) == (a.elems.index(q) % 2)
        for s in S for p in a.elems for q in a.elems if a.down(s, p) == a.down(s, q)
    )
    print(f"  T3  tau_np endpoint-local? {isEL};  units={U.check_units(a,A,e,d)} assoc={U.assoc_sample(a,A,e,d)[0]}")

# ---- ORBIT INDEPENDENCE: count law-satisfying endpoint-local psi, check it factors over orbits ----
print("\n=== orbit-factoring of law-satisfying endpoint-local liftings (2 obj/state) ===")
def find_orbit_map(a):
    parent = {s: s for s in S}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for s in S:
        for p in a.elems:
            parent[find(s)] = find(a.down(s, p))
    return {s: find(s) for s in S}

for a in [reader_triv, Z2_swap, Z2_triv, overwrite]:
    RP = reachable_pairs(a)
    maps4 = [dict(zip(['A', 'B'], v)) for v in product(['A', 'B'], repeat=2)]  # 4 maps O->O
    survivors = 0
    for combo in product(maps4, repeat=len(RP)):
        psi = {RP[i]: combo[i] for i in range(len(RP))}
        A, e, d = build_from_psi(a, psi)
        if U.check_units(a, A, e, d) and U.assoc_sample(a, A, e, d, nsamp=200)[0] == 'ok':
            survivors += 1
    orb = find_orbit_map(a); norb = len(set(orb.values()))
    print(f"  {a.name:22s}: pi0={norb}  law-satisfying endpoint-local psi = {survivors}"
          f"   (per-orbit factor ~ {survivors ** (1.0/norb):.3f})")
