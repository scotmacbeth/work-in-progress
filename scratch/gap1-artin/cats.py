from presheaf import *

def mkcat(objs, arrows, comps):
    comp={}
    for o in objs: 
        pass
    # identities
    A=dict(arrows)
    for o in objs: A['id_'+o]=(o,o)
    for n,(d,c) in A.items():
        comp[('id_'+c,n)]=n; comp[(n,'id_'+d)]=n
    comp.update(comps)
    return Cat(objs,A,comp)

SET   = mkcat(['*'],{},{})
SIERP = mkcat(['0','1'],{'u':('0','1')},{})          # u:0->1, no nontrivial composites
GRAPH = mkcat(['V','E'],{'s':('V','E'),'t':('V','E')},{})
def Zn(n):
    objs=['*']; arrows={('g%d'%i):('*','*') for i in range(1,n)}
    comp={}
    names={0:'id_*'}; names.update({i:'g%d'%i for i in range(1,n)})
    for i in range(n):
        for j in range(n):
            comp[(names[i],names[j])]=names[(i+j)%n]
    return Cat(objs,{**arrows,'id_*':('*','*')},comp)
Z2=Zn(2)
