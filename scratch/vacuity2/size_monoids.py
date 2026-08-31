# Size-level constraints (Task 2 framing).
#
# In ANY monoidal structure ⋆ on Set, |A⋆B| depends only on |A|,|B| (functoriality
# under bijections), the associator iso forces the size operation s(m,n)=|m⋆n| to be
# ASSOCIATIVE, and the unit object I (|I|=u) forces u to be a two-sided IDENTITY.
# So sizes form a monoid.  For the skeleton {∅,1,2,3} closed under ⋆ we need
# s:{0,1,2,3}^2 -> {0,1,2,3}.  Enumerate ALL such monoids and read off the possible
# unit cardinalities.  (Genuine monoidal realizability is stronger; this is necessary.)
import itertools

vals=[0,1,2,3]
def is_assoc(s):
    for a in vals:
        for b in vals:
            for c in vals:
                if s[(s[(a,b)],c)] != s[(a,s[(b,c)])]:
                    return False
    return True
def identities(s):
    ids=[]
    for u in vals:
        if all(s[(u,x)]==x and s[(x,u)]==x for x in vals):
            ids.append(u)
    return ids

# Enumerate all closed binary ops on {0,1,2,3}: 4^16 ~ 4.3e9 -> too many.
# Prune: require a two-sided identity u.  Fix u, then s(u,x)=s(x,u)=x is forced,
# leaving the 3x3 block on {vals}\{u} free = 4^9 ~ 262144 per u.  Feasible.
census={}
unit_geq2=[]
total=0
for u in [0,1,2]:              # unit cardinality candidates (prompt: I in {∅,1,2})
    others=[x for x in vals if x!=u]
    # unknown cells: (a,b) for a,b in others  -> 9 cells, values in vals
    cells=[(a,b) for a in others for b in others]
    cnt=0
    for assign in itertools.product(vals, repeat=len(cells)):
        s={}
        for x in vals:
            s[(u,x)]=x; s[(x,u)]=x
        for k,v in zip(cells,assign):
            s[k]=v
        if is_assoc(s):
            ids=identities(s)
            # record with u as (a) identity; may have more than one only if trivial
            cnt+=1
            total+=1
            if any(i>=2 for i in ids):
                unit_geq2.append((u,tuple(sorted(ids)),tuple(sorted(s.items()))))
    census[u]=cnt
    print(f"unit cardinality u={u}: {cnt} associative unital tables on {{0,1,2,3}}")

print(f"TOTAL monoid tables (by declared unit u in {{0,1,2}}): {total}")
print()
# Which have an identity element of cardinality >=2?
print(f"Tables possessing an identity of cardinality >=2: {len(unit_geq2)}")
# Characterize them: an identity >=2 means s(2,x)=x for all x (and/or 3).
# Show a few and check what element 0 and 1 do (0 must satisfy s(2,0)=0 -> fine).
seen=set()
examples=[]
for u,ids,tbl in unit_geq2:
    key=(ids)
    if key in seen: continue
    seen.add(key)
    examples.append((u,ids,dict(tbl)))
print("distinct identity-sets with an element >=2:", sorted(seen))
for u,ids,s in examples[:8]:
    grid="\n".join("   "+" ".join(str(s[(a,b)]) for b in vals) for a in vals)
    print(f"  declared u={u}, identities={ids}:\n{grid}")

# NOTE: an identity of cardinality>=2 at SIZE level does NOT yet give a monoidal
# category; the associator must be realized naturally.  The genuine-realization
# search (bifunctor+pentagon) is size_search.py.  Here we only learn which unit
# cardinalities are size-consistent.
