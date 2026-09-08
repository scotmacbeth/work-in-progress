"""
Stabilizer-flatness search over small a_0>=1 symmetric operads.

For each signature M:
  * build P_M[m]  = block-fixing products of single-M-element stabilizers on [m]
                    (the class the polynomial-outer Meta-theorem allows)
  * enumerate the each-label-once component (M o M)[m]: outer M-trees whose leaves
    are inner M-elements (disjoint label content covering [m] once) + content-free
    inner "peg" elements (built from constants) as outer leaves.
  * for every realised stabilizer H = Stab(w), test  H in P_M[m] (up to S_m conj).
  * an H not in P_M[m]  ==>  ESCAPE  ==>  M NOT stabilizer-flat, witness = w.

Prints, per (M,m): |P_M|, #(M o M) structures, whether an escape was found + witness.
"""
import importlib.util, sys, time
from itertools import product, combinations, permutations

spec = importlib.util.spec_from_file_location('L', 'scratch/2026-09-07-stabflat-search-lib.py')
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
Sig = L.Sig

# ---------------- outer trees (leaves = inner M-elements) ----------------
def ocanon(sig, t):
    if t[0] == 'OL':
        return t
    i, kids = t[1], t[2]
    ck = tuple(ocanon(sig, c) for c in kids)
    g = sig.sym(i)
    if len(ck) <= 1 or len(g) == 1:
        return ('O', i, ck)
    best = min(tuple(ck[gg[j]] for j in range(len(ck))) for gg in g)
    return ('O', i, best)

def orelabel(sig, t, m):
    if t[0] == 'OL':
        return ('OL', L.relabel(sig, t[1], m))
    i, kids = t[1], t[2]
    return ocanon(sig, ('O', i, tuple(orelabel(sig, c, m) for c in kids)))

def ocontent(t):
    if t[0] == 'OL':
        return L.content(t[1])
    out = []
    for c in t[2]:
        out += ocontent(c)
    return out

def _ocount(t):
    if t[0] == 'OL':
        return 0
    return 1 + sum(_ocount(c) for c in t[2])

def gen_outer(sig, atoms, pad_out, max_nodes_out):
    """all canonical outer trees using each atom (a list, dups allowed) once as a leaf,
       plus 0..pad_out outer constants, <= max_nodes_out outer op-nodes."""
    const_ops = [i for i in range(len(sig.ops)) if sig.arity(i) == 0]
    memo = {}
    def build(atom_idx, nc, nodes_left):
        # atom_idx: tuple of atom indices to place (each once); nc outer-constants
        key = (atom_idx, nc, nodes_left)
        if key in memo:
            return memo[key]
        res = set()
        if len(atom_idx) == 1 and nc == 0:
            res.add(('OL', atoms[atom_idx[0]]))
        if len(atom_idx) == 0 and nc == 1 and nodes_left >= 1:
            for ci in const_ops:
                res.add(('O', ci, ()))
        if nodes_left >= 1 and (len(atom_idx) + nc) >= 1:
            for oi, (ar, g) in enumerate(sig.ops):
                if ar < 1:
                    continue
                for a_assign in _distribute(atom_idx, ar):
                    for c_assign in _comps(nc, ar):
                        child_opts = []
                        ok = True
                        for j in range(ar):
                            aj = a_assign[j]; cj = c_assign[j]
                            if len(aj) == 0 and cj == 0:
                                ok = False; break
                            opts = build(aj, cj, nodes_left - 1)
                            if not opts:
                                ok = False; break
                            child_opts.append(list(opts))
                        if not ok:
                            continue
                        for combo in product(*child_opts):
                            cand = ('O', oi, combo)
                            if _ocount(cand) <= nodes_left:
                                res.add(ocanon(sig, cand))
        memo[key] = res
        return res
    out = set()
    idx = tuple(range(len(atoms)))
    for p in range(pad_out + 1):
        out |= build(idx, p, max_nodes_out)
    return out

def _distribute(items, k):
    items = list(items)
    n = len(items)
    if k == 1:
        yield (tuple(items),); return
    for assign in product(range(k), repeat=n):
        yield tuple(tuple(items[i] for i in range(n) if assign[i] == j) for j in range(k))

def _comps(nc, k):
    if k == 1:
        yield (nc,); return
    for first in range(nc + 1):
        for rest in _comps(nc - first, k - 1):
            yield (first,) + rest

def ostab(sig, t, n):
    G = []
    for p in permutations(range(n)):
        m = dict(zip(range(n), p))
        if orelabel(sig, t, m) == t:
            G.append(p)
    return frozenset(G)

# ---------------- set partitions ----------------
def set_partitions(elts):
    elts = list(elts)
    if not elts:
        yield []; return
    first, rest = elts[0], elts[1:]
    for sm in set_partitions(rest):
        for i in range(len(sm)):
            yield sm[:i] + [sm[i] + [first]] + sm[i+1:]
        yield sm + [[first]]

# ---------------- P_M[m] : block-fixing products ----------------
def group_product(subgroups, n):
    res = {tuple(range(n))}
    for S in subgroups:
        nr = set()
        for x in res:
            for y in S:
                nr.add(L.compose(x, y))
        res = nr
    return frozenset(res)

def P_M(sig, m, pad_inner, max_nodes_inner):
    """conj-classes of block-fixing products of single-M-element stabilizers on [m]."""
    classes = set()
    for part in set_partitions(range(m)):
        block_choices = []
        ok = True
        for blk in part:
            trees = L.gen_trees(sig, blk, pad_inner, max_nodes_inner)
            if not trees:
                ok = False; break
            # stab of each tree as subgroup of S_m (acting within blk, fixing rest)
            subs = []
            for t in trees:
                G = []
                for p in permutations(blk):
                    mp = dict(zip(blk, p))
                    if L.relabel(sig, t, mp) == t:
                        full = tuple(mp.get(i, i) for i in range(m))
                        G.append(full)
                subs.append(frozenset(G))
            block_choices.append(subs)
        if not ok:
            continue
        for combo in product(*block_choices):
            H = group_product(combo, m)
            classes.add(L.canon_conj(H, m))
    return classes

# ---------------- (M o M)[m] enumeration + escape test ----------------
def search(sig, m, pad_inner=1, max_nodes_inner=4, pad_out=2, max_nodes_out=4,
           peg_max=2, verbose=True):
    t0 = time.time()
    PM = P_M(sig, m, pad_inner, max_nodes_inner)
    # precompute content-free "peg" inner elements (built from constants+ops, no labels)
    pegs = list(L.gen_trees(sig, [], peg_max, max_nodes_inner)) if sig.a0 > 0 else []
    # dedupe pegs
    pegs = list(dict.fromkeys(pegs))
    n_struct = 0
    escapes = []
    seen_stab = set()
    for part in set_partitions(range(m)):
        # inner tree choice per block
        block_choices = [list(L.gen_trees(sig, blk, pad_inner, max_nodes_inner)) for blk in part]
        if any(len(bc) == 0 for bc in block_choices):
            continue
        for combo in product(*block_choices):
            real_atoms = list(combo)
            for npeg in range(peg_max + 1):
                for peg_combo in _peg_multisets(pegs, npeg):
                    atoms = real_atoms + list(peg_combo)
                    if len(atoms) == 0:
                        continue
                    for o in gen_outer(sig, atoms, pad_out, max_nodes_out):
                        # verify content each-once
                        cont = sorted(ocontent(o))
                        if cont != list(range(m)):
                            continue
                        n_struct += 1
                        H = ostab(sig, o, m)
                        ck = L.canon_conj(H, m)
                        if ck in seen_stab:
                            continue
                        seen_stab.add(ck)
                        if ck not in PM:
                            escapes.append((o, H))
        if escapes and not verbose:
            break
    dt = time.time() - t0
    return {'PM': PM, 'n_struct': n_struct, 'escapes': escapes,
            'seen_stab': seen_stab, 'time': dt, 'pegs': len(pegs)}

def _peg_multisets(pegs, npeg):
    if npeg == 0:
        yield (); return
    # multisets of size npeg from pegs
    for combo in combinations_with_replacement_idx(len(pegs), npeg):
        yield tuple(pegs[i] for i in combo)

def combinations_with_replacement_idx(n, k):
    from itertools import combinations_with_replacement
    return combinations_with_replacement(range(n), k)

# ---------------- describe a group ----------------
def describe(H, n):
    order = len(H)
    facs = L.indecomposable_factors(H, n)
    fac_desc = [(d, len(dict.fromkeys(f))) for (d, f) in facs]  # (degree, order-of-factor)
    facs2 = []
    for (d, f) in facs:
        facs2.append((d, len(f)))
    return order, facs2

# =====================================================================
# SIGNATURES to test  (perm tuples: new[j]=children[g[j]])
# =====================================================================
def S2(): return [(0,1),(1,0)]
def triv2(): return [(0,1)]
def C3(): return [(0,1,2),(1,2,0),(2,0,1)]
def S3():
    return [p for p in permutations(range(3))]
def triv3(): return [(0,1,2)]

CONST = (0, [()])  # arity-0 op, trivial group (represented with one "empty perm")

SIGS = {
  'M_cb  (const + binary COMMUTATIVE)':        Sig('M_cb',  [CONST, (2, S2())]),
  'M_ncb (const + binary noncommutative)':     Sig('M_ncb', [CONST, (2, triv2())]),
  'M_c3  (const + ternary C_3)':               Sig('M_c3',  [CONST, (3, C3())]),
  'M_s3  (const + ternary S_3)':               Sig('M_s3',  [CONST, (3, S3())]),
  'M_cb_s3 (const + bin-comm + ternary S_3)':  Sig('M_cb_s3',[CONST, (2, S2()), (3, S3())]),
  'M_2c_cb (2 consts + binary comm)':          Sig('M_2c',  [CONST, CONST, (2, S2())]),
}

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    mmax = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    for label, sig in SIGS.items():
        if which != 'all' and which not in label:
            continue
        print('='*70)
        print(label, '   a_0 =', sig.a0, '  non-flat:', sig.nonflat)
        for m in range(2, mmax + 1):
            try:
                r = search(sig, m, verbose=True)
            except Exception as e:
                print(f"  m={m}: ERROR {e}")
                continue
            esc = r['escapes']
            print(f"  m={m}: |P_M|={len(r['PM'])}  MoM-structs={r['n_struct']}  "
                  f"distinct-stabs={len(r['seen_stab'])}  pegs={r['pegs']}  "
                  f"escapes={len(esc)}  [{r['time']:.1f}s]")
            if esc:
                o, H = esc[0]
                order, facs = describe(H, m)
                print(f"       ESCAPE witness stab order={order}, indecomp factors (deg,order)={facs}")
                print(f"       H = {sorted(H)}")
