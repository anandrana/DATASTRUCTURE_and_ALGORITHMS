"""
This is hamiltonian path , this is find the path that is each vertices travels only once if the path is exits the we say that 
hamiltonian cycle is present otherwise not present , it is backtracking concept
"""

from collections import defaultdict


def hamPath(g,i,v,res):
    v[i] = True
    
    if all(v):
        
        #print(v)
        print(res)
        
        return True
    for j in g[i]:
        #print(g[i])
        # print(j,end=" ")
        if v[j]==False:
            res.append(j)
            
            if hamPath(g,j,v,res):
                return True
    v[i] = False
    return False

for _ in range(int(input())):
    n,m = map(int,input().split())
    edges = list(map(int,input().split()))
    g = defaultdict(set)
    for i in range(0,2*m,2):
        g[edges[i]].add(edges[i+1])
        
        
        g[edges[i+1]].add(edges[i])
    
    #print(g)    
    v = [True]+[False]*n
    #print(v)
    
    for i in range(1,n+1):
        if hamPath(g,i,v,[]):
            print(1)
            break
    else:
        print(0)
        
        
        
