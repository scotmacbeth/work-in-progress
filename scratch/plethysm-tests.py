from plethysm_stab import *

def run_case(name, A, x_sizes):
    print("="*70)
    print(f"CASE: {name}   flat={A.is_flat()}   constituents={[(n,len(H)) for n,H in A.constituents]}")
    for x in x_sizes:
        Sa, _, _ = stabilizers_on_X(A, x)
        clo = intersection_closure(Sa, x)
        Saa, Zel, stab_of = evaluate_composite(A, x)
        new = [S for S in Saa if S not in clo]
        print(f"  X=range({x}): |~A(X)| stabs={len(Sa)}  |A.A stabs|={len(Saa)}  "
              f"NEW-stabs(not in intersection-closure of S(~A))={len(new)}")
        for S in sorted(new, key=lambda g:-len(g)):
            print(f"        NEW: {describe_group(S, x)}")
        if not new and A.is_flat()==False:
            print("        (no separating stabilizer at this X)")
    print()

if __name__=="__main__":
    S2 = [(1,0)]      # transposition in S_2
    C3 = [(1,2,0)]    # 3-cycle in S_3
    S3full = [(1,0,2),(1,2,0)]

    # sanity: flat species should NEVER have a new stabilizer (A.A itself = R.A trivially)
    run_case("A = X (identity, flat)", Species([(1,[])]), [2,3,4])
    run_case("A = X + X^2 (flat, has degree-2 free)", Species([(1,[]),(2,[])]), [3,4])

    # guiding example: E_2 (2-element sets), non-flat, expect D_4 wreath at X=4
    run_case("A = E_2 = X^2/S_2 (non-flat)", Species([(2,S2)]), [3,4])

    # minimal non-flat with a unit slot
    run_case("A = X + E_2 (non-flat)", Species([(1,[]),(2,S2)]), [3,4])

    # cyclic species C_3 = X^3/C_3 (non-flat, H=C_3 not S_3): the 'directed triangle'
    run_case("A = X^3/C_3 (non-flat, cyclic)", Species([(3,C3)]), [3])
