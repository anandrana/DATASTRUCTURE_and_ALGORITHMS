from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph=defaultdict(list)
        
    def edgeList(self,v,u):
        self.graph[v].append(u)
    
    def UtilDfs(self,src,vis):
        vis[src]=True 
        
        print(src,end=",")
        
        for i in self.graph[src]:
            if vis[i]==False:
                vis[i]=True
                self.UtilDfs(i,vis)
    
    def Dfs(self,x):
        
        
        v=len(self.graph)

        visited=[False]*(V+1) 
        self.UtilDfs(x,visited)
        
               
e,V=map(int,input().split())

g=Graph()
for i in range(e):
    v1,v2=map(int,input().split())
    if(i==0):
        x=v1 
    g.edgeList(v1,v2)
g.Dfs(x)
