from plethysm_stab import *

def group_desc(G, x_size):
    order=len(G)
    Ys=young_subgroups(x_size)
    young = any(G==Y for Y in Ys.values())
    inside_young = any(G <= Y for Y in Ys.values())
    def cyc_type(p):
        seen=[False]*len(p); t=[]
        for i in range(len(p)):
            if not seen[i]:
                l=0; j=i
                while not seen[j]:
                    seen[j]=True; j=p[j]; l+=1
                if l>1: t.append(l)
        return tuple(sorted(t))
    types=sorted(set(cyc_type(p) for p in G))
    return f"order={order} young={young} inside_young={inside_young} cycletypes={types}"

def report(name, A, x, show=False):
    Sa,_,_ = stabilizers_on_X(A,x)
    clo = intersection_closure(Sa,x)
    Saa,Zel,stab_of = evaluate_composite(A,x)
    new=[S for S in Saa if S not in clo]
    print(f"[{name}] X={x} flat={A.is_flat()} |S(~A)|={len(Sa)} |closure|={len(clo)} "
          f"|S(A.A)|={len(Saa)} NEW={len(new)}", flush=True)
    for S in sorted(new,key=lambda g:-len(g)):
        print("     NEW", group_desc(S,x), flush=True)
        if show:
            print("        subgroup elements:", sorted(S), flush=True)
    return len(new)

if __name__=="__main__":
    S2=[(1,0)]
    D4=[(1,0,2,3),(0,1,3,2),(2,3,0,1)]  # S_2 wr S_2 on {0,1|2,3}

    print("### robustness: E_2 across X=4,5 ###", flush=True)
    for x in [4,5]:
        report("E_2", Species([(2,S2)]), x)

    print("\n### concrete D_4 witness at X=4 ###", flush=True)
    report("E_2", Species([(2,S2)]), 4, show=True)

    print("\n### ESCAPE probe: A = E_2 + M_{D_4} (A already CONTAINS the wreath group) ###", flush=True)
    for x in [4,5]:
        report("E_2+M_D4", Species([(2,S2),(4,D4)]), x)
